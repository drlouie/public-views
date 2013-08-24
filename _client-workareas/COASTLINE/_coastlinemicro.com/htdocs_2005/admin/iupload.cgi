#!/usr/bin/perl5 -w

## Test location of request
require ("referer.nsp");

print "Content-type: text/html\n\n";
## Snif thisurl, in case user needs to login you have somewhere to send em back to
$lasturl = "$ENV{'SCRIPT_NAME'}";
## Snif cookie, if present test for logged in status
require ("cookiesnif.nsp");
## If comes back dead a login prompt was called, kill current process
if ($exit eq '1') { exit; }
## else continue with process

## Check to see if the logged user is granted rights to this action script
if (($Cookies{'UserType'} eq "COManage") || ($Cookies{'UserType'} eq "WEBAdmin")) { $nextone = "1"; }
else {
	$noaccess = `cat noaccess.nsf`;
	print "$noaccess";	
	exit;
}

## Grab User Input
require ("parse_query.nsp");

## script's name
$script = "$ENV{'SCRIPT_NAME'}";
## grab admin date format
require ("date.nsp");

## get perl built dynamic DHTML menu js
my $MenuConfig = `cat js/menu_config.js`;
my $MenuConstructor = `cat js/menu_constructor.js`;
my $MenuConfig = "<script langauage=\"Javascript\">\n$MenuConfig\n</script>";
my $MenuConstructor = "<script langauage=\"Javascript\">\n$MenuConstructor\n</script>";

## get CM legal piece
$legal = `cat legal.nsf`;
if ($FORM{'SAVEONE'}) {

my $Type = "$FORM{'Type'}";
my $SubType = "$FORM{'SubType'}";
my $Width = "$FORM{'Width'}";
my $Height = "$FORM{'Height'}";
my $FileName = "$FORM{'FileName'}";
my $InnerURL = "$FORM{'InnerURL'}";
my $OuterURL = "$FORM{'OuterURL'}";
my $Description = "$FORM{'Description'}";
my $Keywords = "$FORM{'Keywords'}";
my $FeedMe = "$FORM{'FeedMe'}";
my $ActionUser = "$Cookies{'Username'}";

	## SAVE INFO TO NEW DB TABLE DATA ROW
	use DBI; 
	my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>NMS-SysConfigurator</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $sth = $dbh->prepare("INSERT INTO Images (ImageID, Type, SubType, FileName, Width, 
							 Height, InnerURL, OuterURL, Description, Keywords, 
							 UseCount, AddedBy, AddedOn, ModifiedBy, ModifiedOn)
						 
						 	VALUES (Null, '$Type', '$SubType', '$FileName', 
							'$Width', '$Height', '$InnerURL', '$OuterURL', 
							'$Description', '$Keywords', '1', '$ActionUser', 
							Null, '', '')");
	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish; 


	my $sth = $dbh->prepare("SELECT * FROM Images WHERE Type='$Type' AND SubType='$SubType' AND FileName='$FileName'");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		$ImageID = $row[0];
	}
	$sth->finish; 
	$dbh->disconnect; 
	
# START HTML
&topper;

{
print <<EOF

<script language="Javascript">
function feedInfo() {

parent.document.change.$FeedMe.value = "$ImageID";
parent.document.change.$FeedMe.style.color = "EB0000";

}
</script>
</head>
<body bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onLoad="Javascript:feedInfo();">
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
                              <td height="105" bgcolor="#F2F2F7" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1">
                                <b>Save Successful</b><br>
								All information was successfully saved to the system. Now you are finally done with the image upload process. The ImageID number for the image you just uploaded will automatically fill the field in the main document's form to your right (<font color="#EB0000">RED TEXT</font>).
								<br>
                                </font> </td>
                              <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                            </tr>
                          </table>

                        </td>
                    </tr>
                  </table>
				  
EOF
}
&bottom;
}


