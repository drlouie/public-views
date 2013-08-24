// Title: Mouse Over Table BGColor Changer
// Description: Allows for dynamic switching of Table Background Colors
// Version: 1.0
// Date: October 28, 2002 (mm-dd-yyyy)
// Author: Luis Rodriguez <drlouie@netmediasol.com>

function runto(highlightcolor){
source=event.srcElement
if (source.tagName=="TR"||source.tagName=="TABLE")
return
while(source.tagName!="TD")
source=source.parentElement
if (source.style.backgroundColor!=highlightcolor&&source.id!="ignore")
source.style.backgroundColor=highlightcolor
}

function runback(originalcolor){
if (event.fromElement.contains(event.toElement)||source.contains(event.toElement)||source.id=="ignore")
return
if (event.toElement!=source)
source.style.backgroundColor=originalcolor
}

function Brunto(cual,highlightcolor){
	cual.style.borderColor=highlightcolor
}

function Brunback(cual,originalcolor){
	cual.style.borderColor=originalcolor
}

function TDrunto(cual,highlightcolor){
source=cual;
while(source.tagName!="TD")
source=source.parentElement
if (source.style.backgroundColor!=highlightcolor&&source.id!="ignore")
source.style.backgroundColor=highlightcolor
}

function TDrunback(cual,originalcolor){
source=cual;
while(source.tagName!="TD")
source=source.parentElement
if (source.style.backgroundColor!=originalcolor&&source.id!="ignore")
source.style.backgroundColor=originalcolor
}

function FONTrunto(cual,color){
	document.getElementById(""+cual+"").style.color = color;
}


function runto2(cual,highlightcolor){
	if (cual.style.backgroundColor) { 
		cual.style.backgroundColor=highlightcolor;
	}
}

function runback2(cual,originalcolor){
	if (cual.style.backgroundColor) { 
 		cual.style.backgroundColor=originalcolor;
	}
}