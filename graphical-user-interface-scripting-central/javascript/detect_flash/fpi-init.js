// moock fpi [f.lash p.layer i.nspector]
// version: 1.3.4
// written by colin moock
// code maintained at: http://www.moock.org/webdesign/flash/detection/moockfpi/
// unrestricted use permission granted for:
// 		artists, educational institutions and non-profit organizations. 
// restricted use permission granted for commercial purposes under linkware agreement terms set out
// 		at the above url...



// #############################################
// these are the user defined globals
// modify the following variables to customize the inspection behaviour

var requiredVersion = 4;			// version the user needs to view site (max is 5, min is 2)
var useRedirect = true; 			// "true" loads new flash or non-flash page into browser
									// "false" embeds movie or alternate html code into current page

// set next three vars if useRedirect is true...
var flashPage = "movie.html"		// the location of the flash movie page
var noFlashPage = "noflash.html"	// send user here if they don't have the plugin or we can't detect it
var upgradePage = "upgrade.html"	// send user here if we detect an old plugin
// #############################################



// *************
// everything below this point is internal until after the body tag
// do not modify! 
// *************

// system globals
var flash2Installed = false;		// boolean. true if flash 2 is installed
var flash3Installed = false;		// boolean. true if flash 3 is installed
var flash4Installed = false;		// boolean. true if flash 4 is installed
var flash5Installed = false;		// boolean. true if flash 5 is installed
var maxVersion = 5;					// highest version we can actually detect
var actualVersion = 0;				// version the user really has
var hasRightVersion = false;		// boolean. true if it's safe to embed the flash movie in the page
var jsVersion = 1.0;				// the version of javascript supported