<?php
require 'settings.php';
include 'header.inc';

if ($mls_pass == $admin_password) {

	print "<br><center><b>Admin Update Item</b></center>\n";
	$linkID = @mysql_connect("$server", "$username", "$password");
	mysql_select_db("$database", $linkID);

$result = mysql_query("UPDATE users SET u_name = '$update_name', u_company = '$update_company', u_address = '$update_address',
u_city = '$update_city', u_state = '$update_state', u_zip = '$update_zip', u_country = '$update_country', u_phone = '$update_phone',
upass = '$update_password' WHERE uname  =  '$uname'" ,  $linkID);


if ($result == TRUE) {
	print "<br><br><b><center>User registration was updated.</center></b><br><br></center>\n";
		print "<center><a href=login.php>Login</a></center><br>\n";
} else {
	print "<center><font color=red><b>The server was unable to write to the MySQL DataBase.<br><br></b></font></center>\n";
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
