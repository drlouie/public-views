#!/usr/bin/perl5 -w

$lastdate = `cat date.dat`;

print "Content-type: text/html\n\n";
{
print <<EOF

<html>
<head>
<title>Coastline Micro, Inc. - QISV Catalogue</title>
<SCRIPT LANGUAGE="JavaScript">
//Check Search field for completion
function checkSearch() {
	if (document.search.Searchterms.value == "" || document.search.Searchterms.value == "Type Keyword(s) or SKU") {
	document.search.Searchterms.value = 'Please Type Keyword(s) or SKU';
	return false
	}	
}

//On Focus Clear Search Field
function clearSearch() {
	if (document.search.Searchterms.value == "Please Type Keyword(s) or SKU") {
	document.search.Searchterms.value = '';
	}	
}

</SCRIPT>
</head>
<body background="../images/qisvbkgd.gif">
<CENTER><h2><font face=verdana, arial, helvetica>Coastline Micro, Inc.<br><br>VID # 1-33-056-4458-800
<br><br>QISV Ordering Address:</H2></font>
<font face=verdana, arial, helvetica SIZE=3>60 Technology Drive<BR>Irvine, CA 92618</font>
</center>
<P>
<HR>
<CENTER><strong><font face=verdana, arial, helvetica size=2>This is a true and accurate copy of the catalogue approved with the General Services Commission.</font></strong></CENTER>
<CENTER><font face=verdana, arial, helvetica SIZE=2>Effective Date of catalogue:<BR><b>June 15, 2001</b></font></CENTER>
<CENTER><font face=verdana, arial, helvetica SIZE=2>This catalogue last updated $lastdate.</font></CENTER>
<BR>
<HR><p>
<center>
<table cellpadding=15>
<tr>
<td><center><font face=verdana, arial, helvetica size =+1><a href="http://www.gsc.state.tx.us/ecat/index.html">Return to GSC QISV Listing</a></font></center></td>
</tr>
</table></center><p>
<HR>
<H3><U><font face=verdana, arial, helvetica>Vendor Contact Information</font></U></H3>
<TABLE>
<TR>
<TD><font face=verdana, arial, helvetica size=2><b>QISV Contact Information</b></font></TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD><font face=verdana, arial, helvetica size=2><b>CMBL Address:</b></font></TD>
<TD>&nbsp;</TD>
</TR>
<TR>
<TD><font face=verdana, arial, helvetica size=2>Contact Person:</font></TD>
<TD><font face=verdana, arial, helvetica size=2><b>Peter Deralas</b></font></TD>
<TD>&nbsp;</TD>
<TD><font face=verdana, arial, helvetica size=2>60 Technology Drive</font></TD>
<TD>&nbsp;</TD>
</TR>
<TR>
<TD><font face=verdana, arial, helvetica size=2>Phone #:</font></TD>
<TD><font face=verdana, arial, helvetica size=2><b>800-729-6809 x259</b></font></TD>
<TD>&nbsp;</TD>
<TD><font face=verdana, arial, helvetica size=2>Irvine, CA 92618</font></TD>
<TD>&nbsp;</TD>
</TR>
<TR>
<TD><font face=verdana, arial, helvetica size=2>Fax #:</font></TD>
<TD><font face=verdana, arial, helvetica size=2><b>949-450-9977</b></font></TD>
<TD>&nbsp;</TD>
<TD><font face=verdana, arial, helvetica size=2>Phone #: 800-729-6809</font></TD>
<TD>&nbsp;</TD>
</TR>
<TR>
<TD><font face=verdana, arial, helvetica size=2>E-Mail Address:</font></TD>
<TD><font face=verdana, arial, helvetica  COLOR=#0000FF size=2><U>pderalas\@coastline-mail.com</U></font></TD>
<TD>&nbsp;</TD>
<TD><font face=verdana, arial, helvetica size=2>Fax #: 949-450-9977</font></TD>
<TD>&nbsp;</TD>
</TR>
</TABLE>
<BR>
<h3><font face=verdana, arial, helvetica><u>Product / Services Information</u></font></h4>
<br>
<hr>
<table border=1 cellpadding=2>
<tr><td align=middle><font face=verdana, arial, helvetica  size=2><b>Class/Items Available</b></font></td><td><font face=verdana, arial, helvetica  size=2><b>Discription</b></font></td></tr></font>
<tr><td><font face=verdana, arial, helvetica  size=2><b>204</b></font></td><td><font face=verdana, arial, helvetica  size=2>Computer Hardware and Peripherals for Microcomputers</font></td></tr>
<tr><td><font face=verdana, arial, helvetica  size=2><b>208</b></font></td><td><font face=verdana, arial, helvetica  size=2>Computer Software for Microcomputers (Preprogramed)</font></td></tr>
</table>
<br>
<strong><font face=verdana, arial, helvetica  size=3>Manufacturer Listing</font></strong>
<TABLE BORDER=1 CELLPADDING=2>
<TR><TD><CENTER><i><font face=verdana, arial, helvetica  SIZE=2><b>Product / Service</b></font></i></CENTER></TD>
<TD><CENTER><font face=verdana, arial, helvetica  SIZE=2><b><i>Manufacturer (w/ link to home page)</i></b></font></CENTER></TD>
<TD ALIGN=MIDDLE><b><i><font face=verdana, arial, helvetica  SIZE=2><CENTER>Technical Support Phone #</CENTER></font></i></b></TD>
</TR>
<TR>
<TD><font face=verdana, arial, helvetica  size=2><b>Computer Maintenance and diagnostics</b></TD>
<TD><font face=verdana, arial, helvetica size=2 color=#0000FF><A href="http://www.coastlinemicro.com/">Coastline Micro, Inc.</a></font></TD>
<TD ALIGN=MIDDLE><font face=verdana, arial, helvetica size=2>800-729-6809</font></TD>
</TR>
<TR>
<TD><font face=verdana, arial, helvetica size=2><b>Computer Systems</b></font></TD>
<TD><font face=verdana, arial, helvetica size=2 COLOR=#0000FF><A href="http://www.coastlinemicro.com/">Coastline Micro, Inc.</a></font></TD>
<TD ALIGN=MIDDLE><font face=verdana, arial, helvetica size=2>800-729-6809</font></TD>
</TR>
</TABLE>



<BR>



<HR>


	<BR>	
<CENTER><H2><U>Catalogue Information</U></H2>	</CENTER>	 
		

<font face=verdana, arial, helvetica size=2><b>NOTE  to State Agencies:</b><BR>  
If this Qualified Information Systems Vendor provides consulting services and if the value of the consulting contract is reasonably foreseen to exceed $15,000.00, please refer to the <a href="http://www.capitol.state.tx.us/statutes/tocs/gv225400toc.html">
Texas Government Code, Subtitle F, Chapter 2254</a>.
<HR>
<b>NOTES to all Eligible Purchasers:</b>
<LI>Only Automated Information System (AIS) products and services may be purchased from this catalogue.  Products not eligible     for     the catalogue purchase procedure must be edited out by the vendor.
<LI>Any <a href="http://www.gsc.state.tx.us/stpurch/telecom.html">telecommunication services</a> that may be included within this catalogue shall only be procured by the General Services Commission.
<LI>Disregard any statement in this catalogue that states that prices and availability may change without notice.  This catalogue is required to be kept current by the vendor.
<LI>Disregard any "proprietary, confidential, copyright (C), all rights reserved" statements in this catalogue.  Eligible purchasers are allowed to make copies of this catalogue.
<LI>For services and  products offered in this catalogue that have only one price, the price shown may be considered both the list price and state price.
<LI>Any terms and conditions in this catalogue that conflict with the Constitution or laws of the state of Texas shall not be enforceable and, therefore, will not be binding.
<LI>All AIS products and services offered in this catalogue conform and comply with all applicable standards adopted by the DIR; and all products conform to all state and federal requirements such as ANSI, FCC, NEMA, OSHA and UL standards.



<HR>
<b>Vendor Affirmation</b><BR>
By signing the GSC QISV Catalogue Purchasing Program application and submitting this catalogue through the program, the vendor has reviewed TAC 113.19, and agrees to comply with the rules as stated for the QISV program.  The vendor will also:

<LI>not give, offer to give, or intend to give at any time hereafter any economic opportunity, future employment, gift, loan, gratuity, special discount, trip, favor, or service to a public servant in connection with catalogue purchase transactions;
<LI>not currently be delinquent in the payment of any franchise tax owed the State of Texas under Tax Code, Chapter 171(go to <a href="http://www.cpa.state.tx.us/taxinfo/coasintr.html">"Certification of Franchise Tax Account Status "</a> for verification)
; 
<LI><a href="http://www.gsc.state.tx.us/stpurch/q9802.html">Update</a> their catalogue as needed to reflect changes in price and the availability of products or services offered.

<HR>

<br>

<a name="search"></a>
<center>
<h3>Search the Coastline Micro listings by keyword or stock #</h3>
<FORM METHOD="GET" ACTION="s_qisv.cgi" onSubmit="return checkSearch();" name="search">
What are you looking for?
</font>
<TABLE>
<TR>
<TD align="center"><input type="text" name="Searchterms" size="50" OnFocus="clearSearch()" OnClick="clearSearch()"><br><input type="submit" value="Submit Search"></TD>
</TR>
</TABLE>
</form>
</center>
<BR><br><HR>
<font face=verdana, arial, helvetica><H2><center>Catalogue Products / Services</center></H2></font>
<table border=1 cellpadding=2>
<tr><td><b><center><font face=verdana, arial, helvetica size=2>Maintenance, Repair, Support Plan</center>
          </b> It is Coastline Micro's goal to resolve every customer service 
          issue the same day the request for service is submitted. We offer a 
          one-year warranty on all equipment purchased from Coastline Micro. Next 
          day parts replacement, and on-site service are optional for the 1st, 
          2nd and 3rd year of ownership cutting down on your company's IT department 
          costs for computer repair and upgrades. 
          <p>Please call one of our Customer Service Representatives to help with 
            any of your product return issues. Or you can write to our Customer 
            Service Department using our online request forms for an equally fast 
            response. No matter what your workstation, server and/or network needs 
            be, you can rest assure Coastline Micro can meet if not exceed your 
            expectations and deadlines every single time.</p>
          </td></font>
      </tr>
</table>
<br><br>
EOF
}

