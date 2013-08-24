/********************************************************************************
Here's the lib_doc_size object, see www.bratta.com/dhtml for tutorial on how it works.
********************************************************************************/
//Document size object ********
function lib_doc_size(){ 
	this.x=0;this.x2=bw.ie && document.body.offsetWidth-20||innerWidth||0;
	this.y=0;this.y2=bw.ie && document.body.offsetHeight-5||innerHeight||0;
	if(!this.x2||!this.y2) return message('Document has no width or height') 
	this.x50=this.x2/2;this.y50=this.y2/2;
	return this;
}
/********************************************************************************
Div object functions
********************************************************************************/
//Browsercheck (needed) ***************
function lib_bwcheck(){ 
	this.ver=navigator.appVersion
	this.agent=navigator.userAgent
	this.dom=document.getElementById?1:0
	this.opera5=this.agent.indexOf("Opera 5")>-1
	this.ie5=(this.ver.indexOf("MSIE 5")>-1 && this.dom && !this.opera5)?1:0; 
	this.ie6=(this.ver.indexOf("MSIE 6")>-1 && this.dom && !this.opera5)?1:0;
	this.ie4=(document.all && !this.dom && !this.opera5)?1:0;
	this.ie=this.ie4||this.ie5||this.ie6
	this.mac=this.agent.indexOf("Mac")>-1
	this.ns6=(this.dom && parseInt(this.ver) >= 5) ?1:0; 
	this.ns4=(document.layers && !this.dom)?1:0;
	this.bw=(this.ie6 || this.ie5 || this.ie4 || this.ns4 || this.ns6 || this.opera5)
	return this
}
bw=new lib_bwcheck() //Browsercheck object

//Debug function ******************
function lib_message(txt){alert(txt); return false} 

//Lib objects  ********************
function lib_obj(obj,nest,o){ 
	if(!bw.bw) return lib_message('Old browser')
	nest=(!nest) ? '':'document.'+nest+'.'										
   	if(o&&bw.ns4) this.evnt=o; 
	else this.evnt=bw.dom? document.getElementById(obj):bw.ie4?document.all[obj]:bw.ns4?eval(nest+"document.layers." +obj):0;	
	if(!this.evnt) return lib_message('The layer does not exist ('+obj+') - \nIf your using Netscape please check the nesting of your tags!')
	this.css=bw.dom||bw.ie4?this.evnt.style:this.evnt; this.ref=bw.dom||bw.ie4?document:this.css.document;
	this.x=this.css.left||this.css.pixelLeft||this.evnt.offsetLeft||0; this.y=this.css.top||this.css.pixelTop||this.evnt.offsetTop||0
	this.w=this.evnt.offsetWidth||this.css.clip.width||this.ref.width||this.css.pixelWidth||0; this.h=this.evnt.offsetHeight||this.css.clip.height||this.ref.height||this.css.pixelHeight||0
	this.c=0 //Clip values
	if((bw.dom || bw.ie4) && this.css.clip) {
		this.c=this.css.clip; this.c=this.c.slice(5,this.c.length-1); 
		this.c=this.c.split(' '); for(var i=0;i<4;i++){this.c[i]=parseInt(this.c[i])}
	}
	this.ct=this.css.clip.top||this.c[0]||0; this.cr=this.css.clip.right||this.c[1]||this.w||0
	this.cb=this.css.clip.bottom||this.c[2]||this.h||0; this.cl=this.css.clip.left||this.c[3]||0
	this.obj = obj + "Object"; 	eval(this.obj + "=this")
	return this
}
//Moving object to **************
lib_obj.prototype.moveIt = function(x,y){this.x=x;this.y=y; this.css.left=x;this.css.top=y} 
/********************************************************************************
Here we call the object constructor to make objects, then we move
them to a choosen place on the page.
********************************************************************************/
function poInit(){
	//first me make a page object
	page=new lib_doc_size()
	//then we make the layer objects
	oLeftBottom=new lib_obj('divLeftBottom')
	//now we place them
	//The divs has a width and height of 100, so we divide that with 2 to place it at center
	oLeftBottom.moveIt(page.x,page.y2-54)
	//Takes care of the resizing.
	window.onresize=resized;
}
function resized(){
	page2=new lib_doc_size()
	if(page2.x2!=page.x2 || page2.y2!=page.y2){
		if(bw.ns4) location.reload() //If the width or height have changed we reload the page.
		else poInit()
	}
}