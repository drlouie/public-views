/*****************************************************************************
Copyright (c) 2001 Thomas Brattli (www.bratta.com)

eXperience DHTML coolMenus - Get it at www.bratta.com
Version 3.02
This script can be used freely as long as all copyright messages are
intact. 
******************************************************************************/
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

//MENU STARTING - The only thing to remember if you want to have more then 1 menu on the page is to name your menu with another name

oCMenu2=new makeCoolMenu("oCMenu2") //Making the menu object. Argument: menuname
oCMenu2.useframes=0 //Do you want to use the menus as coolframemenu or not? (in frames or not) - Value: 0 || 1
oCMenu2.frame="botOne" //The name of your main frame (where the menus should appear). Leave empty if you're not using frames - Value: "main_frame_name"

/*If you choose to have this code inside a linked js, or if your using frames it's important to set these variables. 
This will help you get your links to link to the right place even if your files are in different folders.
The offlineUrl variable is the actual path to the directory where you js file are locally. 
This is just so you can test it without uploading. Remember to start it with file:/// and only use slashes, no backward slashes!
Also remember to end with a slash                                                                                                 */
oCMenu2.offlineUrl="file:///C|/Inetpub/wwwroot/coolMenus/" //Value: "path_to_js_file_offline/"
//The onlineUrl variable is the online path to your script. Place in the full path to where your js file is. Remember to end with a slash.
oCMenu2.onlineUrl="http://www.dhtmlcentral.com/examples/withframes/" //Value: "path_to_js_file_online/"

oCMenu2.pagecheck=1 //Do you want the menu to check whether any of the subitems are out of the bouderies of the page and move them in again (this is not perfect but it hould work) - Value: 0 || 1
oCMenu2.checkscroll=1 //Do you want the menu to check whether the page have scrolled or not? For frames you should always set this to 1. You can set this to 2 if you want this feature only on explorer since netscape doesn't support the window.onscroll this will make netscape slower (only if not using frames) - Value: 0 || 1 || 2
oCMenu2.resizecheck=1 //Do you want the page to reload if it's resized (This should be on or the menu will crash in Netscape4) - Value: 0 || 1
oCMenu2.wait=1000 //How long to wait before hiding the menu on mouseout. Netscape 6 is a lot slower then Explorer, so to be sure that it works good enough there you should not have this lower then 500 - Value: milliseconds

//Background bar properties
oCMenu2.usebar=1 //If you want to use a background-bar for the top items set this on - Value: 1 || 0
oCMenu2.barcolor="#FF9900" //The color of the background bar - Value: "color"
oCMenu2.barwidth="menu" //The width of the background bar. Set this to "menu" if you want it to be the same width as the menu. (this will change to match the border if you have one) - Value: px || "%" || "menu"
oCMenu2.barheight="menu" //The height of the background bar. Set this to "menu" if you want it to be the same height as the menu. (this will change to match the border if you have one) - Value: px || "%" || "menu"
oCMenu2.barx="menu" //The left position of the bar. Set this to "menu" if you want it be the same as the left position of the menu. (this will change to match the border if you have one)  - Value: px || "%" || "menu"
oCMenu2.bary="menu" //The top position of the bar Set this to "menu" if you want it be the same as the top position of the menu. (this will change to match the border if you have one)  - Value: px || "%" || "menu"
oCMenu2.barinheritborder=0 //Set this to 1 if you want the bar to have the same border as the top menus - Value: 0 || 1

//Placement properties
oCMenu2.rows=0 //This controls whether the top items is supposed to be laid out in rows or columns. Set to 0 for columns and 1 for row - Value 0 || 1
oCMenu2.fromleft=10 //This is the left position of the menu. (Only in use if menuplacement below is 0 or aligned) (will change to adapt any borders) - Value: px || "%"
oCMenu2.fromtop=100 //This is the left position of the menu. (Only in use if menuplacement below is 0 or aligned) (will change to adapt any borders) - Value: px || "%"
oCMenu2.pxbetween=30 //How much space you want between each of the top items. - Value: px || "%"

