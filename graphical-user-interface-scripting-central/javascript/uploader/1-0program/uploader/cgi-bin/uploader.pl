#!/usr/bin/perl
# SPAds File Uploader v1.5 COPYRIGHT 1999 - 2000
#################################################################
#  SPAds (c)  Uploader.pl v1.5     written by: Vince Creazzo    #
# 	                                 vcreazzo@spads.com     #
#        COPYRIGHT NOTICE   Smart Product Ads (c) SPAds (c)     #
# 	 Copyright 1997 / 1998 /1999 All Rights Reserved.     	#
#              SPAds (c) File Uploader (c) v1.5                 #
# 	THIS PROGRAM SCRIPT IS NOT FREEWARE!        11/19/99    #
#	SEND ALL INQUIRES TO:           Current Price $19.95    #
#                                                            	#
# 	         SPAds (c) World Of Perl                   	#
#	         5500 SO. SIMMS PMB 210            	        #
#	         LITTLETON, COLORADO 80127                   	#
# 	    (303) 697-4100  FAX (303) 697-4100  	        #
#                                                            	#
#       COPYRIGHT AND LICENSE AGREEMENT.                     	#
# 	REDISTRIBUTION OF THIS SCRIPT OR ANY MODIFICATIONS   	#
# 	OF THIS SCRIPT IN ANY FORM IS STRICTLY PROHIBITED!   	#
#       IF YOU REGISTER (PAY FOR) IT, YOU CAN MODIFY IT!        #
#                                                            	#
# 	There are no warranties expressed or implied of any  	#
# 	kind, and by using this code you agree to indemnify  	#
# 	Vincent Creazzo and SPADS & Company, from any and all  	#
# 	liability that might arise from it's use. Liability -	#
#       Where Applicable: In any and all cases, liability shall #
#       be limited to, but not exceed the amount of purchase.   #
# 	(c) 1999 Vince Creazzo                               	#
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
require("$required");
};
if ($@) { &error("Can't Find Required: $required file!<br>$@ <br>$! <br>$dpath <br>This file is needed to upload files!"); }

# Do not edit the above
#################################################################
# BELOW ARE VARIABLES, THAT YOU CHANGE TO SUIT YOUR SITE.       #
#################################################################

# Upload directory use machine path here, Unix use forward / slashs
$imagedir = "\\users\\yourdirectory\\images";

# home url or redirect url
$home = "http://www.yourdot.com/index.html";

# http:// path to upload directory
$image_dir = "http://www.yourdot.com/images";

# mail link for error messages
$mail_link = '<a href=mailto:webmaster@yourdot.com>Webmaster</a>';

# allow all files for upload or images only 
$images_only = "Yes";    # options Yes or No

# allow executables to be uploaded, use extreme caution, leave at No 
$exe_files = "No";       # options Yes or No

# Check and test Image file for validity Set to No,
# if you have problems uploading digital camera jpg images
$images_check = "No";    # options Yes or No   

# maximum upload file size in kb
$max_filesize = '131072'; 

# here you can set or add your background image, colors, text, etc.
$body = "<body background=\"/images/1white.jpg\" bgcolor=\"#ffffff\" text=\"#0000AD\">";

# when back button is pressed, -1 back to upload form -2 before form
$back = (-2);    # options -1 or -2

# referer allows addresses listed here only, and prevents others from using
# the program - replace yourdot.com and IP numbers to match your site 

@referers = ('yourdot.com', '209.235.84.30');

# Check Referring URL
&check_url();

####################### End of Config Section ########################
binmode(STDIN);              # we need these for DOS-based systems
binmode(STDOUT);             # and they shouldn't hurt anything else 
binmode(STDERR);

