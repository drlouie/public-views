#!/usr/bin/perl5 -w

###########################################################
# This CGI Software written by NetMedia Solutions         #
# http://www.netmediasol.com                              #
#                                                         #
# Software Written by:                                    #
# Luis Rodriguez (drlouie)                                #
#                                                         #
# If you have any questions or problems with this script  #
# Please contact me directly for help                     #
# drlouie@hapasol.com                                     #
###########################################################

## test location of request
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
	print "<html><head><title>Access Denied</title></head><body>";	
	print "Sorry, you do not have access to the press release administration system. To have your user access rights changed please contact your Coastline Micro Supervisor or Representative.";
	print "</body></html>";
	exit;
}

## Grab User Input
require ("parse_query.nsp");

## script's name
$script = "$ENV{'SCRIPT_NAME'}";

sub date {
# Define arrays for the day of the week and month of the year.           #
@days   = ('Sunday','Monday','Tuesday','Wednesday',
           'Thursday','Friday','Saturday');
@months = ('January','February','March','April','May','June','July',
           'August','September','October','November','December');
@months2 = ('01','02','03','04','05','06','07','08','09','10','11','12');
		   
# Get the current time and format the hour, minutes and seconds.  Add    #
# 1900 to the year to get the full 4 digit year.                         #
($sec,$min,$hour,$mday,$mon,$year,$wday) = (localtime(time))[0,1,2,3,4,5,6];
$time = sprintf("%02d:%02d:%02d",$hour,$min,$sec);
$year += 1900;

# Format the date.                                                       #
$date = "$months[$mon] $mday, $year";
}

##############################################################
########## ROUTE USER DEPENDING ON LINK/FORM INPUT ###########
##############################################################

################ IF LOOKING FOR THE ADMIN MAIN FRAME ################
if ($FORM{'mainadmin'}) { &mainadmin; }

################ IF LOOKING FOR THE ADMIN MAIN FRAME ################
if ($FORM{'jscript'}) { &jscript; }

################ IF ADDING A NEW RELEASE TO ARCHIVE ################
if ($FORM{'newRel'}) { &newRel; }

################ IF DELETING A RELEASE FROM ARCHIVE ################
if ($FORM{'deleRel'}) { &deleRel; }

################ IF VIEWING A PRESS RELEASE################
if ($FORM{'viewRel'}) { &viewRel; }

################ IF PUBLISHING A PRESS RELEASE################
if ($FORM{'pubRel'}) { &pubRel; }

################ IF ARCHIVING A PRESS RELEASE ################
if ($FORM{'unpubRel'}) { &unpubRel; }

################ IF CUSTOMIZING A PRESS RELEASE################
if ($FORM{'custRel'}) { &custRel; }

################ IF SAVING CUSTOMIZATIONS TO A PRESS RELEASE################
if ($FORM{'saveCustRel'}) { &saveCustRel; }

################ IF VIEWING ANY CLASS OF FOOTER ################
if ($FORM{'viewFoot'}) { &viewFoot; }

################ IF CUSTOMIZING A FOOTER ################
if ($FORM{'custFoot'}) { &custFoot; }

################ IF SAVING CHANGES TO A FOOTER ################
if ($FORM{'saveCustFoot'}) { &saveCustFoot; }

################ IF CREATING A NEW FOOTER ################
if ($FORM{'makeFoot'}) { &makeFoot; }

################ IF SAVING A NEW FOOTER ################
if ($FORM{'saveNewFoot'}) { &saveNewFoot; }

################ IF SAVING A NEW FOOTER ################
if ($FORM{'pressHelp'}) { &pressHelp; }

################ ELSE PARSE DEFULT ROUTINE ################
else { &first; }

###########################################################
################ DEFAULT ROUTINE/MAIN PAGE ################
###########################################################
sub first {

{
print <<EOF

<html>
<head>
<title>Coastline Micro, Inc. - Press Release Article Administration System - $date</title>
</head>
<frameset rows="64,*" rows="*" border="0" framespacing="0"> 
  <frame name="topOne" scrolling="NO" noresize src="topper.cgi" marginwidth="0" marginheight="0" frameborder="NO">
  <frame name="botOne" src="$script?mainadmin=1" frameborder="NO" marginheight="0" marginwidth="0" scrolling="AUTO">
</frameset>
<noframes><body bgcolor="#FFFFFF">
</body></noframes>
</html>

EOF
}
exit;
}

################################################################################
################ Admin Tool Internal JavaScript w/call function ################
################################################################################
sub jscript {
if ($FORM{'mousetable'} eq "1") {
{
print <<EOF

/*
Highlight Table Cells Script- 
Last updated: 99/01/21
© Dynamic Drive (www.dynamicdrive.com)
For full source code, installation instructions,
100's more DHTML scripts, and Terms Of
Use, visit dynamicdrive.com
*/

function runto(highlightcolor){
source=event.srcElement
if (source.tagName=="TR"||source.tagName=="TABLE")
return
while(source.tagName!="TD")
source=source.parentElement
if (source.style.backgroundColor!=highlightcolor&&source.id!="ignore")
source.style.backgroundColor=highlightcolor
}

function runback(originalcolor){
if (event.fromElement.contains(event.toElement)||source.contains(event.toElement)||source.id=="ignore")
return
if (event.toElement!=source)
source.style.backgroundColor=originalcolor
}

EOF
}
}

else {
&error('A valid script name was not specified...');
}
exit;
}

################################################################
################ ADMINISTRATION START/MAIN PAGE ################
################################################################
sub mainadmin {

{
print <<EOF
	
<HTML>
<HEAD>
<title>Coastline Micro, Inc. - Press Release Article Administration System - $date</title>
<script language="Javascript" src="$script?jscript=1&mousetable=1"></script>
<SCRIPT LANGUAGE="JavaScript">
//run new pop-up window
function runThis1(thistype) {
var formindex = document.router.release.selectedIndex;
var thisone = document.router.release.options[formindex].value;
window.open('$script?viewRel='+thisone+'','POLLS','width=550,height=595,scrollbars=yes');
}	

function runThis2(thistype) {
var formindex2 = document.router.arelease.selectedIndex;
var thisone2 = document.router.arelease.options[formindex2].value;
window.open('$script?viewRel='+thisone2+'','POLLS','width=550,height=595,scrollbars=yes');
}	

//run current window
function runForm(thistype) {
var formindex = document.router.release.selectedIndex;
var thisone = document.router.release.options[formindex].value;
location.href = "$script?"+thistype+"=1&release="+thisone+"";
}

//run current window
function runForm2(thistype) {
var formindex = document.router.arelease.selectedIndex;
var thisone = document.router.arelease.options[formindex].value;
if (thistype == "deleRel") {
	var agree=confirm("Are you sure you want to delete the selected article?\\n\\nPlease remember to leave at least one article in both the Live and Archived Press Release Article lists.");
	if (agree)
	location.href = "$script?"+thistype+"=1&arelease="+thisone+"";
	else
	nogo=1;
	}
else {
	location.href = "$script?"+thistype+"=1&arelease="+thisone+"";
	}
}

//run current window
function reload() {
parent.location.href = "$script";
}
</SCRIPT>
<!-- for navi -->
<LINK REL="STYLESHEET" HREF="admincss.cgi" Type="text/css">
</HEAD>
	<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<table width="100%" border="0" cellspacing="0" cellpadding="0" align="center" height="55">
  <tr valign="top">
  <td width="100%" align="right" valign="middle"><a href="$script?pressHelp=1"><font face="verdana" size="2">About SimPress</font></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
  </tr>
</table>
<TABLE border="0" width="100%" cellpadding="0" cellspacing="2" onMouseOver="runto('666666')" onMouseOut="runback('8F8FAB')" id="ignore">
	<TR id="ignore">
		<td height="18" align="center" bgcolor="#8F8FAB"><b><A HREF="$script?mainadmin=1"><font class="topnavi"><nobr>PRESS MAIN</nobr></font></A></b></td>    					
		<td height="18" align="center" bgcolor="#8F8FAB"><b><A HREF="$script?custRel=1"><font class="topnavi"><nobr>EDIT ARTICLE</nobr></font></A></b></td>    					
		<td height="18" align="center" bgcolor="#8F8FAB"><b><A HREF="$script?pubRel=1"><font class="topnavi"><nobr>PUBLISH ARTICLE</nobr></font></A></b></td>    					
		<td height="18" align="center" bgcolor="#8F8FAB"><b><A HREF="$script?unpubRel=1"><font class="topnavi"><nobr>ARCHIVE ARTICLE</nobr></font></A></b></td>    					
		<td height="18" align="center" bgcolor="#8F8FAB"><b><A HREF="$script?newRel=1"><font class="topnavi"><nobr>ADD NEW ARTICLE</nobr></font></A></b></td>    					
		<td height="18" align="center" bgcolor="#8F8FAB"><b><A HREF="$script?deleRel=1"><font class="topnavi"><nobr>DELETE ARTICLE</nobr></font></A></b></td>    					
	</TR>
</TABLE>
<br>
<form method="post" action="$script" name="router">
  <table border="1" cellspacing="0" cellpadding="0" align="center" bordercolor="#333366" width="500">
    <tr valign="top" bgcolor="#333366" align="center"> 
      <td height="35" valign="middle" colspan="2"><font face="verdana,arial,helvetica" size="2" color="#ffffff"><b>Press Release Administration System</b></font></td>
    </tr>
    <tr valign="top"> 
      <td width="100%"><br>
        <table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
          <tr> 
            <td><font face="verdana,arial,helvetica" size="1">Welcome to the Coastline Micro's 
              press release administration system. This system allows for you, 
              the site's press release article administrator, to add, delete, 
              modify and publish the company's press releases securely through 
              your web browser.<br>
              <br>
              <b>Application Highlights</b><br>
              <br>
              &nbsp;&nbsp;&nbsp;* Supports HTML/Plain Formatted Data<br>
              &nbsp;&nbsp;&nbsp;* Behind the scenes editing<br>
              &nbsp;&nbsp;&nbsp;* Customizable partner/company footers<br>
              &nbsp;&nbsp;&nbsp;* Sorting on the fly by Date<br>
              &nbsp;&nbsp;&nbsp;* Secure Non-HTTP data structure<br>
              <br>
              <b>Precautions</b><br>
              Please be sure to read all instructions before attemting to change 
              any of the system's data. All system function was completely tested 
              and thoroughly debugged. Yet, if you find any kind of problem with 
              this system please brief the Coastline Micro IT Director of the problem you 
              encountered.<br>
              <br>
              Also, please make sure you leave at least one article in both the 
              'Live Press Releases' and 'Archived Press Releases' lists at all 
              times. If you delete all articles from either list, you might encounter 
              problems down the road with data consistency.</font></td>
          </tr>
        </table>
        <br>
      </td>
    </tr>
    <tr valign="top"> 
      <td width="100%" align="center"> 
        <table width="100%" border="1" bordercolor="#333366" cellpadding="3" cellspacing="0">
          <tr bgcolor="#333366" align="left"> 
            <td width="50%" height="20" bgcolor="#333366" align="center"><font face="verdana,arial,helvetica" size="1" color="#ffffff"><b>Live 
              Press Releases</b></font></td>
          </tr>
          <tr> 
            <td width="50%" align="center" height="180" valign="top"> <br>
              <table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
                <tr> 
                  <td><font face="verdana,arial,helvetica" size="1"><b>Quick Instructions</b> 
                    <ul>
                      <li>To view an article, select an option from the list below 
                        and click 'View Selected Article'</li>
                      <li>To Archive an article (Make it NOT Live / Hide it from 
                        site users), select an option from the list below and 
                        click 'Archive Selected Article'</li>
                    </ul>
                    </font></td>
                </tr>
              </table>
              <select name="release">
EOF
}
## Capture LIVE PRESS RELEASES
$cstuff = "press/releases/releases.dat";
$thestuff = `cat $cstuff`;	
################# START parse form ##################
@lines = split(/:end\n/, $thestuff);
$count=1;
    foreach $line (@lines) {
	$count++;
	@pairs = split(/&&&/, $line);
    	foreach $pair (@pairs) {
			local($name, $value) = split(/===/, $pair);
        $name =~ tr/+/ /;
        $name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

        $value =~ tr/+/ /;
        $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

        $value =~ s/<!--(.|\n)*-->//g;
		
			$Saved{$name} = $value;
		}
   	$a = "$Saved{'title'}";
    $b = substr($a, 0, 30);     # ONLY 25 Characters
	print "<option value=\"$Saved{'file'}\">$Saved{'date'} - $b...";
	}
################# END parse form ##################

{
print <<EOF
              </select>
            </td>
          </tr>
        </table>
        <table width="100%" border="1" cellspacing="0" cellpadding="3" bordercolor="#333366" onMouseOver="runto('ebebeb')" onMouseOut="runback('white')">
          <tr>
            <td height="25" align="left">&nbsp;&nbsp;<font face="verdana,arial,helvetica" size="1"><a href="javascript:runThis1('viewRel')"><b>View 
              Selected Article</b></a></font></td>
          </tr>
          <tr>
            <td height="25" align="left">&nbsp;&nbsp;<font face="verdana,arial,helvetica" size="1"><a href="javascript:runForm('unpubRel')"><b>Archive 
              Selected Article</b></a></font></td>
          </tr>
        </table>
<!-- Start Releases in works -->
        <table width="100%" border="1" bordercolor="#333366" cellpadding="3" cellspacing="0">
          <tr bgcolor="#333366" align="left"> 
            <td width="50%" height="20" bgcolor="#333366" align="center"><font face="verdana,arial,helvetica" size="1" color="#ffffff"><b>Archived 
              Press Releases</b></font></td>
          </tr>
          <tr> 
            <td width="50%" align="center" height="240" valign="top"> <br>
              <table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
                <tr> 
                  <td><font face="verdana,arial,helvetica" size="1"><b>Quick Instructions</b> 
                    <ul>
                      <li>To View an article, select an option from the list below 
                        and click 'View Selected Article'</li>
                      <li>To Edit an article, select an option from the list below 
                        and click 'Edit Selected Article'</li>
                      <li>To Delete an article, select an option from the list 
                        below and click 'Delete Seleted Article'</li>
                      <li>To Publish an article, (Make it Live / Show it to site 
                        users), select an option fromt the list below and click 
                        'Publish Selected Article' </li>
                    </ul>
                    </font></td>
                </tr>
              </table>
              <select name="arelease">
EOF
}

################# START parse form ##################
## Capture ARCHIVED PRESS RELEASES
$cstuff2 = "press/releases/releases.arch";
$thestuff2 = `cat $cstuff2`;	
@lines = split(/:end\n/, $thestuff2);
$count=1;
    foreach $line (@lines) {
	$count++;
	@pairs = split(/&&&/, $line);
    	foreach $pair (@pairs) {
			local($name, $value) = split(/===/, $pair);
        $name =~ tr/+/ /;
        $name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

        $value =~ tr/+/ /;
        $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

        $value =~ s/<!--(.|\n)*-->//g;
		
			$Saved2{$name} = $value;
		}
   	$a1 = "$Saved2{'title'}";
    $b2 = substr($a1, 0, 30);     # ONLY 25 Characters
	print "<option value=\"$Saved2{'file'}\">$Saved2{'date'} - $b2...";
	}
################# END parse form ##################

{
print <<EOF
              </select>
            </td>
          </tr>
        </table>
        <table width="100%" border="1" cellspacing="0" cellpadding="3" bordercolor="#333366" onMouseOver="runto('ebebeb')" onMouseOut="runback('white')">
          <tr>
            <td height="25" align="left">&nbsp;&nbsp;<font face="verdana,arial,helvetica" size="1"><a href="javascript:runThis2('viewRel')"><b>View 
              Selected Article</b></a></font></td>
          </tr>
          <tr>
            <td height="25" align="left">&nbsp;&nbsp;<font face="verdana,arial,helvetica" size="1"><a href="javascript:runForm2('custRel')"><b>Edit 
              Selected Article</b></a></font></td>
          </tr>
          <tr>
            <td height="25" align="left">&nbsp;&nbsp;<font face="verdana,arial,helvetica" size="1"><a href="javascript:runForm2('deleRel')"><b>Delete 
              Selected Article</b></a></font></td>
          </tr>
          <tr>
            <td height="25" align="left">&nbsp;&nbsp;<font face="verdana,arial,helvetica" size="1"><a href="javascript:runForm2('pubRel')"><b>Publish 
              Selected Article</b></a></font></td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
  <br>
<table align="center" border="1" bgcolor="#8F8FAB" bordercolor="#333366" cellspacing="0" cellpadding="5" onMouseOver="runto('666666')" onMouseOut="runback('8F8FAB')"><tr><td width="100%" align="center"><input type="button" value="Reload Page" onClick="javascript:reload()"></td></tr></table>
</form>
	</BODY>
	</HTML>

EOF
}
exit;
}

