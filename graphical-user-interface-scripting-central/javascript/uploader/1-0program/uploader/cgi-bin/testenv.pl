#!/usr/bin/perl
#################################################################
#  SPAds (c)  testenv.pl v1.5     written by: Vince Creazzo     #
# 	                                 vcreazzo@spads.com     #
#        COPYRIGHT NOTICE   Smart Picture Ads (c) SPAds (c)     #
# 	 Copyright 1997 - 2000    All Rights Reserved.    	#
#             SPAds (c) -  Enviroment Report v1.5               #
#                                                            	#
#	 SEND ALL INQUIRES TO:                                  #
#                                                            	#
# 	        SPAds (c) / World of Perl                   	#
#	        5500 SO. SIMMS PMB Suite 210                    #
#	        LITTLETON, COLORADO 80127                   	#
# 	    (303) 697-4100  FAX (303) 697-4100  	        #
#                                                            	#
#       COPYRIGHT AND LICENSE AGREEMENT.                       	#
#                                                            	#
# 	There are no warranties expressed or implied of any  	#
# 	kind, and by using this code you agree to indemnify  	#
# 	Vincent Creazzo and SPADS and Company from any and  	#
# 	all liability that might arise from it's use.           #
# 	(c) 1999 Vince Creazzo                               	#
#################################################################
# 	This script has been tested with Perl 5 build 315    	#
# 	windows nt 4.0, Unix and should work on any server     	#
#	that supports perl 5 build 300 + or higher.          	#
#################################################################
# flush the buffers
$| = 1;
# find out if it is windows OS 
if ($^O eq 'MSWin32' || $ENV{'OS'} eq 'Windows_NT') {
      # this one for windows
      $dpath = "$ENV{'PATH_TRANSLATED'}";
      $dpath =~ s/\\testenv\.pl$//g;
      $windows = 'Yes';
}else{
      # this one for unix type
      $dpath = "$ENV{'SCRIPT_FILENAME'}";
      $dpath =~ s/\/testenv\.pl$//g;
      $windows = 'No';
}

push (@INC, "$dpath");

print "Content-type: text/html\n\n";

  print <<"__END_HTML__";
  <html><head>
  <title>SPAds &copy; - Enviroment Report v1.01</title>
  </head><body bgcolor="#ffffee"><center>
  <table width="95%" cellpadding=0  cellspacing=3 bgcolor="#888888">
  <TR><TH bgcolor="#800040"><font face="Arial Bold" size=5 color="WHITE"><i>SPAds</i> &copy; - Enviroment Report v1.5 </font></TH></TR>
  <TR><TD>
  <table width="100%" cellpadding=4 cellspacing=1 bgcolor="#cccccc">

__END_HTML__

# Print out all the environment variables
while(($key, $value)=each(%ENV)){
   print "  <TR><TD width=\"25%\" valign=\"top\" align=\"right\" bgcolor=\"#EEEEEE\"><font face=\"Arial Narrow\" size=2 color=\"NAVY\"><b> $key:</b> </font></TD><TD valign=\"top\" bgcolor=\"#FFFFFF\"><font face=\"Arial bold\" size=2 color=\"MAROON\"> $value</font></TD></TR>\n";
}

  print <<"__END_HTML__";
  <TR><TD width="25%" valign="top" align="right" bgcolor="#EEEEEE"><font face="Arial Narrow" size=2 color="NAVY"><b>PUSH PATH:</b> </font></td><TD valign="top" bgcolor="#FFFFFF"><font face="Arial bold" size=2 color="MAROON">$dpath </font></td></TR>

  <TR><TD width="25%" valign="top" align="right" bgcolor="#EEEEEE"><font face="Arial Narrow" size=2 color="NAVY"><b>PERL_BINARY:</b> </font></td><TD valign="top" bgcolor="#FFFFFF"><font face="Arial bold" size=2 color="MAROON">$^O </font></td></TR>
  <TR><TD width="25%" valign="top" align="right" bgcolor="#EEEEEE"><font face="Arial Narrow" size=2 color="NAVY"><b>PERL_VERSION: </b></font></td><TD valign="top" bgcolor="#FFFFFF"><font face="Arial bold" size=2 color="MAROON">$] </font></TD>
  <TR><TD width="25%" valign="top" align="right" bgcolor="#EEEEEE"><font face="Arial Narrow" size=2 color="NAVY"><b>PERL_LOCATION:</b> </font></td><TD valign="top" bgcolor="#FFFFFF"><font face="Arial bold" size=2 color="MAROON">$^X </font></td></TR>
__END_HTML__

if ($windows eq 'No') {

@wperl = split(" ", `whereis perl`);
@wperl = sort(@wperl);

  foreach $ploc (@wperl) {

  print <<"__END_HTML__";
  <TR><TD width="25%" valign="top" align="right" bgcolor="#EEEEEE"><font face="Arial Narrow" size=2 color="NAVY"><b>PERL_LOCATION:</b> </font></td><TD valign="top" bgcolor="#FFFFFF"><font face="Arial bold" size=2 color="MAROON">$ploc </font></td></TR>
__END_HTML__
 
  }

@smail = split(" ", `whereis sendmail`);
@smail = sort(@smail);

  foreach $sloc (@smail) {

  print <<"__END_HTML__";
  <TR><TD width="25%" valign="top" align="right" bgcolor="#EEEEEE"><font face="Arial Narrow" size=2 color="NAVY"><b>SENDMAIL_LOCATION:</b> </font></td><TD valign="top" bgcolor="#FFFFFF"><font face="Arial bold" size=2 color="MAROON">$sloc </font></td></TR>
__END_HTML__
 
  }
}
eval {
$required = 'socket.pm';
require "$required";
};
  print <<"__END_HTML__";
  <TR><TD width="25%" valign="top" align="right" bgcolor="#EEEEEE"><font face="Arial Narrow" size=2 color="NAVY"><b>PERL (Use or Require) </b></font></td><TD valign="top" bgcolor="#FFFFFF"><font face="Arial bold" size=2 color="MAROON"><b>$required,</b> $@ </font></TD>
  </TR></TABLE>
  </TD></TR></TABLE>
  <blockquote><p align="left"><font color="RED"><b>Note:</b></font> If you see Can't find 'Socket.pm', This means that you have to use Sendmail instead of Sockets when using this program!</p></blockquote>
  <HR width="90%">
  <TABLE width="70%" border=0 cellpadding=2 cellspacing=0><TR>
  <TH><FORM><INPUT TYPE="button" VALUE="BACK" onClick="history.back();"></FORM></TH>
  </TR></TABLE>
  <p align="center"><font face="Arial, Helvetica" size=1><b>&copy; copyright 2000, </b><a href="http://www.spads.com">SPAds &copy;</a></font></P>
  </CENTER></BODY></HTML>

__END_HTML__

exit;

__END__
