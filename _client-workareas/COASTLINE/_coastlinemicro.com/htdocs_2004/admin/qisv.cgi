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
if (($Cookies{'UserType'} eq "CMManage") || ($Cookies{'UserType'} eq "CMAdmin") || ($Cookies{'UserType'} eq "CMSales") || ($Cookies{'ExtraAccess'} =~ "AdminCust")) { $nextone = "1"; }
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
$MenuConfig = `cat js/menu_config.js`;
$MenuConstructor = `cat js/menu_constructor.js`;
$MenuConfig = "<script langauage=\"Javascript\">\n$MenuConfig\n</script>";
$MenuConstructor = "<script langauage=\"Javascript\">\n$MenuConstructor\n</script>";

## get CM legal piece
$legal = `cat legal.nsf`;

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
$date2 = "$months[$mon] $mday, $year";
}

##############################################################
########## ROUTE USER DEPENDING ON LINK/FORM INPUT ###########
##############################################################

################ IF LOOKING FOR THE ADMIN MAIN FRAME ################
if ($FORM{'mainadmin'}) { &mainadmin; }

################ IF LOOKING FOR THE ADMIN MAIN FRAME ################
if ($FORM{'jscript'}) { &jscript; }

################ IF ADDING A NEW CLASS-ITEM TO THE CATALOGUE################
if ($FORM{'newCat'}) { &newCat; }

################ IF DELETING A RELEASE FROM ARCHIVE ################
if ($FORM{'deleCat'}) { &deleCat; }

################ IF VIEWING A PRESS RELEASE################
if ($FORM{'viewCat'}) { &viewCat; }

################ IF SAVING CUSTOMIZATIONS TO A PRESS RELEASE################
if ($FORM{'saveCat'}) { &saveCat; }

################ IF SAVING A NEW FOOTER ################
if ($FORM{'saveNewCat'}) { &saveNewCat; }

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
<title>Coastline Micro, Inc. - QISV Catalogue Administration System</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
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
<title>Coastline Micro, Inc. - QISV Catalogue Administration System</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="admincss.cgi" Type="text/css">
<script language="Javascript" src="$script?jscript=1&mousetable=1"></script>
<SCRIPT LANGUAGE="JavaScript">
//run new pop-up window
function runThis1(thistype) {
var formindex = document.router.numone.selectedIndex;
var thisone = document.router.numone.options[formindex].value;
if (thistype == "deleCat") {
	var agree=confirm("Deleting a Class-Item will destroy its entire product listings also, you cannot undo this action. Are you sure you want to delete the selected Class-Item?\\n\\n");
	if (agree)
	window.open('$script?'+thistype+'=204&whichone='+thisone+'','DELECAT','width=350,height=350');
	else
	nogo=1;
	}
else if (thistype == "newCat") {
	parent.botOne.location.href = "$script?"+thistype+"=204";
	}
else {
	parent.botOne.location.href = "$script?"+thistype+"=204&whichone="+thisone;
	}
}	

function runThis2(thistype) {
var formindex = document.router.numtwo.selectedIndex;
var thisone = document.router.numtwo.options[formindex].value;
if (thistype == "deleCat") {
	var agree=confirm("Deleting a Class-Item will destroy its entire product listings also, you cannot undo this action. Are you sure you want to delete the selected Class-Item?\\n\\n");
	if (agree)
	window.open('$script?'+thistype+'=208&whichone='+thisone+'','DELECAT','width=350,height=350');
	else
	nogo=1;
	}
else if (thistype == "newCat") {
	parent.botOne.location.href = "$script?"+thistype+"=208";
	}
else {
	parent.botOne.location.href = "$script?"+thistype+"=208&whichone="+thisone;
	}
}	

//run current window
function reload() {
parent.location.href = "$script";
}
</SCRIPT>
$MenuConfig
</HEAD>
<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
$MenuConstructor
<table width="100%" border="0" cellspacing="0" cellpadding="0" background="images/top_tablebg_main.jpg" height="100">
  <tr> 
    <td width="30%" valign="top"><img src="images/illus_main.jpg" width="250" height="100"></td>
    <td width="25%">&nbsp;</td>
    <td align="left" valign="top"><img src="images/title_main.jpg" width="300" height="100"></td>
  </tr>
</table>

<form method="post" action="$script" name="router">
  <table width="100%" border="0" cellpadding="0" cellspacing="0">
    <tr valign="top"> 
      <td width="20%">$legal</td>
      <td align="center" width="80%"> 
        <table width="95%" border="0" cellspacing="0" cellpadding="0">
          <tr> 
            <td width="75%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>QISV 
              </b> (Qualified Information Systems Vendor )<b> Administration</b></font></td>
            <td align="right" width="25%">&nbsp;</td>
          </tr>
          <tr> 
            <td colspan="2"> 
              <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER" bordercolor="#333366">
                <tr bordercolor="#333366"> 
                  <td width="50%" align="center" valign="top"> 
                    <table width="100%" border="0" cellspacing="0" cellpadding="5">
                      <tr> 
                        <td height="100" valign="top" colspan="2"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Function 
                          Overview</b><br>
                          </font><font face="verdana,arial,helvetica" size="1">Welcome 
                          to the Coastline Micro's QISV catalogue administration 
                          system. This system allows for you, the site's QISV 
                          catalogue administrator, to add, delete and modify the 
                          company's list of products.<br>
                          <br>
                          <b>Precautions</b><br>
                          Please be sure to read all instructions before attemting 
                          to change any of the system's data. All system function 
                          was completely tested and thoroughly debugged. Yet, 
                          if you find any kind of problem with this system please 
                          brief the Coastline Micro IT Director of the problem 
                          you encountered.</font><font face="verdana,arial,helvetica" size="1" color="#333366"><font color="#EB0000"><br>
                          <br>
                          </font></font> <br>
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Class 
                                      Number 204</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                    <td height="125" bgcolor="#F2F2F7" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1"> 
                                      <ul>
                                        <li>To VIEW and/or EDIT an item's contents 
                                          select an option from the list and click 
                                          'View Selected Item'</li>
                                        <li>To DELETE an item AND its contents 
                                          select an option from the list and click 
                                          'Delete Selected Item'</li>
                                        <li>To ADD a new item to this class click 
                                          'Add New Item'</li>
                                      </ul>
                                      </font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="55" align="center" width="468"> 
                                      <nobr> <br>
                                      <select name="numone" class="inputtext">
