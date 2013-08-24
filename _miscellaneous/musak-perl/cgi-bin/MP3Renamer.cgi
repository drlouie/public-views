#!D:/Perl/bin/perl.exe

## view all folder files

use CGI ':standard';
print "Content-type: text/html\n\n";

$elDirectorio = '2 Bad Mice';
## This will come up with list of names of all available files
	$allDirs = "D:/downs/$elDirectorio";
	opendir(DIR, $allDirs) or die "can't opendir $allDirs $!";
	while (defined($file = readdir(DIR))) {
		next if $file =~ /^\.\.?$/; ## skip . and .. directories
		## make sure only to push folders, no files
		$splitted = ' - ';
		@splitFile = split(/$splitted/,$file);
		@REVERSED = reverse @splitFile;
		$newFileName = "$REVERSED[0]";
		print "$newFileName<br>";
#		rename("D:/downs/$elDirectorio/$file","D:/downs/$elDirectorio/$newFileName")
	}

exit;