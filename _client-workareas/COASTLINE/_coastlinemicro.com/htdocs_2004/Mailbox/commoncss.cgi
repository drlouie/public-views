#!/usr/bin/perl5 -w

#####################################################################################################
# Company: NetMedia Solutions                                                                       #
# Date: Saturday, September 21, 2001                                                                #
# Location: Los Angeles, California, United States of America                                       #
# Made By: Luis Rodriguez (drlouie)                                                                 #
# Email: drlouie@tstonramp.com                                                                      #
#                                                                                                   #
# This script is made for CoastlineMicro.com. It serves up a different set of css styles depending  #
# on browser and oprating system type. Useful for making those varying fonts dissapear!             #
#                                                                                                   #
#####################################################################################################

require ("parse_query.nsp");
$Agent = $ENV{'HTTP_USER_AGENT'};

###### PARSE BROWSER SPECIFIC SYTLES FOR EACH VARIATION OF BROWSER. THIS IS WHERE ALL THE TESTING AND CHANGING
###### TAKES PLACE. IT ALLOWS TO MAKE ALL BROWSERS ON ALL OS TYPES AND VARIATIONS TO HAVE THE SAME, IF NOT ADVANCED 
###### DHTML/CSS LAYOUTS.

if ($Agent =~ /Mac/i && $Agent =~ /MSIE/i) { 
	$smallestFontSize = "9px";
	$smallFontSize = "10px";
	$littleFontSize = "10px";
	$mediumFontSize = "11px";
	$largemedFontSize = "13px";
	$largeFontSize = "13px";
	$linereg = "14px";
    $searchfield = "text-align:center;
					color:#ffffff;
					background-color:#8f8fab;
					width:170px;
					height:20px;
					font-family : verdana,arial,helvetica;
					font-size : 10px;
					font-weight : bold;";
	$searchbut = "text-align:center;
					color:#ffffff;
					background-color:#8f8fab;
					width:50px;
					height:20px;
					font-family : verdana,arial,helvetica;
					font-size : 10px;
					font-weight : bold;";
	$search1 = "color:#333366;
				background-color:#FFFFF;
				height:17px;
				width:145px;
				font-family : verdana,arial,helvetica;
				font-size : 9px;";
					
}

### Windows Platform and MSIE
elsif ($Agent =~ /Win/i && $Agent =~ /MSIE/i) { 

	$smallestFontSize = "9px";
	$smallFontSize = "10px";
	$littleFontSize = "10px";
	$mediumFontSize = "11px";
	$largemedFontSize = "12px";
	$largeFontSize = "13px";
	$linereg = "16px";
	$searchfield = "text-align:center;
					color:#ffffff;
					background-color:#8f8fab;
					width:170px;
					height:20px;
					font-family : verdana,arial,helvetica;
					font-size : 10px;
					font-weight : bold;";
	$searchbut = "text-align:center;
					color:#ffffff;
					background-color:#8f8fab;
					width:50px;
					height:20px;
					font-family : verdana,arial,helvetica;
					font-size : 10px;
					font-weight : bold;";
	$search1 = "color:#333366;
				background-color:#FFFFF;
				height:17px;
				width:145px;
				font-family : verdana,arial,helvetica;
				font-size : 9px;";				
					
}

### Windows Platform and Netscape6 Browser
elsif ($Agent =~ /Win/i && $Agent =~ /^Mozilla\/*/i && $Agent =~ "Netscape6/") { 

		$smallestFontSize = "9px";
		$smallFontSize = "10px";
		$littleFontSize = "10px";
		$mediumFontSize = "11px";
		$largemedFontSize = "12px";
		$largeFontSize = "13px";
		$linereg = "15px";
		$search1 = "color:#333366;
				background-color:#FFFFF;
				width=100px;
				height:18px;
				font-family : verdana,arial,helvetica;
				font-size : 9px;";		
		$overDiving = "border-top:1px solid #333366;
					   border-bottom:1px solid #333366;
					   border-left:1px solid #333366;
					   border-right:1px solid #333366;";
}

### Windows Platform and Netscape Browser
elsif ($Agent =~ /Win/i && $Agent =~ /^Mozilla\/*/i) { 

		$smallestFontSize = "10px";
		$smallFontSize = "11px";
		$littleFontSize = "11px";
		$mediumFontSize = "12px";
		$largemedFontSize = "13px";
		$largeFontSize = "14px";
		$linereg = "16px";
		$search1 = "color:#333366;
				background-color:#FFFFF;
				height:20px;
				font-family : verdana,arial,helvetica;
				font-size : 11px;";
}

### Macintosh Platform and Netscape Browser
elsif ($Agent =~ /Mac/i && $Agent =~ /^Mozilla\/*/i) { 

	$smallestFontSize = "9px";
	$smallFontSize = "10px";
	$littleFontSize = "10px";
	$mediumFontSize = "11px";
	$largemedFontSize = "12px";
	$largeFontSize = "13px";
	$linereg = "14px";
	$search1 = "color:#333366;
				background-color:#FFFFF;
				height:20px;
				font-family : verdana,arial,helvetica;
				font-size : 9px;";
}

### All other Platforms and browsers
else { 

		$smallestFontSize = "9px";
		$smallFontSize = "10px";
		$littleFontSize = "10px";
		$mediumFontSize = "11px";
		$largemedFontSize = "12px";
		$largeFontSize = "13px";
		$linereg = "14px";
		$search1 = "color:#333366;
				background-color:#FFFFF;
				height:20px;
				font-family : verdana,arial,helvetica;
				font-size : 9px;";
}

print "Content-type: text/html\n\n";

## SEND THE INFORMATION, WHICH SHOULD BE LINKED TO THE DOCUMENT IN WHICH IT WILL BE USED AS A CSS CALL
{
print <<EOF

.comtitle  {
			font-family : verdana,arial,helvetica;
			font-size : $largeFontSize;
			color : #333366;
        }
.comtext  {
			font-family : verdana,arial,helvetica;
			font-size : $mediumFontSize;
			color : #333366;
        }
.comlink {
			font-family : verdana,arial,helvetica;
			font-size : $mediumFontSize;
			color : #333366;
			text-decoration:none;
}

.comtableborder { 	
			border-top:1px solid #8F8FAB;
			border-bottom:1px solid #8F8FAB;
			border-left:1px solid #8F8FAB;
			border-right:1px solid #8F8FAB;
}
		
EOF
}
exit;
