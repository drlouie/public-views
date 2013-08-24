<?php

require 'settings.php';
include 'header.inc';

if ($mls_pass == $admin_password) {

	if ($custom_color_code_bg != "") {
		$table_bg_color2 = "#" . $custom_color_code_bg;
	}

	if ($custom_color_code_text != "") {
		$table_text_color2 = "#" . $custom_color_code_text;
	}

	$linkID = @mysql_connect("$server", "$username", "$password");
	$fileext = ".";
	$filename = $path2;
	$filename = $filename . $fileext;

	if (file_exists($filename)) {
		//
	} else {
		system("mkdir $path2 2>&1");
		system("chmod 0777 $path2 2>&1");
	}
	


	mysql_select_db("$database", $linkID);

$result = mysql_query("UPDATE settings SET admin_password = '$admin_password2', admin_email = '$admin_email2', headers  = '$headers2',
site_name = '$site_name2', site_url = '$site_url2', table_bg_color = '$table_bg_color2', table_text_color = '$table_text_color2',
maxsize = '$maxsize2', path = '$path2', img_url = '$img_url2', image_size_1 = '$image_size_1_2', image_size_2 = '$image_size_2_2',
my_image_size_1 = '$my_image_size_1_2', my_image_size_2 = '$my_image_size_2_2', details_main_image_1 = '$details_main_image_1_2',
details_main_image_2 = '$details_main_image_2_2', details_bottom_image_1a = '$details_bottom_image_1a_2', details_bottom_image_2a = '$details_bottom_image_2a_2',
details_bottom_image_1b = '$details_bottom_image_1b_2', details_bottom_image_2b = '$details_bottom_image_2b_2', details_bottom_image_1c = '$details_bottom_image_1c_2',
details_bottom_image_2c = '$details_bottom_image_2c_2', details_bottom_image_1d = '$details_bottom_image_1d_2', details_bottom_image_2d = '$details_bottom_image_2d_2',
details_bottom_image_1e = '$details_bottom_image_1e_2', details_bottom_image_2e = '$details_bottom_image_2e_2', details_bottom_image_1f = '$details_bottom_image_1f_2',
details_bottom_image_2f = '$details_bottom_image_2f_2', details_bottom_image_1g = '$details_bottom_image_1g_2', details_bottom_image_2g = '$details_bottom_image_2g_2',
details_bottom_image_1h = '$details_bottom_image_1h_2', details_bottom_image_2h = '$details_bottom_image_2h_2', details_bottom_image_1i = '$details_bottom_image_1i_2',
details_bottom_image_2i = '$details_bottom_image_2i_2', php_v = '$php_v_2', paypal = '$paypalid', price_per_listing = '$price_per_listing2'
WHERE id  =  '1'" ,  $linkID);

if ($result == TRUE) {
	print "<br><br><b><center>Configuration settings have been applied.  Please re-login.</center></b><br><br></center>\n";
		print "<center><a href=admin.php>Login</a></center><br>\n";
} else {
	print "<center><font color=red><b>The server was unable to write to the MySQL DataBase.<br><br></b></font></center>\n";
}




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
