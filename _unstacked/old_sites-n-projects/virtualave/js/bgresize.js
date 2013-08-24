<!--
NS4=(document.layers);
IE4=(document.all);
ver4=(NS4 || IE4);

scaleWidth = true;
scaleHeight = true;
imSRC = "/images/test1bg.jpg";

if (NS4) onload = setResize;

function setResize(){
	setTimeout('window.onresize=reDo;',500);
}

function reDo(){
    window.location.reload()
}

if (IE4) onresize = reDoIE;

function reDoIE(){
    imBG.width = document.body.clientWidth;
    imBG.height = document.body.clientHeight;
}


function makeIm() {

  winWid = (NS4) ? innerWidth : document.body.clientWidth;
  winHgt = (NS4) ? innerHeight : document.body.clientHeight;
  imStr = "<DIV ID=elBGim"
  + " STYLE='position:absolute;left:0;top:0;z-index:-1'>"
  + "<IMG NAME='imBG' BORDER=0 SRC="+imSRC;
  if (scaleWidth) imStr += " WIDTH="+winWid;
  if (scaleHeight) imStr += " HEIGHT="+winHgt;
  imStr += "></DIV>";

  document.write(imStr);

}
//-->