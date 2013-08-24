//Writing out the iframe info we need.
if(bw.ie4 || (bw.ie5 && (!bw.ie55 || useBuffer))){ //FOR IE4 AND IE%
	document.write('<div id="bground"><table width="472" height="452" background="images/tables/tablebg.gif" border="0" cellpadding="0" cellspacing="0"><tr><td width="472" height="452">&nbsp;</td></tr></table></div><iframe id="divLoad"></iframe><div id="divCont"><div id="divIEText"></div></div>')
}else if(bw.ns4){ //FOR NETSCAPE 4
	document.write('<div id="bground"><table width="472" height="452" background="images/tables/tablebg.gif" border="0" cellpadding="0" cellspacing="0"><tr><td width="472" height="452">&nbsp;</td></tr></table></div><div id="divCont"><layer id="divLoad"></layer></div>')
}else if(bw.dom){ //FOR IE5.5 (if useBuffer is sets to 0) AND NETSCAPE 6 
	document.write('<div id="bground"><table width="472" height="452" background="images/tables/tablebg.gif" border="0" cellpadding="0" cellspacing="0"><tr><td width="472" height="452">&nbsp;</td></tr></table></div><iframe marginwidth="0" marginheight="0" allowTransparency="false" frameborder="0" id="divLoad" scrollbars="yes"></iframe>')
}