// antiquated DynLayer
// don't bother using this code, use my new code
function DynLayer(id,nestref) {
	if (ns4) {
		if (nestref) {
			this.css = eval("document." + nestref + ".document." + id)
			this.ref = eval("document." + nestref + ".document." + id + ".document")
		}
		else {
			this.css = document.layers[id]
			this.ref = document.layers[id].document
		}
		this.x = this.css.left
		this.y = this.css.top
	}
	else if (ie4) {
		this.css = document.all[id].style
		this.ref = document
		this.x = this.css.pixelLeft
		this.y = this.css.pixelTop
	}
	this.obj = id + "Object"
	eval(this.obj + "=this")
	this.moveBy = DynLayerMoveBy
	this.moveTo = DynLayerMoveTo
	this.show = DynLayerShow
	this.hide = DynLayerHide
}
function DynLayerMoveBy(x,y) {
	this.x += x
	this.css.left = this.x
	this.y += y
	this.css.top = this.y
}
function DynLayerMoveTo(x,y) {
	this.x = x
	this.css.left = this.x
	this.y = y
	this.css.top = this.y
}
function DynLayerShow() {
	if (ns4) this.css.visibility = "show"
	else if (ie4) this.css.visibility = "visible"
}
function DynLayerHide() {
	if (ns4) this.css.visibility = "hide"
	else if (ie4) this.css.visibility = "hidden"
}