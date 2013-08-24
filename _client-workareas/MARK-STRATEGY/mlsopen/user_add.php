<?php
require 'settings.php';

$found = 0;
$active = 0;

	$linkID = @mysql_connect("$server", "$username", "$password");
	mysql_select_db("$database", $linkID);

	$resultID = mysql_query("SELECT * FROM `users`", $linkID);
	for ($x= 0; $x < mysql_num_rows($resultID); $x++) {
		$row = mysql_fetch_assoc($resultID);
		if (($uname == $row[uname]) and ($upass == $row[upass])) {
			$found = 1;
			$u_name = $row[u_name];
			$numlistings = $row[numlistings];
		}
	}

if ($found == 1) {
	setcookie ("mls_uname", $uname,time()+2592000); /* expire in 30 days */
	setcookie ("mls_upass", $upass,time()+2592000); /* expire in 30 days */
} 

include 'header.inc';

if (($mls_uname == $uname) and ($mls_upass == $upass) and ($found == 1)) {

print "
<p align=\"center\"><b>Create New Listing<br>
Items marked with a <font color=\"#FF0000\">*</font> are required fields.</b></p>
<form action=user_post.php method=post enctype=\"multipart/form-data\">
<input type=\"hidden\" name=\"MAX_FILE_SIZE\" value=\"$maxsize\">
<input type=\"hidden\" name=\"uname\" value=\"$uname\">
<input type=\"hidden\" name=\"upass\" value=\"$upass\">
<div align=\"center\">
  <center>
  <table border=\"1\" width=\"720\" height=\"1523\" bgcolor=\"$table_bg_color\"><font color=\"$table_text_color\">
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">MLS Number:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><input type=text name=mls size=20>
  </font>
      <font color=\"#FF0000\"><b>*</b></font></td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">Realtor Name:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=realtor_name size=20>
  </font>
        <font color=\"#FF0000\"><b>*</b></font>
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">Realtor Phone:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=realtor_phone size=20>
  </font>
        <font color=\"#FF0000\"><b>*</b></font>
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">Realtor Email:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=realtor_email size=20>
  </font>
        <font color=\"#FF0000\"><b>*</b></font>
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"19\" colspan=\"2\">&nbsp;</td>
      <td width=\"350\" height=\"19\" colspan=\"2\">&nbsp;</td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">Title of Listing:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=title size=20>
  </font>
        <font color=\"#FF0000\"><b>*</b></font>
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">Short Description:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=short_description size=20>
  </font>
        <font color=\"#FF0000\"><b>*</b></font>
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"16\" colspan=\"2\"><font color=\"$table_text_color\">Detailed Description: (HTML OK)</font></td>
      <td width=\"350\" height=\"16\" colspan=\"2\"><textarea rows=\"5\" name=\"detailed_description\" cols=\"39\"></textarea>
        <font color=\"#FF0000\"><b>*</b></font></td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">Listing Price:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">$ <input type=text name=price size=20>
  </font>
        <font color=\"#FF0000\"><b>*</b></font>
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"19\" colspan=\"2\">&nbsp;</td>
      <td width=\"350\" height=\"19\" colspan=\"2\">&nbsp;</td>
    </tr>
    <tr>
      <td width=\"324\" height=\"19\" colspan=\"2\"><font color=\"$table_text_color\">Number of Bedrooms:</font></td>
      <td width=\"350\" height=\"19\" colspan=\"2\"><select size=\"1\" name=\"bedrooms\">
          <option>1</option>
          <option>2</option>
          <option selected>3</option>
          <option>4</option>
          <option>5</option>
          <option>6</option>
          <option>7</option>
          <option>8</option>
          <option>9</option>
          <option>10</option>
        </select> <font color=\"#FF0000\"><b>*</b></font></td>
    </tr>
    <tr>
      <td width=\"324\" height=\"19\" colspan=\"2\"><font color=\"$table_text_color\">Number of Baths:</font></td>
      <td width=\"350\" height=\"19\" colspan=\"2\"><select size=\"1\" name=\"baths\">
          <option>1</option>
          <option selected>2</option>
          <option>3</option>
          <option>4</option>
          <option>5</option>
          <option>6</option>
          <option>7</option>
          <option>8</option>
          <option>9</option>
          <option>10</option>
        </select> <font color=\"#FF0000\"><b>*</b></font></td>
    </tr>
    <tr>
      <td width=\"324\" height=\"19\" colspan=\"2\"><font color=\"$table_text_color\">Number of Half-Baths:</font></td>
      <td width=\"350\" height=\"19\" colspan=\"2\"><select size=\"1\" name=\"half_baths\">
          <option selected>0</option>
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
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=sqf size=20>
  </font>
        <font color=\"#FF0000\"><b>*</b></font>
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">Total Acres:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=acres size=20>
  </font>
        <font color=\"#FF0000\"><b>*</b></font>
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">Listing Type (IE: Ranch, Townhome,
        etc.)</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=house_type size=20>
  </font>
        <font color=\"#FF0000\"><b>*</b></font>
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"6\" colspan=\"2\">&nbsp;</td>
      <td width=\"350\" height=\"6\" colspan=\"2\">&nbsp;</td>
    </tr>
    <tr>
      <td width=\"674\" height=\"7\" colspan=\"4\"><b>Click on the browse button to select the image. Uploading may take several minutes.</b></td>
    </tr>
    <tr>
      <td width=\"324\" height=\"10\" colspan=\"2\">&nbsp;</td>
      <td width=\"350\" height=\"10\" colspan=\"2\">&nbsp;</td>
    </tr>\n";