EOF
}

##### TABLE 204s
	$mystuff1 = "../qisv/204";
	opendir(DIR, $mystuff1) or die "can't opendir $mystuff1 $!";
	while (defined($myfile = readdir(DIR))) {
	next if $myfile =~ /^\.\.?$/; ## skip . and .. directories
		$a1 = `cat ../qisv/204/$myfile/title.dat`;
	    $mytitle = substr($a1, 0, 50);     # ONLY 50 Characters
		push(@stuffs,"$mytitle,,,$myfile")
	}
	@stuffs = sort(@stuffs);
	foreach $mystuff (@stuffs) {
		@mylines = split(/,,,/, $mystuff);
		print "<option value=\"$mylines[1]\">$mylines[1] $mylines[0]";
	}		
	
{
print <<EOF
                                      </select>
                                      <br>
                                      <br>
                                      <table border="1" cellspacing="0" cellpadding="3" bordercolor="#F2F2F7" onMouseOver="runto('ebebeb')" onMouseOut="runback('white')" align="center" width="100%">
                                        <tr> 
                                          <td height="25" align="left">&nbsp;&nbsp;<font face="verdana,arial,helvetica" size="1"><a href="javascript:runThis1('viewCat')"><b>View 
                                            Selected Item</b></a></font></td>
                                        </tr>
                                        <tr> 
                                          <td height="25" align="left">&nbsp;&nbsp;<font face="verdana,arial,helvetica" size="1"><a href="javascript:runThis1('deleCat')"><b>Delete 
                                            Selected Item</b></a></font></td>
                                        </tr>
                                        <tr> 
                                          <td height="25" align="left">&nbsp;&nbsp;<font face="verdana,arial,helvetica" size="1"><a href="javascript:reload()"><b>Refresh 
                                            Listing</b></a></font></td>
                                        </tr>
                                        <tr> 
                                          <td height="25" align="left">&nbsp;&nbsp;<font face="verdana,arial,helvetica" size="1"><a href="javascript:runThis1('newCat')"><b>Add 
                                            New Item</b></a></font></td>
                                        </tr>
                                      </table>
                                      </nobr></td>
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
                          <br>
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Class 
                                      Number 208</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                    <td height="125" bgcolor="#F2F2F7" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1"> 
                                      <ul>
                                        <li>To VIEW and/or EDIT an item's contents 
                                          select an option from the list and click 
                                          'View Selected Item'</li>
                                        <li>To DELETE an item AND its contents 
                                          select an option from the list and click 
                                          'Delete Selected Item'</li>
                                        <li>To ADD a new item to this class click 
                                          'Add New Item'</li>
                                      </ul>
                                      </font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="55" align="center" width="468"> 
                                      <nobr> <br>
                                      <select name="numtwo" class="inputtext">
EOF
}

##### TABLE 208s
	$mystuff2 = "../qisv/208";
	opendir(DIR, $mystuff2) or die "can't opendir $mystuff2 $!";
	while (defined($myfile = readdir(DIR))) {
	next if $myfile =~ /^\.\.?$/; ## skip . and .. directories
		$a2 = `cat ../qisv/208/$myfile/title.dat`;
	    $mytitle = substr($a2, 0, 50);     # ONLY 50 Characters
		push(@twostuffs,"$mytitle,,,$myfile")
	}
	@twostuffs = sort(@twostuffs);
	foreach $mystuff (@twostuffs) {
		@twomylines = split(/,,,/, $mystuff);
		print "<option value=\"$twomylines[1]\">$twomylines[1] $twomylines[0]";
	}	
	
{
print <<EOF
                                      </select>
                                      <br>
                                      <br>
                                      <table width="100%" border="1" cellspacing="0" cellpadding="3" bordercolor="#F2F2F7" onMouseOver="runto('ebebeb')" onMouseOut="runback('white')">
                                        <tr> 
                                          <td height="25" align="left">&nbsp;&nbsp;<font face="verdana,arial,helvetica" size="1"><a href="javascript:runThis2('viewCat')"><b>View 
                                            Selected Item</b></a></font></td>
                                        </tr>
                                        <tr> 
                                          <td height="25" align="left">&nbsp;&nbsp;<font face="verdana,arial,helvetica" size="1"><a href="javascript:runThis2('deleCat')"><b>Delete 
                                            Selected Item</b></a></font></td>
                                        </tr>
                                        <tr> 
                                          <td height="25" align="left">&nbsp;&nbsp;<font face="verdana,arial,helvetica" size="1"><a href="javascript:reload()"><b>Refresh 
                                            Listing</b></a></font></td>
                                        </tr>
                                        <tr> 
                                          <td height="25" align="left">&nbsp;&nbsp;<font face="verdana,arial,helvetica" size="1"><a href="javascript:runThis2('newCat')"><b>Add 
                                            New Item</b></a></font></td>
                                        </tr>
                                      </table>
                                      </nobr></td>
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
        <br>
      </td>
    </tr>
  </table>
</form>
<table width="100%" background="images/bot_frame_bg.jpg" height="56" align="center" cellpadding="0" cellspacing="0" border="0">
  <tr>
    <td width="55%" align="left" height="56">&nbsp;</td>
  </tr>
</table>
	</BODY>
	</HTML>

EOF
}
exit;
}

