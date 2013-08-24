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


if ($realtor_user_name == $uname) {

	print "<br><center><b>Update Item</b></center>\n";

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

if ($uploadedFile_name[0] != "") {
	$image1 = $uploadedFile_name[0];
}
if ($uploadedFile_name[1] != "") {
	$image2 = $uploadedFile_name[1];
}
if ($uploadedFile_name[2] != "") {
	$image3 = $uploadedFile_name[2];
}
if ($uploadedFile_name[3] != "") {
	$image4 = $uploadedFile_name[3];
}
if ($uploadedFile_name[4] != "") {
	$image5 = $uploadedFile_name[4];
}
if ($uploadedFile_name[5] != "") {
	$image6 = $uploadedFile_name[5];
}
if ($uploadedFile_name[6] != "") {
	$image7 = $uploadedFile_name[6];
}
if ($uploadedFile_name[7] != "") {
	$image8 = $uploadedFile_name[7];
}
if ($uploadedFile_name[8] != "") {
	$image9 = $uploadedFile_name[8];
}
if ($uploadedFile_name[9] != "") {
	$image10 = $uploadedFile_name[9];
}
	$linkID = @mysql_connect("$server", "$username", "$password");
	mysql_select_db("$database", $linkID);

$result = mysql_query("UPDATE user_mls SET realtor_name = '$realtor_name', realtor_phone = '$realtor_phone',realtor_email = '$realtor_email',
title = '$title', short_description = '$short_description', detailed_description = '$detailed_description', price = '$price',
bedrooms = '$bedrooms', baths = '$baths', half_baths = '$half_baths', sqf = '$sqf', acres = '$acres', house_type = '$house_type',
image1 = '$image1', image2 = '$image2', image3 = '$image3', image4 = '$image4', image5 = '$image5',image6 = '$image6',
image7 = '$image7', image8 = '$image8', image9 = '$image9', image10 = '$image10', url = '$url', virtual_tour = '$virtual_tour',
map = '$map', property_address = '$property_address', property_city = '$property_city', property_state = '$property_state',
property_zip = '$property_zip', property_county = '$property_county', property_school_zone = '$property_school_zone',
feature1 = '$feature1', feature2 = '$feature2', feature3 = '$feature3' , feature4 = '$feature4' , feature5 = '$feature5', 
feature6 = '$feature6' , feature7 = '$feature7' , feature8 = '$feature8' , feature9 = '$feature9' , feature10 = '$feature10',
feature11 = '$feature11', feature12 = '$feature12' , feature13 = '$feature13' , feature14 = '$feature14',
feature15 = '$feature15' , feature16 = '$feature16' , feature17 = '$feature17' , feature18 = '$feature18' , 
feature19 = '$feature19' , feature20 = '$feature20' , feature21 = '$feature21' , feature22 = '$feature22' , 
feature23 = '$feature23' , feature24 = '$feature24' , feature25 = '$feature25' , feature26 = '$feature26' , 
feature27 = '$feature27' , feature28 = '$feature28' , feature29 = '$feature29' , feature30 = '$feature30' , 
feature31 = '$feature31' , feature32 = '$feature32' , feature33 = '$feature33' , feature34 = '$feature34' , 
feature35 = '$feature35' , feature36 = '$feature36' , feature37 = '$feature37' , feature38 = '$feature38' , 
feature39 = '$feature39' , feature40 = '$feature40'
WHERE mls  =  '$mls'" ,  $linkID);


if ($result == TRUE) {
	print "<br><br><b><center>MLS number $mls was updated.</center></b><br><br></center>\n";
		print "<center><a href=login.php?uname=$uname&upass=$upass>Home</a></center><br>\n";
} else {
	print "<center><font color=red><b>The server was unable to write to the MySQL DataBase.<br><br></b></font></center>\n";
}

} else {
	print "<br><br><b><font color=red>Sorry, you may only change your listings.</b></center></font><br><br>\n";
	include 'footer.inc';
	die;
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
