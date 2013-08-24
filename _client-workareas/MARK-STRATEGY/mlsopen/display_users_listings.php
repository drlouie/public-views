<?php

//-----------------Display Previous and Next Page------------------------------------------------//
	if ($start == "") {
		$start = 0;
	}
	if ($stop == "") {
		$stop = 5;
	}
	print "<center>\n";
	$count = 0;
	$z = 0;
	$y = 0;
	$page = 0;
	$linkID = @mysql_connect("$server", "$username", "$password");
	mysql_select_db("$database", $linkID);

	$resultID = mysql_query("SELECT mls, realtor_user_name, title, short_description, price, status, bedrooms, baths, half_baths, sqf, acres, house_type, image1, property_city, property_state, property_zip, myimage FROM user_mls WHERE 1 AND `realtor_user_name` = '$id' ", $linkID);
	


	for ($x= 0; $x < mysql_num_rows($resultID); $x++) {
		$count = $count + 1;
	}

		if ($start < 5) {
			// 
		} else {
			$prev = $start - 5;
			$y = 5;
			print "[<a href=index.php?id=$id&start=$prev&stop=$y>Previous Page</a>] \n";
		}

		$next = $start + 5;
		if ($next > $count) {
			//
		} else {

			$y = 5;
			print "[<a href=index.php?id=$id&start=$next&stop=$y>Next Page</a>]\n";
		}
		print "</center>\n";