####################################################
################ VIEW PRESS RELEASE ################
####################################################
sub viewCat {
$viewCat = "$FORM{'viewCat'}";
$whichone = "$FORM{'whichone'}";
$mytitle = `cat ../qisv/$viewCat/$whichone/title.dat`;

{
print <<EOF

<html>
<head>
<title>Coastline Micro, Inc. - QISV Catalogue Administration System</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="admincss.cgi" Type="text/css">
<script language="Javascript" src="$script?jscript=1&mousetable=1"></script>
<SCRIPT LANGUAGE="JavaScript">
//run new pop-up window
function deleme(thisone) {
document.router.deleThis.value = thisone;
document.router.submit();
}	

function noDele() {
	alert('You have added an item to this listing in this session, therefore you cannot DELETE an item before saving your current work. Once your work has been saved return to this Class-Item listing to delete your product of choice.');
}	

function reload() {
	parent.botOne.location.href = "$script?viewCat=$viewCat&whichone=$whichone";
}

function jumpHome() {
	parent.location.href = "$script";
}

function viewHtml(directory,directory2,file) {
	window.open('../qisv/'+directory+'/'+directory2+'/'+file+'.html','VIEWITEM');
}

function noHtml() {
	alert('You have added an item to this listing in this session, therefore you cannot view the HTML file for an item before saving your current work. Once your work has been saved return to this Class-Item listing to view the HTML file your product of choice.');
}	
</SCRIPT>
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
      <td width="20%">$legal</td>
      <td align="center" width="80%"> 
        <table width="95%" border="0" cellspacing="0" cellpadding="0">
          <tr> 
            <td width="95%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>QISV 
              Class-Item: $whichone</b></font></td>
            <td align="right" width="5%">&nbsp;</td>
          </tr>
          <tr> 
            <td colspan="2"> 
              <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER" bordercolor="#333366">
                <tr bordercolor="#333366"> 
                  <td width="50%" align="center" valign="top"> 
                    <table width="100%" border="0" cellspacing="0" cellpadding="5">
                      <tr> 
                        <td height="100" valign="top" colspan="2">
                        <form method="post" action="$script" name="router">
                        
                        <br>
                          <table width="550" border="0" cellspacing="0" cellpadding="0" align="center">
                            <tr> 
                              <td width="550" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="548" valign="top"> 
                                <table width="548" border="0" cellspacing="0" cellpadding="0">
                                  <tr> 
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" bgcolor="#8F8FAB" width="0"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Class-Item 
                                      Description</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                    <td height="0" bgcolor="#F2F2F7" align="left" valign="middle" width="0">&nbsp;</td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="0" align="center" width="0" valign="middle"> 
                                      <nobr> 
                                      <input type="text" value="$mytitle" name="title" size="15" class="inputtext15">
                                      </nobr></td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" align="center" width="0" valign="top" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
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
                          <font size="2" face="verdana,arial,helvetica"><br>
                          </font> 
                          <input type="hidden" name="thisCat" value="$viewCat">
                          <input type="hidden" name="whichone" value="$whichone">
                          <input type="hidden" name="saveCat" value="1">
                          <input type="hidden" name="deleThis" value="null">                      
                          <table border=1 cellpadding=2 cellspacing=0 bordercolor=#333366 align=center width=550>
                            <tr> 
                              <td align="center" width="100"><font size="1" face="verdana,arial,helvetica"><i>Manufacturer</i></font></td>
                              <td align=center width="65"><font size="1" face="verdana,arial,helvetica"><i>Stock / SKU #</i></font></td>
                              <td width="100" align="center"><font size="1" face="verdana,arial,helvetica"><i>Product / Service Description</i></font></td>
                              <td align=center width="35"><font size="1" face="verdana,arial,helvetica"><i>Spec./ Info?</i></font></td>
                              <td align=center width="35"><font size="1" face="verdana,arial,helvetica"><i>Stk. Count<br>(07/11/01)</i></font></td>
                              <td align="center" width="65"><font size="1" face="verdana,arial,helvetica"><i>List Price</i></font></td>
                              <td width="65" align="center"><font size="1" face="verdana,arial,helvetica"><i>St. Disc. Price</i></font></td>
                              <td width="85" align="center"><font size="1" face="verdana,arial,helvetica"><i>Action(s)</i></font></td>
                            </tr>
EOF
}

##### TABLE 204s
		$mycontent = `cat ../qisv/$viewCat/$whichone/content.dat`;		
		@mylines = split(/:end\n/, $mycontent);
		$count=0;
    	foreach $myline (@mylines) {
		$count++;
			@mypairs = split(/,,,,,/, $myline);
			
			if ($FORM{'plusthis'} <= 0) {
				$delete = "<input type=\"button\" value=\"Delete\" onClick=\"javascript:deleme('$count');\">";
				$viewhtml = "<input type=\"button\" value=\"HTML\" onClick=\"javascript:viewHtml('$viewCat','$whichone','$count');\">";
			}
			else {
				$delete = "<input type=\"button\" value=\"Delete\" onClick=\"javascript:noDele();\">";
				$viewhtml = "<input type=\"button\" value=\"HTML\" onClick=\"javascript:noHtml();\">";
			}			
		print "<tr>";
		print "<td align=\"center\" width=\"100\"><input type=\"text\" name=\"$count\_01\" value=\"$mypairs[0]\" size=\"15\" class=\"inputtext15\"></td>";
		print "<td align=\"center\" width=\"65\"><input type=\"text\" name=\"$count\_02\" value=\"$mypairs[1]\" size=\"7\" class=\"inputtext7\"></td>";
		print "<td align=\"center\" width=\"100\"><input type=\"text\" name=\"$count\_03\" value=\"$mypairs[2]\" size=\"15\" class=\"inputtext15\"></td>";
		print "<td align=\"center\" width=\"35\"><input type=\"text\" name=\"$count\_04\" value=\"$mypairs[3]\" size=\"3\" class=\"inputtext3\"></td>";
		print "<td align=\"center\" width=\"35\"><input type=\"text\" name=\"$count\_05\" value=\"$mypairs[4]\" size=\"3\" class=\"inputtext3\"></td>";
		print "<td align=\"center\" width=\"65\"><input type=\"text\" name=\"$count\_06\" value=\"$mypairs[5]\" size=\"7\" class=\"inputtext7\"></td>";
		print "<td align=\"center\" width=\"65\"><input type=\"text\" name=\"$count\_07\" value=\"$mypairs[6]\" size=\"7\" class=\"inputtext7\"></td>";
		print "<td align=\"center\" width=\"85\"><nobr>$delete&nbsp;$viewhtml<input type=\"hidden\" name=\"$count\_08\" value=\"$count\"></nobr></td>";
		print "</tr>";
		}
		
		if ($FORM{'plusthis'} >= 1) {
			$plusthis = "$FORM{'plusthis'}";
			$count = "$FORM{'currentcount'}";	
				print "<tr>";
				print "<td align=\"center\" colspan=\"8\" height=\"100\"><font size=\"1\" face=\"verdana,arial,helvetica\"><b>You have added the following $plusthis products in this session.<br><br>Please remember to save your work before leaving this screen.<br><br>ALSO, before adding more products to this listing, please save your current work.</b></font></td>";
				print "</tr>";
			foreach (1 .. $plusthis) {
				$count++;
				print "<tr>";
				print "<td align=\"center\" width=\"100\"><input type=\"text\" name=\"$count\_01\" size=\"15\" class=\"inputtext15\"></td>";
				print "<td align=\"center\" width=\"65\"><input type=\"text\" name=\"$count\_02\" size=\"7\" class=\"inputtext7\"></td>";
				print "<td align=\"center\" width=\"100\"><input type=\"text\" name=\"$count\_03\" size=\"15\" class=\"inputtext15\"></td>";
				print "<td align=\"center\" width=\"35\"><input type=\"text\" name=\"$count\_04\" size=\"3\" class=\"inputtext3\"></td>";
				print "<td align=\"center\" width=\"35\"><input type=\"text\" name=\"$count\_05\" size=\"3\" class=\"inputtext3\"></td>";
				print "<td align=\"center\" width=\"65\"><input type=\"text\" name=\"$count\_06\" size=\"7\" class=\"inputtext7\"></td>";
				print "<td align=\"center\" width=\"65\"><input type=\"text\" name=\"$count\_07\" size=\"7\" class=\"inputtext7\"></td>";
				print "<td align=\"center\" width=\"85\"><nobr>$delete&nbsp;$viewhtml<input type=\"hidden\" name=\"$count\_08\" value=\"$count\"></nobr></td>";
				print "</tr>";
			}
		}

{
print <<EOF

<input type="hidden" name="thiscount" value="$count"><input type="hidden" name="currentcount" value="$count">
                          </table>
                          <br>
                          <table width="550" border="0" cellspacing="0" cellpadding="0" align="center">
                            <tr> 
                              <td width="550" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="548" valign="top"> 
                                <table width="548" border="0" cellspacing="0" cellpadding="0">
                                  <tr> 
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" bgcolor="#8F8FAB" width="0"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Actions</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                    <td height="0" bgcolor="#F2F2F7" align="left" valign="middle" width="0">&nbsp;</td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="0" align="center" width="0" valign="middle"> 
                                      <nobr> 
                                      <table align="center" border="1" bordercolor="#F2F2F7" cellspacing="0" cellpadding="5" onMouseOver="runto('F2F2F7')" onMouseOut="runback('FFFFFF')" width="100%">
                                        <tr valign="middle"> 
                                          <td align="center">
<input type="submit" value="Save Changes" name="submit2">
                                          </td>
                                          <td align="center">
<input type="reset" value="Clear Changes" name="reset">
                                          </td>
                                          <td align="center">
<input type="button" onClick="javascript:reload();" value="Refresh Listing" name="button">
                                          </td>
                                          <td align="center">
<input type="button" onClick="javascript:jumpHome();" value="QISV Home" name="button">
                                          </td>
                                        </tr>
                                      </table>
                                      </nobr></td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" align="center" width="0" valign="top" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
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
<form method="post" action="$script" name="addmua">
                          <table width="550" border="0" cellspacing="0" cellpadding="0" align="center">
                            <tr> 
                              <td width="550" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="548" valign="top"> 
                                <table width="548" border="0" cellspacing="0" cellpadding="0">
                                  <tr> 
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" bgcolor="#8F8FAB" width="0"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Add 
                                      New Product</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                    <td height="15" bgcolor="#F2F2F7" align="left" valign="middle" width="0">&nbsp;</td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="125" align="center" width="0" valign="bottom"><nobr><font size="1" face="verdana,arial,helvetica"><b>How 
                                      many more products would you like to add 
                                      to this Class-Item list?</b></font><br>
                                      <input type="text" name="plusthis" value="" size="3">
                                      <input type="hidden" name="currentcount" value="$count">
                                      <input type="hidden" name="viewCat" value="$viewCat">
                                      <input type="hidden" name="whichone" value="$whichone">
                                      <br>
                                      <br>
                                      <table align="center" border="1" bordercolor="#F2F2F7" cellspacing="0" cellpadding="5" onMouseOver="runto('F2F2F7')" onMouseOut="runback('FFFFFF')" width="100%">
                                        <tr> 
                                          <td align="center"> 
                                            <input type="submit" value="Add This Many" name="submit3">
                                          </td>
                                        </tr>
                                      </table>
                                      </nobr></td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" align="center" width="0" valign="top" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
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
        <br>
      </td>
    </tr>
  </table>

<table width="100%" background="images/bot_frame_bg.jpg" height="56" align="center" cellpadding="0" cellspacing="0" border="0">
  <tr> 
    <td width="55%" align="left" height="56">&nbsp;</td>
  </tr>
</table>
</body>
</html>

EOF
}
exit;
}

