/*
*******************************
Document magnifying script
Written by Christian Patzer
cpatzer@hotmail.com
VERSION 2.0
  Revamped GUI
  Added resize functionality
  Added zoomFactor adjustability
  Added baseDir var for centralized distribution of files
  Added handle for A tag occurences within the magnifier
For this script and more, visit http://www.dynamicdrive.com
*******************************
*/

//configure iframe src for zoom box
var baseDir="";//configure this to the directory you wish to keep the magnifier files in i.e. /magnifyfile/
var zoomFactor=20;//percentage int[1-100]
var startZoom='120%';//percentage string[>= 0]

//DO NOT EDIT BELOW THIS LINE
//---------------------------
var iframeSrc = "zoom.html";
var tempY,tempX,initialized,X,Y,rX,rY,tempW,tempH,resizeInitialized,zoomIframe,zoomBox,zoomObjStyle,objToResize;
var ie55 = false;
var firstTableWidth;


if(window.createPopup){
	ie55 = true;
}
else{
	ie55 = false;
}
zoomBoxHTML  = "<div id='zoomBox' style='position:absolute;left:0;top:0;visibility:hidden'>";
zoomBoxHTML += "<table width=150 height=100 cellspacing='0' cellpadding='0' style='background-color:#6699CC;border:1px solid #324B64'; id='magContainer'>";
zoomBoxHTML += "<tr>";
zoomBoxHTML += "<td colspan=2 align=center>";
zoomBoxHTML += "<iframe src='"+baseDir+""+iframeSrc+"' name=zoom width=150 height=100 style='border:0px;padding:0px;'></iframe>";
zoomBoxHTML += "</td>";
zoomBoxHTML += "</tr>";
zoomBoxHTML += "<tr>";
zoomBoxHTML += "<td style='height:16px;cursor:move;color:white;font-weight:bold;font-family:verdana;font-size:8pt;border:0px;' OnMouseDown='initXY();'  OnMouseUp='disable();' title='Move'><img src='"+baseDir+"move.gif' align=absmiddle>Magnifier</td>";
zoomBoxHTML += "<td style='border:0px;padding:0px;' id='resizeObj' valign=bottom align=right><img src='"+baseDir+"mag_plus.gif'  OnClick='zoomIn()' style='cursor:hand'  title='Zoom In'><img src='"+baseDir+"blue_spacer.gif' height='1' width='2'><img src='"+baseDir+"mag_minus.gif' OnClick='zoomOut()' style='cursor:hand;' title='Zoom Out'><img src='"+baseDir+"blue_spacer.gif' height='1' width='2'><img src='"+baseDir+"hide.gif' vspace=1 OnMouseDown=\"this.src='"+baseDir+"hide_down.gif'\" OnMouseOut=\"this.src='"+baseDir+"hide.gif'\" OnClick='hideZoomBox();' title='Close'><img src='"+baseDir+"resize.gif' style='cursor:SE-resize' onMouseDown='activateResize()' hspace='0' vspace='0' title='Resize'></td>";
zoomBoxHTML += "</tr>";
zoomBoxHTML += "</table>";
zoomBoxHTML += "</div>";
zoomBoxHTML += "<table border=0 cellpadding=0 cellspacing=0 width='100%'>"; 
zoomBoxHTML += "<tr>";
zoomBoxHTML += "<td>";
  

if(ie55){
	document.write(zoomBoxHTML);	
}


function activateResize(){
	objToResize = document.getElementById('magContainer');
	document.getElementById('resizeObj').attachEvent('onmousemove',resizeMag);
	zoomIframe = document.getElementById('zoom');
	rX=event.clientX;
	rY=event.clientY;
	tempW = parseInt(objToResize.width);
	tempH = parseInt(objToResize.height);
	resizeInitialized=true;
}

function resizeMag(){
	if(resizeInitialized){
		doWidth = (event.clientX-rX)+parseInt(tempW);
		doHeight = (event.clientY-rY)+parseInt(tempH);
		if(doWidth>0)objToResize.width=doWidth;
		if(doWidth>0)zoomIframe.width=doWidth;
		if(doHeight>0)objToResize.height=doHeight;
		if(doHeight>0)zoomIframe.height=doHeight;
		return false;
	}
}

function moveZoomBox(){
	if(initialized==true){
		zoomBox.style.pixelLeft=tempX+event.clientX-X;
		zoomBox.style.pixelTop=tempY+event.clientY-Y;
		document.frames.zoom.scrollTo(tempX+event.clientX-X,tempY+event.clientY-Y);
		return false;
	}
}

function  initXY(){
	X=event.clientX;
	Y=event.clientY;
        document.body.onselectstart=new Function("return false")
	tempX=zoomBox.style.pixelLeft;
	tempY=zoomBox.style.pixelTop;
	initialized=true;
	document.onmousemove=moveZoomBox;	
}

function resize(){
	if(ie55){
		zoomBox.style.pixelLeft=0;
		zoomBox.style.pixelTop=0;
		document.frames.zoom.scrollTo(0,0);
		document.frames.zoom.document.all.tags("TABLE")[1].width=document.body.offsetWidth-25;
	}
}

function init(){
	if(ie55){
		var HTMLtoGrab = document.all.tags("HTML")[0].innerHTML;
		var HTMLtoWrite = HTMLtoGrab;
		var HTMLtoWrite = "<HTML>"+HTMLtoWrite+"</HTML>";
		zoomBox=document.getElementById('zoomBox');
		zoomBox.style.visibility = "visible";
		document.frames.zoom.document.getElementById('writeToMe').outerHTML = HTMLtoWrite;
		document.frames.zoom.document.getElementById('zoomBox').style.visibility="hidden";
		document.frames.zoom.document.body.scroll='no';
		zoomObjStyle = document.frames.zoom.document.body.style;
		zoomObjStyle.zoom=startZoom;
		document.frames.zoom.scrollTo(0,0);
		document.frames.zoom.document.body.mergeAttributes(document.body);
		for(var i=0; i<document.frames.zoom.document.all.tags("A").length; i++){
			document.frames.zoom.document.all.tags("A")[i].target="_top";
		}
		resize();	
		
	}
}
function zoomIn(){
	zoomObjStyle.zoom=parseInt(zoomObjStyle.zoom)+zoomFactor+'%';	
}
function zoomOut(){
	if(parseInt(zoomObjStyle.zoom) <= zoomFactor)return false;
	zoomObjStyle.zoom=parseInt(zoomObjStyle.zoom)-zoomFactor+'%';
}
function hideZoomBox(){
	zoomBox.style.visibility="hidden";
}
function showZoomBox(){
	zoomBox.style.visibility="visible";
}

function disable(){
        document.body.onselectstart=new Function("return true")
	initialized=false;
	document.getElementById('resizeObj').detachEvent('onmousemove',resizeMag);
	resizeInitialized=false;
}
window.onload=init;
window.onresize=resize;
document.onmouseup=disable;
document.ondblclick=showZoomBox;