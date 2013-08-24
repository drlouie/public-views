/* 
WHEN scripting & interfacing by DRL [DrLouie] (aka: LouieRd / dba: NMS [NetMedia Solutions])
FOR business use by: SOE (Sony Online Entertainment) 
OR portfolio use by: DRL !!! NO EXCEPTIONS !!! - REPURPOSING, RECONSTRUCTING, REDEPLOYMENT IS STRICLY PROHIBITED! 
*/

/* Variables for the dynamic content */
var speed = 10;
var myIncomingHTML = '';
var myIncomingTITLE = '';
var itemID = '5376';
var stopAtClose = '135';
/* End Variables ( NO CHANGES NEEDED BEYOND THIS POINT ) */

theX = new Image();
theX.src = "images/theX.gif";
thePlus = new Image();
thePlus.src = "images/thePlus.gif";
tt1 = new Image();
tt1.src = "images/tableTopper.gif";
itb1 = new Image();
itb1.src = "images/innerTableBottomer.gif";
tb1 = new Image();
tb1.src = "images/tableBottomer.gif";
tbm1 = new Image();
tbm1.src = "images/tableBackgroundMarble.jpg";

function parseHTML(title,content) {
	myIncomingTITLE = title;
	myIncomingHTML=content;
	sizeThisWindow();
}
function loadParams() {
	var detailsMovie = document.leDetails;
	detailsMovie.Rewind();
	detailsMovie.SetVariable("_root.dataBox.htmlText", myIncomingHTML);
	detailsMovie.Play();
}
function loadHTML() {
	loadParams();
}
function killThisWindow() {
	document.getElementById("detailsLayer").style.height = 20 + 'px';
}
var myHiddenSizeFinder = "";
function sizeThisWindow() {
	document.getElementById("sizeFinder").innerHTML = myIncomingHTML;
	myHiddenSizeFinder = document.getElementById("sizeFinder").offsetHeight + 10; 
	document.getElementById("titleBar").innerHTML =  myIncomingTITLE;
	loadTabs();
}

var MdetailsLayer1 = "";
var Layer1 = "";
var startY = "";
function loadTabs() {
	MdetailsLayer1 = document.getElementById("detailsLayer");
	Layer1 = document.getElementById("detailsLayer").style;
	startY = MdetailsLayer1.offsetHeight;
	toggledetailsTab1();
}
function toggledetailsTab1() {
	if (MdetailsLayer1.offsetHeight <= startY || MdetailsLayer1.offsetHeight <= stopAtClose) { toggleDetails1Down(); }
	else if (MdetailsLayer1.offsetHeight >= myHiddenSizeFinder) { 
		toggleDetails1Up();
	}
	else { doNothing = 1; }
}
function toggleDetails1Down() {
	newYpos = MdetailsLayer1.offsetHeight + speed;
	MdetailsLayer1.style.height = newYpos + 'px';
	if (MdetailsLayer1.offsetHeight <= myHiddenSizeFinder) { setTimeout("toggleDetails1Down()", 1); }
	else { document.images.controlButton.src = theX.src; }
}
function toggleDetails1Up() {
	newYpos = MdetailsLayer1.offsetHeight - speed;
	MdetailsLayer1.style.height = newYpos + 'px';
	if (MdetailsLayer1.offsetHeight > stopAtClose) { setTimeout("toggleDetails1Up()", 1); }
	else { document.images.controlButton.src = thePlus.src; }
}