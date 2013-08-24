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



print "<center><br><b>Upgrade Account</b><br>You currently have $numlistings assigned to your account.<br></center>\n";

$order_amount = $amount_of_listings * $price_per_listing;

print "$u_name,<br>An additional $amount_of_listings listing will be \$$order_amount per month.<br>
Total quantity ordering: $amount_of_listings listings.
<br>To complete your order please click on the paypal link below:<br><br>\n";

print "
<form action=\"https://www.paypal.com/cgi-bin/webscr\" method=\"post\">
<input type=\"hidden\" name=\"cmd\" value=\"_xclick-subscriptions\">
<input type=\"hidden\" name=\"business\" value=\"$paypal\">
<input type=\"hidden\" name=\"item_name\" value=\"Listing Subscription\">
<input type=\"hidden\" name=\"item_number\" value=\"001\">
<input type=\"hidden\" name=\"no_shipping\" value=\"1\">
<input type=\"hidden\" name=\"no_note\" value=\"1\">
<input type=\"hidden\" name=\"currency_code\" value=\"USD\">
<input type=\"hidden\" name=\"on0\" value=\"quantity\">
<input type=\"hidden\" name=\"os0\" value=\"$amount_of_listings\">
<input type=\"image\" src=\"https://www.paypal.com/images/x-click-but20.gif\" border=\"0\" name=\"submit\" alt=\"Make payments with PayPal - it's fast, free and secure!\">
<input type=\"hidden\" name=\"a3\" value=\"$order_amount\">
<input type=\"hidden\" name=\"p3\" value=\"1\">
<input type=\"hidden\" name=\"t3\" value=\"M\">
<input type=\"hidden\" name=\"src\" value=\"1\">
<input type=\"hidden\" name=\"sra\" value=\"1\">
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
