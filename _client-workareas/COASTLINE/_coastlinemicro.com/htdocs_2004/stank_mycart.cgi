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

require ("referer.nsp"); 
require ("parse_query.nsp");
require ("date.nsp");

$browser = "$ENV{'HTTP_USER_AGENT'}";
if (($browser =~ "Mozilla/" && $browser =~ "6.") || $browser =~ "Netscape6") { $tablewidth = "100%"; $t1 = "5"; $t2 = "64%"; $t3 = "18%"; $t4 = "18%"; $t5 = "100%"; }	
else { $tablewidth = "470"; $t1 = "5"; $t2 = "339"; $t3 = "79"; $t4 = "42"; $t5 = "470"; }
if ($browser =~ "Mozilla/4.7") { $border = "border=\"1\" bordercolor=\"#333366\""; }

if ($browser =~ "MSIE 5.0" || $browser =~ "MSIE 5.5" || $browser =~ "Mozilla/4.7" || $browser =~ "MSIE 4.0") { $StartURLer="javascript:void(0);\" onClick=\"javascript:window.open"; $EndURLer=",'EMAILIT','width=485,height=590');";}
else { $StartURLer="javascript:trigger"; $EndURLer=");";}

$STANKLEGAL = `cat stank_legal.nsf`;

## Snif cookie, if present test for logged in status
require ("cookiesnif.nsp");

