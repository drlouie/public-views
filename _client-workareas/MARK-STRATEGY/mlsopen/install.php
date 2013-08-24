
<br><br><center><b>MLS Lister 3.01 Multi Install</b></center><br><br>

<?php
extract($HTTP_GET_VARS);




	print "<br>To continue we will now need to create the MySQL database:<br>\n";
	print "<div align=center><table border=1>
	<form action=install.php method=post>
	<input type=hidden name=db_connect_test value=1>
	<tr><td>MySQL Server: Usually localhost</td><td><input type=text name=db_server size=20></td></tr>
	<tr><td>MySQL Database Name:</td><td><input type=text name=db_name size=20></td></tr>
	<tr><td>MySQL User Name:</td><td><input type=text name=db_user_name size=20></td></tr>
	<tr><td>MySQL Password:</td><td><input type=text name=db_user_pass size=20></td></tr>
	</table></div><center><input type=submit value=\"Save Setings and Create Database\"></form>\n";




if ($db_connect_test == 1) {

print "<b>Creating MySQL Database. Please wait...<br></b><br>\n";

// this is the name of the table you want to create 
$tablename = "settings";  

	$stmt = "CREATE TABLE $tablename ( 
	id int(11) NOT NULL auto_increment,
	admin_password char(20) NOT NULL default 'default',
        admin_email char(60) NOT NULL default 'robert@techknow.com',
        headers char(200) NOT NULL default 'From: MLS Lister <admin@randbscripting.com>',
        site_name char(100) NOT NULL default 'MLS Lister',
        site_url char(200) NOT NULL default 'http://www.rhomberg.com/mlsopen/',
        table_bg_color char(7) NOT NULL default '#C0C0C0',
        table_text_color char(7) NOT NULL default '#008080',
        maxsize char(100) NOT NULL default '200000',
        path char(200) NOT NULL default '/usr/local/www/vhosts/rhomberg.com/htdocs/mlsopen/',
        img_url char(200) NOT NULL default 'http://www.rhomberg.com/mlsopen/img/',
        realtor_name_set char(200) NOT NULL default '',
        realtor_company char(200) NOT NULL default '',
        realtor_phone_set char(200) NOT NULL default '',
        image_size_1 char(4) NOT NULL default '200',
        image_size_2 char(4) NOT NULL default '200',
        my_image_size_1 char(4) NOT NULL default '100',
        my_image_size_2 char(4) NOT NULL default '100',
        details_main_image_1 char(4) NOT NULL default '400',
  details_main_image_2 char(4) NOT NULL default '400',
  details_bottom_image_1a char(4) NOT NULL default '400',
  details_bottom_image_2a char(4) NOT NULL default '400',
  details_bottom_image_1b char(4) NOT NULL default '400',
  details_bottom_image_2b char(4) NOT NULL default '400',
  details_bottom_image_1c char(4) NOT NULL default '400',
  details_bottom_image_2c char(4) NOT NULL default '400',
  details_bottom_image_1d char(4) NOT NULL default '400',
  details_bottom_image_2d char(4) NOT NULL default '400',
  details_bottom_image_1e char(4) NOT NULL default '400',
  details_bottom_image_2e char(4) NOT NULL default '400',
  details_bottom_image_1f char(4) NOT NULL default '400',
  details_bottom_image_2f char(4) NOT NULL default '400',
  details_bottom_image_1g char(4) NOT NULL default '400',
  details_bottom_image_2g char(4) NOT NULL default '400',
  details_bottom_image_1h char(4) NOT NULL default '400',
  details_bottom_image_2h char(4) NOT NULL default '400',
  details_bottom_image_1i char(4) NOT NULL default '400',
  details_bottom_image_2i char(4) NOT NULL default '400',
  php_v char(5) NOT NULL default '4.2.2',
  paypal char(200) NOT NULL default '',
  price_per_listing char(20) NOT NULL default '',
  PRIMARY KEY  (id)
  )";


// connect to the DB 
if(!($link = mysql_connect($db_server,$db_user_name,$db_user_pass))) {  
 printError(sprintf("Error connecting to host %s, by user %s",$db_server,$db_user_name));  
 exit();  
}  

// select active db 
if(!mysql_select_db($db_name,$link)) {  
 printError(sprintf("Error in selecting %s database",$db_name));  
 printError(sprintf("error: %d %s",mysql_errno($link),mysql_error($link)));  
 exit();  
}  

// create my table 
if(!mysql_query(sprintf($stmt,$tablename), $link)) {  
 printError(sprintf("Error in executing %s stmt",$stmt));  
 printError(sprintf("error: %d %s",mysql_errno($link),mysql_error($link)));  
 exit();  
}  

printf("<br> Created Table %s.%s <br>\n",$db_name,$tablename);  

