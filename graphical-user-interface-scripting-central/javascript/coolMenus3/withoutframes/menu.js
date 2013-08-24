var mDebugging=2 

oCMenu=new makeCoolMenu("oCMenu") 
oCMenu.useframes=0 
oCMenu.frame="frmMain"
oCMenu.useNS4links=1 
oCMenu.checkselect=0
oCMenu.offlineUrl="file:///C|/Inetpub/wwwroot/dhtmlcentral/"
oCMenu.onlineUrl="http://www.dhtmlcentral.com/"


oCMenu.pagecheck=1
oCMenu.checkscroll=2
oCMenu.resizecheck=1 
oCMenu.wait=1000 

oCMenu.usebar=1 
oCMenu.barcolor="#336699" 
oCMenu.barwidth="100%" 
oCMenu.barheight="menu" 
oCMenu.barx=0 
oCMenu.bary="menu"
oCMenu.barinheritborder=0 

oCMenu.rows=1
oCMenu.fromleft=170 
oCMenu.fromtop=118 
oCMenu.pxbetween=0

avail="190+((toppage.x2-210)/6)" 
oCMenu.menuplacement=new Array(190,avail,avail+"*2",avail+"*3",avail+"*4",avail+"*5")

oCMenu.level[0]=new Array() 
oCMenu.level[0].width=90 
oCMenu.level[0].height=19 
oCMenu.level[0].bgcoloroff="transparent"
oCMenu.level[0].bgcoloron="transparent" 
oCMenu.level[0].textcolor="red"
oCMenu.level[0].hovercolor="#FCCE55" 
oCMenu.level[0].style="font-family:arial,helvetica; font-size:12px; font-weight:bold"
oCMenu.level[0].border=0 
oCMenu.level[0].bordercolor="" 
oCMenu.level[0].offsetX=0 
oCMenu.level[0].offsetY=-1 
oCMenu.level[0].NS4font="arial,helvetica"
oCMenu.level[0].NS4fontSize="2"
oCMenu.level[0].NS4fontColor="white"
oCMenu.level[0].align="bottom" 

oCMenu.level[1]=new Array() 
oCMenu.level[1].width=110
oCMenu.level[1].height=22
oCMenu.level[1].bgcoloroff="#CDDBEB"
oCMenu.level[1].bgcoloron="#006699"
oCMenu.level[1].textcolor="#006699"
oCMenu.level[1].hovercolor="#FCCE55"
oCMenu.level[1].style="padding:2px; font-family:arial,helvetica; font-size:11px; font-weight:bold"
oCMenu.level[1].align="bottom" 
oCMenu.level[1].offsetX=0
oCMenu.level[1].offsetY=0
oCMenu.level[1].border=1 
oCMenu.level[1].bordercolor="#006699"
oCMenu.level[1].NS4font="arial,helvetica"
oCMenu.level[1].NS4fontSize="2"
oCMenu.level[1].NS4fontColor="black"

oCMenu.level[2]=new Array()
oCMenu.level[2].width=150
oCMenu.level[2].height=20
oCMenu.level[2].style="padding:2px; font-family: arial,helvetica; font-size:10px; font-weight:bold"
oCMenu.level[2].align="bottom" 
oCMenu.level[2].offsetX=0
oCMenu.level[2].offsetY=0
oCMenu.level[2].border=1 
oCMenu.level[2].bordercolor="#006699"
oCMenu.level[2].NS4fontSize="1"
oCMenu.level[2].NS4fontColor="black"
oCMenu.level[2].bgcoloroff="#CDDBEB"
oCMenu.level[2].bgcoloron="#006699"
oCMenu.level[2].textcolor="#006699"
oCMenu.level[2].hovercolor="#CDDBEB"

oCMenu.makeMenu('top0','','&nbsp;News','news/index.asp','')
	oCMenu.makeMenu('sub00','top0','Newest news','news/index.asp')
		oCMenu.makeMenu('sub001','sub00','- Welcome to this beta version','news/index.asp','',160,0)
	oCMenu.makeMenu('sub01','top0','News archive','news/archive.asp')
	
oCMenu.makeMenu('top1','','&nbsp;Scripts','script/index.asp')
	oCMenu.makeMenu('sub10','top1','New scripts','script/index.asp?show=new')
	oCMenu.makeMenu('sub11','top1','All scripts','script/index.asp?show=all')
	oCMenu.makeMenu('sub12','top1','Popular scripts','script/index.asp?show=pop')
	
oCMenu.makeMenu('top2','','&nbsp;Articles','articles/index.asp')
	oCMenu.makeMenu('sub21','top2','Tutorials','tutorials/index.asp')
		oCMenu.makeMenu('sub210','sub21','New tutorials','tutorials/index.asp')
		oCMenu.makeMenu('sub211','sub21','Tutorials archive','tutorials/archive.asp')
	oCMenu.makeMenu('sub22','top2','Other articles','articles/index.asp')
		oCMenu.makeMenu('sub220','sub22','New articles','articles/index.asp?show=new')
		oCMenu.makeMenu('sub221','sub22','Article archive','articles/archive.asp')

