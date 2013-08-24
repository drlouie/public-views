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

print "<br><center><b>User Settings:<br>(Create Header, Footer, Templates)<br></center></b>\n";



// Edit or Save Header
if ($option == "header") {

	$found = 0;
	$linkID = @mysql_connect("$server", "$username", "$password");
	mysql_select_db("$database", $linkID);

	$resultID = mysql_query("SELECT * FROM `user_settings` WHERE 1 AND uname = '$uname'", $linkID);
	for ($x= 0; $x < mysql_num_rows($resultID); $x++) {
		$found = 1;
	}

	if ($found == "0") {
		$linkID2 = @mysql_connect("$server", "$username", "$password");
		mysql_select_db("$database", $linkID2);

		$result2 = mysql_query("INSERT INTO user_settings (uname,header) VALUES ('$uname','$header')", $linkID2);
		if ($result2 == TRUE) {
			print "<center><br><br>Header was updated/created.<br><a href=login.php?uname=$uname&upass=$upass>Home</a></center><br><br>\n";
		} else {
			print "<center><font color=red><b>The server was unable to write to the MySQL DataBase.<br><br></b></font></center>\n";
		}
	} else {
		$linkID3 = @mysql_connect("$server", "$username", "$password");
		mysql_select_db("$database", $linkID3);

		$result3 = mysql_query("UPDATE user_settings SET header = '$header' WHERE uname = '$uname'" ,  $linkID3);
		if ($result3 == TRUE) {
			print "<center><br><br>Header was updated/created.<br><a href=login.php?uname=$uname&upass=$upass>Home</a></center><br><br>\n";
		} else {
			print "<center><font color=red><b>The server was unable to write to the MySQL DataBase.<br><br></b></font></center>\n";
		}
	}
}
// End header

// Edit or Save Footer
if ($option == "footer") {

	$found = 0;
	$linkID = @mysql_connect("$server", "$username", "$password");
	mysql_select_db("$database", $linkID);

	$resultID = mysql_query("SELECT * FROM `user_settings` WHERE 1 AND uname = '$uname'", $linkID);
	for ($x= 0; $x < mysql_num_rows($resultID); $x++) {
		$found = 1;
	}

	if ($found == "0") {
		$linkID2 = @mysql_connect("$server", "$username", "$password");
		mysql_select_db("$database", $linkID2);

		$result2 = mysql_query("INSERT INTO user_settings (uname,footer) VALUES ('$uname','$footer')", $linkID2);
		if ($result2 == TRUE) {
			print "<center><br><br>Footer was updated/created.<br><a href=login.php?uname=$uname&upass=$upass>Home</a></center><br><br>\n";
		} else {
			print "<center><font color=red><b>The server was unable to write to the MySQL DataBase.<br><br></b></font></center>\n";
		}
	} else {
		$linkID3 = @mysql_connect("$server", "$username", "$password");
		mysql_select_db("$database", $linkID3);

		$result3 = mysql_query("UPDATE user_settings SET footer = '$footer' WHERE uname = '$uname'" ,  $linkID3);
		if ($result3 == TRUE) {
			print "<center><br><br>Footer was updated/created.<br><a href=login.php?uname=$uname&upass=$upass>Home</a></center><br><br>\n";
		} else {
			print "<center><font color=red><b>The server was unable to write to the MySQL DataBase.<br><br></b></font></center>\n";
		}
	}
}
// End Footer

// Edit or Save Main Template
if ($option == "main_template") {

	$found = 0;
	$linkID = @mysql_connect("$server", "$username", "$password");
	mysql_select_db("$database", $linkID);

	$resultID = mysql_query("SELECT * FROM `user_settings` WHERE 1 AND uname = '$uname'", $linkID);
	for ($x= 0; $x < mysql_num_rows($resultID); $x++) {
		$found = 1;
	}

	if ($found == "0") {
		$linkID2 = @mysql_connect("$server", "$username", "$password");
		mysql_select_db("$database", $linkID2);

		$result2 = mysql_query("INSERT INTO user_settings (uname,main_template) VALUES ('$uname','$main_template')", $linkID2);
		if ($result2 == TRUE) {
			print "<center><br><br>Main Template was updated/created.<br><a href=login.php?uname=$uname&upass=$upass>Home</a></center><br><br>\n";
		} else {
			print "<center><font color=red><b>The server was unable to write to the MySQL DataBase.<br><br></b></font></center>\n";
		}
	} else {
		$linkID3 = @mysql_connect("$server", "$username", "$password");
		mysql_select_db("$database", $linkID3);

		$result3 = mysql_query("UPDATE user_settings SET main_template = '$main_template' WHERE uname = '$uname'" ,  $linkID3);
		if ($result3 == TRUE) {
			print "<center><br><br>Main Template was updated/created.<br><a href=login.php?uname=$uname&upass=$upass>Home</a></center><br><br>\n";
		} else {
			print "<center><font color=red><b>The server was unable to write to the MySQL DataBase.<br><br></b></font></center>\n";
		}
	}
}
// End Main Template

// Edit or Save Detailed Template
if ($option == "detailed_template") {

	$found = 0;
	$linkID = @mysql_connect("$server", "$username", "$password");
	mysql_select_db("$database", $linkID);

	$resultID = mysql_query("SELECT * FROM `user_settings` WHERE 1 AND uname = '$uname'", $linkID);
	for ($x= 0; $x < mysql_num_rows($resultID); $x++) {
		$found = 1;
	}

	if ($found == "0") {
		$linkID2 = @mysql_connect("$server", "$username", "$password");
		mysql_select_db("$database", $linkID2);

		$result2 = mysql_query("INSERT INTO user_settings (uname,detailed_template) VALUES ('$uname','$detailed_template')", $linkID2);
		if ($result2 == TRUE) {
			print "<center><br><br>Detailed Template was updated/created.<br><a href=login.php?uname=$uname&upass=$upass>Home</a></center><br><br>\n";
		} else {
			print "<center><font color=red><b>The server was unable to write to the MySQL DataBase.<br><br></b></font></center>\n";
		}
	} else {
		$linkID3 = @mysql_connect("$server", "$username", "$password");
		mysql_select_db("$database", $linkID3);

		$result3 = mysql_query("UPDATE user_settings SET detailed_template = '$detailed_template' WHERE uname = '$uname'" ,  $linkID3);
		if ($result3 == TRUE) {
			print "<center><br><br>Detailed Template was updated/created.<br><a href=login.php?uname=$uname&upass=$upass>Home</a></center><br><br>\n";
		} else {
			print "<center><font color=red><b>The server was unable to write to the MySQL DataBase.<br><br></b></font></center>\n";
		}
	}
}
// End Detailed Template


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
