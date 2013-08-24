<?php
require 'settings.php';
include 'header.inc';

if ($mls_pass == $admin_password) {


	$linkID = @mysql_connect("$server", "$username", "$password");
	mysql_select_db("$database", $linkID);

$result = mysql_query("UPDATE users SET u_name = '$u_name', upass = '$upass', u_company = '$u_company', u_address = '$u_address', u_city = '$u_city', u_state = '$u_state', u_zip = '$u_zip', u_country = '$u_country', u_phone = '$u_phone', u_email = '$u_email', numlistings = '$numlistings' WHERE uname = '$uname'", $linkID);

if ($result == TRUE) {
	print "<br><br><b><center>User record was updated.</center></b><br><br></center>\n";
		print "<center><a href=admin.php>Home</a></center><br>\n";
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
