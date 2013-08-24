#!/usr/bin/perl5 -w

# -------------- >>>  Test location of request
require ("referer.nsp");

print "Content-type: text/html\n\n";

BEGIN {
    $userid = 0; # -------------- >>> This Number is the specific ID - ID number assigned to you on your Unix System.
    $groupid = 0; # -------------- >>> This Number is the specific Group - ID number assigned to people with your access level on your Unix system.
				  # -------------- >>> You can gain your $userid and $groupid by typing 'id' at your - UNIX prompt.  (GID = Group Id, UID = User Id).
    $overwrite = 0; # -------------- >>> Set this value to '1' to allow overwriting of existing files.
                    # -------------- >>> Set this value to '0' to dis-allow the overwriting of existing files.
                    # -------------- >>> NOTE: Existing files WILL NOT be over-written unless they are given the permissions 'a+rw'.  An error message will return to users who try to over-write files which are protected.
    $Windows = 0; # -------------- >>> $Windows allows you to specifiy if you are using the Windows operating system or not.  If you are not running this script under Microsoft Windows, set this value to zero ('0').  If you are running under Windows, set this value to one. ('1')
    $exclusive_lock = 2; # -------------- >>> DO NOT CHANGE THIS VALUE - It should be set to '2'
    $unlock_lock = 8; # -------------- >>> DO NOT CHANGE THIS VALUE - It should be set to '8'
}

$| = 1;
&GetInput;
&Process_File;
&GoodOne;

sub GetInput {
    # -------------- >>> Loads CGI module, assigns $filename the filename the file should be saved as.
    use CGI qw(:standard);
    $CGI::OS = 'WINDOWS' if ($Windows);
    $query = new CGI;
	$filename = $query->param('uploadfile');
    $Type = $query->param('Type');
    $SubType = $query->param('SubType');
    $BackTrack = $query->param('Script');
    $FeedMe = $query->param('FeedMe');
    $Width = $query->param('Width');
    $Height = $query->param('Height');
	$WinWidth = $Width + 10;
	$WinHeight = $Height + 25;
    $path = "/usr/local/www/vhosts/coastlinemicro.com/htdocs/dbimages/$Type";
}