// this is the name of the table you want to create 
$tablename = "user_mls";  

	$stmt = "CREATE TABLE $tablename ( 
  mls char(20) NOT NULL default '',
  realtor_user_name char(60) NOT NULL default '',
  realtor_name char(60) NOT NULL default '',
  realtor_phone char(15) NOT NULL default '',
  realtor_email char(80) NOT NULL default '',
  title char(30) NOT NULL default '',
  short_description char(200) NOT NULL default '',
  detailed_description char(250) NOT NULL default '',
  price char(20) NOT NULL default '',
  status char(20) NOT NULL default '',
  bedrooms char(10) NOT NULL default '',
  baths char(10) NOT NULL default '',
  half_baths char(10) NOT NULL default '',
  sqf char(10) NOT NULL default '',
  acres char(10) NOT NULL default '',
  house_type char(30) NOT NULL default '',
  image1 char(30) NOT NULL default '',
  image2 char(30) NOT NULL default '',
  image3 char(30) NOT NULL default '',
  image4 char(30) NOT NULL default '',
  image5 char(30) NOT NULL default '',
  image6 char(30) NOT NULL default '',
  image7 char(30) NOT NULL default '',
  image8 char(30) NOT NULL default '',
  image9 char(30) NOT NULL default '',
  image10 char(30) NOT NULL default '',
  url char(100) NOT NULL default '',
  virtual_tour char(100) NOT NULL default '',
  map char(100) NOT NULL default '',
  property_address char(60) NOT NULL default '',
  property_city char(60) NOT NULL default '',
  property_state char(60) NOT NULL default '',
  property_zip char(10) NOT NULL default '',
  property_county char(60) NOT NULL default '',
  property_school_zone char(100) NOT NULL default '',
  feature1 char(30) NOT NULL default '',
  feature2 char(30) NOT NULL default '',
  feature3 char(30) NOT NULL default '',
  feature4 char(30) NOT NULL default '',
  feature5 char(30) NOT NULL default '',
  feature6 char(30) NOT NULL default '',
  feature7 char(30) NOT NULL default '',
  feature8 char(30) NOT NULL default '',
  feature9 char(30) NOT NULL default '',
  feature10 char(30) NOT NULL default '',
  feature11 char(30) NOT NULL default '',
  feature12 char(30) NOT NULL default '',
  feature13 char(30) NOT NULL default '',
  feature14 char(30) NOT NULL default '',
  feature15 char(30) NOT NULL default '',
  feature16 char(30) NOT NULL default '',
  feature17 char(30) NOT NULL default '',
  feature18 char(30) NOT NULL default '',
  feature19 char(30) NOT NULL default '',
  feature20 char(30) NOT NULL default '',
  feature21 char(30) NOT NULL default '',
  feature22 char(30) NOT NULL default '',
  feature23 char(30) NOT NULL default '',
  feature24 char(30) NOT NULL default '',
  feature25 char(30) NOT NULL default '',
  feature26 char(30) NOT NULL default '',
  feature27 char(30) NOT NULL default '',
  feature28 char(30) NOT NULL default '',
  feature29 char(30) NOT NULL default '',
  feature30 char(30) NOT NULL default '',
  feature31 char(30) NOT NULL default '',
  feature32 char(30) NOT NULL default '',
  feature33 char(30) NOT NULL default '',
  feature34 char(30) NOT NULL default '',
  feature35 char(30) NOT NULL default '',
  feature36 char(30) NOT NULL default '',
  feature37 char(30) NOT NULL default '',
  feature38 char(30) NOT NULL default '',
  feature39 char(30) NOT NULL default '',
  feature40 char(30) NOT NULL default '',
  myimage char(30) NOT NULL default '',
  PRIMARY KEY  (mls)
  )";


// connect to the DB 
if(!($link2 = mysql_connect($db_server,$db_user_name,$db_user_pass))) {  
 printError(sprintf("Error connecting to host %s, by user %s",$db_server,$db_user_name));  
 exit();  
}  

// select active db 
if(!mysql_select_db($db_name,$link2)) {  
 printError(sprintf("Error in selecting %s database",$db_name));  
 printError(sprintf("error: %d %s",mysql_errno($link2),mysql_error($link2)));  
 exit();  
}  

// create my table 
if(!mysql_query(sprintf($stmt,$tablename), $link2)) {  
 printError(sprintf("Error in executing %s stmt",$stmt));  
 printError(sprintf("error: %d %s",mysql_errno($link2),mysql_error($link2)));  
 exit();  
}  

printf("Created Table %s.%s <br>\n",$db_name,$tablename);  

// this is the name of the table you want to create 
$tablename = "user_settings";  

	$stmt = "CREATE TABLE $tablename ( 
id int(11) NOT NULL auto_increment,
  uname varchar(200) NOT NULL default '',
  header longtext NOT NULL,
  footer longtext NOT NULL,
  main_template longtext NOT NULL,
  detailed_template longtext NOT NULL,
  PRIMARY KEY  (id)
  )";


