#!/usr/bin/perl5 -s

print "Content-type: text/html\n\n";

$allBadMail = "/var/spool/mqueue";
opendir(DIR, $allBadMail) or die "can't opendir $allBadMail";
while (defined($file = readdir(DIR))) {
	next if $file =~ /^\.\.?$/; ## skip . and .. directories
	push(@allFiles,"$file");
}
foreach $unaFila (@allFiles) {
	$thisFile = "/var/spool/mqueue/" . $unaFila;
	print "$thisFile DELETED!\n";
	chmod(7777, $thisFile);
	unlink($thisFile) || &error('cant delete $thisFile');

}

sub error {
	print "error\n";
}
exit;