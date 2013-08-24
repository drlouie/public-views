#!/usr/bin/perl5 -s

###########################################################################################################
# Company: �2001 NetMedia Solutions                                                                       #
# Date: Saturday, September 21, 2001                                                                      #
# Location: Los Angeles County, California, United States of America                                      #
# Made By: Luis Rodriguez (drlouie)                                                                       #
# Email: Drlouie@NetMediaSol.com                                                                          #
#                                                                                                         #
# This program cannot be duplicated, distributed or re-used for any other purpose other than its original #
# intended purpose and function. You may request NetMedia Solutions for a copy of the script,             #
# personalized to fit your exact needs for a small re-programming fee.                                    #
###########################################################################################################

require ("referer.nsp"); 
require ("parse_query.nsp");
require ("date.nsp");

$legal = `cat legal.nsf`;
require ("whichpow2.nsp");
$pow = `cat pow_products.nsf`;
## must have command to run search
$powbutton = "";	

print "Content-type: text/html\n\n";

{
print <<EOF

<html>
<head>
<title>Coastline Micro Inc. - Advanced Inventory Search</title>
<SCRIPT LANGUAGE="JavaScript">
parent.frames.topOne.location.href = "topframe.html";
</script>
<script language="JavaScript" src="js/reload.js"></script>

<!--FOLLOWING EXTERNAL SCRIPT IS USED FOR BROWSER TESTING AND IS INTEGRAL PART OF POW-->
<script language="JavaScript" src="js/dynlayer.js"></script>
<!--END-->

<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta name="keywords" content="coastlinemicro.com, www.coastlinemicro.com, coastline, micro, irvine, ca, california, about, company, location, businsess, competition, competitors, solutions, irvine, california, technology, ceo, own, partner, fast, reliable, heritage, sophisticated, computer, system, build, custom, sample, guarantee, search, product">
<meta name="description" content="Coastline Micro Inc. is in business to develop hardware solutions that make sense for the small to corporate sized business arena. We have been in business for over a decade and have the knowledge and expertise necessary to be competitive in the market. Our every product carries a 100% Product Satisfaction Guarantee. We are located in Irvine, California at 60 N. Technology Drive. For more information about our company and its what it is in business to do please follow the link above. Our company's Heritage dates back to 1989.">
<script language="JavaScript" src="js/menu_config.js"></script>
<LINK REL="STYLESHEET" HREF="common_css.html" Type="text/css">
<script language="Javascript" src="js/mousetable.js"></script>
<style type="text/css">
body { scrollbar-face-color:#F2F2F7; scrollbar-highlight-color:#F2F2F7; scrollbar-shadow-color:#8f8fab; scrollbar-3dlight-color: #333366; scrollbar-arrow-color:#333366; scrollbar-track-color:#F2F2F7; scrollbar-darkshadow-color:#8f8fab; }
</style>

<script language="Javascript">
// FORM CHECKER FUNCTIONS
// By Drlouie \@ NetMedia Solutions
// info\@NetMediaSol.com for help
// Copyright 2001 NetMedia Solutions

function checkForm() {
var missingdrop = "";
var thefirst = "";

// Check Common form fields
if (document.SuperSearch.SSKeys.value == "" || document.SuperSearch.SSKeys.value == " ") {
    missingdrop += "\\n     - You must type in Search Keyword(s)...";
}

// If anything comes back wrong alert and detain form, else submit info
if (missingdrop != "") {
    missingdrop ="___________________________________________                   \\n\\n" + "  Sorry, I cannot process your request because the\\n  following fields are either blank or filled incorrectly:\\n" + "___________________________________________                   \\n\\n" +
    missingdrop + "\\n\\n___________________________________________                   " + "\\n\\n   To continue, check fields and submit form again!" + "\\n___________________________________________";
    alert(missingdrop);
	document.SuperSearch.SSKeys.focus();
    return false;
} 
else {
return true;
}
}
</SCRIPT>
</head>
<body bgcolor="#ffffff" text="#333366" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onLoad="javascript:runSearch();">

<!-- Copyright NetMedia Solutions and Coasltine Micro, Inc.-->
<script language="Javascript" src="js/menu_constructor.js"></script>

<!-- Start header table -->
<table width="100%" border="0" cellspacing="0" cellpadding="0" background="images/newones/top_tablebg_main.jpg" height="100">
  <tr> 
    <td width="30%"><img src="images/newones/illus_products.jpg" width="250" height="100" border="0"></td>
    <td align="right" valign="middle" width="70%"><font size="1" color="#ffffff" face="verdana,arial,helvetica">$date&nbsp;&nbsp;<font size="3">&nbsp;</font></font>
	<center><img src="images/newones/title_advancedsearch.jpg" width="350" height="80" align="bottom"></center></td>
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
<form name="SuperSearch" method="post" action="ss_prod.html" onSubmit="return checkForm();">
      <table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td width="35%"><font class="stextbig"><b>Advanced Inventory Search</b></font></td>
          <td align="right" width="65%">&nbsp;</td>
        </tr>
        <tr bgcolor="#333366"><td colspan="2" height="1"><img src="images/spacer.gif" width="1" height="1"></td></tr>
        <tr><td colspan="2" height="15"><img src="images/spacer.gif" width="1" height="15"></td></tr>
        <tr> 
          <td colspan="2" align="left" width="100%">

<table width="100%" border="0" cellspacing="0" cellpadding="2" align="center">
<tr>
<td width="100%" valign="top" class="stankth">

<table width="95%" border="0" cellspacing="0" cellpadding="2" align="center">
<tr><td width="100%" height="15" colspan="2"><img src="images/spacer.gif" width="1" height="1"></td></tr>
<tr><td width="30%" height="35"><font class="btext4"><b>Search Term(s)</b></font></td><td width="70%"><input type="text" name="SSKeys" value="" size="35" class="inputtext35"></td></tr>
<tr><td width="30%" height="35"><font class="btext4"><b>By Manufacturer</b></font></td><td width="70%">
                    <select name="SSMFG" size="1" class="inputtext">
                      <option value="BIGNULL">All Manufacturers</option>
                      <option value="0000000001">Coastline Micro, Inc.</option>
EOF
}

	## Get list of CM reps
	use DBI;
	my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $sth = $dbh->prepare("SELECT * FROM MFGs ORDER BY Name ASC");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
		while(@row = $sth->fetchrow_array) { 
		my $MFGID = $row[0];
		my $Name = $row[1];
		if ($MFGID != "0000000001") { print "<option value=\"$MFGID\">$Name</option>"; }
	}
	$sth->finish;
	$dbh->disconnect;
	## print closing select tag

{
print <<EOF
                    </select>
</td></tr>
<tr><td width="30%" height="35"><font class="btext4"><b>By Product Type</b></font></td><td>
                    <select name="SSType" size="1" class="inputtext">
                      <option value="All" selected>All Product Types</option>
                      <option value="BIGNULL"></option>
                      <option value="BIGNULL">---- Pre-Confgirued ---- </option>
                      <option value="Desktop">Desktop PCs</option>
                      <option value="Notebook">Notebook Computers</option>
                      <option value="Server">Net Servers</option>
                      <option value="BIGNULL"></option>
                      <option value="BIGNULL">---- Miscellaneous ---- </option>
                      <option value="Audio">Audio Equipment</option>
                      <option value="CDROM">CD-ROM Drives</option>
                      <option value="CDRW">CD-RW Drives</option>
                      <option value="DigitalCam">Digital Cameras</option>
                      <option value="DVDROM">DVD-ROM Drives</option>
                      <option value="Floppy">Floppy Drives</option>
                      <option value="HardDrive">Hard Drives</option>
                      <option value="InternetCam">Internet Cameras</option>
                      <option value="Joystick">Joysticks</option>
                      <option value="Keyboard">Keyboards</option>
                      <option value="Memory">Memory</option>
                      <option value="Modem">Modems</option>
                      <option value="Monitor">Monitors</option>
                      <option value="Networking">Networking</option>
                      <option value="NIC">Network Cards</option>
                      <option value="NoteExtra">Notebooks Extras</option>
                      <option value="Pointer">Pointer Devices</option>
                      <option value="UPS">Power Protection</option>
                      <option value="Printer">Printers</option>
                      <option value="Processor">Processors</option>
                      <option value="Scanner">Scanners</option>
                      <option value="Software">Software</option>
                      <option value="Speaker">Speakers</option>
                      <option value="Storage">Storage Devices</option>
                      <option value="SystemBoard">System Boards</option>
                      <option value="SystemChassis">System Chassis</option>
                      <option value="VideoCard">Video Cards</option>
                      <option value="WirelessNet">Wireless Networking</option>
                      <option value="ZipDrive">Zip Drives</option>
                      <option value="BIGNULL"></option>
                      <option value="BIGNULL">---- All Others ---- </option>
                      <option value="Peripheral">Peripherals (Catchall)</option>
                    </select>
</td></tr>
<tr><td width="30%" height="35"><font class="btext4"><b>CLM Number</b></font></td><td width="70%"><input type="text" name="SSCLMNum" value="" size="35" class="inputtext35"></td></tr>
<tr><td width="30%" height="35"><font class="btext4"><b>MFG Number</b></font></td><td width="70%"><input type="text" name="SSMFGNum" value="" size="35" class="inputtext35"></td></tr>
<tr><td width="30%" height="35"><font class="btext4"><b>Results Per Page</b></font></td><td width="70%">
                    <select name="SSResults" size="1" class="inputtext">
                      <option value="10" selected>10</option>
                      <option value="25">25</option>
                      <option value="50">50</option>
                      <option value="75">75</option>
                      <option value="100">100</option>
                    </select>
</td></tr>
<tr><td width="30%" height="50"><font class="btext4"><b>Order By</b></font></td><td width="70%">
                    <select name="SSOrder" size="1" class="inputtext">
                      <option value="OName" selected>Product Name</option>
                      <option value="OType">Type ( eg: Printer, Software, Peripheral )</option>
                    </select><br><font class="btext3red"><i>* All our systems are re-configurable - Price is flexible</i></font>
</td></tr>
<tr><td width="30%" height="35"><font class="btext4"><b>Show Images?</b></font></td><td width="70%"><a href="#" onClick="javascript:document.SuperSearch.SSImages[0].checked = true;"><font class="btext4">Yes <input type="radio" name="SSImages" value="YES" checked></font></a><font class="btext4">&nbsp;&nbsp;&nbsp;</font><a href="#" onClick="javascript:document.SuperSearch.SSImages[1].checked = true;"><font class="btext4">No <input type="radio" name="SSImages" value="NO"></font></a></td></tr>
<tr><td width="30%" height="35"><font class="btext4"><b>Show Descriptions?</b></font></td><td width="70%"><a href="#" onClick="javascript:document.SuperSearch.SSDescrip[0].checked = true;"><font class="btext4">Yes <input type="radio" name="SSDescrip" value="YES" checked></font></a><font class="btext4">&nbsp;&nbsp;&nbsp;</font><a href="#" onClick="javascript:document.SuperSearch.SSDescrip[1].checked = true;"><font class="btext4">No <input type="radio" name="SSDescrip" value="NO"></font></a></td></tr>
<tr><td width="100%" height="5" colspan="2"><img src="images/spacer.gif" width="1" height="1"></td></tr>
</table>

<table width="350" cellspacing="0" cellpadding="0" bgcolor="#F2F2F7" class="stankth" height="30" $border align="center" width="500" bgcolor="#F2F2F7">
	<tr>
    	<td align="center" width="50%" align="center" onMouseOver="this.style.backgroundColor='EB0000'" onMouseOut="this.style.backgroundColor='F2F2F7'"><input type="reset" value="Reset It!" class="pricebut"></td>
    	<td align="center" width="50%" align="center" onMouseOver="this.style.backgroundColor='EB0000'" onMouseOut="this.style.backgroundColor='F2F2F7'"><input type="submit" value="Find My Product" class="pricebut"></td>
    </tr>
</table>
<br>
</td>
</tr>
</table>


		</td>
        </tr>
        <tr><td colspan="2" height="15"><img src="images/spacer.gif" width="1" height="15"></td></tr>
        <tr bgcolor="#333366"><td colspan="2" height="1"><img src="images/spacer.gif" width="1" height="1"></td></tr>
            </table>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
	</form>
	</td>
  </tr>
</table>

<!-- Dynamic Moving Layers -->
$pow

</body>
</html>

EOF
}