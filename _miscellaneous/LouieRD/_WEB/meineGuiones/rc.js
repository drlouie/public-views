window.status = "Initializing Radio Controls"; onR = new Image(); onR.src = "unserImagenes/show_radio.gif"; offR = new Image(); offR.src = "unserImagenes/hide_radio.gif";
ns4 = (document.layers)? true:false
ie4 = (document.all)? true:false
var xpos = -230; var ypos = 0; var tA = ''; var tB = ''; var tBL = 0; var fL = 0; var timC = 0; var rSD = 0; var mvI = ''; var moveO = ''; function rR() { sFI('bD','250'); mI(); } function cP() { if (fL == 0 && (xpos == 0 || xpos == -230) && timC != 0) { rSD = 1; window.status = ""; } if (fL == 1 || timC == 0 || rSD == 1) { if (xpos == 0) { m0(); } else if (xpos == -230) { mI(); } timC++; } if (tA.thisTimeout) { window.clearTimeout(tA.thisTimeout); } } function cP2nd() { if (rSD == 0) { fL = 1; window.status = ""; cP(); } if (tB.thisTimeout) { window.clearTimeout(tB.thisTimeout); } } function mI() { if (xpos < 0) { xpos += 2; document.getElementById("bD").style.left = xpos + "px"; mvI.thisTimeout = window.setTimeout("mI()",1); } else { if (ns4) { document.bD.document.images['rB'].src = offR.src; } else { document.images['rB'].src = offR.src; } if (mvI.thisTimeout) { window.clearTimeout(mvI.thisTimeout); }	} } function m0() { if (xpos > -230){ xpos -= 2; document.getElementById("bD").style.left = xpos + "px"; moveO.thisTimeout = window.setTimeout("m0()",1); } else { if (ns4) { document.bD.document.images['rB'].src = onR.src; } else { document.images['rB'].src = onR.src; } if (moveO.thisTimeout) { window.clearTimeout(moveO.thisTimeout); } } }