################################################
################ SAVE CATALOGUE ################
################################################
sub saveCat {

$viewCat = "$FORM{'thisCat'}";
$whichone = "$FORM{'whichone'}";
$currentcount = "$FORM{'currentcount'}";
$thefoot = "$FORM{'myfoot'}";
$otherfoot = "$FORM{'otherfeet'}";
$refresh = "$FORM{'refresh'}";
$title = "$FORM{'title'}";
$deleThis = "$FORM{'deleThis'}";

## DELETE OLD HTML PAGES FOR THIS CLASS-LISTING FOR NEW ONES TO COME INTO PLAY
$killme = "../qisv/$viewCat/$whichone";
opendir(DIR, $killme) or die "can't opendir $killme $!";
while (defined($file = readdir(DIR))) {
next if $file =~ /^\.\.?$/; ## skip . and .. directories
next if $file =~ /^\.\.?$/; ## skip .dat files
$file2 = "../qisv/$viewCat/$whichone/$file";
unlink($file2) || &error('cant delete $file2');
}
	
### SAVE TITLE EVEN IF ITS THE SAME ONE
$myfiler = "../qisv/$viewCat/$whichone/title.dat";
open(TITLER,">$myfiler") || &error('can not write to $myfiler');
flock(TITLER, 2);
print TITLER "$title";
flock(TITLER, 8);
close(TITLER);

### SAVE LATEST CHANGE DATE TO TODAYS DATE
&date;
$mydater = "../qisv/date.dat";

open(DATER,">$mydater") || &error('can not write to $mydater');
flock(DATER, 2);
print DATER "$date2";
flock(DATER, 8);
close(DATER);

### Page Header Grab and Drop
$topdrop = `cat ../qisv/topdrop.dat`;

$thecount="0";
$newcount="0";
foreach $thecount (1 .. $currentcount) {

	if ($thecount eq $deleThis) {
		$newcount = $newcount;
	}
	else {
		$newcount++;
	}
	
	if ($thecount != $deleThis) {
		$field01 = $FORM{$thecount . '_01'};
		$field02 = $FORM{$thecount . '_02'};
		$field03 = $FORM{$thecount . '_03'};
		$field04 = $FORM{$thecount . '_04'};
		$field05 = $FORM{$thecount . '_05'};
		$field06 = $FORM{$thecount . '_06'};
		$field07 = $FORM{$thecount . '_07'};
	
		# CREATE ALL NEW SEARCHABLE CATALOGUE FILES
		$myfile = "../qisv/$viewCat/$whichone/$newcount.html";
		open(THEONE,">$myfile") || &error('can not write to $myfile');
		flock(THEONE, 2);
		print THEONE "<html><head><title>Coastline Micro, Inc. - Class-List $whichone - $field02</title></head>";
		print THEONE "<body background=\"../../images/qisvbkgd.gif\">";
		print THEONE "<CENTER><h2><font face=verdana, arial, helvetica>Coastline Micro, Inc.<br><br>VID # 1-33-056-4458-800";
		print THEONE "<br><br>QISV Ordering Address:</H2></font>";
		print THEONE "<font face=verdana, arial, helvetica SIZE=3>60 Technology Drive<BR>Irvine, CA 92618</font>";
		print THEONE "</center>";
		print THEONE "<P>";
		print THEONE "<HR>";
		print THEONE "<CENTER><strong><font face=verdana, arial, helvetica size=2>This is a true and accurate copy of the catalogue approved with the General Services Commission.</font></strong></CENTER>";
		print THEONE "<CENTER><font face=verdana, arial, helvetica SIZE=2>Effective Date of catalogue:<BR><b>June 15, 2001</b></font></CENTER>";
		print THEONE "<CENTER><font face=verdana, arial, helvetica SIZE=2>This catalogue last updated $date2.</font></CENTER>";
		print THEONE "$topdrop";
		print THEONE "<!--KILLSPOTTER-->";
		print THEONE "<font face=verdana, arial, helvetica size=2><b>$whichone $title</b></font>";
		print THEONE "<TABLE border=1 cellpadding=2>";
		print THEONE "<TD align=\"center\" width=\"125\"><font face=verdana, arial, helvetica  SIZE=2><i>Manufacturer</i></font></TD><TD ALIGN=center width=\"300\"><font face=verdana, arial, helvetica  SIZE=-1><i>Stock / SKU #</i></font></TD><TD width=\"250\"><font face=verdana, arial, helvetica  SIZE=-1><i>Product / Service Des cription</i></font></TD><TD ALIGN=center width=\"50\"><font face=verdana, arial, helvetica  SIZE=-1><i>Spec./ Info?</i></font></TD><TD ALIGN=center width=\"100\"><font face=verdana, arial, helvetica  SIZE=-1><i>Stk. Count<BR>($lastdate)</i></font></TD><TD align=\"center\" width=\"50\"><font face=verdana, arial, helvetica  SIZE=-1><i>List Price</i></font></TD><TD width=\"50\" align=\"center\"><font face=verdana, arial, helvetica  SIZE=-1><i>St. Disc. Price</i></font></TD>";
		print THEONE "<tr>";
		print THEONE "<td><font face=verdana, arial, helvetica size=\"1\">$field01</font></td>";
		print THEONE "<td><font face=verdana, arial, helvetica size=\"1\">$field02</font></td>";
		print THEONE "<td><font face=verdana, arial, helvetica size=\"1\">$field03</font></td>";
		print THEONE "<td><font face=verdana, arial, helvetica size=\"1\">$field04</font></td>";
		print THEONE "<td><font face=verdana, arial, helvetica size=\"1\">$field05</font></td>";
		print THEONE "<td><font face=verdana, arial, helvetica size=\"1\">$field06</font></td>";
		print THEONE "<td><font face=verdana, arial, helvetica size=\"1\">$field07</font></td>";
		print THEONE "</tr>";
		print THEONE "</TABLE>";
		print THEONE "<br><br>";
		print THEONE "<!--KILLSPOTTER2-->";
		print THEONE "<font face=verdana, arial, helvetica size=2><center>If you have any questions, comments or suggestions, please <font COLOR=#0000FF><a href=\"framer.cgi?new_url=cont_temp.cgi&sub_link=gencomments\">E-Mail</a></font> us, Coastline Micro, directly!</center></font>";
		print THEONE "</body></html>";
		flock(THEONE, 8);
		close(THEONE);
    	push(@contents,"$field01,,,,,$field02,,,,,$field03,,,,,$field04,,,,,$field05,,,,,$field06,,,,,$field07:end");
	}

}
	
	$mycontents = "../qisv/$viewCat/$whichone/content.dat";
	open(CONTENTS,">$mycontents") || &error('can not write to $mycontents');
	flock(CONTENTS, 2);
	foreach $content (@contents) {
	print CONTENTS "$content\n";
	}
	flock(CONTENTS, 8);
	close(CONTENTS);
	
	$myindex = "../qisv/$viewCat/$whichone/index.html";
	open(INDEXFILE,">$myindex") || &error('can not write to $myindex');
	flock(INDEXFILE, 2);
	print INDEXFILE "<html><head><title>Coastline Micro, Inc. - QISV Catalogue</title>";
	print INDEXFILE "<META HTTP-EQUIV=\"Refresh\" CONTENT=\".001; URL=qisv/\">";
	print INDEXFILE "</head>";
	print INDEXFILE "<body background=\"../../images/qisvbkgd.gif\">";
	print INDEXFILE "</body></html>";
	flock(INDEXFILE, 8);
	close(INDEXFILE);

{
print <<EOF
	
<HTML>
<HEAD>
<title>Coastline Micro, Inc. - QISV Catalogue Administration System</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="admincss.cgi" Type="text/css">
<script language="Javascript" src="$script?jscript=1&mousetable=1"></script>
<SCRIPT LANGUAGE="JavaScript">
//run back to class-listing
function jumpBack() {
	parent.botOne.location.href = "$script?viewCat=$viewCat&whichone=$whichone";
}
function jumpHome() {
	parent.location.href = "$script";
}
</SCRIPT>
$MenuConfig
</HEAD>
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
          <td width="95%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>QISV 
            Changes Saved</b></font></td>
          <td align="right" width="5%">&nbsp;</td>
        </tr>
        <tr> 
          <td colspan="2"> 
            <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER" bordercolor="#333366">
              <tr bordercolor="#333366"> 
                <td width="50%" align="center" valign="top"> 
                  <table width="100%" border="0" cellspacing="0" cellpadding="5">
                    <tr> 
                      <td height="100" valign="top" colspan="2">
                        <form method="post">
                          <br>
                          <table width="550" border="0" cellspacing="0" cellpadding="0" align="center">
                            <tr> 
                              <td width="550" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="548" valign="top"> 
                                <table width="548" border="0" cellspacing="0" cellpadding="0">
                                  <tr> 
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" bgcolor="#8F8FAB" width="520"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Save 
                                      Successful </font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                    <td height="35" bgcolor="#F2F2F7" align="center" valign="middle" width="520"><font face="verdana,arial,helvetica" size="1">Your 
                                      changes have been successfully saved to 
                                      the system.</font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="0" align="center" width="520" valign="middle"> 
                                      <nobr> 
                                      <table align="center" border="1" bordercolor="#F2F2F7" cellspacing="0" cellpadding="5" onMouseOver="runto('F2F2F7')" onMouseOut="runback('FFFFFF')" width="100%">
                                        <tr> 
                                          <td align="center" width="50%"> 
                                            <input type="button" onClick="javascript:jumpBack();" value="Re-Parse $whichone's Content" name="button2">
                                          </td>
                                          <td align="center" width="50%"> 
                                            <input type="button" onClick="javascript:jumpHome();" value="QISV Home" name="button2">
                                          </td>
                                        </tr>
                                      </table>
                                      </nobr></td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" align="center" width="520" valign="top" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
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

                        </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
      <br>
    </td>
  </tr>
</table>
<table width="100%" background="images/bot_frame_bg.jpg" height="56" align="center" cellpadding="0" cellspacing="0" border="0">
  <tr> 
    <td width="55%" align="left" height="56">&nbsp;</td>
  </tr>
</table>
	</BODY>
	</HTML>

EOF
}
exit;
}

