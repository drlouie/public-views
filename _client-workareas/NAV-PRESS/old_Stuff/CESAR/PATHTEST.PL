#!/usr/bin/perl5.00404


                     ### *** IMPORTANT FOR UNIX *** ###

          ### *** Make sure the path to PERL above is correct *** ###

	#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#
	#
	# Program is copyright by Ranson's Scripts all rights reserved
	# Email - support@rlaj.com
	#
	# Program Name ------- pathtest.pl 
	# Program Version ---- 2.0
	# Configuration File - none
	# 
	#
	#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#


print "Content-type: text/html\n\n";

$Perl_Version = "Perl Version $]";

if (-d "C:/" || $^O eq "MSWin32") {
	$windows = 1;
	$platform = "WINDOWS";

} elsif (-e "/etc") {
	$unix = 1;
	$platform = "UNIX";

} else {
	$unix = 1;
	$platform = "UNKNOWN PLATFORM";
}

foreach $key (keys(%ENV)) {
if ($key =~ /cookie/i) { $key = "" }
$My_Key .= "<TR><TD>$key<TD> $ENV{$key}</TD></TR>\n";
if ($ENV{$key} =~ /\w:\\.+\\pathtest.pl/ && $windows eq "1") { $path = "$ENV{$key}"; }
}
if ($0 =~ /pathtest.pl/) { $path = "$0"; }
elsif ($ENV{'SCRIPT_FILENAME'}) { $path = "$ENV{'SCRIPT_FILENAME'}"; }
if ($ENV{'DOCUMENT_ROOT'} ne "") { $document_root = "<B>Document Root:</B> <FONT COLOR=FF0000>$ENV{'DOCUMENT_ROOT'}</FONT>"; }

$path =~ s/pathtest\.pl//;
$path =~ s/\\$//;
$path =~ s/\/$//;


if ($platform eq "UNIX") {
$Sendmail = `whereis sendmail`;
}

@Sendmail = split(/\s+/, $Sendmail);

foreach $place(@Sendmail) {
if($place !~ /\./) {
push(@SendMail, "$place \&nbsp\; ");
 }
}

if ($platform eq "UNIX") {
$Path_to_Sendmail = "<B>sendmail</B> = <FONT COLOR=F04E00 FACE=arial>@SendMail</FONT><P>";
}


                        ### *** :) *** ###



print <<"EOT";

<HTML>
<HEAD>
<TITLE>Path Test by RLAJ.COM</TITLE>
</HEAD>
<BODY BGCOLOR=FFFFFF TEXT=000000>
<TABLE BORDER=0 BGCOLOR="#FFFFFF" CELLPADDING=2 CELLSPACING=0 Width=100%>
<TR>
<TD><B><FONT FACE="Arial" COLOR="000080" SIZE="+3">&nbsp; &nbsp; Path and Environment Test</FONT></B></TD>
<TD Align=right><FONT SIZE="+1"><A HREF="http://www.rlaj.com">Ranson's Scripts</A></FONT><BR><A HREF="mailto:Support\@rlaj.com">Support\@rlaj.com</A></TD>
</TR>
</TABLE>
<P>
<TABLE BORDER=0 BGCOLOR="000080" CELLPADDING=20 CELLSPACING=0>
<TR><TD>
<CENTER>
<TABLE BORDER=0 BGCOLOR="#FFFFFF" CELLPADDING=9 CELLSPACING=0>
<TR><TD>
<BR>
<B>The operating system is:</B> <FONT COLOR=#F04E00 FACE="arial">$platform</FONT> &nbsp; $Perl_Version
<P>
<B>The path for this file is:</B> <FONT COLOR=#F04E00 FACE="arial">$path</FONT>
<P>
$document_root
<P>
$Path_to_Sendmail
</TD></TR>
</TABLE>
</CENTER>
</TD></TR>
</TABLE>
<BR><BR><BR>
<B><FONT FACE="Arial" COLOR="000080" SIZE="+1">Environment Variables</FONT></B>
<BR><BR>
<TABLE BORDER=0 BGCOLOR="#FFFFFF" CELLPADDING=2 CELLSPACING=0 Width=100%>
$My_Key
</TABLE>

EOT

print "<BR><BR><BR><BR></body></html>";


exit;

                          ### *** *** ###