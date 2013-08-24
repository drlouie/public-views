#!/usr/bin/perl5 -s

###########################################################################################################
# Company: ©2001 NetMedia Solutions                                                                       #
# Date: Saturday, September 21, 2001                                                                      #
# Location: Los Angeles County, California, United States of America                                      #
# Made By: Luis Rodriguez (drlouie)                                                                       #
# Email: Drlouie@NetMediaSol.com                                                                          #
#                                                                                                         #
# This program cannot be duplicated, distributed or re-used for any other purpose other than its original #
# intended purpose and function. You may request NetMedia Solutions for a copy of the script,             #
# personalized to fit your exact needs for a small re-programming fee.                                    #
###########################################################################################################

$mailprog = '/usr/sbin/sendmail';

## common dhtml stuff
require ("referer.nsp"); 
require ("date.nsp");
$legal = `cat legal.nsf`;
$pow = `cat pow_products.nsf`;
## must have command to run search
$powbutton = "";	

## sitemailer stuff
&check_url;
&get_date;
&parse_form;
&check_required;
&return_html;
&send_mail;

sub check_url {

    # Localize the check_referer flag which determines if user is valid.     #
    local($check_referer) = 0;

    # If a referring URL was specified, for each valid referer, make sure    #
    # that a valid referring URL was passed to FormMail.                     #

    if ($ENV{'HTTP_REFERER'}) {
        foreach $referer (@referers) {
            if ($ENV{'HTTP_REFERER'} =~ m|https?://([^/]*)$referer|i) {
                $check_referer = 1;
                last;
            }
        }
    }
    else {
        $check_referer = 1;
    }

    # If the HTTP_REFERER was invalid, send back an error.                   #
    if ($check_referer != 1) { &error('bad_referer') }
}

sub get_date {

    # Define arrays for the day of the week and month of the year.           #
    @days   = ('Sunday','Monday','Tuesday','Wednesday',
               'Thursday','Friday','Saturday');
    @months = ('January','February','March','April','May','June','July',
	         'August','September','October','November','December');

    # Get the current time and format the hour, minutes and seconds.  Add    #
    # 1900 to the year to get the full 4 digit year.                         #
    ($sec,$min,$hour,$mday,$mon,$year,$wday) = (localtime(time))[0,1,2,3,4,5,6];
    $time = sprintf("%02d:%02d:%02d",$hour,$min,$sec);
    $year += 1900;

    # Format the date.                                                       #
    $date = "$days[$wday], $months[$mon] $mday, $year";

}

sub parse_form {

    # Define the configuration associative array.                            #
    %Config = ('recipient','',          'subject','',
               'email','',              'realname','',
               'redirect','',           'bgcolor','',
               'background','',         'link_color','',
               'vlink_color','',        'text_color','',
               'alink_color','',        'title','',
               'sort','',               'print_config','',
               'required','',           'env_report','',
               'return_link_title','',  'return_link_url','',
               'print_blank_fields','', 'missing_fields_redirect','');

    # Determine the form's REQUEST_METHOD (GET or POST) and split the form   #
    # fields up into their name-value pairs.  If the REQUEST_METHOD was      #
    # not GET or POST, send an error.                                        #
    if ($ENV{'REQUEST_METHOD'} eq 'GET') {
        # Split the name-value pairs
        @pairs = split(/&/, $ENV{'QUERY_STRING'});
    }
    elsif ($ENV{'REQUEST_METHOD'} eq 'POST') {
        # Get the input
        read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
 
        # Split the name-value pairs
        @pairs = split(/&/, $buffer);
    }
    else {
        &error('request_method');
    }

    # For each name-value pair:                                              #
    foreach $pair (@pairs) {

        # Split the pair up into individual variables.                       #
        local($name, $value) = split(/=/, $pair);
 
        # Decode the form encoding on the name and value variables.          #
        $name =~ tr/+/ /;
        $name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

        $value =~ tr/+/ /;
        $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

        # If they try to include server side includes, erase them, so they
        # aren't a security risk if the html gets returned.  Another 
        # security hole plugged up.
        $value =~ s/<!--(.|\n)*-->//g;

        # If the field name has been specified in the %Config array, it will #
        # return a 1 for defined($Config{$name}}) and we should associate    #
        # this value with the appropriate configuration variable.  If this   #
        # is not a configuration form field, put it into the associative     #
        # array %Form, appending the value with a ', ' if there is already a #
        # value present.  We also save the order of the form fields in the   #
        # @Field_Order array so we can use this order for the generic sort.  #
        if (defined($Config{$name})) {
            $Config{$name} = $value;
        }
        else {
            if ($Form{$name} && $value) {
                $Form{$name} = "$Form{$name}, $value";
            }
            elsif ($value) {
                push(@Field_Order,$name);
                $Form{$name} = $value;
            }
        }
    }

    # The next six lines remove any extra spaces or new lines from the       #
    # configuration variables, which may have been caused if your editor     #
    # wraps lines after a certain length or if you used spaces between field #
    # names or environment variables.                                        #
    $Config{'required'} =~ s/(\s+|\n)?,(\s+|\n)?/,/g;
    $Config{'required'} =~ s/(\s+)?\n+(\s+)?//g;
    $Config{'env_report'} =~ s/(\s+|\n)?,(\s+|\n)?/,/g;
    $Config{'env_report'} =~ s/(\s+)?\n+(\s+)?//g;
    $Config{'print_config'} =~ s/(\s+|\n)?,(\s+|\n)?/,/g;
    $Config{'print_config'} =~ s/(\s+)?\n+(\s+)?//g;

    # Split the configuration variables into individual field names.         #
    @Required = split(/,/,$Config{'required'});
    @Env_Report = split(/,/,$Config{'env_report'});
    @Print_Config = split(/,/,$Config{'print_config'});
}

sub check_required {

    # Localize the variables used in this subroutine.                        #
    local($require, @error);

    if (!$Config{'recipient'}) {
        if (!defined(%Form)) { &error('bad_referer') }
        else                 { &error('no_recipient') }
    }

    # For each require field defined in the form:                            #
    foreach $require (@Required) {

        # If the required field is the email field, the syntax of the email  #
        # address if checked to make sure it passes a valid syntax.          #
        if ($require eq 'email' && !&check_email($Config{$require})) {
            push(@error,$require);
        }

        # Otherwise, if the required field is a configuration field and it   #
        # has no value or has been filled in with a space, send an error.    #
        elsif (defined($Config{$require})) {
            if (!$Config{$require}) {
                push(@error,$require);
            }
        }

        # If it is a regular form field which has not been filled in or      #
        # filled in with a space, flag it as an error field.                 #
        elsif (!$Form{$require}) {
            push(@error,$require);
        }
    }

    # If any error fields have been found, send error message to the user.   #
    if (@error) { &error('missing_fields', @error) }
}

