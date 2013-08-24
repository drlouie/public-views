#!/usr/bin/perl5 -w

## Test location of request
require ("referer.nsp");

print "Content-type: text/html\n\n";
## Snif thisurl, in case user needs to login you have somewhere to send em back to
$lasturl = "$ENV{'SCRIPT_NAME'}";
## Snif cookie, if present test for logged in status
require ("cookiesnif.nsp");
## If comes back dead a login prompt was called, kill current process
if ($exit eq '1') { exit; }
## else continue with process

## Check to see if the logged user is granted rights to this action script
if (($Cookies{'UserType'} eq "CMManage") || ($Cookies{'UserType'} eq "CMAdmin")) { $nextone = "1"; }
else {
	$noaccess = `cat noaccess.nsf`;
	print "$noaccess";	
	exit;
}

## Grab User Input
require ("parse_query.nsp");

## script's name
$script = "$ENV{'SCRIPT_NAME'}";
## grab admin date format
require ("date.nsp");

## get perl built dynamic DHTML menu js
my $MenuConfig = `cat js/menu_config.js`;
my $MenuConstructor = `cat js/menu_constructor.js`;
my $MenuConfig = "<script langauage=\"Javascript\">\n$MenuConfig\n</script>";
my $MenuConstructor = "<script langauage=\"Javascript\">\n$MenuConstructor\n</script>";

## get CM legal piece
$legal = `cat legal.nsf`;

