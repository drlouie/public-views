<?php
require 'settings.php';
include 'header.inc';

	$found = 0;
	$found_email = 0;

	if (($u_name == "") or ($u_address == "") or ($u_city == "") or ($u_state == "") or ($u_zip == "") or ($u_country == "") or ($u_email == "") or ($uname == "") or ($upass == "")) {
		print "<br><br><center><font color=red><b>Sorry, you did not enter in all the required fields.  Please click back to try again.</center></b></font>\n";
		include 'footer.inc';
		die;
	}

	$linkID = @mysql_connect("$server", "$username", "$password");
	mysql_select_db("$database", $linkID);

	$resultID = mysql_query("SELECT `uname`, `u_email` FROM users", $linkID);
	for ($x= 0; $x < mysql_num_rows($resultID); $x++) {
		$row = mysql_fetch_assoc($resultID);
		if ($uname == $row[uname]) {
			$found = 1;
		}
		if ($u_email == $row[u_email]) {
			$found_email = 1;
		}
	}
	if ($found_email == 1) {
		print "<br><br><center><b><font color=red>Sorry, email address $u_email is already in use.  Please click back and select a different username.</font></b></center><br>\n";
		include 'footer.inc';
		die;
	}
		
	if ($found == 1) {
		print "<br><br><center><b><font color=red>Sorry, $uname is already in use.  Please click back and select a different username.</font></b></center><br>\n";
		include 'footer.inc';
		die;
	} else {
		$img_path = $path . $uname . "/";
		$linkID = @mysql_connect("$server", "$username", "$password");
		mysql_select_db("$database", $linkID);

		$result = mysql_query("INSERT INTO users (uname,upass,img_path,u_name,u_company,u_address,u_city,u_state,u_zip,u_country,u_email,u_phone) VALUES (
		'$uname','$upass','$img_path','$u_name','$u_company','$u_address','$u_city','$u_state','$u_zip','$u_country','$u_email','$u_phone')", $linkID);
		
		if ($result == TRUE) {
			print "<br><br><center>$u_name,<br>Your account has been created.  To login please click <a href=login.php>here</a>.</center><br>\n";
			system("mkdir $img_path 2>&1");
			system("chmod 0777 $img_path 2>&1");
		} else {
			print "<br><center><b><font color=red>There was an error connecting to the MySQL database.</b></font></center><br>\n";
			include 'footer.inc';
			die;
		}
	}
// send the welcome letter

$sendto = "$u_email,$admin_email";
$subject = "Welcome to $site_name";
$msg = "$u_name,
Thank you for signing up to use $site_name Multiple Listing Service.  Below you
will find information needed to log into your account.

Login link: $site_url/login.php
username: $uname
password: $upass

To view your listings you may point this link to your web site:
$site_url/index.php?id=$uname

Once again, thank you for signing up.
$site_name
$site_url";
mail($sendto, $subject, $msg, $headers);

include 'footer.inc';
?>
	

