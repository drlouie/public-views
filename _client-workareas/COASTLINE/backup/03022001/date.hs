#!/usr/local/bin/perl

# Define arrays for the day of the week and month of the year.           #
@days   = ('Sunday','Monday','Tuesday','Wednesday',
           'Thursday','Friday','Saturday');
@months = ('January','February','March','April','May','June','July',
           'August','September','October','November','December');

# Get the current time and format the hour, minutes and seconds.  Add    #
# 1900 to the year to get the full 4 digit year.                         #
($sec,$min,$hour,$mday,$mon,$year,$wday) = (localtime(time))[0,1,2,3,4,5,6];
$time = sprintf("%02d:%02d:%02d",$hour,$min,$sec);
$year += 1900;

# Format the date.                                                       #
$date = "$days[$wday], $months[$mon] $mday, $year";

##return =true
1;