/*You have several different ways to place the top items. 
You can have them right beside eachother (only adding the pxbetween variable)
oCMenu2.menuplacement=0

You can have them aligned to one of the sides - This is mostly when not using frames, but can be used in both conditions
Values: (If you get strange results check the fromleft,fromtop and pxbetween variables above)
For menus that are placed in columns (align=left or align=right (se below)) you can align them to the "right" or "center"
For menus that are placed in rows (align=top or align=bottom (se below)) you can align them to the "bottom", "center" or "bottomcenter"
oCMenu2.menuplacement="center"

You can also set them directly in pixels: (Remember to have as many array members as you have top items)
oCMenu2.menuplacement=new Array(10,200,400,600)

Or you can place in percentage: (remember to use the ' ' around the numbers)


Choose one of those options to get the desired results.
*/
oCMenu2.menuplacement=0

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
oCMenu2.level[0]=new Array() //Add this for each new level
oCMenu2.level[0].width=120 //The default width for each level[0] (top) items. You can override this on each item by spesifying the width when making the item. - Value: px || "%"
oCMenu2.level[0].height=25 //The default height for each level[0] (top) items. You can override this on each item by spesifying the height when making the item. - Value: px || "%"
oCMenu2.level[0].bgcoloroff="transparent" //The default background color for each level[0] (top) items. You can override this on each item by spesifying the backgroundcolor when making the item. - Value: "color"
oCMenu2.level[0].bgcoloron="#336699" //The default "on" background color for each level[0] (top) items. You can override this on each item by spesifying the "on" background color when making the item. - Value: "color"
oCMenu2.level[0].textcolor="#336699" //The default text color for each level[0] (top) items. You can override this on each item by spesifying the text color when making the item. - Value: "color"
oCMenu2.level[0].hovercolor="#FF9900" //The default "on" text color for each level[0] (top) items. You can override this on each item by spesifying the "on" text color when making the item. - Value: "color"
oCMenu2.level[0].style="padding:1px; font-family:tahoma,arial,helvetica; font-size:12px; font-weight:bold" //The style for all level[0] (top) items. - Value: "style_settings"
oCMenu2.level[0].border=0 //The border size for all level[0] (top) items. - Value: px
oCMenu2.level[0].bordercolor="red" //The border color for all level[0] (top) items. - Value: "color"
oCMenu2.level[0].offsetX=0 //The X offset of the submenus of this item. This does not affect the first submenus, but you need it here so it can be the default value for all levels. - Value: px
oCMenu2.level[0].offsetY=0 //The Y offset of the submenus of this item. This does not affect the first submenus, but you need it here so it can be the default value for all levels. - Value: px
oCMenu2.level[0].NS4font="tahoma,arial,helvetica"
oCMenu2.level[0].NS4fontSize="2"
/*And last but not least the align variable.

This spesifies how the submenus of this level comes out. 
Values:
"bottom": The sub menus of this level will come out on the top of this item
"top": The sub menus of this level will come out on the bottom of this item
"left": The sub menus of this level will come out on the right of this item
"right": The sub menus of this level will come out on the left of this item

In generally "left" and "right" works best for menus in columns and "top" and "bottom" works best for menus in rows. 
But by all means feel free to play with it.

If you have set pagecheck to 1 above this is what the pagecheck will change when reaching the bounderies of the page.
If it reaches the right boundery and it's aligned left it will change the align to right and so on.
*/
oCMenu2.level[0].align="right" //Value: "top" || "bottom" || "left" || "right" 

//EXAMPLE SUB LEVEL[1] PROPERTIES - You have to spesify the properties you want different from LEVEL[0] - If you want all items to look the same just remove this
oCMenu2.level[1]=new Array() //Add this for each new level (adding one to the number)
oCMenu2.level[1].width=oCMenu2.level[0].width-2
oCMenu2.level[1].height=22
oCMenu2.level[1].bgcoloroff="#FF9900"
oCMenu2.level[1].bgcoloron="#006699"
oCMenu2.level[1].style="padding:2px; font-family:tahoma, arial,helvetica; font-size:11px; font-weight:bold"
oCMenu2.level[1].align="right" 
oCMenu2.level[1].offsetX=0
oCMenu2.level[1].offsetY=0
oCMenu2.level[1].border=1 
oCMenu2.level[1].bordercolor="#006699"

//EXAMPLE SUB LEVEL[2] PROPERTIES - You have to spesify the properties you want different from LEVEL[1] OR LEVEL[0] - If you want all items to look the same just remove this
oCMenu2.level[2]=new Array() //Add this for each new level (adding one to the number)
oCMenu2.level[2].width=oCMenu2.level[0].width
oCMenu2.level[2].height=20
oCMenu2.level[2].bgcoloroff="#FF9900"
oCMenu2.level[2].bgcoloron="#67FF00"
oCMenu2.level[2].style="padding:2px; font-family:tahoma,arial,helvetica; font-size:10px; font-weight:bold"
oCMenu2.level[2].align="right" 
oCMenu2.level[2].offsetX=0
oCMenu2.level[2].offsetY=0
oCMenu2.level[2].border=1 
oCMenu2.level[2].bordercolor="#006699"
oCMenu2.level[2].NS4font="tahoma,arial,helvetica"
oCMenu2.level[2].NS4fontSize="1"

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
oCMenu2.makeMenu('top0','','&nbsp;News','/news/index.asp','')
	oCMenu2.makeMenu('sub00','top0','Newest news','/news/index.asp')
		oCMenu2.makeMenu('sub001','sub00','- New DHTML API released','','',160,0)
		oCMenu2.makeMenu('sub002','sub00','- Explorer 7 is out','','',160,0)
		oCMenu2.makeMenu('sub003','sub00','- Opera 6 supports innerHTML','','',160,0)
	oCMenu2.makeMenu('sub01','top0','News archive','/news/archive.asp')
	
