/*****************************************************************************
Default browsercheck - Leave this one
******************************************************************************/
function lib_bwcheck(){ //Browsercheck (needed)
	this.ver=navigator.appVersion; this.agent=navigator.userAgent
	this.dom=document.getElementById?1:0
	this.ie5=(this.ver.indexOf("MSIE 5")>-1 && this.dom)?1:0;
	this.ie6=(this.ver.indexOf("MSIE 6")>-1 && this.dom)?1:0;
	this.ie4=(document.all && !this.dom)?1:0;
	this.ie=this.ie4||this.ie5||this.ie6
	this.mac=this.agent.indexOf("Mac")>-1
	this.opera5=this.agent.indexOf("Opera 5")>-1
	this.ns6=(this.dom && parseInt(this.ver) >= 5) ?1:0; 
	this.ns4=(document.layers && !this.dom)?1:0;
	this.bw=(this.ie6 || this.ie5 || this.ie4 || this.ns4 || this.ns6 || this.opera5 || this.dom)
	return this
}
var bw=new lib_bwcheck() //Making browsercheck object

var mDebugging=2 //General debugging variable. Set to 0 for no debugging, 1 for alerts or 2 for status debugging.

oCMenu=new makeCoolMenu("oCMenu") //Making the menu object. Argument: menuname
oCMenu.useframes=0 //Do you want to use the menus as coolframemenu or not? (in frames or not) - Value: 0 || 1
oCMenu.frame="" //The name of your main frame (where the menus should appear). Leave empty if you're not using frames - Value: "main_frame_name"

/*If you set this to 1 you will get a "hand" cursor when moving over the links in NS4. The only downside to it is that 
if you're using frames and you don't have spesified that the links should have no "underline" you will get lines on the links.
In that case you have to add this STYLE setting to ALL the pages that will be loaded in the main frame:
<style>A.clNS4{text-decoration:none; padding:YOUR_PADDING}</style>  (if you don't want padding just remove the padding stuff)*/
oCMenu.useNS4links=1 

//After adding the "hover effect" for netscape as well, all styles are lost. But if you want padding add it here.
oCMenu.NS4padding=3 

//If you have select boxes close to your menu the menu will check for that and hide them if they are in the way of the menu.
//This feature does unfortunatly not work in NS4!
oCMenu.checkselect=0

/*If you choose to have this code inside a linked js, or if your using frames it's important to set these variables. 
This will help you get your links to link to the right place even if your files are in different folders.
The offlineUrl variable is the actual path to the directory where you js file are locally. 
This is just so you can test it without uploading. Remember to start it with file:/// and only use slashes, no backward slashes!
Also remember to end with a slash                                                                                                 */
oCMenu.offlineUrl="" //Value: "path_to_menu_file_offline/"
//The onlineUrl variable is the online path to your script. Place in the full path to where your js file is. Remember to end with a slash.
oCMenu.onlineUrl="" //Value: "path_to_menu_file_online/"


oCMenu.pagecheck=1 //Do you want the menu to check whether any of the subitems are out of the bouderies of the page and move them in again (this is not perfect but it hould work) - Value: 0 || 1
oCMenu.checkscroll=0 //Do you want the menu to check whether the page have scrolled or not? For frames you should always set this to 1. You can set this to 2 if you want this feature only on explorer since netscape doesn't support the window.onscroll this will make netscape slower (only if not using frames) - Value: 0 || 1 || 2
oCMenu.resizecheck=1 //Do you want the page to reload if it's resized (This should be on or the menu will crash in Netscape4) - Value: 0 || 1
oCMenu.wait=1000 //How long to wait before hiding the menu on mouseout. Netscape 6 is a lot slower then Explorer, so to be sure that it works good enough there you should not have this lower then 500 - Value: milliseconds

//Background bar properties
oCMenu.usebar=0 //If you want to use a background-bar for the top items set this on - Value: 1 || 0
oCMenu.barcolor="" //The color of the background bar - Value: "color"
oCMenu.barwidth="menu" //The width of the background bar. Set this to "menu" if you want it to be the same width as the menu. (this will change to match the border if you have one) - Value: px || "%" || "menu"
oCMenu.barheight="100%" //The height of the background bar. Set this to "menu" if you want it to be the same height as the menu. (this will change to match the border if you have one) - Value: px || "%" || "menu"
oCMenu.barx="menu" //The left position of the bar. Set this to "menu" if you want it be the same as the left position of the menu. (this will change to match the border if you have one)  - Value: px || "%" || "menu"
oCMenu.bary=0 //The top position of the bar Set this to "menu" if you want it be the same as the top position of the menu. (this will change to match the border if you have one)  - Value: px || "%" || "menu"
oCMenu.barinheritborder=0 //Set this to 1 if you want the bar to have the same border as the top menus - Value: 0 || 1

