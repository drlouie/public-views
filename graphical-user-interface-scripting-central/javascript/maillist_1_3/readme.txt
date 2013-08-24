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


Installation:

1) If the path to perl on your server is different from 
#!/usr/local/bin/perl then you will need to change it on the first line in each script.
(maillist.pl and mail-admin.pl) 

2) Open cfg.pl with a text editor than modify the variables.


3) Upload the scripts to your cgi-bin then chmod them to "755."

4) Modify the header and footer files with a text editor. 
header.txt and footer.txt will go in the email message.
dheader.txt and dfooter.txt will be used when a visitor's email address has been added or removed.

5) Upload header.txt, footer.txt, dheader.txt, and dfooter.txt to the same directory where you uploaded the scripts. 
Then chmod them to "777."

6) Upload pass.dat and list.txt the same directory where you uploaded the scripts. 
Then chmod them to "777."

7) Execute the admin script (mail-admin.pl) with your browser (Point to url to main-admin.pl). 
The script will ask you to set up your admin password. 

8) copy and paste the tags below then paste them on your html document.

<table border="0">
<tr><td>
<form action="cgi-bin/list/maillist.pl" method="post">
<b>Email:</b> <input type="text" name="address" size="20" maxlength="50"><br>
<b>Subscribe</b><input type="radio" name="action" checked value="subscribe">
<b>Unsubscribe</b><input type="radio" name="action" value="unsubscribe">
<br><input type="submit" value="GO!">
</form>
</td></tr>
</table>


9) Done.

!!Important!!
All of the script files and data files have to be uploaded in "ASCII" mode or you will always get a 500 server error while accessing the program.