sub deleCat {
$deleCat = "$FORM{'deleCat'}";
$whichone = "$FORM{'whichone'}";

{
print <<EOF

<HTML>
<HEAD>
<title>Coastline Micro, Inc. - QISV Catalogue Administration System</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="admincss.cgi" Type="text/css">
<script language="Javascript" src="$script?jscript=1&mousetable=1"></script>
</HEAD>
<body bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<table width="100%" border="0" cellspacing="0" cellpadding="0" background="images/top_tablebg_main.jpg" height="100">
  <tr> 
    <td align="center" width="100%" valign="top"><img src="images/title_main.jpg" width="300" height="100"></td>
  </tr>
</table>
<table width="100%" border="0" cellpadding="0" cellspacing="0">
  <tr valign="top"> 
    <td align="center" width="100%"> 
      <table width="95%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td width="95%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>QISV 
            Class-Item Deleted</b></font></td>
          <td align="right" width="5%">&nbsp;</td>
        </tr>
        <tr> 
          <td colspan="2"> 
            <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER" bordercolor="#333366">
              <tr bordercolor="#333366"> 
                <td width="50%" align="center" valign="top"> 
                  <table width="100%" border="0" cellspacing="0" cellpadding="5">
                    <tr> 
                      <td height="100" valign="top" colspan="2">
<form>
<font face="verdana,arial,helvetica" size="1" color="#333366">

EOF
}
$thisdir = "../qisv/$deleCat/$whichone";
print "<b>Deleting Content</b><br>";
opendir(DIR, $thisdir) or die "can't opendir $thisdir $!";
while (defined($file = readdir(DIR))) {
next if $file =~ /^\.\.?$/; ## skip . and .. directories
$file2 = "../qisv/$deleCat/$whichone/$file";
unlink($file2) || &error('cant delete $file2');
print "$file deleted<br>";
}
rmdir("../qisv/$deleCat/$whichone") || &error('cant delete ../qisv/$deleCat/$whichone'); 
print "<br><br><b>Deleting Class-Listing</b><br>$whichone deleted.<br><br>";
print "<b>All content from Class-Listing $whichone has been deleted successfully.</b><br><br>";
print "<b>Please remember to REFRESH the Class Number $deleCat listing on the main screen.</b><br>";
{
print <<EOF

<br><br></font>
                          <table align="center" border="1" bordercolor="#F2F2F7" cellspacing="0" cellpadding="5" onMouseOver="runto('F2F2F7')" onMouseOut="runback('FFFFFF')">
                            <tr><td width="100%" align="center"><input type="button" onClick="javascript:parent.window.close();" value="Close Window"></td></tr></table>
</form></td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
      <br>
    </td>
  </tr>
</table>
<table width="100%" background="images/bot_frame_bg.jpg" height="56" align="center" cellpadding="0" cellspacing="0" border="0">
  <tr> 
    <td width="55%" align="left" height="56">&nbsp;</td>
  </tr>
</table>

</body>
</html>

EOF
}
exit;
}

