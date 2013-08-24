<?php
require 'settings.php';

	$linkID2 = @mysql_connect("$server", "$username", "$password");
	mysql_select_db("$database", $linkID2);

	$resultID2 = mysql_query("SELECT header,footer,main_template,detailed_template FROM`user_settings` WHERE 1 AND `uname` = '$id'", $linkID2);

	for ($x= 0; $x < mysql_num_rows($resultID2); $x++) {
		$row = mysql_fetch_assoc($resultID2);
		$temp_header = $row[header];
		$temp_footer = $row[footer];
		$temp_main_template = $row[main_template];
		$temp_detailed_template = $row[detailed_template];
	}

if ($temp_header == "" ) {
	include 'header.inc';
} else {
	echo "$temp_header\n";
}
$found = 0;

if ($mls_pass == $admin_password) {
	print "[<a href=admin.php>Administration Login</a>]<br>Note: Only the site admin can see this message.<br><br>\n";
}

if ($id == "") {

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

	$resultID = mysql_query("SELECT mls, title, short_description, price, status, bedrooms, baths, half_baths, sqf, acres, house_type, image1, property_city, property_state, property_zip, myimage FROM user_mls", $linkID);
	


	for ($x= 0; $x < mysql_num_rows($resultID); $x++) {
		$count = $count + 1;
	}

		if ($start < 5) {
			// 
		} else {
			$prev = $start - 5;
			$y = 5;
			print "[<a href=index.php?start=$prev&stop=$y>Previous Page</a>] \n";
		}

		$next = $start + 5;
		if ($next > $count) {
			//
		} else {

			$y = 5;
			print "[<a href=index.php?start=$next&stop=$y>Next Page</a>]\n";
		}
		print "</center>\n";

//--------------------------------------------------------------------------//
print "<div align=\"center\"><center><table border=\"0\" width=\"866\" height=\"215\">\n";

	$linkID = @mysql_connect("$server", "$username", "$password");
	mysql_select_db("$database", $linkID);

	$resultID = mysql_query("SELECT mls, realtor_user_name, title, short_description, price, status, bedrooms, baths, half_baths, sqf, acres, house_type, image1, property_city, property_state, property_zip, myimage FROM user_mls LIMIT $start, $stop", $linkID);

	for ($x= 0; $x < mysql_num_rows($resultID); $x++) {
		$row = mysql_fetch_assoc($resultID);
		print "
    			<tr>
		        <td width=\"131\" height=\"33\" bgcolor=\"$table_bg_color\"><font color=\"$table_text_color\">Price:<br>\$$row[price]</font></td>
      		        <td width=\"137\" height=\"33\" bgcolor=\"$table_bg_color\"><font color=\"$table_text_color\">BR:<br>$row[bedrooms]</font></td>
			<td width=\"119\" height=\"33\" bgcolor=\"$table_bg_color\"><font color=\"$table_text_color\">Baths:<br>$row[baths]</font></td>
			<td width=\"156\" height=\"33\" bgcolor=\"$table_bg_color\"><font color=\"$table_text_color\">Sq. Ft.<br>$row[sqf]</font></td>
			<td width=\"287\" height=\"33\" bgcolor=\"$table_bg_color\"><font color=\"$table_text_color\">Listing Type:<br>$row[house_type]</font></td>
			</tr>
			<tr>
			<td width=\"403\" height=\"129\" colspan=\"3\"><img src=\"$img_url$row[realtor_user_name]/$row[image1]\" width=\"$image_size_1\" height=\"$image_size_2\">&nbsp&nbsp&nbsp\n";
if ($row[myimage] != "") {
	print "<img src=\"$img_url$row[realtor_user_name]/$row[myimage]\" width=\"$my_image_1\" height=\"$my_image_2\">\n";
}
			print "</td>
			<td width=\"447\" height=\"129\" colspan=\"2\" valign=\"top\"><u>Short Description:</u>
			<p>$row[short_description]</p><p><br>
			<a href=\"details.php?mls=$row[mls]\">View Details:</a></td>
			</tr><tr>
			<td width=\"402\" height=\"39\" colspan=\"3\" bgcolor=\"$table_bg_color\"><font color=\"$table_text_color\">MLS Number: $row[mls] </font><font color=red><b>$row[status]</b></font></td>
			<td width=\"448\" height=\"39\" colspan=\"2\" bgcolor=\"$table_bg_color\"><font color=\"$table_text_color\">$row[property_city], $row[property_state], $row[property_zip]</font></td>
			</tr><tr><td><br></td></tr>\n";
		$found = 1;
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

	$resultID = mysql_query("SELECT mls, title, short_description, price, status, bedrooms, baths, half_baths, sqf, acres, house_type, image1, property_city, property_state, property_zip, myimage FROM user_mls", $linkID);
	


	for ($x= 0; $x < mysql_num_rows($resultID); $x++) {
		$count = $count + 1;
	}

		if ($start < 5) {
			// 
		} else {
			$prev = $start - 5;
			$y = 5;
			print "[<a href=index.php?start=$prev&stop=$y>Previous Page</a>] \n";
		}

		$next = $start + 5;
		if ($next > $count) {
			//
		} else {

			$y = 5;
			print "[<a href=index.php?start=$next&stop=$y>Next Page</a>]\n";
		}
		print "</center>\n";

//--------------------------------------------------------------------------//

} else {
	include 'display_users_listings.php';
}

print "<br><center>© <a href=http://www.turnkeyhosting.net>Turnkey Hosting</a></center><br>\n";
if ($temp_footer == "" ) {
	include 'footer.inc';
} else {
	print "$temp_footer\n";
}

?>
