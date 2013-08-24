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
<p align=\"center\"><b>Add My Image or Update<br>
<br><center>Leave this form blank and click on Add / Update if you wish to remove MyImage.</center><br>
<form action=user_addmyimage2.php method=post enctype=\"multipart/form-data\">
<div align=\"center\">
  <center>
  <table border=\"1\" width=\"690\" height=\"23\" bgcolor=\"$table_bg_color\"><font color=\"$table_text_color\">
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">My Image Name:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\"><input type=hidden name=mls value=\"$row[mls]\"><input type=hidden name=uname value=\"$uname\"><input type=hidden name=upass value=\"$upass\">\n";

if($uploads <= 1) 
{ 
    $uploads = 1; 
} 


for($i = 1; $i <= $uploads; $i++) { 
	print("<input type=\"file\" name=\"uploadedFile[]\" size=\"25\">\n"); 
}

print "
 


</font></td>
    </tr>
        

  </table></font>
  </center>
</div>
<center><input type=submit value=\"Add / Update MyImage\"></center></form>
<br><center><form action=user_addmyimage2.php method=post>
<input type=hidden name=remove value=remove>
<input type=hidden name=uname value=\"$uname\">
<input type=hidden name=upass value=\"$upass\">
<input type=hidden name=mls value=\"$row[mls]\">
<input type=submit value=\"Remove MyImage\"></center>
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
