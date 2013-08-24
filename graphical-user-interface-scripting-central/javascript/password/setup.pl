#!/usr/local/bin/perl


       ########################################################### 
       # User Password Redirect Script                           #
       # Script name - setup.pl                                  #
       # Written by Ranson Johnson - Email  ranson@rlaj.com      #
       # Version 1.2                                             #
       # Copyrite 1997 Ranson Johnson all right s reserved       #
       ###########################################################

                 ### *** chmod this file to 755 *** ###



                    ### *** SETUP INFORMATION *** ###

# 1. configure the variables in this file below for your server
# 2. place the .cgi's the setup.pl and password.log in your cgi-bin
# 3. add users by accessing the adduser.cgi with your browser
# 4. login to the system by accessing the login.cgi with your browser
# 5. change the <Form method=POST action="/cgi-bin/login.cgi"> tag
#    in the login.htm to point to the login.cgi
#
# Done!

                         ### *** *** ###


# Enter your server type    # 0 = Unix
                            # 1 = NT or win95
$ServerType = '0';

# Enter a Default URL to send user to in case of lookup error
$Default_URL = 'http://www.danhausen.com/client/loginerror.html';

# Enter the title for the login page
$title = 'Danhausen Client Login';

# Enter the path to the main log ( if you want a log file )
# Logs the username and the date they loged in
$mainlog_path = 'main.log';

# Enter the path and name of the password file
$passwordFile = 'password.log';

                         ### *** DONE *** ###

