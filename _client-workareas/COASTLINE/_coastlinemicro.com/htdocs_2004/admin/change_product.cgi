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

## If no resident form processing calls are given continue
if ($FORM{'enformthee'}) {

{
print <<EOF

<html>
<head>
<title>Coastline Micro, Inc. - Shark Tank Admin System - Inventory Administration</title>
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
            Inventory</b></font></td>
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
<form method="post" name="change" onSubmit="return cambiame();">

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
                                      <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">View/Update 
                                        Inventory</font></b></font></td>
                                      <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    </tr>
                                    <tr> 
                                      <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                    </tr>
                                    <tr> 
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                      <td height="75" bgcolor="#F2F2F7" align="left"><font face="verdana,arial,helvetica" size="1" color="#333366">To view or update a product in the system please select the type of product you are going to view/update. Then, type in the the <b>Coastline Micro Part Number</b> for the product you would like to view/update then click 'View/Update'<br><br><font color="#EB0000">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>1. Product Type</b>&nbsp;&nbsp;&nbsp;&nbsp;->->->&nbsp;&nbsp;&nbsp;&nbsp;<b>2. CM Part Number</b>&nbsp;&nbsp;&nbsp;->->->&nbsp;&nbsp;&nbsp;<b>3. Click Button</b></font></font></td>
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    </tr>
                                    <tr> 
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                      <td height="35" align="center"> 
<script language="Javascript">
function cambiame() {
var missingdrop = "";
var formindex = document.change.LeProducto.selectedIndex;
var thisone = document.change.LeProducto.options[formindex].value;
var CMPartNum = document.change.CMPartNum.value;

if (thisone == "BIGNULL") {
	thefirst = "LeProducto";
    missingdrop += "\\nThat is not a valid option, please select another...";
}

else if ((CMPartNum == " ") || (CMPartNum == "")) {
	thefirst = "CMPartNum";
    missingdrop += "\\nYou must type in a Coastline Micro Part Number to continue...";
}

// If anything comes back wrong alert and detain form, else submit info
if (missingdrop != "") {
    alert(missingdrop);
 	document.change(thefirst).focus();
    return false;
} 
else {
	if ((formindex == 1) || (formindex == 2) || (formindex == 3)) {
		location.href='change_product_system.cgi?CMPartNum='+CMPartNum+'&PricingClass='+thisone+'';
		return false;
	}
	else {
		location.href='change_product_common.cgi?CMPartNum='+CMPartNum+'&PricingClass='+thisone+'';
		return false;	
	}
}
}

// FORM FEEDER FUNCTIONS
// By Drlouie \@ NetMedia Solutions
// info\@NetMediaSol.com for help
// Copyright 2001 NetMedia Solutions

function grabThis() {
var formindex = document.change.LeProducto.selectedIndex;
var thisone = document.change.LeProducto.options[formindex].value;
if (thisone == "BIGNULL") { alert('That is an invalid option, please make another selection.'); }
else {
	var b = navigator.appName;
	if (b=="Netscape") { parent.frames.xtraOne.location.href='listProd.cgi?PricingClass='+thisone+''; }
	else { parent.frames.xtraOne.location.href='listProd.cgi?PricingClass='+thisone+''; }
}
}
</SCRIPT>
<select name="LeProducto" onChange="grabThis();" class="inputtext">
<option value="BIGNULL" SELECTED>:::::  Configurables  :::::</option>
<option value="Desktop">Desktop PC</option>
<option value="Server">Server</option>
<option value="Notebook">Notebook</option>
<option value="BIGNULL"> </option>
<option value="BIGNULL">:::::    Components   :::::</option>
<option value="Monitor">Monitor</option>
<option value="Memory">Memory</option>
<option value="HardDrive">Hard Drive</option>
<option value="VideoCard">Video Card</option>
<option value="Peripheral">Peripheral</option>
<option value="Printer">Printer</option>
<option value="Software">Software</option>
</select>&nbsp;&nbsp;
<select name="CMPartNum" class="inputtext">
</select>
&nbsp;&nbsp;<input type="submit" value="View/Update" class="inputbut" name="submit">
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
                                      
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Add Product to Inventory</font></b></font></td>
                                      <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    </tr>
                                    <tr> 
                                      <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                    </tr>
                                    <tr> 
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                      
                                    <td height="35" bgcolor="#F2F2F7" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366">Click 
                                      the button below to create a new product 
                                      profile. </font></td>
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    </tr>
                                    <tr> 
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                      <td height="35" align="center"> 
                                        
<form method="post" name="add" onSubmit="return addProduct();">
<br>
<center>
<script language="Javascript">
function addProduct() {
var missingdrop = "";
var formindex = document.add.ProductType.selectedIndex;
var thisone = document.add.ProductType.options[formindex].value;

if (thisone == "BIGNULL") {
	thefirst = "ProductType";
    missingdrop += "\\nThat is not a valid option, please select another...";
}

// If anything comes back wrong alert and detain form, else submit info
if (missingdrop != "") {
    alert(missingdrop);
 	document.add(thefirst).focus();
    return false;
} 
else {
	if ((formindex == 1) || (formindex == 2) || (formindex == 3)) {
		parent.location.href='add_product_system.cgi?ProductType='+thisone+'';
		return false;
	}
	else {
		parent.location.href='add_product_common.cgi?ProductType='+thisone+'';
		return false;	
	}
}
}
</SCRIPT>
<select name="ProductType" class="inputtext">
<option value="BIGNULL" SELECTED>:::::  Configurables  :::::</option>
<option value="Desktop">Desktop PC</option>
<option value="Server">Server</option>
<option value="Notebook">Notebook</option>
<option value="BIGNULL"> </option>
<option value="BIGNULL">:::::    Components   :::::</option>
<option value="Monitor">Monitor</option>
<option value="Memory">Memory</option>
<option value="HardDrive">Hard Drive</option>
<option value="VideoCard">Video Card</option>
<option value="Peripheral">Peripheral</option>
<option value="Printer">Printer</option>
<option value="Software">Software</option>
</select>
<font size="1" face="verdana,arial,helvetica"><br><br></font>
<input type="submit" value="Add This Type" class="inputbut">
</center>
</form>
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
          <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Search/Browse 
            Inventory</font></b></font></td>
          <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
        </tr>
        <tr> 
          <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
        </tr>
        <tr> 
          <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
          <td height="85" bgcolor="#F2F2F7" align="left"><font face="verdana,arial,helvetica" size="1" color="#333366">To 
            search products in the system, type in the Terms/Keywords to help 
            you locate the product's profile you are interested in reviewing and/or 
            updating. Then, click 'Search Inventory'. You can search using keywords, product name, price, part number (CLM and MFG) and/or description.</font></td>
          <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
        </tr>
        <tr> 
          <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
          <td height="100%" align="center" valign="top"> <br>
            <form method="post" action="s_products.cgi">
              <table border="1" cellspacing="0" cellpadding="0" width="200" bordercolor="#8F8FAB">
                <tr> 
                  <td height="20" align="center" bgcolor="#F2F2F7" class="tableBG" width="200"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Search 
                    Terms/Keywords</b></font></td>
                </tr>
                <tr> 
                  <td align="center" height="40" width="200"> 
                    <input type="text" name="keywords" size="15" class="inputtext">
                  </td>
                </tr>
                <tr> 
                  <td align="center" height="35" valign="middle" width="200"> 
                    <input type="submit" value="Search Inventory" class="inputbut" name="Submit">
                  </td>
                </tr>
              </table>
              <br>
            </form>
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
</center><br>
                      </td>
                    </tr>
                  </table>
                  </td>
              </tr>
            </table>
<br>
          </td>
        </tr>
      </table>    </td>
  </tr>
</table>
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
<title>Coastline Micro, Inc. - Shark Tank Admin System - Inventory Administration</title>
</head>
<frameset rows="64,*,5" rows="*" border="0" framespacing="0"> 
<frame name="topOne" scrolling="NO" noresize src="topper.cgi" marginwidth="0" marginheight="0" frameborder="NO">
<frame name="botOne" src="$script?enformthee=1" frameborder="NO" marginheight="0" marginwidth="0" scrolling="AUTO">
<frame name="xtraOne" src="$script?blank=1" frameborder="NO" marginheight="0" marginwidth="0" scrolling="AUTO">
</frameset>
<noframes><body bgcolor="#FFFFFF">
</body></noframes>
</html>

EOF
}
exit;
}
