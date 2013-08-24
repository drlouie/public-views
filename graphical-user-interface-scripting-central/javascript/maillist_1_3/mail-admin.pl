#!/usr/local/bin/perl

#######################################################
#             Mailing List V1.3	
#
# This program is distributed as freeware. We are not            	
# responsible for any damages that the program causes	
# to your system. It may be used and modified free of 
# charge, as long as the copyright notice
# in the program that give me credit remain intact.
# If you find any bugs in this program. It would be thankful
# if you can report it to us at cgifactory@cgi-factory.com.  
# However, that email address above is only for bugs reporting. 
# We will not  respond to the messages that are sent to that 
# address. If you have any trouble installing this program, 
# olease feel free to post a message on our CGI Support Forum.
# Selling this script is absolutely forbidden and illegal.
##################################################################
#
#               COPYRIGHT NOTICE:
#
#         Copyright 1999-2000 CGI-Factory.com TM 
#		  A subsidiary of SiliconSoup.com LLC
#
#
#      Web site: http://www.cgi-factory.com
#      E-Mail: cgifactory@cgi-factory.com
#      Released Date: August 28, 1999
#	
#   Footer V1.1 is protected by the copyright 
#   laws and international copyright treaties, as well as other 
#   intellectual property laws and treaties.
###################################################################
require "cfg.pl";
read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
@pairs = split(/&/, $buffer);
foreach $pair (@pairs) {
($name, $value) = split(/=/, $pair);
$value =~ tr/+/ /;
$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
$form{$name} = $value;
}

################################# first time
print "Content-type: text/html\n\n";
if ($form{'action'} eq "firsttime") {
&firsttime; 
}
if ($form{'action'} eq "main_page") { 
&main_page; 
}
if ($form{'action'} eq "preview") { 
&preview; 
}
if ($form{'action'} eq "sendnow") { 
&sendnow; 
}
if ($form{'action'} eq "view_all") { 
&view_all; 
}
open (DETECT,"<pass.dat") || &error("Unable to open pass.dat");
if ($flock eq "y") {
flock DETECT, 2; 
}
@detect=<DETECT>;
close (DETECT);
if (!@detect) {
print "Content-type: text/html\n\n";
print "This is the first time you run this script\n";
print "Please set your admin password:\n";
print "<form action=\"mail-admin.pl\" method=\"post\">Password:<input type=\"text\" name=\"password1\"><br>Enter the passward again:<input type=\"text\" name=\"password2\"><input type=\"hidden\" name=\"action\" value=\"firsttime\"><input type=\"submit\" value=\"OK\"></form>";
exit;
}

sub firsttime {

if ($form{'password1'} eq "" and !$form{'password1'}) {
print "Please don't leave the password field blank!";
exit;
}
	
if ($form{'password2'} eq "" and !$form{'password2'}) {
print "Please don't leave the password field blank!";
exit;
}
if ($form{'password1'} ne "$form{'password2'}" and $form{'password1'} != $form{'password2'}){
print "You entered two different passwords. Please try again!";
exit;
}
$form{'password1'}=~ tr/A-Z/a-z/; 
$password = crypt($form{'password1'}, "MM");	
open (PASSWORD, ">pass.dat") || &error("unable to create the password file");
if ($flock eq "y") {
flock PASSWORD, 2; 
}
print PASSWORD "$password";
close (PASSWORD);
print "Setup complete\n";
exit;
}

###

