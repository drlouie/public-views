// next comes the standard javascript detection that uses the navigator.plugins array
// we pack the detector into a function so it loads before we run it

function detectFlash(){	

	if (navigator.plugins){								// does navigator.plugins exist?
		if (navigator.plugins["Shockwave Flash 2.0"] 	// yes>> then is Flash 2 
		|| navigator.plugins["Shockwave Flash"]){		// or flash 3+ installed?

			// set convenient references to flash 2 and the plugin description
			var isVersion2 = navigator.plugins["Shockwave Flash 2.0"] ? " 2.0" : "";
			var flashDescription = navigator.plugins["Shockwave Flash" + isVersion2].description;
			// a flash plugin-description looks like this: Shockwave Flash 4.0 r5
			// so we can get the major version by grabbing the character before the period
			// note that we don't bother with minor version detection. do that in your movie with $version
			var flashVersion = parseInt(flashDescription.charAt(flashDescription.indexOf(".") - 1));

			// we know the version, now set appropriate version flags
			flash2Installed = flashVersion == 2;		
			flash3Installed = flashVersion == 3;
			flash4Installed = flashVersion == 4;
			flash5Installed = flashVersion == 5;
		}
	}
	
	// loop through all versions we're checking, and set actualVersion to highest detected version
	for (var i = 2; i <= maxVersion; i++) {	
		if (eval("flash" + i + "Installed") == true) actualVersion = i;
	}
	// if we're on webtv, the version supported is 2 (pre-summer2000, or 3, post-summer2000)
	// note that we don't bother sniffing varieties of webtv. you could if you were sadistic...
	if(navigator.userAgent.indexOf("WebTV") != -1) actualVersion = 2;	
	
	// uncomment next line to display flash version during testing
	// alert("version detected: " + actualVersion);


	// we're finished getting the version. time to take the appropriate action

	if (actualVersion >= requiredVersion) { 		// user has a new enough version
		hasRightVersion = true;						// flag: it's okay to write out the object/embed tags later

		if (useRedirect) {							// if the redirection option is on, load the flash page
			if(jsVersion > 1.0) {					// need javascript1.1 to do location.replace
				window.location.replace(flashPage);	// use replace() so we don't break the back button
			} else {
				window.location = flashPage;		// otherwise, use .location
			}
		}
	} else {	// user doesn't have a new enough version.
	
		if (useRedirect) {		// if the redirection option is on, load the appropriate alternate page
			if(jsVersion > 1.0) {	// need javascript1.1 to do location.replace
				window.location.replace((actualVersion >= 2) ? upgradePage : noFlashPage);
			} else {
				window.location = (actualVersion >= 2) ? upgradePage : noFlashPage;
			}
		}
	}
}


detectFlash();	// call our detector now that it's safely loaded.		