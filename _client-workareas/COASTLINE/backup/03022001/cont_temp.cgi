#!/usr/local/bin/perl

require ("referer.hs"); 

require ("parse_query.hs");

require ("date.hs");

if ($FORM{'sub_link'}) { 

$sub_link = "$FORM{'sub_link'}";

$filename = "content/contact/$sub_link.txt";

$dropme = `cat $filename`;

$legal = `cat legal.hs`;

$menuback = `cat content/menuback.txt`;

print "Content-type: text/html\n\n";

{
print <<EOF

<html>
<head>
<script language="Javascript" src="js/reload.js"></script>
<title>Coastline Micro Inc.</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta name="keywords" content="coastlinemicro.com, www.coastlinemicro.com, coastline, micro, irvine, ca, california, about, company, location, businsess, competition, competitors, solutions, irvine, california, technology, ceo, own, partner, fast, reliable, heritage, sophisticated, computer, system, build, custom, sample, guarantee, search, product">
<meta name="description" content="Coastline Micro Inc. is in business to develop hardware solutions that make sense for the small to corporate sized business arena. We have been in business for over a decade and have the knowledge and expertise necessary to be competitive in the market. Our every product carries a 100% Product Satisfaction Guarantee. We are located in Irvine, California at 60 N. Technology Drive. For more information about our company and its what it is in business to do please follow the link above. Our company's Heritage dates back to 1989.">
<script language="JavaScript" src="js/dynlayer.js"></script>
<script language="JavaScript" src="js/list.js"></script>
<script language="JavaScript" src="js/menulist.js"></script>
<script language="JavaScript" src="js/menu_construct.js"></script>

<LINK REL="STYLESHEET" HREF="common_css.cgi" Type="text/css">
</head>
<body bgcolor="#ffffff" text="#8f8fab" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onLoad="toggle()" onResize="reload()">

<script language="JavaScript">
document.write(numbers.div)
</script>


<table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
  <tr valign="top"> 
    <td width="50%" height="145" valign=top><img src="images/illus_contact.jpg"></td>
    <td height="145"> 
      <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
        <tr>
          <td>
            <table border="0" width="350" cellspacing="0" cellpadding="0" align="center" height="18">
              <tr height=18> 
                <td width="25" height="18"><img src="images/timer_piece_left.gif" width="25" height="18"></td>
                <td bgcolor="#8f8fab" width="300" align="center" height="18"><font class="timer">$date</font></td>
                <td width="25" align="center" height="18"><img src="images/timer_piece_right.gif" width="25" height="18"></td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
      <table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr valign="top" align="left"> 
          <td height="127"><img src="images/title_contact.jpg"></td>
        </tr>
      </table>
    </td>
  </tr>
</table>
<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td width="10%" align=left valign=top>$menuback</td>
    <td width="5"><img src="images/140spacer.gif" width="5" height="8"></td>
    <td width="90%" align="center" valign=top>

      $dropme 
<br>
      $legal

</td>
  </tr>
</table>

</body>
</html>

EOF
}
}

else {
$sorry = `cat sorry_nospec.hs`;

print "Content-type: text/html\n\n";
{
print <<EOF

$sorry

EOF
}
}