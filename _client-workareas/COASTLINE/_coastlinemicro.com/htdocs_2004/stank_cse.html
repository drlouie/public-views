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

$CMPartNum = "$FORM{'CMPartNum'}";
$PricingClass = "$FORM{'PricingClass'}";
$ItemName = "$FORM{'ItemName'}";
$Warranty = "$FORM{'Warranty'}";
$CMSeries = "$FORM{'CMSeries'}";
$LasPartes = $FORM{'LasPartes'};
$ElPrecio = $FORM{'ElPrecio'};
$ElPeso = $FORM{'ElPeso'};
$Image = $FORM{'Image'};	

## ----------------->>> BACK BUTTON OR NO BACK BUTTON?
$ComingFrom = $FORM{'ComingFrom'};
$GoBack = "<a href=\"javascript:trigger('stank_reconfig.html?CMPartNum=$CMPartNum');\"><img src=\"images/tables/icon_back_on.gif\" width=\"60\" height=\"20\" name=\"back\" border=\"0\"></a>";

##---------------------------->>> CONFIGURE SYSTEM INFORMATION AND IMAGERY FOR OUTPUT
$MainTitle = "$CMSeries&#153; Series System Saver";
if ($CMSeries eq "GreatWhite") { $ITitle = "gw"; }
elsif ($CMSeries eq "Mako") { $ITitle = "mako"; }
elsif ($CMSeries eq "Reef") { $ITitle = "reef"; }
elsif ($CMSeries eq "Tiger") { $ITitle = "tiger"; }
elsif ($CMSeries eq "Thresher") { $ITitle = "thresher"; }
else { $ITitle = "store"; }

## RECONFIGURABLE?
$ConfigIT = "<img src=\"images/tables/but_configureit_dn.gif\" width=\"81\" height=\"20\" name=\"configureit\" border=\"0\">";

if ($FORM{'NSPRINT'}) { $NSPrinter = "onload=\"javascript:printPageNS();\""; }