## -------------------------->>> NO INPUT
elsif ($FORM{'Type'} && $FORM{'SubType'} && $FORM{'FeedMe'}) {

$Type = $FORM{'Type'};
$SubType = $FORM{'SubType'};
$FeedMe = $FORM{'FeedMe'};

## dist AND mfg
if ($Type eq "mfg" || $Type eq "dist") {
	if ($SubType eq "small") { $Width = "85"; $Height = "65"; $TheType = "Small Photo"; }
	elsif ($SubType eq "emblem") { $Width = "85"; $Height = "65"; $TheType = "Product Emblem"; }
	elsif ($SubType eq "medium") { $Width = "125"; $Height = "85"; $TheType = "Medium Photo"; }
	## large
	else { $Width = "165"; $Height = "105"; $TheType = "Large Photo"; }
	$Alert = "FILE CLASSIFICATION\\nIf you are attempting to upload a new image to the system for the profile you are currently working on, keep in mind that the $TheType you are uploading must meet the following system criteria for that specific image class.\\n\\nImage Properties\\n    Image Class - $TheType\\n    Image Type(s) Accepted - .JPG and .GIF\\n    Image Width - $Width Pixels\\n    Image Height - $Height Pixels\\n\\n\\nFILE NAMING EXAMPLES\\nThe naming convention for the file(s) you are attempting to upload must meet the following system criteria. The system does not care if a file\\'s name is lower or upper case, as long as there are no spaces or illegal characters in a file\\'s name. Also, your file must be either a .JPG or .GIF file, no other file types will be accepted via this uploader.\\n\\nProperly Named Files\\n    small_rm1u815.jpg\\n    large1_rm1u815.jpg\\n    large2_rm1u815.jpg\\n    large3_rm1u815.jpg\\n    small_rm1u815.gif\\n    large1_rm1u815.gif\\n    large2_rm1u815.gif\\n    large3_rm1u815.gif\\n\\nImproperly Named Files\\n    small.rm1u815.jpg\\n    large1_rm1u815.zip\\n    large 2 rm1u815.jpg\\n    largethresherseriesrm1u815.jpg";
}
### prod_common
else {
	if ($SubType eq "small") { $Width = "165"; $Height = "100"; $TheType = "Small Photo"; }
	elsif ($SubType eq "emblem") { $Width = "85"; $Height = "65"; $TheType = "Product Emblem"; }
	## large
	else { $Width = "250"; $Height = "250"; $TheType = "Large Photo"; }
	$Alert = "FILE CLASSIFICATION\\nIf you are attempting to upload a new image to the system for the product you are currently working on, keep in mind that the $TheType you are uploading must meet the following system criteria for that specific image class.\\n\\nImage Properties\\n    Image Class - $TheType\\n    Image Type(s) Accepted - .JPG and .GIF\\n    Image Width - $Width Pixels\\n    Image Height - $Height Pixels\\n\\n\\nFILE NAMING EXAMPLES\\nThe naming convention for the file(s) you are attempting to upload must meet the following system criteria. The system does not care if a file\\'s name is lower or upper case, as long as there are no spaces or illegal characters in a file\\'s name. Also, your file must be either a .JPG or .GIF file, no other file types will be accepted via this uploader.\\n\\nProperly Named Files\\n    small_rm1u815.jpg\\n    large1_rm1u815.jpg\\n    large2_rm1u815.jpg\\n    large3_rm1u815.jpg\\n    small_rm1u815.gif\\n    large1_rm1u815.gif\\n    large2_rm1u815.gif\\n    large3_rm1u815.gif\\n\\nImproperly Named Files\\n    small.rm1u815.jpg\\n    large1_rm1u815.zip\\n    large 2 rm1u815.jpg\\n    largethresherseriesrm1u815.jpg";
}

&topper;
{
print <<EOF

<script language="Javascript">
alert('$Alert');
// CROSS-BROWSER FORM CHECKER
// By Drlouie \@ NetMedia Solutions
// info\@NetMediaSol.com for help
// Copyright 2001 NetMedia Solutions

function checkForm() {
var missingdrop = "";
var thefirst = "";

// Check Common form fields
if (document.upload.uploadfile.value == "" || document.upload.uploadfile.value == " ") {
    missingdrop += "\\n     - You must choose a file to upload";
	thefirst = "uploadfile";
}

// If anything comes back wrong alert and detain form, else submit info
if (missingdrop != "") {
    missingdrop ="___________________________________________                   \\n\\n" + "  Sorry, I cannot process your request because the\\n  following fields are either blank or filled incorrectly:\\n" + "___________________________________________                   \\n\\n" +
    missingdrop + "\\n\\n___________________________________________                   " + "\\n\\n   To continue, check fields and submit form again!" + "\\n___________________________________________";
    alert(missingdrop);
	document.upload(thefirst).focus();
    return false;
} 
else {
return true;
}
}
</script>
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
                              <td height="305" bgcolor="#F2F2F7" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1"><b>Description</b><br>
                                To upload an image please follow the directions 
                                below carefully. Keep in mind that this specific 
                                screen/function will NOT allow you to overwrite 
                                files already in the system. If you would like 
                                to update an image currently being used by the 
                                system, use the 'Image Update' function instead.<br>
                                <br>
                                <b>Instructions</b><br>
                                To select an image to upload, click 'Browse'. 
                                Find the image file within your system that you 
                                would like to upload. Once you have located the 
                                file you want double-click it. The path to the 
                                file you are about to upload should now be visible 
                                in the field next to the Browse button. Now click 
                                'Upload My File'. <br>
                                <br>
                                <font color="#EB0000"><b>Precautions</b><br>
                                - Filename can only contain alpha-numeric characters<br>
                                - Files must be at least 1 byte in size<br>
                                - No spaces allowed in filename<br>
                                - The system only supports JPG and GIF image filetypes<br>
                                </font></font> </td>
                              <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                            </tr>
                            <tr> 
                              <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                              <td height="55" align="center">
                                <input type="hidden" name="Type" class="inputtext" value="$Type">
                                <input type="hidden" name="SubType" class="inputtext" value="$SubType">
                                <input type="hidden" name="Width" class="inputtext" value="$Width">
                                <input type="hidden" name="Height" class="inputtext" value="$Height">
                                <input type="hidden" name="FeedMe" class="inputtext" value="$FeedMe">
                                <input type="hidden" name="Script" class="inputtext" value="$script">
								<nobr><font face="verdana,arial,helvetica" size="1" color="#333366">Choose Your File :&nbsp;&nbsp;</font><input type="file" name="uploadfile" size="15" class="inputtext15"></nobr></td>
                              <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                            </tr>
                          </table>

                        </td>
                    </tr>
              <tr bordercolor="#333366" bgcolor="#F2F2F7"> 
                  <td align="center" valign="middle" height="45" width="100%" bgcolor="#F2F2F7" bordercolor="#333366"> 
                    <input type="submit" value="Upload My File" name="submit" class="inputbut">
                    <input type="reset" value="Reset Form" name="reset" class="inputbut">
                    &nbsp;</td>
              </tr>
                  </table>

EOF
}
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
		  
EOF
}
}
exit;

sub bottom {
{
print <<EOF

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
</body>
</html>

EOF
}
}
exit;
