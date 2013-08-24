/*	Pop - Up 2.4 :
	Script by Lefteris Haritou	
	Copyright © 1998 - 1999
	http://popup.jscentral.com
        You are not allowed to modify
        anything in this script
*/

n = (document.layers) ? 1:0
ie = (document.all) ? 1:0
var submenu="popitup";
var wd=0;
var num=0;
var menuitems=0;
var x;
var y;
var lb;
var lr;
var timer1;
var timer2;
var ntt=String.fromCharCode(60,83,112,97,110,32,99,108,97,115,115,61,34,116,116,105,112,34,62,67,108,105,99,107,32,104,101,114,101,32,116,111,32,103,101,116,32,121,111,117,114,32,111,119,110,32,99,111,112,121,32,111,102,32,80,111,112,45,85,112,32,110,111,119,32,33,60,47,83,112,97,110,62);
var ntv=String.fromCharCode(60,78,79,66,82,62,60,97,32,104,114,101,102,61,34,106,97,118,97,115,99,114,105,112,116,58,97,98,116,40,41,34,32,99,108,97,115,115,61,34,110,101,116,109,101,110,117,84,105,116,108,101,34,32,111,110,109,111,117,115,101,111,118,101,114,61,34,114,101,116,117,114,110,32,116,114,117,101,34,62,80,111,112,45,85,112,38,110,98,115,112,59,98,121,60,66,82,62,76,101,102,116,101,114,105,115,32,72,97,114,105,116,111,117,60,47,97,62,60,47,78,79,66,82,62);
var iev=String.fromCharCode(80,111,112,45,85,112,32,98,121,60,66,82,62,76,101,102,116,101,114,105,115,32,72,97,114,105,116,111,117);
var iet=String.fromCharCode(67,108,105,99,107,32,72,101,114,101,32,116,111,32,103,101,116,32,121,111,117,114,32,111,119,110,32,99,111,112,121,32,111,102,32,80,111,112,45,85,112,32,78,111,119,32,33);
var mbcolor="#333366"
var mfcolor="#FF6600"
var tbcolor="#ffffff"
var tfcolor="#FFFFFF"
var tdl=false;

if (n){
wlw = window.innerWidth;
wlh = window.innerHeight;
window.onresize=resz;
}

function resz(){
if (wlw!=window.innerWidth || wlh!=window.innerHeight)
location.reload()
}

function popinit(){
if (ie){
wd=document.all["popitup"].offsetWidth;
for (x=0; x<document.all.length; x++){
if (document.all[x].id.substring(0,4)=="arow"){
document.all[x].style.posLeft=wd-12;
document.all[x].style.posTop-=3;
q=document.all[x-1].id;
num=q.substring(12,q.length);
q=num+"subout";
var i=0;
swd=document.all[q].offsetWidth;
for (z=0; z<document.all.length; z++)
if (document.all[z].id.length>=9 && document.all[z].id.substring(0,4)==q.substring(0,4))
i++
for (z=1;z<=i;z++)
document.all[num+"subitem"+(z)].style.width=swd;
}
if (document.all[x].id.length>=13 && document.all[x].id.substring(0,12)=="mainmenuitem")
menuitems++
}
}
if (n){
document.onmousedown = mdspl;
wd=document.layers["popitup"].clip.width;
document.layers["popitup"].layers["popl"].clip.width=wd-5;
document.layers["ttip"].document.open("text/html");
document.layers["ttip"].document.write(ntt);
document.layers["ttip"].document.close();
document.layers["popitup"].layers["popl"].document.open("text/html");
document.layers["popitup"].layers["popl"].document.write(ntv);
document.layers["popitup"].layers["popl"].document.close();
}
}

function mdspl(e){
if (ie && iev.length==29){
lr=document.body.offsetWidth+document.body.scrollLeft;
lb=document.body.offsetHeight+document.body.scrollTop;
with(window.event.srcElement)
if(tagName!="A" && tagName!="INPUT" && tagName!="TEXTAREA" && tagName!="IMG" && tagName!="SELECT"){
x=window.event.clientX+document.body.scrollLeft;
y=window.event.clientY+document.body.scrollTop;
if (document.all["popitup"].style.visibility=="visible"){
document.all["popitup"].style.visibility="hidden"
document.all[submenu].style.visibility="hidden"
}
else{
if (y+document.all["popitup"].offsetHeight+25>=lb)
y=lb-25-document.all["popitup"].offsetHeight;
if (x+wd+30>=lr)
x=lr-wd-30;
document.all["popitup"].style.left=x;
document.all["popitup"].style.top=y;
document.all["popitup"].style.visibility="visible"
}
}
}
if (n){
if (e.which==1 && ntv.length==125){
lb=window.innerHeight+window.pageYOffset;
lr=window.innerWidth+window.pageXOffset;
a=document.layers["popitup"].clip.height
x=e.pageX;
y=e.pageY;
if (document.layers["popitup"].visibility=="show"){
document.layers["popitup"].visibility="hide"
document.layers["ttip"].visibility="hide"
if (submenu!="popitup")
document.layers[submenu].visibility="hide"
}
else{
if (y+a+20>=lb)
y=lb-a-20;
if (x+wd+20>=lr)
x=lr-wd-20;
document.layers["popitup"].left=x;
document.layers["popitup"].top=y;
document.layers["popitup"].visibility="show";
}
}
}
}

