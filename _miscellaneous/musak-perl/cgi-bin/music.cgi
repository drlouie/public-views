#!D:/Perl/bin/perl.exe

## view all music folders

use CGI ':standard';
print "Content-type: text/html\n\n";

$incomingDir = param('dir');
## Define all folders/files within Pollstuff. Then uncall the files and name the folders.
## This will come up with list of names of all available polls
	$allDirs = "D:/mds/$incomingDir";
	opendir(DIR, $allDirs) or die "can't opendir $allDirs $!";
	while (defined($folder = readdir(DIR))) {
		next if $folder =~ /^\.\.?$/; ## skip . and .. directories
		next if $folder =~ /.txt\.?$/; ## skip .txt files, the SimPoll config files
		next if $folder =~ /.htaccess\.?$/; ## skip .htaccess files, the SimPoll config files
		next if $folder =~ /.htpasswd\.?$/; ## skip .htpasswd files, the SimPoll config files
		## make sure only to push folders, no files
		$folder =~ s/ /%20/gi;
		push(@allFolders,"$folder");
	}

	foreach $af (@allFolders) {
		if ($af eq "dls") {
			print "<a href=\"http://192.168.1.100/cgi-bin/music.cgi?dir=$af\">$af</a><br>";
		}
		elsif ($af eq "SuckedMusic") {
			print "<a href=\"http://192.168.1.100/cgi-bin/music.cgi?dir=$af\">$af</a><br>";
		}
		elsif ($af =~ ".mp3") {
			print "http://192.168.1.100/cgi-bin/fold.cgi?fold=$incomingDir/$af<br>";
		}
		else {
			print "<a href=\"http://192.168.1.100/cgi-bin/fold.cgi?fold=$incomingDir/$af\">$incomingDir/$af</a><br>";
		}
	}	
	

exit;