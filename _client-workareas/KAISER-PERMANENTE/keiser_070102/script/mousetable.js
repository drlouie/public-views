/*
Highlight Table Cells Script- 
Last updated: 99/01/21
© Dynamic Drive (www.dynamicdrive.com)
For full source code, installation instructions,
100's more DHTML scripts, and Terms Of
Use, visit dynamicdrive.com
*/

function runto(cual,highlightcolor){
source=cual;
while(source.tagName!="TR")
source=source.parentElement
if (source.style.backgroundColor!=highlightcolor&&source.id!="ignore")
source.style.backgroundColor=highlightcolor
}

function runback(cual,originalcolor){
source=cual;
while(source.tagName!="TR")
source=source.parentElement
if (source.style.backgroundColor!=originalcolor&&source.id!="ignore")
source.style.backgroundColor=originalcolor
}