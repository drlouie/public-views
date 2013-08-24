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

require("parse_query.cgi");

print "Content-type: text/html \n\n";

$FORM{'pagina'} = $FORM{'pid'};

require("getPage.cgi");

## script for document lower date

##return =true
exit;