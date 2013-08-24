<?php
require 'settings.php';
include 'header.inc';
$found = 0;

if ($mls_pass == $admin_password) {

	print "<br><center><h2>Admin Footer Setup</h2></center>\n";
	$filePointer = fopen("footer.inc", "w");
	fputs($filePointer, "$footer\r\n");
	fclose($filePointer);
	print "<br><br><center>Footer file was updated.  Refresh your screen to see the changes.</center><br><br>\n";
	print "<center><a href=admin.php>Home</a><br><br></center>\n";
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
