<?php
require 'settings.php';
include 'header.inc';

if ($mls_pass == $admin_password) {

	// Edit Users

	if ($action_type == "edit") {

		print "<br><center><b>Edit - View Users</b></center><br>\n";

	
		$resultID = mysql_query("SELECT * FROM `users` WHERE 1 AND `uname` = '$uname' ", $linkID);
		for ($x= 0; $x < mysql_num_rows($resultID); $x++) {
			$row = mysql_fetch_assoc($resultID);
			print "<div align=center><table border=1>
			<form action=admin_users_update.php method=post>
			<input type=hidden name=uname value=\"$uname\">
			<tr><td>User Name:</td><td>$row[uname]</td></tr>
			<tr><td>Password:</td><td><input type=text name=upass value=\"$row[upass]\"></td></tr>
			<tr><td>Name:</td><td><input type=text name=u_name value=\"$row[u_name]\"></td></tr>
			<tr><td>Company:</td><td><input type=text name=u_company value=\"$row[u_company]\"></td></tr>
			<tr><td>Address:</td><td><input type=text name=u_address value=\"$row[u_address]\"></td></tr>
			<tr><td>City:</td><td><input type=text name=u_city value=\"$row[u_city]\"></td></tr>
			<tr><td>State:</td><td><input type=text name=u_state value=\"$row[u_state]\"></td></tr>
			<tr><td>Zip:</td><td><input type=text name=u_zip value=\"$row[u_zip]\"></td></tr>
			<tr><td>Country:</td><td><input type=text name=u_country value=\"$row[u_country]\"></td></tr>
			<tr><td>Phone:</td><td><input type=text name=u_phone value=\"$row[u_phone]\"></td></tr>
			<tr><td>Email:</td><td><input type=text name=u_email value=\"$row[u_email]\"></td></tr>
			<tr><td>Listings Allowed:</td><td><input type=text name=numlistings value=\"$row[numlistings]\"></td></tr>
			</table></div>
			<center><input type=submit value=\"Save Changes\"></center></form><br>\n";
		}
	}

	// Approve Users

	if ($action_type == "approve") {

		$linkID = @mysql_connect("$server", "$username", "$password");
		mysql_select_db("$database", $linkID);

		$result = mysql_query("UPDATE users SET numlistings = '1' WHERE uname = '$uname'", $linkID);

		if ($result == TRUE) {
			print "<br><br><b><center>User record was updated and approved.</center></b><br><br></center>\n";
			print "<center><a href=admin.php>Home</a></center><br>\n";
			$sendto = "$email,$admin_email";
			$subject = "Welcome to $site_name";
			$msg = "$u_name,
			Thank you for signing up to use $site_name Multiple Listing Service.  
			Your account has now been approved and you can start adding listings.

			Once again, thank you for signing up.
			$site_name
			$site_url";
			mail($sendto, $subject, $msg, $headers);
		} else {
			print "<center><font color=red><b>The server was unable to write to the MySQL DataBase.<br><br></b></font></center>\n";
		}
	}

	// Delete Users

	if ($action_type == "delete") {

		$linkID = @mysql_connect("$server", "$username", "$password");
		mysql_select_db("$database", $linkID);
		$result = mysql_query("DELETE FROM user_mls WHERE realtor_user_name = '$uname'", $linkID);

		if ($result == TRUE) {
			print "<center><b>User Listings were deleted.</b></center>\n";
		} else {
			print "<center><b><font color=red>Changed to the database failed.  A possible SQL error.</font></b></center>\n";
		}

		$linkID2 = @mysql_connect("$server", "$username", "$password");
		mysql_select_db("$database", $linkID2);
		$result2 = mysql_query("DELETE FROM users WHERE uname = '$uname'", $linkID);

		if ($result == TRUE) {
			print "<center><b>User Record was deleted.</b></center>\n";
		} else {
			print "<center><b><font color=red>Changed to the database failed.  A possible SQL error.</font></b></center>\n";
		}
		$img_path = $path . $uname . "/";

		system("rm -Rf $img_path 2>&1");

		print "<center><b><font color=blue>Note: If front page extentions are enabled you will have to manually remove the $image_path directory.</center></b></font><br><center><a href=admin.php>Home</a></center><br>\n";
		



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
