#!/usr/local/bin/perl -w

#######################################################################################################
# Company: NetMedia Solutions                                                                         #
# Date: Saturday, September 21, 2001                                                                  #
# Location: Los Angeles, California, United States of America                                         #
# Made By: Luis Rodriguez (drlouie)                                                                   #
# Email: drlouie@tstonramp.com                                                                        #
#                                                                                                     #
# USNightVision.com's dynamic date generator. Dynamically driven by DHTML, HTML, Perl and MySql      #
#                                                                                                     #
#######################################################################################################

print "Content-type: text/html \n\n";

# Define arrays for the day of the week and month of the year.           #
@days   = ('Sunday','Monday','Tuesday','Wednesday',
           'Thursday','Friday','Saturday');

@months = ('January','February','March','April','May','June','July',
           'August','September','October','November','December');

use locale;

@months2 = ('1','2','3','4','5','6','7','8','9','10','11','12');

@months3 = ('01','02','03','04','05','06','07','08','09','10','11','12');

# Get the current time and format the hour, minutes and seconds.  Add    #
# 1900 to the year to get the full 4 digit year.                         #
($sec,$min,$hour,$mday,$mon,$year,$wday) = (localtime(time))[0,1,2,3,4,5,6];
$time = sprintf("%02d:%02d:%02d",$hour,$min,$sec);
$year += 1900;


$days[$wday] = uc($days[$wday]);
$months[$mon] = uc($months[$mon]);

# Format the date.                                              #
$date = "$days[$wday] $months[$mon] $mday, $year";

## script for document lower date
print "if (document.getElementById) { document.getElementById('dater').innerHTML = '$date' };";

##return =true
exit;