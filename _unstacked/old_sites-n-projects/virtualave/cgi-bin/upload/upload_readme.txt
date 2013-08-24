Upload/DownloadCopyleft 1997,1998 Kevin Meltzer
##################################Files:	upload.pl - The script!	README - This.
Setup:1. chmod upload.pl to 755
2. $upload_dir should be set to the server path of the base
   directory that you wish to have as the root directory that
   you want to download to.
 To upload to a directory on a server, the directory perms should be set to
 777 to allow for writting. This script will show directories lower than
 where it is placed. For example, if your set up were:
       /home/ns-home/docs/htdocs/cgi-bin/foo/blah/
 and you placed this script in cgi-bin, you will have access to cgi-bin, foo,
 and blah. But, not htdocs. But, people can only upload to dirs which have
 perms set to allow it.                                                           
                                       
3. Email me and tell me where it is being used! kmeltz@cris.com