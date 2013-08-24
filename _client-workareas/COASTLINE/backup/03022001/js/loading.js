/********************************************************************************
Copyright (C) 1999 Thomas Brattli
This script is made by and copyrighted to Thomas Brattli at www.bratta.com
Visit for more great scripts. This may be used freely as long as this msg is intact!
I will also appriciate any links you could give me.
********************************************************************************/
//Default browsercheck, added to all scripts!
function checkBrowser(){
	this.ver=navigator.appVersion
	this.dom=document.getElementById?1:0
	this.ie5=(this.ver.indexOf("MSIE 5")>-1 && this.dom)?1:0;
	this.ie4=(document.all && !this.dom)?1:0;
	this.ns5=(this.dom && parseInt(this.ver) >= 5) ?1:0;
	this.ns4=(document.layers && !this.dom)?1:0;
	this.bw=(this.ie5 || this.ie4 || this.ns4 || this.ns5)
	return this
}
bw=new checkBrowser()
//Hides the div
function hideIt(div){
	if(bw.bw){
		div="divLoadCont"
		obj=bw.dom?document.getElementById(div).style:bw.ie4?document.all[div].style:bw.ns4?document[div]:0; 
		obj.visibility='hidden'
	}
}
onload=hideIt;