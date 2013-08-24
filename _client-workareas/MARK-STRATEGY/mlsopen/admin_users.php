<?php

require 'settings.php';
include 'header.inc';

if ($mls_pass == $admin_password) {

$found = 0;
$sourt_order = 0;
print "<br><center><b>Edit / View / Approve / Delete Users</b></center><br>
<div align=center><table border=1>
<tr><td><b><a href=admin_users.php?sort=username>User Name</a></b></td><td><b><a href=admin_users.php?sort=name>Name</a></b></td><td><b><a href=admin_users.php?sort=status>Approved</a></b></td><td><b><a href=admin_users.php?sort=listings>Account Limit</a></b></td><td><b>Action</b></td></tr>\n";

	$linkID = @mysql_connect("$server", "$username", "$password");
	mysql_select_db("$database", $linkID);

	
	if ($sort == "username") {
		$resultID = mysql_query("SELECT * FROM `users` WHERE 1 ORDER BY `uname` ASC", $linkID);
		$sourt_order=1;
	}


	if ($sort == "name") {
		$resultID = mysql_query("SELECT * FROM `users` WHERE 1 ORDER BY `u_name` ASC", $linkID);
		$sourt_order=1;
	}

	if ($sort == "status") {
		$resultID = mysql_query("SELECT * FROM `users` WHERE 1 ORDER BY `numlistings` ASC", $linkID);
		$sourt_order=1;
	}


	if ($sort == "listings") {
		$resultID = mysql_query("SELECT * FROM `users` WHERE 1 ORDER BY `numlistings` ASC", $linkID);
		$sourt_order=1;
	}




	if ($sourt_order == 0) {
		$resultID = mysql_query("SELECT * FROM `users`", $linkID);
	}

	for ($x= 0; $x < mysql_num_rows($resultID); $x++) {
		$row = mysql_fetch_assoc($resultID);
		if ($row[numlistings] == 0) {
			$approved = "<font color=red><b>No</b></font>";
		} else {
			$approved = "Yes";
		}
		$found = 1;
		print "<tr><td>$row[uname]</td><td>$row[u_name]</td><td>$approved</td><td>$row[numlistings]</td><td><form action=admin_user_action.php method=post>
<input type=hidden name=uname value=\"$row[uname]\">
<input type=hidden name=email value=\"$row[u_email]\">
<input type=hidden name=u_name value=\"$row[u_name]\">
  <p><input type=\"radio\" value=\"edit\" name=\"action_type\" checked> Edit<input type=\"radio\" value=\"approve\" name=\"action_type\">
  Approve <input type=\"radio\" value=\"delete\" name=\"action_type\"> Delete<input type=\"submit\" value=\"Go\" name=\"submit\"></p>
</form></td></tr>\n";
	}
print "</table></div>\n";

if ($found == 0) {
	print "<br><center><b>There are no users to display.</b></center><br>\n";
}

		


} else {
	print "<center><h2>MLS Lister Administrator Login</h2></center><br><br>\n";
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
