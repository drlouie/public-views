<!--
on = new Image();
on.src = "show_radio.gif";

off = new Image();
off.src = "hide_radio.gif";

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

function showObject(obj) {
	if (ns4) obj.visibility = "show"
	else if (ie4) obj.visibility = "visible"
}

function hideObject(obj) {
	if (ns4) obj.visibility = "hide"
	else if (ie4) obj.visibility = "hidden"
}

function checkImage() {
	if (block.xpos == 0) {
	if (ns4) document.blockDiv.document.images['radiobar'].src = off.src
	else document.images['radiobar'].src = off.src
	}
	else if (block.xpos == -230) {
	if (ns4) document.blockDiv.document.images['radiobar'].src = on.src
	else document.images['radiobar'].src = on.src
	}
}

function loadSource(id,nestref,url) {
	if (ns4) {
		var lyr = (nestref)? eval('document.'+nestref+'.document.'+id) : document.layers[id]
		lyr.load(url,lyr.clip.width)
	}
	else if (ie4) {
		parent.bufferFrame.document.location = url
	}
}
function loadSourceFinish(id) {
	if (ie4) document.all[id].innerHTML = parent.bufferFrame.document.body.innerHTML
}
//-->