//Placement properties
oCMenu.rows=0 //This controls whether the top items is supposed to be laid out in rows or columns. Set to 0 for columns and 1 for row - Value 0 || 1
oCMenu.fromleft=0 //This is the left position of the menu. (Only in use if menuplacement below is 0 or aligned) (will change to adapt any borders) - Value: px || "%"
oCMenu.fromtop=106 //This is the left position of the menu. (Only in use if menuplacement below is 0 or aligned) (will change to adapt any borders) - Value: px || "%"
oCMenu.pxbetween=3 //How much space you want between each of the top items. - Value: px || "%"

/*You have several different ways to place the top items. 
You can have them right beside eachother (only adding the pxbetween variable)
oCMenu.menuplacement=0

You can have them aligned to one of the sides - This is mostly when not using frames, but can be used in both conditions
Values: (If you get strange results check the fromleft,fromtop and pxbetween variables above)
For menus that are placed in columns (align=left or align=right (se below)) you can align them to the "right" or "center"
For menus that are placed in rows (align=top or align=bottom (se below)) you can align them to the "bottom", "center" or "bottomcenter"
oCMenu.menuplacement="center"

You can also set them directly in pixels: (Remember to have as many array members as you have top items)
oCMenu.menuplacement=new Array(10,200,400,600)

Or you can place in percentage: (remember to use the ' ' around the numbers)


Choose one of those options to get the desired results.
*/
oCMenu.menuplacement=0

/*
Now we are ready for the properties of each level. For those of that have used the old 
coolmenus for coolframemenu I will try and explain how this works like this:
level[0] = top items
level[1] = sub items
level[2] = sub2 items
level[3] = sub3 items and so on....
All menus will inherit the properties, and all properties does only HAVE to be spesifed on the top level. 
If a level doesn't have on property spesified it will look for it on the last level that was spesified, 
if it still doesn't exist it will get the properties from level[0]

Which means that if you set the background color on level[0] to "black" and doesn't spesify any more levels or doesn't 
spesify the background color on the last level you spesified ALL menus will get the color from level[0]

Did that make sense at all? This can be a little hard to understand, look at the different examples on my site
and play with and I am sure you'll get what I mean.
*/

