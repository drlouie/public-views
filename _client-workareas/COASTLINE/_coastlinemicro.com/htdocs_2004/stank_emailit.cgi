#!/usr/bin/perl5 -s

###########################################################################################################
# Company: ©2001 NetMedia Solutions                                                                             #
# Date: Saturday, September 21, 2001                                                                      #
# Location: Los Angeles County, California, United States of America                                      #
# Made By: Luis Rodriguez (drlouie)                                                                       #
# Email: Drlouie@NetMediaSol.com                                                                          #
#                                                                                                         #
# This program cannot be duplicated, distributed or re-used for any other purpose other than its original #
# intended purpose and function. You may request NetMedia Solutions for a copy of the script,             #
# personalized to fit your exact needs for a small re-programming fee.                                    #
###########################################################################################################

require ("parse_query.nsp");
require ("date.nsp");

## ----------------->>> GIVE THE DOCUMENT SOME STYLE DEPENDING ON BROWSER AND DOCUMENT LOCATION
$browser = "$ENV{'HTTP_USER_AGENT'}";
if (($browser =~ "Mozilla/" && $browser =~ "6.") || ($browser =~ "Mozilla/" && $browser =~ "4.") || $browser =~ "Netscape6") { $tablewidth = "100%"; $t1 = "2%"; $t2 = "60%"; $t3 = "18%"; $t4 = "18%"; }	
else { $tablewidth = "470"; $t1 = "5"; $t2 = "339"; $t3 = "79"; $t4 = "42"; }
$PrintPage = "";
$TBack = "background=\"images/tables/topbar.jpg\" height=\"24\"";
$TLeft = "<img src=\"images/tables/topbar_left.jpg\" width=\"5\" height=\"24\">";
$TRight = "<img src=\"images/tables/topbar_right.jpg\" width=\"5\" height=\"24\">";
$PrintIt = "&nbsp;";
$EmailIt = "&nbsp;";

## ----------------->>> Must Have MyEmail and MyComments to PROCESS
if ($FORM{'MyPageSubject'}) {

## ----------------------->>> SEND EMAIL START
## ----------------------->>> PREPARE VARIABLES FOR OUTER SEND EMAIL PROGRZM
$ThyAddress = "$ENV{'REMOTE_ADDR'}";
$ThyPort = "$ENV{'REMOTE_PORT'}";
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst)=localtime(time);
$min=sprintf("%02d", $min);
$sec=sprintf("%02d", $sec);
$EmailType = "$FORM{'EmailType'}";
$TO = "$FORM{'MyEmail'}";
$FROM = "stadmin\@coastlinemicro.com(Coastline Micro, Inc. - Shark Tank)";
$SUBJECT = "$FORM{'MyPageSubject'}";
$GREETING = "Concerned,\n\n";
$BODY = "Someone thought you should take a look at the following URL: $FORM{'MyPageURL'}\n\nThey also mentioned,\n$FORM{'MyComments'}\n\n\n";
$ATTACHMENTS = "";
$FOOTER = "Coastline Micro, Inc. - Shark Tank\nhttp://www.coastlinemicro.com/sharktank/\n\n\n";
$MYHTMLTITLE = "<title>$FORM{'MyPageSubject'}</title>";
$MYHTMLSTAMP = "<table width=\"450\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" align=\"center\"><tr><td width=\"100%\" valign=\"top\"><font face=\"verdana,arial,helvetica\" size=\"1\" color=\"#333366\">Concerned,<br><br>Someone thought you should take a look at the following URL: <A href=\"$FORM{'MyPageURL'}\">$FORM{'MyPageURL'}</a><br><br>They also mentioned,<br>$FORM{'MyComments'}<br><br><ul><li>Does this look like it was sent as spam?<br><a href=\"mailto:security\@coastlinemicro.com?Subject=* SECURITY ALERT * Bad Email It Call...&Body=A user connected as $ThyAddress:$ThyPort on $date at around $hour:$min:$sec sent an unsolicited email via the Email It feature within our site. Please make sure you note this or report this to your supervisor or manager. **** Note: This is an automatically generated message that a user has chosen to send for a specific reason. Please make sure you pay special attention to this email message. **** ----> Coastline Micro, Inc. - Shark Tank Security <----\">Report It!</a></li></ul></font></td></tr></table>";
$MYHTMLATTACH = "";
## ----------------------->>> EXECUTE OUTER EMAIL PROGRAM - IT CHECKS - $EmailType for HTML or TEXT
require("mailer_2nd.nsp");
## ----------------------->>> END EMAILINGS

print "Content-type: text/html\n\n";

&topper;

