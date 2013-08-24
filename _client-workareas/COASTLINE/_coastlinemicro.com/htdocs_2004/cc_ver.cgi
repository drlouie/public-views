#!/usr/bin/perl5 -w
#
# CC-Verify script for Visa, MasterCard, Amex and Novus Cards
# Written 29 June 1996 by Spider (spider@servtech.com)
# http://w3works.com
# http://www.servtech.com/public/spider
#
# Loosely based on a re-post of original by Melvyn Myers 
# (initial author unknown) but this revision covers all 13, 
# 15 and 16 digit cards using the Mod 10 algorithm.

##############################################################################
# COPYRIGHT NOTICE                                                           #
# Copyright 1996 Dave Paris (aka Spider)  All Rights Reserved.               #
#                                                                            #
# The Validator may be used and modified free of charge by anyone so long as #
# this copyright notice and the comments above remain intact.  By using this #
# code you agree to indemnify Dave Paris from any liability that might       #  
# arise from it's use.                                                       #  
#                                                                            #
# Selling the code for this program without prior written consent is         #
# expressly forbidden.  In other words, please ask first before you try and  #
# make money off of my program.                                              #
#                                                                            #
# Obtain permission before redistributing this software over the Internet or #
# in any other medium.  In all cases copyright and header must remain intact.#
# This Copyright is in full effect in any country that has International     #
# Trade Agreements with the United States of America.                        #
##############################################################################

# Get the input
require("parse_query.nsp");


print "Content-type: text/html\n\n";

print qq~
<script language="Javascript">
function invalid() {
	alert('Bad Credit Card Number\\n\\nThe Credit Card number you\\'ve supplied does not pass verification. Please verify that the number you\\'ve entered is correct and contains no additional characters other than spaces or hyphens.');
	parent.botOne.leConfig.SeaSeaN.focus();
	location.href='topframe.html';
}