## If SAVING
if (($FORM{'DROPIN'}) && ($FORM{'CopyID'})) {

## TOP HTML TEMPLATE
&topper;

	## Crumble Form Input to Variables
	$CopyID = "$FORM{'CopyID'}";
	$Title = "$FORM{'Title'}";
	$EmailSubject = "$FORM{'EmailSubject'}";
	$BodyText = "$FORM{'BodyText'}";
	$ActionUser = "$Cookies{'Username'}";

{
print <<EOF

<table width="95%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td width="50%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>View/Update Website Copy</b></font></td>
          <td align="right" width="50%">&nbsp;</td>
        </tr>
        <tr> 
          <td colspan="2"> 
            <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER">
              <tr bordercolor="#333366"> 
                <td width="50%" align="center" valign="top" height="250"> 
                  <table width="100%" border="0" cellspacing="0" cellpadding="5">
                    <tr> 
                      <td width="100%"><font face="verdana,arial,helvetica" size="1" color="#333366">
					  
EOF
}
	print "<center><br><b>Update Website Copy</b><br><br>The copy you just updated has been successfully saved to the system.<br><br><form><input type=\"button\" value=\"Back to Copy Main\" onClick=\"javascript:parent.location.href='change_copy.cgi'\" class=\"inputbut\"><br></center>";
	print "<br><br></font>";
	my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $sth = $dbh->prepare("UPDATE LOW_PRIORITY Copy 
							 SET Title='$Title', 
							 BodyText='$BodyText', 
							 EmailSubject='$EmailSubject', 
							 ModifiedBy='$ActionUser', 
							 ModifiedOn=Null 
							 WHERE CopyID='$CopyID'");
	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish; 
	$dbh->disconnect; 	
	
{
print <<EOF

                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
	  
EOF
}
	
## END PAGE TEMPLATE
&bottom;

exit;
}

## If VIEWING
elsif ($FORM{'CopyID'}) {

	## Crumble Form Input to Variables
	my $CopyID = "$FORM{'CopyID'}";
	my $ActionUser = "$Cookies{'Username'}";

	##----------->>> Grab user Account Information
	my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $count=0;
	my $sth = $dbh->prepare("SELECT * FROM Copy WHERE CopyID='$CopyID'");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		my $SavedTitle = $row[1];
		my $SavedBodyText = $row[2];
		my $SavedLinksTitle = $row[3];
		my $SavedLinks = $row[4];
		my $SavedEmailSubject = $row[5];
		my $SavedAddedBy = $row[6];
		my $SavedAddedOn = $row[7];
		my $SavedModifiedBy = $row[8];
		my $SavedModifiedOn = $row[9];
		## Re-Structure data as necessary
		my $AddYear = substr($SavedAddedOn, 0, 2);
		my $AddMonth = substr($SavedAddedOn, 2, 2);
		my $AddDay = substr($SavedAddedOn, 4, 2);
		my $ModYear = substr($SavedModifiedOn, 0, 2);
		my $ModMonth = substr($SavedModifiedOn, 2, 2);
		my $ModDay = substr($SavedModifiedOn, 4, 2);
		$count++;
##----------->>> IF user Account DELETED, Show user who deleted profile
if ($SavedDeletedBy != "" || $SavedDeletedBy != " " || $SavedDeletedOn > 0) {
	print "<b>Deleted By:</b>$SavedDeletedBy<br>";
	print "<b>Deleted On:</b> <input type=\"text\" name=\"DeletedOn\" size=\"7\" class=\"inputtext7\" value=\"$DelMonth/$DelDay/$DelYear\"><br>";
}
##----------->>> ELSE read User Account Profile
else {

{
print <<EOF

<html>
<head>
<title>Add User Account</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="admincss.cgi" Type="text/css">
<script language="Javascript">
// HTML TAGGING SCRIPT FOR HTML 4.0 COMPLIANT CHARACTERS ON ALL BROWSERS
// By Drlouie \@ NetMedia Solutions
// info\@NetMediaSol.com for help
// Copyright 2001 NetMedia Solutions
function htmlUsIn() {
	BodyText = document.change.BodyText.value;
	BodyText = BodyText.replace(/&reg;/g, "®");
	BodyText = BodyText.replace(/&#153;/g, "™");
	BodyText = BodyText.replace(/&copy;/g, "©");
	BodyText = BodyText.replace(/&#8216;/g, "‘");
	BodyText = BodyText.replace(/&#8216;/g, "'");
	BodyText = BodyText.replace(/&#34;/g, "\\"");
	BodyText = BodyText.replace(/\\n<br>/g, "\\n");
	document.change.BodyText.value = BodyText;

	Title = document.change.Title.value;
	Title = Title.replace(/&reg;/g, "®");
	Title = Title.replace(/&#153;/g, "™");
	Title = Title.replace(/&copy;/g, "©");
	Title = Title.replace(/&#8216;/g, "‘");
	Title = Title.replace(/&#8216;/g, "'");
	Title = Title.replace(/&#34;/g, "\\"");
	document.change.Title.value = Title;
	
	EmailSubject = document.change.EmailSubject.value;
	EmailSubject = EmailSubject.replace(/&reg;/g, "®");
	EmailSubject = EmailSubject.replace(/&#153;/g, "™");
	EmailSubject = EmailSubject.replace(/&copy;/g, "©");
	EmailSubject = EmailSubject.replace(/&#8216;/g, "‘");
	EmailSubject = EmailSubject.replace(/&#8216;/g, "'");
	EmailSubject = EmailSubject.replace(/&#34;/g, "\\"");
	document.change.EmailSubject.value = EmailSubject;
}

function htmlUsOut() {
	BodyText = document.change.BodyText.value;
	BodyText = BodyText.replace(/®/g, "&reg;");
	BodyText = BodyText.replace(/™/g, "&#153;");
	BodyText = BodyText.replace(/©/g, "&copy;");
	BodyText = BodyText.replace(/‘/g, "&#8216;");
	BodyText = BodyText.replace(/'/g, "&#8216;");
	BodyText = BodyText.replace(/\\"/g, "&#34;");
	BodyText = BodyText.replace(/\\n\\n/g, "<br><br>");
	BodyText = BodyText.replace(/\\n/g, "<br>");
	document.change.BodyText.value = BodyText;

	Title = document.change.Title.value;
	Title = Title.replace(/®/g, "&reg;");
	Title = Title.replace(/™/g, "&#153;");
	Title = Title.replace(/©/g, "&copy;");
	Title = Title.replace(/‘/g, "&#8216;");
	Title = Title.replace(/'/g, "&#8216;");
	Title = Title.replace(/\\"/g, "&#34;");
	document.change.Title.value = Title;
	
	EmailSubject = document.change.EmailSubject.value;
	EmailSubject = EmailSubject.replace(/®/g, "&reg;");
	EmailSubject = EmailSubject.replace(/™/g, "&#153;");
	EmailSubject = EmailSubject.replace(/©/g, "&copy;");
	EmailSubject = EmailSubject.replace(/‘/g, "&#8216;");
	EmailSubject = EmailSubject.replace(/'/g, "&#8216;");
	EmailSubject = EmailSubject.replace(/\\"/g, "&#34;");
	document.change.EmailSubject.value = EmailSubject;
}
</script>
<script language="Javascript">
// FORM CHECKER FUNCTIONS
// By Drlouie \@ NetMedia Solutions
// info\@NetMediaSol.com for help
// Copyright 2001 NetMedia Solutions

function checkForm() {
var missingdrop = "";
var thefirst = "";

// Check Common form fields
if (document.change.BodyText.value == "" || document.change.BodyText.value == " ") {
    missingdrop += "\\n     - Body Text is blank";
	thefirst = "BodyText";
}

if (document.change.Title.value == "" || document.change.Title.value == " ") {
    missingdrop += "\\n     - Page Title is blank";
	if (thefirst == "") { thefirst = "Title"; }
}

if (document.change.EmailSubject.value == "" || document.change.EmailSubject.value == " ") {
    missingdrop += "\\n     - Email Subject is blank";
	if (thefirst == "") { thefirst = "EmailSubject"; }
}

// If anything comes back wrong alert and detain form, else submit info
if (missingdrop != "") {
    missingdrop ="___________________________________________                   \\n\\n" + "  Sorry, I cannot process your request because the\\n  following fields are either blank or filled incorrectly:\\n" + "___________________________________________                   \\n\\n" +
    missingdrop + "\\n\\n___________________________________________                   " + "\\n\\n   To continue, check fields and submit form again!" + "\\n___________________________________________";
    alert(missingdrop);
	document.add(thefirst).focus();
    return false;
} 
else {
htmlUsOut();
return true;
}
}
</SCRIPT>
$MenuConfig
</head>

<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onLoad="javascript:htmlUsIn();">
$MenuConstructor
<table width="100%" border="0" cellspacing="0" cellpadding="0" background="images/top_tablebg_main.jpg" height="100">
  <tr> 
    <td width="30%" valign="top"><img src="images/illus_main.jpg" width="250" height="100"></td>
    <td width="25%">&nbsp;</td>
    <td align="left" valign="top"><img src="images/title_main.jpg" width="300" height="100"></td>
  </tr>
</table>
<form method="post" action="$script" name="change" onSubmit="return checkForm();">
  <table width="100%" border="0" cellpadding="0" cellspacing="0">
    <tr valign="top"> 
    <td width="20%">$legal</td>
      <td align="center" width="80%"> 
        <table width="95%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
            <td width="50%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>View/Update 
              Website Copy</b></font></td>
            <td align="right" width="50%">&nbsp;</td>
        </tr>
        <tr> 
          <td colspan="2"> 
              <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER" bordercolor="#333366">
                <tr bordercolor="#333366" valign="middle"> 
                  <td width="100%" align="center" height="50" class="tableBG"><font face="verdana,arial,helvetica" size="1" color="#EB0000">*If 
                    you have any questions please ask your Supervisor or Manager 
                    for help using the system or updating it's information.</font> 
                    <font face="verdana,arial,helvetica" size="1" color="#333366"></font><font face="verdana,arial,helvetica" size="1" color="#333366"></font></td>
              </tr>
              <tr bordercolor="#333366"> 
                  <td width="50%" align="center" valign="top" bordercolor="#333366"> 
                    <table width="100%" border="0" cellspacing="0" cellpadding="5">
                      <tr> 
                        <td width="100%" align="center" height="25" bgcolor="#F2F2F7" class="tableBG" colspan="2"><font face="verdana,arial,helvetica" size="2" color="#333366"><b>!LIVE! 
                          - Website Copy - !LIVE!</b></font></td>
                      </tr>
                      <tr> 
                        <td align="center" valign="top" colspan="2"><br>
                          <table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
                            <tr> 
                              <td width="348" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="100%" valign="top"> 
                                <table border="0" cellspacing="0" cellpadding="0" width="100%">
                                  <tr> 
                                    <td width="2%" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" bgcolor="#8F8FAB" width="96%" colspan="2"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Copy 
                                      Information</font></b></font></td>
                                    <td width="2%" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="4" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="20" align="center" width="48%" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Page 
                                      Title</b></font></td>
                                    <td height="20" align="center" width="48%" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Email 
                                      Subject</b></font></td>
                                    <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="25" align="center" width="48%" valign="middle"> 
                                      <input type="text" name="Title" size="35" class="inputtext35" value="$SavedTitle">
                                      <br>
                                      <input type="hidden" name="CopyID" value="$CopyID">
                                    </td>
                                    <td height="25" align="center" width="48%" valign="middle"> 
                                      <input type="text" size="35" class="inputtext35" name="EmailSubject" value="$SavedEmailSubject">
                                    </td>
                                    <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="20" align="center" colspan="2" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Body 
                                      Text</b> (Copy)</font></td>
                                    <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="65" align="center" colspan="2"> 
                                      <textarea name="BodyText" cols="50" class="textarea2" rows="5">$SavedBodyText</textarea>
                                    </td>
                                    <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="2%" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" align="center" width="96%" valign="top" bgcolor="#F2F2F7" colspan="2"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td width="2%" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                </table>
                              </td>
                              <td bgcolor="#8F8FAB" width="1" height="70"><img src="images/verticalbar.gif" width="1" height="25"></td>
                            </tr>
                            <tr> 
                              <td width="100%" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                          </table>
                          <br>
                        </td>
                      </tr>
                    </table>
                </td>
              </tr>
              <tr bordercolor="#333366" bgcolor="#F2F2F7"> 
                  <td align="center" valign="middle" height="45" width="100%" bordercolor="#333366" bgcolor="#F2F2F7"> 
                    <input type="submit" value="Save Changes" name="submit" class="inputbut">
                    <input type="reset" value="Reset Form" name="reset" class="inputbut">
                    &nbsp;</td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
        
      </td>
  </tr>
</table>
  <table width="100%" background="images/bot_frame_bg.jpg" height="56" align="center" cellpadding="0" cellspacing="0" border="0">
    <tr> 
      <td width="55%" align="left" height="56">&nbsp;</td>
    </tr>
  </table>


<input type="hidden" name="DROPIN" value="1">
</form>
</body>
</html>

EOF
}
}
exit;
}
}

## If no resident form processing calls are given continue
elsif ($FORM{'enformthee'}) {

{
print <<EOF

<html>
<head>
<title>Coastline Micro, Inc. - Shark Tank Admin System - Website Copy</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="admincss.cgi" Type="text/css">
$MenuConfig
</head>

<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
$MenuConstructor
<table width="100%" border="0" cellspacing="0" cellpadding="0" background="images/top_tablebg_main.jpg" height="100">
  <tr> 
    <td width="30%" valign="top"><img src="images/illus_main.jpg" width="250" height="100"></td>
    <td width="25%">&nbsp;</td>
    <td align="left" valign="top"><img src="images/title_main.jpg" width="300" height="100"></td>
  </tr>
</table>
<table width="100%" border="0" cellpadding="0" cellspacing="0">
  <tr valign="top"> 
    <td width="20%"><br>$legal</td>
    <td align="center" width="80%"> 


<table width="95%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
            
          <td width="50%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>View/Add/Update 
            Website Copy</b></font></td>
            <td align="right" width="50%">&nbsp;</td>
        </tr>
        <tr> 
          <td colspan="2"> 
            <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER" bordercolor="#333366">
              <tr valign="middle"> 
                        <td height="50" width="100%"> 
                          <center>
                            <font face="verdana,arial,helvetica" size="1" color="#EB0000">*If 
                            you have any questions please ask your Supervisor 
                            or Manager for help using the system or updating it's 
                            information.</font> 
                          </center>
                        </td>
                      </tr>
              <tr> 
                  <td width="50%" align="center" valign="top"> 
                    <table width="100%" border="0" cellspacing="0" cellpadding="5">
                    <tr> 
                      <td width="100%"><center>
                            <font face="verdana,arial,helvetica" size="1" color="#333366"> 
                            </font> <br>
<form method="post" action="$script" name="change">
                            <table width="500" border="0" cellspacing="0" cellpadding="0" align="center">
                              <tr> 
                                <td width="348" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                              </tr>
                              <tr> 
                                <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                                <td width="348" valign="top"> 
                                  <table width="500" border="0" cellspacing="0" cellpadding="0">
                                    <tr> 
                                      <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                      <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">View/Update Website Copy</font></b></font></td>
                                      <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    </tr>
                                    <tr> 
                                      <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                    </tr>
                                    <tr> 
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                      <td height="55" bgcolor="#F2F2F7" align="left"><font face="verdana,arial,helvetica" size="1" color="#333366">To 
                                        change or update the website copy for any of the listed pages, just select a title/item from the list, which would be the title also being used within the site. Then click 'View It!'</font></td>
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    </tr>
                                    <tr> 
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                      <td height="35" align="center"> 

                                        <select name="CopyID" class="inputtext">
EOF
}

	## Get list of CM reps
	use DBI;
	my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $sth = $dbh->prepare("SELECT * FROM Copy ORDER BY CopyID ASC");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
		while(@row = $sth->fetchrow_array) { 
		my $CopyID = $row[0];
		my $Title = $row[1];
		print "<option value=\"$CopyID\">$Title</option>";
	}
	$sth->finish;
	$dbh->disconnect;
	## print closing select tag

{
print <<EOF
</select>
&nbsp;&nbsp;
<input type="submit" value="View It!" class="inputbut">

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
                            </table></form>
<br>
          </td>
        </tr>
      </table>
          </td>
        </tr>
      </table>
          </td>
        </tr>
      </table>    </td>
  </tr>
</table>
<table width="100%" background="images/bot_frame_bg.jpg" height="56" align="center" cellpadding="0" cellspacing="0" border="0"><tr><td width="55%" align="left" height="56">&nbsp;</td></tr></table>
</body>
</html>

EOF
}

exit;
}

## if no useful calls present frameset
else {
{
print <<EOF

<html>
<head>
<title>Coastline Micro, Inc. - Administration System - $date</title>
</head>
<frameset rows="64,*" rows="*" border="0" framespacing="0"> 
<frame name="topOne" scrolling="NO" noresize src="topper.cgi" marginwidth="0" marginheight="0" frameborder="NO">
<frame name="botOne" src="$script?enformthee=1" frameborder="NO" marginheight="0" marginwidth="0" scrolling="AUTO">
</frameset>
<noframes><body bgcolor="#FFFFFF">
</body></noframes>
</html>

EOF
}
exit;
}

sub topper {
{
print <<EOF
<html>
<head>
<title>Website Copy</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="admincss.cgi" Type="text/css">
<SCRIPT LANGUAGE="JavaScript">
// QUICK CROSS-BROWSER MOUSE-OVER/OFF FUNCTIONS
// By Drlouie \@ NetMedia Solutions
// info\@NetMediaSol.com for help
// Copyright 2001 NetMedia Solutions

function imageOff(which,thisone) {
	var cual = 	"images/button_"+which+"_"+thisone+".gif";
	document.images[which].src = cual;
}
function imageOn(which,thisone) {
	var cual = 	"images/button_"+which+"_"+thisone+".gif";
	document.images[which].src = cual;
}
</script>
$MenuConfig
</head>

<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
$MenuConstructor
<table width="100%" border="0" cellspacing="0" cellpadding="0" background="images/top_tablebg_main.jpg" height="100">
  <tr> 
    <td width="30%" valign="top"><img src="images/illus_main.jpg" width="250" height="100"></td>
    <td width="25%">&nbsp;</td>
    <td align="left" valign="top"><img src="images/title_main.jpg" width="300" height="100"></td>
  </tr>
</table>
<table width="100%" border="0" height="100%" cellpadding="0" cellspacing="0">
  <tr valign="top"> 
    <td width="20%"><br>$legal</td>
    <td align="center" width="80%"> 

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
<table width="100%" background="images/bot_frame_bg.jpg" height="56" align="center" cellpadding="0" cellspacing="0" border="0"><tr><td width="55%" align="left" height="56">&nbsp;</td></tr></table>
</body>
</html>

EOF
}
}
exit;