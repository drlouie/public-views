<?php
require 'settings.php';
$found = 0;

	$linkID2 = @mysql_connect("$server", "$username", "$password");
	mysql_select_db("$database", $linkID2);

	$resultID2 = mysql_query("SELECT header,footer,main_template,detailed_template FROM `user_settings` WHERE 1 AND `uname` = '$id'", $linkID2);

	for ($x= 0; $x < mysql_num_rows($resultID2); $x++) {
		$row = mysql_fetch_assoc($resultID2);
		$temp_header = $row[header];
		$temp_footer = $row[footer];
		$temp_main_template = $row[main_template];
		$temp_detailed_template = $row[detailed_template];
	}

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
		if ($row[mls] == $mls) {
		if ($temp_detailed_template == "") {
			print "
<a href=\"javascript:history.back(1)\"><img alt=\"Back One Page\" src=\"back.gif\" border=\"0\" width=\"55\" height=\"19\"></a>
<a href=\"javascript:window.print()\"><img alt=\"Print This Page\" src=\"print.gif\" border=\"0\" width=\"60\" height=\"18\"></a>
<table cellSpacing=\"0\" cellPadding=\"10\" width=\"670\" border=\"0\">
  <tbody>
    <tr>
      <td><font face=\"Arial Black, Arial, sans-serif\" color=\"#999999\" size=\"-1\">Home
        Listings :</font><font face=\"Arial Black, Arial, sans-serif\" size=\"-1\"> <font color=\"#2b4fa2\">MLS#
        $row[mls]&nbsp; Title: $row[title]</font></font>&nbsp;&nbsp;<font color=red><b>$row[status]</b></font></td>
    </tr>
  </tbody>
</table>
<table cellSpacing=\"0\" cellPadding=\"0\" width=\"670\" border=\"0\">
  <tbody>
    <tr>
      <td vAlign=\"top\" width=\"400\">
        <table cellSpacing=\"0\" cellPadding=\"25\" width=\"400\" border=\"0\">
          <tbody>
            <tr>
              <td vAlign=\"top\">
                <div align=\"center\">
                  <table cellSpacing=\"0\" cellPadding=\"0\" width=\"350\" border=\"0\">
                    <tbody>
                      <tr>
                        <td align=\"middle\" width=\"50%\" bgColor=\"$table_bg_color\"><b><font color=$table_text_color><b>$row[property_city], $row[property_state], $row[property_zip]</b></font></b></td>
                        <td align=\"middle\" width=\"50%\" bgColor=\"$table_bg_color\"><b><font color=$table_text_color>\$$row[price]</font></b></td>
                      </tr>
                    </tbody>
                  </table>
                  <table cellSpacing=\"0\" cellPadding=\"10\" width=\"350\" border=\"0\">
                    <tbody>
                      <tr>
                        <td align=\"middle\"><img src=\"$img_url$id/$row[image1]\" width=\"$details_main_image_1\" height=\"$details_main_image_2\"></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                <table cellSpacing=\"0\" cellPadding=\"10\" width=\"350\" border=\"0\">
                  <tbody>
                    <tr>
                      <td>$row[detailed_description]</td>
                    </tr>
                  </tbody>
                </table>
                <table cellSpacing=\"0\" cellPadding=\"0\" width=\"350\" border=\"0\">
                  <tbody>
                    <tr>
                      <td><font face=\"Arial, Helvetica, sans-serif\"><b>
                        <p align=\"left\">Contact Us</b>:<br>
			<b>$row[realtor_name]<br></b>
			<b>$row[realtor_phone]<br></b>
			<b><a href=\"mailto:$row[realtor_email]?subject=MLS Number $row[mls]\">Tell me more about this listing</a></b>                        

			</font></p>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </td>
            </tr>
          </tbody>
        </table>
      </td>
      <td vAlign=\"top\" width=\"270\">
        <table cellSpacing=\"0\" cellPadding=\"10\" width=\"270\" border=\"0\">
          <tbody>
            <tr>
              <td vAlign=\"top\">
                <table cellSpacing=\"0\" cellPadding=\"0\" width=\"229\" border=\"0\">
                  <tbody>
                    <tr>
                      <td><img alt=\"Features\" src=\"features.gif\" width=\"229\" height=\"21\"></td>
                    </tr>
                    <tr>
                      <td vAlign=\"top\"><br>\n";

if ($row[feature1] != "") {
	print "<li>$row[feature1]</li>\n";
}
if ($row[feature2] != "") {
	print "<li>$row[feature2]</li>\n";
}
if ($row[feature3] != "") {
	print "<li>$row[feature3]</li>\n";
}
if ($row[feature4] != "") {
	print "<li>$row[feature4]</li>\n";
}
if ($row[feature5] != "") {
	print "<li>$row[feature5]</li>\n";
}
if ($row[feature6] != "") {
	print "<li>$row[feature6]</li>\n";
}
if ($row[feature7] != "") {
	print "<li>$row[feature7]</li>\n";
}
if ($row[feature8] != "") {
	print "<li>$row[feature8]</li>\n";
}
if ($row[feature9] != "") {
	print "<li>$row[feature9]</li>\n";
}
if ($row[feature10] != "") {
	print "<li>$row[feature10]</li>\n";
}
if ($row[feature11] != "") {
	print "<li>$row[feature11]</li>\n";
}
if ($row[feature12] != "") {
	print "<li>$row[feature12]</li>\n";
}
if ($row[feature13] != "") {
	print "<li>$row[feature13]</li>\n";
}
if ($row[feature14] != "") {
	print "<li>$row[feature14]</li>\n";
}
if ($row[feature15] != "") {
	print "<li>$row[feature15]</li>\n";
}
if ($row[feature16] != "") {
	print "<li>$row[feature16]</li>\n";
}
if ($row[feature17] != "") {
	print "<li>$row[feature17]</li>\n";
}
if ($row[feature18] != "") {
	print "<li>$row[feature18]</li>\n";
}
if ($row[feature19] != "") {
	print "<li>$row[feature19]</li>\n";
}
if ($row[feature20] != "") {
	print "<li>$row[feature20]</li>\n";
}
if ($row[feature21] != "") {
	print "<li>$row[feature21]</li>\n";
}
if ($row[feature22] != "") {
	print "<li>$row[feature22]</li>\n";
}
if ($row[feature23] != "") {
	print "<li>$row[feature23]</li>\n";
}
if ($row[feature24] != "") {
	print "<li>$row[feature24]</li>\n";
}
if ($row[feature25] != "") {
	print "<li>$row[feature25]</li>\n";
}
if ($row[feature26] != "") {
	print "<li>$row[feature26]</li>\n";
}
if ($row[feature27] != "") {
	print "<li>$row[feature27]</li>\n";
}
if ($row[feature28] != "") {
	print "<li>$row[feature28]</li>\n";
}
if ($row[feature29] != "") {
	print "<li>$row[feature29]</li>\n";
}
if ($row[feature30] != "") {
	print "<li>$row[feature30]</li>\n";
}
if ($row[feature31] != "") {
	print "<li>$row[feature31]</li>\n";
}
if ($row[feature32] != "") {
	print "<li>$row[feature32]</li>\n";
}
if ($row[feature33] != "") {
	print "<li>$row[feature33]</li>\n";
}
if ($row[feature34] != "") {
	print "<li>$row[feature34]</li>\n";
}
if ($row[feature35] != "") {
	print "<li>$row[feature35]</li>\n";
}
if ($row[feature36] != "") {
	print "<li>$row[feature36]</li>\n";
}
if ($row[feature37] != "") {
	print "<li>$row[feature37]</li>\n";
}
if ($row[feature38] != "") {
	print "<li>$row[feature38]</li>\n";
}
if ($row[feature39] != "") {
	print "<li>$row[feature39]</li>\n";
}
if ($row[feature40] != "") {
	print "<li>$row[feature40]</li>\n";
}


                        print "</td>
                    </tr>
                    <tr>
                      <td align=\"TOP\"><img src=\"featuresbottom.gif\" width=\"229\" height=\"21\"><br>
			<a href=\"#Images\"><font size=\"5\"><b>See More Pictures</b></font></a><br>\n";
if ($row[url] != "") {
	print "<a href=$row[url] target=\"_new\">More Details</a><br>\n";
}
if ($row[virtual_tour] != "") {
	print "<a href=$row[virtual_tour] target=\"_new\">Virtual Tour</a><br>\n";
}
if ($row[map] != "") {
	print "<a href=$row[map] target=\"_new\">Map</a><br>\n";
}

                      print "</td>
                    </tr>
                  </tbody>
                </table>
              </td>
            </tr>
          </tbody>
        </table>
      </td>
    </tr>
  </tbody>
</table>
\n";
print "<p><a name=\"Images\"><b>More Pictures:</b></a></p>\n";
if ($row[image2] != "") {
	print "<img src=\"$img_url$id/$row[image2]\" width=\"$details_bottom_image_1a\" height=\"$details_bottom_image_2a\">\n";
}
if ($row[image3] != "") {
	print "<img src=\"$img_url$id/$row[image3]\"  width=\"$details_bottom_image_1b\" height=\"$details_bottom_image_2b\">\n";
}
if ($row[image4] != "") {
	print "<img src=\"$img_url$id/$row[image4]\"  width=\"$details_bottom_image_1c\" height=\"$details_bottom_image_2c\"><br>\n";
}
if ($row[image5] != "") {
	print "<img src=\"$img_url$id/$row[image5]\"  width=\"$details_bottom_image_1d\" height=\"$details_bottom_image_2d\">\n";
}
if ($row[image6] != "") {
	print "<img src=\"$img_url$id/$row[image6]\"  width=\"$details_bottom_image_1e\" height=\"$details_bottom_image_2e\">\n";
}
if ($row[image7] != "") {
	print "<img src=\"$img_url$id/$row[image7]\"  width=\"$details_bottom_image_1f\" height=\"$details_bottom_image_2f\"><br>\n";
}
if ($row[image8] != "") {
	print "<img src=\"$img_url$id/$row[image8]\"  width=\"$details_bottom_image_1g\" height=\"$details_bottom_image_2g\">\n";
}
if ($row[image9] != "") {
	print "<img src=\"$img_url$id/$row[image9]\"  width=\"$details_bottom_image_1h\" height=\"$details_bottom_image_2h\">\n";
}
if ($row[image10] != "") {
	print "<img src=\"$img_url$id/$row[image10]\"  width=\"$details_bottom_image_1i\" height=\"$details_bottom_image_2i\">\n";
}
print "<br>\n";


		} else {
			// Display main template
			$found = 1;


			if ($row[image1] == "") {
				$image1 = "../../blank.jpg";
			} else {
				$image1 = $row[image1];
			}
			if ($row[image2] == "") {
				$image2 = "../../blank.jpg";
			} else {
				$image2 = $row[image2];
			}
			if ($row[image3] == "") {
				$image3 = "../../blank.jpg";
			} else {
				$image3 = $row[image3];
			}
			if ($row[image4] == "") {
				$image4 = "../../blank.jpg";
			} else {
				$image4 = $row[image4];
			}
			if ($row[image5] == "") {
				$image5 = "../../blank.jpg";
			} else {
				$image5 = $row[image5];
			}
			if ($row[image6] == "") {
				$image6 = "../../blank.jpg";
			} else {
				$image6 = $row[image6];
			}
			if ($row[image7] == "") {
				$image7 = "../../blank.jpg";
			} else {
				$image7 = $row[image7];
			}
			if ($row[image8] == "") {
				$image8 = "../../blank.jpg";
			} else {
				$image8 = $row[image8];
			}
			if ($row[image9] == "") {
				$image9 = "../../blank.jpg";
			} else {
				$image9 = $row[image9];
			}
			if ($row[image10] == "") {
				$image10 = "../../blank.jpg";
			} else {
				$image10 = $row[image10];
			}


			if ($row[myimage] == "") {
				$myimage = "../../blank.jpg";
			} else {
				$myimage = $row[myimage];
			}
			$user_img_path = "$img_url$id/";
			$detailed_url = "$site_url/details.php?mls=$row[mls]&id=$id";


			$temp_detailed_template = str_replace("#mls#", "$row[mls]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#realtor_name#", "$row[realtor_name]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#realtor_phone#", "$row[realtor_phone]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#realtor_email#", "$row[realtor_email]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#title#", "$row[title]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#short_description#", "$row[short_description]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#detailed_description#", "$row[detailed_description]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#price#", "$row[price]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#status#", "$row[status]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#bedrooms#", "$row[bedrooms]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#baths#", "$row[baths]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#half_baths#", "$row[half_baths]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#sqf#", "$row[sqf]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#acres#", "$row[acres]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#house_type#", "$row[house_type]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#image1#", "$image1", $temp_detailed_template);
			$temp_detailed_template = str_replace("#image2#", "$image2", $temp_detailed_template);
			$temp_detailed_template = str_replace("#image3#", "$image3", $temp_detailed_template);
			$temp_detailed_template = str_replace("#image4#", "$image4", $temp_detailed_template);
			$temp_detailed_template = str_replace("#image5#", "$image5", $temp_detailed_template);
			$temp_detailed_template = str_replace("#image6#", "$image6", $temp_detailed_template);
			$temp_detailed_template = str_replace("#image7#", "$image7", $temp_detailed_template);
			$temp_detailed_template = str_replace("#image8#", "$image8", $temp_detailed_template);
			$temp_detailed_template = str_replace("#image9#", "$image9", $temp_detailed_template);
			$temp_detailed_template = str_replace("#image10#", "$image10", $temp_detailed_template);
			$temp_detailed_template = str_replace("#url#", "$row[url]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#virtual_tour#", "$row[virtual_tour]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#map#", "$row[map]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#property_address#", "$row[property_address]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#property_city#", "$row[property_city]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#property_state#", "$row[property_state]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#property_zip#", "$row[property_zip]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#property_county#", "$row[property_county]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#property_school_zone#", "$row[property_school_zone]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature1#", "$row[feature1]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature2#", "$row[feature2]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature3#", "$row[feature3]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature4#", "$row[feature4]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature5#", "$row[feature5]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature6#", "$row[feature6]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature7#", "$row[feature7]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature8#", "$row[feature8]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature9#", "$row[feature9]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature10#", "$row[feature10]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature11#", "$row[feature11]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature12#", "$row[feature12]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature13#", "$row[feature13]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature14#", "$row[feature14]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature15#", "$row[feature15]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature16#", "$row[feature16]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature17#", "$row[feature17]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature18#", "$row[feature18]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature19#", "$row[feature19]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature20#", "$row[feature20]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature21#", "$row[feature21]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature22#", "$row[feature22]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature23#", "$row[feature23]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature24#", "$row[feature24]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature25#", "$row[feature25]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature26#", "$row[feature26]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature27#", "$row[feature27]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature28#", "$row[feature28]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature29#", "$row[feature29]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature30#", "$row[feature30]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature31#", "$row[feature31]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature32#", "$row[feature32]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature33#", "$row[feature33]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature34#", "$row[feature34]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature35#", "$row[feature35]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature36#", "$row[feature36]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature37#", "$row[feature37]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature38#", "$row[feature38]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature39#", "$row[feature39]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#feature40#", "$row[feature40]", $temp_detailed_template);
			$temp_detailed_template = str_replace("#user_img_path#", "$user_img_path", $temp_detailed_template);

			print "$temp_detailed_template\n";

		}
		}
	}




?>
