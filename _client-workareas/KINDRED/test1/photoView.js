function popWindow(url,name,w,h,closeit) {
	//GET SIZE OF WINDOW/SCREEN
	windowW = w;
	windowH = h;
	var windowX = (screen.width/2)-(windowW/2);
	var windowY = (screen.height/2)-(windowH/2);
	
	var myExtra = "";

	// if viewing large photo create document
	if (url.indexOf(".jpg") != -1) {
		var poppedWindow = window.open('',name,'width='+w+',height='+h+',top='+windowY+',left=' + windowX + myExtra + '');
		if (closeit == "YES") { parent.window.close(); }
		else { poppedWindow.focus(); }

		poppedWindow.document.open();
		poppedWindow.document.write('<html><head><title>Photo Viewer ( by NetMedia Solutions )</title></head><body bgcolor=\"#000000\" LEFTMARGIN=\"0\" TOPMARGIN=\"0\" MARGINWIDTH=\"0\" MARGINHEIGHT=\"0\"><font size=\"1\" color=\"#cccccc\" face=\"Verdana\"><center><br>Click photo to close window<br><br><a href=\"#\" onClick=\"javascript:window.close();\"><img src=\"'+url+'\" border=\"0\"></a><br><br>Click photo to close window<br></center></font></body></html>');
		poppedWindow.document.close();
	}
	// else load document requested
	else {
		var poppedWindow = window.open(url,name,'width='+w+',height='+h+',top='+windowY+',left=' + windowX + myExtra + '');
		if (closeit == "YES") { parent.window.close(); }
		else { poppedWindow.focus(); }
	}
	
}

function viewPhoto(cual) {
	popWindow(cual,'viewPhotos','500','600','NO');	
}


