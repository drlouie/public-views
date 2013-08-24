<?php
require 'settings.php';
include 'header.inc';
$found = 0;

if ($mls_pass == $admin_password) {

	print "<br><center><h2>Admin Delete MLS Number</h2></center>\n";
	print "<div align=center><table border=1  bgcolor=\"$table_bg_color\">
	<tr><td><center><b><font color=\"$table_text_color\">MLS Number</font></b></center></td><td><center><b><font color=\"$table_text_color\">Title</font></b></center></td><td><center><b><font color=\"$table_text_color\">Listing Price</font></b></center></td><td><center><b><font color=\"$table_text_color\">City</font></b></center></td><td></td></tr>\n";

	$linkID = @mysql_connect("$server", "$username", "$password");
	mysql_select_db("$database", $linkID);

	$resultID = mysql_query("SELECT mls, title, price, property_city FROM mls", $linkID);

	for ($x= 0; $x < mysql_num_rows($resultID); $x++) {
		$row = mysql_fetch_assoc($resultID);
		print "<tr><td><font color=\"$table_text_color\">$row[mls]</font></td><td><font color=\"$table_text_color\">$row[title]</font></td><td><font color=\"$table_text_color\">\$$row[price]</font></td><td><font color=\"$table_text_color\">$row[property_city]</font></td><td><form action=admin_delete2.php method=post><input type=hidden name=mls value=\"$row[mls]\"><input type=submit value=\"Delete MLS Number\"></form></td></tr>\n";
		$found = 1;
	}
	
	print "</table></div><br><br>\n";
	
	if ($found == 0) {
		print "<br><br><b><center>There are no items to display.<br></b><br></center>\n";
		include 'footer.inc';
		die;
	}
} else {
	print "<center><h2>Administrator Login</h2></center><br><br>\n";
	print "
	<form action=admin.php method=post>
	<div align=center><table border=1 width=600>
	<tr><td>Administration Password:</td><td><input type=password name=pass></td></tr>
	</table></div>
	<center><input type=submit value=Login></center>
	<br><br>
	\n";
} 

include 'footer.inc';
?>
