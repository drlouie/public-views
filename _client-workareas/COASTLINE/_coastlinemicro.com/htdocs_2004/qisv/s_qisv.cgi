#!/usr/bin/perl5 -w
##################################################################################
#site Search Version 2.01 Copyright (C) 1997, 1998, 1999, Jayakrishnan Krishnan. #
#All Rights Reserved. Read the file 'copyright' for more information.	         #
##################################################################################

$version = "2.01";

&Intro;
sub Intro{
if ($ENV{"HTTP_USER_AGENT"} eq ""){
print <<"ENDPRINT";

site Search version $version, by Jayakrishnan Krishnan.
Copyright (C) 1997, 1998, 1999.

site Search is a search Engine written in perl. Some of its key features are , 
  
% Can Perform Searches of three types, "As a Phrase", "Any Search Term", 
  and "All Search Terms". 
% Can Search for "Exact" or "Fuzzy" pattern matches.
% Can display "n" hits per page, where "n" is any set of numbers configured 
  by the web-administrator on the search form. 
% Displays the number of occurrences of each search term. 
% Can Display "n" bytes of information containing the search term(s).
% Displays the title and description of each successful hit, each of which 
  are extracted from HTML tag of the file. 
% Can Display an alternative description which can be included from a text 
  file. Description can also be a hypertext link. 
% Can be customized to include/exclude sets of files/directories in the 
  search path. 
% Can be configured to include a separate form at the end of each search 
  output which searches only the successful hits to narrow down the possibility.
% Can be configured to include a header and footer file for a search output.
% Can search HTML pages in languages other than english.
% Fast & extremely customizable.

This is shareware; Read the file 'copyright' for 
more information about registering this program.

Please report bugs/modifications to 
saljxk\@tank.agl.uh.edu

##################################################################################
#This copy of site Search is unregistered, Please read the file 'copyright' to   #
#obtain more information                                                         #
##################################################################################
ENDPRINT
exit;
}
}

unshift(@INC,".");
open(READ,"site_Search.conf") or &Error_Module("1");close(READ);
use CGI qw(:cgi-lib);
require("site_Search.conf") ;

@months = (January,February,March,April,May,June,July,August,September,October,November,December);

##Codes Translate 
#You may not see these codes on any editor, 'vi' works.
%html_codes = (

'€'	=>	'&Ccedil;',
''	=>	'&uuml;',
'‚'	=>	'&egrave;',
'ƒ'	=>	'&circ;',
'„'	=>	'&auml;',
'…'	=>	'&agrave;',
'†'	=>	'&aring;',
'‡'	=>	'&ccedil;',
'ˆ'	=>	'&ecirc;',
'‰'	=>	'&euml;',
'Š'	=>	'&egrave;',
'‹'	=>	'&iuml;',
'Œ'	=>	'&icirc;',
''	=>	'&igrave;',
'Ž'	=>	'&Auml;',
''	=>	'&Aring;',
''	=>	'&Egrave;',
'‘'	=>	'&aelig;',
'’'	=>	'&AElig;',
'“'	=>	'&ocirc;',
'•'	=>	'&ograve;',
'–'	=>	'&ouml;',
'—'	=>	'&ugrave;',
'˜'	=>	'&yuml;',
'™'	=>	'&Ouml;',
'š'	=>	'&Uuml;',
'›'	=>	'&oslash;',
''	=>	'&Oslash;',
' '	=>	'&aacute;',
'¡'	=>	'&iacute;',
'¢'	=>	'&oacute;',
'£'	=>	'&uacute;',
'¤'	=>	'&ntilde;',
'¥'	=>	'&Ntilde;',
'µ'	=>	'&Aacute;',
'¶'	=>	'&Acirc;',
'·'	=>	'&Agrave;',
'Æ'	=>	'&atilde;',
'Ç'	=>	'&Atilde;',
'Ð'	=>	'&eth;',
'Ñ'	=>	'&ETH;',
'Ò'	=>	'&Ecirc;',
'Ó'	=>	'&Euml;',
'Ô'	=>	'&Egrave;',
'Ö'	=>	'&Iacute;',
'×'	=>	'&Icirc;',
'Ø'	=>	'&Iuml;',
'Þ'	=>	'&Igrave;',
'à'	=>	'&Oacute;',
'á'	=>	'&szlig;',
'â'	=>	'&Ocirc;',
'ã'	=>	'&Oacute;',
'ä'	=>	'&otilde;',
'å'	=>	'&Otilde;',
'ç'	=>	'&thorn;',
'è'	=>	'&THORN;',
'é'	=>	'&Uacute;',
'ê'	=>	'&Ucirc;',
'ë'	=>	'&Ugrave;',
'ì'	=>	'&yacute;',
);

