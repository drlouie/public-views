#!/usr/bin/perl5 -s


###########################################################################################################
# Company: ©2001 NetMedia Solutions                                                                       #
# Date: Saturday, September 21, 2001                                                                      #
# Location: Los Angeles County, California, United States of America                                      #
# Made By: Luis Rodriguez (drlouie)                                                                       #
# Email: Drlouie@NetMediaSol.com                                                                          #
#                                                                                                         #
# drlouie's DB product table parsing script. Dynamically driven by DHTML, HTML, Perl and MySql #
#                                                                                                         #
# This program cannot be duplicated, distributed or re-used for any other purpose other than its original #
# intended purpose and function. You may request NetMedia Solutions for a copy of the script,             #
# personalized to fit your exact needs for a small re-programming fee.                                    #
###########################################################################################################

$script = $ENV{'SCRIPT_NAME'};

require ("referer.nsp"); 
require ("date.nsp");

$legal = `cat legal.nsf`;

################# START parse form ##################
    if ($ENV{'REQUEST_METHOD'} eq 'GET') {
        @pairs = split(/&/, $ENV{'QUERY_STRING'});
    }
    elsif ($ENV{'REQUEST_METHOD'} eq 'POST') {
        read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
 
        @pairs = split(/&/, $buffer);
    }
    else {
        &error('request_method');
    }

    foreach $pair (@pairs) {

        local($name, $value) = split(/=/, $pair);
 
        $name =~ tr/+/ /;
        $name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

        $value =~ tr/+/ /;
        $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

        $value =~ s/<!--(.|\n)*-->//g;

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
################# END parse form ##################

##############################################################
########## ROUTE USER DEPENDING ON LINK/FORM INPUT ###########
##############################################################

################ IF VIEWING PRESS RELEASE################
if ($Form{'viewRel'}) { &viewRel; }

################ IF LOOKING FOR ADMIN MAIN FRAME ################
if ($Form{'jscript'}) { &jscript; }

################ ELSE PARSE DEFULT ROUTINE ################
else { &first; }

###########################################################
################ DEFAULT ROUTINE/MAIN PAGE ################
###########################################################
sub first {
	print "Content-type: text/html\n\n";
	$legal = `cat legal.nsf`;
	$pow = `cat pow_products.nsf`;
	## must have command to run search
	$powbutton = "";	

## START PRESS STUFF
## Capture saved PRESS RELEASES
$cstuff = "admin/press/releases/releases.dat";
$thestuff = `cat $cstuff`;

{
print <<EOF

<HTML>
<HEAD>
<TITLE>Coastline Micro, Inc. - Press Releases - $date</TITLE>
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
<script language="Javascript" src="$script?jscript=1&mousetable=1"></script>
<script language="JavaScript" src="js/menu_config.js"></script>
<LINK REL="STYLESHEET" HREF="common_css.html" Type="text/css">

</head>
<body bgcolor="#ffffff" text="#333366" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onLoad="javascript:loadScript();runSearch();">

<!-- Copyright NetMedia Solutions and Coasltine Micro, Inc.-->
<script language="Javascript" src="js/menu_constructor.js"></script>

<!-- Start header table -->
<table width="100%" border="0" cellspacing="0" cellpadding="0" background="images/newones/top_tablebg_main.jpg" height="100">
  <tr> 
    <td width="30%"><img src="images/newones/illus_aboutus.jpg" width="250" height="100" border="0"></td>
    <td align="right" valign="middle" width="70%"><font size="1" color="#ffffff" face="verdana,arial,helvetica">$date&nbsp;&nbsp;<font size="3">&nbsp;</font></font>
	<center><img src="images/newones/title_press.jpg" width="350" height="80" align="bottom"></center></td>
  </tr>
</table>
<!-- End header table -->

<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td width="175" align=left valign=top><img src="images/newmenu/place_holder.gif" width="175" height="150"><img src="images/spacer.gif" width="190" height="20" border="0">$powbutton $legal</td>
    <td width="5"><img src="images/140spacer.gif" width="5" height="8"></td>
    <td width="100%" align="center" valign=top><br>

 <!-- START DROP ME TABLE-->
<table width="90%" border="0" cellspacing="0" cellpadding="0" align="center">
  <tr> 
    <td> 
      <table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td width="12" height="24"><img src="images/table_top_left.gif" border=0 width="12" height="24"></td>
          <td bgcolor="#333366" align="center" width="50%">&nbsp;</td>
          <td align="center" width="30" height="24"><img src="images/table_top_mid.gif" border=0 width="30" height="24"></td>
          <td bgcolor="#8f8fab" align="center" width="50%"><b><font class="tableheading">Press Releases / News</font></b></td>
          <td align="right" height="24" width="12"><img src="images/table_top_right.gif" border=0 width="12" height="24"></td>
        </tr>
      </table>
    </td>
  </tr>
  <tr bgcolor="#333366" align="center"> 
    <td> <br>
      <table width="95%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td>  
            <p>
            <font class="regtextnobold">Below you will find a list of press releases 
            and information briefs about Coastline Micro. If you are looking for 
            specific corporate information about Coastline Micro and have not 
            found it on this site, please feel free to contact a Customer Service 
            Representative with your questions or concerns. We will make every 
            effort to answer your question within 24 hours of your request. <br><br><br><br>

<table cellpadding="0" cellspacing="0" border="0" align="center" width="100%">
  <tr>
  <td width="100%" align="left">
<ul>
<font class="regtextnobold" color="#FFFFFF">
EOF
}

################# START parse form ##################
@lines = split(/:end\n/, $thestuff);
$count=1;
    foreach $line (@lines) {
		## add more years here...
		if ($line =~ "year2006") { push(@sixlines,"$line"); }
		elsif ($line =~ "year2005") { push(@fivelines,"$line"); }
		elsif ($line =~ "year2004") { push(@fourlines,"$line"); }
		elsif ($line =~ "year2003") { push(@threelines,"$line"); }
		elsif ($line =~ "year2002") { push(@twolines,"$line"); }
		elsif ($line =~ "year2001") { push(@onelines,"$line"); }
		elsif ($line =~ "year2000") { push(@zerolines,"$line"); }
		else { push(@older,"$line"); }
	}
	
	@sixsorted = reverse sort (@sixlines); 	
    foreach $line (@sixsorted) { &parseit; }
	@fivesorted = reverse sort (@fivelines); 	
    foreach $line (@fivesorted) { &parseit; }
	@foursorted = reverse sort (@fourlines); 	
    foreach $line (@foursorted) { &parseit; }
	@threesorted = reverse sort (@threelines); 	
    foreach $line (@threesorted) { &parseit; }
	@twosorted = reverse sort (@twolines); 	
    foreach $line (@twosorted) { &parseit; }
	@onesorted = reverse sort (@onelines); 	
    foreach $line (@onesorted) { &parseit; }
	@zerosorted = reverse sort (@zerolines); 	
    foreach $line (@zerosorted) { &parseit; }
	@oldersorted = reverse sort (@older); 	
    foreach $line (@oldersorted) { &parseit; }	

################# END parse form ##################

{
print <<EOF
</font>
</ul>
</td></tr>
</table>

             </td>
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
 <!-- END DROP ME TABLE-->	
	</td>
  </tr>
</table>

<!-- Dynamic Moving Layers -->
$pow
</body>
</html>
  
EOF
}
exit;
}

sub parseit {
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
	print "<li><A HREF=\"$script?viewRel=$Saved{'file'}\"><b>$Saved{'date'} - </b>$Saved{'title'}</A><br><br><br></li>";
}

################################################################################
################ Admin Tool Internal JavaScript w/call function ################
################################################################################
sub jscript {
print "Content-type: text/html\n\n";
if ($Form{'mousetable'} eq "1") {
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

####################################################
################ VIEW PRESS RELEASE ################
####################################################
sub viewRel {
$viewRel = "$Form{'viewRel'}";
require ("admin/press/releases/$viewRel.sms");
print "Content-type: text/html\n\n";
if ($myfoot != "") {
	require ("admin/press/coastfoot/$myfoot.foot");
	$breakone = "<br><br><br>";
	$yourtitle = "<b>$foottitle</b><br>";
	$yourlink = "<br><center><a href=\"$footlink\" target=\"_top\"><<< More Info >>></a></center>";
	$yourbody = $footbody;
	}
else { 
	$breakone = "";
	$yourtitle = "";
	$yourlink = "";
	$yourbody = "";
	}
		
	## common dhtml stuff
	$legal = `cat legal.nsf`;
	$pow = `cat pow_products.nsf`;
	## must have command to run search
	$powbutton = "";	
{
print <<EOF

<HTML>
<HEAD>
<TITLE>Coastline Micro, Inc. - Press Releases - $date</TITLE>
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
<SCRIPT LANGUAGE="JavaScript">
//run current window
function runForm(thisone) {
window.open('$script?viewRel='+thisone+'','POLLS','width=550,height=595,scrollbars=yes');
}

</SCRIPT>
<script language="JavaScript" src="js/reload.js"></script>

<!--FOLLOWING EXTERNAL SCRIPT IS USED FOR BROWSER TESTING AND IS INTEGRAL PART OF POW-->
<script language="JavaScript" src="js/dynlayer.js"></script>
<!--END-->

<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta name="keywords" content="coastlinemicro.com, www.coastlinemicro.com, coastline, micro, irvine, ca, california, about, company, location, businsess, competition, competitors, solutions, irvine, california, technology, ceo, own, partner, fast, reliable, heritage, sophisticated, computer, system, build, custom, sample, guarantee, search, product">
<meta name="description" content="Coastline Micro Inc. is in business to develop hardware solutions that make sense for the small to corporate sized business arena. We have been in business for over a decade and have the knowledge and expertise necessary to be competitive in the market. Our every product carries a 100% Product Satisfaction Guarantee. We are located in Irvine, California at 60 N. Technology Drive. For more information about our company and its what it is in business to do please follow the link above. Our company's Heritage dates back to 1989.">
<script language="Javascript" src="$script?jscript=1&mousetable=1"></script>
<script language="JavaScript" src="js/menu_config.js"></script>
<LINK REL="STYLESHEET" HREF="common_css.html" Type="text/css">

</head>
<body bgcolor="#ffffff" text="#333366" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onLoad="javascript:loadScript();runSearch();">

<!-- Copyright NetMedia Solutions and Coasltine Micro, Inc.-->
<script language="Javascript" src="js/menu_constructor.js"></script>

<!-- Start header table -->
<table width="100%" border="0" cellspacing="0" cellpadding="0" background="images/newones/top_tablebg_main.jpg" height="100">
  <tr> 
    <td width="30%"><img src="images/newones/illus_aboutus.jpg" width="250" height="100" border="0"></td>
    <td align="right" valign="middle" width="70%"><font size="1" color="#ffffff" face="verdana,arial,helvetica">$date&nbsp;&nbsp;<font size="3">&nbsp;</font></font>
	<center><img src="images/newones/title_press.jpg" width="350" height="80" align="bottom"></center></td>
  </tr>
</table>
<!-- End header table -->

<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td width="175" align=left valign=top><img src="images/newmenu/place_holder.gif" width="175" height="150"><img src="images/spacer.gif" width="190" height="20" border="0">$powbutton $legal</td>
    <td width="5"><img src="images/140spacer.gif" width="5" height="8"></td>
    <td width="100%" align="center" valign=top><br>

 <!-- START DROP ME TABLE-->
<table width="90%" border="0" cellspacing="0" cellpadding="0" align="center">
  <tr> 
    <td> 
      <table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td width="12" height="24"><img src="images/table_top_left.gif" border=0 width="12" height="24"></td>
          <td bgcolor="#333366" align="center" width="50%">&nbsp;</td>
          <td align="center" width="30" height="24"><img src="images/table_top_mid.gif" border=0 width="30" height="24"></td>
          <td bgcolor="#8f8fab" align="center" width="50%"><b><font class="tableheading">Press Releases / News</font></b></td>
          <td align="right" height="24" width="12"><img src="images/table_top_right.gif" border=0 width="12" height="24"></td>
        </tr>
      </table>
    </td>
  </tr>
  <tr bgcolor="#333366" align="center"> 
    <td> <br>
      <table width="95%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td>
		  
<font class="regtextbold"><b>$location - $date</b></font>
<br><br>
<font class="regtextnobold"><b>$title</b>
<br>
$para1
</font>
<table width="90%" align="center" cellpadding="0" cellspacing="0" border="0">
<tr><td width="100%" align="left">
<font class="topnavi">
$breakone
$yourtitle
$yourbody $yourlink

EOF
}

if ($partners eq "" || $partners eq " " ) { $no=1; }
else { 	
	@feetses = split(/,/, $partners);
		foreach $myfeet (@feetses) {
			require ("admin/press/otherfoot/$myfeet.foot");
			print "<br><br><br>";
			print "<b>$foottitle</b><br>";
			print "$footbody <br><center><a href=\"$footlink\" target=\"new\"><<< More Info >>></a></center>";
	   	}
}

{
print <<EOF

<br><br>
</font>		
</td></tr>
</table>  
		  </td>
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
 <!-- END DROP ME TABLE-->	
	</td>
  </tr>
</table>

<!-- Dynamic Moving Layers -->
$pow

</body>
</html>

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