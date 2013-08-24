<!--
on = new Image();
on.src = "images/show_radio.gif";

off = new Image();
off.src = "images/hide_radio.gif";

ns4 = (document.layers)? true:false
ie4 = (document.all)? true:false

function runit() {
	if (ns4) block = document.blockDiv
	if (ie4) block = blockDiv.style
	block.xpos = parseInt(block.left)
	block.ypos = parseInt(block.top)
}

function checkPos() {
	if (block.xpos == 0) {
	moveOut()			
	}
	else if (block.xpos == -230) {
	moveIn()			
	}
}

function moveIn() {
	if (block.xpos < 0) {		
	block.xpos += 10		
	block.left = block.xpos
	setTimeout("moveIn()",1);
	
	if (ns4) document.blockDiv.document.images['radiobar'].src = off.src
	else document.images['radiobar'].src = off.src
	}
}

function moveOut() {
	if (block.xpos > -230){		
	block.xpos -= 10	
	block.left = block.xpos
	setTimeout("moveOut()",1);
		
	if (ns4) document.blockDiv.document.images['radiobar'].src = on.src
	else document.images['radiobar'].src = on.src
	}
}

function hideLayer(layer) {

  if (isMinNS4)
    layer.visibility = "hide";
  if (isMinIE4)
    layer.style.visibility = "hidden";
}

function showLayer(layer) {

  if (isMinNS4)
    layer.visibility = "show";
  if (isMinIE4)
    layer.style.visibility = "visible";
}
//-->