//TOP LEVEL PROPERTIES - ALL OF THESE MUST BE SPESIFIED FOR LEVEL[0]
oCMenu.level[0]=new Array() //Add this for each new level
oCMenu.level[0].width=172 //The default width for each level[0] (top) items. You can override this on each item by spesifying the width when making the item. - Value: px || "%"
oCMenu.level[0].height=20 //The default height for each level[0] (top) items. You can override this on each item by spesifying the height when making the item. - Value: px || "%"
oCMenu.level[0].bgcoloroff="CBCBD7" //The default background color for each level[0] (top) items. You can override this on each item by spesifying the backgroundcolor when making the item. - Value: "color"
oCMenu.level[0].bgcoloron="8F8FAB" //The default "on" background color for each level[0] (top) items. You can override this on each item by spesifying the "on" background color when making the item. - Value: "color"
oCMenu.level[0].textcolor="333366" //The default text color for each level[0] (top) items. You can override this on each item by spesifying the text color when making the item. - Value: "color"
oCMenu.level[0].hovercolor="FFFFFF" //The default "on" text color for each level[0] (top) items. You can override this on each item by spesifying the "on" text color when making the item. - Value: "color"
oCMenu.level[0].style="padding:3px; font-family:verdana,arial,helvetica; font-size:11px; font-weight:bold" //The style for all level[0] (top) items. - Value: "style_settings"
oCMenu.level[0].border=1 //The border size for all level[0] (top) items. - Value: px
oCMenu.level[0].bordercolor="8F8FAB" //The border color for all level[0] (top) items. - Value: "color"
oCMenu.level[0].offsetX=2 //The X offset of the submenus of this item. This does not affect the first submenus, but you need it here so it can be the default value for all levels. - Value: px
oCMenu.level[0].offsetY=0 //The Y offset of the submenus of this item. This does not affect the first submenus, but you need it here so it can be the default value for all levels. - Value: px
oCMenu.level[0].NS4font="verdana,arial,helvetica"
oCMenu.level[0].NS4fontSize="1"
oCMenu.level[0].pxbetween=2
oCMenu.level[0].align="right" //Value: "top" || "bottom" || "left" || "right" 
oCMenu.level[1]=new Array() //Add this for each new level (adding one to the number)
oCMenu.level[1].width=172
oCMenu.level[1].height=18
oCMenu.level[1].bgcoloroff="CBCBD7" //The default background color for each level[0] (top) items. You can override this on each item by spesifying the backgroundcolor when making the item. - Value: "color"
oCMenu.level[1].bgcoloron="8F8FAB" //The default "on" background color for each level[0] (top) items. You can override this on each item by spesifying the "on" background color when making the item. - Value: "color"
oCMenu.level[1].textcolor="333366" //The default text color for each level[0] (top) items. You can override this on each item by spesifying the text color when making the item. - Value: "color"
oCMenu.level[1].hovercolor="FFFFFF" //The default "on" text color for each level[0] (top) items. You can override this on each item by spesifying the "on" text color when making the item. - Value: "color"
oCMenu.level[1].style="padding:3px; font-family:verdana,arial,helvetica; font-size:10px; font-weight:bold" //The style for all level[0] (top) items. - Value: "style_settings"
oCMenu.level[1].border=1 //The border size for all level[0] (top) items. - Value: px
oCMenu.level[1].bordercolor="8F8FAB" //The border color for all level[0] (top) items. - Value: "color"
oCMenu.level[1].offsetX=2 //The X offset of the submenus of this item. This does not affect the first submenus, but you need it here so it can be the default value for all levels. - Value: px
oCMenu.level[1].offsetY=0 //The Y offset of the submenus of this item. This does not affect the first submenus, but you need it here so it can be the default value for all levels. - Value: px
oCMenu.level[1].NS4font="verdana,arial,helvetica"
oCMenu.level[1].NS4fontSize="1"
oCMenu.level[1].pxbetween=2
oCMenu.level[1].align="right" //Value: "top" || "bottom" || "left" || "right" 
/*Variables for each menu item: (** means that they have to be spesified!)
name: The name of the item. This must be unique for each item. Do not use spaces or strange charachters in this one! **
parent: The name of the menuitem you want this to "connect" to. This will be a submenu of the item that have the name you place in here. ** for all other then the topitems
text: The text you want in the item. ** (except if you use images) 
link: The page you want this item to link to.
target: The target window or frame you want the link to go to (Default is same window if you're not using frames, and the mainframe if you're using frames)
width: The width of the element. If not spesified it will get the default width spesified above.
height: The height of the element. If not spesified it will get the default height spesified above.
img1: The "off" image for element if you want to use images.
img2: The image that appears onmouseover if using images.
bgcoloroff: The background color for this item. If not spesified it will get the default background color spesified above.
bgcoloron: The "on" background color for this item. If not spesified it will get the default "on" background color spesified above.
textcolor: The text color for this item. If not spesified it will get the default text color spesified above.
hovercolor: The "on" text color for this item. If not spesified it will get the default "on" text color spesified above. Netscape4 ignores this
onclick: If you want something to happen when the element is clicked (different from going to a link) spesifiy it here.
onmouseover: This will happen when you mouseover the element. Could be status text, another imageswap or whatever.
onmouseout: This will happen when you mouseout the element.

Remember you can have as many levels/sublevels as you want. Just make sure you spesify the correct "parent" for each item.
To set styles for each level see above.
*/
oCMenu.makeMenu('top0','','<font class=\"menu1\">Product Catalog</font>','','',0,0,'','')
	oCMenu.makeMenu('sub00','top0','Value Desktop PCs','','',0,0,'','')
		oCMenu.makeMenu('sub001','sub00','Thresher Series','http://www.coastlinemicro.com/products.cgi?title=thresher&loadthis=/sharktank/thresher/index.html','',0,0,'','')
	oCMenu.makeMenu('sub01','top0','Performance Desktop PCs','','',0,0,'','')
		oCMenu.makeMenu('sub002','sub01','Mako Series','http://www.coastlinemicro.com/products.cgi?title=mako&loadthis=/sharktank/mako/index.html','',0,0,'','')
	oCMenu.makeMenu('sub02','top0','PIII Servers','','',0,0,'','')
		oCMenu.makeMenu('sub003','sub02','Tiger Series','http://www.coastlinemicro.com/products.cgi?title=tiger&loadthis=/sharktank/tiger/index.html','',0,0,'','')
	oCMenu.makeMenu('sub03','top0','Xeon Servers','','',0,0,'','')
		oCMenu.makeMenu('sub004','sub03','Great White Series','http://www.coastlinemicro.com/products.cgi?title=gw&loadthis=/sharktank/gw/index.html','',0,0,'','')
	oCMenu.makeMenu('sub04','top0','Notebooks','','',0,0,'','')
		oCMenu.makeMenu('sub005','sub04','Reef Series','http://www.coastlinemicro.com/products.cgi?title=reef&loadthis=/sharktank/reef/index.html','',0,0,'','')
	oCMenu.makeMenu('sub05','top0','Intel Networking','http://www.coastlinemicro.com/everything_intel.cgi?title=intel','',0,0,'','')