####################################################
################ VIEW PRESS RELEASE ################
####################################################
sub viewRel {
$viewRel = "$FORM{'viewRel'}";
require ("press/releases/$viewRel.sms");

if ($myfoot != "") {
	require ("press/coastfoot/$myfoot.foot");
	$breakone = "<br><br>";
	$yourtitle = $foottitle;
	$yourlink = $footlink;
	$yourbody = $footbody;
	}
else { 
	$breakone = "";
	$yourtitle = "";
	$yourlink = "";
	$yourbody = "";
	}
		
{
print <<EOF

<html>
<head>
<title>Coastline Micro, Inc. - Press Release Article Administration System - $date</title>
</head>
<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<table cellpadding="2" cellspacing="0" border="0" width="95%" align="center">
<tr><td>
<font size="2" face="verdana,arial,helvetica"><b>$location - $date</b></font>
</td></tr>
<tr><td>
<br>
<font size="2" face="verdana,arial,helvetica"><b>$title</b>
<br>
$para1
$breakone
<b>$yourtitle</b><br>
$yourbody <a href="$yourlink" target="new">More Info-></a>

EOF
}

if ($partners eq "" || $partners eq " " ) { $no=1; }
else { 	
	@feetses = split(/,/, $partners);
		foreach $myfeet (@feetses) {
			require ("press/otherfoot/$myfeet.foot");
			print "<br><br>";
			print "<b>$foottitle</b><br>";
			print "$footbody <a href=\"$footlink\" target=\"new\">More Info-></a>";
	   	}
}

{
print <<EOF

<br><br>
<center>###
<br><br>
<font size="1">Coastline Micro, Inc. and the CM logo are trademarks and/or registered trademarks of Coastline Micro, Inc.<br>
All other names are trademarks and/or registered trademarks of their respective owners</font>
<br><br>
</center>
</font>
</td></tr>
</table>
</body>
</html>

EOF
}
exit;
}

#######################################################
################ ADD NEW PRESS RELEASE ################
#######################################################
sub newRel {
$title = "$FORM{'title'}";
$themonth = "$FORM{'themonth'}";
$theday = "$FORM{'theday'}";
$theyear = "$FORM{'theyear'}";

if ($themonth == "01") { $allmonth = "January"; }
elsif ($themonth == "02") { $allmonth = "February"; }
elsif ($themonth == "03") { $allmonth = "March"; }
elsif ($themonth == "04") { $allmonth = "April"; }
elsif ($themonth == "05") { $allmonth = "May"; }
elsif ($themonth == "06") { $allmonth = "June"; }
elsif ($themonth == "07") { $allmonth = "July"; }
elsif ($themonth == "08") { $allmonth = "August"; }
elsif ($themonth == "09") { $allmonth = "September"; }
elsif ($themonth == "10") { $allmonth = "October"; }
elsif ($themonth == "11") { $allmonth = "November"; }
else { $allmonth = "December"; }

# Define arrays for the day of the week and month of the year.           #
@days   = ('Sunday','Monday','Tuesday','Wednesday',
           'Thursday','Friday','Saturday');
@months = ('January','February','March','April','May','June','July',
           'August','September','October','November','December');
@months2 = ('01','02','03','04','05','06','07','08','09','10','11','12');
		   
# Get the current time and format the hour, minutes and seconds.  Add    #
# 1900 to the year to get the full 4 digit year.                         #
($sec,$min,$hour,$mday,$mon,$year,$wday) = (localtime(time))[0,1,2,3,4,5,6];
$time = sprintf("%02d:%02d:%02d",$hour,$min,$sec);
$year += 1900;



## if subject form field is being submitted, must be coming from the ADD A POLL FORM
if (($title) && ($themonth) && ($theday) && ($theyear)) {
		## read current count
		$countfile = "press/releases/count.dat";
		open(COUNT,"$countfile") || &error('can not write to $countfile');
   		$countme = <COUNT>;
		$countme++;
		close(COUNT);
		## write out current count on tracking file, count is used for press release filenames
		open(COUNT2,">$countfile") || &error('can not write to $countfile');
		flock(COUNT2, 2);
		print COUNT2 "$countme";
		flock(COUNT2, 8);
		close(COUNT2);
		## write out user input information into Archive Tracking File
		$archfile = "press/releases/releases.arch";
		$catarch = `cat $archfile`;
		open(ARCHIVE,">$archfile") || &error('can not write to $archfile');
		flock(ARCHIVE, 2);
		print ARCHIVE "sortby===$themonth$theday$theyear&&&year===year$theyear&&&date===$allmonth $theday, $theyear&&&title===$title&&&file===$countme:end\n";
		print ARCHIVE "$catarch";
		flock(ARCHIVE, 8);
		close(ARCHIVE);
		# CREATE NEW PRESS RELEASE FILE
		$newfile = "press/releases/$countme.sms";
		open(NEWONE,">$newfile") || &error('can not write default configuration file');
		flock(NEWONE, 2);
		print NEWONE "#!/usr/bin/perl5 -w\n\n";
		print NEWONE "\$date = \"$date\";\n\n";
		print NEWONE "\$title = \"$title\";\n\n";
		print NEWONE "\$data = \"This is the default data.\";\n\n";
		print NEWONE "\$location = \"Irvine, CA\";\n\n";
		print NEWONE "\@partners = (\"vigon\",\"evolve\");\n\n";
		print NEWONE "##return = true\n";
		print NEWONE "1;";
		flock(NEWONE, 8);
		close(NEWONE);
		chmod (0755, $newfile)  || &error('cant chmod $newfile');
{
print <<EOF
	
<HTML>
<HEAD>
<title>Coastline Micro, Inc. - Press Release Article Administration System - $date</title>
<script language="Javascript" src="$script?jscript=1&mousetable=1"></script>
<SCRIPT LANGUAGE="JavaScript">
//run current window
function runForm() {
parent.location.href = "$script";
}
</SCRIPT>
</HEAD>
<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<form>
  <br>
  <table border="1" cellspacing="0" cellpadding="0" align="center" bordercolor="#333366" width="500">
    <tr valign="top"> 
      <td width="100%" align="center"> 
        <table width="498" border="1" bordercolor="#333366" cellpadding="3" cellspacing="0">
          <tr bgcolor="#333366" align="center"> 
            <td width="50%" height="20" bgcolor="#333366" align="center"><font face="verdana,arial,helvetica" size="2" color="#FFFFFF"><b> 
              <font color="#ffffff">Press Release Addition Successful</font></b></font></td>
          </tr>
          <tr> 
            <td width="50%" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1"><br>Your new press release, <b>$title</b>, has been successfully added to the press release archive.<br><br></font></td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
<br>
<table align="center" border="1" bgcolor="#8F8FAB" bordercolor="#333366" cellspacing="0" cellpadding="5" onMouseOver="runto('666666')" onMouseOut="runback('8F8FAB')"><tr><td width="100%" align="center"><input type="button" onClick="javascript:runForm();" value="Back to Start Page"></td></tr></table>
</form>
	</BODY>
	</HTML>

EOF
}
exit;
}
## if TITLE and DATE form fields are NOT being submitted, parse the ADD A POLL FORM
else {
&date;
{
print <<EOF
	
<HTML>
<HEAD>
<title>Coastline Micro, Inc. - Press Release Article Administration System - $date</title>
<script language="Javascript" src="$script?jscript=1&mousetable=1"></script>
<SCRIPT LANGUAGE="JavaScript">
//Check Search field for completion
function checkForm() {
	var formindex = document.router.themonth.selectedIndex;
	var thisone = document.router.themonth.options[formindex].value;
	if (thisone == "unselected") {
	alert('Please choose a Month for your Press Release.');		
	document.router.themonth.focus();
	return false;
	}	

	var formindex2 = document.router.theday.selectedIndex;
	var thisone2 = document.router.theday.options[formindex2].value;
	if (thisone2 == "unselected") {
	alert('Please choose a Day for your Press Release.');		
	document.router.theday.focus();
	return false;
	}	

	var formindex3 = document.router.theyear.selectedIndex;
	var thisone3 = document.router.theyear.options[formindex3].value;
	if (thisone3 == "unselected") {
	alert('Please choose a Year for your Press Release.');		
	document.router.theyear.focus();
	return false;
	}	
		
	else if (document.router.title.value == "") {
	alert('The title is missing, please type a title for your new press release.');
	document.router.title.focus();
	return false;
	}	

	else {
	return true;
	}
}
</SCRIPT>
</HEAD>
<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<form method="GET" name="router" action="$script" onSubmit="return checkForm();">
<input type="hidden" value="1" name="newRel">
  <br>
  <table border="1" cellspacing="0" cellpadding="0" align="center" bordercolor="#333366" width="500">
    <tr valign="top"> 
      <td width="100%" align="center"> 
        <table width="100%" border="1" bordercolor="#333366" cellpadding="3" cellspacing="0">
          <tr bgcolor="#333366" align="center"> 
            <td width="50%" height="35" bgcolor="#333366" align="center"><font face="verdana,arial,helvetica" size="2" color="#FFFFFF"><b> 
              <font color="#ffffff">Add Press Release Article</font></b></font></td>
          </tr>
          <tr> 
            <td width="50%" align="left" valign="middle"> <br>
              <table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
                <tr> 
                  <td><font face="verdana,arial,helvetica" size="1"><b>Instructions</b><br>
                    Please read the following instructions carefully before beginning. 
                    Feel free to use as many words as you deem necessary for your 
                    new press release article's title. Try to make it as catchy 
                    as possible, for the title is what the user is first presented 
                    within your site's press release main page. Keep in mind that 
                    a well-planned and worded title will certainly catch more 
                    attention that a poorly written one. 
                    <ul>
                      <li>Ok, now start by selecting the date for your new press release article using the drop-down menus below.</li>
                      <li>Now, type in your title in the 'Title' field. <b>Example:</b> 
                        <i>Coastline Micro Moves Operations to new Irvine facility</i></li>
                      <li>Finally, click 'Add Release' to add your new press release article to the system archive.</li>
                    </ul>
                    </font></td>
                </tr>
              </table>
              <br>
            </td>
          </tr>
        </table>
        <table width="100%" border="1" cellspacing="0" cellpadding="3" bordercolor="#333366">
          <tr> 
            <td bgcolor="#333366" align="center" height="20"><font face="verdana,arial,helvetica" size="1" color="#ffffff"><b>Date</b></font></td>
          </tr>
          <tr> 
            <td align="center" id="ignore"><select name="themonth"><option selected value="unselected">Month<option value="01">January<option value="02">February<option value="03">March<option value="04">April<option value="05">May<option value="06">June<option value="07">July<option value="08">August<option value="09">September<option value="10">October<option value="11">November<option value="12">December</select><select name="theday"><option selected value="unselected">Day<option value="01">01<option value="02">02<option value="03">03<option value="04">04<option value="05">05<option value="06">06<option value="07">07<option value="08">08<option value="09">09<option value="10">10<option value="11">11<option value="12">12<option value="13">13<option value="14">14<option value="15">15<option value="16">16<option value="17">17<option value="18">18<option value="19">19<option value="20">20<option value="21">21<option value="22">22<option value="23">23<option value="24">24<option value="25">25<option value="26">26<option value="27">27<option value="28">28<option value="29">29<option value="30">30<option value="31">31</select><select name="theyear"><option selected value="unselected">Year<option value="2000">2000<option value="2001">2001<option value="2002">2002<option value="2003">2003<option value="2004">2004<option value="2005">2005<option value="2006">2006</select></td>
          </tr>
          <tr> 
            <td bgcolor="#333366" align="center" height="20"><font face="verdana,arial,helvetica" size="1" color="#ffffff"><b>Title</b></font></td>
          </tr>
          <tr> 
            <td align="center" id="ignore"><input type="text" value="" name="title"></td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
<br>
<table align="center" border="1" bgcolor="#8F8FAB" bordercolor="#333366" cellspacing="0" cellpadding="5" onMouseOver="runto('666666')" onMouseOut="runback('8F8FAB')"><tr><td width="100%" align="center"><input type="submit" value="Add Release"></td></tr></table>
</form>
	</BODY>
	</HTML>

EOF
}
}
exit;
}

