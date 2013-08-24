// check the browser...we're looking for ie/win
var isIE = (navigator.appVersion.indexOf("MSIE") != -1) ? true : false;		// true if we're on ie
var isWin = (navigator.appVersion.indexOf("Windows") != -1) ? true : false; // true if we're on windows

// this is a js1.1 code block, so make note that js1.1 is supported.
jsVersion = 1.1;

// write vbscript detection if we're not on mac.
if(isIE && isWin){ // don't write vbscript tags on anything but ie win
	document.write('<SCR' + 'IPT LANGUAGE=VBScript\> \n');
	document.write('on error resume next \n');
	document.write('flash2Installed = (IsObject(CreateObject("ShockwaveFlash.ShockwaveFlash.2"))) \n');
	document.write('flash3Installed = (IsObject(CreateObject("ShockwaveFlash.ShockwaveFlash.3"))) \n');
	document.write('flash4Installed = (IsObject(CreateObject("ShockwaveFlash.ShockwaveFlash.4"))) \n');
	document.write('flash5Installed = (IsObject(CreateObject("ShockwaveFlash.ShockwaveFlash.5"))) \n');	
	document.write('</SCR' + 'IPT\> \n'); // break up end tag so it doesn't end our script
}