oCMenu.makeMenu('top3','','&nbsp;Forums','forums/')
	oCMenu.makeMenu('sub30','top3','General','forums/forum.asp?FORUM_ID=6&CAT_ID=1&Forum_Title=General+DHTML+issues')
	oCMenu.makeMenu('sub31','top3','Scripts','forums/forum.asp?FORUM_ID=4&CAT_ID=1&Forum_Title=DHTML+Scripts')
	oCMenu.makeMenu('sub32','top3','Crossbrowser','forums/forum.asp?FORUM_ID=3&CAT_ID=1&Forum_Title=Crossbrowser+DHTML')
	oCMenu.makeMenu('sub33','top3','CoolMenus','forums/forum.asp?FORUM_ID=2&CAT_ID=1&Forum_Title=CoolMenus')
	oCMenu.makeMenu('sub34','top3','dhtmlcentral.com','forums/forum.asp?FORUM_ID=5&CAT_ID=1&Forum_Title=dhtmlcentral%2Ecom')
	oCMenu.makeMenu('sub35','top3','Cool sites','forums/forum.asp?FORUM_ID=1&CAT_ID=1&Forum_Title=Cool+sites')

oCMenu.makeMenu('top5','','&nbsp;CoolMenus','coolmenus/index.asp')
	oCMenu.makeMenu('sub50','top5','Examples','coolmenus/examples/')
	oCMenu.makeMenu('sub51','top5','Download','coolmenus/download.asp')
		oCMenu.makeMenu('sub510','sub51','Download the source code to this menu','coolmenus/download.asp','',150,40)
	oCMenu.makeMenu('sub52','top5','Tutorial','coolmenus/tutorial.asp')
		oCMenu.makeMenu('sub520','sub52','Learn how to set up the menu','coolmenus/tutorial.asp','',150,40)
	oCMenu.makeMenu('sub53','top5','MenuMaker','','_blank',0,0,'','','','','','','if(!bw.ns4)window.open("/coolmenus/maker/","","width=800,height=600")')
		oCMenu.makeMenu('sub530','sub53','Use the menuMaker to make the menu code for you<br>(the menumaker does not work in Netscap4)','','_blank',150,50,'','','','','','','if(!bw.ns4)window.open("/coolmenus/maker/","","width=800,height=600")')
	oCMenu.makeMenu('sub54','top5','FAQ','faq/index.asp')
		oCMenu.makeMenu('sub540','sub54','Frequently asked questions','coolmenus/faq.asp','',150,40)
	oCMenu.makeMenu('sub55','top5','Help forum','forums/forum.asp?FORUM_ID=2&CAT_ID=1&Forum_Title=CoolMenus')
		oCMenu.makeMenu('sub550','sub55','Go to this forum and post you problems or suggestions regarding the CoolMenus','forum/forum.asp?forum_id=2','',150,40)

oCMenu.makeMenu('top6','','&nbsp;dhtmlcentral','dhtmlcentral/index.asp')
	oCMenu.makeMenu('sub060','top6','This site is made by Thomas Brattli from www.bratta.com. The site is still in beta, info will come here when it\'s ready','http://www.bratta.com/','',0,130)


oCMenu.makeStyle(); oCMenu.construct()		

function cm_checkScrolled(obj){
	if(bw.ns4 || bw.ns6) obj.scrolledY=obj.win.pageYOffset
	else obj.scrolledY=obj.win.document.body.scrollTop
	if(obj.scrolledY!=obj.lastScrolled){
		if(!obj.useframes){
			self.status=obj.scrolledY
			if(obj.scrolledY>119){
				for(i=0;i<obj.l[0].num;i++){var sobj=obj.l[0].o[i].oBorder; sobj.moveY(obj.scrolledY)}
				if(obj.usebar) obj.oBar.moveY(obj.scrolledY)
			}else{
				for(i=0;i<obj.l[0].num;i++){var sobj=obj.l[0].o[i].oBorder; sobj.moveY(obj.fromtop)}
				if(obj.usebar) obj.oBar.moveY(obj.fromtop)
			}

		}
		obj.lastScrolled=obj.scrolledY; page.y=obj.scrolledY; page.y2=page.y2orig+obj.scrolledY
		if(!obj.useframes || bw.ie){ clearTimeout(obj.tim); obj.isover=0; obj.hideSubs(1,0)}
	}
	if((bw.ns4 || bw.ns6) && !obj.useframes) setTimeout("cm_checkScrolled("+obj.name+")",200)
}