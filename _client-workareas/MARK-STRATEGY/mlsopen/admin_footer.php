<?php
require 'settings.php';
include 'header.inc';
$found = 0;

if ($mls_pass == $admin_password) {

	print "<br><center><h2>Admin Footer Setup</h2></center>\n";
	print "<br><center><font color=blue>Do not use special HTML quotes.<br>Example: <font color=yellow><b>\"you.html\"</b></font> should be <font color=yellow><b>you.html</b></font> <br></center>\n"; 
	PRINT "<center><form action=admin_footer2.php method=post>
	<textarea rows=\"20\" name=\"footer\" cols=\"90\">\n";
	$filePointer = fopen("footer.inc", "r");
	while (!feof($filePointer)) {
		$line = fgets($filePointer, 4096);
		print $line;
	}
	fclose($filePointer);
	print "</textarea><br><input type=submit value=\"Save Footer\"></center></form><br><br>\n";
	

} else {
	print "<center><h2>Administrator Login</h2></center><br><br>\n";
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
