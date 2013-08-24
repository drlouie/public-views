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
$value =~ s/\n/ /g;
$form{$name} = $value;
}

################################# actions

print "Content-type: text/html\n\n";
$count=0;
if ($form{'action'} eq "subscribe") {
&subscribe;
exit;
}

if ($form{'action'} eq "unsubscribe") {
&unsubscribe;
exit;
}


else {
print "Access Denied";
exit;
}

######################################### subscribe

sub subscribe {
	
###search the data to see if the address is already in the database


if ($form{'address'}=~ tr/;<>*|`&$!#()[]{}:'"//) {
&dheader;
print "<h2>Unable to subscribe your email address</h2>\n"; 
print "Please don't use weird symbols<br>\n";
print "Please click <a href=\"$main_page\">here</a> to return to our main page.<br>\n";
&dfooter;
exit;
}

unless ($form{'address'}=~/.*\@.*\..*/)   { 
&dheader;
print "<h2>Unable to subscribe your email address</h2>\n"; 
print "You've entered an invalid email address.<br>\n";
print "Please click <a href=\"$main_page\">here</a> to return to our main page.<br>\n";
&dfooter;
exit;
}
	
open (list, "<$listdata") or &error("Unable to open the data file for reading");
if ($flock eq "y") {
flock list, 2; 
}
@list=<list>;
close(list);
	
foreach $list(@list) {
if ($list =~ /$form{'address'}/i) {
&dheader;
print "<h2>Unable to subscribe your email address</h2>\n"; 
print "Sorry, this email address \"$form{'address'}\" is already in the database<br>\n";
print "Please click <a href=\"$main_page\">here</a> to return to our main page.<br>\n";
&dfooter;
exit;
}
}

#######add the address	
	
open (data, ">>$listdata") or &error("Unable to open the data file for writing");
if ($flock eq "y") {
flock data, 2; 
}
print data "$form{'address'}\n";
close(data);
&dheader;	
print "<br>Thank you, your email address has been added<br>\n";
print "Please click <a href=\"$main_page\">here</a> to return to our main page.<br>\n";
&dfooter;
exit;	
}

#######unsubscribe


sub unsubscribe {
	
###search the data to see if the address is already in the database then remove

if ($form{'address'}=~ tr/;<>*|`&$!#()[]{}:'"//) {
&dheader;
print "<h2>Unable to unsubscribe your email address</h2>\n";
print "Please don't use weird symbols\n";
print "Please click <a href=\"$main_page\">here</a> to return to our main page.<br>\n";
&footer;
exit;
}
unless ($form{'address'}=~/.*\@.*\..*/)   {
&dheader;
print "<h2>Unable to unsubscribe your email address</h2>\n"; 
print "You've entered an invalid email address.<br>\n";
print "Please click <a href=\"$main_page\">here</a> to return to our main page.<br>\n";
&dfooter;
exit;
}

open (list, "<$listdata") or &error("Unable to open the data file for reading");
if ($flock eq "y") {
flock list, 2; 
}
@list=<list>;
close(list);
	
foreach $list(@list) {
$count++;
if ($list =~ /$form{'address'}/i) {
$count--;
splice(@list, $count, 1);
open (wlist, ">$listdata") or &error("Unable to open the data file for writing");
if ($flock eq "y") {
flock wlist, 2; 
}

print wlist @list;
	
close(wlist);
&dheader;
print "<br>\"$form{'address'}\" was removed from the database successfully.<br>\n";
print "Please click <a href=\"$main_page\">here</a> to return to our main page.<br>\n";
&dfooter;
exit;
}
}
&dheader;
print "<br>\"$form{'address'}\" was not found in the database.<br>\n";
print "Please click <a href=\"$main_page\">here</a> to return to our main page.<br>\n";
&dfooter;
}

######################header input
sub dheader {
open (dheader, "<dheader.txt") or &error("Unable to open the dheader file");
if ($flock eq "y") {
flock dheader, 2; 
}
@dheader=<dheader>;
close(dheader);
print @dheader;
}
####################footer input
sub dfooter {
open (dfooter, "<dfooter.txt") or &error("Unable to open the dfooter file");
if ($flock eq "y") {
flock dfooter, 2; 
}
@dfooter=<dfooter>;
close(dfooter);
print @dfooter;
}
############################error alert

sub error{
print "An error has occured, the error is: $_[0]<br>\n";
print "<font color=\"red\">$!</font>\n";
exit;
}

		
		

	
	
	