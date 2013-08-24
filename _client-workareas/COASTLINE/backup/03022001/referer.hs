#!/usr/local/bin/perl

##########################################################
##Check for referer, if not user is  jumped to Home Page #
##########################################################
@referers = ('www.coastlinemicro.com','coastlinemicro.com');

&check_url;

sub check_url {

    # Localize the check_referer flag which determines if user is valid.     #
    local($check_referer) = 0;

    # If a referring URL was specified, for each valid referer, make sure    #
    # that a valid referring URL was passed to FormMail.                     #

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

    # If the HTTP_REFERER was invalid, send back an error.                   #
    if ($check_referer != 1) { &bad_referer; }
}

sub bad_referer {

print "Location: index.html\n\n";

exit;
}
####################
##End Check Referer#
####################
##return =true
1;