&Check_Configurations	if($check_script eq "1");
&Assign_Default_Values;
&Clean_Scratch          if($clean_scratch eq "1");
&Get_Search_Terms;
#&Debug;
&Get_Files_to_Search	if($skip_search ne "1");
&Search_Files;
&Display_Results1 if ((scalar(@file_names_to_display) == 0) ||
                (scalar(@file_names_to_display) <= int($get_hits)) ||
                ($get_hits =~ /all/i) ||
                ($get_hits eq "") ||
		($multi_display eq "0"));
		
&Display_Results2;

#########################################################
#		-:PRIMARY MODULES:-			#
#########################################################
#    Module Checks for errors in configuration file	#
#########################################################
sub Check_Configurations{
print &Header;

&Error_Module("3")	if(!(-r "site_Search.desc") && ($desc1 eq "1"));
&Error_Module("4")	if(!(-d "$base_path") || !(-r "$base_path") ||  !(-x "$base_path"));
&Error_Module("5")	if(scalar(@filetypes) == 0);   

if ($multi_display eq "1" || $output_form eq "1"){
&Error_Module("6")	
	if(($scratch eq "") || !(-d "$base_path/$scratch") || !(-w "$base_path/$scratch") || !(-r "$base_path/$scratch") || 
	!(-x "$base_path/$scratch"));

}

if ($record_usage eq "1"){
&Error_Module("7")	if ((-e "site_Search.usage") && !(-w "site_Search.usage"));
}

&Error_Module("8")	if ($path_to_searchform eq "");
&Error_Module("9")	if ((($output_form eq "1") && ($form_to_use !~ /\binternal\b/)) && !(-r "$form_to_use"));
&Error_Module("10")	if (($output_header ne "") && !(-r "$output_header"));
&Error_Module("10")	if (($output_footer ne "") && !(-r "$output_footer"));

print

"<P>No errors were Found. However, the script only runs a simple check through the configuration file.
If you notice the script not working as intended please go through the file,
<BR><BR><STRONG><LI>readme.html<BR><BR></STRONG> to diagnose and solve problems. 
<P>If you are a registered user, you are eligible to obtain assistance configuring the program.
Please send me a mail (saljxk\@tank.agl.uh.edu), with your registration information.</P>
<P>To run the script set the variable \"\$check_script\" to \"0\" in the configuration file.</P>"
if ($errors ne "1");
print &Bottom;
exit;
}

#################################################
#       Module Assigns Certain Default Values   #
#################################################
sub Assign_Default_Values{
($name_of_URI = "http:\/\/" . $ENV{'HTTP_HOST'}) if (length($name_of_URI) == 0);
($output_bytes = 512) if (($output_line eq "1") && ($output_bytes == 0));
}


#################################################
#       Module Cleans the Scratch directory     #
#################################################
sub Clean_Scratch{
my @list;
@list = <$base_path/$scratch/[1-9]*.html>;
$^T = time;
 
foreach (@list){
        unlink($_) if (int(100*($age = -M)) > int(100*($empty_scratch)));
}
}

