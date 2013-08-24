// Title: Mouse Over Table BGColor Changer
// Description: Allows for dynamic switching of Table Background Colors
// Version: 1.0
// Date: October 28, 2002 (mm-dd-yyyy)
// Author: Luis Rodriguez <drlouie@netmediasol.com>

function runto(cual,highlightcolor){
source=cual;
	if (source.tagName) {
		while(source.tagName!="TR")
		source=source.parentElement
		if (source.style.backgroundColor!=highlightcolor&&source.id!="ignore")
		source.style.backgroundColor=highlightcolor
	}
}

function runback(cual,originalcolor){
source=cual;
	if (source.tagName) {
		while(source.tagName!="TR")
		source=source.parentElement
		if (source.style.backgroundColor!=originalcolor&&source.id!="ignore")
		source.style.backgroundColor=originalcolor
	}
}

function TDrunto(cual,highlightcolor){
source=cual;
	if (source.tagName) {
		while(source.tagName!="TD")
		source=source.parentElement
		if (source.style.backgroundColor!=highlightcolor&&source.id!="ignore")
		source.style.backgroundColor=highlightcolor
	}
}

function TDrunback(cual,originalcolor){
source=cual;
	if (source.tagName) {
		while(source.tagName!="TD")
		source=source.parentElement
		if (source.style.backgroundColor!=originalcolor&&source.id!="ignore")
		source.style.backgroundColor=originalcolor
	}
}

function FONTrunto(cual,color){
	if (document.getElementById) {
		document.getElementById(""+cual+"").style.color = color;
	}
}


function runto2(cual,highlightcolor){
	if (document.getElementById) {
		if (cual.style.backgroundColor) { 
			cual.style.backgroundColor=highlightcolor;
		}
	}
}

function runback2(cual,originalcolor){
	if (cual.style) {
		if (cual.style.backgroundColor) { 
 			cual.style.backgroundColor=originalcolor;
		}
	}
}