//--------------------------------------------------------------------------//
print "<div align=\"center\"><center><table border=\"0\" width=\"866\" height=\"215\">\n";

	$linkID = @mysql_connect("$server", "$username", "$password");
	mysql_select_db("$database", $linkID);

	$resultID = mysql_query("SELECT mls, realtor_user_name, title, short_description, price, status, bedrooms, baths, half_baths, sqf, acres, house_type, image1, property_city, property_state, property_zip, myimage FROM user_mls WHERE 1 AND `realtor_user_name` = '$id'  LIMIT $start, $stop", $linkID);

	for ($x= 0; $x < mysql_num_rows($resultID); $x++) {
		$row = mysql_fetch_assoc($resultID);


		if ($temp_main_template == "") {

			print "
    			<tr>
		        <td width=\"131\" height=\"33\" bgcolor=\"$table_bg_color\"><font color=\"$table_text_color\">Price:<br>\$$row[price]</font></td>
      		        <td width=\"137\" height=\"33\" bgcolor=\"$table_bg_color\"><font color=\"$table_text_color\">BR:<br>$row[bedrooms]</font></td>
			<td width=\"119\" height=\"33\" bgcolor=\"$table_bg_color\"><font color=\"$table_text_color\">Baths:<br>$row[baths]</font></td>
			<td width=\"156\" height=\"33\" bgcolor=\"$table_bg_color\"><font color=\"$table_text_color\">Sq. Ft.<br>$row[sqf]</font></td>
			<td width=\"287\" height=\"33\" bgcolor=\"$table_bg_color\"><font color=\"$table_text_color\">Listing Type:<br>$row[house_type]</font></td>
			</tr>
			<tr>
			<td width=\"403\" height=\"129\" colspan=\"3\"><img src=\"$img_url$id/$row[image1]\" width=\"$image_size_1\" height=\"$image_size_2\">&nbsp&nbsp&nbsp\n";
			if ($row[myimage] != "") {
				print "<img src=\"$img_url$id/$row[myimage]\" width=\"$my_image_1\" height=\"$my_image_2\">\n";
			}
			print "</td>
			<td width=\"447\" height=\"129\" colspan=\"2\" valign=\"top\"><u>Short Description:</u>
			<p>$row[short_description]</p><p><br>
			<a href=\"details.php?mls=$row[mls]&id=$id\">View Details:</a></td>
			</tr><tr>
			<td width=\"402\" height=\"39\" colspan=\"3\" bgcolor=\"$table_bg_color\"><font color=\"$table_text_color\">MLS Number: $row[mls] </font><font color=red><b>$row[status]</b></font></td>
			<td width=\"448\" height=\"39\" colspan=\"2\" bgcolor=\"$table_bg_color\"><font color=\"$table_text_color\">$row[property_city], $row[property_state], $row[property_zip]</font></td>
			</tr><tr><td><br></td></tr>\n";
			$found = 1;
		} else {
			// Display main template
			$found = 1;
			$mls = $row[mls];
			$title = $row[title];
			$short_description = $row[short_description];
			$status = $row[status];
			$bedrooms = $row[bedrooms];
			$baths = $row[baths];
			$half_baths = $row[half_baths];
			$sqf = $row[sqf];
			$acres = $row[acres];
			$house_type = $row[house_type];
			$image1 = $row[image1];
			$property_city = $row[property_city];
			$property_state = $row[property_state];
			$property_zip = $row[property_zip];
			if ($row[myimage] == "") {
				$myimage = "../../blank.jpg";
			} else {
				$myimage = $row[myimage];
			}
			$user_img_path = "$img_url$id/";
			$detailed_url = "$site_url/details.php?mls=$row[mls]&id=$id";


			$temp_main_template = str_replace("#mls#", "$mls", $temp_main_template);
			$temp_main_template = str_replace("#title#", "$title", $temp_main_template);
			$temp_main_template = str_replace("#short_description#", "$short_description", $temp_main_template);
			$temp_main_template = str_replace("#price#", "$row[price]", $temp_main_template);
			$temp_main_template = str_replace("#status#", "$status", $temp_main_template);
			$temp_main_template = str_replace("#bedrooms#", "$bedrooms", $temp_main_template);
			$temp_main_template = str_replace("#baths#", "$baths", $temp_main_template);
			$temp_main_template = str_replace("#half_baths#", "$half_baths", $temp_main_template);
			$temp_main_template = str_replace("#sqf#", "$sqf", $temp_main_template);
			$temp_main_template = str_replace("#acres#", "$acres", $temp_main_template);
			$temp_main_template = str_replace("#house_type#", "$house_type", $temp_main_template);
			$temp_main_template = str_replace("#image1#", "$image1", $temp_main_template);
			$temp_main_template = str_replace("#property_city#", "$property_city", $temp_main_template);
			$temp_main_template = str_replace("#property_state#", "$property_state", $temp_main_template);
			$temp_main_template = str_replace("#property_zip#", "$property_zip", $temp_main_template);
			$temp_main_template = str_replace("#myimage#", "$myimage", $temp_main_template);
			$temp_main_template = str_replace("#user_img_path#", "$user_img_path", $temp_main_template);
			$temp_main_template = str_replace("#detailed_url#", "$detailed_url", $temp_main_template);
			print "<tr>$temp_main_template</tr>\n";

		}
			
	}
	
	print "</table></center></div>\n";
	
	if ($found == 0) {
		print "<br><br><b><center>There are no items to display.<br></b><br></center>\n";
if ($temp_footer == "" ) {
	include 'footer.inc';
} else {
	print "$temp_footer\n";
}
		die;
	}


//-----------------Display Previous and Next Page------------------------------------------------//
	if ($start == "") {
		$start = 0;
	}
	if ($stop == "") {
		$stop = 5;
	}
	print "<center>\n";
	$count = 0;
	$z = 0;
	$y = 0;
	$page = 0;
	$linkID = @mysql_connect("$server", "$username", "$password");
	mysql_select_db("$database", $linkID);

	$resultID = mysql_query("SELECT mls, realtor_user_name, title, short_description, price, status, bedrooms, baths, half_baths, sqf, acres, house_type, image1, property_city, property_state, property_zip, myimage FROM user_mls WHERE 1 AND `realtor_user_name` = '$id' ", $linkID);
	


	for ($x= 0; $x < mysql_num_rows($resultID); $x++) {
		$count = $count + 1;
	}

		if ($start < 5) {
			// 
		} else {
			$prev = $start - 5;
			$y = 5;
			print "[<a href=index.php?id=$id&start=$prev&stop=$y>Previous Page</a>] \n";
		}

		$next = $start + 5;
		if ($next > $count) {
			//
		} else {

			$y = 5;
			print "[<a href=index.php?id=$id&start=$next&stop=$y>Next Page</a>]\n";
		}
		print "</center>\n";

//--------------------------------------------------------------------------//

?>:q