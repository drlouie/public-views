currentX = currentY = 0;
whichEl = null;

if (ver4) {
    with (document) {
	write("<DIV ID='elDRAGOne'><P>Drag Me!</P></DIV>");
	write("<DIV ID='elTwoDRAG'>No, Me!</DIV>");
	write("<DIV ID='elDRAGThree'>Me, Me, Me!</DIV>");
	write("<DIV ID='elFourDRAG'><I><B><FONT>What a drag!</FONT></B></I></DIV>");
    }
}

if (NS4) {
    elDRAGOne = document.elDRAGOne;
    elTwoDRAG = document.elTwoDRAG;
    elDRAGThree = document.elDRAGThree;
    elFourDRAG = document.elFourDRAG;
}

function setEls(first) {
    if (!ver4) { return };
    if (NS4) {
        elDRAGOne.left = document.elAll.document.images["imOne"].x;
        elDRAGOne.top  = document.elAll.document.images["imOne"].y;
        elTwoDRAG.left = document.elAll.document.images["imTwo"].x;
        elTwoDRAG.top  = document.elAll.document.images["imTwo"].y;
        elDRAGThree.left = document.elAll.document.images["imThree"].x;
        elDRAGThree.top  = document.elAll.document.images["imThree"].y;
        elFourDRAG.left = document.elAll.document.images["imFour"].x;
        elFourDRAG.top  = document.elAll.document.images["imFour"].y;
        if (first) { document.elDRAGOne.visibility = document.elTwoDRAG.visibility = document.elDRAGThree.visibility = document.elFourDRAG.visibility = "visible"};
    }
    else {
        elDRAGOne.style.pixelLeft = 75;
        elDRAGOne.style.pixelTop  = elAll.offsetTop;
        elTwoDRAG.style.pixelLeft = 180;
        elTwoDRAG.style.pixelTop  = elAll.offsetTop;
        elDRAGThree.style.pixelLeft = 285;
        elDRAGThree.style.pixelTop  = elAll.offsetTop; 
        elFourDRAG.style.pixelLeft = 390;
        elFourDRAG.style.pixelTop  = elAll.offsetTop;
        if (first) { elDRAGOne.style.visibility = elTwoDRAG.style.visibility = elDRAGThree.style.visibility = elFourDRAG.style.visibility = "visible"};
    }
}

function grabEl(e) {
    if (IE4) {
        whichEl = event.srcElement;

        while (whichEl.id.indexOf("DRAG") == -1) {
            whichEl = whichEl.parentElement;
            if (whichEl == null) { return }
        }
    }
    else {
        mouseX = e.pageX;
        mouseY = e.pageY;

        for ( i=0; i<document.layers.length; i++ ) {
	    tempLayer = document.layers[i];
            if ( tempLayer.id.indexOf("DRAG") == -1 ) { continue }
            if ( (mouseX > tempLayer.left) && (mouseX < (tempLayer.left + tempLayer.clip.width)) && (mouseY > tempLayer.top) && (mouseY < (tempLayer.top + tempLayer.clip.height)) ) {
                whichEl = tempLayer;
            }
        } 

        if (whichEl == null) { return}
    }


if (whichEl != activeEl) {
    if (IE4) { whichEl.style.zIndex = activeEl.style.zIndex+1 }
        else { whichEl.moveAbove(activeEl) };
    activeEl = whichEl;
}
    if (IE4) {
        whichEl.style.pixelLeft = whichEl.offsetLeft;
        whichEl.style.pixelTop = whichEl.offsetTop;

        currentX = (event.clientX + document.body.scrollLeft);
        currentY = (event.clientY + document.body.scrollTop); 

    }
    else {
	currentX = e.pageX;
	currentY = e.pageY;

	document.captureEvents(Event.MOUSEMOVE);
	document.onmousemove = moveEl;
    }

    ww = (whichEl == elFourDRAG) ? "Ouch!!" : "Thanks!";
    qq = "<FONT COLOR=white><B>&nbsp;&nbsp;" + ww + "</B></FONT>";
    if (NS4) {
        whichEl.document.write(qq);
        whichEl.document.close();
    }
    else { whichEl.innerHTML = qq }
}

function moveEl(e) {
    if (whichEl == null) { return };

    if (IE4) {
        newX = (event.clientX + document.body.scrollLeft);
        newY = (event.clientY + document.body.scrollTop);
    }
    else {
        newX = e.pageX;
        newY = e.pageY;
    }
    distanceX = (newX - currentX);
    distanceY = (newY - currentY);
    currentX = newX;
    currentY = newY;

    if (IE4) {
        whichEl.style.pixelLeft += distanceX;
        whichEl.style.pixelTop += distanceY;
        event.returnValue = false;
    }
    else { whichEl.moveBy(distanceX,distanceY) }
}

function checkEl() {
    if (whichEl!=null) { return false }
}

function dropEl() {
    if (NS4) { document.releaseEvents(Event.MOUSEMOVE) }
    whichEl = null;
}

function cursEl() {
    if (event.srcElement.id.indexOf("DRAG") != -1) {
        event.srcElement.style.cursor = "move"
    }
}

if (ver4) {
    if (NS4) {
        document.captureEvents(Event.MOUSEDOWN | Event.MOUSEUP);
        activeEl = document.elFourDRAG
    }
    else {
        document.onmousemove = moveEl;
	document.onmouseover = cursEl;
        document.onselectstart = checkEl;
        activeEl= document.all.elFourDRAG;
    }

    document.onmousedown = grabEl;
    document.onmouseup = dropEl;
    setEls(true);
}
