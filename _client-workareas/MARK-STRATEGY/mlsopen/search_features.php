<?php
require 'settings.php';
include 'header.inc';
$found = 0;

print "<div align=\"center\"><center><table border=\"0\" width=\"866\" height=\"215\">\n";

$linkID = @mysql_connect("$server", "$username", "$password");
	mysql_select_db("$database", $linkID);

	$resultID = mysql_query("SELECT mls,realtor_user_name,realtor_name,realtor_phone,realtor_email,title,short_description,detailed_description,price,status,bedrooms,
baths,half_baths,sqf,acres,house_type,image1,image2,image3,image4,image5,image6,image7,image8,image9,image10,
url,virtual_tour,map,property_address,property_city,property_state,property_zip,property_county,property_school_zone,
feature1,feature2,feature3,feature4,feature5,feature6,feature7,feature8,feature9,feature10,feature11,feature12,
feature13,feature14,feature15,feature16,feature17,feature18,feature19,feature20,feature21,feature22,feature23,
feature24,feature25,feature26,feature27,feature28,feature29,feature30,feature31,feature32,feature33,feature34,
feature35,feature36,feature37,feature38,feature39,feature40 FROM user_mls", $linkID);

	for ($x= 0; $x < mysql_num_rows($resultID); $x++) {
		$row = mysql_fetch_assoc($resultID);

		if ((preg_match ("/$features/i", "$row[feature1]")) or (preg_match ("/$features/i", "$row[feature2]")) or (preg_match ("/$features/i", "$row[feature3]")) or (preg_match ("/$features/i", "$row[feature4]")) or (preg_match ("/$features/i", "$row[feature5]")) or (preg_match ("/$features/i", "$row[feature6]")) or (preg_match ("/$features/i", "$row[feature7]")) or (preg_match ("/$features/i", "$row[feature8]")) or (preg_match ("/$features/i", "$row[feature9]")) or (preg_match ("/$features/i", "$row[feature10]")) or (preg_match ("/$features/i", "$row[feature11]")) or (preg_match ("/$features/i", "$row[feature12]")) or (preg_match ("/$features/i", "$row[feature13]")) or (preg_match ("/$features/i", "$row[feature14]")) or (preg_match ("/$features/i", "$row[feature15]")) or (preg_match ("/$features/i", "$row[feature16]")) or (preg_match ("/$features/i", "$row[feature17]")) or (preg_match ("/$features/i", "$row[feature18]")) or (preg_match ("/$features/i", "$row[feature19]")) or 
(preg_match ("/$features/i", "$row[feature20]")) or (preg_match ("/$features/i", "$row[feature21]")) or (preg_match ("/$features/i", "$row[feature22]")) or (preg_match ("/$features/i", "$row[feature23]")) or (preg_match ("/$features/i", "$row[feature24]")) or (preg_match ("/$features/i", "$row[feature25]")) or (preg_match ("/$features/i", "$row[feature26]")) or (preg_match ("/$features/i", "$row[feature27]")) or (preg_match ("/$features/i", "$row[feature28]")) or (preg_match ("/$features/i", "$row[feature29]")) or (preg_match ("/$features/i", "$row[feature30]")) or (preg_match ("/$features/i", "$row[feature31]")) or (preg_match ("/$features/i", "$row[feature32]")) or (preg_match ("/$features/i", "$row[feature33]")) or (preg_match ("/$features/i", "$row[feature34]")) or (preg_match ("/$features/i", "$row[feature35]")) or (preg_match ("/$features/i", "$row[feature36]")) or (preg_match ("/$features/i", "$row[feature37]")) or (preg_match ("/$features/i", "$row[feature38]")) or 
(preg_match ("/$features/i", "$row[feature39]")) or (preg_match ("/$features/i", "$row[feature40]"))) {


			print "
    			<tr>
		        <td width=\"131\" height=\"33\" bgcolor=\"$table_bg_color\"><font color=\"$table_text_color\">Price:<br>\$$row[price]</font></td>
      		        <td width=\"137\" height=\"33\" bgcolor=\"$table_bg_color\"><font color=\"$table_text_color\">BR:<br>$row[bedrooms]</font></td>
			<td width=\"119\" height=\"33\" bgcolor=\"$table_bg_color\"><font color=\"$table_text_color\">Baths:<br>$row[baths]</font></td>
			<td width=\"156\" height=\"33\" bgcolor=\"$table_bg_color\"><font color=\"$table_text_color\">Sq. Ft.<br>$row[sqf]</font></td>
			<td width=\"287\" height=\"33\" bgcolor=\"$table_bg_color\"><font color=\"$table_text_color\">Listing Type:<br>$row[house_type]</font></td>
			</tr>
			<tr>
			<td width=\"403\" height=\"129\" colspan=\"3\"><img src=\"$img_url$row[realtor_user_name]/$row[image1]\" width=\"$image_size_1\" height=\"$image_size_2\"></td>
			<td width=\"447\" height=\"129\" colspan=\"2\" valign=\"top\"><u>Short Description:</u>
			<p>$row[short_description]</p><p><br>
			<a href=\"details.php?mls=$row[mls]\">View Details:</a></td>
			</tr><tr>
			<td width=\"402\" height=\"39\" colspan=\"3\" bgcolor=\"$table_bg_color\"><font color=\"$table_text_color\">MLS Number: $row[mls] </font><font color=red><b>$row[status]</b></font></td>
			<td width=\"448\" height=\"39\" colspan=\"2\" bgcolor=\"$table_bg_color\"><font color=\"$table_text_color\">$row[property_city], $row[property_state], $row[property_zip]</font></td>
			</tr><tr><td><br></td></tr>\n";
			$found = 1;

		}
	}
	
	print "</table></center></div>\n";
	
	if ($found == 0) {
		print "<br><br><b><center>There are no items to display.<br></b><br></center>\n";
		include 'footer.inc';
		die;
	}




include 'footer.inc';
?>