######################################################
################ DELETE PRESS RELEASE ################
######################################################
sub deleRel {
$thisfile = "$FORM{'arelease'}";

## if subject form field is being submitted, must be coming from the ADD A POLL FORM
if ($thisfile) {
		## write out user input information into Archive Tracking File
		$archfile = "press/releases/releases.arch";
		$catarch = `cat $archfile`;
		## open and lock archive file for usage
		open(ARCHIVER,">$archfile") || &error('can not write to $archfile');
		flock(ARCHIVER, 2);
		################# START parse form ##################
		## Capture ARCHIVED PRESS RELEASES
		@lines = split(/:end\n/, $catarch);
		$count=0;
    		foreach $line (@lines) {
			$count++;
			if ($line =~ $thisfile) {
				@pairs = split(/&&&/, $line);
		    	foreach $pair (@pairs) {
				local($name, $value) = split(/===/, $pair);
        		$name =~ tr/+/ /;
        		$name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

        		$value =~ tr/+/ /;
        		$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

        		$value =~ s/<!--(.|\n)*-->//g;
		
				$Saved2{$name} = $value;
				}
   				$deadtitle = "$Saved2{'title'}";
   				$deaddate = "$Saved2{'date'}";
			
				$unlinked = "press/releases/$thisfile.sms";
				unlink($unlinked) || &error('cant delete $unlinked');
{
print <<EOF
	
<HTML>
<HEAD>
<title>Coastline Micro, Inc. - Press Release Article Administration System - $date</title>
<script language="Javascript" src="$script?jscript=1&mousetable=1"></script>
<SCRIPT LANGUAGE="JavaScript">
//run current window
function runForm() {
parent.location.href = "$script";
}
</SCRIPT>
</HEAD>
<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<form>
<input type="hidden" value="1" name="deleRel">
  <br>
  <table border="1" cellspacing="0" cellpadding="0" align="center" bordercolor="#333366" width="500">
    <tr valign="top"> 
      <td width="100%" align="center"> 
        <table width="498" border="1" bordercolor="#333366" cellpadding="3" cellspacing="0">
          <tr bgcolor="#333366" align="center"> 
            <td width="50%" height="35" bgcolor="#333366" align="center"><font face="verdana,arial,helvetica" size="2" color="#FFFFFF"><b> 
              <font color="#ffffff">Archived Press Release Deleted Successfully</font></b></font></td>
          </tr>
          <tr> 
            <td width="50%" align="left" valign="middle"><br>
              <table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
                <tr> 
                  <td><font face="verdana,arial,helvetica" size="1">You have deleted 
                    the archived press release titled: <b>$deadtitle</b>, which 
                    was created on <b>$deaddate</b></font></td>
                </tr>
              </table>
              <br>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
<br>
<table align="center" border="1" bgcolor="#8F8FAB" bordercolor="#333366" cellspacing="0" cellpadding="5" onMouseOver="runto('666666')" onMouseOut="runback('8F8FAB')"><tr><td width="100%" align="center"><input type="button" onClick="javascript:runForm();" value="Back to Start Page"></td></tr></table>
</form>
	</BODY>
	</HTML>

EOF
}
			}
			else {
				print ARCHIVER "$line:end\n";
			}
			}
		################# END parse form ##################
		## close the archive file and unlock it
		flock(ARCHIVER, 8);
		close(ARCHIVER);
		exit;
}
## if TITLE and DATE form fields are NOT being submitted, parse the ADD A POLL FORM
else {
{
print <<EOF
	
<HTML>
<HEAD>
<title>Coastline Micro, Inc. - Press Release Article Administration System - $date</title>
<script language="Javascript" src="$script?jscript=1&mousetable=1"></script>
<SCRIPT LANGUAGE="JavaScript">
//run current window
function checkForm() {
	var agree=confirm("Are you sure you want to delete the selected article?\\n\\nPlease remember to leave at least one article in both the Live and Archived Press Release Article lists.");
	if (agree)
	return true;
	else
	return false;
}
</SCRIPT>
</HEAD>
<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<form method="GET" name="router" action="$script" onSubmit="return checkForm();">
<input type="hidden" value="1" name="deleRel">
  <br>
  <table border="1" cellspacing="0" cellpadding="0" align="center" bordercolor="#333366" width="500">
    <tr valign="top"> 
      <td width="100%" align="center"> 
        <table width="100%" border="1" bordercolor="#333366" cellpadding="3" cellspacing="0">
          <tr bgcolor="#333366" align="center"> 
            <td width="50%" height="35" bgcolor="#333366" align="center"><font face="verdana,arial,helvetica" size="2" color="#FFFFFF"><b> 
              <font color="#ffffff">Delete Press Release Instructions</font></b></font></td>
          </tr>
          <tr> 
            <td width="50%" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1"> 
              </font><br>
              <table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
                <tr> 
                  <td><font face="verdana,arial,helvetica" size="1"><b>Instructions</b><br>
                    Please read the following instructions carefully before beginning. <br><br><center><font color="red">Please remember to leave at least one article in the Archive.</font></center>
<ul>
                      <li>Select the press release article you would like to delete 
                        from the 'Archived Press Releases' list. </li>
                      <li>Then click 'Delete Selected Article' to automatically 
                        delete the selected press release article from the system.</li>
                    </ul>
                    </font> </td>
                </tr>
              </table>
              <br>
            </td>
          </tr>
        </table>
<table width="100%" border="1" bordercolor="#333366" cellpadding="3" cellspacing="0">
          <tr bgcolor="#333366" align="left"> 
            <td width="50%" height="20" bgcolor="#333366" align="center"><font face="verdana,arial,helvetica" size="1" color="#ffffff"><b>Archived Press Releases</b></font></td>
          </tr>
          <tr> 
            <td width="50%" align="center" height="50"> 
              <select name="arelease">
EOF
}

################# START parse form ##################
## Capture ARCHIVED PRESS RELEASES
$cstuff2 = "press/releases/releases.arch";
$thestuff2 = `cat $cstuff2`;	
@lines = split(/:end\n/, $thestuff2);
$count=1;
    foreach $line (@lines) {
	$count++;
	@pairs = split(/&&&/, $line);
    	foreach $pair (@pairs) {
			local($name, $value) = split(/===/, $pair);
        $name =~ tr/+/ /;
        $name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

        $value =~ tr/+/ /;
        $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

        $value =~ s/<!--(.|\n)*-->//g;
		
			$Saved2{$name} = $value;
		}
   	$a1 = "$Saved2{'title'}";
    $b2 = substr($a1, 0, 39);     # ONLY 25 Characters
	print "<option value=\"$Saved2{'file'}\">$Saved2{'date'} - $b2...";
	}
################# END parse form ##################

{
print <<EOF
              </select>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
<br>
<table align="center" border="1" bgcolor="#8F8FAB" bordercolor="#333366" cellspacing="0" cellpadding="5" onMouseOver="runto('666666')" onMouseOut="runback('8F8FAB')"><tr><td width="100%" align="center">
        <input type="submit" value="Delete Selected Article">
      </td></tr></table>
</form>
	</BODY>
	</HTML>

EOF
}
}
exit;
}

