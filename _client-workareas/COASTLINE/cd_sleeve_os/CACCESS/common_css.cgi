#!/usr/bin/perl5

#################################
# Luis Rodriguez (drlouie)
# drlouie@tstonramp.com
#
# Serves up a different set of css styles depending on browser and oprating system type.
#
#Useful for making those varying fonts dissapear!
#################################

require ("parse_query.hs");

$Agent = $ENV{'HTTP_USER_AGENT'};

#Macintosh Platform and MSIE
if ($Agent =~ /Mac/i && $Agent =~ /MSIE/i) { 

	$smallFontSize = "10px";
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

}

#Windows Platform and MSIE
elsif ($Agent =~ /Win/i && $Agent =~ /MSIE/i) { 

	$smallFontSize = "10px";
	$mediumFontSize = "12px";
	$largemedFontSize = "13px";
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

}

#Windows Platform and Netscape Browser
elsif ($Agent =~ /Win/i && $Agent =~ /^Mozilla\/*/i) { 

		$smallFontSize = "11px";
		$mediumFontSize = "12px";
		$largemedFontSize = "12px";
		$largeFontSize = "13px";
		$linereg = "16px";
}

#Macintosh Platform and Netscape Browser
elsif ($Agent =~ /Mac/i && $Agent =~ /^Mozilla\/*/i) { 

	$smallFontSize = "10px";
	$mediumFontSize = "11px";
	$largemedFontSize = "13px";
	$largeFontSize = "13px";
	$linereg = "14px";

}

#All other Platforms and browsers
else { 

		$smallFontSize = "9px";
		$mediumFontSize = "10px";
		$largemedFontSize = "12px";
		$largeFontSize = "15px";
		$linereg = "16px";

}

print "Content-type: text/html\n\n";

print <<EOF
a {
	color:#BEBECC;text-decoration:underline;font-weight:bold;
	}

a:hover {
		 color:#ffffff;text-decoration:none;font-weight:bold;
		}

.tableheading  {
        	font-family : verdana,arial,helvetica;
			font-size : $largeFontSize;
			color : #ffffff;
			font-weight : bold;
        }

.secondhead  {
        	font-family : verdana,arial,helvetica;
			font-size : $largemedFontSize;
			color : #ffffff;
			font-weight : bold;
        }
		
.formbold  {
        	font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #ffffff;
			font-weight : bold;
        }
		
.formnobold  {
        	font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #ffffff;
        }

.regtextnobold  {
        	line-height : $linereg;
			font-family : verdana,arial,helvetica;
			font-size : $mediumFontSize;
			color : #ffffff;
        }
		
.topnavi  {
			font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #ffffff;
			text-decoration : none;
        }
		
.prodmenu  {
        	line-height : $linereg;
			font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #ffffff;
        }

.regtextbold  {
        	font-family : verdana,arial,helvetica;
			font-size : $mediumFontSize;
			color : #ffffff;
			font-weight : bold
        }

.outerlink {
			color : #333366;
        }

.star  {
        	font-family : verdana,arial,helvetica;
			font-size : $mediumFontSize;
			color : #ffffff;
        }

.timer  {
        	font-family : verdana,arial,helvetica;
			font-size : $mediumFontSize;
			color : #ffffff;
			font-weight : bold;
			letter-spacing: 2px;
        }

EOF
}
