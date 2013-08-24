/*
Dynamic Window Opener With Other Params
*/

function popWindow(url,name,w,h,closeit) {
	//GET SIZE OF WINDOW/SCREEN
	windowW = w;
	windowH = h;
	var windowX = (screen.width/2)-(windowW/2);
	var windowY = (screen.height/2)-(windowH/2);

	window.open(url,name,'width='+w+',height='+h+',top='+windowY+',left='+windowX+'');
	if (closeit == "YES") { parent.window.close(); }
}