sub newCat {
$newCat = "$FORM{'newCat'}";

{
print <<EOF

<HTML>
<HEAD>
<title>Coastline Micro, Inc. - QISV Catalogue Administration System</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="admincss.cgi" Type="text/css">
<script language="Javascript" src="$script?jscript=1&mousetable=1"></script>
<SCRIPT LANGUAGE="JavaScript">
function checkForm() {
	if (document.router.code.value == "" || document.router.code.value == " ") {
	alert('The Class-Item Code is missing or incorrect.');
	document.router.code.focus();
	return false;
	}	

	if (document.router.desc.value == "" || document.router.desc.value == " ") {
	alert('The Class-Item Description is missing.');
	document.router.desc.focus();
    return false;
    }
		
	else {
	return true;
	}	
}

function jumpHome() {
	parent.location.href = "$script";
}
</script>
$MenuConfig
</HEAD>
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
          <td width="95%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>Creating 
            New Class-List for Class: $newCat</b></font></td>
          <td align="right" width="5%">&nbsp;</td>
        </tr>
        <tr> 
          <td colspan="2"> 
            <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER" bordercolor="#333366">
              <tr bordercolor="#333366"> 
                <td width="50%" align="center" valign="top"> 
                  <table width="100%" border="0" cellspacing="0" cellpadding="5">
                    <tr> 
                      <td height="100" valign="top" colspan="2"> 
                        <form method="POST" name="router" action="$script" onSubmit="return checkForm();">
                          <br>
                          <table width="550" border="0" cellspacing="0" cellpadding="0" align="center">
                            <tr> 
                              <td width="550" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="548" valign="top"> 
                                <table width="548" border="0" cellspacing="0" cellpadding="0">
                                  <tr> 
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" bgcolor="#8F8FAB" width="518"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Class-Item 
                                      Configuration</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                    <td height="135" bgcolor="#F2F2F7" align="left" valign="middle" width="518"><font face="verdana,arial,helvetica" size="1"><b>Quick 
                                      Instructions</b> 
                                      <input type="hidden" value="1" name="saveNewCat">
                                      <input type="hidden" value="$newCat" name="thisCat">
                                      <br>
                                      You are about to create a new Class-List 
                                      in your QISV Catalogue for Class Number 
                                      <strong>$newCat</strong>.<br>
                                      <br>
                                      <b>Step 1: </b>Fill in the 'Class-Item Code' 
                                      field. This TWO digit number should be acquired 
                                      from the <a href="javascript:void(0);" onClick="javascript:window.open('http://www.gsc.state.tx.us/stpurch/qisvcodes.html','QISV');">QISV 
                                      Class-item Codes</a>.<br>
                                      <br>
                                      <b>Step 2:</b>Fill in the 'Class-Item Description' 
                                      field. This title should be the same as 
                                      found on the QISV Class-Item Codes.<br>
                                      <br>
                                      <b>Step 3:</b>Click the Add Class-Listing 
                                      button to continue.</font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="35" align="center" width="518" valign="middle"> 
                                      <nobr> <font face="verdana,arial,helvetica" size="1"><b>Class 
                                      Item Code:</b></font></nobr><nobr></nobr><nobr> 
                                      <input type="text" name="code" size="15" class="inputtext15" maxlenght="2">
                                      </nobr></td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="35" align="center" width="518" valign="middle"> 
                                      <font face="verdana,arial,helvetica" size="1"><b>Class 
                                      Item Description: </b></font> 
                                      <input type="text" name="desc" size="15" class="inputtext15">
                                    </td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td align="center" width="518" valign="top" bgcolor="#F2F2F7">
                                      <table align="center" border="1" width="100%" bordercolor="#F2F2F7" cellspacing="0" cellpadding="5" onMouseOver="runto('F2F2F7')" onMouseOut="runback('FFFFFF')" bgcolor="#ffffff">
                                        <tr> 
                                          <td align="center" width="50%"> 
                                            <input type="submit" value="Add Class-Listing" name="submit">
                                          </td>
                                          <td align="center" width="50%"> 
                                            <input type="button" value="Cancel Addition" onClick="javascript:jumpHome();" name="button2">
                                          </td>
                                        </tr>
                                      </table>
                                    </td>
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
                          <br>
                        </form>
                        
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
      <br>
    </td>
  </tr>
</table>
<table width="100%" background="images/bot_frame_bg.jpg" height="56" align="center" cellpadding="0" cellspacing="0" border="0">
  <tr> 
    <td width="55%" align="left" height="56">&nbsp;</td>
  </tr>
</table>
	</BODY>
	</HTML>

EOF
}
exit;
}

