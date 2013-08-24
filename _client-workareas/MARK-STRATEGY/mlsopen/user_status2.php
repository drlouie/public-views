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
	$linkID = @mysql_connect("$server", "$username", "$password");
	mysql_select_db("$database", $linkID);

	$resultID = mysql_query("SELECT mls, realtor_user_name, myimage FROM user_mls", $linkID);

	for ($x= 0; $x < mysql_num_rows($resultID); $x++) {
		$row = mysql_fetch_assoc($resultID);
		if (($row[mls] == $mls) and ($row[realtor_user_name] == $uname)) {
			print "
<p align=\"center\"><b>Update Listing Status<br>
<form action=user_status3.php method=post>
<div align=\"center\">
  <center>
  <table border=\"1\" width=\"690\" height=\"23\" bgcolor=\"$table_bg_color\"><font color=\"$table_text_color\">
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">New Status:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">
<select size=\"1\" name=\"status\">
    <option selected value=\"\">For Sale</option>
    <option>For Rent</option>
    <option>For Lease</option>
    <option>Under Contract</option>
    <option>Sold</option>
</select>
<input type=hidden name=mls value=\"$row[mls]\">
<input type=hidden name=uname value=\"$uname\">
<input type=hidden name=upass value=\"$upass\">
</font></td>
    </tr>
        

  </table></font>
  </center>
</div>
<center><input type=submit value=\"Update Status\"></center>
</form>
\n";
	}
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

?>
