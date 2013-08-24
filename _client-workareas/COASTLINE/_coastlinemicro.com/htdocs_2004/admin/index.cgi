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

if ($FORM{'enformthee'}) {

{
print <<EOF

<html>
<head>
<title>Untitled Document</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
$MenuConfig
<LINK REL="STYLESHEET" HREF="admincss.cgi" Type="text/css">
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
      <table width="95%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td colspan="2"> 
            <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER">
              <tr bordercolor="#333366"> 
                <td width="50%" align="center" valign="top"> 
                  <table width="100%" border="0" cellspacing="0" cellpadding="10">
                    <tr> 
                      <td width="100%" height="225" valign="top"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Coastline 
                        Micro's Shark Tank&#153;</b><br>
                        First of all, let us take the time to thank you for visiting 
                        our new E-Com store, our newest idea in making our customer's 
                        system buying experience as easy and personable as it 
                        can possibly be. Here we can dynamically display all our 
                        inventory, including all our high performance re-configurable 
                        systems, to allow our customers to seemlessly configure 
                        and order products securely online. Our trademark name, 
                        Shark Tank&#153;, the name for our E-Com store, and our 
                        trademarked product lines; Thresher Series&#153; Value 
                        Desktop PCs, Mako Series&#153; Performance Desktop PCs, 
                        Reef Series&#153; Notebooks, Tiger Series&#153; PIII Servers 
                        and the all mighty Great White&#153; Xeon&#153; Servers 
                        are all part of our contiuing efforts to make our product 
                        line exciting and easily recognizable within the systems 
                        marketplace.<br>
                        <br>
                        <b>The Admin System<br>
                        </b>Here in the administration system you can do as many 
                        actions as the DHTML menu gives you access to do within 
                        the system. If you would like your access rights changed, 
                        updated or re-implemented please contact a Coastline Micro 
                        Supervisor or Manager for further assistance. If you should 
                        recieve an error please be sure to report it immediatly 
                        along with whatever actions led to the error to: stdev\@coastlinemicro.com</font></td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
      <br>
      <br>
    </td>
  </tr>
</table>
<table width="100%" background="images/bot_frame_bg.jpg" height="56" align="center" cellpadding="0" cellspacing="0" border="0"><tr><td width="55%" align="left" height="56">&nbsp;</td></tr></table>
</body>
</html>



EOF
}
exit;
}

else {
{
print <<EOF

<html>
<head>
<title>Coastline Micro, Inc. - Press Release Article Administration System - $date</title>
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