sub Process_File {
    # -------------- >>> Takes all the input, determines if the user is using the appropiate browser, then extracts the filename, and saves the file.  Uploaded files are chmodded to 644, and given ownership to the user defined in $userid and $groupid.
    &Exit_Not_A_Netscape_User if ($ENV{'HTTP_USER_AGENT'} !~ /^Mozilla\/[432]/);

    if ($filename =~ /\//) {
        @array = split(/\//, $filename);
        $real_name = pop(@array);
    } elsif ($filename =~ /\\/) {
        @array = split(/\\/, $filename);
        $real_name = pop(@array);
    } else {
        $real_name = "$filename";
    }

	## if image file
	if ($real_name =~ ".jpg" || $real_name =~ ".gif") { $continueit=1; }
	## else error
	else {
		&topper;
        print "<font color=\"#EB0000\"><b>Error </b><br>The file you are attempting to upload is not being recognized by the system as being an image. Please make sure the file you are attempting to upload is named correctly with either a .JPG or .GIF extension.<br><br><center>Your File: <b>$real_name</b></center></font>";
		&bottom;
        exit;
	}
	## if image name contains spaces send error
	if ($real_name =~ " ") { 
		&topper;
        print "<font color=\"#EB0000\"><b>Error </b><br>The file you are attempting to upload contains a space in it's name. Please remove the space from the file's name and try uploading the file again.<br><br><center>Your File: <b>$real_name</b></center></font>";
		&bottom;
        exit;
	}
	## else continue
	else { $continueit=1; }
	
	$OLDreal_name = "$real_name";
	## make new filename
	$outfile = "$path" . "/" . "$real_name";	
    $filename = $query->param('uploadfile');

    &Exit_File_Exists if ((-e "$outfile") && (!$overwrite));

    if (!open(OUTFILE, ">$outfile")) {
		&topper;
        print "<font color=\"#EB0000\"><b>Administrator Error </b><br>Make sure that the directory: $path has been chmodded with the permissions '777'. $!<br><br>Please report this error to Coastline Micro, Inc.</font>";
		&bottom;
        exit;
    }

    while ($bytesread = read($filename,$buffer,1024)) {
        $totalbytes += $bytesread;
        binmode OUTFILE;
        print OUTFILE $buffer;               
    }

    close($filename);
    close(OUTFILE);

    if ((stat $outfile)[7] < 1) {
        unlink $outfile;
        &Exit_Size_Error;
    }
    chmod (0644, "$outfile")              if (!$Windows);
    chown ($userid, $groupid, "$outfile") if (!$Windows);
}

# -------------- >>> Succcess INFORM (hehe!) Originating Script.
sub GoodOne {

{
print <<EOF

<html>
<head>
<title>Shark Tank Admin System - File Uploader</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="admincss.cgi" Type="text/css">
<script language="Javascript">
// CROSS-BROWSER FORM CHECKER
// By Drlouie \@ NetMedia Solutions
// info\@NetMediaSol.com for help
// Copyright 2001 NetMedia Solutions

function checkForm() {
var missingdrop = "";
var thefirst = "";

// Check Common form fields
if (document.save.Description.value == "" || document.save.Description.value == " ") {
    missingdrop += "\\n     - Description";
	thefirst = "Description";
}

if (document.save.Keywords.value == "" || document.save.Keywords.value == " ") {
    missingdrop += "\\n     - Keywords";
	if (thefirst == "") { thefirst = "Keywords"; }
}

// If anything comes back wrong alert and detain form, else submit info
if (missingdrop != "") {
    missingdrop ="___________________________________________                   \\n\\n" + "  Sorry, I cannot process your request because the\\n  following fields are either blank or filled incorrectly:\\n" + "___________________________________________                   \\n\\n" +
    missingdrop + "\\n\\n___________________________________________                   " + "\\n\\n   To continue, check fields and submit form again!" + "\\n___________________________________________";
    alert(missingdrop);
	document.save(thefirst).focus();
    return false;
} 
else {
return true;
}
}
</script>
<script language="Javascript">
function iPreview() {
window.open('http://www.rhomberg.com/systemConfigurator/dbimages/$Type/$real_name','PREVIEW','width=400,height=400');
}
</script>
</head>
<body bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">

<form action="$BackTrack" method="post" onSubmit="return checkForm();" name="save">
<input type="hidden" name="SAVEONE" value="1">
<input type="hidden" name="Type" value="$Type">
<input type="hidden" name="SubType" value="$SubType">
<input type="hidden" name="Width" value="$Width">
<input type="hidden" name="Height" value="$Height">
<input type="hidden" name="FileName" value="$real_name">
<input type="hidden" name="InnerURL" value="dbimages/$Type/$real_name">
<input type="hidden" name="OuterURL" value="http://www.rhomberg.com/systemConfigurator/dbimages/$Type/$real_name">
<input type="hidden" name="FeedMe" value="$FeedMe">
  <table border="0" cellpadding="0" cellspacing="0" align="left">
    <tr valign="top"> 
      <td align="left"> 
        <table border="0" cellspacing="0" cellpadding="0" width="280" align="left">
          <tr> 
          <td colspan="2"> 
            <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER">
              <tr bordercolor="#333366"> 
                <td width="100%" align="center" valign="top"> 

                    <table width="100%" border="0" cellspacing="0" cellpadding="0">
                      <tr> 
                      <td width="100%" align="center"> 

                          <table width="100%" border="0" cellspacing="0" cellpadding="0">
                            <tr> 
                              <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                              <td height="20" bgcolor="#8F8FAB" colspan="2"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Upload 
                                Image</font></b></font></td>
                              <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                            </tr>
                            <tr> 
                              <td colspan="4" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                            </tr>
                            <tr> 
                              <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                              <td height="15" bgcolor="#F2F2F7" align="center" colspan="2"><img src="images/verticalbar.gif" width="15" height="15"></td>
                              <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                            </tr>
                            <tr> 
                              <td width="15" bgcolor="#F2F2F7" rowspan="10">&nbsp;</td>
                              <td height="315" align="left" colspan="2" valign="top"> 
                                <font face="verdana,arial,helvetica" size="1"><b>Upload was successful!</b><br>
                                Your image upload was successful and is now saved 
                                to the system. Following are the characteristics 
                                of the saved file with it's system filename.<br>
                                <br>
                                Now you must configure the marketing data for 
                                this image. The marketing data allows the system 
                                to have extra information available for the store's 
                                viewing user. <br>
                                <br>
                                <b>Instructions</b><br>
                                First of all, type in a description for this image. 
                                <br>
                                Example: <i>Intel Pentium III Processor - Now 
                                available in all our Thresher Series Desktop Systems.</i><br>
                                <br>
                                Next, type in some keywords for this image. Keywords 
                                on an image allow for the administrator(s) of 
                                the system to find images while administering 
                                the system.<br>
                                <br>
                                Now just click 'Save Database Info' to finish 
                                the image upload process. Sorry we couldn't make 
                                this process any easier...<br>
                                </font></td>
                              <td width="15" bgcolor="#F2F2F7" rowspan="10">&nbsp;</td>
                            </tr>
                            <tr> 
                              <td height="25" align="right" width="100"><font face="verdana,arial,helvetica" size="1"><b>Your 
                                file</b>&nbsp;&nbsp;</font></td>
                              <td height="25" align="left" width="148"><font face="verdana,arial,helvetica" size="1">&nbsp;&nbsp;$OLDreal_name</font></td>
                            </tr>
                            <tr> 
                              <td height="25" align="right" width="100"><font face="verdana,arial,helvetica" size="1"><b>Server 
                                file</b>&nbsp;&nbsp;</font></td>
                              <td height="25" align="left" width="148"><font face="verdana,arial,helvetica" size="1">&nbsp;&nbsp;$real_name</font></td>
                            </tr>
                            <tr> 
                              <td height="25" align="right" width="100"><font face="verdana,arial,helvetica" size="1"><b>Type</b>&nbsp;&nbsp;</font></td>
                              <td height="25" align="left" width="148"><font face="verdana,arial,helvetica" size="1">&nbsp;&nbsp;$Type</font></td>
                            </tr>
                            <tr> 
                              <td height="25" align="right" width="100"><font face="verdana,arial,helvetica" size="1"><b>Sub 
                                Type</b>&nbsp;&nbsp;</font></td>
                              <td height="25" align="left" width="148"><font face="verdana,arial,helvetica" size="1">&nbsp;&nbsp;$SubType</font></td>
                            </tr>
                            <tr> 
                              <td height="25" align="right" width="100"><font face="verdana,arial,helvetica" size="1"><b>Parameters 
                                </b>&nbsp;&nbsp;</font></td>
                              <td height="25" align="left" width="148"><font face="verdana,arial,helvetica" size="1">&nbsp;&nbsp;$Width 
                                W - $Height H</font></td>
                            </tr>
                            <tr> 
                              <td height="25" align="right" width="100"><font face="verdana,arial,helvetica" size="1"><b>File 
                                Size</b>&nbsp;&nbsp;</font></td>
                              <td height="25" align="left" width="148"><font face="verdana,arial,helvetica" size="1">&nbsp;&nbsp;$totalbytes 
                                Bytes</font></td>
                            </tr>
                            <tr> 
                              <td height="25" align="right" width="100"><font face="verdana,arial,helvetica" size="1"><b>Preview</b>&nbsp;&nbsp;</font></td>
                              <td height="25" align="left" width="148"><font face="verdana,arial,helvetica" size="1">&nbsp;&nbsp;<a href="javascript:iPreview()" color="#333366">$real_name</a></font></td>
                            </tr>
                            <tr> 
                              <td height="25" align="right" width="100"><font face="verdana,arial,helvetica" size="1"><b>Description</b>&nbsp;&nbsp;</font></td>
                              <td height="25" align="left" width="148"><font face="verdana,arial,helvetica" size="1">&nbsp;&nbsp; 
                                <input type="text" name="Description" size="15" class="inputtext15">
                                </font></td>
                            </tr>
                            <tr> 
                              <td height="25" align="right" width="100"><font face="verdana,arial,helvetica" size="1"><b>Keywords</b>&nbsp;&nbsp;</font></td>
                              <td height="25" align="left" width="148"><font face="verdana,arial,helvetica" size="1"> 
                                &nbsp;&nbsp; 
                                <input type="text" name="Keywords" size="15" class="inputtext15">
                                </font></td>
                            </tr>
                            <tr> 
                              <td align="center" colspan="4" valign="middle" height="75" width="100%" bgcolor="#F2F2F7"> 
                                <input type="submit" value="Save Database Info" name="submit" class="inputbut">
                                <font face="verdana,arial,helvetica" size="1"><br>
                                <br>
                                </font> 
                                <input type="reset" value="Reset Form" name="reset" class="inputbut">
                              </td>
                            </tr>
                          </table>
</td></tr></table></td></tr></table></td></tr></table><br>
      </td>
    </tr></table>
</form></body></html>

EOF
}
exit;
}

sub Exit_Not_A_Netscape_User {
    # -------------- >>> This user is not using a compatible browser for the upload...
	&topper;
    print "<font color=\"#EB0000\"><b>Error </b><br>Sorry, but you must have an updated browser with file upload capabilities in order to use the uploading capabilities of this site. Please return with a different browser in order to continue with this process.<br><br><center>Your Browser: <b>$Agent</b></center></font>";
	&bottom;
    exit;
}

sub Exit_File_Exists {
    # -------------- >>> This user is trying to upload a file with a filename that is already in use, and this script is set not to overwrite existing files.
	&topper;
    print "<font color=\"#EB0000\"><b>Error </b><br>Sorry, but this system is not allowed to overwrite existing files. The file you are attempting to upload has the same name as a file already in use by the system. Please change the name of the file you are attempting to upload, and try again.<br><br><b>Note</b><br>If you are attempting to update an image currently being used by the system please use the 'Update Image' function instead.<br><br><center>Your File: <b>$real_name</b></center></font>";
	&bottom;
    exit;
}

sub topper {
{
print <<EOF
<html>
<head>
<title>Shark Tank Admin System - File Uploader</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="admincss.cgi" Type="text/css">
</head>
<body bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<form enctype="multipart/form-data" action="uploader.cgi" method="post" onSubmit="return checkForm();" name="upload">
<table border="0" cellpadding="0" cellspacing="0" align="center">
  <tr valign="top"> 
    <td align="center"> 
      <table border="0" cellspacing="0" cellpadding="0" width="300" align="center">
        <tr> 
          <td colspan="2"> 
            <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER">
              <tr bordercolor="#333366"> 
                <td width="100%" align="center" valign="top"> 

                    <table width="100%" border="0" cellspacing="0" cellpadding="0">
                      <tr> 
                      <td width="100%" align="center"> 

                          <table width="100%" border="0" cellspacing="0" cellpadding="0">
                            <tr> 
                              <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                              <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Upload 
                                Image</font></b></font></td>
                              <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                            </tr>
                            <tr> 
                              <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                            </tr>
                            <tr> 
                              <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                              <td bgcolor="#F2F2F7" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1"><br>
					  
EOF
}
}
exit;

sub bottom {
{
print <<EOF

								<br><br></font></td>
                              <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                            </tr>
                          </table>

                        </td>
                    </tr>
              <tr bordercolor="#333366" bgcolor="#F2F2F7"> 
                  <td align="center" valign="middle" height="45" width="100%" bgcolor="#F2F2F7" bordercolor="#333366"><input type="button" value="Try Again" name="button" class="inputbut" onClick="javascript:history.go(-1);"></td>
              </tr>
                  </table>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
      <br>
    </td>
  </tr>
</table>
</form>
</body>
</html>

EOF
}
}
exit;
