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
	$login_name = "login.php?uname=$uname&upass=$upass";
	setcookie ("mls_uname", $uname,time()+2592000); /* expire in 30 days */
	setcookie ("mls_upass", $upass,time()+2592000); /* expire in 30 days */
	$mls_uname = $uname;
	$mls_upass = $upass; 
	
} 

include 'header.inc';

if (($mls_uname == $uname) and ($mls_upass == $upass) and ($found == 1)) {
	$linkID = @mysql_connect("$server", "$username", "$password");
	mysql_select_db("$database", $linkID);

	$resultID = mysql_query("SELECT * FROM `user_mls`", $linkID);
	for ($x= 0; $x < mysql_num_rows($resultID); $x++) {
		$row = mysql_fetch_assoc($resultID);
		if ($row[realtor_user_name] == $uname) {
			$active = $active + 1;
		}
	}

	print "
	<center><br><br><center><b><H2>$u_name : User Administration</H2></b></center>
<div align=\"center\">
  <center>
  <table border=\"3\" width=\"651\" height=\"144\" cellspacing=\"0\" cellpadding=\"0\">
    <tr>
      <td width=\"197\" height=\"6\" bgcolor=\"#FFFFFF\" bordercolor=\"#FFFFFF\">
        <ul>
          \n";

if (($active == $numlistings) or ($active > $numlistings)) {
	print "<li>Add Listing</li>\n";
} else {
	print "<li><a href=user_add.php?uname=$uname&upass=$upass>Add Listing</a></li>\n";
}

        print "</ul>
      </td>
      <td width=\"244\" height=\"144\" rowspan=\"6\" bgcolor=\"#FFFFFF\" bordercolor=\"#FFFFFF\">
        <p align=\"center\">\n";


	print "User Level: $numlistings listings.<br>
		Active listings: $active<br>\n";
	if ($active > 0) {
		$diff_list = $numlistings - $active;
		if ($diff_list == 0) {
			print "<b><font color=red>You have used all your listings.</b></font>\n";
		} else {
			print "Listing remaining: $diff_list<br>\n";
		}
	}
	if ($numlistings == 0) {
		print "<center><b><font color=red>Your account is pending approval.</b></font></center>\n";
	}
	print "<br><center><a href=$site_url/index.php?id=$uname target=_blank>View your listing page</a></center>\n";


	print "</td>
      <td width=\"188\" height=\"2\" bgcolor=\"#FFFFFF\" bordercolor=\"#FFFFFF\">
        <ul>

        </ul>
      </td>
    </tr>
    <tr>
      <td width=\"197\" height=\"26\" bgcolor=\"#FFFFFF\" bordercolor=\"#FFFFFF\">
        <ul>
          <li><a href=user_edit.php?uname=$uname&upass=$upass>Edit Listings</li>
        </ul>
      </td>
      <td width=\"188\" height=\"22\" bgcolor=\"#FFFFFF\" bordercolor=\"#FFFFFF\">
        <ul>
          <li><a href=user_settings.php?uname=$uname&upass=$upass>Edit Settings</a></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td width=\"197\" height=\"16\" bgcolor=\"#FFFFFF\" bordercolor=\"#FFFFFF\">
        <ul>
          <li><a href=user_delete.php?uname=$uname&upass=$upass>Delete Listings</a></li>
        </ul>
      </td>
      <td width=\"188\" height=\"21\" bgcolor=\"#FFFFFF\" bordercolor=\"#FFFFFF\">
        <ul>
          <li><a href=updatereg.php?uname=$uname&upass=$upass>Update Registration</a></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td width=\"197\" height=\"23\" bgcolor=\"#FFFFFF\" bordercolor=\"#FFFFFF\">
        <ul>
          <li><a href=user_myimage.php?uname=$uname&upass=$upass>Add My Image</a></li>
        </ul>
      </td>
      <td width=\"188\" height=\"21\" bgcolor=\"#FFFFFF\" bordercolor=\"#FFFFFF\">
        <ul>
          <li><a href=user_upgrade.php?uname=$uname&upass=$upass>Upgrade Account</a></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td width=\"197\" height=\"21\" bgcolor=\"#FFFFFF\" bordercolor=\"#FFFFFF\">
        <ul>
          <li><a href=user_status.php?uname=$uname&upass=$upass>Change Listing Status</a></li>
        </ul>
      </td>
      <td width=\"188\" height=\"21\" bgcolor=\"#FFFFFF\" bordercolor=\"#FFFFFF\">
        <ul>
          <li><a href=user_troubleticket.php?uname=$uname&upass=$upass>Open Trouble Ticket</a></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td width=\"197\" height=\"24\" bgcolor=\"#FFFFFF\" bordercolor=\"#FFFFFF\"></td>
      <td width=\"188\" height=\"24\" bgcolor=\"#FFFFFF\" bordercolor=\"#FFFFFF\">&nbsp;</td>
    </tr>
  </table>
  </center>
</div>\n";










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

if ($licdata[expire] != "never")
{
   $now = time();
   $date = date("m-d-Y", $now);
   $exp_date = date("m-d-Y", $licdata[expire]);
   $time = date("G:i:s", $now);
   $exp_time = date("G:i:s", $licdata[expire]);
   list($exp_month,$exp_day,$exp_year) = explode("-", $exp_date);
   list($month,$day,$year) = explode("-", $date);
   list($hour,$minute,$second) = explode(":", $time);
   list($exp_hour,$exp_minute,$exp_second) = explode(":", $exp_time);
   $warnday = mktime($exp_hour,$exp_minute,$exp_second,$exp_month,$exp_day-3,$exp_year);
   $expire = $licdata[expire];

   if ($warnday <= $now)
   {
      $exp = "<br>Expires: <font color=\"#ff0000\"><b>" . date("m/d/Y h:i:s", $expire) . "</b></font>";
   }
   else
   {
      $exp = "<br>Expires: <b>" . date("m/d/Y", $expire) . "</b>";
   }
}
else
{
   $exp = "";
}


include 'footer.inc';
