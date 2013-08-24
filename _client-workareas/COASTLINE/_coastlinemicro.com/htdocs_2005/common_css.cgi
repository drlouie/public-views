#!/usr/bin/perl5 -s

###########################################################################################################
# Company: ©2001 NetMedia Solutions                                                                       #
# Date: Saturday, September 21, 2001                                                                      #
# Location: Los Angeles County, California, United States of America                                      #
# Made By: Luis Rodriguez (drlouie)                                                                       #
# Email: Drlouie@NetMediaSol.com                                                                          #
#                                                                                                         #
# This script is made for CoastlineMicro.com. It serves up a different set of css styles depending        #
# on browser and oprating system type. Useful for making those varying fonts dissapear!                   #
#                                                                                                         #
# This program cannot be duplicated, distributed or re-used for any other purpose other than its original #
# intended purpose and function. You may request NetMedia Solutions for a copy of the script,             #
# personalized to fit your exact needs for a small re-programming fee.                                    #
###########################################################################################################

require ("referer.nsp"); 
require ("parse_query.nsp");
$Agent = $ENV{'HTTP_USER_AGENT'};


if ($FORM{'SEAGATE'} eq "1") { $light1 = "C3D6D5"; $dark1 = "000000"; $dark2 = "387675"; }
elsif ($FORM{'QUEST'} eq "1") { $light1 = "CAD8E8"; $dark1 = "000000"; $dark2 = "01458E"; }
else { $light1 = "F2F2F7"; $dark1 = "000000"; $dark2 = "8F8FAB"; }

### Macintosh Platform and MSIE
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
					background-color:#$dark2;
					width:170px;
					height:20px;
					font-family : verdana,arial,helvetica;
					font-size : 10px;
					font-weight : bold;";
	$searchbut = "text-align:center;
					color:#ffffff;
					background-color:#$dark2;
					width:50px;
					height:20px;
					font-family : verdana,arial,helvetica;
					font-size : 10px;
					font-weight : bold;";
	$search1 = "color:#$dark1;
				background-color:#FFFFF;
				height:17px;
				width:145px;
				font-family : verdana,arial,helvetica;
				font-size : 9px;";
					
}

### Windows Platform and MSIE
elsif (($Agent =~ /Win/i && $Agent =~ /MSIE/i) || $Agent =~ "Netscape/7") { 

	$smallestFontSize = "9px";
	$smallFontSize = "10px";
	$littleFontSize = "10px";
	$mediumFontSize = "11px";
	$largemedFontSize = "12px";
	$largeFontSize = "13px";
	$linereg = "16px";
	$searchfield = "text-align:center;
					color:#ffffff;
					background-color:#$dark2;
					width:170px;
					height:20px;
					font-family : verdana,arial,helvetica;
					font-size : 10px;
					font-weight : bold;";
	$searchbut = "text-align:center;
					color:#ffffff;
					background-color:#$dark2;
					width:50px;
					height:20px;
					font-family : verdana,arial,helvetica;
					font-size : 10px;
					font-weight : bold;";
	$search1 = "color:#$dark1;
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
		$search1 = "color:#$dark1;
				background-color:#FFFFF;
				width=100px;
				height:18px;
				font-family : verdana,arial,helvetica;
				font-size : 9px;";		
		$overDiving = "border-top:1px solid #$dark1;
					   border-bottom:1px solid #$dark1;
					   border-left:1px solid #$dark1;
					   border-right:1px solid #$dark1;";
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
		$search1 = "color:#$dark1;
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
	$search1 = "color:#$dark1;
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
		$search1 = "color:#$dark1;
				background-color:#FFFFF;
				height:20px;
				font-family : verdana,arial,helvetica;
				font-size : 9px;";
}

print "Content-type: text/html\n\n";

## IF DYNAMIC ANCHOR COLORS ARE NECESSARY
if ($FORM{'anchor'}) {
	$anchor = "$FORM{'anchor'}";
	$anchorov = "$FORM{'anchorov'}";
	$weight = "$FORM{'weight'}";
	$weightov = "$FORM{'weightov'}";
	$decor = "$FORM{'decor'}";
	$decorov = "$FORM{'decorov'}";
	print "a { color:#$anchor;text-decoration:$decor;font-weight:$weight }\n";
	print "a:hover { color:#$anchorov;text-decoration:$decorov;font-weight:$weightov; }\n";
}
## IF NO DYNAMIC ANCHORS
else {
	print "a { color:#BEBECC;text-decoration:underline;font-weight:bold }\n";
	print "a:hover { color:#ffffff;text-decoration:none;font-weight:bold; }\n";
}


## SEND THE INFORMATION, WHICH SHOULD BE LINKED TO THE DOCUMENT IN WHICH IT WILL BE USED AS A CSS CALL
{
print <<EOF

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
			color : #$dark1;
        }