oCMenu.makeMenu('top1','','Customer Support','','',0,0,'','')
	oCMenu.makeMenu('sub06','top1','Customer Service','http://www.coastlinemicro.com/support.cgi?title=cs','',0,0,'','')
	oCMenu.makeMenu('sub07','top1','Technical Support','http://www.coastlinemicro.com/support.cgi?title=ts','',0,0,'','')

oCMenu.makeMenu('top2','','Contact Us','','',0,0,'','')
	oCMenu.makeMenu('sub08','top2','Store Access Request','http://www.coastlinemicro.com/contact.cgi?title=access_request','',0,0,'','')
	oCMenu.makeMenu('sub09','top2','Credit Application','http://www.coastlinemicro.com/contact.cgi?title=credit','',0,0,'','')
	oCMenu.makeMenu('sub10','top2','General Comments','http://www.coastlinemicro.com/contact.cgi?title=gencomments','',0,0,'','')
	oCMenu.makeMenu('sub11','top2','Site Comments','http://www.coastlinemicro.com/contact.cgi?title=sitecomments','',0,0,'','')
	
oCMenu.makeMenu('top3','','Client Services','','',0,0,'','')
	oCMenu.makeMenu('sub12','top3','Configuration & Assembly','http://www.coastlinemicro.com/services.cgi?title=config','',0,0,'','')
	oCMenu.makeMenu('sub13','top3','Internet/Intranet','http://www.coastlinemicro.com/services.cgi?title=inter_intra','',0,0,'','')
	oCMenu.makeMenu('sub14','top3','Networking','http://www.coastlinemicro.com/services.cgi?title=networking','',0,0,'','')
	oCMenu.makeMenu('sub15','top3','Requirement Analysis','http://www.coastlinemicro.com/services.cgi?title=requirement','',0,0,'','')
	oCMenu.makeMenu('sub16','top3','Product Shipping','http://www.coastlinemicro.com/services.cgi?title=shipping','',0,0,'','')
	oCMenu.makeMenu('sub17','top3','System Testing','http://www.coastlinemicro.com/services.cgi?title=testing','',0,0,'','')
	oCMenu.makeMenu('sub18','top3','Service Contracts','http://www.coastlinemicro.com/services.cgi?title=contracts','',0,0,'','')
		
oCMenu.makeMenu('top4','','About Coastline Micro','','',0,0,'','')
	oCMenu.makeMenu('sub19','top4','Company Location','http://www.coastlinemicro.com/aboutus.cgi?title=location','',0,0,'','')
	oCMenu.makeMenu('sub20','top4','Heritage','http://www.coastlinemicro.com/aboutus.cgi?title=heritage','',0,0,'','')
	oCMenu.makeMenu('sub21','top4','Press Releases','http://www.coastlinemicro.com/press.cgi','',0,0,'','')
	oCMenu.makeMenu('sub22','top4','Product Authorizations','http://www.coastlinemicro.com/aboutus.cgi?title=auth','',0,0,'','')

oCMenu.makeMenu('top5','','Related Links','','',0,0,'','')
	oCMenu.makeMenu('sub23','top5','ChannelWeb.com','http://www.coastlinemicro.com/go.cgi?new_url=http://www.channelweb.com/','',0,0,'','')
	oCMenu.makeMenu('sub24','top5','CMP.com','http://www.coastlinemicro.com/go.cgi?new_url=http://www.cmp.com/','',0,0,'','')
	oCMenu.makeMenu('sub25','top5','CRN.com','http://www.coastlinemicro.com/go.cgi?new_url=http://www.crn.com/','',0,0,'','')
	oCMenu.makeMenu('sub26','top5','NetworkVAR.com','http://www.coastlinemicro.com/go.cgi?new_url=http://www.networkvar.com/','',0,0,'','')
		
//Leave these two lines! Making the styles and then constructing the menu
oCMenu.makeStyle(); oCMenu.construct()		