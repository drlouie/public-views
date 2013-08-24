<?php
require 'config.php';


	$linkID = @mysql_connect("$server", "$username", "$password");
	mysql_select_db("$database", $linkID);

	$resultID = mysql_query("SELECT `admin_password` , `admin_email` , `headers` , `site_name` , `site_url` , `table_bg_color` , `table_text_color` , `maxsize` , `path` , `img_url` , `realtor_name_set` , `realtor_company` , `realtor_phone_set` , `image_size_1` , `image_size_2` , `my_image_size_1` , `my_image_size_2` , `details_main_image_1` , `details_main_image_2` , `details_bottom_image_1a` , `details_bottom_image_2a` , `details_bottom_image_1b` , `details_bottom_image_2b` , `details_bottom_image_1c` , `details_bottom_image_2c` , `details_bottom_image_1d` , `details_bottom_image_2d` , `details_bottom_image_1e` , `details_bottom_image_2e` , `details_bottom_image_1f` , `details_bottom_image_2f` , `details_bottom_image_1g` , `details_bottom_image_2g` , `details_bottom_image_1h` , `details_bottom_image_2h` , `details_bottom_image_1i` , `details_bottom_image_2i` , `php_v`, `paypal`, `price_per_listing` FROM `settings` WHERE 1 LIMIT 0, 1 ", $linkID);

	for ($x= 0; $x < mysql_num_rows($resultID); $x++) {
		// These are global varables.
		$row = mysql_fetch_assoc($resultID);
		$admin_password = $row[admin_password];
		$admin_email = $row[admin_email];
		$headers = $row[headers];
		$site_name = $row[site_name];
		$site_url = $row[site_url];
		$table_bg_color = $row[table_bg_color];
		$table_text_color = $row[table_text_color];
		$maxsize = $row[maxsize];
		$path = $row[path];
		$img_url = $row[img_url];
		$realtor_name_set = $row[realtor_name_set];
		$realtor_company = $row[realtor_company];
		$realtor_phone_set = $row[realtor_phone_set];
		$image_size_1 = $row[image_size_1];
		$image_size_2 = $row[image_size_2];
		$my_image_1 = $row[my_image_size_1];
		$my_image_2 = $row[my_image_size_2];
		$details_main_image_1 = $row[details_main_image_1];
		$details_main_image_2 = $row[details_main_image_2];
		$details_bottom_image_1a = $row[details_bottom_image_1a];
		$details_bottom_image_2a = $row[details_bottom_image_2a];
		$details_bottom_image_1b = $row[details_bottom_image_1b];
		$details_bottom_image_2b = $row[details_bottom_image_2b];
		$details_bottom_image_1c = $row[details_bottom_image_1c];
		$details_bottom_image_2c = $row[details_bottom_image_2c];
		$details_bottom_image_1d = $row[details_bottom_image_1d];
		$details_bottom_image_2d = $row[details_bottom_image_2d];
		$details_bottom_image_1e = $row[details_bottom_image_1e];
		$details_bottom_image_2e = $row[details_bottom_image_2e];
		$details_bottom_image_1f = $row[details_bottom_image_1f];
		$details_bottom_image_2f = $row[details_bottom_image_2f];
		$details_bottom_image_1g = $row[details_bottom_image_1g];
		$details_bottom_image_2g = $row[details_bottom_image_2g];
		$details_bottom_image_1h = $row[details_bottom_image_1h];
		$details_bottom_image_2h = $row[details_bottom_image_2h];
		$details_bottom_image_1i = $row[details_bottom_image_1i];
		$details_bottom_image_2i = $row[details_bottom_image_2i];
		$php_v = $row[php_v];
		$paypal = $row[paypal];
		$price_per_listing = $row[price_per_listing];
	}

if ($php_v == "4.2.2") {
	//
} else {
	extract($HTTP_GET_VARS);
}			


?>
