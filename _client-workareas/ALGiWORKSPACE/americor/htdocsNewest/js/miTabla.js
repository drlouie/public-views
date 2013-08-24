function runto(cual,highlightcolor){
	source=cual;
	if (source.tagName) {
		source.style.backgroundColor=highlightcolor
//		source.style.fontWeight='bold';
	}
}
function runback(cual,originalcolor){
	source=cual;
	if (source.tagName) {
		source.style.backgroundColor=originalcolor
	}
}
function lib_bwcheck(){
	this.ver=navigator.appVersion; this.agent=navigator.userAgent; this.dom=document.getElementById?1:0; this.opera5=this.agent.indexOf("Opera 5")>-1; this.ie5=(this.ver.indexOf("MSIE 5")>-1 && this.dom && !this.opera5)?1:0; this.ie6=(this.ver.indexOf("MSIE 6")>-1 && this.dom && !this.opera5)?1:0; this.ie4=(document.all && !this.dom && !this.opera5)?1:0; this.ie=this.ie4||this.ie5||this.ie6;	this.mac=this.agent.indexOf("Mac")>-1;	this.ns6=(this.dom && parseInt(this.ver) >= 5) ?1:0; this.ns4=(document.layers && !this.dom)?1:0;	this.bw=(this.ie6 || this.ie5 || this.ie4 || this.ns4 || this.ns6 || this.opera5);
	return this
}
var bw=new lib_bwcheck()


// 0 = column
// 1 = row
nPlace=0


//How many menus do you have? (remember to copy and add divs in the body if you add menus)
var nNumberOfMenus=5

var nMwidth=171 //The width on the menus (set the width in the stylesheet as well)
var nPxbetween=-54 //Pixels between the menus
var nFromleft=0 //The first menus left position
var nFromtop=0 //The top position of the menus
var nBgcolor='#999999' //The bgColor of the bottom mouseover div 
var nBgcolorchangeto='#F77D1D' //The bgColor to change to
var nImageheight=1 //The position the mouseover line div will stop at when going up!

//Object constructor
function MakeALGiMenu(obj,nest){
	nest=(!nest) ? "":'document.'+nest+'.'					
   	this.css=bw.dom? document.getElementById(obj).style:bw.ie4?document.all[obj].style:bw.ns4?eval(nest+"document.layers." +obj):0;		
	this.evnt=bw.dom? document.getElementById(obj):bw.ie4?document.all[obj]:bw.ns4?eval(nest+"document.layers." +obj):0;			
	this.scrollHeight=bw.ns4?this.css.document.height:this.evnt.offsetHeight
	this.moveIt=b_moveIt;this.bgChange=b_bgChange;
	this.slideUp=b_slideUp; this.slideDown=b_slideDown;
	this.clipTo=b_clipTo;
    this.obj = obj + "Object"; 	eval(this.obj + "=this")		
}
//Objects methods

// A unit of measure that will be added when setting the position of a layer.
var px = bw.ns4||window.opera?"":"px";