#######################################################
################ PUBLISH PRESS RELEASE ################
#######################################################
sub pubRel {
$thisfile = "$FORM{'arelease'}";

## if subject form field is being submitted, must be coming from the ADD A POLL FORM
if ($thisfile) {
		## write out user input information into Archive Tracking File
		$archfile = "press/releases/releases.arch";
		$catarch = `cat $archfile`;
		################# START parse form ##################
		## Capture ARCHIVED PRESS RELEASES
		@lines = split(/:end\n/, $catarch);
		$count=0;
    		foreach $line (@lines) {
			$count++;
			if ($line =~ $thisfile) {
				@pairs = split(/&&&/, $line);
		    	foreach $pair (@pairs) {
				local($name, $value) = split(/===/, $pair);
        		$name =~ tr/+/ /;
        		$name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

        		$value =~ tr/+/ /;
        		$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

        		$value =~ s/<!--(.|\n)*-->//g;
		
				$Saved2{$name} = $value;
				}
				$newtitle = "$Saved2{'title'}";
   				$newdate = "$Saved2{'date'}";
				## open and lock archive file for usage
				$relfile = "press/releases/releases.dat";
				$catRel = `cat $relfile`;
				open(RELEASE,">$relfile") || &error('can not write to $relfile');
				flock(RELEASE, 2);
				print RELEASE "$catRel";
				print RELEASE "$line:end\n";
				## close the release file and unlock it
				flock(RELEASE, 8);
				close(RELEASE);
{
print <<EOF
	
	<HTML>
	<HEAD>
<title>Coastline Micro, Inc. - Press Release Article Administration System - $date</title>
<script language="Javascript" src="$script?jscript=1&mousetable=1"></script>
<SCRIPT LANGUAGE="JavaScript">
//run current window
function runForm() {
parent.location.href = "$script";
}
</SCRIPT>
</HEAD>
<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<form>
<input type="hidden" value="1" name="pubRel">
  <br>
  <table border="1" cellspacing="0" cellpadding="0" align="center" bordercolor="#333366" width="500">
    <tr valign="top"> 
      <td width="100%" align="center"> 
        <table width="100%" border="1" bordercolor="#333366" cellpadding="3" cellspacing="0">
          <tr bgcolor="#333366" align="center"> 
            <td width="50%" height="35" bgcolor="#333366" align="center"><font face="verdana,arial,helvetica" size="2" color="#FFFFFF"><b> 
              <font color="#ffffff">Press Release Article Published Sucessfully</font></b></font></td>
          </tr>
          <tr> 
            <td width="50%" align="left" valign="middle"> <br>
              <table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
                <tr> 
                  <td><font face="verdana,arial,helvetica" size="1">You have sucessfully 
                    published the press release titled: <b>$newtitle</b>, which 
                    was created on <b>$newdate</b>.</font></td>
                </tr>
              </table>
              <br>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
<br>
<table align="center" border="1" bgcolor="#8F8FAB" bordercolor="#333366" cellspacing="0" cellpadding="5" onMouseOver="runto('666666')" onMouseOut="runback('8F8FAB')"><tr><td width="100%" align="center"><input type="button" onClick="javascript:runForm();" value="Back to Start Page"></td></tr></table>
</form>
	</BODY>
	</HTML>

EOF
}
			}
			else {
				$archfile2 = "press/releases/releases.arch2";
				$catArch2 = `cat $archfile2`;
				## open and lock archive file for usage
				open(ARCHIVER,">$archfile2") || &error('can not write to $archfile2');
				flock(ARCHIVER, 2);
				print ARCHIVER "$catArch2";
				print ARCHIVER "$line:end\n";
				## close the archive file and unlock it
				flock(ARCHIVER, 8);
				close(ARCHIVER);
			}
			use File::Copy;
			copy("press/releases/releases.arch2", "press/releases/releases.arch") || &error('cant copy press/releases/releases.arch2');
			}
		################# END parse form ##################
			open(ARCHIVER,">$archfile2") || &error('can not write to $archfile2');
			flock(ARCHIVER, 2);
			print ARCHIVER "";
			flock(ARCHIVER, 8);
			close(ARCHIVER);
		exit;
}
## if TITLE and DATE form fields are NOT being submitted, parse the ADD A POLL FORM
else {
{
print <<EOF
	
	<HTML>
	<HEAD>
<title>Coastline Micro, Inc. - Press Release Article Administration System - $date</title>
<script language="Javascript" src="$script?jscript=1&mousetable=1"></script>
</HEAD>
<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<form method="GET" name="router" action="$script">
<input type="hidden" value="1" name="pubRel">
  <br>
  <table border="1" cellspacing="0" cellpadding="0" align="center" bordercolor="#333366" width="500">
    <tr valign="top"> 
      <td width="100%" align="center"> 
        <table width="100%" border="1" bordercolor="#333366" cellpadding="3" cellspacing="0">
          <tr bgcolor="#333366" align="center"> 
            <td width="50%" height="35" bgcolor="#333366" align="center"><font face="verdana,arial,helvetica" size="2" color="#FFFFFF"><b> 
              <font color="#ffffff">Publish Press Release</font></b></font></td>
          </tr>
          <tr> 
            <td width="50%" align="left" valign="middle"><br>
              <table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
                <tr> 
                  <td><font face="verdana,arial,helvetica" size="1"><b>Instructions</b><br>
                    Please read the following instructions carefully before beginning. <br><br><center><font color="red">Please remember to leave at least one article in the Archive.</font></center>
                    </font>
                    <ul>
                      <li><font face="verdana,arial,helvetica" size="1">Select 
                        the press release article you would like to publish(make 
                        it live to the user) from the 'Archived Press Releases' 
                        list. </font></li>
                      <li><font face="verdana,arial,helvetica" size="1">Then click 
                        'Publish Selected Article' to publish the selected press 
                        release article. When you publish an article the site 
                        users will automatically be able to view the article.</font></li>
                    </ul>
                  </td>
                </tr>
              </table>
              <br>
            </td>
          </tr>
        </table>
<table width="100%" border="1" bordercolor="#333366" cellpadding="3" cellspacing="0">
          <tr bgcolor="#333366" align="left"> 
            <td width="50%" height="20" bgcolor="#333366" align="center"><font face="verdana,arial,helvetica" size="1" color="#ffffff"><b>Archived Press Releases</b></font></td>
          </tr>
          <tr> 
            <td width="50%" align="center" height="50"> 
              <select name="arelease">
EOF
}

################# START parse form ##################
## Capture ARCHIVED PRESS RELEASES
$cstuff2 = "press/releases/releases.arch";
$thestuff2 = `cat $cstuff2`;	
@lines = split(/:end\n/, $thestuff2);
$count=1;
    foreach $line (@lines) {
	$count++;
	@pairs = split(/&&&/, $line);
    	foreach $pair (@pairs) {
			local($name, $value) = split(/===/, $pair);
        $name =~ tr/+/ /;
        $name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

        $value =~ tr/+/ /;
        $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

        $value =~ s/<!--(.|\n)*-->//g;
		
			$Saved2{$name} = $value;
		}
   	$a1 = "$Saved2{'title'}";
    $b2 = substr($a1, 0, 39);     # ONLY 25 Characters
	print "<option value=\"$Saved2{'file'}\">$Saved2{'date'} - $b2...";
	}
################# END parse form ##################

{
print <<EOF
              </select>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
<br>
<table align="center" border="1" bgcolor="#8F8FAB" bordercolor="#333366" cellspacing="0" cellpadding="5" onMouseOver="runto('666666')" onMouseOut="runback('8F8FAB')"><tr><td width="100%" align="center">
        <input type="submit" value="Publish Selected Article">
      </td></tr></table>
</form>
	</BODY>
	</HTML>

EOF
}
}
exit;
}

#######################################################
################ PUBLISH PRESS RELEASE ################
#######################################################
sub unpubRel {
$thisfile = "$FORM{'release'}";

## if $thisfile is being submitted
if ($thisfile) {
		## write out user input information into LIVE Tracking File
		$relfile = "press/releases/releases.dat";
		$catRel = `cat $relfile`;
		################# START parse form ##################
		## Capture LIVE PRESS RELEASES
		@lines = split(/:end\n/, $catRel);
		$count=0;
    		foreach $line (@lines) {
			$count++;
			if ($line =~ $thisfile) {
				@pairs = split(/&&&/, $line);
		    	foreach $pair (@pairs) {
				local($name, $value) = split(/===/, $pair);
        		$name =~ tr/+/ /;
        		$name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

        		$value =~ tr/+/ /;
        		$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

        		$value =~ s/<!--(.|\n)*-->//g;
		
				$Saved2{$name} = $value;
				}
				$oldtitle = "$Saved2{'title'}";
   				$olddate = "$Saved2{'date'}";
				## open and lock archive file for usage
				$archfile = "press/releases/releases.arch";
				$catArch = `cat $archfile`;
				open(ARCH,">$archfile") || &error('can not write to $archfile');
				flock(ARCH, 2);
				print ARCH "$catArch";
				print ARCH "$line:end\n";
				## close the release file and unlock it
				flock(ARCH, 8);
				close(ARCH);
{
print <<EOF
	
	<HTML>
	<HEAD>
<title>Coastline Micro, Inc. - Press Release Article Administration System - $date</title>
<script language="Javascript" src="$script?jscript=1&mousetable=1"></script>
<SCRIPT LANGUAGE="JavaScript">
//run current window
function runForm() {
parent.location.href = "$script";
}
</SCRIPT>
</HEAD>
<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<form>
<input type="hidden" value="1" name="unpubRel">
  <br>
  <table border="1" cellspacing="0" cellpadding="0" align="center" bordercolor="#333366" width="500">
    <tr valign="top"> 
      <td width="100%" align="center"> 
        <table width="498" border="1" bordercolor="#333366" cellpadding="3" cellspacing="0">
          <tr bgcolor="#333366" align="center"> 
            <td width="50%" height="35" bgcolor="#333366" align="center"><font face="verdana,arial,helvetica" size="2" color="#FFFFFF"><b> 
              <font color="#ffffff">Press Release Archived Successfully</font></b></font></td>
          </tr>
          <tr> 
            <td width="50%" align="left" valign="middle"><br>
              <table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
                <tr> 
                  <td><font face="verdana,arial,helvetica" size="1">You have sucessfully 
                    archived the press release titled: <b>$oldtitle</b>, which 
                    was created on <b>$olddate</b>.</font></td>
                </tr>
              </table>
              <br>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
<br>
<table align="center" border="1" bgcolor="#8F8FAB" bordercolor="#333366" cellspacing="0" cellpadding="5" onMouseOver="runto('666666')" onMouseOut="runback('8F8FAB')"><tr><td width="100%" align="center"><input type="button" onClick="javascript:runForm();" value="Back to Start Page"></td></tr></table>
</form>
	</BODY>
	</HTML>

EOF
}
			}
			else {
				$datfile2 = "press/releases/releases.dat2";
				$catDat2 = `cat $datfile2`;
				## open and lock archive file for usage
				open(DATER,">$datfile2") || &error('can not write to $datfile2');
				flock(DATER, 2);
				print DATER "$catDat2";
				print DATER "$line:end\n";
				## close the archive file and unlock it
				flock(DATER, 8);
				close(DATER);
			}
			use File::Copy;
			copy("press/releases/releases.dat2", "press/releases/releases.dat") || &error('cant copy press/releases/releases.dat2');
			}
		################# END parse form ##################
			open(DATER,">$datfile2") || &error('can not write to $datfile2');
			flock(DATER, 2);
			print DATER "";
			flock(DATER, 8);
			close(DATER);
		exit;
}
## if $thisone is not being input parse form
else {
{
print <<EOF
	
	<HTML>
	<HEAD>
<title>Coastline Micro, Inc. - Press Release Article Administration System - $date</title>
<script language="Javascript" src="$script?jscript=1&mousetable=1"></script>
</HEAD>
<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<form method="GET" name="router" action="$script">
<input type="hidden" value="1" name="unpubRel">
  <br>
  <table border="1" cellspacing="0" cellpadding="0" align="center" bordercolor="#333366" width="500">
    <tr valign="top"> 
      <td width="100%" align="center"> 
        <table width="100%" border="1" bordercolor="#333366" cellpadding="3" cellspacing="0">
          <tr bgcolor="#333366" align="center"> 
            <td width="50%" height="35" bgcolor="#333366" align="center"><font face="verdana,arial,helvetica" size="2" color="#FFFFFF"><b> 
              <font color="#ffffff">Archive Press Release</font></b></font></td>
          </tr>
          <tr> 
            <td width="50%" align="left" valign="middle"> <br>
              <table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
                <tr> 
                  <td><font face="verdana,arial,helvetica" size="1"><b>Instructions</b><br>
                    Please read the following instructions carefully before beginning. <br><br><center><font color="red">Please remember to always have at least one Live press release article available.</font></center>
                    </font> 
                    <ul>
                      <li><font face="verdana,arial,helvetica" size="1">Select 
                        the press release article you would like to archive(make 
                        it NOT live to the user) from the 'Live Press Releases' 
                        list. </font></li>
                      <li><font face="verdana,arial,helvetica" size="1">Then click 
                        'Archive Selected Article' to archive the selected press 
                        release article. When you archive an article the site 
                        user will no longer be able to see the article.</font></li>
                    </ul>
                  </td>
                </tr>
              </table>
              <br>
            </td>
          </tr>
        </table>
<table width="100%" border="1" bordercolor="#333366" cellpadding="3" cellspacing="0">
          <tr bgcolor="#333366" align="left"> 
            <td width="50%" height="20" bgcolor="#333366" align="center"><font face="verdana,arial,helvetica" size="1" color="#ffffff"><b>Live Press Releases</b></font></td>
          </tr>
          <tr> 
            <td width="50%" align="center" height="50"> 
              <select name="release">
EOF
}

################# START parse form ##################
## Capture LIVE PRESS RELEASES
$cstuff2 = "press/releases/releases.dat";
$thestuff2 = `cat $cstuff2`;	
@lines = split(/:end\n/, $thestuff2);
$count=1;
    foreach $line (@lines) {
	$count++;
	@pairs = split(/&&&/, $line);
    	foreach $pair (@pairs) {
			local($name, $value) = split(/===/, $pair);
        $name =~ tr/+/ /;
        $name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

        $value =~ tr/+/ /;
        $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

        $value =~ s/<!--(.|\n)*-->//g;
		
			$Saved2{$name} = $value;
		}
   	$a1 = "$Saved2{'title'}";
    $b2 = substr($a1, 0, 39);     # ONLY 25 Characters
	print "<option value=\"$Saved2{'file'}\">$Saved2{'date'} - $b2...";
	}
################# END parse form ##################

{
print <<EOF
              </select>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
<br>
<table align="center" border="1" bgcolor="#8F8FAB" bordercolor="#333366" cellspacing="0" cellpadding="5" onMouseOver="runto('666666')" onMouseOut="runback('8F8FAB')"><tr><td width="100%" align="center">
        <input type="submit" value="Archive Selected Article">
      </td></tr></table>
</form>
	</BODY>
	</HTML>

EOF
}
}
exit;
}

