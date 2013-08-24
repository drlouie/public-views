// DHTMLapi.js custom API for cross-platform
// object positioning by Danny Goodman (http://www.dannyg.com)

// Global variables
var isNav4, isIE4
var insideWindowWidth
var range = ""
var styleObj = ""
if (navigator.appVersion.charAt(0) == "4") {
	if (navigator.appName == "Netscape") {
		isNav4 = true
		insideWindowWidth = window.innerWidth
	} else {
		isIE4 = true
		range = "all."
		styleObj = ".style"
	}
}

// Convert object name string or object reference
// into a valid object reference
function getObject(obj) {
	var theObj
	if (typeof obj == "string") {
		theObj = eval("document." + range + obj + styleObj)
	} else {
		theObj = obj
	}
	return theObj
}

// Positioning an object at a specific pixel coordinate
function shiftTo(obj, x, y) {
	var theObj = getObject(obj)
	if (isNav4) {
		theObj.moveTo(x,y)
	} else {
		theObj.pixelLeft = x
		theObj.pixelTop = y
	}
}

// Moving an object by x and/or y pixels
function shiftBy(obj, deltaX, deltaY) {
	var theObj = getObject(obj)
	if (isNav4) {
		theObj.moveBy(deltaX, deltaY)
	} else {
		theObj.pixelLeft += deltaX
		theObj.pixelTop += deltaY
	}
}

// Setting the z-order of an object
function setZIndex(obj, zOrder) {
	var theObj = getObject(obj)
	theObj.zIndex = zOrder
}

// Setting the background color of an object
function setBGColor(obj, color) {
	var theObj = getObject(obj)
	if (isNav4) {
		theObj.bgColor = color
	} else {
		theObj.backgroundColor = color
	}
}

// Setting the visibility of an object to visible
function show(obj) {
	var theObj = getObject(obj)
	theObj.visibility = "visible"
}

// Setting the visibility of an object to hidden
function hide(obj) {
	var theObj = getObject(obj)
	theObj.visibility = "hidden"
}

// Retrieving the x coordinate of a positionable object
function getObjectLeft(obj)  {
	var theObj = getObject(obj)
	if (isNav4) {
		return theObj.left
	} else {
		return theObj.pixelLeft
	}
}

// Retrieving the y coordinate of a positionable object
function getObjectTop(obj)  {
	var theObj = getObject(obj)
	if (isNav4) {
		return theObj.top
	} else {
		return theObj.pixelTop
	}
}

function showProps(o, objName) {
	var result = ""
	count = 0
	for (var i in o) {
		result += o + "." + i + "=" + o[i] + "\n"
		count++
		if (count == 25) {
			alert(result)
			result = ""
			count = 0
		}
	}
	alert(result)
}
