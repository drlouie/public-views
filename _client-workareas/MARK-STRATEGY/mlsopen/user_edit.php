<?php
require 'settings.php';

$found = 0;
$active = 0;

	$linkID = @mysql_connect("$server", "$username", "$password");
	mysql_select_db("$database", $linkID);

	$resultID = mysql_query("SELECT * FROM `users`", $linkID);
	for ($x= 0; $x < mysql_num_rows($resultID); $x++) {
		$row = mysql_fetch_assoc($resultID);
		if (($uname == $row[uname]) and ($upass == $row[upass])) {
			$found = 1;
			$u_name = $row[u_name];
			$numlistings = $row[numlistings];
		}
	}

if ($found == 1) {
	setcookie ("mls_uname", $uname,time()+2592000); /* expire in 30 days */
	setcookie ("mls_upass", $upass,time()+2592000); /* expire in 30 days */
} 

include 'header.inc';

if (($mls_uname == $uname) and ($mls_upass == $upass) and ($found == 1)) {

	print "<br><center><h2>Edit Items for $u_name</h2></center>\n";
	print "<div align=center><table border=1  bgcolor=\"$table_bg_color\">
	<tr><td><center><b><font color=\"$table_text_color\">MLS Number</font></b></center></td><td><center><b><font color=\"$table_text_color\">Title</font></b></center></td><td><center><b><font color=\"$table_text_color\">Listing Price</font></b></center></td><td><center><b><font color=\"$table_text_color\">City</font></b></center></td><td></td></tr>\n";

	$linkID = @mysql_connect("$server", "$username", "$password");
	mysql_select_db("$database", $linkID);

	$resultID = mysql_query("SELECT mls, realtor_user_name, title, price, property_city FROM user_mls", $linkID);

	for ($x= 0; $x < mysql_num_rows($resultID); $x++) {
		$row = mysql_fetch_assoc($resultID);
		if ($row[realtor_user_name] == $uname) {
			print "<tr><td><font color=\"$table_text_color\">$row[mls]</font></td><td><font color=\"$table_text_color\">$row[title]</font></td><td><font color=\"$table_text_color\">\$$row[price]</font></td><td><font color=\"$table_text_color\">$row[property_city]</font></td><td><form action=user_edit2.php method=post><input type=hidden name=uname value=\"$uname\"><input type=hidden name=upass value=\"$upass\"><input type=hidden name=mls value=\"$row[mls]\"><input type=submit value=\"Edit\"></form></td></tr>\n";
			$found = 1;
		}
	}
	
	print "</table></div><br><br>\n";
	
	if ($found == 0) {
		print "<br><br><b><center>There are no items to display.<br></b><br></center>\n";
		include 'footer.inc';
		die;
	}
} else {
	print "<center><h2>User Administrator Login</h2></center><br><br>\n";
	print "
	<form action=login.php method=post>
	<div align=center><table border=1 width=600>
	<tr><td>Username:</td><td><input type=text name=uname></td></tr>
	<tr><td>Password:</td><td><input type=password name=upass></td></tr>
	</table></div>
	<center><input type=submit value=Login></center>
	<br><br>
	\n";
} 

include 'footer.inc';
?>
