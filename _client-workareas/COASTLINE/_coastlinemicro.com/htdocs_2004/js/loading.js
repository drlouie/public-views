///////////////////////////////////////////////////////////////////
// This script and its counterparts are ©2001 NetMedia Solutions //
// For use ONLY with CoastlineMicro.com                          //
// To re-use or have this script re-interfaced for your specific //
// needs please contact SServices\@NetMediaSolutions.com         //
// Prices are cheap for re-interfacing of current scripts and    //
// programs, so email us today to get you own LEGAL programming  //
// licensed for use only on YOUR site(s) or for YOUR purpose(s). //
//                                                               //
// Original script Copyright (C) 1999 Thomas Brattli             //
// dhtmlcentral.com                                              //
//                                                               //
// Re-Written and tied into other Back-End and Front-End apps to //
// achieve a cross-browser compatible DHTML store interface.     //
// Re-Written by NetMedia Solutions.                             //
///////////////////////////////////////////////////////////////////

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