function lib_bwcheck(){ //Browsercheck (needed)
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
var bw=new lib_bwcheck()

foldImg = 1						

var px = bw.ns4||window.opera?"":"px";

if(navigator.userAgent.indexOf('Opera')>-1 && document.getElementById){ //Opera 5 resize fix.
	scrX= innerWidth; scrY= innerHeight;
	document.onmousemove= function(){
		if(scrX<innerWidth-10 || scrY<innerHeight-10 || scrX>innerWidth+10 || scrY>innerHeight+10){
			scrX = innerWidth;
			scrY = innerHeight;
			initFoldout();
		}
	};
}

//object constructor...
function makeMenu(obj,nest){
	nest= (!nest)?"":'document.'+nest+'.';
	this.el= bw.ie4?document.all[obj]:bw.ns4?eval(nest+'document.'+obj):document.getElementById(obj);	
   	this.css= bw.ns4?this.el:this.el.style;
	this.ref= bw.ns4?this.el.document:document;		
	this.x= (bw.ns4||bw.opera5)?this.css.left:this.el.offsetLeft;
	this.y= (bw.ns4||bw.opera5)?this.css.top:this.el.offsetTop;
	this.h= (bw.ie||bw.ns6)?this.el.offsetHeight:bw.ns4?this.ref.height:bw.opera5?this.css.pixelHeight:0;
    this.vis= b_vis;
	this.hideIt= b_hideIt;
    this.showIt= b_showIt;
    this.moveIt= b_moveIt;
	return this
}
//object methods...
function b_showIt(){this.css.visibility='visible'}
function b_hideIt(){this.css.visibility='hidden'}
function b_vis(){if(this.css.visibility=='hidden' || this.css.visibility=='HIDDEN' || this.css.visibility=='hide') return true;}
function b_moveIt(x,y){this.x=x; this.y=y; this.css.left=this.x+px; this.css.top=this.y+px}

/************************************************************************************
This is the function that changes the sub menus to folded or unfolded state.
************************************************************************************/
function menu(num){
	if(bw.bw){
		if (!stayFolded){
			for (var i=0; i<oSub.length; i++){
				if (i!=num){
					oSub[i].hideIt()
					if (foldImg)oTop[i].ref["imgA"+i].src = unImg.src
				}
			}
			for(var i=1; i<oTop.length; i++){
				oTop[i].moveIt(0,oTop[i-1].y+oTop[i-1].h)
			}
		}
		if (oSub[num].vis()){
			oSub[num].showIt()
			if (foldImg)oTop[num].ref["imgA"+num].src = exImg.src
		}else{
			oSub[num].hideIt()
			if(foldImg)oTop[num].ref["imgA"+num].src = unImg.src
		}
		for(var i=1; i<oTop.length; i++){ 
			if (!oSub[i-1].vis()) oTop[i].moveIt(0,oTop[i-1].y+oTop[i-1].h+oSub[i-1].h+mainOffsetY) 
			else oTop[i].moveIt(0,oTop[i-1].y+oTop[i-1].h+mainOffsetY)
		}
	}
}

/*********************************************************************
The init function... there should be no need to change anything here.
*********************************************************************/
function initFoldout(){
	//Fixing the browsercheck for opera... this can be removed if the browsercheck has been updated!!
	bw.opera5 = (navigator.userAgent.indexOf("Opera")>-1 && document.getElementById)?true:false
	if (bw.opera5) bw.ns6 = 0

	oTop = new Array()
	oSub = new Array()
	//Making the objects and hiding the subs...
	for (var i=0; i<FoldNumber; i++){
		oTop[i] = new makeMenu('divTop'+i,'divCont')
		oSub[i] = new makeMenu('divSub'+i,'divCont.document.divTop'+i)
		oSub[i].hideIt()
	}
	
	//Positioning the top objects...
	oTop[0].moveIt(0,0)
	for (var i=1; i<oTop.length; i++){
		oTop[i].moveIt(0, oTop[i-1].y+oTop[i-1].h+mainOffsetY)
	}
	
	//Making the containing menu object and showing it...
	oCont = new makeMenu('divCont')
	oCont.showIt()
}

// If the browser is ok, the script is started onload...
/// if(bw.bw) onload = ;