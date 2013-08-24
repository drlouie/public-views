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

	$active = 0;
	$linkID4 = @mysql_connect("$server", "$username", "$password");
	mysql_select_db("$database", $linkID4);

	$resultID4 = mysql_query("SELECT * FROM `user_mls`", $linkID4);
	for ($x4= 0; $x4 < mysql_num_rows($resultID4); $x4++) {
		$row4 = mysql_fetch_assoc($resultID4);
		if ($row4[realtor_user_name] == $uname) {
			$active = $active + 1;
		}
	}

	if (($active == $numlistings) or ($active > $numlistings)) {
		print "<br><center><b><font color=red>We are sorry, but you have used all your listing slots.<br>Please consider upgrading your account or remove some of your current property listings.</b></font></center><br><br>\n";
		include 'footer.inc';
		die;
	}



// Check for empty fields:
if (($mls == "") or ($realtor_name == "") or ($realtor_phone == "") or ($realtor_email == "") or ($title == "")
or ($short_description == "") or ($detailed_description == "") or ($price == "") or ($sqf == "") or ($acres == "")
or ($house_type == "") or ($uploadedFile_name[0] == "") or ($property_address == "") or ($property_city == "") 
or ($property_state == "") or ($property_zip == "") or ($Feature1 == "")) {
	print "<br><br><b><center><font color=red>Sorry, you did not enter all required fields.<br>Click back and correct the form.</b></font></center><br><br>\n";
	include 'footer.inc';
	die;
}

	print "<br><center><b>Post New Item</b></center>\n";
	$linkID = @mysql_connect("$server", "$username", "$password");
	mysql_select_db("$database", $linkID);

	$result = mysql_query("INSERT INTO user_mls (
mls,realtor_user_name,realtor_name,realtor_phone,realtor_email,title,short_description,detailed_description,price,status,bedrooms,
baths,half_baths,sqf,acres,house_type,image1,image2,image3,image4,image5,image6,image7,image8,image9,image10,
url,virtual_tour,map,property_address,property_city,property_state,property_zip,property_county,property_school_zone,
feature1,feature2,feature3,feature4,feature5,feature6,feature7,feature8,feature9,feature10,feature11,feature12,
feature13,feature14,feature15,feature16,feature17,feature18,feature19,feature20,feature21,feature22,feature23,
feature24,feature25,feature26,feature27,feature28,feature29,feature30,feature31,feature32,feature33,feature34,
feature35,feature36,feature37,feature38,feature39,feature40) VALUES (
'$mls','$uname','$realtor_name','$realtor_phone','$realtor_email','$title','$short_description','$detailed_description','$price','$status','$bedrooms','$baths',
'$half_baths','$sqf','$acres','$house_type','$uploadedFile_name[0]','$uploadedFile_name[1]','$uploadedFile_name[2]','$uploadedFile_name[3]','$uploadedFile_name[4]','$uploadedFile_name[5]','$uploadedFile_name[6]','$uploadedFile_name[7]','$uploadedFile_name[8]','$uploadedFile_name[9]','$url',
'$virtual_tour','$map','$property_address','$property_city','$property_state','$property_zip','$property_county','$property_school_zone','$Feature1',
'$Feature2','$Feature3','$Feature4','$Feature5','$Feature6','$Feature7','$Feature8','$Feature9','$Feature10','$Feature11','$Feature12','$Feature13',
'$Feature14','$Feature15','$Feature16','$Feature17','$Feature18','$Feature19','$Feature20','$Feature21','$Feature22','$Feature23','$Feature24',
'$Feature25','$Feature26','$Feature27','$Feature28','$Feature29','$Feature30','$Feature31','$Feature32','$Feature33','$Feature34','$Feature35',
'$Feature36','$Feature37','$Feature38','$Feature39','$Feature40')", $linkID);


if($uploads <= 1) 
{ 
    $uploads = 10; 
} 
$fields = $uploads + $uploads; 

for($n = 0; $n < $uploads; $n++) 
{ 
    if($uploadedFile[$n] != "" && $uploadedFile[$n] != "none") 
    { 
    copy("$uploadedFile[$n]", "$path$uname/$uploadedFile_name[$n]"); 
    if(file_exists("$path$fileName[$n]")) 
    { 
	//
    } 
    else 
    { 
        print("error: upload failed<br>\n"); 
    } 
    } 
} 


if ($result == TRUE) {
	print "<br><br><b><center>MLS number $mls was added to the database.</center></b><br><br></center>\n";
		print "<center><a href=login.php?uname=$uname&upass=$upass>Home</a></center><br>\n";
} else {
	print "<center><font color=red><b>The server was unable to write to the MySQL DataBase.<br><br></b></font></center>\n";
}

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
