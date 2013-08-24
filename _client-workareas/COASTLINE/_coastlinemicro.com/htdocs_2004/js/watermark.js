var topOffset = 10

function keepAlive() {
	document.all.navBar.style.pixelTop = document.body.scrollTop + topOffset
}

function smoothMove() {
	var Dif = parseInt((document.body.scrollTop+topOffset-document.all.navBar.offsetTop)*.1)
	// Work-around wierd Netscape NaN bug
	if (isNaN(Dif)) Dif=0
	document.all.navBar.style.pixelTop+=Dif

}

function doLoad() {
	setup()
//	window.onscroll = keepAlive;
//	keepAlive()
	window.setInterval("smoothMove()",20)
}
window.onload = doLoad;