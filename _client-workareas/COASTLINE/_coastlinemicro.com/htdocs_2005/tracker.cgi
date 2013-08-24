#!/usr/bin/perl5 -s

  use LWP::Simple;
  use CGI;
  use CGI::Carp qw(fatalsToBrowser);
  use Text::CSV_XS;
  use Business::UPS;
  
  my $q = new CGI;
  my $fedex_url = "http://www.fedex.com/cgi-bin/tracking?action=track&initial=x";
  my $language="english";
  my $country_code = "us";
  my $order_num = $q->param('order_num');
  my $csv_file = "/usr/local/www/vhosts/usnightvision.com/htdocs/tracking/tracker.csv";
  my $return_code,$message,$date,$time,$note;
  
  print $q->header;
  print qq(<html><body>);
  
  if ($order_num) {
  	my ($track_type,$track_num) = &get_tracking_num($order_num);
  	if (!$track_num) {
  		print qq(Invalid order number<BR>);
  	} else {
  		if ($track_type eq 'fedex') {
  			($return_code,$message,$date,$time,$note) = &parse_fedex_html($track_num);
  		} elsif ($track_type eq 'ups') {
  			($return_code,$message,$note) = &parse_ups_data($track_num);
  		}
  	
  		if ($return_code == 0) {
  			print qq(Invalid tracking number<BR>);
  		} else {
  			print "Last updated: $date, $time<BR>" if $date && $time;
  			print "Package was last scanned in: $message $note\n";
  		}
  	}
  }
  
  &print_form;
  print qq(</body></html>);
  
  sub get_tracking_num {
  	my $order_num = shift;
  	open(CSV,$csv_file) || die "Cannot open $csv_file for read: $!";
  	my $csv = new Text::CSV_XS;	
  	
  	while (<CSV>) {
  		$csv->parse($_);
  		my ($order,$fedex,$ups) = $csv->fields;
  		if ($order eq $order_num) {
  			if ($fedex) {
  				return "fedex",$fedex;
  			} else {
  				return "ups",$ups;	
  			}
  		}
  	}
  	return 0;
  }
  
  sub parse_fedex_html {
  	my $track_num = shift;
  	my $url = $fedex_url . "&language=$language&cntry_code=$country_code&tracknumbers=$track_num";
  	my $page = get ($url);
  
  	return 0,0 if $page =~ /Invalid/i;
  
  	my $record;
  
  	$page =~ m|CLASS="resultstableheader".*?</tr>(.*?)</table>|gis;
  	my $results = $1;
  
  	$col_match = "<td.*?>(.*?)</td>";
  	$record_match = ".*?$col_match.*?$col_match.*?$col_match";
  
  	$results =~ m|<tr.*?>(.*?)</tr>|gis;
  	my $record = $1;
  	
  	$record =~ s/&nbsp;/ /g;
  	$record =~ m|$record_match|gis;
  	my $message = $1;
  	my $datetime = $2;
  	my $note = $3;
  	
  	$datetime =~ m|(\d\d/\d\d/\d\d\d\d)\s+(\d\d:\d\d)|;
  	my $date = $1;
  	my $time = $2;
  	
  	return 1,$message,$date,$time,$note;
  }
  
  sub parse_ups_data {
  	my $track_num = shift;
  	%track = UPStrack($track_num);
  	return 0 if $track{'error'};
  	
  	my $message = $track{'Last Scanned at'};
  	my $note;
  	
  	return 1,$message,$note;
  }
  
  sub print_form {
  	print qq(
  <form action="tracker.cgi" method="get">
  Please enter your order number: <input name="order_num" value="$order_num"><input type="submit">
  </form>);	
  }
