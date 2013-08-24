SPAds © File Uploader © v1.0
Copyright 1999 / 2000 All Rights Reserved
Written by: V. Creazzo  email: vcreazzo@spads.com
http://www.spads.com
http://www.2010ad.com  (mirror)

README.TXT

PRODUCT INFORMATION:
SPAds © File Uploader © v1.0

File upload using cgi-lib.pl, can upload images only (.gif or .jpg)
or all types of files. Use with caution! 

It does have an option to exclude .exe .dll and .bat files

I Wrote this little upload program to demonstrate how to use cgi-lib.pl
written by: Steven E. Brenner (Do Not Edit) Copyright (c) 1993-1998 ) 

In order to make it work on Windows NT I had to change a forward slash / to a
double back slash \\ in The multipart section of his script. 

The file called ucgi-lib.pl is the original and should be used if your on a 
Unix Server. just, rename the cgi-lib.pl to wcgi-lib.pl and then rename the 
ucgi-lib.pl to cgi-lib.pl .

The way it stands now it will auto detect if windows is present and put the right
forward / slash or backward double slashs \\ in the right place.

if you need more assistance, contact me at 303 697-4100 9am to 6pm mountain time.

Setup Instructions:
-------------------------------------------------------------------------

There are a few things that you have to change in the configuration section,
The changes are simple, and reflect your site's address, and file upload 
directory location, etc.

Below are the names of the Program files and were they go on your site.

__These files go in your ROOT directory__

# These pages need to be edited to correct the paths to the program scripts!

IE; 
<form method="POST" enctype="multipart/form-data" action="cgi-bin/uploader.pl">

upform.htm     = This is the upload form page (edit as needed )

__Upload files go in a directory called IMAGES, in your ROOT directory__

All the image files that will be uploaded, will go in here. you need to create
and for Unix you need to chmode it to 777

__These files go in your CGI directory__
be sure to copy all of these files into your CGI directory (unix chmod 755)

uploader.pl   = main program file

cgi-lib.pl    = (Do Not Edit - written by: Steven E. Brenner  Copyright (c) 1993-1998 )

cgi-lib.pl written by: Steven E. Brenner (Do Not Edit) Copyright (c) 1993-1998 ) 
you should always download his latest version yourself, and it is provided here just 
for completeness and demonstration purposes. Thanks Steve!

ucgi-lib.pl    = (rename this file to cgi-lib.pl - if your using Unix - )

__The uploaded files go in a directory called IMAGES in your root directory__

All the image files that will be uploaded, will go in here. you need to create
and for Unix you need to chmode it to 777

__All of the files below have to edited to reflect there new location path__

Important Note: The very first line of every program script (at the very top) you will see,
#!/usr/bin/perl   -  you have to change this to point to your servers perl program, IE;
#!/usr/local/bin/perl -  or something like that. if your not sure were it is, ask your ISP.

Note: if using Window NT you don't have to worry about the above!

#################################################################
# flush the buffers
$|=1;
# find if it is a windows operating system
if ( ($^O eq 'MSWin32') || defined($ENV{'OS'}) ) {
      # this one for windows
      $windows = "Yes";
      $dpath = "$ENV{'PATH_TRANSLATED'}";
      $dpath =~ s/\\uploader\.pl$//g;
      $slash = '\\';
}else{
      # this one for unix type
      $windows = "No";
      $dpath = "$ENV{'SCRIPT_FILENAME'}";
      $dpath =~ s/\/uploader\.pl$//g;
      $slash = '/';
}

push (@INC, "$dpath");

# eval required 
eval {
# assign required file needed to upload the images
$required = 'cgi-lib.pl';

# load required file
require("$dpath$slash$required");
};
if ($@) { &error("Can't Find Required: $required file!<br>$@ <br>$! <br>$dpath <br>This file is needed to upload files!"); }

# Do not edit the above
#################################################################
# BELOW ARE VARIABLES, THAT YOU CHANGE TO SUIT YOUR SITE.       #
#################################################################

# Upload directory use machine path here, Unix use forward / slashs
$imagedir = "\\inetpub\\wwwroot\\yourdirectory\\images";

# home url or redirect url
$home = "http://www.yourdot.com/index.html";

# http:// path to upload directory
$image_dir = "http://www.yourdot.com/images";

# background image for program
$bkimg = "http://www.yourdot.com/images/1white.jpg";

# mail link for error messages
$mail_link = '<a href=mailto:webmaster@yourdot.com>Webmaster</a>';

# allow all files for upload or images only 
$images_only = "Yes";    # options Yes or No

# allow executables to be uploaded, use extreme caution, leave at No 
$exe_files = "No";       # options Yes or No

# when back button is pressed, -1 back to upload form -2 before form
$back = (-1);    # options -1 or -2

# referer allows addresses listed here only, and prevents others from using
# the program - replace yourdot.com and IP numbers to match your site 

@referers = ('yourdot.com', '209.235.84.30');

# Check Referring URL
&check_url();

####################### End of Config Section ########################
-------------------------- End of Configuration Section ----------------------------

List of your HTML pages addresses:

http://www.yourdot.com/upform.htm     = Main upload Page


If you run into problems, Please write down what error message that you are getting
along with any other messages and Email me at, vcreazzo@spads.com and I'll try to help!


Contact: vcreazzo@spads.com
Thanks, enjoy!

 

