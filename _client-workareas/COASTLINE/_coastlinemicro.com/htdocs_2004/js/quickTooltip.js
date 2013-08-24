<!-- Begin hiding script from older browsers

function toolTips(evt,currElem) {
  var deeWidth = document.body.clientWidth;
  if ((navigator.appName == "Microsoft Internet Explorer") && (parseInt(navigator.appVersion) >= 4)) {

    tipWin = eval("document.all." + currElem + ".style");
	if (deeWidth <= "800") { tipWin.top = parseInt(evt.y)+20; }
	else { tipWin.top = parseInt(evt.y)+-150; }
    tipWin.left = Math.max(2,parseInt(evt.x)+20);
    tipWin.visibility = "visible";
    tipWin.status = "";
  }
  if ((navigator.appName == "Netscape") && (parseInt(navigator.appVersion) >= 4)) {
    tipWin = eval("document." + currElem);
	if (deeWidth <= "800") { tipWin.top = parseInt(evt.pageY)+20; }
	else { tipWin.top = parseInt(evt.pageY)+-150; }
    
    tipWin.left = Math.max(2,parseInt(evt.pageX)+20);
    tipWin.visibility = "visible";
    tipWin.status = "";
  }
}


function tipDown(currElem) {
  if ((navigator.appName == "Microsoft Internet Explorer") && (parseInt(navigator.appVersion) >= 4)) {
    tipWin = eval("document.all." + currElem + ".style");
    tipWin.visibility = "hidden";
  }
  if ((navigator.appName == "Netscape") && (parseInt(navigator.appVersion) >= 4)) {
    tipWin = eval("document." + currElem);
    tipWin.visibility = "hidden";
  }
}
-->
