<!--

ns4 = (document.layers)? true:false
ie4 = (document.all)? true:false

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