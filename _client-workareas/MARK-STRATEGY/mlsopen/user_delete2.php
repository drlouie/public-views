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

	print "<br><center><h2>Admin Delete MLS Number</h2></center>\n";
	$linkID = @mysql_connect("$server", "$username", "$password");
	mysql_select_db("$database", $linkID);
	$result = mysql_query("DELETE FROM user_mls WHERE mls = '$mls'", $linkID);
	//$result = mysql_query("DELETE FROM feedback WHERE mls_number = '$mls'", $linkID);
	if ($result == TRUE) {
		print "<center><b>MLS Number $mls was successfully deleted.</b></center>\n";
		print "<center><a href=login.php?uname=$uname&upass=$upass>Home</a></center><br>\n";
	} else {
		print "<center><b><font color=red>Changed to the database failed.  A possible SQL error.</font></b></center>\n";
	}
	mysql_close($linkID);


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
