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

	$linkID2 = @mysql_connect("$server", "$username", "$password");
	mysql_select_db("$database", $linkID2);

	$resultID2 = mysql_query("SELECT header,footer,main_template,detailed_template FROM `user_settings` WHERE 1 AND `uname` = '$uname'", $linkID2);

	for ($x= 0; $x < mysql_num_rows($resultID2); $x++) {
		$row = mysql_fetch_assoc($resultID2);
		$temp_header = $row[header];
		$temp_footer = $row[footer];
		$temp_main_template = $row[main_template];
		$temp_detailed_template = $row[detailed_template];
	}
print "
<div align=center><table>

<tr><td>
	<div align=center><table border=1>
	<form action=user_settings_save.php>
	<input type=hidden name=option value=header>
	<input type=hidden name=uname value=\"$uname\">
	<input type=hidden name=upass value=\"$upass\">
	<tr><td>Create/Edit Header</td></tr>
	<tr><td><textarea rows=\"8\" name=\"header\" cols=\"40\">$temp_header</textarea></td></tr>
	<tr><td><center><input type=submit value=\"Save Header\"></center></form></td></tr>
	</table></div>
</td><td>
	<div align=center><table border=1>
	<form action=user_settings_save.php>
	<input type=hidden name=option value=footer>
	<input type=hidden name=uname value=\"$uname\">
	<input type=hidden name=upass value=\"$upass\">
	<tr><td>Create/Edit Footer</td></tr>
	<tr><td><textarea rows=\"8\" name=\"footer\" cols=\"40\">$temp_footer</textarea></td></tr>
	<tr><td><center><input type=submit value=\"Save Footer\"></center></form></td></tr>
	</table></div>
</td></tr>
<tr><td>
	<div align=center><table border=1>
	<form action=user_settings_save.php>
	<input type=hidden name=uname value=\"$uname\">
	<input type=hidden name=upass value=\"$upass\">
	<input type=hidden name=option value=main_template>
	<tr><td>Create/Edit Main Template<br><a href=template_commands.php#main target=_blank>Click here for template commands</a></td></tr>
	<tr><td><textarea rows=\"8\" name=\"main_template\" cols=\"40\">$temp_main_template</textarea></td></tr>
	<tr><td><center><input type=submit value=\"Save Main Template\"></center></form></td></tr>
	</table></div>
</td><td>
	<div align=center><table border=1>
	<form action=user_settings_save.php>
	<input type=hidden name=option value=detailed_template>
	<input type=hidden name=uname value=\"$uname\">
	<input type=hidden name=upass value=\"$upass\">
	<tr><td>Create/Edit Detailed Template<br><a href=template_commands.php#detailed target=_blank>Click here for template commands</a></td></tr>
	<tr><td><textarea rows=\"8\" name=\"detailed_template\" cols=\"40\">$temp_detailed_template</textarea></td></tr>
	<tr><td><center><input type=submit value=\"Save Detailed Template\"></center></form></td></tr>
	</table></div>
</td></tr>
</table></div>\n";










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