## ----------------->>> Must Be Logged In!
if ($Cookies{'Echado'} eq "YES") {

##----------->>> CONNECT TO DB
use DBI;
my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
$dbh->{RaiseError} = 1; 

$count=0;
if ($Cookies{'CNFIGS'} ne "") {

	@EstosCNFIGS = split(/,/, $Cookies{'CNFIGS'});
	foreach $EsteCNFIG (@EstosCNFIGS) {
		@muaCF = split(/-----/, $EsteCNFIG);
		$ConfigID = "$muaCF[0]";

		## IF RESTACKING AND OLD CNFIG DOES NOT HAVE (%%) COUNTER
		if ($FORM{'reStackit'} eq "YES") {
			$laCuenta = $FORM{$ConfigID};
		}
		else {
			$laCuenta = "$muaCF[1]";
		}

		## GET CONFIGURATION INFORMATION
		my $sth = $dbh->prepare("SELECT * FROM Configs WHERE ConfigID='$ConfigID'");
		$sth->execute or die "Unable to execute query\n";
		my @row;
		while(@row = $sth->fetchrow_array) {
			$Parent = $row[1];
			$CMSeries = $row[3];
			$ProductIDs = $row[4];
			$TotalPrice = $row[7];
			$TotalWeight = $row[8];
			$CreatedOn = $row[9];
			if ($ConfigID != $FORM{'DelConfig'}) {
				if ($laCuenta > 0) {
					push(@Configs,"$Parent=====$CMSeries=====$ProductIDs=====$TotalPrice=====$TotalWeight=====$CreatedOn=====$ConfigID=====$laCuenta");

					## how many calls for this config? IF more than one tally in as many as there are specified
					if ($laCuenta eq "1") { push(@losPrecios,$TotalPrice); }
					else {
						foreach (1 .. $laCuenta) {
							push(@losPrecios,$TotalPrice);
						}
					}

				}
			}
			$count++;
		}
		$sth->finish;
	}
}

## add cart totals
$PCount=0;
foreach $elPrecio (@losPrecios) {
$PCount++;
	if ($PCount eq "1") { $EntireTotal = $elPrecio; }
	else { $EntireTotal = $EntireTotal + $elPrecio; }
	$EntireTotal = sprintf("%.2f", $EntireTotal);
}

## NS PRINT FUNCTION
if ($FORM{'NSPRINT'}) { $NSPrinter = "onload=\"javascript:printPageNS();\""; }

$MainTitle = "Your Shark Tank&#153; Cart";

## IF DELETING A CONFIGURATION RESET CART
$DelCount=0;
if ($FORM{'reStackit'} eq "YES" || $FORM{'DelConfig'} > 0) {
	foreach $oldStack (@Configs) {
		$DelCount++;
		@cutStack = split(/=====/, $oldStack);
		$elConfig = $cutStack[6];
		$suCuenta = $cutStack[7];
		if ($DelCount eq "1") { $newConfigs = $elConfig . "-----" . $suCuenta; }
		else { $newConfigs = $newConfigs . "," . $elConfig . "-----" . $suCuenta; }
	}
	print "Content-type: text/html\n";
	&SetCookies('Echado','YES');
	&SetCookies('CeeEmmNo', "$Cookies{'CeeEmmNo'}");
	&SetCookies('EDomi', "$Cookies{'EDomi'}");
	&SetCookies('GID', "$Cookies{'GID'}");
	&SetCookies('FiNo', "$Cookies{'FiNo'}");
	&SetCookies('LaNo', "$Cookies{'LaNo'}");
	&SetCookies('UTipe', "$Cookies{'UTipe'}");
	&SetCookies('CoNo', "$Cookies{'CoNo'}");
	&SetCookies('DTV', "$Cookies{'DTV'}");
	&SetCookies('SRV', "$Cookies{'SRV'}");
	&SetCookies('NBV', "$Cookies{'NBV'}");
	&SetCookies('MOV', "$Cookies{'MOV'}");
	&SetCookies('MYV', "$Cookies{'MYV'}");
	&SetCookies('HDV', "$Cookies{'HDV'}");
	&SetCookies('VDV', "$Cookies{'VDV'}");
	&SetCookies('PHV', "$Cookies{'PHV'}");
	&SetCookies('PRV', "$Cookies{'PRV'}");
	&SetCookies('SWV', "$Cookies{'SWV'}");
	&SetCookies('CNFIGS', "$newConfigs");
	&SetCookies('PTIES', "$Cookies{'PTIES'}");
    # End the headers by laying last \n
   	print "\n";
}
## IF NOT LEAVE IT
else {
	print "Content-type: text/html\n\n";
}

{
print <<EOF

<html>
<head>
<title>Coastline Micro Inc.</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="common_css.html?anchor=333366&anchorov=EB0000&weight=normal&weightov=normal&decor=underline&decorov=underline" Type="text/css">
<STYLE TYPE="text/css">
body { background-color:#ffffff; scrollbar-face-color:#F2F2F7; scrollbar-highlight-color:#F2F2F7; scrollbar-shadow-color:#8f8fab; scrollbar-3dlight-color: #333366; scrollbar-arrow-color:#333366; scrollbar-track-color:#F2F2F7; scrollbar-darkshadow-color:#8f8fab; }
</STYLE>
<script language="Javascript" src="js/mousetable.js"></script>
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

// QUICK CROSS-BROWSER MOUSE-OVER/OFF FUNCTIONS
// By Drlouie \@ NetMedia Solutions
// info\@NetMediaSol.com for help
// Copyright 2001 NetMedia Solutions

function imageOffDHTML(which,thisone) {
	var cual = 	"images/tables/but_"+which+"_"+thisone+".gif";
	document.images[which].src = cual;
}
function imageOnDHTML(which,thisone) {
	var cual = 	"images/tables/but_"+which+"_"+thisone+".gif";
	document.images[which].src = cual;
}

function imageOffDHTML2(which,thei,thisone) {
	var cual = 	"images/db/but_"+thei+"_"+thisone+".gif";
	document.images[which].src = cual;
}
function imageOnDHTML2(which,thei,thisone) {
	var cual = 	"images/db/but_"+thei+"_"+thisone+".gif";
	document.images[which].src = cual;
}
</SCRIPT>
<script language="javascript">

///////////////////////////////////////////////////////////////////
// This script and its counterparts are ©2001 NetMedia Solutions //
// For use ONLY with CoastlineMicro.com                          //
// To re-use or have this script re-interfaced for your specific //
// needs please contact SServices\@NetMediaSolutions.com         //
// Prices are cheap for re-interfacing of current scripts and    //
// programs, so email us today to get you own LEGAL programming  //
// licensed for use only on YOUR site(s) or for YOUR purpose(s). //
///////////////////////////////////////////////////////////////////

<!--
function trigger(myurl) {
var b = navigator.appName;
if (b=="Netscape" && navigator.userAgent.indexOf("6.")) {
	this.location.href=myurl;
	}
else if (b=="Netscape") {
	mainFrame = parent.frames.botOne;
	mainFrame.frame.loadpage(''+myurl+'');
}
else {
	this.location.href=myurl;
	}
}
//-->
</script>
<script language="javascript">

///////////////////////////////////////////////////////////////////
// This script and its counterparts are ©2001 NetMedia Solutions //
// For use ONLY with CoastlineMicro.com                          //
// To re-use or have this script re-interfaced for your specific //
// needs please contact SServices\@NetMediaSolutions.com         //
// Prices are cheap for re-interfacing of current scripts and    //
// programs, so email us today to get you own LEGAL programming  //
// licensed for use only on YOUR site(s) or for YOUR purpose(s). //
///////////////////////////////////////////////////////////////////

function abrete(me) {
	parent.window.open(me,'VCONFIG','width=600,height=600');
}
</script>
<base href="http://www.coastlinemicro.com/">
</head>
<body bgcolor="#ffffff" text="#8F8FAB" leftmargin="0" topmargin="0" marginwidth="0" scroll="yes" marginheight="0">
<form name="leCart" action="stank_mycart.html" method="post">
<input type="hidden" name="reStackit" value="YES">
<table width="$tablewidth" border="0" cellspacing="0" cellpadding="0">
  <tr> 
    <td align="center" valign="middle" width="$tablewidth" height="25"> 
      <table width="$tablewidth" border="0" cellspacing="0" cellpadding="0" background="images/tables/topbar.jpg" height="24">
        <tr> 
          <td width="$t1"><img src="images/tables/topbar_left.jpg" width="5" height="24"></td>
          <td width="$t2"><nobr><font class="btext">&nbsp;&nbsp;<b>$MainTitle</b></font></nobr></td>
          <td width="$t3" align="center" valign="top">&nbsp;</td>
          <td width="$t4" align="center" valign="top">&nbsp;</td>
          <td width="$t1" align="left" valign="top"><img src="images/tables/topbar_right.jpg" width="5" height="24"></td>
        </tr>
      </table>
    </td>
  </tr>
  <tr> 
    <td align="center"> 
      <table width="$tablewidth" border="0" cellspacing="0" cellpadding="0" height="30">
        <tr align="center"> 
          <td width="20%" align="left"><img src="images/tables/icon_back_off.gif" width="60" height="20" name="back" border="0"></td>
          <td width="16%"><img src="images/tables/but_configureit_dn.gif" width="81" height="20" name="configureit" border="0"></td>
          <td width="16%"><img src="images/tables/but_techspecs_dn.gif" width="77" height="20" name="techspecs" border="0"></td>
          <td width="16%"><img src="images/tables/but_sysdrivers_dn.gif" width="78" height="20" name="sysdrivers" border="0"></td>
          <td width="16%"><img src="images/tables/but_lphoto_dn.gif" width="75" height="20" name="lphoto" border="0"></td>
          <td width="16%"><img src="images/tables/but_multimedia_dn.gif" width="73" height="20" name="sysmedia" border="0"></td>
        </tr>
      </table>
    </td>
  </tr>
  <tr> 
    <td valign="top"> 
      <table width="$tablewidth" border="0" cellspacing="1" cellpadding="0" align="center">
        <tr> 
          <td valign="top" width="$t5"> 
            <table width="100%" cellspacing="1" cellpadding="0" bgcolor="#FFFFFF">
              <tr> 
                <td> 
                  <table width="100%" cellspacing="0" cellpadding="0" bgcolor="#F2F2F7" class="stankth" height="18" $border>
                    <tr> 
                      <td align="center"><font class="btext"><b>Contents of your Cart</b></font></td>
                    </tr>
                  </table>
                </td>
              </tr>
              <tr> 
                <td> 
                  <table width="100%" cellspacing="0" cellpadding="2" class="stankth" $border>
                    <tr> 
                      <td valign="top"><br>
					  
EOF
}

if (@Configs) {

print "
<table width=\"85%\" align=\"center\" cellpadding=\"3\" cellspacing=\"0\" border=\"0\">
<tr> 
<td width=\"100%\" valign=\"top\"><font class=\"stankprice\"><center><b>Your Cart's Total \$$EntireTotal</b></center></font><br><font class=\"btext\">The contents of your cart consists of either:<br><br><li type=\"circle\"><img src=\"images/checkbox_green.gif\" border=\"0\">&nbsp;&nbsp;&nbsp;<b>Configurations</b> (Systems)</li><li type=\"circle\"><img src=\"images/checkbox_red.gif\" border=\"0\">&nbsp;&nbsp;&nbsp;<b>Other Products</b> (IE: Mouse, NIC, ETC...)</li><br><br>
To purchase these items simply click 'Check Out!'. To change the the contents of your cart click 'Update Cart!'. Use the 'Act' button(s) or the 'Quantity' field(s) to alter the contents of your cart. </font></td>
</tr>
</table>
<br>
<table width=\"100%\" align=\"center\" cellpadding=\"2\" cellspacing=\"0\" border=\"0\">
<tr> 
<td width=\"65%\" valign=\"top\">
<table width=\"95%\" align=\"center\" cellspacing=\"0\" cellpadding=\"0\" class=\"stankth\" height=\"18\" $border>
<tr height=\"12\" bgcolor=\"#F2F2F7\"><td width=\"4%\" align=\"center\">&nbsp;</td><td align=\"center\" width=\"17%\"><font class=\"btext\"><b>CFGID</b></font></td><td width=\"45%\"><font class=\"btext\"><b>System's Name</b></font></td><td width=\"18%\" align=\"center\"><font class=\"btext\"><b>Price</b></font></td><td width=\"8%\" align=\"center\"><font class=\"btext\"><b>Qty.</b></font></td><td align=\"center\" width=\"8%\" align=\"center\"><font class=\"btext\"><b>Act</b></font></td></tr>
</table>

<table width=\"95%\" align=\"center\" cellspacing=\"0\" cellpadding=\"0\" border=\"0\" height=\"1\">
<tr height=\"1\"><td width=\"100%\"><img src=\"images/spacer.gif\" border=\"0\" height=\"1\" width=\"1\"></td></tr>
</table>

<table width=\"95%\" align=\"center\" cellspacing=\"0\" cellpadding=\"0\" class=\"stankth\" height=\"18\" $border>
<tr height=\"10\"><td width=\"100%\" colspan=\"5\"><img src=\"images/spacer.gif\" border=\"0\" height=\"10\" width=\"1\"></td></tr>
";
	$CFGCount=0;
	foreach $Config (@Configs) {
	$CFGCount++;
		@leConfig = split(/=====/, $Config);
		$leParent = "$leConfig[0]";
		$leCMSeries = "$leConfig[1]";
		$leProductIDs = "$leConfig[2]";
		$leTotalPrice = "$leConfig[3]";
		$leTotalWeight = "$leConfig[4]";
		$leCreatedOn = "$leConfig[5]";
		$leConfigID = "$leConfig[6]";
		$leCuenta = "$leConfig[7]";
		$leCuenta = $leCuenta;
		my $sth = $dbh->prepare("SELECT * FROM Products WHERE CMPartNum='$leParent'");
		$sth->execute or die "Unable to execute query\n";
		my @row;
		while(@row = $sth->fetchrow_array) {
			$MuaNombre = $row[11];
			$MuaSPhoto = $row[17];
			$MuaWarr = $row[19];
			$MuaAccessories = $row[24];
		}
		$sth->finish;
		print "<tr height=\"45\"><td valign=\"top\" width=\"4%\" align=\"right\"><img src=\"images/checkbox_green.gif\" border=\"0\"></td><td valign=\"top\" align=\"center\" width=\"17%\"><font class=\"btext\">$leConfigID</font></td><td valign=\"top\" width=\"45%\"><font class=\"btext\">$MuaNombre</font></td><td width=\"18%\" valign=\"top\" align=\"center\"><font class=\"btext_red\">$leTotalPrice</font></td><td valign=\"top\" width=\"8%\" align=\"center\"><input type=\"text\" value=\"$leCuenta\" class=\"inputtext3\" name=\"$leConfigID\"></td><td valign=\"top\" align=\"center\" width=\"8%\" align=\"center\"><a href=\"javascript:trigger('stank_mycart.html?DelConfig=$leConfigID');\" onMouseOver=\"javascript:imageOnDHTML2('D_$CFGCount','delete','ov');\" onMouseOut=\"javascript:imageOffDHTML2('D_$CFGCount','delete','off');\"><img src=\"images/db/but_delete_off.gif\" border=\"0\" name=\"D_$CFGCount\" alt=\"Remove this item from your cart...\"></a><br>
		<a href=\"javascript:abrete('stank_vconfig.html?CID=$leConfigID&InnerLink=1');\" onMouseOver=\"javascript:imageOnDHTML2('I_$CFGCount','info','ov');\" onMouseOut=\"javascript:imageOffDHTML2('I_$CFGCount','info','off');\"><img src=\"images/db/but_info_off.gif\" width=\"12\" height=\"12\" vspace=\"5\" border=\"0\" name=\"I_$CFGCount\" alt=\"Click for more information about this configuration...\"></a></td></tr>";
	}

	print "<tr height=\"20\" bgcolor=\"#F2F2F7\"><td valign=\"middle\" width=\"34%\" align=\"right\" colspan=\"3\"><font class=\"btext\"><b>Cart Total</b> (No shipping included) &nbsp;</font></td><td valign=\"middle\" width=\"18%\" align=\"center\"><font class=\"btext_red\"><b>\$$EntireTotal</b></font></td><td valign=\"middle\" width=\"43%\" align=\"center\" colspan=\"2\"><font class=\"btext\">&nbsp;</font></td></tr>";
	
}

## if nothing in cart
else {

print "<table width=\"85%\" align=\"center\" cellpadding=\"3\" cellspacing=\"0\" border=\"0\">
<tr> 
<td width=\"100%\" valign=\"top\"><center><font class=\"stankprice\"><b>Your Cart's Total \$0</b></font><br><font class=\"btext\"><br><b>Your Shark Tank&#153; Shopping Cart is currently empty...</b><br><br><br></font></center></td>
</tr>
</table>";

}

{
print <<EOF

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
EOF
}

if (@Configs) {
print "<table width=\"95%\" align=\"center\" cellspacing=\"0\" cellpadding=\"0\" border=\"0\" height=\"1\">
<tr height=\"1\"><td width=\"100%\"><img src=\"images/spacer.gif\" border=\"0\" height=\"1\" width=\"1\"></td></tr>
</table>
	  
<table width=\"100%\" cellspacing=\"0\" cellpadding=\"0\" bgcolor=\"#F2F2F7\" class=\"stankth\" height=\"30\" $border align=\"center\" width=\"500\" bgcolor=\"#F2F2F7\">
	<tr>
    	<td align=\"center\" width=\"50%\" align=\"center\"><input type=\"submit\" value=\"Update Cart!\" class=\"pricebut\"></td>
    	<td align=\"center\" width=\"50%\" align=\"center\"><input type=\"button\" value=\"Check Out!\" class=\"pricebut\" onClick=\"javascript:trigger('stank_checkout.html');\"></td>
    </tr>
</table>";
}

{
print <<EOF
    </td>
  </tr>
</table>

<br>
<table width="$tablewidth" border="0" cellspacing="0" cellpadding="0"><tr><td align="center" width="$tablewidth"> 
$STANKLEGAL
</td></tr></table>

</form>
</body>
</html>

EOF
}

## DISCONNECT DB 
$dbh->disconnect; 

exit;
}


## SORRY YALL NO GOOD CALL
else {
$sorry = `cat sorry_nospec.nsf`;

{
print <<EOF

$sorry

EOF
}
exit;
}