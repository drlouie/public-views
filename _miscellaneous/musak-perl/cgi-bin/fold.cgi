#!D:/Perl/bin/perl.exe

## view all music inside music folders

use CGI ':standard';
print "Content-type: text/html\n\n";

$whichDir = param('fold');

## Define all folders/files within Pollstuff. Then uncall the files and name the folders.
## This will come up with list of names of all available polls
	my $aDir = "D:/mds/$whichDir";
	opendir(FILE, $aDir) or die "can't opendir $aDir $!";
	while (defined($file = readdir(FILE))) {
		next if $file =~ /^\.\.?$/; ## skip . and .. directories
		next if $file =~ /.txt\.?$/; ## skip .txt files
		next if $file =~ /.htaccess\.?$/; ## skip .htaccess files
		next if $file =~ /.htpasswd\.?$/; ## skip .htpasswd files
		$file =~ s/ /%20/gi;
		$whichDir =~ s/ /%20/gi;
		if ($file =~ ".mp3" || $file =~ ".wsx") {
			print "http://192.168.1.100/$whichDir/$file<br>";
		}
		else {
			print "http://192.168.1.100/cgi-bin/fold.cgi?fold=$whichDir/$file<br>";
		}
	}

exit;