#########################################################
################ SAVE NEW ARTICLE FOOTER ################
#########################################################
sub saveNewCat {


$newCat = "$FORM{'thisCat'}";
$code = "$FORM{'code'}";
$desc = "$FORM{'desc'}";

## for escaping the dollar sign, common perl variable sign
$dollar='\$';

$newCat =~ s/[\$]+/$dollar/g;
$newCat =~ s/^[^\S\n]+//gm;
$newCat =~ s/\n\n/<br><br>/g;
$newCat =~ s/"/\\"/g;
$newCat =~ s/@/\\@/g;

$code =~ s/[\$]+/$dollar/g;
$code =~ s/^[^\S\n]+//gm;
$code =~ s/\n\n/<br><br>/g;
$code =~ s/"/\\"/g;
$code =~ s/@/\\@/g;

$desc =~ s/[\$]+/$dollar/g;
$desc =~ s/^[^\S\n]+//gm;
$desc =~ s/\n\n/<br><br>/g;
$desc =~ s/"/\\"/g;
$desc =~ s/@/\\@/g;

	### SAVE TITLE EVEN IF ITS THE SAME ONE
	$whichone = "$newCat-$code";
	mkdir("../qisv/$newCat/$whichone", 0777) || &error('cant write create class-list, must already exist?');
	$myfiler = "../qisv/$newCat/$whichone/title.dat";
	open(TITLER,">$myfiler") || &error('can not write to $myfiler');
	flock(TITLER, 2);
	print TITLER "$desc";
	flock(TITLER, 8);
	close(TITLER);

	### SAVE LATEST CHANGE DATE TO TODAYS DATE
	&date;
	$mydater = "../qisv/date.dat";
	open(DATER,">$mydater") || &error('can not write to $mydater');
	flock(DATER, 2);
	print DATER "$date2";
	flock(DATER, 8);
	close(DATER);

	
	$mycontents = "../qisv/$newCat/$whichone/content.dat";
	open(CONTENTS,">$mycontents") || &error('can not write to $mycontents');
	flock(CONTENTS, 2);
    push(@contents,"default,,,,,default,,,,,default,,,,,default,,,,,default,,,,,default,,,,,default:end");
	foreach $content (@contents) {
	print CONTENTS "$content\n";
	}
	flock(CONTENTS, 8);
	close(CONTENTS);

{
print <<EOF
	
<HTML>
<HEAD>
<title>Coastline Micro, Inc. - QISV Catalogue Administration System</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="admincss.cgi" Type="text/css">
<script language="Javascript" src="$script?jscript=1&mousetable=1"></script>
<SCRIPT LANGUAGE="JavaScript">
function jumpHome() {
	parent.location.href = "$script";
}
</script>
</HEAD>
<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
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
          <td width="95%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>New 
            Class-Item Created Successfully</b></font></td>
          <td align="right" width="5%">&nbsp;</td>
        </tr>
        <tr> 
          <td colspan="2"> 
            <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER" bordercolor="#333366">
              <tr bordercolor="#333366"> 
                <td width="50%" align="center" valign="top"> 
                  <table width="100%" border="0" cellspacing="0" cellpadding="5">
                    <tr> 
                      <td height="100" valign="top" colspan="2"> 
                        <form>
                          <br>
                          <table width="550" border="0" cellspacing="0" cellpadding="0" align="center">
                            <tr> 
                              <td width="550" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="548" valign="top"> 
                                <table width="548" border="0" cellspacing="0" cellpadding="0">
                                  <tr> 
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" bgcolor="#8F8FAB" width="520"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Action</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                    <td height="35" bgcolor="#F2F2F7" align="left" valign="middle" width="520"><font face="verdana,arial,helvetica" size="1">Your 
                                      new Class-List, <strong>$whichone</strong>, 
                                      has been successfully added to the system.</font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="0" align="center" width="520" valign="middle"><nobr> 
                                      <table align="center" border="1" bordercolor="#F2F2F7" cellspacing="0" cellpadding="5" onMouseOver="runto('F2F2F7')" onMouseOut="runback('FFFFFF')" width="100%">
                                        <tr> 
                                          <td align="center" width="100%"> 
                                            <input type="button" onClick="javascript:jumpHome();" value="QISV Home" name="button2">
                                          </td>
                                        </tr>
                                      </table>
                                      </nobr></td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" align="center" width="520" valign="top" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
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
                          <br>
                        </form>
                        </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
      <br>
    </td>
  </tr>
</table>
<table width="100%" background="images/bot_frame_bg.jpg" height="56" align="center" cellpadding="0" cellspacing="0" border="0">
  <tr> 
    <td width="55%" align="left" height="56">&nbsp;</td>
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