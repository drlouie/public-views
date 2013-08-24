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

print "
<br><center><b>Open New Trouble Ticket</b></center><br>
<form action=user_troubleticket2.php method=post>
<input type=hidden name=uname value=\"$uname\">
<input type=hidden name=upass value=\"$upass\">
<div align=center>
<table border=1>
<tr><td>Name:</td><td>$u_name</td></tr>
<tr><td>User Name:</td><td>$uname</td></tr>
<tr><td>Problem Description:</td><td><input type=text name=subject size=20 maxlength=20></td></tr>
<tr><td>Detailed Description:</td><td><textarea rows=5 name=msg cols=40></textarea></td></tr>
</table></div>
<center><input type=submit value=\"Submit Trouble Ticket\"></center></form>\n";

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