## ----------------->>> EQUOTE
if (($FORM{'LasPartes'} ||  $FORM{'CID'}) && $FORM{'CartSaveEQuote'} eq "EQUOTE") {

use DBI;
my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
$dbh->{RaiseError} = 1; 

	$countfile = "EQCNT.cnt";
	open(COUNT,"$countfile") || &error('can not write to $countfile');
	$countEQ = <COUNT>;
	$countEQ++;
	close(COUNT);
	## write out current count on tracking file
	open(COUNT2,">$countfile") || &error('can not write to $countfile');
	flock(COUNT2, 2);
	print COUNT2 "$countEQ";
	flock(COUNT2, 8);
	close(COUNT2);
	
	$EQCNT = "$countEQ";
	
if ($Cookies{'Echado'} ne "" && $Cookies{'Echado'} ne " " && $Cookies{'Echado'} ne "NO") {
	$Username = "$Cookies{'GID'}";
	$CMCustNum = "$Cookies{'CeeEmmNo'}";
	$FirstName = "$Cookies{'FiNo'}";
	$LastName = "$Cookies{'LaNo'}";
	$Email = "$Cookies{'EDomi'}";
	$UTipe = "$Cookies{'UTipe'}";
	$CoNo = "$Cookies{'CoNo'}";
	$DTV = "$Cookies{'DTV'}";
	$SRV = "$Cookies{'SRV'}";
	$NBV = "$Cookies{'NBV'}";
	$MOV = "$Cookies{'MOV'}";
	$MYV = "$Cookies{'MYV'}";
	$HDV = "$Cookies{'HDV'}";
	$VDV = "$Cookies{'VDV'}";
	$PHV = "$Cookies{'PHV'}";
	$PRV = "$Cookies{'PRV'}";
	$SWV = "$Cookies{'SWV'}";

	my $sth = $dbh->prepare("SELECT * FROM Customers WHERE CMCustNum='$CMCustNum'");
	$sth->execute or die "Unable to execute query\n";
	my @row;
	while(@row = $sth->fetchrow_array) {
		$SavedPhone = $row[8];
	}
	$sth->finish;
	
	$Area = substr($SavedPhone, 0, 3);
	$Phone3 = substr($SavedPhone, 3, 3);
	$Phone4 = substr($SavedPhone, 6, 4);
}

else {
	$countfile2 = "GUCNT.cnt";
	open(COUNT2,"$countfile2") || &error('can not write to $countfile2');
	$countGU = <COUNT2>;
	$countGU++;
	close(COUNT2);
	## write out current count on tracking file
	open(COUNT3,">$countfile2") || &error('can not write to $countfile2');
	flock(COUNT3, 2);
	print COUNT3 "$countGU";
	flock(COUNT3, 8);
	close(COUNT3);
	
	$Username = "Guest_$countGU";
	$CMCustNum = "Guest_$countGU";
	$FirstName = "$FORM{'FirstName'}";
	$LastName = "$FORM{'LastName'}";
	$Email = "$FORM{'Email'}";
	$Area = "$FORM{'Area'}";
	$Phone = "$FORM{'Phone'}";
	$UTipe = "GuestUser";
	$CoNo = "$FORM{'CoNo'}";
	$DTV = "35";
	$SRV = "35";
	$NBV = "35";
	$MOV = "35";
	$MYV = "35";
	$HDV = "35";
	$VDV = "35";
	$PHV = "35";
	$PRV = "35";
	$SWV = "35";

	$Phone3 = substr($Phone, 0, 3);
	$Phone4 = substr($Phone, 3, 4);
}

	$Parent = "$FORM{'CMPartNum'}";
	$OrderIDs = "0";
	$ProductIDs = "$LasPartes";
	$TotalPrice = "$ElPrecio";
	$TotalWeight = "$ElPeso";
	push(@elConfig,"$Parent=-=-=$Username=-=-=$CMCustNum=-=-=$OrderIDs=-=-=$CMSeries=-=-=$ProductIDs=-=-=$TotalPrice=-=-=$TotalWeight=-=-=$CreatedOn=-=-=$CID");

$MainTitle = "Shark Tank&#153; Electronic Quoting System";

@splitConfig = split(/=-=-=/, $elConfig[0]);
$leParent = $splitConfig[0];
$leUser = $splitConfig[1];
$leCMC = $splitConfig[2];
$leOIDs = $splitConfig[3];
$leCMS = $splitConfig[4];
$lePIDs = $splitConfig[5];
$lePrice = $splitConfig[6];
$leWeight = $splitConfig[7];
$leCreated = $splitConfig[8];
$leCID = $splitConfig[9];

my $sth = $dbh->prepare("SELECT * FROM Products WHERE CMPartNum='$leParent'");
$sth->execute or die "Unable to execute query\n";
my @row;
while(@row = $sth->fetchrow_array) {
	$ProductNombre = $row[11];
	$SmallPhoto = $row[17];
}
$sth->finish;

my $sth = $dbh->prepare("SELECT * FROM Images WHERE ImageID='$SmallPhoto'");
$sth->execute or die "Unable to execute query\n";
my @row;
while(@row = $sth->fetchrow_array) { 
	$SavedFileName = $row[3];
	$SavedDesc = $row[8];
	$SmallImageN = "$SavedFileName"; 
	$SmallImageD= "$SavedDesc";
}
$sth->execute or die "Unable to execute query\n"; 
$sth->finish;

if ($leCMS eq "GreatWhite") { $leCMS = "gw"; }
elsif ($leCMS eq "Mako") { $leCMS = "mako"; }
elsif ($leCMS eq "Reef") { $leCMS = "reef"; }
elsif ($leCMS eq "Thresher") { $leCMS = "thresher"; }
else { $leCMS = "tiger"; }

if ($FORM{'InnerLink'} eq "1") {
	$CARTITLink = "&nbsp;"; 
	$RECONFIGLink = "&nbsp;";
	$LayerCSS = "#divNewsCont {position:absolute; left:150; top:12px; width:300px; height:80px; clip:rect(0px 300px 80px 0px); visibility:hidden; overflow:hidden;}\n";
	$LayerCSS2 = "#divNews     {position:absolute;}\n";
}
else { 
	$CARTITLink = "<a href=\"javascript:location.href = 'framer.html?subject=$leCMS&title=$leCMS&cartit=$leCID';\" onMouseOver=\"javascript:imageOnDHTML3('cartit','ov');\" onMouseOut=\"javascript:imageOffDHTML3('cartit','off');\"><img src=\"images/newones/cartit_off.gif\" border=\"0\" name=\"cartit\"></a>"; 
	$RECONFIGLink = "<a href=\"javascript:location.href = 'framer.html?subject=$leCMS&title=$leCMS&loadsys=$leParent';\" onMouseOver=\"javascript:imageOnDHTML3('reconfigit','ov');\" onMouseOut=\"javascript:imageOffDHTML3('reconfigit','off');\"><img src=\"images/newones/reconfigit_off.gif\" border=\"0\" name=\"reconfigit\"></a>";
	$LayerCSS = "#divNewsCont {position:absolute; top:12px; width:300px; height:80px; clip:rect(0px 300px 80px 0px); visibility:hidden; overflow:hidden;}\n";
	$LayerCSS2 = "#divNews     {position:absolute;}\n";
}

@losProductos = split(/,,,,,/, $lePIDs);
foreach $elProducto (@losProductos) {
	@splitItem = split(/-----/, $elProducto);	
	$MiCate = $splitItem[0];
	$MiNume = $splitItem[1];
	my $sth = $dbh->prepare("SELECT * FROM Products WHERE CMPartNum='$MiNume'");
	$sth->execute or die "Unable to execute query\n";
	my @row;
	while(@row = $sth->fetchrow_array) { 
		$Compania = $row[6];
		$ItemName = $row[11];
		$Description = $row[12];
		if ($Compania ne "" && $Compania ne " " && $Compania ne "NONE") { push(@Companias,"$Compania"); }
		if ($row[16] ne "" && $row[16] ne " ") { push(@emblems, "$row[16]"); }
		push(@theItems, "$MiCate-----$MiNume-----$ItemName-----$Description");
	}
	$sth->finish;
}

foreach $Company (@Companias) {
	my $sth = $dbh->prepare("SELECT * FROM MFGs WHERE ManufacturerID='$Company'");
	$sth->execute or die "Unable to execute query\n";
	my @row;
	while(@row = $sth->fetchrow_array) { 
		$MuaName = $row[1];
		$SImage = $row[18];
		if ($Company ne "" && $Company ne $LastCompany) { push(@Emblems,"$Company,,,,,$MuaName,,,,,$SImage"); $LastCompany = $Company; }
	}
	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish;
}

foreach $EmblemIt (@Emblems) {
	@EsteEmb = split(/,,,,,/, $EmblemIt);
	$MuaCompany = $EsteEmb[0];
	$MuaName = $EsteEmb[1];
	$MuaSImage = $EsteEmb[2];
	
	my $sth = $dbh->prepare("SELECT * FROM Images WHERE ImageID='$MuaSImage'");
	$sth->execute or die "Unable to execute query\n";
	my @row;
	while(@row = $sth->fetchrow_array) { 
		$InnerURL = $row[6];
		if ($lastImage ne "$InnerURL") { push (@leImagen, "<br><img src=\"/$InnerURL\" border=\"0\"><br>$MuaName\<br><br><br>"); }
		$lastImage = $InnerURL;
	}
	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish;
}


$SCuenta=0;
foreach $anItem (@theItems) {
	@splitCosas = split(/-----/, $anItem);	
	$Category = $splitCosas[0];
	$MiNume = $splitCosas[1];
	$MiEsteNombre = $splitCosas[2];
	$ItsDesc = $splitCosas[3];

	##--->> REFORMAT INCOMING DATA FOR PARSING
	$DCount = "0";
	@DescCount = split(//, $ItsDesc);
	foreach $DescDesc (@DescCount) { 
	$DCount++; 
		if ($DCount >= "50" && ($DescDesc eq "." || $DescDesc eq "!")) { 
			$ItsDesc = substr($ItsDesc, 0, $DCount); 
		} 
	}
	##--->> REFORMAT INCOMING DATA FOR PARSING
	$NCount = "0";
	@NameCount = split(//, $MiName);
	foreach $NameName (@NameCount) { 
	$NCount++; 
		if ($NCount >= "35" && $NameName eq " ") { 
			$MiEsteNombre = substr($MiEsteNombre, 0, $NCount); 
		} 
	}

	if ($SCuenta ne "0" && $lastCate ne "$Category") { print "<table width=\"100%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" bgcolor=\"#F2F2F7\"><tr><tr><td width=\"100%\" height=\"10\"><font size=\"-4\" face=\"verdana,arial,helvetica\">&nbsp;</font></td></tr></table><hr width=\"65%\" align=\"center\" size=\"1\" color=\"#333366\">"; }
	
	## check categories
	if ($lastCate ne "$Category") { 
		push (@leProductos, "<table width=\"100%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" bgcolor=\"#F2F2F7\"><tr><td height=\"20\" width=\"90%\" ><font class=\"btext4\">&nbsp;<b>$Category</b></font></td></tr><tr><td width=\"90%\" align=\"right\"><table width=\"95%\" border=\"0\" cellspacing=\"0\" cellpadding=\"3\"><tr><td colspan=\"2\" width=\"95%\" bgcolor=\"#FFFFFF\"><font class=\"btext3\"><a href=\"stank_viewprod.html?CMPartNum=$MiNume&ComingFrom=vconfig&OGPart=$leCID&InnerLink=1\">$MiEsteNombre</a></font></td><td rowspan=\"2\" width=\"5%\" height=\"15\" align=\"center\" valign=\"top\"><a href=\"stank_viewprod.html?CMPartNum=$MiNume&ComingFrom=vconfig&OGPart=$leCID\" onMouseOver=\"javascript:imageOnDHTML2('I_$SCuenta','info','ov');\" onMouseOut=\"javascript:imageOffDHTML2('I_$SCuenta','info','off');\"><img src=\"images/db/but_info_off.gif\" width=\"12\" height=\"12\" vspace=\"5\" border=\"0\" name=\"I_$SCuenta\"></a></td></tr><tr><td width=\"4%\" bgcolor=\"#FFFFFF\">&nbsp;</td><td width=\"91%\" bgcolor=\"#FFFFFF\"><font class=\"btext3\">$ItsDesc</font></td></tr></table></td></tr></table>"); 
	}
	else {
		push (@leProductos, "<table width=\"100%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" bgcolor=\"#F2F2F7\"><tr><td height=\"1\" width=\"90%\"><img src=\"images/spacer.gif\" width=\"1\" height=\"1\"></td></tr><tr><td width=\"90%\" align=\"right\"><table width=\"95%\" border=\"0\" cellspacing=\"0\" cellpadding=\"3\"><tr><td colspan=\"2\" width=\"95%\" bgcolor=\"#FFFFFF\"><a href=\"stank_viewprod.html?CMPartNum=$MiNume&ComingFrom=vconfig&OGPart=$leCID&InnerLink=1\"><font class=\"btext3\">$MiEsteNombre</font></a></td><td rowspan=\"2\" width=\"5%\" height=\"15\" align=\"center\" valign=\"top\"><a href=\"stank_viewprod.html?CMPartNum=$MiNume&ComingFrom=vconfig&OGPart=$leCID\"><img src=\"images/db/but_info_off.gif\" width=\"12\" height=\"12\" vspace=\"5\" border=\"0\" name=\"I_$SCuenta\"></a></td></tr><tr><td width=\"4%\" bgcolor=\"#FFFFFF\">&nbsp;</td><td width=\"91%\" bgcolor=\"#FFFFFF\"><font class=\"btext3\">$ItsDesc</font></td></tr></table></td></tr></table>"); 
	}
	$lastCate = "$Category";

$SCuenta++;
}

if ($FORM{'NMUSD'} eq "1") { 
	$lePrecious="<font class=\"stankprice\"><br><center>For faster service, feel free to give us a call anytime...</center></font><br>"; 
	$leType = "School District Program";
}
if ($FORM{'MSP'} eq "1") { 
	$lePrecious="<font class=\"stankprice\"><br><center>For faster service, feel free to give us a call anytime...</center></font><br>"; 
	$leType = "Intel&reg; Model School Program";
}
else { 
	$lePrecious="<br><font class=\"stankprice\"><center>System's Price<br><b>\$$TotalPrice</b></center></font>"; 
}

############		
## ----------------------->>> SEND EMAIL MESSAGE TO CM
############
my $SenderIn = "$Email($FirstName $LastName)";
my $Recipient = "mpnunez\@coastlinemicro.com";
my $Subby = "----->>> Shark Tank EQuote ID: $EQCNT";
use lib "/www/htdocs/MIME-Lite-2.117/lib/";
use MIME::Lite;
my $msg = MIME::Lite->new(
				From    =>$SenderIn,
                To      =>$Recipient,
                Subject =>$Subby,
                Type    =>'multipart/related'
                );
   $msg->attach(Type => 'text/html',
   Data => qq{ 

<html>
<head>
<title>Coastline Micro Inc.</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="http://www.coastlinemicro.com/common_css.html?anchor=333366&anchorov=EB0000&weight=normal&weightov=normal&decor=underline&decorov=underline" Type="text/css">
<STYLE TYPE="text/css">
body { background-color:#ffffff; scrollbar-face-color:#F2F2F7; scrollbar-highlight-color:#F2F2F7; scrollbar-shadow-color:#8f8fab; scrollbar-3dlight-color: #333366; scrollbar-arrow-color:#333366; scrollbar-track-color:#F2F2F7; scrollbar-darkshadow-color:#8f8fab; }
</STYLE>

<style type="text/css">
$LayerCSS
$LayerCSS2
.link { line-height:12px; font-family:verdana,arial,helvetica; font-size:10px; text-decoration:none; }
.nolink { line-height:12px; font-family:verdana,arial,helvetica; font-size:10px; text-decoration:none; font-weight:bold; }
.red { color:#EB0000; }
a { text-decoration:underline; }
a:hover { text-decoration:none; }
</style>

<base href="http://www.coastlinemicro.com/">
</head>
<body bgcolor="#ffffff" text="#8F8FAB" leftmargin="0" topmargin="0" marginwidth="0" scroll="yes" marginheight="0">
<br>
<table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
<tr height="40">
<td rowspan="2" width="15%" align="left" valign="top"><a href="http://www.coastlinemicro.com/"><img src="http://www.coastlinemicro.com/Mailbox/images/top_cm_logo.jpg" width="116" height="37" border="0"></a></td>
<td rowspan="2" align="center" valign="bottom" width="30%">&nbsp;</td>
<td width="55%" align="right" valign="bottom"><img src="http://www.coastlinemicro.com/Mailbox/images/god_bless_america.gif" width="118" height="35"></td>
</tr>
<tr><td colspan="3" width="100%" bgcolor="#FFFFFF" height="5"><img src="http://www.coastlinemicro.com/Mailbox/images/spacer.gif" width="2" height="5"></td></tr>
<tr><td colspan="3" width="100%" bgcolor="#8F8FAB" height="2"><img src="http://www.coastlinemicro.com/Mailbox/images/spacer.gif" width="2" height="2"></td></tr>
<tr><td colspan="3" width="100%" bgcolor="#FFFFFF" height="2"><img src="http://www.coastlinemicro.com/Mailbox/images/spacer.gif" width="2" height="2"></td></tr>
</table>
<table width="95%" align="center" cellspacing="0" cellpadding="0" border="1" bordercolor="#8F8FAB" class="comtableborder"><tr><td width="100%" valign="top">

<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr> 
    <td align="center" valign="middle" width="100%" height="25"> 
      <table width="100%" border="0" cellspacing="0" cellpadding="0" background="images/tables/topbar.jpg" height="24">
        <tr> 
          <td width="5"><img src="images/tables/topbar_left.jpg" width="5" height="24"></td>
          <td width="64%"><nobr><font class="btext">&nbsp;&nbsp;<b>$MainTitle</b></font></nobr></td>
          <td width="18%" align="center" valign="top">&nbsp;</td>
          <td width="18%" align="center" valign="top">&nbsp;</td>
          <td width="100%" align="left" valign="top"><img src="images/tables/topbar_right.jpg" width="5" height="24"></td>
        </tr>
      </table>
    </td>
  </tr>
  <tr> 
    <td align="left">
	 <table width="85%" border="0" cellspacing="1" cellpadding="0" align="center">
        <tr> 
          <td align="left" valign="top" width="100%">
		  <font class="btext3"><br>This Electronic Quote (E-Quote) request has been sent by <b>$FirstName $LastName</b> from <b>$CoNo</b>. Below you will find the components of the system <b>$FirstName $LastName</b> requested a quote for. He/She has been adviced that a Coastline Micro Representative would contact him/her in timely manner. Directly below is the <b>$FirstName's</b> contact information for user: <b>$Username</b><br><br><b>Program Type</b> - $leType<br><b>First and Last Name</b> - $FirstName $LastName<br><b>Company Name</b> - $CoNo<br><b>Email Address</b> - $Email<br><b>Phone Number</b> - ($Area) $Phone3-$Phone4<br><br><br><center><b>As always, thank you for using the Shark Tank&#153;, our prize winning e-commerce store.</b></center><br><br></font></td>
		</tr>
	 </table>
</td>
  </tr>
  <tr> 
    <td valign="top"> 
      <table width="100%" border="0" cellspacing="1" cellpadding="0" align="center">
        <tr> 
          <td align="center" valign="top" height="150" width="35%">
		  <font class="stankprice">$lePrecious<img src="/dbimages/prod_common/$SmallImageN" width="165" height="100" vspace="20" border="0" alt="$SmallImageD"></font>
            <table width="100%" cellspacing="1" cellpadding="0" bgcolor="#FFFFFF">
              <tr> 
                <td> 
                  <table width="100%" cellspacing="0" cellpadding="0" bgcolor="#F2F2F7" class="stankth" height="18" $border>
                    <tr> 
                      <td align="center"><font class="btext"><b>Trusted Performance By</b></font></td>
                    </tr>
                  </table>
                </td>
              </tr>
              <tr> 
                <td> 
                  <table width="100%" cellspacing="0" cellpadding="0" class="stankth" $border>
                    <tr> 
                      <td width="5%">&nbsp;</td><td align="center" width="90%"><font class="btext">
				
@leImagen
					  						<br></font></td><td width="5%">&nbsp;</td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </td>
          <td valign="top" width="65%"> 
            <table width="100%" cellspacing="1" cellpadding="0" bgcolor="#FFFFFF">
              <tr> 
                <td> 
                  <table width="100%" cellspacing="0" cellpadding="0" bgcolor="#F2F2F7" class="stankth" height="18" $border>
                    <tr> 
                      <td align="center"><font class="btext"><b>System Specifications</b></font></td>
                    </tr>
                  </table>
                </td>
              </tr>
              <tr> 
                <td> 
                  <table width="100%" cellspacing="0" cellpadding="2" class="stankth" $border>
                    <tr> 
                      <td> 

@leProductos

<table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#F2F2F7"><tr><tr><td width="100%" height="10"><font size="-4" face="verdana,arial,helvetica">&nbsp;</font></td></tr></table>
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
</table>

    </td>
  </tr>
</table>



<table width="95%" border="0" cellspacing="0" cellpadding="0"><tr><td align="center" width="100%"> 
$STANKLEGAL
</td></tr></table>

</body>
</html>
								}
                     );
        $msg->send();
		
		


###########	
## ----------------------->>> SEND EMAIL MESSAGE TO USER
###########
my $SenderIn = "Configs\@coastlinemicro.com(Coastline Micro, Inc. - Shark Tank E-Com Store)";
use lib "/www/htdocs/MIME-Lite-2.117/lib/";
use MIME::Lite;
my $msg = MIME::Lite->new(
				From    =>$SenderIn,
                To      =>$Email,
                Subject =>'Copy Of: Your Shark Tank EQuote Request',
                Type    =>'multipart/related'
                );
   $msg->attach(Type => 'text/html',
   Data => qq{ 

<html>
<head>
<title>Coastline Micro Inc.</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="http://www.coastlinemicro.com/common_css.html?anchor=333366&anchorov=EB0000&weight=normal&weightov=normal&decor=underline&decorov=underline" Type="text/css">
<STYLE TYPE="text/css">
body { background-color:#ffffff; scrollbar-face-color:#F2F2F7; scrollbar-highlight-color:#F2F2F7; scrollbar-shadow-color:#8f8fab; scrollbar-3dlight-color: #333366; scrollbar-arrow-color:#333366; scrollbar-track-color:#F2F2F7; scrollbar-darkshadow-color:#8f8fab; }
</STYLE>

<style type="text/css">
$LayerCSS
$LayerCSS2
.link { line-height:12px; font-family:verdana,arial,helvetica; font-size:10px; text-decoration:none; }
.nolink { line-height:12px; font-family:verdana,arial,helvetica; font-size:10px; text-decoration:none; font-weight:bold; }
.red { color:#EB0000; }
a { text-decoration:underline; }
a:hover { text-decoration:none; }
</style>

<base href="http://www.coastlinemicro.com/">
</head>
<body bgcolor="#ffffff" text="#8F8FAB" leftmargin="0" topmargin="0" marginwidth="0" scroll="yes" marginheight="0">
<br>
<table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
<tr height="40">
<td rowspan="2" width="15%" align="left" valign="top"><a href="http://www.coastlinemicro.com/"><img src="http://www.coastlinemicro.com/Mailbox/images/top_cm_logo.jpg" width="116" height="37" border="0"></a></td>
<td rowspan="2" align="center" valign="bottom" width="30%">&nbsp;</td>
<td width="55%" align="right" valign="bottom"><img src="http://www.coastlinemicro.com/Mailbox/images/god_bless_america.gif" width="118" height="35"></td>
</tr>
<tr><td colspan="3" width="100%" bgcolor="#FFFFFF" height="5"><img src="http://www.coastlinemicro.com/Mailbox/images/spacer.gif" width="2" height="5"></td></tr>
<tr><td colspan="3" width="100%" bgcolor="#8F8FAB" height="2"><img src="http://www.coastlinemicro.com/Mailbox/images/spacer.gif" width="2" height="2"></td></tr>
<tr><td colspan="3" width="100%" bgcolor="#FFFFFF" height="2"><img src="http://www.coastlinemicro.com/Mailbox/images/spacer.gif" width="2" height="2"></td></tr>
</table>
<table width="95%" align="center" cellspacing="0" cellpadding="0" border="1" bordercolor="#8F8FAB" class="comtableborder"><tr><td width="100%" valign="top">

<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr> 
    <td align="center" valign="middle" width="100%" height="25"> 
      <table width="100%" border="0" cellspacing="0" cellpadding="0" background="images/tables/topbar.jpg" height="24">
        <tr> 
          <td width="5"><img src="images/tables/topbar_left.jpg" width="5" height="24"></td>
          <td width="64%"><nobr><font class="btext">&nbsp;&nbsp;<b>$MainTitle</b></font></nobr></td>
          <td width="18%" align="center" valign="top">&nbsp;</td>
          <td width="18%" align="center" valign="top">&nbsp;</td>
          <td width="100%" align="left" valign="top"><img src="images/tables/topbar_right.jpg" width="5" height="24"></td>
        </tr>
      </table>
    </td>
  </tr>
  <tr> 
    <td align="left">
	 <table width="85%" border="0" cellspacing="1" cellpadding="0" align="center">
        <tr> 
          <td align="left" valign="top" width="100%">
		  <font class="btext3"><br><b>$FirstName $LastName</b>,<br>Your Electronic Quote (E-Quote) request has been delivered for your customized <b>$CMSeries Series&#153;</b> $PricingClass system. Below you will find the parameters of that configuration. A Coastline Micro Representative will contact you regarding this request in a timely manner. Please feel free to call us if you do NOT want to wait for our Representative to call you.<br><br>You can use <b>$EQCNT</b>, this request's <b>EQuote ID</b>, when contacting Coastline Micro regarding this specific configuration. You can find our contact information at the foot of this email message.<br><br><center><b>As always, thank you for using the Shark Tank&#153;, our prize winning e-commerce store.</b></center><br><br></font></td>
		</tr>
	 </table>
</td>
  </tr>
  <tr> 
    <td valign="top"> 
      <table width="100%" border="0" cellspacing="1" cellpadding="0" align="center">
        <tr> 
          <td align="center" valign="top" height="150" width="35%">
		  <font class="stankprice">$lePrecious<img src="/dbimages/prod_common/$SmallImageN" width="165" height="100" vspace="20" border="0" alt="$SmallImageD"></font>
            <table width="100%" cellspacing="1" cellpadding="0" bgcolor="#FFFFFF">
              <tr> 
                <td> 
                  <table width="100%" cellspacing="0" cellpadding="0" bgcolor="#F2F2F7" class="stankth" height="18" $border>
                    <tr> 
                      <td align="center"><font class="btext"><b>Trusted Performance By</b></font></td>
                    </tr>
                  </table>
                </td>
              </tr>
              <tr> 
                <td> 
                  <table width="100%" cellspacing="0" cellpadding="0" class="stankth" $border>
                    <tr> 
                      <td width="5%">&nbsp;</td><td align="center" width="90%"><font class="btext">
				
@leImagen
					  						<br></font></td><td width="5%">&nbsp;</td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </td>
          <td valign="top" width="65%"> 
            <table width="100%" cellspacing="1" cellpadding="0" bgcolor="#FFFFFF">
              <tr> 
                <td> 
                  <table width="100%" cellspacing="0" cellpadding="0" bgcolor="#F2F2F7" class="stankth" height="18" $border>
                    <tr> 
                      <td align="center"><font class="btext"><b>System Specifications</b></font></td>
                    </tr>
                  </table>
                </td>
              </tr>
              <tr> 
                <td> 
                  <table width="100%" cellspacing="0" cellpadding="2" class="stankth" $border>
                    <tr> 
                      <td> 

@leProductos

<table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#F2F2F7"><tr><tr><td width="100%" height="10"><font size="-4" face="verdana,arial,helvetica">&nbsp;</font></td></tr></table>
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
</table>

    </td>
  </tr>
</table>



<table width="95%" border="0" cellspacing="0" cellpadding="0"><tr><td align="center" width="100%"> 
$STANKLEGAL
</td></tr></table>

</body>
</html>
								}
                     );
        $msg->send();

		
		

		
print "Content-type: text/html\n\n";
&topper;
{
print <<EOF

<table width="100%" align="center" cellpadding="0" cellspacing="0" border="0">
<tr> 
<td width="40%" valign="middle" align="center"><img src="/dbimages/prod_common/$Image" width="165" height="100" vspace="20" border="0"></td>
<td width="55%" valign="middle"><font class="btext"><br>An Electronic Quote (E-Quote) request has been delivered for your customized <b>$CMSeries Series&#153;</b> $PricingClass system. You will recieve an email specifying the parameters of your configuration. A Coastline Micro Representative will contact you regarding this request in a timely manner. Please feel free to call us if you do NOT want to wait for our Representative to call you.<br><br>You can use <b>$EQCNT</b>, this request's <b>EQuote ID</b>, when contacting Coastline Micro regarding this specific configuration. You can find our contact information at the foot of this screen.<br><br><b>As always, thank you for using the Shark Tank&#153;, our prize winning e-commerce store.</b><br><br></font>
</td>
<td width="5%">&nbsp;</td>
</tr>
</table>
<br>

EOF
}

&bottom;


## DISCONNECT DB 
$dbh->disconnect; 

exit;
}



## ----------------->>> SAVE
if ($FORM{'CartSaveEQuote'} eq "SAVE" && $FORM{'LasPartes'} && $FORM{'ElPrecio'} && $Cookies{'Echado'} eq "YES") {

use DBI;
my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
$dbh->{RaiseError} = 1; 


	## SAVE CONFIG
	my $sth = $dbh->prepare("INSERT INTO Configs (ConfigID, Parent, Username, CMCustNum, OrderIDs, 
							CMSeries, ProductIDs, TotalPrice, TotalWeight, AddedOn, ModifiedBy, ModifiedOn)

							VALUES (Null, '$CMPartNum', '$Cookies{'GID'}', '$Cookies{'CeeEmmNo'}', Null, '$CMSeries', 
							'$LasPartes', '$ElPrecio', '$ElPeso', Null, Null, '')");
	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish;

	## GET LAST INSERT ID
	my $sth = $dbh->prepare("SELECT LAST_INSERT_ID() FROM Configs");
	$sth->execute or die "Unable to execute query\n"; 
	my $row = $sth->fetchrow_arrayref;
	$LastOne = $row->[0];
	$sth->finish;
	
my $Username = "$Cookies{'GID'}";
my $FirstName = "$Cookies{'FiNo'}";
my $Email = "$Cookies{'EDomi'}";
my $LastOne = $LastOne;

## ----------------------->>> SEND EMAIL MESSAGE
my $SenderIn = "Configs\@coastlinemicro.com(Coastline Micro, Inc. - Shark Tank E-Com Store)";
use lib "/www/htdocs/MIME-Lite-2.117/lib/";
use MIME::Lite;
my $msg = MIME::Lite->new(
				From    =>$SenderIn,
                To      =>$Email,
                Subject =>'Configuration Saved!',
                Type    =>'multipart/related'
                );
   $msg->attach(Type => 'text/html',
   Data => qq{ 
<html>
<head>
<title>Coastline Micro, Inc. - Shark Tank E-Com Store - Configuration Saved</title>
<LINK REL="STYLESHEET" HREF="http://www.coastlinemicro.com/commoncss.html" Type="text/css">
</head>
<body bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<br>
<table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
<tr height="40">
<td rowspan="2" width="15%" align="left" valign="top"><a href="http://www.coastlinemicro.com/"><img src="http://www.coastlinemicro.com/Mailbox/images/top_cm_logo.jpg" width="116" height="37" border="0"></a></td>
<td rowspan="2" align="center" valign="bottom" width="30%">&nbsp;</td>
<td width="55%" align="right" valign="bottom"><img src="http://www.coastlinemicro.com/Mailbox/images/god_bless_america.gif" width="118" height="35"></td>
</tr>
<tr><td colspan="3" width="100%" bgcolor="#FFFFFF" height="5"><img src="http://www.coastlinemicro.com/Mailbox/images/spacer.gif" width="2" height="5"></td></tr>
<tr><td colspan="3" width="100%" bgcolor="#8F8FAB" height="2"><img src="http://www.coastlinemicro.com/Mailbox/images/spacer.gif" width="2" height="2"></td></tr>
<tr><td colspan="3" width="100%" bgcolor="#FFFFFF" height="2"><img src="http://www.coastlinemicro.com/Mailbox/images/spacer.gif" width="2" height="2"></td></tr>
</table>
<table width="95%" align="center" cellspacing="0" cellpadding="0" border="1" bordercolor="#8F8FAB" class="comtableborder"><tr><td width="100%" valign="top">

<table width="100%" border="0" cellspacing="0" cellpadding="0" background="http://www.coastlinemicro.com/images/newones/top_tablebg_main.jpg" height="100">
  <tr> 
    <td width="30%"><img src="http://www.coastlinemicro.com/images/newones/illus_products.jpg" width="250" height="100" border="0"></td>
    <td align="right" valign="middle" width="70%"><font size="1" color="#ffffff" face="verdana,arial,helvetica">$date&nbsp;&nbsp;<font size="3">&nbsp;</font></font>
	<center><img src="http://www.coastlinemicro.com/images/newones/title_$ITitle.jpg" width="350" height="80" align="bottom"></center></td>
  </tr>
</table>

<table width="400" border="0" cellspacing="0" cellpadding="0" align="center"><tr><td width="100%" valign="top">
<font face="verdana,arial,helvetica" size="1" color="#333366">$FirstName,<br><br>You have successfully saved your new $CMSeries&#153; Series configuration. This configuration will be saved for a total of 30 days.<br><br>All <b>$Cookies{'CoNo'}</b> users can review/purchase this system securely online by logging onto the Shark Tank&#153; with their own username/password.<br><ul><li><b>Your $CMSeries&#153; Series Configuration</b><br><a href="http://www.coastlinemicro.com/stank_vconfig.html?CID=$LastOne">$ItemName</a></li><li><b>Shark Tank&#153; E-Com Store</b><br><a href="http://www.coastlinemicro.com/">http://www.coastlinemicro.com/</a></li><li><b>Did not reque