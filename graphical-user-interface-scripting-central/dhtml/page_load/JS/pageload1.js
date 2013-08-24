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
/************************************************************************************
Regular cross-browser objects.
************************************************************************************/
function makeObj(obj,nest){
    nest=(!nest) ? '':'document.'+nest+'.'
   	this.css=bw.dom? document.getElementById(obj).style:bw.ie4?document.all[obj].style:bw.ns4?eval(nest+"document.layers." +obj):0;					
	this.evnt=bw.dom? document.getElementById(obj):bw.ie4?document.all[obj]:bw.ns4?eval(nest+"document.layers." +obj):0;		
	this.height=bw.ns4?this.css.document.height||this.css.clip.bottom:this.evnt.offsetHeight||this.css.pixelHeight
	this.width=bw.ns4?this.css.document.width:this.evnt.offsetWidth
	this.moveIt=b_moveIt; this.x; this.y; this.moveBy=b_moveBy;
	return this
}
function b_moveIt(x,y){this.x=x;this.y=y; this.css.left=this.x; this.css.top=this.y}
function b_moveBy(x,y){this.moveIt(this.x+x,this.y+y)}
/************************************************************************************
Making iframe objects!
************************************************************************************/
function makeFrame(iframe,contdiv,textdiv,arrowdiv,usebuffer){
	this.loader=new makeObj(iframe,contdiv)
	if(arrowdiv) this.arrow=new makeObj(arrowdiv)
	this.usebuffer=(usebuffer || bw.ie4 || (bw.ie5 && !bw.ie55) || bw.ns4) && !bw.ns5
	if(this.usebuffer){
		this.cont=new makeObj(contdiv)
		if(!bw.ns4){
			this.ifr=document.frames[iframe]
		        this.text=new makeObj(textdiv)
		}else{
			this.text=this.loader
		}
		this.text.moveIt(0,0)
		if(arrowdiv) this.arrow.css.visibility='visible'
		this.checkloaded=ifr_checkloaded;
		this.up=ifr_up;
		this.down=ifr_down;
	}else if(bw.dom){
	
		this.loader.css.visibility='visible'
	}	
	this.scroll=1
	this.loadpage=ifr_loadpage;
    this.obj = iframe + "Object"; 	eval(this.obj + "=this")	
}
/************************************************************************************
Scroll functions for iframe
************************************************************************************/
function ifr_up(speed){
	go=false
	if(this.scroll){
		if(this.text.y<0){
			this.text.moveBy(0,speed)
			go=true
		}
	}
	if(go)setTimeout(this.obj+".up("+speed+")",20)
}
function ifr_down(speed){
	go=false
	if(this.scroll){
		h=bw.ns4?this.text.css.document.height:this.text.evnt.offsetHeight
		if(this.text.y>-h+this.cont.height){
			this.text.moveBy(0,-speed)
			go=true
		}
	}
	if(go)setTimeout(this.obj+".down("+speed+")",20)
}

/************************************************************************************
Object functions for Iframe object
************************************************************************************/
function ifr_loadpage(url){
	if(bw.ns4) this.loader.css.load(url,780)
	else this.loader.evnt.src=url
	if(this.usebuffer && !bw.ns4 && !bw.ns5){
		setTimeout(this.obj+".checkloaded()",780)
	}
	if(this.usebuffer){
		this.text.moveIt(0,0)
	}
}
/************************************************************************************
IE5 and IE4 uses the iframe as a buffer, so the content is moved to a layer after it
's loaded.
************************************************************************************/
function ifr_checkloaded(){
	if(bw.ns6) this.text.evnt.innerHTML=this.ifr.document.getElementsByTagName("body")(0).innerHTML
	if(this.ifr.document.readyState=="complete"){
		//Move Content to text div
		this.text.evnt.innerHTML=this.ifr.document.body.innerHTML
	}else setTimeout(this.obj+".checkloaded()",100)
}

/************************************************************************************
Initiating page
************************************************************************************/

function ifrinit(){
	//Making a frame. You can have as many frames you want on a page
	//Arguments:
	// makeFrame('LOADING_IFRAME/LAYER','THE_LAYER_AROUND_THE_OTHER_LAYERS','THE_TEXT_BUFFER_LAYER','THE_UP&DOWN_LAYER',useBuffer)
	frame=new makeFrame('divLoad','divCont','divIEText','divArrows',useBuffer)
}
 
useBuffer=0 //If you set this one to 1 Explorer5.5 will also use the buffer trick. Set to 0 to make it work for ie6 
			