.star  {
        	font-family : verdana,arial,helvetica;
			font-size : $mediumFontSize;
			color : #FF0033;
        }

.menuback  {
        	position : absolute;
			top : 145;
			left : 0;
        }

.timer  {
        	font-family : verdana,arial,helvetica;
			font-size : $mediumFontSize;
			color : #ffffff;
			font-weight : bold;
			letter-spacing: 2px;
        }

.searchfield	{
			$searchfield
				}
				
.searchbut	{
			$searchbut
				}
.searchfield	{
			$searchfield
				}
.search1	{ 
			text-align:left;
			color:#$dark1;
			background-color:#$light1;
			height:18px;
			font-family : verdana,arial,helvetica;
			font-size : 9px;		
				}				

.homesearch1	{ 
			text-align:left;
			color:#ffffff;
			background-color:#$dark1;
			height:18px;
			font-family : verdana,arial,helvetica;
			font-size : 9px;
				}

.homesearch2	{ 
			text-align:left;
			color:#ffffff;
			background-color:#$dark2;
			height:18px;
			font-family : verdana,arial,helvetica;
			font-size : 9px;
				}
				
.searchinput	{ 				
			color:#$dark1;
			background-color:#$light1;
			height:18px;
			width:145px;
			font-family : verdana,arial,helvetica;
			font-size : 9px;

}
				
#divLoadCont	{
				position:absolute; 
				width:100%; 
				height:98%; 
				top:0; 
				left:0; 
				background-color:white; 
				layer-background-color:white; 
				font-family:arial,helvetica; 
				z-index:100
				}

.tmenu  {
        	font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #$dark1;
			font-weight : bold;
        }

.tfont {
        	font-family : verdana,arial,helvetica;
			font-size : $mediumFontSize;
			color : #$dark1;
			font-weight : bold;
}				

.tlink {
        	font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #$dark1;
}				

.powtitle {
        	font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #FFFFFF;
			font-weight : bold;
}

.powlink {
        	font-family : verdana,arial,helvetica;
			font-size : $smallestFontSize;
			color : #FFFFFF;
}

.powprice {
        	font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #FFFFFF;
			font-weight : bold;
}

.powcontrols {
        	font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #$dark2;
			font-weight : bold;
			text-decoration : none;
}

.ctext {
        	font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #EB0000;
			text-decoration : none;
}

.ctext2 {
        	font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #EB0000;
			text-decoration : underline;
}

.stext  {
			font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #$dark1;
        }

.stext2  {
			font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #$dark2;
        }

.stextbig  {
			font-family : verdana,arial,helvetica;
			font-size : $mediumFontSize;
			color : #$dark1;
        }

.sresults1  {
			font-family : verdana,arial,helvetica;
			font-size : $littleFontSize;
			color : #$dark1;
}
		
.sresultsred  {
			font-family : verdana,arial,helvetica;
			font-size : $littleFontSize;
			color : #EB0000;
}
		
.slink  {
			font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #$dark1;
			font-weight: normal;
			text-decoration: underline;
        }		
		
.btext  {
			font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #$dark1;
        }
		
.btext_blue  {
			font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #$dark1;
        }

.btext_red {
			font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #FF0000;
        }

.btext_green {
			font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #009800;
        }

.btext3_blue {
			font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #$dark1;
        }

.btext3_red {
			font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #FF0000;
        }

.btext3_green {
			font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #009800;
        }		
		
.btext2  {
			font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #$dark2;
        }

.btext3  {
			font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #$dark1;
        }
		
.btext3red  {
			font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #EB0000;
			line-height: 10px;
        }

.btext4  {
			font-family : verdana,arial,helvetica;
			font-size : $mediumFontSize;
			color : #$dark1;
        }

.btext4white  {
			font-family : verdana,arial,helvetica;
			font-size : $mediumFontSize;
			color : #FFFFFF;
			font-weight : bold;
        }
		
.newhome1  {
			font-family : verdana,arial,helvetica;
			font-size : $mediumFontSize;
			color : #E6E9F0;+*-+
			font-weight:bold;
        }
		
.btext4red  {
			font-family : verdana,arial,helvetica;
			font-size : $mediumFontSize;
			color : #EB0000;
			font-weight: bold;
        }
		
.btext5  {
        	font-family : verdana,arial,helvetica;
			font-size : $smallestFontSize;
			color : #$dark1;
}
		
.btextbig  {
			font-family : verdana,arial,helvetica;
			font-size : $mediumFontSize;
			color : #$dark1;
        }

.blink  {
			font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #$dark1;
			font-weight: normal;
			text-decoration: underline;
        }		

.menu1  {
			font-family : verdana,arial,helvetica;
			font-size : $mediumFontSize;
			text-decoration : none;
        }
