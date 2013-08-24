#!/usr/local/bin/perl
#########################################################################
#	The function of this program is to generate a description 	#
#	file to be used with site_Search version 2.01. Please		#
#	configure the "site_Search.conf" file for your site before 	#
#	running this script. To understand a description read the 	#
#	readme.html files.						#
#########################################################################

require("./site_Search.conf") || die "cannot find site_Search.conf file\n";
print "Searching for files ..This may take a moment\n";
&Get_Files_to_Search;

open(WRITE,">site_Search.desc") || die 
"Cannot open site_Search.desc for writing, check permissions and try again!!!\n";

print scalar(@files_to_be_searched) . " files found, creating site_Search.desc\n"; 
foreach $file (@files_to_be_searched)
{
	print WRITE "$file"."[sep]\n";
}	
print "ALL DONE, site_Search.desc created successfully.\n";

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
                return 0 if($dir eq $check_dir);
        }
}

#______Module Checks for Validity of File______#
sub files_avoid
{
my $check_file = ($_[0]);
my $file;

        foreach $file (@files_to_avoid){
                return 0 if($file  eq $check_file);
        }
}

