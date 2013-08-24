<?php
require 'settings.php';
include 'header.inc';

if ($mls_pass == $admin_password) {

	$linkID = @mysql_connect("$server", "$username", "$password");
	mysql_select_db("$database", $linkID);

	$resultID = mysql_query("SELECT mls, realtor_name ,realtor_phone ,realtor_email ,title ,short_description ,detailed_description ,price ,status ,bedrooms ,baths ,half_baths ,sqf ,acres ,house_type ,image1 ,image2 ,image3 ,image4 ,image5 ,image6 ,image7 ,image8 ,image9 ,image10 ,url ,virtual_tour ,map ,property_address ,property_city ,property_state ,property_zip ,property_county ,property_school_zone , feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9, feature10, feature11, feature12, feature13, feature14, feature15, feature16,feature17,feature18,feature19,feature20,feature21,feature22,feature23,feature24,feature25,feature26,feature27,feature28,feature29,feature30,feature31,feature32,feature33,feature34,feature35,feature36,feature37,feature38,feature39,feature40 FROM mls", $linkID);

	for ($x= 0; $x < mysql_num_rows($resultID); $x++) {
		$row = mysql_fetch_assoc($resultID);
		if ($row[mls] == $mls) {
			print "
<p align=\"center\"><b>Edit Listing<br>
<form action=admin_edit3.php method=post>
<div align=\"center\">
  <center>
  <table border=\"1\" width=\"690\" height=\"1523\" bgcolor=\"$table_bg_color\"><font color=\"$table_text_color\">
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">MLS Number:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">$row[mls]<input type=hidden name=mls value=\"$row[mls]\"></font></td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">Realtor Name:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=realtor_name value=\"$row[realtor_name]\" size=20>
  </font>
        
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">Realtor Phone:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=realtor_phone value=\"$row[realtor_phone]\" size=20>
  </font>
        
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">Realtor Email:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=realtor_email value=\"$row[realtor_email]\" size=20>
  </font>
        
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"19\" colspan=\"2\">&nbsp;</td>
      <td width=\"350\" height=\"19\" colspan=\"2\">&nbsp;</td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">Title of Listing:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=title value=\"$row[title]\" size=20>
  </font>
        
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">Short Description:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=short_description value=\"$row[short_description]\" size=20>
  </font>
        
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"16\" colspan=\"2\"><font color=\"$table_text_color\">Detailed Description: (HTML OK)</font></td>
      <td width=\"350\" height=\"16\" colspan=\"2\"><textarea rows=\"5\" name=\"detailed_description\" cols=\"39\">$row[detailed_description]</textarea>
        </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">Listing Price:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">$ <input type=text name=price value=\"$row[price]\" size=20>
  </font>
        
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"19\" colspan=\"2\">&nbsp;</td>
      <td width=\"350\" height=\"19\" colspan=\"2\">&nbsp;</td>
    </tr>
    <tr>
      <td width=\"324\" height=\"19\" colspan=\"2\"><font color=\"$table_text_color\">Number of Bedrooms:</font></td>
      <td width=\"350\" height=\"19\" colspan=\"2\"><select size=\"1\" name=\"bedrooms\">
	  <option selected>$row[bedrooms]</option>
          <option>1</option>
          <option>2</option>
          <option>3</option>
          <option>4</option>
          <option>5</option>
          <option>6</option>
          <option>7</option>
          <option>8</option>
          <option>9</option>
          <option>10</option>
        </select> </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"19\" colspan=\"2\"><font color=\"$table_text_color\">Number of Baths:</font></td>
      <td width=\"350\" height=\"19\" colspan=\"2\"><select size=\"1\" name=\"baths\">
	  <option selected>$row[baths]</option>
          <option>1</option>
          <option>2</option>
          <option>3</option>
          <option>4</option>
          <option>5</option>
          <option>6</option>
          <option>7</option>
          <option>8</option>
          <option>9</option>
          <option>10</option>
        </select> </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"19\" colspan=\"2\"><font color=\"$table_text_color\">Number of Half-Baths:</font></td>
      <td width=\"350\" height=\"19\" colspan=\"2\"><select size=\"1\" name=\"half_baths\">
          <option selected>$row[half_baths]</option>
          <option>0</option>
          <option>1</option>
          <option>2</option>
          <option>3</option>
          <option>4</option>
          <option>5</option>
          <option>6</option>
          <option>7</option>
          <option>8</option>
          <option>9</option>
          <option>10</option>
        </select></td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">Total Square Feet:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=sqf value=\"$row[sqf]\" size=20>
  </font>
        
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">Total Acres:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=acres value=\"$row[acres]\" size=20>
  </font>
        
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">Listing Type (IE: Ranch, Townhome,
        etc.)</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=house_type value=\"$row[house_type]\" size=20>
  </font>
        
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"6\" colspan=\"2\">&nbsp;</td>
      <td width=\"350\" height=\"6\" colspan=\"2\">&nbsp;</td>
    </tr>
    <tr>
      <td width=\"674\" height=\"7\" colspan=\"4\"><b>Example : Image Name:
        logo.gif</b></td>
    </tr>
    <tr>
      <td width=\"324\" height=\"10\" colspan=\"2\">&nbsp;</td>
      <td width=\"350\" height=\"10\" colspan=\"2\">&nbsp;</td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Image 1</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=image1 value=\"$row[image1]\" size=20>
  </font>
        
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Image 6</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=image6 value=\"$row[image6]\" size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Image 2</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=image2 value=\"$row[image2]\" size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Image 7</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=image7 value=\"$row[image7]\" size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Image 3</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=image3 value=\"$row[image3]\" size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Image 8</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=image8 value=\"$row[image8]\" size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Image 4</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=image4 value=\"$row[image4]\" size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Image 9</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=image9 value=\"$row[image9]\" size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Image 5</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=image5 value=\"$row[image5]\" size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Image 10</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=image10 value=\"$row[image10]\" size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"19\" colspan=\"2\">&nbsp;</td>
      <td width=\"350\" height=\"19\" colspan=\"2\">&nbsp;</td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">URL to more detailed page:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=url value=\"$row[url]\" size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">URL to Virtual Tour:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=virtual_tour value=\"$row[virtual_tour]\" size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">URL to property map:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=map value=\"$row[url]\" size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"19\" colspan=\"2\">&nbsp;</td>
      <td width=\"350\" height=\"19\" colspan=\"2\">&nbsp;</td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">Property Address:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=property_address value=\"$row[property_address]\" size=20>
  </font>
        
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">Property City:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=property_city value=\"$row[property_city]\" size=20>
  </font>
        
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">Property State:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=property_state value=\"$row[property_state]\" size=20>
  </font>
        
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">Property County:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=property_county value=\"$row[property_county]\" size=20>
  </font>
        
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">Property Zip Code:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=property_zip value=\"$row[property_zip]\" size=20>
  </font>
        
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">Property School Zone:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=property_school_zone value=\"$row[property_school_zone]\" size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"19\" colspan=\"2\">&nbsp;</td>
      <td width=\"350\" height=\"19\" colspan=\"2\">&nbsp;</td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 1</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=feature1 value=\"$row[feature1]\" size=20>
  </font>
        
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 21</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=feature21 value=\"$row[feature21]\" size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 2</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=feature2 value=\"$row[feature2]\" size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 22</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=feature22 value=\"$row[feature22]\" size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 3</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=feature3 value=\"$row[feature3]\" size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 23</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=feature23 value=\"$row[feature23]\" size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 4</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=feature4 value=\"$row[feature4]\" size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 24</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=feature24 value=\"$row[feature24]\" size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 5</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=feature5 value=\"$row[feature5]\" size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 25</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=feature25 value=\"$row[feature25]\" size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 6</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=feature6 value=\"$row[feature6]\" size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 26</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=feature26 value=\"$row[feature26]\" size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 7</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=feature7 value=\"$row[feature7]\" size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 27</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=feature27 value=\"$row[feature27]\" size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 8</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=feature8 value=\"$row[feature8]\" size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 28</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=feature28 value=\"$row[feature28]\" size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 9</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=feature9 value=\"$row[feature9]\" size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 29</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=feature29 value=\"$row[feature29]\" size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 10</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=feature10 value=\"$row[feature10]\" size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 30</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=feature30 value=\"$row[feature30]\" size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 11</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=feature11 value=\"$row[feature11]\" size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 31</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=feature31 value=\"$row[feature31]\" size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 12</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=feature12 value=\"$row[feature12]\" size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 32</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=feature32 value=\"$row[feature32]\" size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 13</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=feature13 value=\"$row[feature13]\" size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 33</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=feature33 value=\"$row[feature33]\" size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 14</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=feature14 value=\"$row[feature14]\" size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 34</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=feature34 value=\"$row[feature34]\" size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 15</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=feature15 value=\"$row[feature15]\" size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 35</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=feature35 value=\"$row[feature35]\" size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 16</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=feature16 value=\"$row[feature16]\" size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 36</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=feature36 value=\"$row[feature36]\" size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 17</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=feature17 value=\"$row[feature17]\" size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 37</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=feature37 value=\"$row[feature37]\" size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 18</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=feature18 value=\"$row[feature18]\" size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 38</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=feature38 value=\"$row[feature38]\" size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 19</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=feature19 value=\"$row[feature19]\" size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 39</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=feature39 value=\"$row[feature39]\" size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 20</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=feature20 value=\"$row[feature20]\" size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 40</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=feature40 value=\"$row[feature40]\" size=20>
  </font>
      </td>
    </tr>
  </table></font>
  </center>
</div>
<center><input type=submit value=\"Save Changes\"></center>
</form>
\n";
	}
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

?>
