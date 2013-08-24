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
# address. If you have any trouble installing this program. 
# Please feel free to post a message on our CGI Support Forum.
# Selling this script is absolutely forbidden and illegal.
##################################################################
#
#               COPYRIGHT NOTICE:
#
#         Copyright 1999 CGI-Factory.com 
#
#      Author:  Yutung Liu
#      Web site: http://www.cgi-factory.com
#      E-Mail: cgifactory@cgi-factory.com
#      Released Date: August 28, 1999
#	
#   Mailing List V1.3 is protected by the copyright 
#   laws and international copyright treaties, as well as other 
#   intellectual property laws and treaties.
###################################################################
$mailprog="/usr/lib/sendmail -t";
#the system path to your mail program

$listdata="list.txt";
#the file name of the data file. You need to create this file and upload it to your server. Then chmod it to 777.

$main_page="http://www.yourname.com/maillist/";
#main page url. 

$yourmail="your\@name.com";
#your email. don't forget the back slash - \ 

$alert="n";
#send an alert mail to you if someone enters a wrong password

$header="y";
#Set this variable to n if you want to turn the header text off 
#It is the header for the email message, not the html pages

$footer="y";
#set this variable to n if you want to turn the footer text off
#It is the footer for the email message, not the html pages

$flock="y";
###file locking. Don't change it to n unless your system has trouble using file locking.