if($uploads <= 1) 
{ 
    $uploads = 10; 
} 


for($i = 1; $i <= $uploads; $i++) 
{ 
    if (($i == 1) or ($i == 3) or ($i == 5) or ($i == 7) or ($i == 9)) {
	print("<tr>\n");
    }
    print("<td><font color=\"$table_text_color\">Image $i</font></td><td><input type=\"file\" name=\"uploadedFile[]\" size=\"25\"></td>\n"); 
    if (($i == 2) or ($i == 4) or ($i == 6) or ($i == 8) or ($i == 10)) {
	print("</tr>\n");
    }

} 



    print "<tr>
      <td width=\"324\" height=\"19\" colspan=\"2\">&nbsp;</td>
      <td width=\"350\" height=\"19\" colspan=\"2\">&nbsp;</td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">URL to more detailed page:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=url size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">URL to Virtual Tour:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=virtual_tour size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">URL to property map:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=map size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"19\" colspan=\"2\">&nbsp;</td>
      <td width=\"350\" height=\"19\" colspan=\"2\">&nbsp;</td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">Property Address:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=property_address size=20>
  </font>
        <font color=\"#FF0000\"><b>*</b></font>
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">Property City:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=property_city size=20>
  </font>
        <font color=\"#FF0000\"><b>*</b></font>
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">Property State:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=property_state size=20>
  </font>
        <font color=\"#FF0000\"><b>*</b></font>
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">Property County:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=property_county size=20>
  </font>
        <font color=\"#FF0000\"><b>*</b></font>
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">Property Zip Code:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=property_zip size=20>
  </font>
        <font color=\"#FF0000\"><b>*</b></font>
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"23\" colspan=\"2\"><font color=\"$table_text_color\">Property School Zone:</font></td>
      <td width=\"350\" height=\"23\" colspan=\"2\"><font color=\"#008080\"><input type=text name=property_school_zone size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"324\" height=\"19\" colspan=\"2\">&nbsp;</td>
      <td width=\"350\" height=\"19\" colspan=\"2\">&nbsp;</td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 1</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature1 size=20>
  </font>
        <font color=\"#FF0000\"><b>*</b></font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 21</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature21 size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 2</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature2 size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 22</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature22 size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 3</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature3 size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 23</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature23 size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 4</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature4 size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 24</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature24 size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 5</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature5 size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 25</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature25 size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 6</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature6 size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 26</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature26 size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 7</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature7 size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 27</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature27 size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 8</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature8 size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 28</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature28 size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 9</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature9 size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 29</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature29 size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 10</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature10 size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 30</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature30 size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 11</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature11 size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 31</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature31 size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 12</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature12 size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 32</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature32 size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 13</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature13 size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 33</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature33 size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 14</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature14 size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 34</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature34 size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 15</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature15 size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 35</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature35 size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 16</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature16 size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 36</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature36 size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 17</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature17 size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 37</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature37 size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 18</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature18 size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 38</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature38 size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 19</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature19 size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 39</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature39 size=20>
  </font>
      </td>
    </tr>
    <tr>
      <td width=\"149\" height=\"23\"><font color=\"$table_text_color\">Feature 20</font></td>
      <td width=\"169\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature20 size=20>
  </font>
      </td>
      <td width=\"179\" height=\"23\"><font color=\"$table_text_color\">Feature 40</font></td>
      <td width=\"165\" height=\"23\"><font color=\"#008080\"><input type=text name=Feature40 size=20>
  </font>
      </td>
    </tr>
  </table></font>
  </center>
</div>
<center><input type=submit value=\"Post Listing\"></center>
</form>
\n";

} else {
	print "<center><h2>User Administrator Login</h2></center><br><br>\n";
	print "
	<form action=login.php method=post>
	<div align=center><table border=1 width=600>
	<tr><td>Username:</td><td><input type=text name=uname></td></tr>
	<tr><td>Password:</td><td><input type=password name=upass></td></tr>
	</table></div>
	<center><input type=submit value=Login></center>
	<br><br>
	\n";
} 

include 'footer.inc';
?>
