window.status = "Loading fDr package..."; var cual = ''; var vis = ''; var sop = ''; var fop = ''; var c0p = ''; var voz = ''; var viz = ''; function sFO(cual,lapse) { cual = cual; lapse = lapse; voz.thisTimeout = window.setTimeout("fDr('" + cual + "','hide','96','20','100')",lapse); } function sFI(cual,lapse) { cual = cual; lapse = lapse; viz.thisTimeout = window.setTimeout("fDr('" + cual + "','show','01','96','00')",lapse); } var me = ''; function fDr(cual, vis, sop, fop, c0p) { if (voz.thisTimeout) { window.clearTimeout(voz.thisTimeout); } if (viz.thisTimeout) { window.clearTimeout(viz.thisTimeout); } if (me.thisTimeout) { window.clearTimeout(me.thisTimeout); } c0p = Number(c0p); if (vis == 'show') { if (fop > c0p) { nOp = Number(c0p + 1); c0p = nOp; } } else if (vis == 'hide') { if (fop < c0p) { nOp = Number(c0p - 1); c0p = nOp; } } myLayer = document.getElementById(""+cual+"").style; if (myLayer.MozOpacity) { myLayer.MozOpacity="." + c0p + ""; } else if (myLayer.filter) { myLayer.filter = "Alpha(Opacity=" + c0p + ");"; } me.thisTimeout = window.setTimeout("fDr('" + cual + "','" + sop + "','" + fop + "','" + vis + "','" + c0p + "')", 30); } window.status = "";