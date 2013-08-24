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

	print "<br><center><b>Update Status</b></center>\n";
	$linkID = @mysql_connect("$server", "$username", "$password");
	mysql_select_db("$database", $linkID);

$result = mysql_query("UPDATE user_mls SET status = '$status' WHERE 1 AND mls  =  '$mls' AND realtor_user_name = '$uname'" ,  $linkID);


if ($result == TRUE) {
	print "<br><br><b><center>MLS number $mls was updated.</center></b><br><br></center>\n";
		print "<center><a href=login.php?uname=$uname&upass=$upass>Home</a></center><br>\n";
} else {
	print "<center><font color=red><b>The server was unable to write to the MySQL DataBase.<br><br></b></font></center>\n";
}

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
