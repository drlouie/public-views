<?

# Version 1.1 Debugged, please upgrade older ones...

########################################################################
# Global Settings...
########################################################################

# Set the password for the eMail List editor!
$pass="mallory";
# Name of the datafile
$filelocation="subscribers.txt";
# Title of the newsletter, will be displayed in the FROM field of the mailclient
$lettername="Americor Lending Newsletter";
# Your email, will be the reply-to mail
$youremail="test@test.com";

########################################################################
# Displayed Messages
########################################################################

# Welcome message displayed above the form for subscribing/unsubscribing
$welcomemessage = "This is the place to subscribe and unsubscribe for the Americor Newsletter.  Your data will not be given to anyone and we send out small, once a month, text mails only.";

# Sorrymessage for failed subscription, will be followed by the email!
$sorrysignmessage = "Sorry, there is already an entry for ";

# Subscribe message, will be displayed when subscribing
$subscribemessage = "Thank you for subscribing. A confirmation email is being sent to ";
# Subscribemail, will be sent when someone subscribes.
$subscribemail = "Thank you for subscribing to the newsletter.";

# Unsubscribemessage for deletion, will be followed by the email!
$unsubscribemessage = "We deleted the following entry: ";

# Unsubscribemessage for failed deletion, will be followed by the email!
$failedunsubscriptionmessage = "Sorry, you cannot unssubscribe as we didn't find an entry for ";

########################################################################
# Let the code begin...
########################################################################

# Checks if the file exists, if not creates a new one
if (!file_exists($filelocation)) {
	$newfile = fopen($filelocation,"w+");
	fclose($newfile);
	}
# Open the datafile and read the content
$newfile = fopen($filelocation,"r");
$content = fread($newfile, filesize($filelocation));
fclose($newfile);
# Remove the slashes PHP automatically puts before special characters
$content=stripslashes($content);
# Reset the output of the "search result"
$out="";
# Put the entries into the array lines
$lines = explode("%",$content);
for ($key=1;$key<sizeof($lines);$key++){
# when the email is not in the list, add the old entries
	if ($lines[$key] != $email){
		$out .= "%".$lines[$key];
	}
# when it's already in the list, set found
	else {
		$found=1;
	}
}

########################################################################
# Signing in
########################################################################

if ($action=="sign"){
# When there is already a subscription for this email *duh*
	if ($found==1){
# Display Sorrymessage
		echo "<div align=\"center\"><b>".$sorrysignmessage.$email."</b></div><br><br>";
		$disp="yes";
	}
# otherwise, add the email to the list
	else {
	$disp="no";
	$newfile = fopen($filelocation,"a+");
	$add = "%".$email;
	fwrite($newfile, $add);
	fclose($newfile);
# display the message of subscription
	echo "<div align=\"center\"><font size=2 face=Verdana, Arial, Helvetica, sans-serif>".$subscribemessage.$email."</font></div><br><br>";
# send confirmation Mail
	$submailheaders = "From: $lettername subscription form\n";
	$submailheaders .= "Reply-To: $youremail\n";
	mail ($email,$lettername." subscription",$subscribemail,$submailheaders);
	}
}

########################################################################
# Signing out
########################################################################

if ($action=="delete"){
$disp="no";
# If the email is in the list...
	if ($found == 1){
	$newfile = fopen($filelocation,"w+");
	fwrite($newfile, $out);
	fclose($newfile);
# display the message for deleted items...
	echo "<div align=\"center\"><b>".$unsubscribemessage.$email."</b></div><br><br>";
	$disp="no";
	}
# if the email is not in the list
	if ($found != 1){
# display the message that tells that...
	echo "<div align=\"center\"><b>".$failedunsubscriptionmessage.$email."</b></div><br><br>";
	$disp="YES";
	}
}

########################################################################
# The core for the owner of the letter
########################################################################

if ($pw	== $pass){

# When nothing was entered so far, display the form
if ($send != "yes" && $send != "test"){
print'<form method="post"><input type="hidden" name=pw value='.$pass.'><input type="hidden" name=send value=yes>
<br><b>Newsletter editor:</b><br><br>
Subject:<br>
<input type="text" name="subject" size=20><br>
Message:<br>
<textarea cols=50 rows=10 wrap="virtual" name="message"></textarea><br><br>
<input type="submit" value="send">
</form>';
}

# Predefine the Mail Settings for sending...
$mailheaders = "From: $lettername\n";
$mailheaders .= "Reply-To:$youremail\n";
# add data in bcc fields

# Data was ok, send button is pressed
if ($send == "yes"){
	$message=stripslashes($message);
	$subject=stripslashes($subject);
	$lines = explode("%",$content);
		for ($key=1;$key<sizeof($lines);$key++){
		mail ($lines[$key],$subject,$message,$mailheaders);
		}
	print "<b>The following email has been sent!</b>";
	print "<pre>$mailheaders\n$subject\n$message</pre>";
	}
}


########################################################################
# The Form for the users...
########################################################################
if ($pw != $pass && $disp != "no"){
print $welcomemessage;
print'
<div align="center"><form method="post">
<input type="text" name="email" value="crackrat@attbi.com" size=30>
<input type="radio" name="action" value="sign" checked>subscribe
<input type="radio" name="action" value="delete">unsubscribe<br>
<input type="submit" value="send">
</form></div>
';
}
?>
