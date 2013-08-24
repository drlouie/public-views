<?php

require 'settings.php';
include 'header.inc';

if ($mls_pass == $admin_password) {

print "
<form action=admin_settings2.php method=post>
<b><center>MLS Lister Configuration</center></b>
<br><br><center><b>General Settings:</b></center>
<div align=center><table border=1>
<tr><td>Admin Password:</td><td><input type=text name=admin_password2 value=\"$admin_password\" size=40></td></tr>
<tr><td>Admin Email:</td><td><input type=text name=admin_email2 value=\"$admin_email\" size=40></td></tr>
<tr><td>E-Mail Headers:</td><td><input type=text name=headers2 value=\"$headers\" size=40></td></tr>
<tr><td>Site Name:</td><td><input type=text name=site_name2 value=\"$site_name\" size=40></td></tr>
<tr><td>Site URL:</td><td><input type=text name=site_url2 value=\"$site_url\" size=40></td></tr>
<tr><td>Table Background Color:</td><td>
<select size=\"1\" name=\"table_bg_color2\">
    <option value=\"$table_bg_color\" selected>$table_bg_color</option>
    <option value=\"#000000\">Black</option>
    <option value=\"#FFFFFF\">White</option>
    <option value=\"#008000\">Green</option>
    <option value=\"#800000\">Maroon</option>
    <option value=\"#808000\">Olive</option>
    <option value=\"#000080\">Navy</option>
    <option value=\"#800080\">Purple</option>
    <option value=\"#808080\">Gray</option>
    <option value=\"#FFFF00\">Yellow</option>
    <option value=\"#00FF00\">Lime</option>
    <option value=\"#00FFFF\">Aqua</option>
    <option value=\"#FF00FF\">Fuchsia</option>
    <option value=\"#C0C0C0\">Silver</option>
    <option value=\"#FF0000\">Red</option>
    <option value=\"#0000FF\">Blue</option>
    <option value=\"#008080\">Teal</option>
  </select> Or Custom Color Code: #<input type=text name=custom_color_code_bg size=5></td></tr>
<tr><td>Table Text Color:</td><td>
<select size=\"1\" name=\"table_text_color2\">
    <option value=\"$table_text_color\" selected>$table_text_color</option>
    <option value=\"#000000\">Black</option>
    <option value=\"#FFFFFF\">White</option>
    <option value=\"#008000\">Green</option>
    <option value=\"#800000\">Maroon</option>
    <option value=\"#808000\">Olive</option>
    <option value=\"#000080\">Navy</option>
    <option value=\"#800080\">Purple</option>
    <option value=\"#808080\">Gray</option>
    <option value=\"#FFFF00\">Yellow</option>
    <option value=\"#00FF00\">Lime</option>
    <option value=\"#00FFFF\">Aqua</option>
    <option value=\"#FF00FF\">Fuchsia</option>
    <option value=\"#C0C0C0\">Silver</option>
    <option value=\"#FF0000\">Red</option>
    <option value=\"#0000FF\">Blue</option>
    <option value=\"#008080\">Teal</option>
  </select> Or Custom Color Code: #<input type=text name=custom_color_code_text size=5></td></tr>
<tr><td>Image Upload Max Size:</td><td><input type=text name=maxsize2 value=\"$maxsize\" size=40></td></tr>
<tr><td>Image Path:</td><td><input type=text name=path2 value=\"$path\" size=40><br><font size=-1 color=blue>Hint: $DOCUMENT_ROOT/mlslister/img/</font></td><tr>
<tr><td>Image URL:</td><td><input type=text name=img_url2 value=\"$img_url\" size=40></td><tr>
</table></div>
<br><center><b>Image Size Configuration:</b></center>
<div align=center><table border=1>
<tr><td>Main Image Width:</td><td><input type=text name=image_size_1_2 value=\"$image_size_1\" size=20></td></tr>
<tr><td>Main Image Height:</td><td><input type=text name=image_size_2_2 value=\"$image_size_2\" size=20></td></tr>
<tr><td>My Image Width:</td><td><input type=text name=my_image_size_1_2 value=\"$my_image_1\" size=20></td></tr>
<tr><td>My Image Height:</td><td><input type=text name=my_image_size_2_2 value=\"$my_image_2\" size=20></td></tr>
<tr><td>Details Main Image Width:</td><td><input type=text name=details_main_image_1_2 value=\"$details_main_image_1\" size=20></td></tr>
<tr><td>Details Main Image Height:</td><td><input type=text name=details_main_image_2_2 value=\"$details_main_image_2\" size=20></td></tr>
<tr><td>Details Bottom Image 1 Width:</td><td><input type=text name=details_bottom_image_1a_2 value=\"$details_bottom_image_1a\" size=20></td></tr>
<tr><td>Details Bottom Image 1 Height:</td><td><input type=text name=details_bottom_image_2a_2 value=\"$details_bottom_image_2a\" size=20></td></tr>
<tr><td>Details Bottom Image 2 Width:</td><td><input type=text name=details_bottom_image_1b_2 value=\"$details_bottom_image_1b\" size=20></td></tr>
<tr><td>Details Bottom Image 2 Height:</td><td><input type=text name=details_bottom_image_2b_2 value=\"$details_bottom_image_2b\" size=20></td></tr>
<tr><td>Details Bottom Image 3 Width:</td><td><input type=text name=details_bottom_image_1c_2 value=\"$details_bottom_image_1c\" size=20></td></tr>
<tr><td>Details Bottom Image 3 Height:</td><td><input type=text name=details_bottom_image_2c_2 value=\"$details_bottom_image_2c\" size=20></td></tr>
<tr><td>Details Bottom Image 4 Width:</td><td><input type=text name=details_bottom_image_1d_2 value=\"$details_bottom_image_1d\" size=20></td></tr>
<tr><td>Details Bottom Image 4 Height:</td><td><input type=text name=details_bottom_image_2d_2 value=\"$details_bottom_image_2d\" size=20></td></tr>
<tr><td>Details Bottom Image 5 Width:</td><td><input type=text name=details_bottom_image_1e_2 value=\"$details_bottom_image_1e\" size=20></td></tr>
<tr><td>Details Bottom Image 5 Height:</td><td><input type=text name=details_bottom_image_2e_2 value=\"$details_bottom_image_2e\" size=20></td></tr>
<tr><td>Details Bottom Image 6 Width:</td><td><input type=text name=details_bottom_image_1f_2 value=\"$details_bottom_image_1f\" size=20></td></tr>
<tr><td>Details Bottom Image 6 Height:</td><td><input type=text name=details_bottom_image_2f_2 value=\"$details_bottom_image_2f\" size=20></td></tr>
<tr><td>Details Bottom Image 7 Width:</td><td><input type=text name=details_bottom_image_1g_2 value=\"$details_bottom_image_1g\" size=20></td></tr>
<tr><td>Details Bottom Image 7 Height:</td><td><input type=text name=details_bottom_image_2g_2 value=\"$details_bottom_image_2g\" size=20></td></tr>
<tr><td>Details Bottom Image 8 Width:</td><td><input type=text name=details_bottom_image_1h_2 value=\"$details_bottom_image_1h\" size=20></td></tr>
<tr><td>Details Bottom Image 8 Height:</td><td><input type=text name=details_bottom_image_2h_2 value=\"$details_bottom_image_2h\" size=20></td></tr>
<tr><td>Details Bottom Image 9 Width:</td><td><input type=text name=details_bottom_image_1i_2 value=\"$details_bottom_image_1i\" size=20></td></tr>
<tr><td>Details Bottom Image 9 Height:</td><td><input type=text name=details_bottom_image_2i_2 value=\"$details_bottom_image_2i\" size=20></td></tr>
</table></div>
<br><center><b>Payment Information:</b></center>
<div align=center><table border=1>
<tr><td>PayPal Email Address:</td><td><input type=text name=paypalid value=\"$paypal\" size=20></td></tr>
<tr><td>Price Per Listing:</td><td>\$ <input type=text name=price_per_listing2 value=\"$price_per_listing\" size=20></td></tr>
</table></div>

<br>
<center><b>Server PHP Version:</center></b>
<div align=center><table border=1>
<tr><td>PHP Version:</td><td>
<select size=\"1\" name=\"php_v_2\">
<option value=\"$php_v\" selected>$php_v</option>
<option value=\"4.2.2\">4.2.2</option>
<option value=\"4.2.3\">4.2.3</option>
</select><br>Hint: <a href=info.php target=_blank>PHP Information</a></td></tr>


</table></div>

<center><input type=submit value=\"Save Settings\"></center>
</form>\n";


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

include 'footer.inc';

?>