#########################################################
################ CUSTOMIZE PRESS RELEASE ################
#########################################################
sub custRel {
$thisfile = "$FORM{'arelease'}";

## if $thisfile is being submitted
if ($thisfile) {
		require ("press/releases/$thisfile.sms");
		$para1 =~ s/<br>\n/\n/g;		
		$para1 =~ s/<br>/\n/g;				
		
		## check coastfooters to see if it already contains a footer
		if ($myfoot != "") { 
		require ("press/coastfoot/$myfoot.foot");
			$tablescript1 = "onMouseOver=\"runto('ebebeb')\" onMouseOut=\"runback('white')\"";
			$myfootstuff = "<a href=\"#\" onClick=\"javascript:window.open('$script?viewFoot=coastfoot&whichone=$myfoot.foot','FOOT','width=550,height=595,scrollbars=yes');\">$foottitle</a><input type=\"hidden\" name=\"myfoot\" value=\"$myfoot\">";
			$thefoottitle = $foottitle;
			}
		## check coastfooters to see if it already contains a footer
		else { 
			$tablescript1 = "";
			$myfootstuff = "None Selected<input type=\"hidden\" name=\"myfoot\" value=\"\">";
			}
		
		## use ARCHIVE Tracking File
		$archfile = "press/releases/releases.arch";
		$catArch = `cat $archfile`;
		################# START parse form ##################
		## Capture the necessary ARCHIVED PRESS RELEASE
		@lines = split(/:end\n/, $catArch);
		$count=0;
    		foreach $line (@lines) {
			$count++;
			if ($line =~ $thisfile) {
				@pairs = split(/&&&/, $line);
		    	foreach $pair (@pairs) {
				local($name, $value) = split(/===/, $pair);
        		$name =~ tr/+/ /;
        		$name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

        		$value =~ tr/+/ /;
        		$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

        		$value =~ s/<!--(.|\n)*-->//g;
		
				$Saved2{$name} = $value;
				}
				$title = "$Saved2{'title'}";
   				$date = "$Saved2{'date'}";
   				$file = "$Saved2{'file'}";
{
print <<EOF
	
	<HTML>
	<HEAD>
<title>Coastline Micro, Inc. - Press Release Article Administration System - $date</title>
<script language="Javascript" src="$script?jscript=1&mousetable=1"></script>
<SCRIPT LANGUAGE="JavaScript">
//run current window
function checkForm() {
if (document.router.location.value == "" || document.router.location.value == " ") {
	alert('Please type in the article release location. Example: Irvine, CA');
	document.router.location.focus();
	return false;
}	
if (document.router.para1.value == "" || document.router.para1.value == " ") {
	alert('Please type in your press release\\'s main section data.');
	document.router.para1.focus();
	return false;
}	
var strValues = "";
	var boxLength = document.router.otherfoot2.length;
	var count = 0;
	if (boxLength != 0) {
	for (i = 0; i < boxLength; i++) {
		if (count == 0) {
			strValues = document.router.otherfoot2.options[i].value;
		}
		else {
			strValues = strValues + "," + document.router.otherfoot2.options[i].value;
		}
	count++;
   }
}
if (strValues.length == 0) {
	return true;
}
else {
	document.router.otherfeet.value = strValues;
	return true;
   }
}

function runForm() {
parent.location.href = "$script";
}

//run current window
function runForm2(thistype) {
var formindex2 = document.router.release.selectedIndex;
var thisone2 = document.router.release.options[formindex2].value;
location.href = "$script?"+thistype+"=1&release="+thisone2+"";
}

function runThis1(thistype) {
var formindex1 = document.router.coastfoot.selectedIndex;
var thisone1 = document.router.coastfoot.options[formindex1].value;
if (thisone1 == "none") { alert('You must select an item from the Coastline Micro Available Footers to use this function.'); }
else { window.open('$script?'+thistype+'=coastfoot&whichone='+thisone1+'','FOOT','width=550,height=595,scrollbars=yes'); }
}	

function runThis2(thistype) {
var formindex2 = document.router.otherfoot.selectedIndex;
var thisone2 = document.router.otherfoot.options[formindex2].value;
if (thisone2 == "none") { alert('You must select an item from the Partner/Client Available Footers to use this function.'); }
else { window.open('$script?'+thistype+'=otherfoot&whichone='+thisone2+'','FOOT','width=550,height=595,scrollbars=yes'); }
}	

function switch1() {
var formindex = document.router.coastfoot.selectedIndex;
var thisone = document.router.coastfoot.options[formindex].value;
if (thisone == "none") { alert('You must select an item from the Coastline Micro Available Footers to use this function.'); }
else { 
document.router.myfoot.value=thisone;
document.router.refresh.value=1;
var strValues = "";
var boxLength = document.router.otherfoot2.length;
var count = 0;
if (boxLength != 0) {
for (i = 0; i < boxLength; i++) {
if (count == 0) {
strValues = document.router.otherfoot2.options[i].value;
}
else {
strValues = strValues + "," + document.router.otherfoot2.options[i].value;
}
count++;
   }
}
if (strValues.length == 0) {
document.router.submit();
}
else {
document.router.otherfeet.value = strValues;
document.router.submit();
   }
}
}	

function refresh1() {
if (document.router.location.value == "" || document.router.location.value == " ") {
	alert('Please type in the article release location. Example: Irvine, CA');
	document.router.location.focus();
}	
if (document.router.para1.value == "" || document.router.para1.value == " ") {
	alert('Please type in your press release\\'s main section data.');
	document.router.para1.focus();
}	
document.router.refresh.value=1;
var strValues = "";
var boxLength = document.router.otherfoot2.length;
var count = 0;
if (boxLength != 0) {
for (i = 0; i < boxLength; i++) {
if (count == 0) {
strValues = document.router.otherfoot2.options[i].value;
}
else {
strValues = strValues + "," + document.router.otherfoot2.options[i].value;
}
count++;
   }
}
if (strValues.length == 0) {
document.router.submit();
}
else {
document.router.otherfeet.value = strValues;
document.router.submit();
   }
}	

function makeFoot(which) {
	window.open('$script?makeFoot='+which+'','FOOT','width=550,height=595,scrollbars=yes');
}	

function jumpFoot() {
otherfoot2 = document.forms[0].otherfoot2;
otherfoot = document.forms[0].otherfoot; 
var sizer = otherfoot2.length;
for(var i = 0; i < otherfoot.length; i++) {
if ((otherfoot.options[i] != null) && (otherfoot.options[i].selected)) {
var there = false;
for(var count = 0; count < sizer; count++) {
if (otherfoot2.options[count] != null) {
if (otherfoot.options[i].text == otherfoot2.options[count].text) {
there = true;
break;
      }
   }
}
if (there != true) {
otherfoot2.options[sizer] = new Option(otherfoot.options[i].text); 
otherfoot2.options[sizer].value = otherfoot.options[i].value;
sizer++;
         }
      }
   }
}

function killFoot() {
var otherfoot2  = document.forms[0].otherfoot2;
var sizer = otherfoot2.options.length;
for(var i = (sizer-1); i >= 0; i--) {
if ((otherfoot2.options[i] != null) && (otherfoot2.options[i].selected == true)) {
otherfoot2.options[i] = null;
      }
   }
}

function checkFeet() {
otherfoot2 = document.forms[0].otherfoot2;
otherfoot = document.forms[0].otherfoot; 
var sizer = otherfoot2.length;
for(var i = 0; i < otherfoot.length; i++) {
for(var count = 0; count < sizer; count++) {
if (otherfoot.options[i] != null) {
if (otherfoot2.options[count] != null) {
if (otherfoot2.options[count].text == otherfoot.options[i].value) {
otherfoot2.options[count] = new Option(otherfoot.options[i].text); 
otherfoot2.options[count].value = otherfoot.options[i].value;
sizer++;
      		}
   		  }
		}
      }
   }
}
// End -->
</SCRIPT>
</HEAD>
<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onLoad="javascript:checkFeet();">
<form method="POST" action="$script" name="router" onSubmit="return checkForm();">
  <br>
  <table border="1" cellspacing="0" cellpadding="0" align="center" bordercolor="#333366" width="500">
    <tr valign="top"> 
      <td width="100%" align="center"> 
        <table width="498" border="1" bordercolor="#333366" cellpadding="3" cellspacing="0">
          <tr bgcolor="#333366" align="center"> 
            <td width="50%" height="35" bgcolor="#333366" align="center"><font face="verdana,arial,helvetica" size="2" color="#FFFFFF"><b>Edit<font color="#ffffff"> 
              Press Release</font></b></font></td>
          </tr>
          <tr> 
            <td width="50%" align="left" valign="middle"><br>
              <table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
                <tr> 
                  <td><font face="verdana,arial,helvetica" size="1"><b>Instructions</b><br>
                    <br>
                    Please make sure you read all the instructions below thoroughly 
                    before attemping to change any of the system's information. 
                    This will aid in publishing a nicely laid out press release 
                    article time and time again.<br>
                    <br>
                    <b><br>
                    <br>
                    Article Title<br>
                    </b>$title<br>
                    <br>
                    <b>Article Date</b>&nbsp;&nbsp;<br>
                    $date<br>
					<br>
                    <b>Release Location</b>&nbsp;&nbsp;<br>
                    <input type="text" name="location" value="$location"></font></td>
                </tr>
              </table>
              
              <br>
            </td>
          </tr>
        </table>
        <table width="100%" border="1" bordercolor="#333366" cellpadding="3" cellspacing="0">
          <tr bgcolor="#333366"> 
            <td width="50%" height="20" bgcolor="#333366" align="center"><font face="verdana,arial,helvetica" size="1" color="#ffffff"><b>Article 
              Main Section</b></font></td>
          </tr>
          <tr> 
            <td width="50%" align="center" height="20" valign="top"> <br>
              <table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
                <tr> 
                  <td><font face="verdana,arial,helvetica" size="1"><b>Instructions</b><br>
                    <br>
                    Its simple to edit your press release article. All you have 
                    to do is drop your custom HTML/Plain-Text article body text 
                    into the text field below. <br>
                    <br>
                    * Keep in mind that this application was built smart and will 
                    try to convert all HTML and Plain-Text into functional program 
                    code on the fly. Yet, in some cases, if using both HTML and 
                    Plain-Text in your article body, you might see some problems 
                    in the formatting of the article as you view it from the admin 
                    panel or the user-end. To fix this kind of problem, just have 
                    a knowledgable HTML coder look through your article, he/she 
                    should be able to figure a SIMPLE work-around for the problem 
                    at hand.</font></td>
                </tr>
              </table>
              <br>
              <textarea name="para1" cols="50" rows="10">$para1</textarea>
              <br>
            </td>
          </tr>
		</table>
        <table width="100%" border="1" bordercolor="#333366" cellpadding="3" cellspacing="0">
          <tr bgcolor="#333366"> 
            <td width="50%" height="20" bgcolor="#333366" align="center"><font face="verdana,arial,helvetica" size="1" color="#ffffff"><b>Coastline Micro 
              Footer </b></font></td>
          </tr>
          <tr> 
            <td width="50%" align="center" height="50"> <br>
              <table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
                <tr> 
                  <td colspan="3"><font face="verdana,arial,helvetica" size="1"><b>Instructions</b><br>
                    <br>
                    The Coastline Micro Footer is used to describe Coastline Micro to the user reading 
                    a press release article. Please follow the current footer 
                    format in order to keep all footers looking and the same throughout 
                    all articles.<br>
                    <br>
                    Choose a pre-defined Coastline Micro Footer for this press release 
                    article. If you don't see an Coastline Micro Footer that fits this 
                    specific press release article's topic, you can very easily 
                    create a new one that better fits. <br>
                    <ul>
                      <li>To choose an Coastline Micro Footer to use with this press release 
                        article just select your footer of choice from the 'Available 
                        Footers' list below and click the '&gt;&gt;&gt;' button.</li>
                      <li>To add a new Coastline Micro Footer click 'Create New Footer'. 
                        Don't worry you will not lose any of the information on 
                        this screen.</li>
                      <li>To preview an Coastline Micro Footer just select the footer you 
                        would like to preview from the 'Available Footers' list 
                        below and click 'View Selected Footer'</li>
                      <li>To edit an Coastline Micro Footer just select the article you 
                        would like to edit from the 'Available Footers' list below 
                        and click 'Edit Selected Footer'</li>
                      <li>If you have created a new Coastline Micro Footer but do not see 
                        it in this list yet, just click 'Refresh Listing' to be 
                        able to view your new footer.</li>
                    </ul>
                    </font></td>
                </tr>
                <tr> 
                  <td width="40%" valign="top"> 
                    <table width="100%" border="1" cellspacing="0" cellpadding="3" bordercolor="#333366">
                      <tr> 
                        <td height="25" align="center" bgcolor="#333366"><font face="verdana,arial,helvetica" size="1" color="#ffffff"><b>Available 
                          Footers </b></font></td>
                      </tr>
                      <tr> 
                        <td height="50" align="center"> 
                          <select name="coastfoot" style="width:170;"><option value="none">None Selected
EOF
}
	
	$userstuffs = "press/coastfoot";
	opendir(DIR, $userstuffs) or die "can't opendir $userstuffs $!";
	while (defined($file = readdir(DIR))) {
	next if $file =~ /^\.\.?$/; ## skip . and .. directories
	next if $file =~ /count.dat\.?$/; ## skip count.dat file, a config file
	next if $file =~ /.htaccess\.?$/; ## skip .htaccess files, the Managers config files
	next if $file =~ /.htpasswd\.?$/; ## skip .htpasswd files, the Managers config files
	if ($file =~ $myfoot) { $foottitle = $thefoottitle; }
	else { require ("press/coastfoot/$file"); }
	$myfoottitle = substr($foottitle, 0, 25);   
	print "<option value=\"$file\">$myfoottitle</option>";
	} 

{
print <<EOF
                          </select>
                        </td>
                      </tr>
                    </table>
                    <table width="100%" border="1" cellspacing="0" cellpadding="3" bordercolor="#333366" onMouseOver="runto('ebebeb')" onMouseOut="runback('white')">
                      <tr> 
                        <td height="25" align="left">&nbsp;&nbsp;<font face="verdana,arial,helvetica" size="1"><a href="javascript:runThis1('viewFoot')"><b>View 
                          Selected Footer</b></a></font></td>
                      </tr>
                      <tr> 
                        <td height="25" align="left">&nbsp;&nbsp;<font face="verdana,arial,helvetica" size="1"><a href="javascript:runThis1('custFoot')"><b>Edit 
                          Selected Footer</b></a></font></td>
                      </tr>
                      <tr> 
                        <td height="25" align="left">&nbsp;&nbsp;<font face="verdana,arial,helvetica" size="1"><a href="javascript:makeFoot('coastfoot')"><b>Create New Footer</b></a></font></td>
                      </tr>
                      <tr> 
                        <td height="25" align="left">&nbsp;&nbsp;<font face="verdana,arial,helvetica" size="1"><a href="javascript:refresh1();"><b>Refresh Listing</b></a></font></td>
                      </tr>
                    </table>
                  </td>
                  <td width="20%" align="center">
                    <table align="center" border="1" bgcolor="#8F8FAB" bordercolor="#333366" cellspacing="0" cellpadding="5" onMouseOver="runto('666666')" onMouseOut="runback('8F8FAB')">
                      <tr>
                        <td width="100%" align="center">
                          <input type="Button" value=">>>" onClick="javascript:switch1();">
                        </td>
                      </tr>
                    </table>
                  </td>
                  <td width="40%" valign="top"> 
                    <table width="100%" border="1" cellspacing="0" cellpadding="3" bordercolor="#333366" $tablescript1>
                      <tr id="ignore"> 
                        <td height="25" align="center" bgcolor="#333366" id="ignore"><font face="verdana,arial,helvetica" size="1" color="#ffffff"><b>Footer in Use</b></font></td>
                      </tr>
                      <tr id="ignore"> 
                        <td height="50" align="center"><font face="verdana,arial,helvetica" size="1"><b>&nbsp;$myfootstuff&nbsp;</b></font></td>
                      </tr>
                    </table>
                  </td>
                </tr>
              </table>
              <br>
            </td>
          </tr>
        </table>
        <table width="100%" border="1" bordercolor="#333366" cellpadding="3" cellspacing="0">
          <tr bgcolor="#333366"> 
            <td width="50%" height="20" bgcolor="#333366" align="center"><font face="verdana,arial,helvetica" size="1" color="#ffffff"><b>Partner/Client 
              Footer</b></font></td>
          </tr>
          <tr> 
            <td width="50%" align="center" height="50"> <br>
              <table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
                <tr> 
                  <td colspan="3"><font face="verdana,arial,helvetica" size="1"><b><font face="verdana,arial,helvetica" size="1">Instructions</font></b><br>
                    <br>
                    The Partner/Client Footer is used to describe a Partner/Client 
                    company to the user reading a press release article. You should 
                    only need to implement a Partner/Client Footer when you describe 
                    or elaborate on a Partner/Client company. Please follow the 
                    current footer format in order to keep all footers looking 
                    and the same throughout all articles.<br>
                    <br>
                    Choose as many Partner/Client Footers for this press release 
                    article as you deem necessary. If you don't see an Partner/Client 
                    Footer that fits this specific press release article, you 
                    can very easily create a new one that does by clicking 'Create 
                    New Footer'. <br>
                    </font> 
                    <ul>
                      <li><font face="verdana,arial,helvetica" size="1">To choose 
                        your Partner/Client Footer(s) for this press release article 
                        just select your footer of choice from the 'Available 
                        Footers' list below and click the '&gt;&gt;&gt;' button. 
                        Feel free to use as many as you deem necessary, but still 
                        try to keep the number of Partner/Client Footers within 
                        your article to a bare minimum.</font></li>
                      <li><font face="verdana,arial,helvetica" size="1">To remove 
                        an item from the 'Footer(s) in Use' list just click the 
                        '&lt;&lt;&lt;' button. Please remember to save your changes 
                        when you add or delete from the 'Footer(s) in Use' list.</font></li>
                      <li><font face="verdana,arial,helvetica" size="1">To add 
                        a new Partner/Client Footer click 'Create New Footer'. 
                        Don't worry you will not lose any of the information on 
                        this screen.</font></li>
                      <li><font face="verdana,arial,helvetica" size="1">To preview 
                        a Partner/Client Footer just select the footer you would 
                        like to preview from the 'Available Footers' list below 
                        and click 'View Selected Footer'</font></li>
                      <li><font face="verdana,arial,helvetica" size="1">To edit 
                        a Partner/Client Footer just select the article you would 
                        like to edit from the 'Available Footers' list below and 
                        click 'Edit Selected Footer'</font></li>
                      <li><font face="verdana,arial,helvetica" size="1">If you 
                        have created a new Partner/Client Footer but do not see 
                        it in this list yet, just click 'Refresh Listing' to be 
                        able to view your new footer.</font></li>
                    </ul>
                    </td>
                </tr>
                <tr> 
                  <td width="40%" valign="top"> 
                    <table width="100%" border="1" cellspacing="0" cellpadding="3" bordercolor="#333366">
                      <tr> 
                        <td height="25" align="center" bgcolor="#333366"><font face="verdana,arial,helvetica" size="1" color="#ffffff"><b>Available 
                          Footers </b></font></td>
                      </tr>
                      <tr> 
                        <td height="50" align="center"> 
                          <select name="otherfoot" size="5" style="width:170;" multiple>
EOF
}
	
## Define all folders/files within Pollstuff. Then uncall the files and name the folders.
## This will come up with list of names of all available polls
	$userstuffs = "press/otherfoot";
	opendir(DIR, $userstuffs) or die "can't opendir $userstuffs $!";
	while (defined($file = readdir(DIR))) {
	next if $file =~ /^\.\.?$/; ## skip . and .. directories
	next if $file =~ /count.dat\.?$/; ## skip count.dat file, a config file
	next if $file =~ /.htaccess\.?$/; ## skip .htaccess files, the Managers config files
	next if $file =~ /.htpasswd\.?$/; ## skip .htpasswd files, the Managers config files
	require ("press/otherfoot/$file");
	$foottitle = substr($foottitle, 0, 25);   
	print "<option value=\"$file\">$foottitle</option>"; 
	} 
	$foottitle = "";
{ 
print <<EOF
                          </select>
                        </td>
                      </tr>
                    </table>
                    <table width="100%" border="1" cellspacing="0" cellpadding="3" bordercolor="#333366" onMouseOver="runto('ebebeb')" onMouseOut="runback('white')">
                      <tr> 
                        <td height="25" align="left">&nbsp;&nbsp;<font face="verdana,arial,helvetica" size="1"><a href="javascript:runThis2('viewFoot')"><b>View 
                          Selected Footer</b></a></font></td>
                      </tr>
                      <tr> 
                        <td height="25" align="left">&nbsp;&nbsp;<font face="verdana,arial,helvetica" size="1"><a href="javascript:runThis2('custFoot')"><b>Edit 
                          Selected Footer</b></a></font></td>
                      </tr>
                      <tr> 
                        <td height="25" align="left">&nbsp;&nbsp;<font face="verdana,arial,helvetica" size="1"><a href="javascript:makeFoot('otherfoot')"><b>Create New Footer</b></a></font></td>
                      </tr>
                      <tr> 
                        <td height="25" align="left">&nbsp;&nbsp;<font face="verdana,arial,helvetica" size="1"><a href="javascript:refresh1();"><b>Refresh Listing</b></a></font></td>
                      </tr>
                    </table>
                  </td>
                  <td width="20%" align="center"> 
                    <table align="center" border="1" bgcolor="#8F8FAB" bordercolor="#333366" cellspacing="0" cellpadding="5" onMouseOver="runto('666666')" onMouseOut="runback('8F8FAB')">
                      <tr> 
                        <td width="100%" align="center" valign="middle"> 
                          <input type="Button" value=" >>> "  onClick="javascript:jumpFoot();"><br><br>
						  <input type="Button" value=" <<< "  onClick="javascript:killFoot();">
                        </td>
                      </tr>
                    </table>
                  </td>
                  <td width="40%" valign="top"> 
                    <table width="100%" border="1" cellspacing="0" cellpadding="3" bordercolor="#333366">
                      <tr> 
                        <td height="25" align="center" bgcolor="#333366"><font face="verdana,arial,helvetica" size="1" color="#ffffff"><b>Footer(s) in Use</b></font></td>
                      </tr>
                      <tr> 
                        <td height="50" align="center">
<select name="otherfoot2" size="5" style="width:170;" multiple>

EOF
}

if ($partners eq "" || $partners eq " " ) { $no=1; }
else { 	
	@feets = split(/,/, $partners);
	   foreach $feet (@feets) {
			print "<option value=\"$feet.foot\">$feet.foot</option>";
	   }
}

{
print <<EOF

						</select>
						</td>
                      </tr>
                    </table>
                  </td>
                </tr>
              </table>
              <br>
              <br>
              <br>
            </td>
          </tr>
        </table>
        
      </td>
    </tr>
  </table>
<br>
<table align="center" border="1" bgcolor="#8F8FAB" bordercolor="#333366" cellspacing="0" cellpadding="5" onMouseOver="runto('666666')" onMouseOut="runback('8F8FAB')"><tr><td width="100%" align="center"><input type="Submit" value="Save Changes"></td></tr></table>
<br>
<table align="center" border="1" bgcolor="#8F8FAB" bordercolor="#333366" cellspacing="0" cellpadding="5" onMouseOver="runto('666666')" onMouseOut="runback('8F8FAB')"><tr><td width="100%" align="center"><input type="button" onClick="javascript:runForm();" value="Back to Start Page"></td></tr></table>
<input type="hidden" value="1" name="saveCustRel">
<input type="hidden" value="$date" name="date">
<input type="hidden" value="$thisfile" name="file">
<input type="hidden" name="title" value="$title">
<input type="hidden" name="refresh" value="0">
<input type="hidden" name="otherfeet" value="">
</form>
	</BODY>
	</HTML>

EOF
}
}
else { $next = 1; }
}
exit;
}
## if $thisone is not being input parse form
else {
{
print <<EOF
	
	<HTML>
	<HEAD>
<title>Coastline Micro, Inc. - Press Release Article Administration System - $date</title>
<script language="Javascript" src="$script?jscript=1&mousetable=1"></script>
</HEAD>
<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<form method="GET" name="router" action="$script">
<input type="hidden" value="1" name="custRel">
  <br>
  <table border="1" cellspacing="0" cellpadding="0" align="center" bordercolor="#333366" width="500">
    <tr valign="top"> 
      <td width="100%" align="center"> 
        <table width="100%" border="1" bordercolor="#333366" cellpadding="3" cellspacing="0">
          <tr bgcolor="#333366" align="center"> 
            <td width="50%" height="35" bgcolor="#333366" align="center"><font face="verdana,arial,helvetica" size="2" color="#FFFFFF"><b>Edit<font color="#ffffff"> 
              Press Release Instructions</font></b></font></td>
          </tr>
          <tr> 
            <td width="50%" align="left" valign="middle"><br>
              <table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
                <tr> 
                  <td><font face="verdana,arial,helvetica" size="1"><b>Instructions</b><br>
                    Please read the following instructions carefully before beginning. 
                    </font> 
                    <ul>
                      <li><font face="verdana,arial,helvetica" size="1">Select 
                        the press release article you would like to edit from 
                        the 'Archived Press Releases' list below. </font></li>
                      <li><font face="verdana,arial,helvetica" size="1">Then click 
                        'Edit Selected Article' to begin editing the selected 
                        article. Don't worry, the site user is not able to see 
                        this press release article until you decide to publish 
                        it.</font></li>
                    </ul>
                  </td>
                </tr>
              </table>
              <br>
            </td>
          </tr>
        </table>
        <table width="100%" border="1" bordercolor="#333366" cellpadding="3" cellspacing="0">
          <tr bgcolor="#333366" align="left"> 
            <td width="50%" height="20" bgcolor="#333366" align="center"><font face="verdana,arial,helvetica" size="1" color="#ffffff"><b>Archived 
              Press Releases</b></font></td>
          </tr>
          <tr> 
            <td width="50%" align="center" height="50"> 
              <select name="arelease">
EOF
}

################# START parse form ##################
## Capture LIVE PRESS RELEASES
$cstuff2 = "press/releases/releases.arch";
$thestuff2 = `cat $cstuff2`;	
@lines = split(/:end\n/, $thestuff2);
$count=1;
    foreach $line (@lines) {
	$count++;
	@pairs = split(/&&&/, $line);
    	foreach $pair (@pairs) {
			local($name, $value) = split(/===/, $pair);
        $name =~ tr/+/ /;
        $name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

        $value =~ tr/+/ /;
        $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

        $value =~ s/<!--(.|\n)*-->//g;
		
			$Saved2{$name} = $value;
		}
   	$a1 = "$Saved2{'title'}";
    $b2 = substr($a1, 0, 39);     # ONLY 25 Characters
	print "<option value=\"$Saved2{'file'}\">$Saved2{'date'} - $b2...";
	}
################# END parse form ##################

{
print <<EOF
              </select>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
<br>
<table align="center" border="1" bgcolor="#8F8FAB" bordercolor="#333366" cellspacing="0" cellpadding="5" onMouseOver="runto('666666')" onMouseOut="runback('8F8FAB')"><tr><td width="100%" align="center">
        <input type="submit" value="Edit Selected Article">
      </td></tr></table>
</form>
	</BODY>
	</HTML>

EOF
}
}
exit;
}

##################################################################
################ SAVE PRESS RELEASE CUSTOMIZATIONS################
##################################################################
sub saveCustRel {

$thedate = "$FORM{'date'}";
$thefile = "$FORM{'file'}";
$thefoot = "$FORM{'myfoot'}";
$otherfoot = "$FORM{'otherfeet'}";
$refresh = "$FORM{'refresh'}";

if ($thefoot =~ ".foot") { $thefoot = substr($thefoot, 0, 8); }
else { $thefoot = $thefoot; }

if ($otherfoot != "" && $otherfoot != " ") {
@feets = split(/,/, $otherfoot);
	foreach $foot (@feets) {
		if ($foot =~ ".foot") { 
			$foot = substr($foot, 0, 8); 
			push(@partners,"$foot"); 
		}
	else { 
		push(@partners,"$foot"); 
		}
	}
	$partners = join(',', @partners);
}
else {
	$partners = "";
}

## for escaping the dollar sign, common perl variable sign
$dollar='\$';

$title = "$FORM{'title'}";
$title =~ s/[\$]+/$dollar/g;
$title =~ s/^[^\S\n]+//gm;
$title =~ s/\n\n/<br><br>/g;
$title =~ s/"/\\"/g;
$title =~ s/@/\\@/g;

$para1 = "$FORM{'para1'}";
$para1 =~ s/[\$]+/$dollar/g;
$para1 =~ s/^[^\S\n]+//gm;
$para1 =~ s/\n\n/<br><br>/g;
$para1 =~ s/"/\\"/g;
$para1 =~ s/@/\\@/g;

$location = "$FORM{'location'}";
$location =~ s/[\$]+/$dollar/g;
$location =~ s/^[^\S\n]+//gm;
$location =~ s/\n\n/<br><br>/g;
$location =~ s/"/\\"/g;
$location =~ s/@/\\@/g;

	## read current count
	# CREATE NEW PRESS RELEASE FILE
	$thisfile = "press/releases/$thefile.sms";
	unlink($thisfile) || &error('cant delete $thisfile');
	open(THEONE,">$thisfile") || &error('can not write to $thisfile');
	flock(THEONE, 2);
	print THEONE "#!/usr/bin/perl5 -w\n\n";
	print THEONE "\$date = \"$thedate\";\n\n";
	print THEONE "\$title = \"$title\";\n\n";
	print THEONE "\$para1 = \"$para1\";\n\n";
	print THEONE "\$location = \"$location\";\n\n";
	print THEONE "\$myfoot = \"$thefoot\";\n\n";
	print THEONE "\$partners = \"$partners\";\n\n";
	print THEONE "##return = true\n";
	print THEONE "1;";
	flock(THEONE, 8);
	close(THEONE);
	chmod (0755, $thisfile);

if ($refresh eq "1") {
	print "<script language=\"Javascript\">";
	print "location.href='$script?custRel=1&arelease=$thefile';";
	print "</script>";
}

else {
{
print <<EOF
	
<HTML>
<HEAD>
<title>Coastline Micro, Inc. - Press Release Article Administration System - $date</title>
<script language="Javascript" src="$script?jscript=1&mousetable=1"></script>
<SCRIPT LANGUAGE="JavaScript">
//run current window
function runForm() {
parent.location.href = "$script";
}
</SCRIPT>
</HEAD>
<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<form>
<input type="hidden" value="1" name="deleRel">
  <br>
  <table border="1" cellspacing="0" cellpadding="0" align="center" bordercolor="#333366" width="500">
    <tr valign="top"> 
      <td width="100%" align="center"> 
        <table width="100%" border="1" bordercolor="#333366" cellpadding="3" cellspacing="0">
          <tr bgcolor="#333366" align="center"> 
            <td width="50%" height="35" bgcolor="#333366" align="center"><font face="verdana,arial,helvetica" size="2" color="#FFFFFF"><b> 
              <font color="#ffffff">Press Release Article Changes Saved</font></b></font></td>
          </tr>
          <tr> 
            <td width="50%" align="left" valign="middle"><br>
              <table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
                <tr> 
                  <td><font face="verdana,arial,helvetica" size="1">Your changes 
                    to the press release article titled: <b>$title</b> have been 
                    successfully saved to the system.</font></td>
                </tr>
              </table>
              <br>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
<br>
<table align="center" border="1" bgcolor="#8F8FAB" bordercolor="#333366" cellspacing="0" cellpadding="5" onMouseOver="runto('666666')" onMouseOut="runback('8F8FAB')"><tr><td width="100%" align="center"><input type="button" onClick="javascript:runForm();" value="Back to Start Page"></td></tr></table>
</form>
	</BODY>
	</HTML>

EOF
}
}
exit;
}

sub viewFoot {
$viewFoot = "$FORM{'viewFoot'}";
$whichone = "$FORM{'whichone'}";
if ($viewFoot eq "coastfoot") { 
$whichfoot = "Coastline Micro";
require ("press/coastfoot/$whichone"); 
}
else { 
$whichfoot = "Partner/Client";
require ("press/otherfoot/$whichone"); 
}

{
print <<EOF

<html>
<head>
<title>Coastline Micro, Inc. - Press Release Article Administration System - $date</title>
</head>
<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0"  onLoad="javascript:window.focus()">
<table cellpadding="3" cellspacing="0" border="0" width="500" align="center">
<tr><td>
<font size="3" face="verdana,arial,helvetica"><br><b>$whichfoot Press Release Article Footer</b></font><br><br>
<font size="2" face="verdana,arial,helvetica"><b>Footer Title</b><br>$foottitle
<br><br>
<b>Footer Link</b><br>$footlink
<br><br>
<b>Footer Text</b><br>$footbody
</font>

</td></tr>
</table>
</body>
</html>

EOF
}
exit;
}

sub custFoot {
$custFoot = "$FORM{'custFoot'}";
$whichone = "$FORM{'whichone'}";

	if ($custFoot eq "coastfoot") { 
	$foottype = "coastfoot";
	require ("press/coastfoot/$whichone");
	}
	else {
	$foottype = "otherfoot";
	require ("press/otherfoot/$whichone");
	}
	$footbody =~ s/<br>\n/\n/g;		
	$footbody =~ s/<br>/\n/g;				
		
{
print <<EOF
	
	<HTML>
	<HEAD>
<title>Coastline Micro, Inc. - Press Release Article Administration System - $date</title>
<script language="Javascript" src="$script?jscript=1&mousetable=1"></script>
<SCRIPT LANGUAGE="JavaScript">
//run current window
function checkForm() {
	if (document.router.foottitle.value == "" || document.router.foottitle.value == " ") {
	alert('Your footer title is missing.');
	document.router.foottitle.focus();
	return false;
	}	

	if (document.router.footlink.value == "" || document.router.footlink.value == " " || document.router.footlink.value.indexOf('http')==-1 || document.router.footlink.value.indexOf('://')==-1) {
	alert('Your footer link is missing or in an incorrect format.');
	document.router.footlink.focus();
    return false;
    }
		
	if (document.router.footbody.value == "" || document.router.footbody.value == " ") {
	alert('Your footer body text is missing.');
	document.router.footbody.focus();
	return false;
	}	
	else {
	return true;
	}	
}
</script>
</HEAD>
<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<form method="POST" name="router" action="$script" onSubmit="return checkForm();">
<input type="hidden" value="1" name="saveCustFoot">
<input type="hidden" value="$whichone" name="whichone">
<input type="hidden" value="$foottype" name="foottype">
  <br>
  <table border="1" cellspacing="0" cellpadding="0" align="center" bordercolor="#333366" width="500">
    <tr valign="top"> 
      <td width="100%" align="center"> 
        <table width="498" border="1" bordercolor="#333366" cellpadding="3" cellspacing="0">
          <tr bgcolor="#333366" align="center"> 
            <td width="50%" height="20" bgcolor="#333366" align="center"><font face="verdana,arial,helvetica" size="2" color="#FFFFFF"><b>Edit<font color="#ffffff"> 
              Press Release Footer</font></b></font></td>
          </tr>
          <tr> 
            <td width="50%" align="left" valign="middle"> <br>
              <table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
                <tr> 
                  <td><font face="verdana,arial,helvetica" size="1"><b>Quick Instructions</b> 
                    <br>
                    <br>
                    Just fill in, or change the data in form fields below then 
                    click 'Save Changes'<br>
                    </font> </td>
                </tr>
              </table>
              <br>
            </td>
          </tr>
        </table>
<!-- Start Releases in works -->
        <table width="498" border="1" bordercolor="#333366" cellpadding="3" cellspacing="0">
          <tr bgcolor="#333366" align="left"> 
            <td width="50%" height="20" bgcolor="#333366" align="center"><font face="verdana,arial,helvetica" size="1" color="#ffffff"><b>FOOTER 
              TITLE</b></font></td>
          </tr>
          <tr> 
            <td width="50%" align="center" height="50">
              <input type="text" name="foottitle" value="$foottitle" size="55">
            </td>
          </tr>
        </table>
        <table width="498" border="1" bordercolor="#333366" cellpadding="3" cellspacing="0">
          <tr bgcolor="#333366" align="left"> 
            <td width="50%" height="20" bgcolor="#333366" align="center"><font face="verdana,arial,helvetica" size="1" color="#ffffff"><b>FOOTER 
              LINK</b></font></td>
          </tr>
          <tr> 
            <td width="50%" align="center" height="50"> 
              <input type="text" name="footlink" value="$footlink" size="55">
            </td>
          </tr>
        </table>
        <table width="498" border="1" bordercolor="#333366" cellpadding="3" cellspacing="0">
          <tr bgcolor="#333366" align="left"> 
            <td width="50%" height="20" bgcolor="#333366" align="center"><font face="verdana,arial,helvetica" size="1" color="#ffffff"><b>FOOTER 
              BODY TEXT</b></font></td>
          </tr>
          <tr> 
            <td width="50%" align="center" height="50"> 
              <textarea name="footbody" cols="50" rows="10">$footbody</textarea>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
<br>
<table align="center" border="1" bgcolor="#8F8FAB" bordercolor="#333366" cellspacing="0" cellpadding="5" onMouseOver="runto('666666')" onMouseOut="runback('8F8FAB')"><tr><td width="100%" align="center">
        <input type="submit" value="Save Changes" name="Submit">
      </td></tr></table>
</form>
	</BODY>
	</HTML>

EOF
}
exit;
}


##################################################################
################ SAVE ARTICLE FOOTER CUSTOMIZATIONS################
##################################################################
sub saveCustFoot {

$foottype = "$FORM{'foottype'}";
$whichone = "$FORM{'whichone'}";
$foottitle = "$FORM{'foottitle'}";
$footlink = "$FORM{'footlink'}";
$footbody = "$FORM{'footbody'}";

## for escaping the dollar sign, common perl variable sign
$dollar='\$';

$foottitle =~ s/[\$]+/$dollar/g;
$foottitle =~ s/^[^\S\n]+//gm;
$foottitle =~ s/\n\n/<br><br>/g;
$foottitle =~ s/"/\\"/g;
$foottitle =~ s/@/\\@/g;

$footlink =~ s/[\$]+/$dollar/g;
$footlink =~ s/^[^\S\n]+//gm;
$footlink =~ s/\n\n/<br><br>/g;
$footlink =~ s/"/\\"/g;
$footlink =~ s/@/\\@/g;

$footbody =~ s/[\$]+/$dollar/g;
$footbody =~ s/^[^\S\n]+//gm;
$footbody =~ s/\n\n/<br><br>/g;
$footbody =~ s/"/\\"/g;
$footbody =~ s/@/\\@/g;

	# SAVE FOOTER
	$thisfile = "press/$foottype/$whichone";
	open(THEONE,">$thisfile") || &error('can not write to $thisfile');
	flock(THEONE, 2);
	print THEONE "#!/usr/bin/perl5 -w\n\n";
	print THEONE "\$foottitle = \"$foottitle\";\n\n";
	print THEONE "\$footlink = \"$footlink\";\n\n";
	print THEONE "\$footbody = \"$footbody\";\n\n";
	print THEONE "##return = true\n";
	print THEONE "1;";
	flock(THEONE, 8);
	close(THEONE);
	chmod (0755, $thisfile);
{
print <<EOF
	
	<HTML>
	<HEAD>
<title>Coastline Micro, Inc. - Press Release Article Administration System - $date</title>
<script language="Javascript" src="$script?jscript=1&mousetable=1"></script>
</HEAD>
<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
  <br>
  <table border="1" cellspacing="0" cellpadding="0" align="center" bordercolor="#333366" width="500">
    <tr valign="top"> 
      <td width="100%" align="center"> 
        <table width="498" border="1" bordercolor="#333366" cellpadding="3" cellspacing="0">
          <tr bgcolor="#333366" align="center"> 
            <td width="50%" height="20" bgcolor="#333366" align="center"><font face="verdana,arial,helvetica" size="2" color="#FFFFFF"><b>
              <font color="#ffffff">Changes to Article Footer Saved</font></b></font></td>
          </tr>
          <tr> 
            <td width="50%" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1"><br>Your changes to <b>$foottitle</b> have been successfully saved to the system.<br><br></font></td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
<br>
<form>
<table align="center" border="1" bgcolor="#8F8FAB" bordercolor="#333366" cellspacing="0" cellpadding="5" onMouseOver="runto('666666')" onMouseOut="runback('8F8FAB')"><tr><td width="100%" align="center"><input type="button" onClick="javascript:window.close();" value="Close Window"></td></tr></table>
</form>
	</BODY>
	</HTML>

EOF
}
exit;
}

sub makeFoot {
$makeFoot = "$FORM{'makeFoot'}";
if ($makeFoot eq "coastfoot") { 
$thistitle = "Coastline Micro Company Footer";
$whichfooter = "Coastline Micro";
$existing = "'Coastline Micro Available Footers'";
$howmany = "up to <b><i>two</i></b>";
$steptwo = "Type in a link to a section or page within Coastline Micro's site that closely relates to the press release article you are creating this footer for.";
$elaborate = "Coastline Micro's services, support, technology, past and present or basically anything that gives the press release reader a clear idea of the company";
$thisbody = "Coastline Micro";
}
else { 
$thistitle = "Partner/Client Company Footer";
$whichfooter = "Partner/Client";
$existing = "'Partner/Client Available Footers'";
$howmany = "no more than <b><i>one</i></b>";
$steptwo = "Type in a link to the website of the Partner/Client company for whom this footer is being created.";
$elaborate = "the Partner/Client company for whom this footer is being created";
$thisbody = "the Partner/Client company for whom this footer is being created.";
}

{
print <<EOF

	<HTML>
	<HEAD>
<title>Coastline Micro, Inc. - Press Release Article Administration System - $date</title>
<script language="Javascript" src="$script?jscript=1&mousetable=1"></script>
<SCRIPT LANGUAGE="JavaScript">
//run current window
function checkForm() {
	if (document.router.foottitle.value == "" || document.router.foottitle.value == " ") {
	alert('Your footer title is missing.');
	document.router.foottitle.focus();
	return false;
	}	

	if (document.router.footlink.value == "" || document.router.footlink.value == " " || document.router.footlink.value.indexOf('http')==-1 || document.router.footlink.value.indexOf('://')==-1) {
	alert('Your footer link is missing or in an incorrect format.');
	document.router.footlink.focus();
    return false;
    }
		
	if (document.router.footbody.value == "" || document.router.footbody.value == " ") {
	alert('Your footer body text is missing.');
	document.router.footbody.focus();
	return false;
	}	
	else {
	return true;
	}	
}
</script>
</HEAD>
<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<form method="POST" name="router" action="$script" onSubmit="return checkForm();">
<input type="hidden" value="1" name="saveNewFoot">
<input type="hidden" value="$makeFoot" name="foottype">
  <table border="1" cellspacing="0" cellpadding="0" align="center" bordercolor="#333366" width="500">
    <tr valign="top"> 
      <td width="100%" align="center"> 
        <table width="100%" border="1" bordercolor="#333366" cellpadding="3" cellspacing="0">
          <tr bgcolor="#333366" align="center"> 
            <td width="50%" height="20" bgcolor="#333366" align="center"><font face="verdana,arial,helvetica" size="2" color="#FFFFFF"><b>Creating 
              New <font color="#ffffff">Press Release Footer</font></b></font></td>
          </tr>
          <tr> 
            <td width="50%" align="left" valign="middle"> <br>
              <table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
                <tr> 
                  <td><font face="verdana,arial,helvetica" size="1"><b>Quick Instructions</b> 
                    <br>
                    You are about to create a new $whichfooter company footer for use 
                    within the site's press release articles. Please make sure 
                    you have checked all existing $existing to 
                    make sure there isn't a footer that relates to your new press 
                    release article. This way you can save yourself some time 
                    by not creating a new one.<br>
                    <br>
                    <b>Step 1: </b>Fill in the 'Footer Title' field. This title 
                    need not be more than <i><b>five</b> </i>descriptive words at 
                    most.<br>
                    <br>
                    <b>Step 2:</b> $steptwo Please use the example link's 
                    method in order for your link to work properly on the user-end.<br>
                    <br>
                    <b>Step 3:</b> Type in a brief description of $thisbody in the 
                    'Footer Body Text'. Feel free to use $howmany small 
                    sized paragraphs to elaborate on $elaborate.</font></td>
                </tr>
              </table>
              <br>
            </td>
          </tr>
        </table>
<!-- Start Releases in works -->
        <table width="500" border="1" bordercolor="#333366" cellpadding="3" cellspacing="0">
          <tr bgcolor="#333366" align="left"> 
            <td width="50%" height="20" bgcolor="#333366" align="center"><font face="verdana,arial,helvetica" size="1" color="#ffffff"><b>FOOTER 
              TITLE</b></font></td>
          </tr>
          <tr> 
            <td width="50%" align="center" height="50">
              <input type="text" name="foottitle" value="$foottitle" size="55">
            </td>
          </tr>
        </table>
        <table width="100%" border="1" bordercolor="#333366" cellpadding="3" cellspacing="0">
          <tr bgcolor="#333366" align="left"> 
            <td width="50%" height="20" bgcolor="#333366" align="center"><font face="verdana,arial,helvetica" size="1" color="#ffffff"><b>FOOTER 
              LINK</b></font></td>
          </tr>
          <tr> 
            <td width="50%" align="center" height="50"> 
              <input type="text" name="footlink" value="$footlink" size="55">
            </td>
          </tr>
        </table>
        <table width="100%" border="1" bordercolor="#333366" cellpadding="3" cellspacing="0">
          <tr bgcolor="#333366" align="left"> 
            <td width="50%" height="20" bgcolor="#333366" align="center"><font face="verdana,arial,helvetica" size="1" color="#ffffff"><b>FOOTER 
              BODY TEXT</b></font></td>
          </tr>
          <tr> 
            <td width="50%" align="center" height="50"> 
              <textarea name="footbody" cols="50" rows="10">$footbody</textarea>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
<br>
<table align="center" width="150" border="1" bgcolor="#8F8FAB" bordercolor="#333366" cellspacing="0" cellpadding="5" onMouseOver="runto('666666')" onMouseOut="runback('8F8FAB')"><tr><td align="center"><input type="submit" value="Save Changes"></td><td width="25" id="ignore" bgcolor="#666666">&nbsp;&nbsp;&nbsp;</td><td align="center"><input type="button" value="Cancel Footer" onClick="javascript:window.close();"></td></tr></table>
</form>
	</BODY>
	</HTML>

EOF
}
exit;
}

#########################################################
################ SAVE NEW ARTICLE FOOTER ################
#########################################################
sub saveNewFoot {

$foottype = "$FORM{'foottype'}";
$foottitle = "$FORM{'foottitle'}";
$footlink = "$FORM{'footlink'}";
$footbody = "$FORM{'footbody'}";

## for escaping the dollar sign, common perl variable sign
$dollar='\$';

$foottitle =~ s/[\$]+/$dollar/g;
$foottitle =~ s/^[^\S\n]+//gm;
$foottitle =~ s/\n\n/<br><br>/g;
$foottitle =~ s/"/\\"/g;
$foottitle =~ s/@/\\@/g;

$footlink =~ s/[\$]+/$dollar/g;
$footlink =~ s/^[^\S\n]+//gm;
$footlink =~ s/\n\n/<br><br>/g;
$footlink =~ s/"/\\"/g;
$footlink =~ s/@/\\@/g;

$footbody =~ s/[\$]+/$dollar/g;
$footbody =~ s/^[^\S\n]+//gm;
$footbody =~ s/\n\n/<br><br>/g;
$footbody =~ s/"/\\"/g;
$footbody =~ s/@/\\@/g;

	# SAVE FOOTER
	$thecount = `cat press/$foottype/count.dat`;
	$thecount++;
	$thisfile = "press/$foottype/count.dat";
	open(COUNT,">$thisfile") || &error('can not write to $thisfile');
	flock(COUNT, 2);
	print COUNT "$thecount";
	flock(COUNT, 8);
	close(COUNT);
	chmod (0755, $thisfile);
	$thisnew = "press/$foottype/$thecount.foot";
	open(THEONE,">$thisnew") || &error('can not write to $thisnew');
	flock(THEONE, 2);
	print THEONE "#!/usr/bin/perl5 -w\n\n";
	print THEONE "\$foottitle = \"$foottitle\";\n\n";
	print THEONE "\$footlink = \"$footlink\";\n\n";
	print THEONE "\$footbody = \"$footbody\";\n\n";
	print THEONE "##return = true\n";
	print THEONE "1;";
	flock(THEONE, 8);
	close(THEONE);
	chmod (0755, $thisnew)  || &error('cant chmod $thisnew');
{
print <<EOF
	
	<HTML>
	<HEAD>
<title>Coastline Micro, Inc. - Press Release Article Administration System - $date</title>
<script language="Javascript" src="$script?jscript=1&mousetable=1"></script>
</HEAD>
<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
  <br>
  <table border="1" cellspacing="0" cellpadding="0" align="center" bordercolor="#333366" width="500">
    <tr valign="top"> 
      <td width="100%" align="center"> 
        <table width="498" border="1" bordercolor="#333366" cellpadding="3" cellspacing="0">
          <tr bgcolor="#333366" align="center"> 
            <td width="50%" height="20" bgcolor="#333366" align="center"><font face="verdana,arial,helvetica" size="2" color="#FFFFFF"><b>
              <font color="#ffffff">New Article Footer Added</font></b></font></td>
          </tr>
          <tr> 
            <td width="50%" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1"><br>Your new press release article footer, <b>$foottitle</b>, has been successfully added to the system.<br><br></font></td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
<br>
<form>
<table align="center" border="1" bgcolor="#8F8FAB" bordercolor="#333366" cellspacing="0" cellpadding="5" onMouseOver="runto('666666')" onMouseOut="runback('8F8FAB')"><tr><td width="100%" align="center"><input type="button" onClick="javascript:window.close();" value="Close Window"></td></tr></table>
</form>
	</BODY>
	</HTML>

EOF
}
exit;
}

sub pressHelp {

{
print <<EOF
	
<HTML>
<HEAD>
<title>Coastline Micro, Inc. - Press Release Article Administration System - $date</title>
<script language="Javascript" src="$script?jscript=1&mousetable=1"></script>
</HEAD>
<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<br>
<table border="1" cellspacing="0" cellpadding="0" align="center" bordercolor="#333366" width="500">
    <tr valign="top"> 
      <td width="100%"><br>
        <table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
          <tr> 
            <td><center><img src="press/simpress_logo_large.gif" width="165" height="119" border="0"></center><br>
			<br><font face="verdana,arial,helvetica" size="1"><b>About SimPress</b><br><br>
			SimPress is an Internet application that gives a site's administrator(s), be it a Novice or and Expert user, full control over a site's press release articles on the fly. The application is fully customizable to every site's needs and taste. Furthermore, the application was built smart to take both HTML and Plain-Text formatted data, or a combination of the two. And that's just one of the many new-age ideas driving this Cross-Browser and Cross-Platform server application that just blows away competing applications hands-down.
			<br><br>
			This version of SimPress was fully customized to fit Coastline Micro, Inc.'s website interface by NetMedia Solutions. SimPress is just one of the many fully customizable internet applications NetMedia Solutions has developed for resale. The NetMedia Solutions website, where you will be able to find more information on SimPress and other fully customizable applications, is currently under construction and will be completed shortly. Once the site is complete you will be able buy your very own customizable application directly from NetMedia Solutions.<br>
              <br>
              <b>Application Highlights</b><br>
              <br>
              &nbsp;&nbsp;&nbsp;* Supports HTML/Plain Formatted Data<br>
              &nbsp;&nbsp;&nbsp;* Behind the scenes editing<br>
              &nbsp;&nbsp;&nbsp;* Customizable partner/company footers<br>
              &nbsp;&nbsp;&nbsp;* Sorting on the fly by Date<br>
              &nbsp;&nbsp;&nbsp;* Secure Non-HTTP data structure<br>
              <br><br><center><b>SimPress is &copy;NetMedia Solutions</b></center>
			</font></td>
          </tr>
        </table>
        <br>
      </td>
    </tr>
  </table>
</BODY>
</HTML>

EOF
}
exit;
}

sub error{
print "An error has occured, the error is $_[0]<br>\n";
print "<font color=\"red\">$!</font>\n";
exit;
}
exit;