function b_moveIt(x,y){this.x=x; this.y=y; this.css.left=this.x+px; this.css.top=this.y+px;}
function b_bgChange(color){this.css.backgroundColor=color; this.css.bgColor=color; this.css.background=color;}
function b_clipTo(t,r,b,l){
	if(bw.ns4){this.css.clip.top=t; this.css.clip.right=r; this.css.clip.bottom=b; this.css.clip.left=l
	}else this.css.clip="rect("+t+"px "+r+"px "+b+"px "+l+"px)";
}
function b_slideUp(ystop,moveby,speed,fn,wh){
	speed = 10;
	if(!this.slideactive){
		if(this.y>ystop){
			this.moveIt(this.x,this.y-5); eval(wh)
			setTimeout(this.obj+".slideUp("+ystop+","+moveby+","+speed+",'"+fn+"','"+wh+"')",speed)
		}else{
			this.slideactive=false; this.moveIt(0,ystop); eval(fn)
		}
	}
}
function b_slideDown(ystop,moveby,speed,fn,wh){
	speed = 10;
	if(!this.slideactive){
		if(this.y<ystop){
			this.moveIt(this.x,this.y+5); eval(wh)
			setTimeout(this.obj+".slideDown("+ystop+","+moveby+","+speed+",'"+fn+"','"+wh+"')",speed)
		}else{
			this.slideactive=false; this.moveIt(0,ystop); eval(fn)
		}
	}
}
//Initiating the page, making cross-browser objects
function ALGiMenuInit(){
	oTopMenu=new Array()
	zindex=10
	for(i=0;i<=nNumberOfMenus;i++){
		oTopMenu[i]=new Array()
		oTopMenu[i][0]=new MakeALGiMenu('divTopMenu'+i)
		oTopMenu[i][1]=new MakeALGiMenu('divTopMenuBottom'+i,'divTopMenu'+i)
		oTopMenu[i][2]=new MakeALGiMenu('divTopMenuText'+i,'divTopMenu'+i)
		oTopMenu[i][1].moveIt(0,nImageheight)
		oTopMenu[i][0].clipTo(0,nMwidth,nImageheight+3,0)
		if(!nPlace) oTopMenu[i][0].moveIt(i*nMwidth+nFromleft+(i*nPxbetween),nFromtop)
		else{
			oTopMenu[i][0].moveIt(nFromleft,i*nImageheight+nFromtop+(i*nPxbetween))
			oTopMenu[i][0].css.zIndex=zindex--
		}
		oTopMenu[i][0].css.visibility="visible"
	}
}
//Moves the menu
function topMenu(num){
	if(oTopMenu[num][1].y==nImageheight) oTopMenu[num][1].slideDown(oTopMenu[num][2].scrollHeight+20,10,40,'oTopMenu['+num+'][0].clipTo(0,nMwidth,oTopMenu['+num+'][1].y+3,0)','oTopMenu['+num+'][0].clipTo(0,nMwidth,oTopMenu['+num+'][1].y+3,0)')
	else if(oTopMenu[num][1].y==oTopMenu[num][2].scrollHeight+20) oTopMenu[num][1].slideUp(nImageheight,10,40,'oTopMenu['+num+'][0].clipTo(0,nMwidth,oTopMenu['+num+'][1].y+3,0)','oTopMenu['+num+'][0].clipTo(0,nMwidth,oTopMenu['+num+'][1].y+3,0)')
}
function closeAll() {
	if(oTopMenu[0][1].y==oTopMenu[0][2].scrollHeight+20) oTopMenu[0][1].slideUp(nImageheight,10,40,'oTopMenu[0][0].clipTo(0,nMwidth,oTopMenu[0][1].y+3,0)','oTopMenu[0][0].clipTo(0,nMwidth,oTopMenu[0][1].y+3,0)')
	if(oTopMenu[1][1].y==oTopMenu[1][2].scrollHeight+20) oTopMenu[1][1].slideUp(nImageheight,10,40,'oTopMenu[1][0].clipTo(0,nMwidth,oTopMenu[1][1].y+3,0)','oTopMenu[1][0].clipTo(0,nMwidth,oTopMenu[1][1].y+3,0)')
	if(oTopMenu[2][1].y==oTopMenu[2][2].scrollHeight+20) oTopMenu[2][1].slideUp(nImageheight,10,40,'oTopMenu[2][0].clipTo(0,nMwidth,oTopMenu[2][1].y+3,0)','oTopMenu[2][0].clipTo(0,nMwidth,oTopMenu[2][1].y+3,0)')
	if(oTopMenu[3][1].y==oTopMenu[3][2].scrollHeight+20) oTopMenu[3][1].slideUp(nImageheight,10,40,'oTopMenu[3][0].clipTo(0,nMwidth,oTopMenu[3][1].y+3,0)','oTopMenu[3][0].clipTo(0,nMwidth,oTopMenu[3][1].y+3,0)')
	if(oTopMenu[4][1].y==oTopMenu[4][2].scrollHeight+20) oTopMenu[4][1].slideUp(nImageheight,10,40,'oTopMenu[4][0].clipTo(0,nMwidth,oTopMenu[4][1].y+3,0)','oTopMenu[4][0].clipTo(0,nMwidth,oTopMenu[4][1].y+3,0)')
}

//Changes background onmouseover
function menuOver(num){oTopMenu[num][1].bgChange(nBgcolorchangeto)}
function menuOut(num){oTopMenu[num][1].bgChange(nBgcolor)}

//Calls the init function onload if the browser is ok...
if (bw.bw) onload = ALGiMenuInit;