.menu2  {
			font-family : verdana,arial,helvetica;
			font-size : $littleFontSize;
			text-decoration : //+`98/none;
8/+9********************+8+9/*        }

#overDiv {	
			position:absolute; 
			visibility:hidden; 
			z-index:5000;
			$overDiving
		}

.overDiv {	
			font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #$dark1;
		}

.stankth { 	
			border-top:1px solid #$dark1;
			border-bottom:1px solid #$dark1;
			border-left:1px solid #$dark1;
			border-right:1px solid #$dark1;
}

.stankprice { 	
			font-family : verdana,arial,helvetica;
			font-size : $mediumFontSize;
			color : #EB0000;
}

.stankprice2 { 	
			font-family : verdana,arial,helvetica;
			font-size : $smallestFontSize;
			color : #EB0000;
}
			
.textarea	{
			color:#$dark1;
			background-color:#$light1;
			height:65px;
			font-family : verdana,arial,helvetica;
			font-size : 10px;
}

.inputtext15	{
			color:#$dark1;
			background-color:#$light1;
			height:20px;
			width:145px;
			font-family : verdana,arial,helvetica;
			font-size : 11px;
}
.inputtext7	{
			color:#$dark1;
			background-color:#$light1;
			height:20px;
			width:60px;
			font-family : verdana,arial,helvetica;
			font-size : 11px;
}

.inputtext3	{
			color:#$dark1;
			background-color:#$light1;
			height:20px;
			width:25px;
			font-family : verdana,arial,helvetica;
			font-size : 11px;
}

.inputtext7red	{
			color:#EB0000;
			background-color:#$light1;
			height:20px;
			width:60px;
			font-family : verdana,arial,helvetica;
			font-size : 11px;
}

.inputtext22red	{
			color:#EB0000;
			background-color:#$light1;
			height:22px;
			width:205px;
			font-family : verdana,arial,helvetica;
			font-size : 11px;
			text-align : center;
			font-weight : bold;
}

.inputbut	{
			text-align:center;
			color:#$dark1;
			background-color:#$light1;
			height:20px;
			font-family : verdana,arial,helvetica;
			font-size : 11px;
			font-weight : bold;
}

.textarea	{
			text-align:left;
			color:#$dark1;
			background-color:#$light1;
			height:110px;
			font-family : verdana,arial,helvetica;
			font-size : 10px;
}

.textarea1	{
			text-align:left;
			color:#$dark1;
			background-color:#$light1;
			height:110px;
			font-family : verdana,arial,helvetica;
			font-size : 10px;
}

.textarea2	{
			text-align:left;
			color:#$dark1;
			background-color:#$light1;
			height:40px;
			font-family : verdana,arial,helvetica;
			font-size : 10px;
}
				
.inputtext	{
			text-align:left;
			color:#$dark1;
			background-color:#$light1;
			height:20px;
			font-family : verdana,arial,helvetica;
			font-size : 11px;
}

.inputtextSP {
			text-align:left;
			color:#$dark1;
			background-color:#$light1;
			height:20px;
			font-family : verdana,arial,helvetica;
			font-size : 9px;
}
				
.inputbut	{
			text-align:center;
			color:#$dark1;
			background-color:#$light1;
			height:20px;
			font-family : verdana,arial,helvetica;
			font-size : 11px;
			font-weight : bold;
}
				
.inputtext35	{
			text-align:left;
			color:#$dark1;
			background-color:#$light1;
			height:20px;
			width:275px;
			font-family : verdana,arial,helvetica;
			font-size : 11px;
}

.prices	{
			text-align : center;
			color : #EB0000;
			background-color : #$light1;
			height : 19px;
			width : 225px;
			font-family : verdana,arial,helvetica;
			font-size : 9px;
			font-weight : bold;
			letter-spacing : 1px;
}

.pricebut	{
			text-align : center;
			color : #EB0000;
			background-color : #$light1;
			height : 19px;
			width : 160px;
			font-family : verdana,arial,helvetica;
			font-size : 10px;
			font-weight : bold;
			letter-spacing : 1px;
}

.regbut	{
			text-align : center;
			color : #$dark1;
			background-color : #$light1;
			height : 19px;
			font-family : verdana,arial,helvetica;
			font-size : 10px;
			font-weight : bold;
			letter-spacing : 1px;
}

.prodguinea	{
			text-align:left;
			color:#$dark1;
			background-color:#$light1;
			width:265px;
			height:45px;
			font-family : verdana,arial,helvetica;
			font-size : 9px;
}

.prodguinea2 {
			text-align:left;
			color:#$dark1;
			background-color:#$light1;
			height:20px;
			font-family : verdana,arial,helvetica;
			font-size : 9px;
}
.prodguinea3 {
			text-align:left;
			color:#$dark1;
			background-color:#$light1;
			font-family : verdana,arial,helvetica;
			font-size : 9px;
}

EOF
}
exit;