{
print <<EOF

<table width="300" border="0" align="center" cellspacing="0" cellpadding="0">
                            <tr> 
                              <td width="270" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="270" valign="top"> 
                                <table width="300" border="0" cellspacing="0" cellpadding="0">
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="115" bgcolor="#F2F2F7"><font class="btext"><b>Dear 
                                      User,</b><br>
                                      Your email message has been sent to <font class="btext2">$FORM{'MyEmail'}</font>. 
                                      We take this opportunity to thank you once 
                                      again for letting others know about our 
                                      site.<br>
                                      <br>
                                      <b>Sincerely,</b><br>
                                      The Coastline Micro Management</font></td>
                                    <td width="11" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="5"></td>
                                    <td height="5" align="center" width="318" valign="top" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="5" height="5"></td>
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="5"></td>
                                  </tr>
                                </table>
                              </td>
                              <td bgcolor="#8F8FAB" width="1" height="70"><img src="images/verticalbar.gif" width="1" height="25"></td>
                            </tr>
                            <tr> 
                              <td width="270" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                          </table>
                          

EOF
}

&bottom;									

exit;

}

## ----------------->>> Must Have MySubject and MYURL to START
elsif ($FORM{'EmailSubject'} && $FORM{'MySubject'} && $FORM{'MyTitle'} && $FORM{'MyLoad'} && $FORM{'MyData'}) {

if ($FORM{'MySubject'} eq "GreatWhite" || $FORM{'MyTitle'} eq "GreatWhite") { 
	$muacmseries = "gw"; 
	$MyURL = "framer.html?subject=$muacmseries&title=$muacmseries&$FORM{'MyLoad'}=$FORM{'MyData'}";
}
elsif ($FORM{'MySubject'} eq "Mako" || $FORM{'MyTitle'} eq "Mako") { 
	$muacmseries = "mako"; 
	$MyURL = "framer.html?subject=$muacmseries&title=$muacmseries&$FORM{'MyLoad'}=$FORM{'MyData'}";
}
elsif ($FORM{'MySubject'} eq "Reef" || $FORM{'MyTitle'} eq "Reef") { 
	$muacmseries = "reef"; 
	$MyURL = "framer.html?subject=$muacmseries&title=$muacmseries&$FORM{'MyLoad'}=$FORM{'MyData'}";
}
elsif ($FORM{'MySubject'} eq "Thresher" || $FORM{'MyTitle'} eq "Thresher") { 
	$muacmseries = "thresher"; 
	$MyURL = "framer.html?subject=$muacmseries&title=$muacmseries&$FORM{'MyLoad'}=$FORM{'MyData'}";
}
elsif ($FORM{'MySubject'} eq "Tiger" || $FORM{'MyTitle'} eq "Tiger") { 
	$muacmseries = "tiger"; 
	$MyURL = "framer.html?subject=$muacmseries&title=$muacmseries&$FORM{'MyLoad'}=$FORM{'MyData'}";
}
else { $MyURL = "framer.html?subject=$FORM{'MySubject'}&title=$FORM{'MyTitle'}&$FORM{'MyLoad'}=$FORM{'MyData'}"; }

## ----------------->>> IF SUBJECT CONTAINS SPECIAL CHARACTERS RE-ENCODE EM
$EmailSubject = "$FORM{'EmailSubject'}";
$EsteTM = "&#153; ";
$EmailSubject =~ s/(tm) /$EsteTM/gi;

## ----------------->>> IF SUBJECT DOES NOT CONTAIN Micro, ONLY NS DOES THIS
if ($EmailSubject =~ "Micro") { }
else { $EmailSubject = "Coastline Micro's - Shark Tank&#153;"; }
if ($browser =~ "Mozilla/" && $browser =~ "4.") { $FormMethod = "method=\"GET\""; $FormAction = "action=\"stank_emailit.html\""; }
else { $FormMethod = ""; $FormAction = ""; }

print "Content-type: text/html\n\n";
{
print <<EOF

<html>
<head>
<title>Coastline Micro Inc.</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<STYLE TYPE="text/css">
body { background-color:#ffffff; scrollbar-face-color:#F2F2F7; scrollbar-highlight-color:#F2F2F7; scrollbar-shadow-color:#8f8fab; scrollbar-3dlight-color: #333366; scrollbar-arrow-color:#333366; scrollbar-track-color:#F2F2F7; scrollbar-darkshadow-color:#8f8fab; }
</STYLE>
<LINK REL="STYLESHEET" HREF="common_css.html" Type="text/css">

<script language="Javascript">

///////////////////////////////////////////////////////////////////
// This script and its counterparts are ©2001 NetMedia Solutions //
// For use ONLY with CoastlineMicro.com                          //
// To re-use or have this script re-interfaced for your specific //
// needs please contact SServices\@NetMediaSolutions.com         //
// Prices are cheap for re-interfacing of current scripts and    //
// programs, so email us today to get you own LEGAL programming  //
// licensed for use only on YOUR site(s) or for YOUR purpose(s). //
///////////////////////////////////////////////////////////////////

// FORM CHECKER FUNCTIONS
// By Drlouie \@ NetMedia Solutions
// info\@NetMediaSol.com for help
// Copyright 2001 NetMedia Solutions

function checkForm() {
var missingdrop = "";
var thefirst = "";

// Check Common form fields
// CHECK EMAIL
  if (document.EmailIt.MyEmail.value == "")	{
    missingdrop += "\\n     - Recipient's Email";
	if (thefirst == "") { thefirst = "MyEmail"; }
  } else if ((document.EmailIt.MyEmail.value.indexOf('\@') == -1) || 
        (document.EmailIt.MyEmail.value.indexOf('.') == -1)) {
    missingdrop += "\\n     - Recipient's Email Format should be: username\@company.com";
	if (thefirst == "") { thefirst = "MyEmail"; }
  }
  if ((document.EmailIt.MyEmail.value.indexOf(',') != -1)) {
    missingdrop += "\\n     - Commas are not allowed in email addresses";
	if (thefirst == "") { thefirst = "MyEmail"; }
  }
  if ((document.EmailIt.MyEmail.value.indexOf(';') != -1)) {
    missingdrop += "\\n     - Semicolons are not allowed in email addresses";
	if (thefirst == "") { thefirst = "MyEmail"; }
  }
  if ((document.EmailIt.MyEmail.value.indexOf(':') != -1)) {
    missingdrop += "\\n     - Colons are not allowed in email addresses";
	if (thefirst == "") { thefirst = "MyEmail"; }
  }
  if ((document.EmailIt.MyEmail.value.indexOf('&') != -1)) {
    missingdrop += "\\n     - Ampersands are not allowed in email addresses";
	if (thefirst == "") { thefirst = "MyEmail"; }
  }
  if ((document.EmailIt.MyEmail.value.indexOf(' ') != -1)) {
    missingdrop += "\\n     - Spaces are not allowed in email addresses";
	if (thefirst == "") { thefirst = "MyEmail"; }
  }

if (document.EmailIt.MyComments.value == "" || document.EmailIt.MyComments.value == " ") {
    missingdrop += "\\n     - Your Comments are missing";
	if (thefirst == "") { thefirst = "MyComments"; }
}
  
// If anything comes back wrong alert and detain form, else submit info
if (missingdrop != "") {
    missingdrop ="___________________________________________                   \\n\\n" + "  Sorry, I cannot process your request because the\\n  following fields are either blank or filled incorrectly:\\n" + "___________________________________________                   \\n\\n" +
    missingdrop + "\\n\\n___________________________________________                   " + "\\n\\n   To continue, check fields and submit form again!" + "\\n___________________________________________";
    alert(missingdrop);
	document.EmailIt(thefirst).focus();
    return false;
} 
else {
return true;
}
}
</SCRIPT>

</head>
<body bgcolor="#ffffff" text="#8F8FAB" leftmargin="0" topmargin="0" marginwidth="0" scroll="yes" marginheight="0">

<table width="$tablewidth" border="0" cellspacing="0" cellpadding="0">
  <tr> 
    <td align="center" valign="middle" width="$tablewidth" height="25"> 
      <table width="$tablewidth" border="0" cellspacing="0" cellpadding="0" $TBack>
        <tr> 
          <td width="$t1" align="left">$TLeft</td>
          <td width="$t2"><nobr><font class="btext">&nbsp;&nbsp;<b>Coastline Micro, Inc. - Email It!</b></font></nobr></td>
          <td width="$t3" align="center" valign="top">$EmailIt</td>
          <td width="$t4" align="center" valign="top">$PrintIt</td>
          <td width="$t1" align="right" valign="top">$TRight</td>
        </tr>
      </table>
    </td>
  </tr>
  <tr>
    <td height="4"><img src="spacer.gif" width="1" height="4" border="0"></td>
  </tr>
  <tr> 
    <td width="100%"> 
      <table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
        <tr> 
          <td width="100%"><font class="btext"> 
            <p>You have selected to send a link of the page you were just visiting. To do so you must complete the fields below. We thank you very much for letting others know about this site.
			<form name="EmailIt" onSubmit="return checkForm();" $FormMethod $FormAction>

<table width="300" border="0" cellspacing="0" cellpadding="0" align="center">
  <tr> 
	<td width="348" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
  </tr>
  <tr> 
    <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
    <td width="348" valign="top"> 
                                <table width="300" border="0" cellspacing="0" cellpadding="0">
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                    <td height="25" bgcolor="#F2F2F7" align="center" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366"><font color="#EB0000">All 
                                      fields must be complete...</font></font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="350" align="center"><nobr> 
                                      <font face="verdana,arial,helvetica" size="1" color="#333366"><b>Email Subject</b><br></font>
									  <input type="text" name="LeSUBJECT" value="$EmailSubject" onFocus="javascript:alert(this.value);document.EmailIt.MyEmail.focus();" class="inputtext15">
									  <br>
                                      <br>
                                      <font face="verdana,arial,helvetica" size="1" color="#333366"><b>Page URL</b><br></font>
									  <input type="text" name="LeURL" value="http://www.coastlinemicro.com/$MyURL" onFocus="javascript:alert(this.value);document.EmailIt.MyEmail.focus();" class="inputtext15">
									  <br>
                                      <br>
                                      <font face="verdana,arial,helvetica" size="1" color="#333366"><b>Recipient's Email</b><br></font> 
                                      <input type="text" name="MyEmail" size="15" class="inputtext15">
                                      <br>
                                      <br>
                                      <font face="verdana,arial,helvetica" size="1" color="#333366"><b>Email Format</b><br> 
                                      Html</font><input type="radio" name="EmailType" value="HTML" checked><font face="verdana,arial,helvetica" size="1" color="#333366">&nbsp;&nbsp;Text</font><input type="radio" name="EmailType" value="TEXT">
                                      <br>
                                      <br>
                                      <font face="verdana,arial,helvetica" size="1" color="#333366"><b>Your Comments</b><br>
                                      </font> 
                                      <textarea name="MyComments" cols="25" class="textarea" rows="2"></textarea>
                                      <br>
                                      <br><input type="submit" value="Send Email" name="submit" class="inputbut">
                    <input type="reset" value="Reset Form" name="reset" class="inputbut">
                                      </nobr>
                                      <input type="hidden" name="MyPageSubject" value="$EmailSubject">
                                      <input type="hidden" name="MyPageURL" value="http://www.coastlinemicro.com/$MyURL">

</td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" align="center" width="318" valign="top" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                </table>
  	</td>
    <td bgcolor="#8F8FAB" width="1" height="70"><img src="images/verticalbar.gif" width="1" height="25"></td>
      </tr>
      <tr> 
    <td width="100%" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
  </tr>
</table>
                          
			
			</form>
			</p>
            </font> </td>
        </tr>
      </table>
    </td>
  </tr>
</table>

<table width="$tablewidth" border="0" cellspacing="0" cellpadding="0"><tr><td align="center" width="$tablewidth"> 
$STANKLEGAL
</td></tr></table>

</body>
</html>

EOF
}
exit;
}

## SORRY YALL NO GOOD CALL
else {
$sorry = `cat sorry_nospec.nsf`;

print "Content-type: text/html\n\n";
{
print <<EOF

$sorry

EOF
}
exit;
}

sub topper {

{
print <<EOF

<html>
<head>
<title>Coastline Micro Inc.</title>
<script>

///////////////////////////////////////////////////////////////////
// This script and its counterparts are ©2001 NetMedia Solutions //
// For use ONLY with CoastlineMicro.com                          //
// To re-use or have this script re-interfaced for your specific //
// needs please contact SServices\@NetMediaSolutions.com         //
// Prices are cheap for re-interfacing of current scripts and    //
// programs, so email us today to get you own LEGAL programming  //
// licensed for use only on YOUR site(s) or for YOUR purpose(s). //
///////////////////////////////////////////////////////////////////

</script>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<STYLE TYPE="text/css">
body { background-color:#ffffff; }
</STYLE>
<LINK REL="STYLESHEET" HREF="common_css.html" Type="text/css">
</head>
<body bgcolor="#ffffff" text="#8F8FAB" leftmargin="0" topmargin="0" marginwidth="0" scroll="yes" marginheight="0">

<table width="$tablewidth" border="0" cellspacing="0" cellpadding="0">
  <tr> 
    <td align="center" valign="middle" width="$tablewidth" height="25"> 
      <table width="$tablewidth" border="0" cellspacing="0" cellpadding="0" $TBack>
        <tr> 
          <td width="$t1" align="left">$TLeft</td>
          <td width="$t2"><nobr><font class="btext">&nbsp;&nbsp;<b>Coastline Micro, Inc. - Email It!</b></font></nobr></td>
          <td width="$t3" align="center" valign="top">$EmailIt</td>
          <td width="$t4" align="center" valign="top">$PrintIt</td>
          <td width="$t1" align="right" valign="top">$TRight</td>
        </tr>
      </table>
    </td>
  </tr>
  <tr>
    <td height="4"><img src="spacer.gif" width="1" height="4" border="0"></td>
  </tr>
  <tr> 
    <td width="100%"> 


EOF
}
}
exit;

sub bottom {

{
print <<EOF


    </td>
  </tr>
</table>

<table width="$tablewidth" border="0" cellspacing="0" cellpadding="0"><tr><td align="center" width="$tablewidth"> 
$STANKLEGAL
</td></tr></table>

</body>
</html>

EOF
}
}
exit;