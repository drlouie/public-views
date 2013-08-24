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

require ("referer.nsp"); 
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
}

print "Content-type: text/html\n\n";

## SEND THE INFORMATION, WHICH SHOULD BE LINKED TO THE DOCUMENT IN WHICH IT WILL BE USED AS A CSS CALL
{
print <<EOF

body {
	background-color:#ffffff; 
	scrollbar-face-color:#F2F2F7; 
	scrollbar-highlight-color:#F2F2F7; 
	scrollbar-shadow-color:#8f8fab; 
	scrollbar-3dlight-color: #333366; 
	scrollbar-arrow-color:#333366; 
	scrollbar-track-color:#F2F2F7; 
	scrollbar-darkshadow-color:#8f8fab;
}

.topnavi  {
			font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #ffffff;
			text-decoration : none;
}

.stext  {
			font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #333366;
}

.stext2  {
			font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #8F8FAB;
}

.stextbig  {
			font-family : verdana,arial,helvetica;
			font-size : $mediumFontSize;
			color : #333366;
}
		
.slink  {
			font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #333366;
			font-weight: normal;
			text-decoration: underline;
}		

.btext  {
			font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #333366;
}

.btext2  {
			font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #8F8FAB;
}

.btext3  {
			font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #333366;
}

.btextred  {
			font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #EB0000;
}

.samplesmall  {
			font-family : verdana,arial,helvetica;
			font-size : $smallestFontSize;
			color : #333366;
}

.btextbig  {
			font-family : verdana,arial,helvetica;
			font-size : $mediumFontSize;
			color : #333366;
}
		
.blink  {
			font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #333366;
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
			text-decoration : none;
}

#overDiv {	
			position:absolute; 
			visibility:hidden; 
			z-index:5000;
			$overDiving
}

.overDiv {	
			font-family : verdana,arial,helvetica;
			font-size : $smallFontSize;
			color : #333366;
}

.stankth { 	
			border-top:1px solid #333366;
			border-bottom:1px solid #333366;
			border-left:1px solid #333366;
			border-right:1px solid #333366;
}

.sresults1  {
			font-family : verdana,arial,helvetica;
			font-size : $littleFontSize;
			color : #333366;
}
		
.sresultsred  {
			font-family : verdana,arial,helvetica;
			font-size : $littleFontSize;
			color : #EB0000;
}

.multiselect	{
			text-align:left;
			color:#333366;
			background-color:#F2F2F7;
			width:115px;
			height:110px;
			font-family : verdana,arial,helvetica;
			font-size : 11px;
}
				
.singleselect	{
			text-align:left;
			color:#333366;
			background-color:#F2F2F7;
			width:115px;
			height:20px;
			font-family : verdana,arial,helvetica;
			font-size : 11px;
}

.prodselect	{
			text-align:left;
			color:#333366;
			background-color:#F2F2F7;
			width:265px;
			height:90px;
			font-family : verdana,arial,helvetica;
			font-size : 9px;
}
				
.radiobut	{
			font-color:#333366;
			bgcolor:#F2F2F7;
}				
.prodguinea	{
			text-align:left;
			color:#333366;
			background-color:#F2F2F7;
			width:265px;
			height:200px;
			font-family : verdana,arial,helvetica;
			font-size : 9px;
}

.prodguinea2	{
			text-align:left;
			color:#333366;
			background-color:#F2F2F7;
			width:265px;
			height:90px;
			font-family : verdana,arial,helvetica;
			font-size : 9px;
}

.prodguinea2Grey	{
			text-align:left;
			color:#333366;
			background-color:#ebebeb;
			width:265px;
			height:90px;
			font-family : verdana,arial,helvetica;
			font-size : 9px;
}

.textarea	{
			text-align:left;
			color:#333366;
			background-color:#F2F2F7;
			height:110px;
			font-family : verdana,arial,helvetica;
			font-size : 10px;
}

.textarea1	{
			text-align:left;
			color:#333366;
			background-color:#F2F2F7;
			height:110px;
			font-family : verdana,arial,helvetica;
			font-size : 10px;
}

.textarea2	{
			text-align:left;
			color:#333366;
			background-color:#F2F2F7;
			height:40px;
			font-family : verdana,arial,helvetica;
			font-size : 10px;
}

.textarea_large	{
			text-align:left;
			color:#333366;
			background-color:#F2F2F7;
			height:200px;
			font-family : verdana,arial,helvetica;
			font-size : 10px;
}
				
.inputtext	{
			text-align:left;
			color:#333366;
			background-color:#F2F2F7;
			height:20px;
			font-family : verdana,arial,helvetica;
			font-size : 11px;
}

.inputtextSP {
			text-align:left;
			color:#333366;
			background-color:#F2F2F7;
			height:20px;
			font-family : verdana,arial,helvetica;
			font-size : 9px;
}
				
.inputbut	{
			text-align:center;
			color:#333366;
			background-color:#F2F2F7;
			height:20px;
			font-family : verdana,arial,helvetica;
			font-size : 11px;
			font-weight : bold;
}
				
.inputtext35	{
			text-align:left;
			color:#333366;
			background-color:#F2F2F7;
			height:20px;
			width:275px;
			font-family : verdana,arial,helvetica;
			font-size : 11px;
}

.prices	{
			text-align : center;
			color : #EB0000;
			background-color : #F2F2F7;
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
			background-color : #F2F2F7;
			height : 25px;
			width : 225px;
			font-family : verdana,arial,helvetica;
			font-size : 10px;
			font-weight : bold;
			letter-spacing : 1px;
}

.inputtext15	{
			text-align:left;
			color:#333366;
			background-color:#F2F2F7;
			height:20px;
			width:145px;
			font-family : verdana,arial,helvetica;
			font-size : 11px;
}
.inputtext7	{
			text-align:left;
			color:#333366;
			background-color:#F2F2F7;
			height:20px;
			width:60px;
			font-family : verdana,arial,helvetica;
			font-size : 11px;
}
.inputtext3	{
			text-align:left;
			color:#333366;
			background-color:#F2F2F7;
			height:20px;
			width:25px;
			font-family : verdana,arial,helvetica;
			font-size : 11px;
}
				
EOF
}
exit;