#################################################
#         Module Parses the Form Output         #
#################################################
sub Get_Search_Terms{

ReadParse(*input);
$search_terms = ($input{'Searchterms'});
$search_terms =~ s/(\\|\||\(|\)|\[|\{|\^|\$|\*|\+|\?|\.)/\\$1/g;
@get_search_terms = split(/ /,$search_terms);
&Ascii_to_html_code if($ascii_to_html_code eq "1");

$get_case = ($input{'Case'});
$get_type = ($input{'Type'});
$get_construct = ($input{'Construct'});

$get_case = "Insensitive" if (($get_case !~ /insensitive/i) && ($get_case !~ /sensitive/i));
$get_type = "Fuzzy Match" if (($get_type !~ /exact/i) && ($get_type !~ /fuzzy/i));
$get_construct = "Any search term" if (($get_construct !~ /Any search term/i) && ($get_construct !~ /All search terms/i) && ($get_construct !~ /As a phrase/i));

open(READHEADER,"$output_header");
@header = <READHEADER>;
close(READHEADER);

open(READFOOTER,"$output_footer");
@footer = <READFOOTER>;
close(READFOOTER);

if (defined $input{'OUTPUT_FORM'}){
	$skip_search = $skip_hits = "1";
	$get_hits = "ALL";
	open(READ,$input{'List_File'});
	@files_to_be_searched = <READ>;
}


$get_hits = ($input{'Hits'}) if ($skip_hits ne "1");
&no_search_terms if (scalar(@get_search_terms) == 0);
&record_usage if($record_usage eq "1");
&get_desc if ($desc1 eq "1");
}

#################################################
#    Module Gathers the Files to be Searched    #
#################################################
sub Get_Files_to_Search{
my $file;

@files_from_scandir = &scandir($base_path);


foreach $file (@files_from_scandir){
                push(@files_from_scandir,&scandir($file)) if((-d $file) && (&dirs_avoid($file) ne "0"));
}

foreach $file (@files_from_scandir){
        push(@files_to_be_searched,$file) if((&scantype($file) == 1) && (&files_avoid($file) ne "0"));
}

foreach $file (@files_to_include){
        push(@files_to_be_searched,$file);
}
}

#################################################
#    Module Searches Files for Search Term(s)   #
#################################################
sub Search_Files{

	foreach $file_name (@files_to_be_searched){
	my $count;
	my $file_match_y = 0;
	my $str_length = 0;
	$mod_time = (stat($file_name))[9];
        $mod_time{$file_name} = &Get_Date;
        open(READ,"$file_name");
        my @file_chars = <READ>;
        $file_to_search = join("",@file_chars);
        $title_array{$file_name} = "$1"
        if ($file_to_search =~ /<TITLE>([^>]+)<\/TITLE>/i);
        $desc_array{$file_name} = "$1"
        if (($file_to_search =~ /<[^>]*META[^>]+NAME\s*=[ "]*description[ "]+CONTENT\s*=\s*"(([^>"])*)"[^>]*>/i) && ($desc2 == "1"));
	$file_to_search =~ s/<([^>])*>//gs;
 	$_ = $file_to_search;

	if ($get_type =~ /exact/i){
	if ($get_construct eq "As a phrase"){
        	$get_search_terms = join(" ",@get_search_terms);
		push(@file_names_to_display,$file_name) if (($count = /\b$get_search_terms\b/o)  && ($get_case eq "Sensitive"));
		push(@file_names_to_display,$file_name) if (($count = /\b$get_search_terms\b/io)  && ($get_case eq "Insensitive"));
        	$line_array{$file_name} = &get_line() if  (($output_line eq "1") && ($count > 0));
		$hits_array{$file_name} = &get_hits() if (($output_hits eq "1") && ($count > 0));
	}
	
	if ($get_construct eq "Any search term"){
		 foreach $get_search_term (@get_search_terms)
                        {
		push(@file_names_to_display,$file_name) if (($count = /\b$get_search_term\b/) && ($get_case eq "Sensitive"));
		push(@file_names_to_display,$file_name) if (($count = /\b$get_search_term\b/i) && ($get_case eq "Insensitive"));
		last if($count > 0);	
                        }
                $line_array{$file_name} = &get_line() if(($output_line eq "1") && ($count > 0));
                $hits_array{$file_name} = &get_hits() if (($output_hits eq "1") && ($count > 0));
		}

	if ($get_construct eq "All search terms"){		
                $str_length = @get_search_terms;
                foreach $get_search_term (@get_search_terms){
		$file_match_y++ if (($count = /\b$get_search_term\b/) && ($get_case eq "Sensitive"));
		$file_match_y++ if (($count = /\b$get_search_term\b/i) && ($get_case eq "Insensitive"));
		}
    		push(@file_names_to_display,$file_name) if ($file_match_y == $str_length);
		$line_array{$file_name} = &get_line() if (($output_line eq "1") && ($count > 0));
		$hits_array{$file_name} = &get_hits()  if (($output_hits eq "1") && ($count > 0));
                }
	}

	if ($get_type =~ /fuzzy/i){
	if ($get_construct eq "As a phrase"){
        	$get_search_terms = join(" ",@get_search_terms);
		push(@file_names_to_display,$file_name) if (($count = /.*?$get_search_terms.*?/o)  && ($get_case eq "Sensitive"));
		push(@file_names_to_display,$file_name) if (($count = /.*?$get_search_terms.*?/io)  && ($get_case eq "Insensitive"));
        	$line_array{$file_name} = &get_line() if  (($output_line eq "1") && ($count > 0));
		$hits_array{$file_name} = &get_hits() if (($output_hits eq "1") && ($count > 0));
	}
	
	if ($get_construct eq "Any search term"){
		 foreach $get_search_term (@get_search_terms)
                        {
		push(@file_names_to_display,$file_name) if (($count = /.*?$get_search_term.*?/) && ($get_case eq "Sensitive"));
		push(@file_names_to_display,$file_name) if (($count = /.*?$get_search_term.*?/i) && ($get_case eq "Insensitive"));
		last if($count > 0);	
                        }
                $line_array{$file_name} = &get_line() if(($output_line eq "1") && ($count > 0));
                $hits_array{$file_name} = &get_hits() if (($output_hits eq "1") && ($count > 0));
		}

	if ($get_construct eq "All search terms"){		
                $str_length = @get_search_terms;
                foreach $get_search_term (@get_search_terms){
		$file_match_y++ if (($count = /.*?$get_search_term.*?/) && ($get_case eq "Sensitive"));
		$file_match_y++ if (($count = /.*?$get_search_term.*?/i) && ($get_case eq "Insensitive"));
		}
    		push(@file_names_to_display,$file_name) if ($file_match_y == $str_length);
		$line_array{$file_name} = &get_line() if (($output_line eq "1") && ($count > 0));
		$hits_array{$file_name} = &get_hits()  if (($output_hits eq "1") && ($count > 0));
                }
	}

} 
}

#################################################
#       Modules Display the Search Results      #
#################################################
sub Display_Results1{
my $file_name;

        &No_Matches if (scalar(@file_names_to_display) == 0);
        print &Header;
        print &Top($title_for_search_page);
        print "<CENTER>";
	$search_terms =~ s/\\//g;
        print "<!--Case:$get_case | Type:$get_type | Construct:$get_construct | Hits Per Page:$get_hits<BR><BR>--><b>Search Query:&nbsp;</b>$search_terms<br><br>";
        print "<!--<B>".scalar(@files_to_be_searched)."File(s) Searched --><b>".scalar(@file_names_to_display)."</b> possible match(es) found...<BR><br>";
        print "</CENTER>";
	print @header;
                        
        foreach $file_name (@file_names_to_display)
        {
                my $file1 = substr($file_name,rindex($file_name,"/")+1);
                my $file2 = substr($file_name,length($base_path));
                my $mod_time = $mod_time{$file_name};

                print "<BR><table class=\"regtextnobold\" width=\"95%\" align=\"center\"><TR><TD width=\"100%\"><font size=\"2\" face=\"verdana,arial,helvetica\"><A HREF=\"$name_of_URI$file2\" target=\"_top\">$title_array{\"$file_name\"}</a></li><BR>";
                print "<!--<I><B>&nbsp;Modified:</B>$mod_time</I><BR>-->";
		### capture file contents and only use the necesary table information
				$myfile = substr($file2, 12, -5);     # Get filename from 12 to -5
				$mylocation = substr($file2, 1, 10);     # Get the location of file from 1 to 12
				$mystuff = `cat $mylocation/$myfile.html`;
				@mystuffs = split(/<!--KILLSPOTTER-->/, $mystuff);
				$mystuff2 = $mystuffs[1];
				@twomystuffs = split(/<!--KILLSPOTTER2-->/, $mystuff2);
				print "<p>$twomystuffs[0]</p>";
                print "</font></TD></TR></TABLE>";
        }
        print "<BR>";
        print "";
	print @footer;
	print &output_form if ($output_form eq "1");	
	print &Bottom;
	exit;
}

### ... Module 2
sub Display_Results2{
my $counter = 0;
my $counter2;
my $files_displayed = 0;
my $files_to_display = int($get_hits);
my $output_fileno = 1;
my $hits = int($get_hits);
$search_terms =~ s/\\//g;

	while($counter < scalar(@file_names_to_display)){
		if($files_displayed == 0){
			print &Header;
			$output = "STDOUT";
			$next_file = $$ . "_$output_fileno" . "_of_" . "$hits" . ".html";
			}else{
			$output = "WRITE";
			open(WRITE,">$base_path/$scratch/$next_file");
			$output_fileno++;
			$next_file = $$ . "_$output_fileno" . "_of_" . "$hits" . ".html";
			}
print $output &Top($title_for_search_page);
print $output "<CENTER>";
print $output "<!--Case:$get_case | Type:$get_type | Construct:$get_construct | Hits Per Page:$get_hits | Terms:$search_terms<BR><BR>--><b>Search Query:&nbsp;</b>$search_terms<br><br>";
print $output "<!--<B>".scalar(@files_to_be_searched)."File(s) Searched --><b>".scalar(@file_names_to_display)."</B> possible match(es) found...<BR><br>";
print $output "<P>Match(es) " . ($files_displayed+1) . " to " . ($files_displayed+$hits) . " </P>"
		if (($counter + $hits) < scalar(@file_names_to_display));
print $output "<P>Match(es) " . ($files_displayed+1) . " to " . scalar(@file_names_to_display) . " </P>"
		if (($counter + $hits) > scalar(@file_names_to_display));
print $output "</CENTER>";
print $output @header;
print $output "<FORM METHOD=\"GET\" ACTION=\"$name_of_URI/$scratch/$next_file\">" 
		if (($counter + $hits) < scalar(@file_names_to_display));

 		for($counter2 = $files_displayed;$counter2 < $files_to_display;$counter2++)
                {
                        last if(length($file_names_to_display[$counter2]) == 0);
                        $file1 = substr($file_names_to_display[$counter2],rindex($file_names_to_display[$counter2],"/")+1);
                        $file2 = substr($file_names_to_display[$counter2],length($base_path));
                        $mod_time = $mod_time{$file_names_to_display[$counter2]};
			print $output "<BR><TR><TD><font class=regtextnobold><li><b>Title:</b>&nbsp;$title_array{\"$file_names_to_display[$counter2]\"}</li><BR>";
            print $output "<!--<I><B>Modified:</B>$mod_time</I><BR>-->";
			print $output "<li><b>Link:</b>&nbsp;&nbsp;<A HREF=\"$name_of_URI$file2\" target=\"_top\" class=\"innerlink\">$file1</A></LI><BR>";
			print $output "<B>Description:</B>$desc_array{\"$file_names_to_display[$counter2]\"}<BR>" 
					if (($desc1 eq "1") || ($desc2 eq "1"));
			print $output "$hits_array{\"$file_names_to_display[$counter2]\"}<BR>" if ($output_hits eq "1");
                	print $output "$line_array{\"$file_names_to_display[$counter2]\"}" if ($output_line eq "1");
        		print $output "</font></TD></TR>";
        
                }

		print $output "<P><CENTER><INPUT TYPE=\"SUBMIT\" VALUE=\"GET NEXT $hits HITS\"></CENTER></P>"
		if (($counter + $hits) < scalar(@file_names_to_display));

		print $output "";
		print $output "</FORM>";
		print $output @footer;
		print $output &output_form if ($output_form eq "1");

		print $output "<!--Copyright Jayakrishnan-->";
		print $output &Bottom;

	$files_displayed += $hits;
	$counter += $hits;
	$files_to_display += $hits;
}
}

#########################################################
#		-:SECONDARY MODULES:-			#
#########################################################
#___Module Prints Error Messages to Help Rectify___#
sub Error_Module
{
        $errors = "1";
        print &Header if (($_[0] eq "1") || ($_[0] eq "2") || ($_[0] eq "10"));
        print "<FONT SIZE=\"3\" FACE=\"HELVETICA\"><BR>";
        print "<P> A Configuration file <STRONG> site_Search.conf </STRONG> could not be located in the current<BR>
                directory, either the file is not present or does not have read permissions. To get help rectifying<BR>
                the error, read the \"Errors\" section, (Error-1) of the \"readme.html\" file.<BR>" if ($_[0] eq "1");
        print "<P> The description file <STRONG> site_Search.desc </STRONG> could not be opened for reading. There<BR>
                could be a permission problem. To get help rectifying the error, read the \"Errors\" section, (Error-3) of<BR>
                of the \"readme.html\" file.<BR>" 						if ($_[0] eq "3");
        print "<P> There is a problem with the base-path specified to start the search. To get help rectifying the error,<BR>
                read the \"Errors\" section, (Error-4) of the \"readme.html\" file.<BR>" 	if ($_[0] eq "4");
        print "<P> No filetypes have been specified to search. To get help rectifying the error, read the \"Errors\" section,<BR>
                (Error-5) of the \"readme.html\" file.<BR>" 					if ($_[0] eq "5");
        print "<P> There is a problem with the scratch directory specified. To get help rectifying the error, read the <BR>
                \"Errors\" section, (Error-6) of the \"readme.html\" file.<BR>" 		if ($_[0] eq "6");
        print "<P> There is a problem recording the script usage. To get help rectifying the error, read the \"Errors\" <BR>
                section, (Error-7) of the \"readme.html\" file.<BR>" 				if ($_[0] eq "7");
        print "<P> A HTTP Path to the search form was not specified. To get help rectifying the error, read the \"Errors\" <BR>
                section, (Error-8) of the \"readme.html\" file.<BR>" 				if ($_[0] eq "8");
        print "<P> No Valid form was found at $form_to_use . To get help rectifying the error, read the \"Errors\" <BR>
                section, (Error-9) of the \"readme.html\" file.<BR>" 				if ($_[0] eq "9");
        print "<P> No Valid file was found at either output_header or output_footer . To get help rectifying the error, read the \"Errors\" <BR>
                section, (Error-10) of the \"readme.html\" file.<BR>" if ($_[0] eq "10");
        print "</FONT>";
        print &Bottom;
 }

#_____Module Returns the Output Document Type______#
sub Header
{
        return "Content-type: text/html\n\n";
}   

#_____Module Returns the Output Document Head_______#
sub Top
{
        my ($title) = @_;

require ("../referer.nsp"); 

$lastdate = `cat date.dat`;

        return <<"ENDPRINT";
<!--Start Main HTML Template-->
<html>
<head>
<title>Coastline Micro, Inc. - QISV Catalogue</title>
<SCRIPT LANGUAGE="JavaScript">
//run current window
function research() {
	parent.location.href = "index.cgi#search";
}
</SCRIPT>
</head>
<body background="../images/qisvbkgd.gif">
<CENTER><h2><font face=verdana, arial, helvetica>Coastline Micro, Inc.<br><br>VID # 1-33-056-4458-800
<br><br>QISV Ordering Address:</H2></font>
<font face=verdana, arial, helvetica SIZE=3>60 Technology Drive<BR>Irvine, CA 92618</font>
</center>
<P>
<HR><BR>
<CENTER><strong><font face=verdana, arial, helvetica size=2>This is a true and accurate copy of the catalogue approved with the General Services Commission.</font></strong></CENTER>
<CENTER><font face=verdana, arial, helvetica SIZE=2>Effective Date of catalogue:<BR><b>June 15, 2001</b></font></CENTER>
<CENTER><font face=verdana, arial, helvetica SIZE=2>This catalogue last updated $lastdate.
<BR>
<form>
<input type="button" value="Search Again" onClick="javascript:research();">
</form>
</CENTER>
<HR>
<BR>
<table width="95%" align="center" cellpadding="3" cellspacing="0" border="0">
<tr><td align="right">
<font face="verdana" size="2">

ENDPRINT
}

#_____Module Returns the Output Document Bottom______#
sub Bottom
{
        return "";
}

#____Module Scans Directories for all Files_____#
sub scandir   
{
        $directory_to_scan = ($_[0]);
        return(<$directory_to_scan/*>);
}

#__Module Returns Only Files of Specified Type__#
sub scantype
{       
my $extension;

        foreach $type (@filetypes){
		$extension = substr($_[0], rindex($_[0], "."));		
                return 1 if($extension eq $type);
        }
}

#____Module Checks for Validity of Directory____#
sub dirs_avoid
{
my $check_dir = ($_[0]);
my $dir; 
 
        foreach $dir (@directories_to_avoid){
                return 0 if(($dir eq $check_dir) || ($check_dir =~ /$dir/));
        }
}       

#______Module Checks for Validity of File______#
sub files_avoid
{
my $check_file = ($_[0]);
my $file;

        foreach $file (@files_to_avoid){
                return 0 if($file eq $check_file);
        }
}

#__Module converts certain ASCII characters into HMTL-CODES__#
sub Ascii_to_html_code{
my $char;
my $word;
my @chars;
my @temp_array;
my @temp_array2;

foreach $word (@get_search_terms){
@chars = split(//,$word);

foreach $char (@chars){
push(@temp_array, $html_codes{$char}) if($html_codes{$char});
push(@temp_array, $char) if!($html_codes{$char});
}
push(@temp_array2, join("",@temp_array));
undef @temp_array;
}

(@get_search_terms) = (@temp_array2);

}

#_Module Prints Message if no Search Terms are Entered_#
sub no_search_terms{
print &Header;
print &Top("No Search Terms Entered");

print<<"ENDPRINT";
        <CENTER><BR><P>No search terms were entered for search. Please try again...</CENTER>
        <FONT SIZE=-1>

							</p>
							</font>
</td></tr>
</table>

<br>
<font face=verdana, arial, helvetica size=2><center>If you have any questions, comments or suggestions, please <font COLOR=#0000FF><a href="../framer.cgi?subject=contact&title=gencomments">E-Mail</a></font> us, Coastline Micro, directly!</center></font>
</body>
</html>
ENDPRINT
print &Bottom;
exit;
}

#_________Module Records Script Usage___________#
sub record_usage{
        open(WRITE,">>site_Search.usage");
        $date = scalar localtime;
        chomp($date);
        print WRITE $date ."|".$ENV{'REMOTE_ADDR'}."|".$ENV{'REMOTE_HOST'}."|"."$search_terms\n";
        close(WRITE);
}

#_________Module Gathers Descriptions___________#
sub get_desc{
my $file_name;
my $description;

open(READ,"site_Search.desc");
while(<READ>){
	($file_name,$description) = split(/[sep]/,$_);
	$desc_array{"$file_name"} = "$description";
}
}

#_______Module Returns the File Mod_Date________#
sub Get_Date{
        $mod_time = time unless ($mod_time);
        ($day,$month,$year) = (localtime($mod_time))[3,4,5];
        $date = "$day $months[$month] 19$year";
        return $date;
}
        
#_Module Returns the Line with the Search Term(s)_#
sub get_line{
my $count;
my $search_term;
my $search_term1;
my $search_terms;
my $sentinel;
my $string;
my @strings;
my $term;
my $hold;
my $val;
my $val1;

$search_terms = $get_search_terms;
$sentinel = -1;

	if ($get_construct eq "As a phrase"){
		$val = index($_,$search_terms);
		$val = $val - ($output_bytes/2);
		$val = 0 if ($val < 0);
		$string =  substr($_,$val,$output_bytes+length($search_terms));		
		$count = $string =~ s/$get_search_terms/\<B\>\<FONT COLOR=\"\#ffffff\"\>$get_search_terms\<\/FONT\>\<\/B\>/g if(($get_case eq "Sensitive") && ($get_type =~ /fuzzy/ig));
		$count = $string =~ s/$get_search_terms/\<B\>\<FONT COLOR=\"\#ffffff\"\>$get_search_terms\<\/FONT\>\<\/B\>/ig if(($get_case eq "Insensitive")  && ($get_type =~ /fuzzy/ig));
		$count = $string =~ s/\b$get_search_terms?\b/\<B\>\<FONT COLOR=\"\#ffffff\"\>$get_search_terms\<\/FONT\>\<\/B\>/g if(($get_case eq "Sensitive") && ($get_type =~ /exact/ig));
		$count = $string =~ s/\b$get_search_terms?\b/\<B\>\<FONT COLOR=\"\#ffffff\"\>$get_search_terms\<\/FONT\>\<\/B\>/ig if(($get_case eq "Insensitive") && ($get_type =~ /exact/ig));
		return  "<FONT SIZE=\"2\" FACE=\"HELVETICA\">$string</FONT><BR>" if ($count > 0);
	}

	$hold = lc($_) if ($get_case eq "Insensitive");
	$hold = ($_) if ($get_case eq "Sensitive");
	foreach $search_term (@get_search_terms){
		$search_term = lc($search_term) if ($get_case eq "Insensitive");
		$pos = 0;
		while($sentinel == -1){
			$search_term1 = $search_term;
			$search_term1 =~ s/(\\)//gi;
			$search_term = $search_term1;
			$val = index($hold,$search_term,$pos);
			$val1 = index($hold," ",$val);
			$term = substr($hold,$val,$val1-$val);
			if (($term eq $search_term) || ($val == -1)){
				$sentinel = 1;
			}else{
				$pos = $val+1;
			}
		}
		$val = index($hold,$search_term) if($val == -1);
		$val = $val - ($output_bytes/2);
		$val = 0 if ($val < 0);
		$string =  substr($_,$val,$output_bytes+length($search_term));
		$search_term =~ s/(\\|\||\(|\)|\[|\{|\^|\$|\*|\+|\?|\.)/\\$1/g;
		$count = ($string =~ s/$search_term/\<B\>\<FONT COLOR=\"\#ffffff\"\>$search_term\<\/FONT\>\<\/B\>/ig) if(($get_case eq "Insensitive")  && ($get_type =~ /fuzzy/ig));
		$count = ($string =~ s/$search_term/\<B\>\<FONT COLOR=\"\#ffffff\"\>$search_term\<\/FONT\>\<\/B\>/g) if(($get_case eq "Sensitive")  && ($get_type =~ /fuzzy/ig));
		$count = ($string =~ s/\b$search_term?\b/\<B\>\<FONT COLOR=\"\#ffffff\"\>$search_term\<\/FONT\>\<\/B\>/ig) if(($get_case eq "Insensitive") && ($get_type =~ /exact/ig));
		$count = ($string =~ s/\b$search_term?\b/\<B\>\<FONT COLOR=\"\#ffffff\"\>$search_term\<\/FONT\>\<\/B\>/g) if(($get_case eq "Sensitive") && ($get_type =~ /exact/ig));
		$string =~ s/(\\)//gi;
		push(@strings,"<FONT SIZE=\"2\" FACE=\"HELVETICA\">$string</FONT><BR><BR>") if ($count > 0);
		$sentinel = -1;
	}
	$string = join("",@strings);
	return "$string";

}

#_________Module Returns the no of Hits__________#
sub get_hits{
$_ = $file_to_search;
my @hits;
my $hits;
my $search_term;
my $search_term2;
my $get_search_terms2;
my $line;
my @lines;

$get_search_terms2  = $get_search_terms;

if ($get_type =~ /exact/i){
if ($get_construct eq "As a phrase"){
	((@hits) = /\b$get_search_terms2\b/og)  if ($get_case eq "Sensitive");
        ((@hits) = /\b$get_search_terms2\b/iog) if ($get_case eq "Insensitive");
	$hits = int(scalar(@hits));
	$get_search_terms2 =~ s/\\//g;
	return "<FONT class=regtextnobold><LI><b>$hits</b> occurence(s) of the search term <B>$get_search_terms2</B></li></FONT><BR>"; 
}


foreach $search_term (@get_search_terms){
($hits = (@hits = /\b$search_term\b/g)) if ($get_case eq "Sensitive");
($hits = (@hits = /\b$search_term\b/ig)) if ($get_case eq "Insensitive");
$search_term2 = $search_term;
$search_term2 =~ s/\\//g;
push(@lines,"<FONT class=regtextnobold><LI><b>$hits</b>  occurence(s) of the search term <B>$search_term2</B></LI></FONT><br>"); 
}

$line = join("",@lines);
return $line."<BR>";
}

if ($get_type =~ /fuzzy/i){
if ($get_construct eq "As a phrase"){
	((@hits) = /.*?$get_search_terms2.*?/og)  if ($get_case eq "Sensitive");
        ((@hits) = /.*?$get_search_terms2.*?/iog) if ($get_case eq "Insensitive");
	$hits = int(scalar(@hits));
	$get_search_terms2 =~ s/\\//g;
	return "<FONT class=regtextnobold><LI><b>$hits</b> occurence(s) of the search term <B>$get_search_terms2</B></LI></FONT><BR>"; 
}


foreach $search_term (@get_search_terms){
($hits = (@hits = /.*?$search_term.*?/g)) if ($get_case eq "Sensitive");
($hits = (@hits = /.*?$search_term.*?/ig)) if ($get_case eq "Insensitive");
$search_term2 = $search_term;
$search_term2 =~ s/\\//g;
push(@lines,"<FONT class=regtextnobold><LI><b>$hits</b>  occurence(s) of the search term <B>$search_term2</B></LI></FONT><br>"); 
}

$line = join("",@lines);
return $line."<BR>";
}

}

#__Module Prints a Message if no Matches are Found___#
sub No_Matches
{
print &Header;
print &Top("No Matches Found");
$search_terms =~ s/\\//g;                
print "<!--<CENTER>Case:$get_case | Type:$get_type | Construct:$get_construct | Hits Per Page:$get_hits | Terms:$search_terms</CENTER><BR><BR>-->";
        print<<"ENDPRINT";
        <CENTER><BR><P><strong>No successful matches were found after the search.
	Please try a different search.</strong></P></CENTER><br>
<!--End CGI/Perl Search Output-->
							</p>
							</font>
</td></tr>
</table>
<br>
<font face=verdana, arial, helvetica size=2><center>If you have any questions, comments or suggestions, please <font COLOR=#0000FF><a href="../framer.cgi?subject=contact&title=gencomments">E-Mail</a></font> us, Coastline Micro, directly!</center></font>
</body>
</html>
<!--End Main Template-->

ENDPRINT
print &Bottom;
exit;
}

#_Module Outputs a Form to Perform Additional Searches_#
sub output_form{
my $files = scalar(@file_names_to_display);
my $list_of_files = $$ . "_list_" . ".html";

open(LIST,">$base_path/$scratch/$list_of_files");

foreach $file (@file_names_to_display){
chomp($file);
print LIST "$file\n";
}	
if ($form_to_use !~ /\binternal\b/){
open(READFORM,"$form_to_use");
@lines = <READFORM>;
return @lines;
}

return <<"ENDPRINT";

<!--End CGI/Search Output-->


							</p>
							</font>
</td></tr>
</table>
<br>
<font face=verdana, arial, helvetica size=2><center>If you have any questions, comments or suggestions, please <font COLOR=#0000FF><a href="../framer.cgi?subject=contact&title=gencomments">E-Mail</a></font> us, Coastline Micro, directly!</center></font>
</body>
</html>
<!--End Main Template-->


ENDPRINT
}

sub Debug{
@get_search_terms = ("geophysics","krishnan","computer");
$get_case = "Insensitive";
$get_construct = "Any search term";
$get_type = "Exact Match";
$get_hits = "ALL";
}
