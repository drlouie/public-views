<?php

require 'settings.php';
include 'header.inc';

if ($mls_pass == $admin_password) {

$found = 0;
$sourt_order = 0;
print "<br><center><b>Edit / View / Approve / Delete Listings</b></center><br>
<div align=center><table border=1>
<tr><td><b><a href=admin_listings.php?sort=username>User Name</a></b></td><td><b><a href=admin_listings.php?sort=price>Price</a></b></td><td><b><a href=admin_listings.php?sort=mls>MLS Number</a></b></td><td><b><a href=admin_listings.php?sort=title>Title</a></b></td><td><b>Action</b></td></tr>\n";

	$linkID = @mysql_connect("$server", "$username", "$password");
	mysql_select_db("$database", $linkID);

	
	if ($sort == "username") {
		$resultID = mysql_query("SELECT * FROM `user_mls` WHERE 1 ORDER BY `realtor_user_name` ASC", $linkID);
		$sourt_order=1;
	}


	if ($sort == "price") {
		$resultID = mysql_query("SELECT * FROM `user_mls` WHERE 1 ORDER BY `price` ASC", $linkID);
		$sourt_order=1;
	}

	if ($sort == "mls") {
		$resultID = mysql_query("SELECT * FROM `user_mls` WHERE 1 ORDER BY `mls` ASC", $linkID);
		$sourt_order=1;
	}


	if ($sort == "title") {
		$resultID = mysql_query("SELECT * FROM `user_mls` WHERE 1 ORDER BY `title` ASC", $linkID);
		$sourt_order=1;
	}




	if ($sourt_order == 0) {
		$resultID = mysql_query("SELECT * FROM `user_mls`", $linkID);
	}

	for ($x= 0; $x < mysql_num_rows($resultID); $x++) {
		$row = mysql_fetch_assoc($resultID);
		$found = 1;
		print "<tr><td>$row[realtor_user_name]</td><td>$row[price]</td><td>$row[mls]</td><td>$row[title]</td><td><form action=admin_listings_action.php method=post>
<input type=hidden name=uname value=\"$row[realtor_user_name]\">
<input type=hidden name=mls value=\"$row[mls]\">
  <p><input type=\"radio\" value=\"edit\" name=\"action_type\" checked> Edit
  <input type=\"radio\" value=\"delete\" name=\"action_type\"> Delete<input type=\"submit\" value=\"Go\" name=\"submit\"></p>
</form></td></tr>\n";
	}
print "</table></div>\n";

if ($found == 0) {
	print "<br><center><b>There are no listings to display.</b></center><br>\n";
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
