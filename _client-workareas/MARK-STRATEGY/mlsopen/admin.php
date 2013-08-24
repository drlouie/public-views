<?php
require 'settings.php';

if ($pass == $admin_password) {
	setcookie ("mls_pass", $pass,time()+2592000); /* expire in 30 days */
}

include 'header.inc';

if (($mls_pass == $admin_password) or ($pass == $admin_password)) {
	print "
	<center><br><br><center><b><H2>MLS Lister Administration</H2></b></center>
	<div align=center><table width=600 border=1 bgcolor=\"$table_bg_color\"><font color=\"$table_text_color\">
	<tr><td><li><a href=admin_users.php>User Management</a></li></td><td><li><a href=admin_listings.php>Listing Management</a></li></td></tr>
	<tr><td><li><a href=admin_header.php>Edit Header File</a></li></td><td><li><a href=admin_footer.php>Edit Footer File</a></li></td></tr>
	<tr><td><li><a href=admin_settings.php>View / Edit Settings</a></li></td><td><li></li></td></tr>

	</font></table></div><br><br>
	\n";
} else {
	print "<center><h2>MLS Lister Administrator Login</h2></center><br><br>\n";
	print "
	<form action=admin.php method=post>
	<div align=center><table border=1 width=600>
	<tr><td>Administration Password:</td><td><input type=password name=pass></td></tr>
	</table></div>
	<center><input type=submit value=Login></center>
	<br><br>
	\n";
} 

echo "</font><br><br>";
include 'footer.inc';
