#!/usr/local/bin/perl -w

#######################################################################################################
# Company: NetMedia Solutions                                                                         #
# Date: Saturday, September 21, 2001                                                                  #
# Location: Los Angeles, California, United States of America                                         #
# Made By: Luis Rodriguez (drlouie)                                                                   #
# Email: drlouie@tstonramp.com                                                                        #
#                                                                                                     #
# CoastlineMicro.com's dynamic query/input parser. Dynamically driven by DHTML, HTML, Perl and MySql  #
#                                                                                                     #
#######################################################################################################

    if ($ENV{'REQUEST_METHOD'} eq 'GET') {
        # Split the name-value pairs
        @pairs = split(/&/, $ENV{'QUERY_STRING'});
    }
    elsif ($ENV{'REQUEST_METHOD'} eq 'POST') {
        # Get the input
        read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
 
        # Split the name-value pairs
        @pairs = split(/&/, $buffer);
    }
    else {
        ##return =false
		0;;
    }

    foreach $pair (@pairs) {

        # Split the pair up into individual variables.                       #
        local($name, $value) = split(/=/, $pair);
 
        # Decode the form encoding on the name and value variables.          #
        $name =~ tr/+/ /;
        $name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

        $value =~ tr/+/ /;
        $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

        # If they try to include server side includes, erase them, so they
        # aren't a security risk if the html gets returned.  Another 
        # security hole plugged up.
        $value =~ s/<!--(.|\n)*-->//g;

            if ($FORM{$name} && $value) {
                push(@Todo_Form,"$name-----$value");

                $FORM{$name} = "$FORM{$name}, $value";
            }
            elsif ($value) {
                push(@Todo_Form,"$name-----$value");

                push(@Field_Order,$name);
                $FORM{$name} = $value;
           }

    }

##return =true
1;