sub return_html {
    # Local variables used in this subroutine initialized.                   #
    local($key,$sort_order,$sorted_field);

    #CHECK SUBJECT TO CEHCK THE NEXT HTTP FEEDBACK FOR THE USER. IF CREDIT APP, REDIRECT USER TO DOWNLOAD PAGE ELSE PRINT DEFAULT HTML FEEDBACK#
    if ($Config{'subject'} eq 'Online_Credit_Application') {
        print "Location: contact.html?title=creditfilled\n\n";
    }
    # Otherwise, begin printing the response page.                           #
    else {

	if ($Config{'subject'} eq 'Store_Access_Request') {
	$text = "Thank you for requesting an on-line account. Your account number and password will be issued to you within one business day. If you are a new customer, a dedicated Coastline Micro account representative will be assigned to your account. They will work with you directly on all orders. They will confirm product allocation, special configuration requests, and delivery dates.";	
	}
	
	else {
	$text = "Thanks for taking the time to write to us. We safeguard all our gathered information from the public eye for your valuable privacy.";	
	}

print "Content-type: text/html\n\n";

{
print <<EOF

<html>
<head>
<title>Company Name</title>
<SCRIPT LANGUAGE="JavaScript">

///////////////////////////////////////////////////////////////////
// This script and its counterparts are ©2001 NetMedia Solutions //
// For use ONLY with CoastlineMicro.com                          //
// To re-use or have this script re-interfaced for your specific //
// needs please contact SServices\@NetMediaSolutions.com         //
// Prices are cheap for re-interfacing of current scripts and    //
// programs, so email us today to get you own LEGAL programming  //
// licensed for use only on YOUR site(s) or for YOUR purpose(s). //
///////////////////////////////////////////////////////////////////

<!-- Begin
function loadScript() {
if (document.getElementById) {  // DOM3 = IE5, NS6
document.getElementById('hidepage').style.visibility = 'hidden';
}
else {
if (document.layers) {  // Netscape 4
document.hidepage.visibility = 'hidden';
}
else {  // IE 4
document.all.hidepage.style.visibility = 'hidden';
      }
   }
}
//  End -->
</script>
<style type="text/css">
#hidepage {z-index:2000}
body { scrollbar-face-color:#F2F2F7; scrollbar-highlight-color:#F2F2F7; scrollbar-shadow-color:#8f8fab; scrollbar-3dlight-color: #333366; scrollbar-arrow-color:#333366; scrollbar-track-color:#F2F2F7; scrollbar-darkshadow-color:#8f8fab; }
</style>
<div id="hidepage" style="position: absolute; left:0px; top:0px; background-color: #FFFFFF; layer-background-color: #FFFFFF; height: 100%; width: 100%;">
<table width=100% cellpadding="0" cellspacing="0">
<tr height="100%"><td align="center" valign="middle"><br><br><img src="sharktank/images/cm_logo_large.jpg" width="166" height="59" border="0"><font face="verdana,arial,helvetica" size="2" color="#333366"><br><br>Loading DHTML interactive user interface, please wait...<br><br><br><br><br><font size="1"><b><u>Compatibility</u></b><br><br>Win/Mac MSIE 4/5/6<br>Win/Mac/Linux Netscape 4/6<br><br><i>Best if viewed on Windows 95/98/2000 platform using MSIE 4+</i></font></font></td></tr>
</table>
</div> 
<script language="JavaScript" src="js/reload.js"></script>

<!--FOLLOWING EXTERNAL SCRIPT IS USED FOR BROWSER TESTING AND IS INTEGRAL PART OF POW-->
<script language="JavaScript" src="js/dynlayer.js"></script>
<!--END-->

<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta name="keywords" content="coastlinemicro.com, www.coastlinemicro.com, coastline, micro, irvine, ca, california, about, company, location, businsess, competition, competitors, solutions, irvine, california, technology, ceo, own, partner, fast, reliable, heritage, sophisticated, computer, system, build, custom, sample, guarantee, search, product">
<meta name="description" content="Coastline Micro Inc. is in business to develop hardware solutions that make sense for the small to corporate sized business arena. We have been in business for over a decade and have the knowledge and expertise necessary to be competitive in the market. Our every product carries a 100% Product Satisfaction Guarantee. We are located in Irvine, California at 60 N. Technology Drive. For more information about our company and its what it is in business to do please follow the link above. Our company's Heritage dates back to 1989.">
<script language="JavaScript" src="js/menu_config.js"></script>
<LINK REL="STYLESHEET" HREF="common_css.html" Type="text/css">

</head>
<body bgcolor="#ffffff" text="#333366" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onLoad="javascript:loadScript();runSearch();">

<!-- Copyright NetMedia Solutions and Coasltine Micro, Inc.-->
<script language="Javascript" src="js/menu_constructor.js"></script>

<!-- Start header table -->
<table width="100%" border="0" cellspacing="0" cellpadding="0" background="images/newones/top_tablebg_main.jpg" height="100">
  <tr> 
    <td width="30%"><img src="images/newones/illus_contact.jpg" width="250" height="100" border="0"></td>
    <td align="right" valign="middle" width="70%"><font size="1" color="#ffffff" face="verdana,arial,helvetica">$date&nbsp;&nbsp;<font size="3">&nbsp;</font></font>
	<center><img src="images/newones/title_contact.jpg" width="350" height="80" align="bottom"></center></td>
  </tr>
</table>
<!-- End header table -->

<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td width="175" align=left valign=top><img src="images/newmenu/place_holder.gif" width="175" height="150"><img src="images/spacer.gif" width="190" height="20" border="0">$powbutton $legal</td>
    <td width="5"><img src="images/140spacer.gif" width="5" height="8"></td>
    <td width="100%" align="center" valign=top><br>
<table width="90%" border="0" cellspacing="0" cellpadding="0" align="center">
  <tr> 
    <td> 
      <table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td width="12" height="24"><img src="images/table_top_left.gif" border=0 width="12" height="24"></td>
          <td bgcolor="#333366" align="center" width="50%">&nbsp;</td>
          <td align="center" width="30" height="24"><img src="images/table_top_mid.gif" border=0 width="30" height="24"></td>
          <td bgcolor="#8f8fab" align="center" width="50%"><b><font class=tableheading>Coastline 
            Micro Emailer</font></b></td>
          <td align="right" height="24" width="12"><img src="images/table_top_right.gif" border=0 width="12" height="24"></td>
        </tr>
      </table>
    </td>
  </tr>
  <tr bgcolor="#333366" align="center"> 
    <td> <br>
      <table width=95% border=0 cellspacing=0 cellpadding=0 align=center>
        <tr> 
          <td width=10>&nbsp;</td>
          <td colspan=3 align=left valign=top> 
            <table border=0 cellspacing=0 cellpadding=0 align=left height=25>
              <tr> 
                                  <td width="65"><font class="regtextbold"><b>Phone</b></font></td>
                                  <td width="200"><font  class="regtextnobold">(800) 729-6809</font></td>
                                </tr>
                                <tr> 
                                  <td width="65"><font class="regtextbold"><b>Fax</b></font></td>
                                  <td width="200"><font class="regtextnobold">(949) 450-9977</font></td>
              </tr>
              <tr> 
                <td width=65>&nbsp;</td>
                <td width=200>&nbsp;</td>
              </tr>
            </table>
          </td>
          <td>&nbsp;</td>
        </tr>
        <tr> 
          <td width=10>&nbsp;</td>
          <td colspan=3> 
            <p><font class=regtextnobold><b>Thank You!</b><br>
              $text<br>
              <br>
              Hope You enjoy the rest of our site! <br>
              </font></p>
          </td>
          <td width=10>&nbsp;</td>
        </tr>
      </table>
      <br>
    </td>
  </tr>
  <tr> 
    <td> 
      <table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td width="12" height="24"><img src="images/table_bot_left.gif" border=0 width="12" height="24"></td>
          <td bgcolor="#8f8fab" align="center" width="50%">&nbsp;</td>
          <td align="center" width="30" height="24"><img src="images/table_bot_mid.gif" border=0 width="30" height="24"></td>
          <td bgcolor="#333366" align="center" width="50%">&nbsp;</td>
          <td align="right" height="24" width="12"><img src="images/table_bot_right.gif" border=0 width="12" height="24"></td>
        </tr>
      </table>
    </td>
  </tr>
</table>
</td>
  </tr>
</table>

<!-- Dynamic Moving Layers -->
$pow
</body>
</html>

EOF
}
    }
}

sub send_mail {
    # Localize variables used in this subroutine.                            #
    local($print_config,$key,$sort_order,$sorted_field,$env_report);

    # Open The Mail Program
    open(MAIL,"|$mailprog -t");

print MAIL "To: mpnunez\@coastlinemicro.com\n";
#print MAIL "To: drhomberg\@coastline-mail.com\n";
#print MAIL "Cc: jtraficante\@coastline-mail.com,mpnunez\@coastline-mail.com\n";

$emailer = "(An Online User)";
print MAIL "From: $Config{'email'} $emailer\n";
print MAIL "Subject: $Config{'subject'}\n\n";

    print MAIL "-" x 75 . "\n\n";

    if (@Print_Config) {
        foreach $print_config (@Print_Config) {
            if ($Config{$print_config}) {
                print MAIL "$print_config: $Config{$print_config}\n\n";
            }
        }
    }

    # Sort alphabetically if specified:                                      #
    if ($Config{'sort'} eq 'alphabetic') {
        foreach $field (sort keys %Form) {

            # If the field has a value or the print blank fields option      #
            # is turned on, print out the form field and value.              #
            if ($Config{'print_blank_fields'} || $Form{$field} ||
                $Form{$field} eq '0') {
                print MAIL "$field: $Form{$field}\n\n";
            }
        }
    }

    # If a sort order is specified, sort the form fields based on that.      #
    elsif ($Config{'sort'} =~ /^order:.*,.*/) {

        # Remove extraneous line breaks and spaces, remove the order:        #
        # directive and split the sort fields into an array.                 #
        $Config{'sort'} =~ s/(\s+|\n)?,(\s+|\n)?/,/g;
        $Config{'sort'} =~ s/(\s+)?\n+(\s+)?//g;
        $Config{'sort'} =~ s/order://;
        @sorted_fields = split(/,/, $Config{'sort'});

        # For each sorted field, if it has a value or the print blank        #
        # fields option is turned on print the form field and value.         #
        foreach $sorted_field (@sorted_fields) {
            if ($Config{'print_blank_fields'} || $Form{$sorted_field} ||
                $Form{$sorted_field} eq '0') {
                print MAIL "$sorted_field: $Form{$sorted_field}\n\n";
            }
        }
    }

    # Otherwise, default to the order in which the fields were sent.         #
    else {

        # For each form field, if it has a value or the print blank          #
        # fields option is turned on print the form field and value.         #
        foreach $field (@Field_Order) {
            if ($Config{'print_blank_fields'} || $Form{$field} ||
                $Form{$field} eq '0') {
                print MAIL "$field: $Form{$field}\n\n";
            }
        }
    }

    print MAIL "-" x 75 . "\n\n";

    # Send any specified Environment Variables to recipient.                 #
    foreach $env_report (@Env_Report) {
        if ($ENV{$env_report}) {
            print MAIL "$env_report: $ENV{$env_report}\n";
        }
    }

    close (MAIL);
}

sub check_email {
    # Initialize local email variable with input to subroutine.              #
    $email = $_[0];

    # If the e-mail address contains:                                        #
    if ($email =~ /(@.*@)|(\.\.)|(@\.)|(\.@)|(^\.)/ ||

        # the e-mail address contains an invalid syntax.  Or, if the         #
        # syntax does not match the following regular expression pattern     #
        # it fails basic syntax verification.                                #

        $email !~ /^.+\@(\[?)[a-zA-Z0-9\-\.]+\.([a-zA-Z]{2,3}|[0-9]{1,3})(\]?)$/) {

        # Basic syntax requires:  one or more characters before the @ sign,  #
        # followed by an optional '[', then any number of letters, numbers,  #
        # dashes or periods (valid domain/IP characters) ending in a period  #
        # and then 2 or 3 letters (for domain suffixes) or 1 to 3 numbers    #
        # (for IP addresses).  An ending bracket is also allowed as it is    #
        # valid syntax to have an email address like: user@[255.255.255.0]   #

        # Return a false value, since the e-mail address did not pass valid  #
        # syntax.                                                            #
        return 0;
    }

    else {

        # Return a true value, e-mail verification passed.                   #
        return 1;
    }
}

sub body_attributes {
    # Check for Background Color
    if ($Config{'bgcolor'}) { print " bgcolor=\"$Config{'bgcolor'}\"" }

    # Check for Background Image
    if ($Config{'background'}) { print " background=\"$Config{'background'}\"" }

    # Check for Link Color
    if ($Config{'link_color'}) { print " link=\"$Config{'link_color'}\"" }

    # Check for Visited Link Color
    if ($Config{'vlink_color'}) { print " vlink=\"$Config{'vlink_color'}\"" }

    # Check for Active Link Color
    if ($Config{'alink_color'}) { print " alink=\"$Config{'alink_color'}\"" }

    # Check for Body Text Color
    if ($Config{'text_color'}) { print " text=\"$Config{'text_color'}\"" }
}

sub error { 
    # Localize variables and assign subroutine input.                        #
    local($error,@error_fields) = @_;
    local($host,$missing_field,$missing_field_list);

    if ($error eq 'bad_referer') {
        if ($ENV{'HTTP_REFERER'} =~ m|^https?://([\w\.]+)|i) {
            $host = $1;
			
            print <<"(END ERROR HTML)";
Content-type: text/html

<html>
<head>
<title>Company Name</title>
<SCRIPT LANGUAGE="JavaScript">

///////////////////////////////////////////////////////////////////
// This script and its counterparts are ©2001 NetMedia Solutions //
// For use ONLY with CoastlineMicro.com                          //
// To re-use or have this script re-interfaced for your specific //
// needs please contact SServices\@NetMediaSolutions.com         //
// Prices are cheap for re-interfacing of current scripts and    //
// programs, so email us today to get you own LEGAL programming  //
// licensed for use only on YOUR site(s) or for YOUR purpose(s). //
///////////////////////////////////////////////////////////////////

<!-- Begin
function loadScript() {
if (document.getElementById) {  // DOM3 = IE5, NS6
document.getElementById('hidepage').style.visibility = 'hidden';
}
else {
if (document.layers) {  // Netscape 4
document.hidepage.visibility = 'hidden';
}
else {  // IE 4
document.all.hidepage.style.visibility = 'hidden';
      }
   }
}
//  End -->
</script>
<style type="text/css">
#hidepage {z-index:2000}
body { scrollbar-face-color:#F2F2F7; scrollbar-highlight-color:#F2F2F7; scrollbar-shadow-color:#8f8fab; scrollbar-3dlight-color: #333366; scrollbar-arrow-color:#333366; scrollbar-track-color:#F2F2F7; scrollbar-darkshadow-color:#8f8fab; }
</style>
<div id="hidepage" style="position: absolute; left:0px; top:0px; background-color: #FFFFFF; layer-background-color: #FFFFFF; height: 100%; width: 100%;">
<table width=100% cellpadding="0" cellspacing="0">
<tr height="100%"><td align="center" valign="middle"><br><br><img src="sharktank/images/cm_logo_large.jpg" width="166" height="59" border="0"><font face="verdana,arial,helvetica" size="2" color="#333366"><br><br>Loading DHTML interactive user interface, please wait...<br><br><br><br><br><font size="1"><b><u>Compatibility</u></b><br><br>Win/Mac MSIE 4/5/6<br>Win/Mac/Linux Netscape 4/6<br><br><i>Best if viewed on Windows 95/98/2000 platform using MSIE 4+</i></font></font></td></tr>
</table>
</div> 
<script language="JavaScript" src="js/reload.js"></script>

<!--FOLLOWING EXTERNAL SCRIPT IS USED FOR BROWSER TESTING AND IS INTEGRAL PART OF POW-->
<script language="JavaScript" src="js/dynlayer.js"></script>
<!--END-->

<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta name="keywords" content="coastlinemicro.com, www.coastlinemicro.com, coastline, micro, irvine, ca, california, about, company, location, businsess, competition, competitors, solutions, irvine, california, technology, ceo, own, partner, fast, reliable, heritage, sophisticated, computer, system, build, custom, sample, guarantee, search, product">
<meta name="description" content="Coastline Micro Inc. is in business to develop hardware solutions that make sense for the small to corporate sized business arena. We have been in business for over a decade and have the knowledge and expertise necessary to be competitive in the market. Our every product carries a 100% Product Satisfaction Guarantee. We are located in Irvine, California at 60 N. Technology Drive. For more information about our company and its what it is in business to do please follow the link above. Our company's Heritage dates back to 1989.">
<script language="JavaScript" src="js/menu_config.js"></script>
<LINK REL="STYLESHEET" HREF="common_css.html" Type="text/css">

</head>
<body bgcolor="#ffffff" text="#333366" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onLoad="javascript:loadScript();runSearch();">

<!-- Copyright NetMedia Solutions and Coasltine Micro, Inc.-->
<script language="Javascript" src="js/menu_constructor.js"></script>

<!-- Start header table -->
<table width="100%" border="0" cellspacing="0" cellpadding="0" background="images/newones/top_tablebg_main.jpg" height="100">
  <tr> 
    <td width="30%"><img src="images/newones/illus_contact.jpg" width="250" height="100" border="0"></td>
    <td align="right" valign="middle" width="70%"><font size="1" color="#ffffff" face="verdana,arial,helvetica">$date&nbsp;&nbsp;<font size="3">&nbsp;</font></font>
	<center><img src="images/newones/title_contact.jpg" width="350" height="80" align="bottom"></center></td>
  </tr>
</table>
<!-- End header table -->

<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td width="175" align=left valign=top><img src="images/newmenu/place_holder.gif" width="175" height="150"><img src="images/spacer.gif" width="190" height="20" border="0">$powbutton $legal</td>
    <td width="5"><img src="images/140spacer.gif" width="5" height="8"></td>
    <td width="100%" align="center" valign=top><br>  
     <table width="90%" border="0" cellspacing="0" cellpadding="0" align="center">
  <tr> 
    <td> 
      <table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td width="12" height="24"><img src="images/table_top_left.gif" border=0 width="12" height="24"></td>
          <td bgcolor="#333366" align="center" width="50%">&nbsp;</td>
          <td align="center" width="30" height="24"><img src="images/table_top_mid.gif" border=0 width="30" height="24"></td>
          <td bgcolor="#8f8fab" align="center" width="50%"><b><font class="tableheading">Coastline 
            Micro Emailer</font></b></td>
          <td align="right" height="24" width="12"><img src="images/table_top_right.gif" border=0 width="12" height="24"></td>
        </tr>
      </table>
    </td>
  </tr>
  <tr bgcolor="#333366" align="center"> 
    <td> <br>
      <table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
        <tr> 
          <td width=10>&nbsp;</td>
          <td colspan="3" align="left" valign="top"> 
            <table border="0" cellspacing="0" cellpadding="0" align="left" height="25">
              <tr> 
                                  <td width="65"><font class="regtextbold"><b>Phone</b></font></td>
                                  <td width="200"><font  class="regtextnobold">(800) 729-6809</font></td>
                                </tr>
                                <tr> 
                                  <td width="65"><font class="regtextbold"><b>Fax</b></font></td>
                                  <td width="200"><font class="regtextnobold">(949) 450-9977</font></td>
              </tr>
              <tr> 
                <td width="65">&nbsp;</td>
                <td width="200">&nbsp;</td>
              </tr>
            </table>
          </td>
          <td>&nbsp;</td>
        </tr>
        <tr> 
          <td width=10>&nbsp;</td>
          <td colspan="3"> 
            <p><font class="regtextnobold"> <b>Referring File Location</b><br>
              $ENV{'HTTP_REFERER'}<br>
              <br>
              <b>Problem</b><br>
              You are trying to use this script from unspecified location. This 
              script can only be used by a number of specified domains and your 
              is not one of those.<br>
              <br>
              <b> Solution</b><br>
              Have your webmaster add your domain name to this script's valid 
              referrer list and then you can use it without any further problems. 
              You will be forwarded to our site's homepage in less than 10 seconds. 
              Sorry for the inconvenience this may have caused.<br>
              <br>
              </font></p>
          </td>
          <td width=10>&nbsp;</td>
        </tr>
      </table>
      <br>
    </td>
  </tr>
  <tr> 
    <td> 
      <table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td width="12" height="24"><img src="images/table_bot_left.gif" border=0 width="12" height="24"></td>
          <td bgcolor="#8f8fab" align="center" width="50%">&nbsp;</td>
          <td align="center" width="30" height="24"><img src="images/table_bot_mid.gif" border=0 width="30" height="24"></td>
          <td bgcolor="#333366" align="center" width="50%">&nbsp;</td>
          <td align="right" height="24" width="12"><img src="images/table_bot_right.gif" border=0 width="12" height="24"></td>
        </tr>
      </table>
    </td>
  </tr>
</table>
</td>
  </tr>
</table>

<!-- Dynamic Moving Layers -->
$pow
</body>
</html>

(END ERROR HTML)
        }
        else {

            print <<"(END ERROR HTML)";
Content-type: text/html

<html>
<head>
<title>Company Name</title>
<SCRIPT LANGUAGE="JavaScript">

///////////////////////////////////////////////////////////////////
// This script and its counterparts are ©2001 NetMedia Solutions //
// For use ONLY with CoastlineMicro.com                          //
// To re-use or have this script re-interfaced for your specific //
// needs please contact SServices\@NetMediaSolutions.com         //
// Prices are cheap for re-interfacing of current scripts and    //
// programs, so email us today to get you own LEGAL programming  //
// licensed for use only on YOUR site(s) or for YOUR purpose(s). //
///////////////////////////////////////////////////////////////////

<!-- Begin
function loadScript() {
if (document.getElementById) {  // DOM3 = IE5, NS6
document.getElementById('hidepage').style.visibility = 'hidden';
}
else {
if (document.layers) {  // Netscape 4
document.hidepage.visibility = 'hidden';
}
else {  // IE 4
document.all.hidepage.style.visibility = 'hidden';
      }
   }
}
//  End -->
</script>
<style type="text/css">
#hidepage {z-index:2000}
body { scrollbar-face-color:#F2F2F7; scrollbar-highlight-color:#F2F2F7; scrollbar-shadow-color:#8f8fab; scrollbar-3dlight-color: #333366; scrollbar-arrow-color:#333366; scrollbar-track-color:#F2F2F7; scrollbar-darkshadow-color:#8f8fab; }
</style>
<div id="hidepage" style="position: absolute; left:0px; top:0px; background-color: #FFFFFF; layer-background-color: #FFFFFF; height: 100%; width: 100%;">
<table width=100% cellpadding="0" cellspacing="0">
<tr height="100%"><td align="center" valign="middle"><br><br><img src="sharktank/images/cm_logo_large.jpg" width="166" height="59" border="0"><font face="verdana,arial,helvetica" size="2" color="#333366"><br><br>Loading DHTML interactive user interface, please wait...<br><br><br><br><br><font size="1"><b><u>Compatibility</u></b><br><br>Win/Mac MSIE 4/5/6<br>Win/Mac/Linux Netscape 4/6<br><br><i>Best if viewed on Windows 95/98/2000 platform using MSIE 4+</i></font></font></td></tr>
</table>
</div> 
<script language="JavaScript" src="js/reload.js"></script>

<!--FOLLOWING EXTERNAL SCRIPT IS USED FOR BROWSER TESTING AND IS INTEGRAL PART OF POW-->
<script language="JavaScript" src="js/dynlayer.js"></script>
<!--END-->

<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta name="keywords" content="coastlinemicro.com, www.coastlinemicro.com, coastline, micro, irvine, ca, california, about, company, location, businsess, competition, competitors, solutions, irvine, california, technology, ceo, own, partner, fast, reliable, heritage, sophisticated, computer, system, build, custom, sample, guarantee, search, product">
<meta name="description" content="Coastline Micro Inc. is in business to develop hardware solutions that make sense for the small to corporate sized business arena. We have been in business for over a decade and have the knowledge and expertise necessary to be competitive in the market. Our every product carries a 100% Product Satisfaction Guarantee. We are located in Irvine, California at 60 N. Technology Drive. For more information about our company and its what it is in business to do please follow the link above. Our company's Heritage dates back to 1989.">
<script language="JavaScript" src="js/menu_config.js"></script>
<LINK REL="STYLESHEET" HREF="common_css.html" Type="text/css">

</head>
<body bgcolor="#ffffff" text="#333366" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onLoad="javascript:loadScript();runSearch();">

<!-- Copyright NetMedia Solutions and Coasltine Micro, Inc.-->
<script language="Javascript" src="js/menu_constructor.js"></script>

<!-- Start header table -->
<table width="100%" border="0" cellspacing="0" cellpadding="0" background="images/newones/top_tablebg_main.jpg" height="100">
  <tr> 
    <td width="30%"><img src="images/newones/illus_contact.jpg" width="250" height="100" border="0"></td>
    <td align="right" valign="middle" width="70%"><font size="1" color="#ffffff" face="verdana,arial,helvetica">$date&nbsp;&nbsp;<font size="3">&nbsp;</font></font>
	<center><img src="images/newones/title_contact.jpg" width="350" height="80" align="bottom"></center></td>
  </tr>
</table>
<!-- End header table -->

<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td width="175" align=left valign=top><img src="images/newmenu/place_holder.gif" width="175" height="150"><img src="images/spacer.gif" width="190" height="20" border="0">$powbutton $legal</td>
    <td width="5"><img src="images/140spacer.gif" width="5" height="8"></td>
    <td width="100%" align="center" valign=top><br>  
<table width="90%" border="0" cellspacing="0" cellpadding="0" align="center">
  <tr> 
    <td> 
      <table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td width="12" height="24"><img src="images/table_top_left.gif" border=0 width="12" height="24"></td>
          <td bgcolor="#333366" align="center" width="50%">&nbsp;</td>
          <td align="center" width="30" height="24"><img src="images/table_top_mid.gif" border=0 width="30" height="24"></td>
          <td bgcolor="#8f8fab" align="center" width="50%"><b><font class="tableheading">Coastline 
            Micro Emailer</font></b></td>
          <td align="right" height="24" width="12"><img src="images/table_top_right.gif" border=0 width="12" height="24"></td>
        </tr>
      </table>
    </td>
  </tr>
  <tr bgcolor="#333366" align="center"> 
    <td> <br>
      <table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
        <tr> 
          <td width=10>&nbsp;</td>
          <td colspan="3" align="left" valign="top"> 
            <table border="0" cellspacing="0" cellpadding="0" align="left" height="25">
              <tr> 
                                  <td width="65"><font class="regtextbold"><b>Phone</b></font></td>
                                  <td width="200"><font  class="regtextnobold">(800) 729-6809</font></td>
                                </tr>
                                <tr> 
                                  <td width="65"><font class="regtextbold"><b>Fax</b></font></td>
                                  <td width="200"><font class="regtextnobold">(949) 450-9977</font></td>
              </tr>
              <tr> 
                <td width="65">&nbsp;</td>
                <td width="200">&nbsp;</td>
              </tr>
            </table>
          </td>
          <td>&nbsp;</td>
        </tr>
        <tr> 
          <td width=10>&nbsp;</td>
          <td colspan="3"> 
            <p><font class="regtextnobold"> <b>Problem</b><br>
              Seems like you are trying to call this emailing script solo. Sorry 
              that is not a possibility with this script....<br>
              <br>
              <b> Solution</b><br>
              Use an HTML based form to be able to utilize this handy script. 
              You will be redirected to our main site page in less than 10 seconds. 
              Sorry for the inconvenience this may have caused...</font> </p>
          </td>
          <td width=10>&nbsp;</td>
        </tr>
      </table>
      <br>
    </td>
  </tr>
  <tr> 
    <td> 
      <table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td width="12" height="24"><img src="images/table_bot_left.gif" border=0 width="12" height="24"></td>
          <td bgcolor="#8f8fab" align="center" width="50%">&nbsp;</td>
          <td align="center" width="30" height="24"><img src="images/table_bot_mid.gif" border=0 width="30" height="24"></td>
          <td bgcolor="#333366" align="center" width="50%">&nbsp;</td>
          <td align="right" height="24" width="12"><img src="images/table_bot_right.gif" border=0 width="12" height="24"></td>
        </tr>
      </table>
    </td>
  </tr>
</table>
</td>
  </tr>
</table>

<!-- Dynamic Moving Layers -->
$pow
</body>
</html>

(END ERROR HTML)
        }
    }

    elsif ($error eq 'request_method') {
	
            print <<"(END ERROR HTML)";
Content-type: text/html

<html>
<head>
<title>Company Name</title>
<SCRIPT LANGUAGE="JavaScript">

///////////////////////////////////////////////////////////////////
// This script and its counterparts are ©2001 NetMedia Solutions //
// For use ONLY with CoastlineMicro.com                          //
// To re-use or have this script re-interfaced for your specific //
// needs please contact SServices\@NetMediaSolutions.com         //
// Prices are cheap for re-interfacing of current scripts and    //
// programs, so email us today to get you own LEGAL programming  //
// licensed for use only on YOUR site(s) or for YOUR purpose(s). //
///////////////////////////////////////////////////////////////////

<!-- Begin
function loadScript() {
if (document.getElementById) {  // DOM3 = IE5, NS6
document.getElementById('hidepage').style.visibility = 'hidden';
}
else {
if (document.layers) {  // Netscape 4
document.hidepage.visibility = 'hidden';
}
else {  // IE 4
document.all.hidepage.style.visibility = 'hidden';
      }
   }
}
//  End -->
</script>
<style type="text/css">
#hidepage {z-index:2000}
body { scrollbar-face-color:#F2F2F7; scrollbar-highlight-color:#F2F2F7; scrollbar-shadow-color:#8f8fab; scrollbar-3dlight-color: #333366; scrollbar-arrow-color:#333366; scrollbar-track-color:#F2F2F7; scrollbar-darkshadow-color:#8f8fab; }
</style>
<div id="hidepage" style="position: absolute; left:0px; top:0px; background-color: #FFFFFF; layer-background-color: #FFFFFF; height: 100%; width: 100%;">
<table width=100% cellpadding="0" cellspacing="0">
<tr height="100%"><td align="center" valign="middle"><br><br><img src="sharktank/images/cm_logo_large.jpg" width="166" height="59" border="0"><font face="verdana,arial,helvetica" size="2" color="#333366"><br><br>Loading DHTML interactive user interface, please wait...<br><br><br><br><br><font size="1"><b><u>Compatibility</u></b><br><br>Win/Mac MSIE 4/5/6<br>Win/Mac/Linux Netscape 4/6<br><br><i>Best if viewed on Windows 95/98/2000 platform using MSIE 4+</i></font></font></td></tr>
</table>
</div> 
<script language="JavaScript" src="js/reload.js"></script>

<!--FOLLOWING EXTERNAL SCRIPT IS USED FOR BROWSER TESTING AND IS INTEGRAL PART OF POW-->
<script language="JavaScript" src="js/dynlayer.js"></script>
<!--END-->

<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta name="keywords" content="coastlinemicro.com, www.coastlinemicro.com, coastline, micro, irvine, ca, california, about, company, location, businsess, competition, competitors, solutions, irvine, california, technology, ceo, own, partner, fast, reliable, heritage, sophisticated, computer, system, build, custom, sample, guarantee, search, product">
<meta name="description" content="Coastline Micro Inc. is in business to develop hardware solutions that make sense for the small to corporate sized business arena. We have been in business for over a decade and have the knowledge and expertise necessary to be competitive in the market. Our every product carries a 100% Product Satisfaction Guarantee. We are located in Irvine, California at 60 N. Technology Drive. For more information about our company and its what it is in business to do please follow the link above. Our company's Heritage dates back to 1989.">
<script language="JavaScript" src="js/menu_config.js"></script>
<LINK REL="STYLESHEET" HREF="common_css.html" Type="text/css">

</head>
<body bgcolor="#ffffff" text="#333366" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onLoad="javascript:loadScript();runSearch();">

<!-- Copyright NetMedia Solutions and Coasltine Micro, Inc.-->
<script language="Javascript" src="js/menu_constructor.js"></script>

<!-- Start header table -->
<table width="100%" border="0" cellspacing="0" cellpadding="0" background="images/newones/top_tablebg_main.jpg" height="100">
  <tr> 
    <td width="30%"><img src="images/newones/illus_contact.jpg" width="250" height="100" border="0"></td>
    <td align="right" valign="middle" width="70%"><font size="1" color="#ffffff" face="verdana,arial,helvetica">$date&nbsp;&nbsp;<font size="3">&nbsp;</font></font>
	<center><img src="images/newones/title_contact.jpg" width="350" height="80" align="bottom"></center></td>
  </tr>
</table>
<!-- End header table -->

<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td width="175" align=left valign=top><img src="images/newmenu/place_holder.gif" width="175" height="150"><img src="images/spacer.gif" width="190" height="20" border="0">$powbutton $legal</td>
    <td width="5"><img src="images/140spacer.gif" width="5" height="8"></td>
    <td width="100%" align="center" valign=top><br>  
<table width="90%" border="0" cellspacing="0" cellpadding="0" align="center">
  <tr> 
    <td> 
      <table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td width="12" height="24"><img src="images/table_top_left.gif" border=0 width="12" height="24"></td>
          <td bgcolor="#333366" align="center" width="50%">&nbsp;</td>
          <td align="center" width="30" height="24"><img src="images/table_top_mid.gif" border=0 width="30" height="24"></td>
          <td bgcolor="#8f8fab" align="center" width="50%"><b><font class="tableheading">Request 
            Method Invalid</font></b></td>
          <td align="right" height="24" width="12"><img src="images/table_top_right.gif" border=0 width="12" height="24"></td>
        </tr>
      </table>
    </td>
  </tr>
  <tr bgcolor="#333366" align="center"> 
    <td> <br>
      <table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
        <tr> 
          <td width=10>&nbsp;</td>
          <td colspan="3" align="left" valign="top"> 
            <table border="0" cellspacing="0" cellpadding="0" align="left" height="25">
              <tr> 
                                  <td width="65"><font class="regtextbold"><b>Phone</b></font></td>
                                  <td width="200"><font  class="regtextnobold">(800) 729-6809</font></td>
                                </tr>
                                <tr> 
                                  <td width="65"><font class="regtextbold"><b>Fax</b></font></td>
                                  <td width="200"><font class="regtextnobold">(949) 450-9977</font></td>
              </tr>
              <tr> 
                <td width="65">&nbsp;</td>
                <td width="200">&nbsp;</td>
              </tr>
            </table>
          </td>
          <td>&nbsp;</td>
        </tr>
        <tr> 
          <td width=10>&nbsp;</td>
          <td colspan="3"> 
            <p><font class="regtextnobold"><b>Problem</b><br>
              The request method is not GET or POST on the form you are submitting 
              from.<br>
              <br>
              <b>Solution</b><br>
              Make sure the form you are using is passing GET or POST as the METHOD 
              for data transfer when using this particular CGI script. You will 
              be re-directed to our main site page in less than 10 seconds. Sorry 
              for the inconvenience this may have caused you.<br>
              <br>
              <br>
              </font></p>
            <center>
              <a href="javascript:history.go(-1)"><img src="images/back_but.gif" border=0></a> 
            </center>
            <p>&nbsp; </p>
          </td>
          <td width=10>&nbsp;</td>
        </tr>
      </table>
      <br>
    </td>
  </tr>
  <tr> 
    <td> 
      <table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td width="12" height="24"><img src="images/table_bot_left.gif" border=0 width="12" height="24"></td>
          <td bgcolor="#8f8fab" align="center" width="50%">&nbsp;</td>
          <td align="center" width="30" height="24"><img src="images/table_bot_mid.gif" border=0 width="30" height="24"></td>
          <td bgcolor="#333366" align="center" width="50%">&nbsp;</td>
          <td align="right" height="24" width="12"><img src="images/table_bot_right.gif" border=0 width="12" height="24"></td>
        </tr>
      </table>
    </td>
  </tr>
</table>
</td>
  </tr>
</table>

<!-- Dynamic Moving Layers -->
$pow
</body>
</html>

(END ERROR HTML)
    }

    elsif ($error eq 'no_recipient') {

            print <<"(END ERROR HTML)";
Content-type: text/html

<html>
<head>
<title>Company Name</title>
<SCRIPT LANGUAGE="JavaScript">

///////////////////////////////////////////////////////////////////
// This script and its counterparts are ©2001 NetMedia Solutions //
// For use ONLY with CoastlineMicro.com                          //
// To re-use or have this script re-interfaced for your specific //
// needs please contact SServices\@NetMediaSolutions.com         //
// Prices are cheap for re-interfacing of current scripts and    //
// programs, so email us today to get you own LEGAL programming  //
// licensed for use only on YOUR site(s) or for YOUR purpose(s). //
///////////////////////////////////////////////////////////////////

<!-- Begin
function loadScript() {
if (document.getElementById) {  // DOM3 = IE5, NS6
document.getElementById('hidepage').style.visibility = 'hidden';
}
else {
if (document.layers) {  // Netscape 4
document.hidepage.visibility = 'hidden';
}
else {  // IE 4
document.all.hidepage.style.visibility = 'hidden';
      }
   }
}
//  End -->
</script>
<style type="text/css">
#hidepage {z-index:2000}
body { scrollbar-face-color:#F2F2F7; scrollbar-highlight-color:#F2F2F7; scrollbar-shadow-color:#8f8fab; scrollbar-3dlight-color: #333366; scrollbar-arrow-color:#333366; scrollbar-track-color:#F2F2F7; scrollbar-darkshadow-color:#8f8fab; }
</style>
<div id="hidepage" style="position: absolute; left:0px; top:0px; background-color: #FFFFFF; layer-background-color: #FFFFFF; height: 100%; width: 100%;">
<table width=100% cellpadding="0" cellspacing="0">
<tr height="100%"><td align="center" valign="middle"><br><br><img src="sharktank/images/cm_logo_large.jpg" width="166" height="59" border="0"><font face="verdana,arial,helvetica" size="2" color="#333366"><br><br>Loading DHTML interactive user interface, please wait...<br><br><br><br><br><font size="1"><b><u>Compatibility</u></b><br><br>Win/Mac MSIE 4/5/6<br>Win/Mac/Linux Netscape 4/6<br><br><i>Best if viewed on Windows 95/98/2000 platform using MSIE 4+</i></font></font></td></tr>
</table>
</div> 
<script language="JavaScript" src="js/reload.js"></script>

<!--FOLLOWING EXTERNAL SCRIPT IS USED FOR BROWSER TESTING AND IS INTEGRAL PART OF POW-->
<script language="JavaScript" src="js/dynlayer.js"></script>
<!--END-->

<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta name="keywords" content="coastlinemicro.com, www.coastlinemicro.com, coastline, micro, irvine, ca, california, about, company, location, businsess, competition, competitors, solutions, irvine, california, technology, ceo, own, partner, fast, reliable, heritage, sophisticated, computer, system, build, custom, sample, guarantee, search, product">
<meta name="description" content="Coastline Micro Inc. is in business to develop hardware solutions that make sense for the small to corporate sized business arena. We have been in business for over a decade and have the knowledge and expertise necessary to be competitive in the market. Our every product carries a 100% Product Satisfaction Guarantee. We are located in Irvine, California at 60 N. Technology Drive. For more information about our company and its what it is in business to do please follow the link above. Our company's Heritage dates back to 1989.">
<script language="JavaScript" src="js/menu_config.js"></script>
<LINK REL="STYLESHEET" HREF="common_css.html" Type="text/css">

</head>
<body bgcolor="#ffffff" text="#333366" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onLoad="javascript:loadScript();runSearch();">

<!-- Copyright NetMedia Solutions and Coasltine Micro, Inc.-->
<script language="Javascript" src="js/menu_constructor.js"></script>

<!-- Start header table -->
<table width="100%" border="0" cellspacing="0" cellpadding="0" background="images/newones/top_tablebg_main.jpg" height="100">
  <tr> 
    <td width="30%"><img src="images/newones/illus_contact.jpg" width="250" height="100" border="0"></td>
    <td align="right" valign="middle" width="70%"><font size="1" color="#ffffff" face="verdana,arial,helvetica">$date&nbsp;&nbsp;<font size="3">&nbsp;</font></font>
	<center><img src="images/newones/title_contact.jpg" width="350" height="80" align="bottom"></center></td>
  </tr>
</table>
<!-- End header table -->

<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td width="175" align=left valign=top><img src="images/newmenu/place_holder.gif" width="175" height="150"><img src="images/spacer.gif" width="190" height="20" border="0">$powbutton $legal</td>
    <td width="5"><img src="images/140spacer.gif" width="5" height="8"></td>
    <td width="100%" align="center" valign=top><br>  
<table width="90%" border="0" cellspacing="0" cellpadding="0" align="center">
  <tr> 
    <td> 
      <table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td width="12" height="24"><img src="images/table_top_left.gif" border=0 width="12" height="24"></td>
          <td bgcolor="#333366" align="center" width="50%">&nbsp;</td>
          <td align="center" width="30" height="24"><img src="images/table_top_mid.gif" border=0 width="30" height="24"></td>
          <td bgcolor="#8f8fab" align="center" width="50%"><b><font class="tableheading">Email 
            Address Missing</font></b></td>
          <td align="right" height="24" width="12"><img src="images/table_top_right.gif" border=0 width="12" height="24"></td>
        </tr>
      </table>
    </td>
  </tr>
  <tr bgcolor="#333366" align="center"> 
    <td> <br>
      <table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
        <tr> 
          <td width=10>&nbsp;</td>
          <td colspan="3" align="left" valign="top"> 
            <table border="0" cellspacing="0" cellpadding="0" align="left" height="25">
              <tr> 
                                  <td width="65"><font class="regtextbold"><b>Phone</b></font></td>
                                  <td width="200"><font  class="regtextnobold">(800) 729-6809</font></td>
                                </tr>
                                <tr> 
                                  <td width="65"><font class="regtextbold"><b>Fax</b></font></td>
                                  <td width="200"><font class="regtextnobold">(949) 450-9977</font></td>
              </tr>
              <tr> 
                <td width="65">&nbsp;</td>
                <td width="200">&nbsp;</td>
              </tr>
            </table>
          </td>
          <td>&nbsp;</td>
        </tr>
        <tr> 
          <td width=10>&nbsp;</td>
          <td colspan="3"> 
            <p><font class="regtextnobold"> <b>Problem</b><br>
              No email address was specified. This form cannot be submitted unless 
              you specify your CORRECT email address.<br>
              <br>
              <b> Solution</b><br>
              Click the 'Back' button below to get back to the form then make 
              sure you fill our your email address and try again. Thank you for 
              your time and patience.t</font></p>
            <br>
            <br>
            <center>
              <a href="javascript:history.go(-1)"><img src="images/back_but.gif" border=0></a> 
            </center>
          </td>
          <td width=10>&nbsp;</td>
        </tr>
      </table>
      <br>
    </td>
  </tr>
  <tr> 
    <td> 
      <table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td width="12" height="24"><img src="images/table_bot_left.gif" border=0 width="12" height="24"></td>
          <td bgcolor="#8f8fab" align="center" width="50%">&nbsp;</td>
          <td align="center" width="30" height="24"><img src="images/table_bot_mid.gif" border=0 width="30" height="24"></td>
          <td bgcolor="#333366" align="center" width="50%">&nbsp;</td>
          <td align="right" height="24" width="12"><img src="images/table_bot_right.gif" border=0 width="12" height="24"></td>
        </tr>
      </table>
    </td>
  </tr>
</table>
</td>
  </tr>
</table>

<!-- Dynamic Moving Layers -->
$pow
</body>
</html>
(END ERROR HTML)
    }

    elsif ($error eq 'missing_fields') {
        if ($Config{'missing_fields_redirect'}) {
            print "Location: $Config{'missing_fields_redirect'}\n\n";
        }
        else {
            foreach $missing_field (@error_fields) {
                $missing_field_list .= "      <li>$missing_field\n";
            }

            print <<"(END ERROR HTML)";
Content-type: text/html

<html>
<head>
<title>Company Name</title>
<SCRIPT LANGUAGE="JavaScript">

///////////////////////////////////////////////////////////////////
// This script and its counterparts are ©2001 NetMedia Solutions //
// For use ONLY with CoastlineMicro.com                          //
// To re-use or have this script re-interfaced for your specific //
// needs please contact SServices\@NetMediaSolutions.com         //
// Prices are cheap for re-interfacing of current scripts and    //
// programs, so email us today to get you own LEGAL programming  //
// licensed for use only on YOUR site(s) or for YOUR purpose(s). //
///////////////////////////////////////////////////////////////////

<!-- Begin
function loadScript() {
if (document.getElementById) {  // DOM3 = IE5, NS6
document.getElementById('hidepage').style.visibility = 'hidden';
}
else {
if (document.layers) {  // Netscape 4
document.hidepage.visibility = 'hidden';
}
else {  // IE 4
document.all.hidepage.style.visibility = 'hidden';
      }
   }
}
//  End -->
</script>
<style type="text/css">
#hidepage {z-index:2000}
body { scrollbar-face-color:#F2F2F7; scrollbar-highlight-color:#F2F2F7; scrollbar-shadow-color:#8f8fab; scrollbar-3dlight-color: #333366; scrollbar-arrow-color:#333366; scrollbar-track-color:#F2F2F7; scrollbar-darkshadow-color:#8f8fab; }
</style>
<div id="hidepage" style="position: absolute; left:0px; top:0px; background-color: #FFFFFF; layer-background-color: #FFFFFF; height: 100%; width: 100%;">
<table width=100% cellpadding="0" cellspacing="0">
<tr height="100%"><td align="center" valign="middle"><br><br><img src="sharktank/images/cm_logo_large.jpg" width="166" height="59" border="0"><font face="verdana,arial,helvetica" size="2" color="#333366"><br><br>Loading DHTML interactive user interface, please wait...<br><br><br><br><br><font size="1"><b><u>Compatibility</u></b><br><br>Win/Mac MSIE 4/5/6<br>Win/Mac/Linux Netscape 4/6<br><br><i>Best if viewed on Windows 95/98/2000 platform using MSIE 4+</i></font></font></td></tr>
</table>
</div> 
<script language="JavaScript" src="js/reload.js"></script>

<!--FOLLOWING EXTERNAL SCRIPT IS USED FOR BROWSER TESTING AND IS INTEGRAL PART OF POW-->
<script language="JavaScript" src="js/dynlayer.js"></script>
<!--END-->

<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta name="keywords" content="coastlinemicro.com, www.coastlinemicro.com, coastline, micro, irvine, ca, california, about, company, location, businsess, competition, competitors, solutions, irvine, california, technology, ceo, own, partner, fast, reliable, heritage, sophisticated, computer, system, build, custom, sample, guarantee, search, product">
<meta name="description" content="Coastline Micro Inc. is in business to develop hardware solutions that make sense for the small to corporate sized business arena. We have been in business for over a decade and have the knowledge and expertise necessary to be competitive in the market. Our every product carries a 100% Product Satisfaction Guarantee. We are located in Irvine, California at 60 N. Technology Drive. For more information about our company and its what it is in business to do please follow the link above. Our company's Heritage dates back to 1989.">
<script language="JavaScript" src="js/menu_config.js"></script>
<LINK REL="STYLESHEET" HREF="common_css.html" Type="text/css">

</head>
<body bgcolor="#ffffff" text="#333366" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onLoad="javascript:loadScript();runSearch();">

<!-- Copyright NetMedia Solutions and Coasltine Micro, Inc.-->
<script language="Javascript" src="js/menu_constructor.js"></script>

<!-- Start header table -->
<table width="100%" border="0" cellspacing="0" cellpadding="0" background="images/newones/top_tablebg_main.jpg" height="100">
  <tr> 
    <td width="30%"><img src="images/newones/illus_contact.jpg" width="250" height="100" border="0"></td>
    <td align="right" valign="middle" width="70%"><font size="1" color="#ffffff" face="verdana,arial,helvetica">$date&nbsp;&nbsp;<font size="3">&nbsp;</font></font>
	<center><img src="images/newones/title_contact.jpg" width="350" height="80" align="bottom"></center></td>
  </tr>
</table>
<!-- End header table -->

<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td width="175" align=left valign=top><img src="images/newmenu/place_holder.gif" width="175" height="150"><img src="images/spacer.gif" width="190" height="20" border="0">$powbutton $legal</td>
    <td width="5"><img src="images/140spacer.gif" width="5" height="8"></td>
    <td width="100%" align="center" valign=top><br>  
      <table align="center" cellpadding=0 cellspacing=0 border=0>
        <tr> 
          <td width="12" height="24"  valign=top><img src="images/table_top_left.gif" border=0></td>
          <td bgcolor="#333366" width="273">&nbsp;</td>
          <td width="30" height="24"  valign=top><img src="images/table_top_mid.gif" border=0></td>
          <td bgcolor="#8f8fab" width="273" align="center"><b><font class="tableheading">Form 
            Incomplete </font></b></td>
          <td width="12" height="24" valign=top><img src="images/table_top_right.gif" border=0></td>
        </tr>
        <tr> 
          <td width="12" colspan="5" bgcolor="#333366"> 
            <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
              <tr> 
                <td colspan="2"> 
                  <table width="100%" border="0" cellspacing="0" cellpadding="0">
                    <tr align="center"> 
                      <td width="100%"> 
                        <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
                          <tr> 
                            <td colspan="5"> <br>
                              <table width="600" border="0" cellspacing="0" cellpadding="0" align="center">
                                <tr> 
                                  <td colspan=5 height=5><font size="-4">&nbsp;</font></td>
                                </tr>
                                <tr> 
                                  <td width=10>&nbsp;</td>
                                  <td colspan="3" align="left" valign="top"> 
                                    <table border="0" cellspacing="0" cellpadding="0" align="left" height="25">
                                      <tr> 
                                  <td width="65"><font class="regtextbold"><b>Phone</b></font></td>
                                  <td width="200"><font  class="regtextnobold">(800) 729-6809</font></td>
                                </tr>
                                <tr> 
                                  <td width="65"><font class="regtextbold"><b>Fax</b></font></td>
                                  <td width="200"><font class="regtextnobold">(949) 450-9977</font></td>
                                      </tr>
                                      <tr> 
                                        <td width="65">&nbsp;</td>
                                        <td width="200">&nbsp;</td>
                                      </tr>
                                    </table>
                                  </td>
                                  <td>&nbsp;</td>
                                </tr>
                                <tr> 
                                  <td width=10>&nbsp;</td>
                                  <td colspan="3"> 
                                    <p><font class="regtextnobold"> <b>Problem</b><br>
                                      The form you have just submitted is not 
                                      complete.<br>
                                      <br>
                                      <b> Solution</b><br>
                                      Below is a list of all the form fields which 
                                      were not complete at the time you submitted 
                                      your form. Click on the button below to 
                                      go back and complete the form. Thank you 
                                      very much for your time and patience..<br>
                                      <br>
                                      <b>Incomplete Fields</b><br>
                                      $missing_field_list</font></p>
                                    <br>
                                    <br>
                                    <center>
                                      <a href="javascript:history.go(-1)"><img src="images/back_but.gif" border=0></a> 
                                    </center>
                                  </td>
                                  <td width=10>&nbsp;</td>
                                </tr>
                                <tr> 
                                  <td colspan=5 height=5><font size="-4">&nbsp;</font></td>
                                </tr>
                              </table>
                              <br>
                            </td>
                          </tr>
                        </table>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </td>
        </tr>
        <tr> 
          <td width="12" height="24"  valign=bottom><img src="images/table_bot_left.gif" border=0></td>
          <td bgcolor="#8f8fab" width="273">&nbsp;</td>
          <td width="30" height="24"  valign=bottom><img src="images/table_bot_mid.gif" border=0></td>
          <td bgcolor="#333366" width="273">&nbsp;</td>
          <td width="12" height="24" valign=bottom><img src="images/table_bot_right.gif" border=0></td>
        </tr>
      </table>
</td>
  </tr>
</table>

<!-- Dynamic Moving Layers -->
$pow
</body>
</html>
(END ERROR HTML)
        }
    }
    exit;
}