##### TABLE 204s
	$mystuff1 = "204";
	opendir(DIR, $mystuff1) or die "can't opendir $mystuff1 $!";
	while (defined($file = readdir(DIR))) {
	next if $file =~ /^\.\.?$/; ## skip . and .. directories
		$mytitle = `cat 204/$file/title.dat`;
		print "<font face=verdana, arial, helvetica size=2><b>$file $mytitle</b></font>";
		print "<TABLE border=\"1\" cellpadding=\"2\" width=\"100%\" cellspacing=\"0\">";
		print "<tr><TD align=\"center\" width=\"125\"><font face=verdana, arial, helvetica  SIZE=2><i>Manufacturer</i></font></TD><TD ALIGN=center width=\"300\"><font face=verdana, arial, helvetica  SIZE=2><i>Stock / SKU #</i></font></TD><TD width=\"250\"><font face=verdana, arial, helvetica  SIZE=2><i>Product / Service Description</i></font></TD><TD ALIGN=center width=\"50\"><font face=verdana, arial, helvetica  SIZE=2><i>Spec./ Info?</i></font></TD><TD ALIGN=center width=\"100\"><font face=verdana, arial, helvetica  SIZE=2><i>Stk. Count<BR>($lastdate)</i></font></TD><TD align=\"center\" width=\"50\"><font face=verdana, arial, helvetica  SIZE=2><i>List Price</i></font></TD><TD width=\"50\" align=\"center\"><font face=verdana, arial, helvetica  SIZE=2><i>St. Disc. Price</i></font></TD></tr>";		

		$mycontent = `cat 204/$file/content.dat`;		
		@mylines = split(/:end\n/, $mycontent);
    	foreach $myline (@mylines) {
			@mypairs = split(/,,,,,/, $myline);
			print "<tr>";
			print "<td><font face=verdana, arial, helvetica size=\"1\">$mypairs[0]</font></td>";
			print "<td><font face=verdana, arial, helvetica size=\"1\">$mypairs[1]</font></td>";
			print "<td><font face=verdana, arial, helvetica size=\"1\">$mypairs[2]</font></td>";
			print "<td><font face=verdana, arial, helvetica size=\"1\">$mypairs[3]</font></td>";
			print "<td><font face=verdana, arial, helvetica size=\"1\">$mypairs[4]</font></td>";
			print "<td><font face=verdana, arial, helvetica size=\"1\">$mypairs[5]</font></td>";
			print "<td><font face=verdana, arial, helvetica size=\"1\">$mypairs[6]</font></td>";
			print "</tr>";
		}
		print "</TABLE><br><br>";
	}

