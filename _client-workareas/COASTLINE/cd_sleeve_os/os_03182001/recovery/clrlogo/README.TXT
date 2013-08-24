BIOS Logo Tools
---------------

INTRODUCTION

This document includes instructions on how to convert and install an OEM
logo into the Flash memory on an Intel motherboard.  These logo utilities
allow either a custom black & white or a custom color graphics logo to be
displayed during the Power-On Self Test each time the system is booted.  
The logo graphics file must first be saved as a bitmap (.BMP) file.  It can 
then be converted from a bitmap (.BMP) file to a user (.USR) file.  This 
user (.USR) file is then flashed into the FLASH ROM memory.

The BWLOGO.EXE utility takes an OEM black and white bitmap (.BMP) file
(generated using a scanner or a graphics application like Microsoft ® Windows (TM) 
Paint) and converts it into a user (.USR) file.  The default name for the new user
(.USR) file is LOGODATA.USR.  The CRLLOGO.EXE utility takes an OEM 
16-color bitmap (.BMP) file and converts it into a user (.USR) file.  The default 
name for the new user (.USR) file is LOGODATA.USR.  Once the file has been
converted to a  .USR file, the iFLASH utility is used to insert or flash the 
user (.USR) file into the FLASH ROM memory.

Note: The CLRLOGO.EXE utility requires that you specify the starting column
position for displaying the logo image, whereas BWLOGO.EXE automatically places the
image in the upper right corner of the screen.

Note: Not all Intel motherboards support these features.  Check the
following Model List for the specific motherboard being used.  In general,
all newer products (Q3'96 or newer) will require the CLRLOGO.EXE utility.
See the list below for specific products.

Models that use BWLOGO.EXE:	Models that use CLRLOGO.EXE:
---------------------------------------------------------------------------------------
	VS440FX 			AP440FX
	Performance/AU			PR440FX
	Advanced/RH			TC430HX	
	Advanced/ML 			(All subsequent motherboards 
	Advanced/ATX				Q3’96 or newer)
	Advanced/AS			 
	Advanced/EV		
	Advanced/MA
	Advanced/MN
	Advanced/ZE
	Advanced/ZP
	
----------------------------------------------------------------------------

INSTRUCTIONS

Before using this logo bitmap utility, save the predesigned graphics logo as
either a black and white or 16 color bitmap (.BMP) file, depending on which
type of logo the motherboard supports.  The color logo bitmap files must be
saved using the standard EGA color palette.

For Black and White Bitmaps:

Use the BWLOGO.EXE file to convert the saved black and white logo from a
bitmap (.BMP) file to a user (.USR) file.  Foreground and Background colors
of the black & white logos can be specified by using the /b<num> and /f<num>
format.  Please refer to the BWLOGO.TXT file for further information

Once this has been done, the user (.USR) file can then be inserted into the
flash ROM memory using the iFLASH utility.  
Create a bootable floppy disk.
	Copy the file IFLASH.EXE and your converted user (.USR) file onto
   	your new bootable floppy disk.
	Insert the floppy into your a: (or respective) drive.
	Reboot the system.
	At the A:\ prompt, type iflash.exe and press Enter
	Press Enter at the title screen.
	Select ‘Update FLASH Memory Area From a File’.
	Select ‘Update User Data Area’.
	Highlight the file to be flashed and press Enter.
	To continue with programming press Enter.
	To reboot the system press Enter. Be sure to remove the floppy from drive a:

For 16-color Bitmaps:

Use the CRLLOGO.EXE file to convert the saved 16-color graphics logo from a
bitmap (.BMP) file to a user (.USR) file.  Please refer to the CRLLOGO.DOC
file for further information.

Once this has been done, the user (.USR) file can then be inserted into the
flash ROM memory using the iFLASH utility.  Follow the same steps as listed
above.

The recommended command lines that are used for the file conversions are:

	For black and white logos ---	BWLOGO [Option] [FileName]

	For 16-color logos --- CRLLOGO /c400/display [FileName]

Note: For information regarding Option Switches that can be used with the 
BWLOGO.EXE and CLRLOGO.EXE, please refer to the BWLOGO.TXT file
and CLRLOGO.DOC respectively.

The BWLOGO.BMP file is an example of a black and white sample logo,
CLRLOGO.BMP is an example of a 16 color sample logo.  To practice converting
and loading a bitmap (.BMP) file, try converting one of these bit map files
into a user (.USR) file.



----------------------------------------------------------------------------
FILE LIST

The following is the list of files included in the BIOS Logo Utilities:

BWLOGO.EXE      ---     The utility that converts black and white bitmap 
                       	    (.BMP) files into user (.USR) files.

BWLOGO.TXT	---	Information about how to use BWLOGO.EXE.

BWLOGO.BMP	---	Sample b/w logo bitmap file.

BWLOGO.USR	---	Sample b/w logo user (.USR) file.

CLRLOGO.EXE	---	The utility that converts 16-color bitmap (.BMP) files
                    	 into user (.USR) files.

CLRLOGO.DOC	---	Information about how to use CRLLOGO.EXE.

CLRLOGO.BMP     ---     Sample 16 color bitmap file.

CLRLOGO.USR     ---     Sample color logo user (.USR) file.


IFLASH.EXE	---     Menu driven utility that can be used to insert .USR
                          files into FLASH memory.

README.TXT	---	This file.

----------------------------------------------------------------------------

EXAMPLES

The following examples indicate typical BWLOGO invocations:

	BWLOGO /tCustom_Logo1 /f2 logo1.bmp

Invoking BWLOGO with this syntax would take the file logo1.bmp and produce
an output file called logodata.usr containing a green on black logo.  The
title 'Custom_Logo1' would be embedded within LOGODATA.USR.

	BWLOGO /tLogo2 /f4 /b1 logo2.bmp

Invoking BWLOGO with this syntax would take the file logo2.bmp and produce
an output file called logodata.usr containing a red on blue logo.  The title
'Logo2' would be embedded within LOGODATA.USR.

	BWLOGO /tOEM_Logo /Fuoem_logo.usr /Fa oem_logo.bmp

Invoking BWLOGO with this syntax would take the file oem_logo.bmp and
produce two output files.  The first would be called oem_logo.usr and would
contain a default white on black logo with the title 'OEM_Logo' embedded
within it.  The second file would be called LOGODATA.ASM and would contain
logo data ready for assembly.


Note: For information about possible Error Messages, please refer to the
appropriate text file.