function dataMissing() {
	alert('Missing Credit Card Information\\n\\nLooks like you\\'ve forgotten to fill in one or more of the required fields. Please try again.');
	parent.botOne.leConfig.SeaSeaN.focus();
	location.href='topframe.html';
}
</script>
</head>
<body bgcolor="#FFFFFF">
<TABLE width="100%" cellspacing ="0" cellpadding="10" border="0" valign="middle">
     <TR> 
         <TD width="100%" align="left" valign="middle"><font style="font-size:11px;font-family:verdana,arial,helvetica;color:#000000;">
~;


$FORM{'cardholder'} = "f";
if ($FORM{'SeaSeaN'} ne "" && $FORM{'SeaSeaN'} ne " " && $FORM{'SeaSeaEX'} ne "" && $FORM{'SeaSeaEX'} ne " " && $FORM{'SeaSeaT'} ne "" && $FORM{'SeaSeaT'} ne " ") {
	$FORM{'cardnumber'} = "$FORM{'SeaSeaN'}";
	$FORM{'cardexp'} = "$FORM{'SeaSeaEX'}";
	$FORM{'cardtype'} = "$FORM{'SeaSeaT'}";
}
else {
	&no_data;
}

&CC_Verify;

    
sub CC_Verify {

$cardnumber = $FORM{'cardnumber'}; 

# Remove any spaces or dashes in card number
$cardnumber =~ s/ //g;
$cardnumber =~ s/-//g;
$length = length($cardnumber);

# Make sure that only numbers exist
if (!($cardnumber =~ /^[0-9]*$/)) {
 &invalid_cc;
 }

# Verify correct length for each card type
if ($FORM{'cardtype'} eq "visa") { &vlen; }
if ($FORM{'cardtype'} eq "mastercard") { &mclen; }
if ($FORM{'cardtype'} eq "amex") { &alen; }
if ($FORM{'cardtype'} eq "novus") { &nlen; }

sub vlen {
    &invalid_cc unless (($length ==13) || ($length == 16));
}
sub mclen {
    &invalid_cc unless ($length == 16);    
}
sub alen {
    &invalid_cc unless ($length == 15);    
}
sub nlen {
    &invalid_cc unless ($length == 16);    
}

# Now Verify via Mod 10 for each one
if ($FORM{'cardtype'} eq "visa") { &vver; }
if ($FORM{'cardtype'} eq "mastercard") { &ver16; }
if ($FORM{'cardtype'} eq "amex") { &ver15; }
if ($FORM{'cardtype'} eq "novus") { &ver16; }

# pick one for Visa
sub vver {
	if ($length == 13) { &ver13; }
	if ($length == 16) { &ver16; }
}

# For 13 digit cards
sub ver13 {
        $cc0 = substr($cardnumber,0,1);
        $cc1 = substr($cardnumber,1,1);
        $cc2 = substr($cardnumber,2,1);
        $cc3 = substr($cardnumber,3,1);
        $cc4 = substr($cardnumber,4,1);
        $cc5 = substr($cardnumber,5,1);
        $cc6 = substr($cardnumber,6,1);
        $cc7 = substr($cardnumber,7,1);
        $cc8 = substr($cardnumber,8,1);
        $cc9 = substr($cardnumber,9,1);
        $cc10 = substr($cardnumber,10,1);
        $cc11 = substr($cardnumber,11,1);
        $cc12 = substr($cardnumber,12,1);

        $cc1a = $cc1 * 2;
        $cc3a = $cc3 * 2;
        $cc5a = $cc5 * 2;
        $cc7a = $cc7 * 2;
        $cc9a = $cc9 * 2;
        $cc11a = $cc11 * 2;

        if ($cc1a >= 10) {
            $cc1b = substr($cc1a,0,1);
            $cc1c = substr($cc1a,1,1);
            $cc1 = $cc1b+$cc1c;
        } else {
            $cc1 = $cc1a;
        }
        if ($cc3a >= 10) {
            $cc3b = substr($cc3a,0,1);
            $cc3c = substr($cc3a,1,1);
            $cc3 = $cc3b+$cc3c;
        } else {
            $cc3 = $cc3a;
        }
        if ($cc5a >= 10) {
            $cc5b = substr($cc5a,0,1);
            $cc5c = substr($cc5a,1,1);
            $cc5 = $cc5b+$cc5c;
        } else {
            $cc5 = $cc5a;
        }
        if ($cc7a >= 10) {
            $cc7b = substr($cc7a,0,1);
            $cc7c = substr($cc7a,1,1);
            $cc7 = $cc7b+$cc7c;
        } else {
            $cc7 = $cc7a;
        }
        if ($cc9a >= 10) {
            $cc9b = substr($cc9a,0,1);
            $cc9c = substr($cc9a,1,1);
            $cc9 = $cc9b+$cc9c;
        } else {
            $cc9 = $cc9a;
        }
        if ($cc11a >= 10) {
            $cc11b = substr($cc11a,0,1);
            $cc11c = substr($cc11a,1,1);
            $cc11 = $cc11b+$cc11c;
        } else {
            $cc11 = $cc11a;
        }

        $val = $cc0+$cc1+$cc2+$cc3+$cc4+$cc5+$cc6+$cc7+$cc8+$cc9+$cc10+$cc11+$cc12;
        if (substr($val,1,1) !=0 ) {
            &invalid_cc;
        }
	}

# For 16 digit cards
sub ver16 {
        $cc0 = substr($cardnumber,0,1);
        $cc1 = substr($cardnumber,1,1);
        $cc2 = substr($cardnumber,2,1);
        $cc3 = substr($cardnumber,3,1);
        $cc4 = substr($cardnumber,4,1);
        $cc5 = substr($cardnumber,5,1);
        $cc6 = substr($cardnumber,6,1);
        $cc7 = substr($cardnumber,7,1);
        $cc8 = substr($cardnumber,8,1);
        $cc9 = substr($cardnumber,9,1);
        $cc10 = substr($cardnumber,10,1);
        $cc11 = substr($cardnumber,11,1);
        $cc12 = substr($cardnumber,12,1);
        $cc13 = substr($cardnumber,13,1);
        $cc14 = substr($cardnumber,14,1);
        $cc15 = substr($cardnumber,15,1);

        $cc0a = $cc0 * 2;
        $cc2a = $cc2 * 2;
        $cc4a = $cc4 * 2;
        $cc6a = $cc6 * 2;
        $cc8a = $cc8 * 2;
        $cc10a = $cc10 * 2;
        $cc12a = $cc12 * 2;
        $cc14a = $cc14 * 2;

        if ($cc0a >= 10) {
            $cc0b = substr($cc0a,0,1);
            $cc0c = substr($cc0a,1,1);
            $cc0 = $cc0b+$cc0c;
        } else {
            $cc0 = $cc0a;
        }
        if ($cc2a >= 10) {
            $cc2b = substr($cc2a,0,1);
            $cc2c = substr($cc2a,1,1);
            $cc2 = $cc2b+$cc2c;
        } else {
            $cc2 = $cc2a;
        }
        if ($cc4a >= 10) {
            $cc4b = substr($cc4a,0,1);
            $cc4c = substr($cc4a,1,1);
            $cc4 = $cc4b+$cc4c;
        } else {
            $cc4 = $cc4a;
        }
        if ($cc6a >= 10) {
            $cc6b = substr($cc6a,0,1);
            $cc6c = substr($cc6a,1,1);
            $cc6 = $cc6b+$cc6c;
        } else {
            $cc6 = $cc6a;
        }
        if ($cc8a >= 10) {
            $cc8b = substr($cc8a,0,1);
            $cc8c = substr($cc8a,1,1);
            $cc8 = $cc8b+$cc8c;
        } else {
            $cc8 = $cc8a;
        }
        if ($cc10a >= 10) {
            $cc10b = substr($cc10a,0,1);
            $cc10c = substr($cc10a,1,1);
            $cc10 = $cc10b+$cc10c;
        } else {
            $cc10 = $cc10a;
        }
        if ($cc12a >= 10) {
            $cc12b = substr($cc12a,0,1);
            $cc12c = substr($cc12a,1,1);
            $cc12 = $cc12b+$cc12c;
        } else {
            $cc12 = $cc12a;
        }
        if ($cc14a >= 10) {
            $cc14b = substr($cc14a,0,1);
            $cc14c = substr($cc14a,1,1);
            $cc14 = $cc14b+$cc14c;
        } else {
            $cc14 = $cc14a;
        }

        $val = $cc0+$cc1+$cc2+$cc3+$cc4+$cc5+$cc6+$cc7+$cc8+$cc9+$cc10+$cc11+$cc12+$cc13+$cc14+$cc15;
        if (substr($val,1,1) !=0 ) {
            &invalid_cc;
        }
    }


# For 15 digit (Amex) cards
sub ver15 {
        $cc0 = substr($cardnumber,0,1);
        $cc1 = substr($cardnumber,1,1);
        $cc2 = substr($cardnumber,2,1);
        $cc3 = substr($cardnumber,3,1);
        $cc4 = substr($cardnumber,4,1);
        $cc5 = substr($cardnumber,5,1);
        $cc6 = substr($cardnumber,6,1);
        $cc7 = substr($cardnumber,7,1);
        $cc8 = substr($cardnumber,8,1);
        $cc9 = substr($cardnumber,9,1);
        $cc10 = substr($cardnumber,10,1);
        $cc11 = substr($cardnumber,11,1);
        $cc12 = substr($cardnumber,12,1);
        $cc13 = substr($cardnumber,13,1);
        $cc14 = substr($cardnumber,14,1);

        $cc1a = $cc1 * 2;
        $cc3a = $cc3 * 2;
        $cc5a = $cc5 * 2;
        $cc7a = $cc7 * 2;
        $cc9a = $cc9 * 2;
        $cc11a = $cc11 * 2;
        $cc13a = $cc13 * 2;

        if ($cc1a >= 10) {
            $cc1b = substr($cc1a,0,1);
            $cc1c = substr($cc1a,1,1);
            $cc1 = $cc1b+$cc1c;
        } else {
            $cc1 = $cc1a;
        }
        if ($cc3a >= 10) {
            $cc3b = substr($cc3a,0,1);
            $cc3c = substr($cc3a,1,1);
            $cc3 = $cc3b+$cc3c;
        } else {
            $cc3 = $cc3a;
        }
        if ($cc5a >= 10) {
            $cc5b = substr($cc5a,0,1);
            $cc5c = substr($cc5a,1,1);
            $cc5 = $cc5b+$cc5c;
        } else {
            $cc5 = $cc5a;
        }
        if ($cc7a >= 10) {
            $cc7b = substr($cc7a,0,1);
            $cc7c = substr($cc7a,1,1);
            $cc7 = $cc7b+$cc7c;
        } else {
            $cc7 = $cc7a;
        }
        if ($cc9a >= 10) {
            $cc9b = substr($cc9a,0,1);
            $cc9c = substr($cc9a,1,1);
            $cc9 = $cc9b+$cc9c;
        } else {
            $cc9 = $cc9a;
        }
        if ($cc11a >= 10) {
            $cc11b = substr($cc11a,0,1);
            $cc11c = substr($cc11a,1,1);
            $cc11 = $cc11b+$cc11c;
        } else {
            $cc11 = $cc11a;
        }
        if ($cc13a >= 10) {
            $cc13b = substr($cc13a,0,1);
            $cc13c = substr($cc13a,1,1);
            $cc13 = $cc13b+$cc13c;
        } else {
            $cc13 = $cc13a;
        }

        $val = $cc0+$cc1+$cc2+$cc3+$cc4+$cc5+$cc6+$cc7+$cc8+$cc9+$cc10+$cc11+$cc12+$cc13+$cc14;
        if (substr($val,1,1) !=0 ) {
            &invalid_cc;
        }
    }


}

#####
#
# This Section For Anything Past CC Validation
#
#####
print "<script language=\"Javascript\">parent.botOne.leConfig.CCPassed.value=\"YES\";parent.botOne.leConfig.submit();location.href='topframe.html';</script>";
print "</body></html>";
exit;

sub invalid_cc {
	print "<script language=\"Javascript\">invalid();parent.botOne.leConfig.CCPassed.value=\"NO\";</script>";
	print "</body></html>";
	exit;
}

sub kill_input {
    print "Content-type: text/html\n\n";
    $value = "";
    print "<CENTER><H1><FONT COLOR=\"\#FF0000\">CGI Alert</FONT></H1></CENTER>\n";
    print "<CENTER><H3>It appears as though you've tried to \n";
    print "execute a system command via a SSI tag or shell metacharacter. \n";
    print "Please use your <B>Back</B> button, remove the tags or characters and re-submit. \n";
    print "Thanks\!</H3></CENTER></TD></TR>";
	print "<TR><TD width=\"100%\" align=\"center\" valign=\"middle\" height=\"50\"><font style=\"font-face:verdana;font-size:11px;color:#000000;font-weight:bold;\"><div id=\"numberCountdown\"></div></nobr></font></TD></TR>";
	print "</TABLE></body></html>";
	exit;
}

sub no_data {
	print "<script language=\"Javascript\">dataMissing();parent.botOne.leConfig.CCPassed.value=\"NO\";</script>";
	print "</body></html>";
	exit;
}

exit;