// connect to the DB 
if(!($link3 = mysql_connect($db_server,$db_user_name,$db_user_pass))) {  
 printError(sprintf("Error connecting to host %s, by user %s",$db_server,$db_user_name));  
 exit();  
}  

// select active db 
if(!mysql_select_db($db_name,$link3)) {  
 printError(sprintf("Error in selecting %s database",$db_name));  
 printError(sprintf("error: %d %s",mysql_errno($link3),mysql_error($link3)));  
 exit();  
}  

// create my table 
if(!mysql_query(sprintf($stmt,$tablename), $link3)) {  
 printError(sprintf("Error in executing %s stmt",$stmt));  
 printError(sprintf("error: %d %s",mysql_errno($link3),mysql_error($link3)));  
 exit();  
}  

printf("Created Table %s.%s <br>\n",$db_name,$tablename);  

// this is the name of the table you want to create 
$tablename = "users";  

	$stmt = "CREATE TABLE $tablename ( 
 id int(11) NOT NULL auto_increment,
  uname char(200) NOT NULL default '',
  upass char(200) NOT NULL default '',
  numlistings int(30) NOT NULL default '0',
  img_path char(200) NOT NULL default '',
  u_name char(200) NOT NULL default '',
  u_company char(200) NOT NULL default '',
  u_address char(200) NOT NULL default '',
  u_city char(200) NOT NULL default '',
  u_state char(200) NOT NULL default '',
  u_zip char(200) NOT NULL default '',
  u_country char(200) NOT NULL default '',
  u_email char(200) NOT NULL default '',
  u_phone char(200) NOT NULL default '',
  PRIMARY KEY  (id),
  UNIQUE KEY uname (uname)
  )";


// connect to the DB 
if(!($link4 = mysql_connect($db_server,$db_user_name,$db_user_pass))) {  
 printError(sprintf("Error connecting to host %s, by user %s",$db_server,$db_user_name));  
 exit();  
}  

// select active db 
if(!mysql_select_db($db_name,$link4)) {  
 printError(sprintf("Error in selecting %s database",$db_name));  
 printError(sprintf("error: %d %s",mysql_errno($link4),mysql_error($link4)));  
 exit();  
}  

// create my table 
if(!mysql_query(sprintf($stmt,$tablename), $link4)) {  
 printError(sprintf("Error in executing %s stmt",$stmt));  
 printError(sprintf("error: %d %s",mysql_errno($link4),mysql_error($link4)));  
 exit();  
}  

printf("Created Table %s.%s <br>\n",$db_name,$tablename);  

// import default settings
$linkID = @mysql_connect("$db_server", "$db_user_name", "$db_user_pass");
mysql_select_db("$db_name", $linkID);

$result = mysql_query("INSERT INTO settings VALUES (1, 'default', 'robert@techknow.com', 'From: R&B Scripting <robert@techknow.com>', 'R&B Scripting', 'http://www.turnkeyhosting.net/mlslister', '#C0C0C0', '#000000', '200000', '/home/virtual/site1/fst/var/www/html/mlslister/img3/', 'http://www.turnkeyhosting.net/mlslister/img3/', 'Your Name', 'ABC Realty', '(800) 555-1212', '100', '100', '100', '100', '400', '400', '400', '400', '400', '400', '400', '400', '400', '400', '400', '400', '400', '400', '400', '400', '400', '400', '400', '400', '4.2.2', 'robert@techknow.com', '0.05')", $linkID);
if ($result == TRUE) {
	print "<br>Default settings were imported.\n";
} else {
	print "<br><font color=red>MySQL error - unable to import default settings. Contact <a href=\"mailto:robert@techknow.com\">robert@techknow.com</a> for help.  Install will continue...</font>\n";
}

// create the config file

$configi = fopen("config.php","w");
$config_write = "<?php
\$server   = \"$db_server\";
\$database = \"$db_name\";
\$username = \"$db_user_name\";
\$password = \"$db_user_pass\";
?>
";

fwrite($configi, $config_write);
fclose($configi);

print "<br>Created config.php\n";

print "<br><b><u><i>Post Installation:<br>
</i></u></b><br><b>Install is now complete.  If you did not receive any errors then you may continue.<br>
<br>
Please note: <font color=#FF0000>PHP SAFE MODE = OFF</font> is now <font color=#FF0000><u>required</u></font>.&nbsp;
Contact your system administration for help turning<br>
safe mode off.<br>
<br>
You will now need to FTP or SSH into your account and set the file permission of
header.inc and footer.inc to 644.<br>
<p><b><br>
To login to the admin interface click <a href=admin.php>admin.php</a><br>
The default password is <font color=blue>default</font>. Before you get started please <font color=red><b>delete install.php</font></b> from the web server<br>
then login to the admin interface and click on Settings.</b></p>
<p><b>Thank you for using MLS Lister --<br>
</b><a href=\"http://cripts.blurstorm.com\">http://scripts.blurstorm.com</a><b><br><br></b></p>
\n";
}

?>