function toolon(){
if (!tdl)
timer1=setTimeout('tooldspl()',600)
}

function tooloff(){
clearTimeout(timer1)
}

function tooldspl(){
if (x+wd+document.layers["ttip"].clip.width+10>lr)
document.layers["ttip"].left=x-document.layers["ttip"].clip.width;
else
document.layers["ttip"].left=x+wd;
document.layers["ttip"].top=y+2;
document.layers["ttip"].visibility="show";
tdl=true;
timer2=setTimeout('tooludspl()',2000)
}

function tooludspl(){
tdl=false;
document.layers["ttip"].visibility="hide"
}

function sdspl(w,t,num){
if (ie){
hg=document.all[w].offsetHeight+t;
swd=document.all[w].offsetWidth;
if (y+hg+10>=lb){
sy=y+t-document.all[w].offsetHeight+16;
document.all[w].style.top=sy;
}
else
document.all[w].style.top=y+t-2;
if (x+wd+swd+30>=lr){
sx=document.all["popitup"].style.posLeft-swd+6;
document.all[w].style.left=sx;
}
else
document.all[w].style.left=x+wd-4;
document.all[w].style.visibility="visible";
}
if (n && ntt.length==73){
hg=document.layers[w].clip.height;
swd=document.layers[w].clip.width;
if (y+t+hg+5>=lb){
sy=y+t-hg+12;
document.layers[w].top=sy;
}
else
document.layers[w].top=y+t-2;
if (x+wd+swd+10>=lr){
sx=x-swd+6;
document.layers[w].left=sx;
}
else
document.layers[w].left=x+wd-5;
document.layers[w].visibility="show";
}
}


function cdspl(w,s){
if (ie && iet.length==47){
t=document.all[w].offsetTop;
document.all[w].style.color=tfcolor;
document.all[w].style.background=mfcolor;
if(s==true){
if (submenu!="popitup")
document.all[submenu].style.visibility="hidden"
num=w.substring(12,w.length);
w=num+"subout";
submenu=w;
sdspl(w,t,num)
}
if (s==false && submenu!="popitup")
document.all[submenu].style.visibility="hidden"
}
if (n){
t=document.layers[w.parentLayer.name].layers[w.name].top;
document.layers[w.parentLayer.name].layers[w.name].bgColor=mfcolor;
if(s==true){
if(submenu!="popitup")
document.layers[submenu].visibility="hide";
c=w.name
num=c.substring(8,c.length);
c="sub"+num+"menu";
submenu=c;
sdspl(c,t)
}
if(s==false && submenu!="popitup")
document.layers[submenu].visibility="hide";
}
}

function udspl(w){
if (ie){
fromElement=window.event.fromElement;
toElement=window.event.toElement;
if (fromElement!=null && toElement!=null)
if((window.event.fromElement.id==window.event.toElement.id.substring(4,window.event.toElement.id.length)) || (window.event.fromElement.id.substring(4,window.event.fromElement.id.length)==window.event.toElement.id))
return;
document.all[w].style.color=tbcolor;
document.all[w].style.background="transparent";
}
if (n)
document.layers[w.parentLayer.name].layers[w.name].bgColor=mbcolor;
}

function gomenu(address){
if (n){
document.layers["popitup"].visibility="hide";
document.layers[submenu].visibility="hide";
}
if (iev.length+iet.length+ntv.length+ntt.length==274)
location.href=address;
}

function abt(){
if (n){
document.layers["popitup"].visibility="hide";
document.layers[submenu].visibility="hide";
}
window.open(String.fromCharCode(104,116,116,112,58,47,47,112,111,112,117,112,46,106,115,99,101,110,116,114,97,108,46,99,111,109),'','width=640,height=440,top=0,left=0,scrollbars=1,location=1,status=1')
}