oCMenu2.makeMenu('top1','','&nbsp;Scripts','/scripts/index.asp')
	oCMenu2.makeMenu('sub10','top1','New scripts','/scripts/index.asp?show=new')
	oCMenu2.makeMenu('sub11','top1','All scripts','/scripts/index.asp?show=all')
	oCMenu2.makeMenu('sub12','top1','Popular scripts','/scripts/index.asp?show=pop')
	
oCMenu2.makeMenu('top2','','&nbsp;Articles','/articles/index.asp')
	oCMenu2.makeMenu('sub21','top2','Tutorials','/tutorials/index.asp')
		oCMenu2.makeMenu('sub210','sub21','New tutorials','/tutorials/index.asp')
		oCMenu2.makeMenu('sub211','sub21','Tutorials archive','/tutorials/archive.asp')
	oCMenu2.makeMenu('sub22','top2','Other articles','/articles/index.asp')
		oCMenu2.makeMenu('sub220','sub22','New articles','/articles/index.asp?show=new')
		oCMenu2.makeMenu('sub221','sub22','Article archive','/articles/archive.asp')

oCMenu2.makeMenu('top3','','&nbsp;Forums','/forums/')
	oCMenu2.makeMenu('sub30','top3','General','/forums/forum.asp?FORUM_ID=6&CAT_ID=1&Forum_Title=General+DHTML+issues')
	oCMenu2.makeMenu('sub31','top3','Scripts','/forums/forum.asp?FORUM_ID=4&CAT_ID=1&Forum_Title=DHTML+Scripts')
	oCMenu2.makeMenu('sub32','top3','Crossbrowser','/forums/forum.asp?FORUM_ID=3&CAT_ID=1&Forum_Title=Crossbrowser+DHTML')
	oCMenu2.makeMenu('sub33','top3','CoolMenus','/forums/forum.asp?FORUM_ID=2&CAT_ID=1&Forum_Title=CoolMenus')
	oCMenu2.makeMenu('sub34','top3','dhtmlcentral.com','/forums/forum.asp?FORUM_ID=5&CAT_ID=1&Forum_Title=dhtmlcentral%2Ecom')
	oCMenu2.makeMenu('sub35','top3','Cool sites','/forums/forum.asp?FORUM_ID=1&CAT_ID=1&Forum_Title=Cool+sites')

oCMenu2.makeMenu('top5','','&nbsp;CoolMenus','/coolmenus/index.asp')
	oCMenu2.makeMenu('sub50','top5','Examples','/coolmenus/examples.asp')
		oCMenu2.makeMenu('sub500','sub50','With frames','/coolmenus/examples.asp?show=with')
		oCMenu2.makeMenu('sub501','sub50','Without frames','/coolmenus/examples.asp?show=without')
	oCMenu2.makeMenu('sub51','top5','Download','/coolmenus/download.asp')
		oCMenu2.makeMenu('sub510','sub51','Download the source code to this menu','/coolmenus/download.asp','',150,40)
	oCMenu2.makeMenu('sub52','top5','Tutorial','/coolmenus/tutorial.asp')
		oCMenu2.makeMenu('sub520','sub52','Learn how to set up the menu','/coolmenus/tutorial.asp','',150,40)
	oCMenu2.makeMenu('sub53','top5','MenuMaker','','',0,0,'','','','','','','window.open("/coolmenus/maker/","","width=800,height=600")')
		oCMenu2.makeMenu('sub530','sub53','Use the menuMaker to make the menu code for you','','',150,40,'','','','','','','window.open("/coolmenus/maker/","","width=800,height=600")')
	oCMenu2.makeMenu('sub54','top5','FAQ','/coolmenus/faq.asp')
		oCMenu2.makeMenu('sub540','sub54','Frequently asked questions','coolmenus/faq.asp','',150,40)
	oCMenu2.makeMenu('sub55','top5','Help forum','/forums/forum.asp?FORUM_ID=2&CAT_ID=1&Forum_Title=CoolMenus')
		oCMenu2.makeMenu('sub550','sub55','Go to this forum and post you problems or suggestions regarding the CoolMenus','/forum/forum.asp?forum_id=2','',150,40)

oCMenu2.makeMenu('top6','','&nbsp;dhtmlcentral','dhtmlcentral/index.asp')
	oCMenu2.makeMenu('sub060','top6','Sitemap','dhtmlcentral/sitemap.asp')
	oCMenu2.makeMenu('sub061','top6','Who and why?','dhtmlcentral/who.asp')
	oCMenu2.makeMenu('sub062','top6','Help','dhtmlcentral/help.asp')
	oCMenu2.makeMenu('sub063','top6','Link to us','dhtmlcentral/link.asp')
	oCMenu2.makeMenu('sub064','top6','Advertise','dhtmlcentral/advertise.asp')
		
		
//Leave these two lines! Making the styles and then constructing the menu


	oCMenu2.makeStyle(); 
	oCMenu2.construct()