<?php
require 'settings.php';
include 'header.inc';
$found = 0;

if ($mls_pass == $admin_password) {

	print "<br><center><h2>Admin Delete MLS Number</h2></center>\n";
	$linkID = @mysql_connect("$server", "$username", "$password");
	mysql_select_db("$database", $linkID);
	$result = mysql_query("DELETE FROM mls WHERE mls = '$mls'", $linkID);
	$result = mysql_query("DELETE FROM feedback WHERE mls_number = '$mls'", $linkID);
	if ($result == TRUE) {
		print "<center><b>MLS Number $mls was successfully deleted.</b></center>\n";
		print "<center><a href=admin.php>Home</a></center><br>\n";
	} else {
		print "<center><b><font color=red>Changed to the database failed.  A possible SQL error.</font></b></center>\n";
	}
	mysql_close($linkID);


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
