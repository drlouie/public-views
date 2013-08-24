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
			$update_upass = $row[upass];
			$update_u_name = $row[u_name];
			$update_u_company = $row[u_company];
			$update_u_address = $row[u_address];
			$update_u_city = $row[u_city];
			$update_u_state = $row[u_state];
			$update_u_zip = $row[u_zip];
			$update_u_country = $row[u_country];
			$update_u_phone = $row[u_phone];
		}
	}

if ($found == 1) {
	setcookie ("mls_uname", $uname,time()+2592000); /* expire in 30 days */
	setcookie ("mls_upass", $upass,time()+2592000); /* expire in 30 days */
} 

include 'header.inc';

if (($mls_uname == $uname) and ($mls_upass == $upass) and ($found == 1)) {

print "<br><center><b>Update Registration</b></center><br>\n";
print "<form action=updatereg2.php method=post>
<input type=hidden name=uname value=\"$uname\">
<input type=hidden name=upass valud=\"$upass\">
<div align=center><table border=1>
<tr><td>Name:</td><td><input type=text name=update_name value=\"$update_u_name\" size=20></td></tr>
<tr><td>Company:</td><td><input type=text name=update_company value=\"$update_u_company\" size=20></td></tr>
<tr><td>Address:</td><td><input type=text name=update_address value=\"$update_u_address\" size=20></td></tr>
<tr><td>City:</td><td><input type=text name=update_city value=\"$update_u_city\" size=20></td></tr>
<tr><td>State:</td><td><input type=text name=update_state value=\"$update_u_state\" size=20></td></tr>
<tr><td>Zip:</td><td><input type=text name=update_zip value=\"$update_u_zip\" size=20></td></tr>
<tr><td>Country:</td><td><input type=text name=update_country value=\"$update_u_country\" size=20></td></tr>
<tr><td>Phone:</td><td><input type=text name=update_phone value=\"$update_u_phone\" size=20></td></tr>
<tr><td>Password:</td><td><input type=text name=update_password value=\"$update_upass\" size=20></td></tr>
</table></div>
<center><input type=submit value=\"Update Registration\"></center><br>\n";








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