MAIN: {
  my (%cgi_data, %cgi_cfn, %cgi_ct, %cgi_sfn, $ret, $buf);

  # Spool the files to the desired directory
  $cgi_lib::writefiles = "$imagedir";   

  $cgi_lib::filepre = "TMP";

  # Limit upload size to avoid using too much memory 
  $cgi_lib::maxdata = $max_filesize; 

  # Start off by reading and parsing the data.  Save the return value.
  # Pass references to retreive the data, the filenames, and the content-type
  $ret = &ReadParse(\%cgi_data,\%cgi_cfn,\%cgi_ct,\%cgi_sfn);

  # Note that $cgi_data is the rest of the forms data if any to pass along
  # and would look like this $cgi_data{'name'} or $cgi_data{'address'} etc.
  # you would have to add code to handle these fields, this program was written
  # to handle only one uploaded file as an example, you would have to modify it
  # to do more files or to handle additional fields etc. 

  # check to see if image directory is vaild and premissions are ok
  if ( !(-e $imagedir) || !(-W $imagedir) || !(-d $imagedir) ) {
      &error("Bad Directory Name or you need to set it's permissions to ( rwx ).");
      exit(0);
  }
  # check for errors
    if (!($cgi_cfn{'upfile'})) { 
        &error("You forgot to select a file to upload!");
    }
    elsif (!(defined $ret)) {
        &error("Error in reading and parsing of form input: $!");
    } 
    elsif (!$ret) { &error("Missing parameters: $!");
    }
    else { # lets check the file name for errors and get only the name
           # This will remove spaces and replace with an unline
           $cgi_cfn{'upfile'}  =~ s/^\s+/_/;

	   if ($cgi_cfn{'upfile'} =~ /([^\/\\]+)$/) {
		    $file_name = $1;
		    $file_name =~ s/^\.+//;

	   }else { # assign file name for error message
		   $problem_file = $cgi_cfn{'upfile'};

                   # delete temp uploaded file
                   unlink ($cgi_sfn{'upfile'});

                   # send user error message
		   &error("Bad File Name: $problem_file, File Name Can't Have A Slash In It!<br> Please Rename It And Try Again!");
		   exit(0);
	    }
            unless ($exe_files eq "Yes") {
                if( ($file_name =~ /^.+(\.exe)$/i) || ($file_name =~ /^.+(\.dll)$/i) || ($file_name =~ /^.+(\.bat)$/i) ) {
                   # assign file name for error message
		   $problem_file = $file_name;

                   # delete temp uploaded file
                   unlink ($cgi_sfn{'upfile'});

                   # send user error message
		   &error("Executable File: <b>$problem_file</b>, Not Allowed On This Server!<p> <b>Please Do Not Try It Again!</b> <br> Offenders IP Address: $ENV{'REMOTE_ADDR'} ");
		   exit(0);
	        }
            }
         # when server uploads the file it assigns a new name
         # to the file which is handled in cgi-lib.pl  the
         # servers temp name for the file is in $cgi_sfn{'upfile'}
         $up_image = $cgi_sfn{'upfile'};

         if ($images_only eq "Yes") {
             if ($images_check eq "No") {
                 if($file_name =~ /^.+(\.jpg)$/i) { 
                       $up_file = $file_name;
                 }
                 elsif($file_name =~ /^.+(\.gif)$/i) { 
                       $up_file = $file_name;
                 }
                 else{ # delete temp uploaded file
                       unlink ($cgi_sfn{'upfile'});

                       # send user error message
                       &error("The file: <b>$file_name</b> you tried to upload,<br>is not a valid .jpg or .gif file.<br>Please Check the file and try again!");
	              exit(0);
                 }
             }else{
             # lets find out if it is an image file
             $status = &get_image_type($up_image);

                if ($status eq "gif") { $up_file = $file_name; 
                }
                 elsif ($status eq "jpg") { $up_file = $file_name;
                 }
                  elsif ($status eq "unk") {
                      # delete temp uploaded file
                      unlink ($cgi_sfn{'upfile'});

                      # send user error message
                      &error("The file: <b>$file_name</b> you tried to upload,<br>is not a valid .jpg or .gif file.<br>Please Check the file and try again!");
	              exit(0);
                  }
              }
         }else {
                 # original name of the file
                 $up_file = $file_name;
          }
         # Check to see if the file name all ready exists we don't want to over write any files
         if (-e "$imagedir$slash$file_name") {
             # delete temp uploaded file
             unlink ($cgi_sfn{'upfile'});

             # send user error message
             &error("Bad File Name: <b>$file_name</b>, This File Name All Ready Exists!<br> Please Rename It And Try Again!");
	     exit(0);
         }
         # lets do the magic
         if ($windows eq "Yes") {
               # set up the path to the upload directory and add original name
    	       $path_image = "$imagedir$slash$up_file";

               # copy the uploaded file to its original name
               system("copy $up_image $path_image");
         }else{
               # set up the path to the upload directory and add original name
    	       $path_image = "$imagedir$slash$up_file";

               # link the uploaded file to its original name
               link($up_image, $path_image);
          }
               # delete the servers temp uploaded file
               unlink ("$cgi_sfn{'upfile'}");

              # send the user acknolgement
              &success($up_file);
    }

} # end of Main
################### SUBROUTINES START HERE ###################
# HTML Header
sub html_header {
    my ($msg_title) = @_;

print "content-type: text/html\n\n";  # Print the header
	print <<"__END_HTML__";

<HTML><HEAD><TITLE>$msg_title</TITLE></HEAD>
$body
<center><font size=7>SPADS - World of Perl</font></center>
<HR width="80%">
<CENTER>
<table width="482" bordercolor="#222222" border="1" cellpadding="1" cellspacing="2" bgcolor="#777777">
<tr><td bgcolor="#999999"> 		
<table width="480" border="0" cellpadding="8" cellspacing="4" bgcolor="#ffffff">
<tr><td bgcolor="#333388" width="100%" height="30"><center><font size="3" color="#ffffff"><b>$msg_title</b></font></center></td></tr>
<tr><td bgcolor="#ffffff" align="center"><font face="Comic Sans MS" size="2"><p>

__END_HTML__

}
sub html_footer {

print <<"__END_HTML__";
</FONT>
</td></tr>
<tr><td align="center">
<TABLE width="70%" border=0 cellpadding=2 cellspacing=0><TR>
<TH><FORM><INPUT TYPE="button" VALUE="BACK" onClick="history.back($back); return false;"></FORM></TH>
<TH><FORM ACTION="$home" Method="GET"><INPUT TYPE="submit" VALUE="HOME"></FORM></TH>
</TR></TABLE>
</td></tr></table></td></tr></table>
<HR width="80%">
<p><b><font face="Arial, Helvetica" size="1">&copy; copyright 1999 / 2000, <a href="http://www.spads.com">SPAds &copy;</a>  File <i>Uploader</i> &copy; v1.5</font></b>
</center>
</BODY></HTML>

__END_HTML__

}# end of sub
# Error message
sub error { 
	my ($errormsg) = @_;

        &html_header("ERROR!");
        print "<p>\n";
        print "There was an error processing your request.<p>\n";
        print "The Error: $errormsg <br> $! <p>\n";
        print "If you require assistance. Please contact the $mail_link.<p>\n";
        &html_footer;
  exit(0);
}# end of sub
# Success message
sub success {
	my ($up_file) = @_;
	if ($images_only eq "Yes") {
	       $new_file = "<img src=\"$image_dir/$up_file\">";
	}else {
	       $new_file = "View Uploaded File: <a href=\"$image_dir/$up_file\">$up_file</a>";
	}
        &html_header("SUCCESS!");
        print "<p>\n";
        print "Your file was uploaded successfully!<p>\n";
        print "Your File: <b>$up_file</b><p> $new_file <p>\n";
        print "Thank You!<br>\n";
        &html_footer;

exit(0);
}# end of sub
###########################################################
# This subroutine was created by the one and only         #
# #42 - aka - Jim Phillips. It opens the uploaded file    #
# and reads a little of it, and then closes it. It then   #
# attempts to determine if it is an image file of either  # 
# type .jpg or .gif and returns a three char string of    #
# either "jpg" "gif" or "unk" for unknown. Which we can   #
# then decide if the file is one that we can use or       #
# destroy it as a potential hazard!                       #
###########################################################
sub get_image_type 
    {
    my ($fut) = @_;  # File Under Test
    my ($gifid, $jpgid, $gifflg, $jpgflg, $retval, $nn, $xx, $ofs);
    open (INSND, "<$fut") or return ($retval='unk'); 
    read (INSND, $xx, 15) or return ($retval='unk');
    close INSND;
    $gifid = '474946383961000000000000';
    $jpgid = 'ffd8ffe000104a4649460001';
    $gifflg = 'T';
    $jpgflg = 'T';
    $retval = 'unk';
    for ($ofs=0; $ofs < 12; $ofs++)
        {
        $nn = unpack ("H2", substr($xx, $ofs, 1)); # Get both hex nybbles 'H2'
        if ($ofs < 6) 
            {
            if ($nn ne substr($gifid, ($ofs * 2), 2)) {$gifflg = 'F';}
            }
        if ($nn ne substr($jpgid, ($ofs * 2), 2)) {$jpgflg = 'F';}
        # this line is for testing jpgid accuracy print "$nn,$gifflg$jpgflg ";
        }
    if ($gifflg eq 'T') {$retval = 'gif';}
    if ($jpgflg eq 'T') {$retval = 'jpg';}
    return $retval;

} # end of sub
####### Check to see if another site is trying to use the program ########
sub check_url {
    local($check_url) = 0;

    if ($ENV{'HTTP_REFERER'}) {
        foreach $referer (@referers) {
            if ($ENV{'HTTP_REFERER'} =~ m|https?://([^/]*)$referer|i) {
                $check_referer = 1;
                last;
            }
        }
    }
    else {
        $check_referer = 1;
    }
    # If the referer was invalid, send error.
    if ($check_referer != 1) { &error("Bad Referer - $ENV{'REMOTE_HOST'} - $ENV{'REMOTE_ADDR'} <br> - Access Denied -"); 
    }
} # end of sub

###### The following lines are solely to suppress 'only used once' warnings ######

  $cgi_lib::maxdata = $cgi_lib::maxdata;
  $cgi_lib::filepre  = $cgi_lib::filepre;
  $cgi_lib::writefiles = $cgi_lib::writefiles;