##### TABLE 208s
	$mystuff2 = "208";
	opendir(DIR, $mystuff2) or die "can't opendir $mystuff2 $!";
	while (defined($file = readdir(DIR))) {
	next if $file =~ /^\.\.?$/; ## skip . and .. directories
		$mytitle = `cat 208/$file/title.dat`;
		print "<font face=verdana, arial, helvetica size=2><b>$file $mytitle</b></font>";
		print "<TABLE border=\"1\" cellpadding=\"2\" width=\"100%\" cellspacing=\"0\">";
		print "<TD align=\"center\" width=\"125\"><font face=verdana, arial, helvetica  SIZE=2><i>Manufacturer</i></font></TD><TD ALIGN=center width=\"300\"><font face=verdana, arial, helvetica  SIZE=2><i>Stock / SKU #</i></font></TD><TD width=\"250\"><font face=verdana, arial, helvetica  SIZE=2><i>Product / Service Description</i></font></TD><TD ALIGN=center width=\"50\"><font face=verdana, arial, helvetica  SIZE=2><i>Spec./ Info?</i></font></TD><TD ALIGN=center width=\"100\"><font face=verdana, arial, helvetica  SIZE=2><i>Stk. Count<BR>($lastdate)</i></font></TD><TD align=\"center\" width=\"50\"><font face=verdana, arial, helvetica  SIZE=2><i>List Price</i></font></TD><TD width=\"50\" align=\"center\"><font face=verdana, arial, helvetica  SIZE=2><i>St. Disc. Price</i></font></TD>";		

		$mycontent = `cat 208/$file/content.dat`;		
		@mylines = split(/:end\n/, $mycontent);
    	foreach $myline (@mylines) {
			@mypairs = split(/,,,,,/, $myline);
			print "<tr>";
			print "<td><font face=verdana, arial, helvetica size=\"1\">$mypairs[0]</font></td>";
			print "<td><font face=verdana, arial, helvetica size=\"1\">$mypairs[1]</font></td>";
			print "<td><font face=verdana, arial, helvetica size=\"1\">$mypairs[2]</font></td>";
			print "<td><font face=verdana, arial, helvetica size=\"1\">$mypairs[3]</font></td>";
			print "<td><font face=verdana, arial, helvetica size=\"1\">$mypairs[4]</font></td>";
			print "<td><font face=verdana, arial, helvetica size=\"1\">$mypairs[5]</font></td>";
			print "<td><font face=verdana, arial, helvetica size=\"1\">$mypairs[6]</font></td>";
			print "</tr>";
		}
		print "</TABLE><br><br>";
	}
	
{
print <<EOF

<font face=verdana, arial, helvetica size=2><center>If you have any questions, comments or suggestions, please <font COLOR=#0000FF><a href="../framer.cgi?new_url=cont_temp.cgi&sub_link=gencomments">E-Mail</a></font> us, Coastline Micro, directly!</center></font>
</body>
</html>

EOF
}
exit;