print <<EOF;
<html>
<head>
<title>Mailing list Admin</title>
</head>
<body bgcolor="#ffffff">
<center><font face="Arial">
<b><font size="+3">Mailing List V1.3</font></b><font size="-1">&nbsp;&nbsp;<a href="http://www.cgi-factory.com/">from CGI-Factory.com!</a></font>
<br><br>
<table border="0">
<form action="mail-admin.pl" method="post">
<tr><td><b>Admin Password:</b></td><td><input type="password" name="password"></td></tr>
<tr><td></td><td><input type="hidden" name="action" value="main_page">
<input type="submit" value="GO!">
</form></td></tr></table></font></center>
</body>
</html>
EOF
###
sub main_page {

&vpassword;
open (list, "<$listdata") or &error("Unable to open the data file for reading");
if ($flock eq "y") {
flock list, 2; 
}
@list=<list>;
close(list);
$count=0;
foreach $list(@list) {
$count++;
}	
print <<EOF;
<html>
<head>
<title>Mailing list Admin</title>
</head>
<body bgcolor="#ffffff">
<center><font face="Arial">
<b><font size="+3">Mailing List V1.3</font></b><font size="-1">&nbsp;&nbsp;<a href="http://www.cgi-factory.com/">from CGI-Factory.com!</a></font>
<br><br>
<table border="0">
You have $count subscribers.<br>
<form action="mail-admin.pl" method="post">
<tr><td><b>Subject:</b></td><td><input type="text" name="subject" size="60"></td></tr>
<tr><td valign="top"><b>Message:</b></td><td><br><textarea cols="70" rows="15" name="message"></textarea></td></tr>
<tr><td></td><td><input type="hidden" name="password" value="$form{'password'}"></td></tr>
<tr><td></td><td><input type="hidden" name="action" value="preview">
<input type="submit" value="GO!">
</form></td></tr></table>
<table border="0" bgcolor="#ffffff"><tr><td>
<form action="mail-admin.pl" method="post">
<input type="hidden" name="password" value="$form{'password'}">
<input type="hidden" name="action" value="view_all">
<br><input type="submit" value="View all subscribers">
</form>
</td></tr></table>
<br><br>
<h3>Add/Remove an address</h3>
<table border="0" bgcolor="#ffffff"><tr><td>
<form action="maillist.pl" method="post">
<b>Email:</b> <input type="text" name="address" size="18" maxlength="50"><br>
<font size="-1">
<b>Subscribe</b>
<input type="radio" name="action" checked value="subscribe">
<b>Unsubscribe</b>
<input type="radio" name="action" value="unsubscribe"></font>
<br><input type="submit" value="GO!">
</form>
</td></tr>
</table>
</font></center>
</body>
</html>
EOF
exit;
}
sub view_all {

&vpassword;
open (list, "<$listdata") or &error("Unable to open the data file for reading");
if ($flock eq "y") {
flock list, 2; 
}
@list=<list>;
close(list);
print "<html><head><title>Mailing list Admin</title></head>
<body bgcolor=\"#ffffff\"><center><font face=\"Arial\">
<b><font size=\"+3\">Mailing List V1.3</font></b><font size=\"-1\">&nbsp;&nbsp;<a href=\"http://www.cgi-factory.com/\">from CGI-Factory.com!</a></font><br><br>";
@list=sort(@list);
foreach $list (@list) {
chomp ($list);
print "<form action=\"maillist.pl\" method=\"post\">$list
<input type=\"hidden\" name=\"address\" value=\"$list\"><br>
<input type=\"hidden\" name=\"action\" checked value=\"unsubscribe\">
<input type=\"submit\" value=\"Remove\">
</form>
";	
}	
print "<br>please close your browser if you want to log out.<br>
<form action=\"mail-admin.pl\" method=\"post\">
<input type=\"hidden\" name=\"action\" value=\"main_page\">
<input type=\"hidden\" name=\"password\" value=\"$form{'password'}\">
<input type=\"submit\" value=\"Back to the admin main page\">
</form>
";

print "</body></html>";
exit;
}

sub preview {

&vpassword;

$form{'subject'}=~ s/"/&quot;/ig;
$form{'message'}=~ s/"/&quot;/ig;
$form{'message'}=~ s/\n/<br>/ig;

print "<html>\n";
print "<head>\n";
print "<title>\n";
print "Mailing list Admin\n";
print "</title>\n";
print "</head>\n";
print "<body bgcolor=\"#ffffff\">\n";
print "The following information will be sent:<br>\n";
print "Subject: $form{'subject'}<br>\n";
print "Message:<br> $form{'message'}</br>\n";
$form{'message'}=~ s/<br>/\n/ig;
$form{'subject'}=~ s/</&lt;/ig;
$form{'subject'}=~ s/>/&gt;/ig;
$form{'message'}=~ s/</&lt;/ig;
$form{'message'}=~ s/>/&gt;/ig;
print <<EOF;
<form action="mail-admin.pl" method="post">
<input type="hidden" name="subject" value="$form{'subject'}">
<input type="hidden" name="message" value="$form{'message'}">
<input type="hidden" name="password" value="$form{'password'}"><br>
<input type="hidden" name="action" value="sendnow">
<input type="submit" value="GO!">
</form>
</body></br>
</html></br>

EOF
exit;
}
sub sendnow {
&vpassword;
$pid = fork();
$pid;

if (!pid) {
&error("fork error");
}	
if ($pid) {
print "<br>Your message has been sent.<br>
please close your browser if you want to log out.<br>
<form action=\"mail-admin.pl\" method=\"post\">
<input type=\"hidden\" name=\"action\" value=\"main_page\">
<input type=\"hidden\" name=\"password\" value=\"$form{'password'}\">
<input type=\"submit\" value=\"Back to the admin main page\">
</form>
";
exit;
}
else {
close (STDOUT);
}
$form{'subject'}=~ s/&quot;/"/ig;
$form{'message'}=~ s/&quot;/"/ig;
$form{'subject'}=~ s/&lt;/</ig;
$form{'subject'}=~ s/&gt;/>/ig;
$form{'message'}=~ s/&lt;/</ig;
$form{'message'}=~ s/&gt;/>/ig;
open (list, "<$listdata") or &error("Unable to open the data file for reading");
if ($flock eq "y") {
flock list, 2; 
}
@list=<list>;
close(list);
if ($header eq "y") {
open (HEADER, "<header.txt") or &error("Unable to open the header file for reading");
if ($flock eq "y") {
flock HEADER, 2; 
}
@header=<HEADER>;
close(HEADER);
}
if ($footer eq "y") {
open (FOOTER, "<footer.txt") or &error("Unable to open the header file for reading");
if ($flock eq "y") {
flock FOOTER, 2; 
}
@footer=<FOOTER>;
close(FOOTER);
}
foreach $list (@list) {
chomp ($list);
open (MAIL, "|$mailprog") || &error("Can't open the mail program!");
print MAIL "To: $list\n";
print MAIL "From: $yourmail\n";
print MAIL "Subject: $form{'subject'}\n\n";
if ($header eq "y") {
print MAIL "@header";
print MAIL "\n\n";
}
print MAIL "$form{'message'}\n\n";
if ($footer eq "y") {
print MAIL "@footer";
}
close (MAIL);
}		
exit;
}	
	
################check password
sub vpassword{
if (!$ENV{'REMOTE_HOST'}) {
$IP=$ENV{'REMOTE_ADDR'};
}
else {
$IP=$ENV{'REMOTE_HOST'};
}
open (PASS,"pass.dat") || &error("Unable to open the password file"); 
if ($flock eq "y") {
flock PASS, 2; 
}
$pass = <PASS>;
close(PASS);
$form{'password'}=~ tr/A-Z/a-z/;
$pass2 = crypt($form{'password'}, "MM");
unless ($pass eq "$pass2") {
$timenow=localtime();
print "Incorrect logon. Use your back button to try again.<br>";
print "The password you entered is incorrect.<br>";
print "The following information has been sent to the webmaster of the web site<br>";
print "Your Information: <ul>$IP</ul>";
print "<ul>Password: $form{'password'}</ul>";
print "<ul>Time: $timenow</ul>";
print "</body></html>";
 
if ($alert eq "y") {       
open (MAIL, "|$mailprog -t") or &error("Unable to open the mail program");
print MAIL "To: $yourmail\n";
print MAIL "From: $yourmail\n";
print MAIL "Subject: bad password\n";
print MAIL "Just a quick note to let you know that someone\n";
print MAIL "entered the wrong password for entering the mailing list admin script.\n";
print MAIL "Here are the information:\n\n";
print MAIL "$ENV{'REMOTE_ADDR'}\n";
print MAIL "Password: $form{'password'}\n";
print MAIL "$timenow\n";
close(MAIL);
exit;
}      
exit;
}
}	

###############error alert
sub error{
print "An error has been occured. The error is: $_[0]<br>\n";
print "<font color=\"red\">Reason: $!</font>\n";
exit;
}

