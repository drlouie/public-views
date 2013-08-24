
/*** 
This is the menu creation code - place it right after you body tag
Feel free to add this to a stand-alone js file and link it to your page.
**/

//Menu object creation
oCMenu=new makeCM("oCMenu") //Making the menu object. Argument: menuname

oCMenu.frames = 0

//Menu properties   
oCMenu.pxBetween=0
oCMenu.fromLeft=11 
oCMenu.fromTop=0   
oCMenu.rows=1
oCMenu.menuPlacement="left"
                                                             
oCMenu.offlineRoot="" 
oCMenu.onlineRoot="" 
oCMenu.resizeCheck=1 
oCMenu.wait=1000 
oCMenu.fillImg="menui/spacer.gif"
oCMenu.zIndex=100

//Background bar properties
oCMenu.useBar=1
oCMenu.barWidth = editorWidth + 1;
oCMenu.barHeight="menu" 
oCMenu.barClass="clBar"
oCMenu.barX='11'
oCMenu.barY=0
oCMenu.barBorderX=0
oCMenu.barBorderY=0
oCMenu.barBorderClass=""

//Level properties - ALL properties have to be spesified in level 0
oCMenu.level[0]=new cm_makeLevel() //Add this for each new level
oCMenu.level[0].width=50
oCMenu.level[0].height=20
oCMenu.level[0].regClass="clLevel0"
oCMenu.level[0].overClass="clLevel0over"
oCMenu.level[0].borderX=0
oCMenu.level[0].borderY=0
oCMenu.level[0].borderClass="clLevel0border"
oCMenu.level[0].offsetX=0
oCMenu.level[0].offsetY=0
oCMenu.level[0].rows=0
oCMenu.level[0].arrow=0
oCMenu.level[0].arrowWidth=0
oCMenu.level[0].arrowHeight=0
oCMenu.level[0].align="bottom"

//EXAMPLE SUB LEVEL[1] PROPERTIES - You have to specify the properties you want different from LEVEL[0] - If you want all items to look the same just remove this
oCMenu.level[1]=new cm_makeLevel() //Add this for each new level (adding one to the number)
oCMenu.level[1].width=150
oCMenu.level[1].height=25
oCMenu.level[1].regClass="clLevel1"
oCMenu.level[1].overClass="clLevel1over"
oCMenu.level[1].borderX=0
oCMenu.level[1].borderY=0
oCMenu.level[1].align="right" 
oCMenu.level[1].offsetX=-(oCMenu.level[0].width-2)/2+20
oCMenu.level[1].offsetY=0
oCMenu.level[1].borderClass="clLevel1border"


//EXAMPLE SUB LEVEL[2] PROPERTIES - You have to spesify the properties you want different from LEVEL[1] OR LEVEL[0] - If you want all items to look the same just remove this
oCMenu.level[2]=new cm_makeLevel() //Add this for each new level (adding one to the number)
oCMenu.level[2].width=150
oCMenu.level[2].height=20
oCMenu.level[2].offsetX=0
oCMenu.level[2].offsetY=0
oCMenu.level[2].regClass="clLevel2"
oCMenu.level[2].overClass="clLevel2over"
oCMenu.level[2].borderClass="clLevel2border"


/******************************************
Menu item creation:
myCoolMenu.makeMenu(name, parent_name, text, link, target, width, height, regImage, overImage, regClass, overClass , align, rows, nolink, onclick, onmouseover, onmouseout) 
*************************************/
oCMenu.makeMenu('top0','','<img src="menui/dd_infobutton.gif" width="13" height="13" border="0">','','','17','','','','','','','','','editor.focusEditor();editor.execCommand("about",null);')

oCMenu.makeMenu('top1','','<center>&nbsp;<u>F</u>ile</center>','/scripts/index.asp','','35','','','')
	oCMenu.makeMenu('sub09','top1','','','','','1','menui/150line.gif','')
	oCMenu.makeMenu('sub10','top1','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_new.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">New','')
	oCMenu.makeMenu('sub11','top1','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_open.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Open','')
	oCMenu.makeMenu('sub12','top1','','','','','8','menui/150break.gif','')
	oCMenu.makeMenu('sub13','top1','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_docstructure.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Document Structure','')
	oCMenu.makeMenu('sub14','top1','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_docstats.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Document Statistics','')
	oCMenu.makeMenu('sub15','top1','','','','','8','menui/150break.gif','')
	oCMenu.makeMenu('sub16','top1','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_styleproperties.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Style Properties','')
	oCMenu.makeMenu('sub17','top1','','','','','1','menui/150line.gif','')

oCMenu.makeMenu('top2','','<center>&nbsp;<u>E</u>dit</center>','http://www.sdf.sdf.sdf/','','36','','','')
	oCMenu.makeMenu('sub20','top2','','','','','1','menui/150line.gif','')
	oCMenu.makeMenu('sub21','top2','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_undo.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Undo','','','','','','','','','','','','document.execCommand("ta", "undo");')
	oCMenu.makeMenu('sub22','top2','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_redo.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Redo','')
	oCMenu.makeMenu('sub23','top2','','','','','8','menui/150break.gif','')
	oCMenu.makeMenu('sub24','top2','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_cut.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Cut','')
	oCMenu.makeMenu('sub25','top2','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_copy.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Copy','')
	oCMenu.makeMenu('sub26','top2','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_paste.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Paste','')
	oCMenu.makeMenu('sub27','top2','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_paste.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Paste With Filter','')
	oCMenu.makeMenu('sub28','top2','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_paste.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Paste as Plain Text','')
	oCMenu.makeMenu('sub29','top2','','','','','8','menui/150break.gif','')
	oCMenu.makeMenu('sub291','top2','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_find.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Find and Replace','')
	oCMenu.makeMenu('sub292','top2','','','','','8','menui/150break.gif','')
	oCMenu.makeMenu('sub293','top2','<img src="menui/spacer.gif" width="5" height="16" border="0">Select All','')
	oCMenu.makeMenu('sub294','top2','','','','','1','menui/150line.gif','')

oCMenu.makeMenu('top3','','<center>&nbsp;<u>I</u>nsert</center>','mailto:test.html')
	oCMenu.makeMenu('sub30','top3','','','','','1','menui/150line.gif','')
	oCMenu.makeMenu('sub31','top3','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_insertimage.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Image','','','','','','','','','','','','document.execCommand("insertimage","editor");','if (editor._doc.selection) { docu}')
	oCMenu.makeMenu('sub32','top3','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_insertlink.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Hyperlink','','','','','','','','','','','','document.execCommand("createlink","editor");','')
	oCMenu.makeMenu('sub33','top3','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_horizontal.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Horizontal Line','','','','','','','','','','','','document.execCommand("inserthorizontalrule","editor");','')
	oCMenu.makeMenu('sub34','top3','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_insertsymbol.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Symbol','')
	oCMenu.makeMenu('sub35','top3','','','','','1','menui/150line.gif','')

oCMenu.makeMenu('top4','','<center>&nbsp;<u>F</u>ormat</center>','mailto:test.html','','55','','','')
	oCMenu.makeMenu('sub40','top4','','','','','1','menui/150line.gif','')
	oCMenu.makeMenu('sub41','top4','<img src="menui/spacer.gif" width="5" height="16" border="0">Font Type','')
		oCMenu.makeMenu('sub410','sub41','<img src="menui/spacer.gif" width="5" height="12" border="0">Arial','')
	oCMenu.makeMenu('sub42','top4','<img src="menui/spacer.gif" width="5" height="16" border="0">Font Size','')
		oCMenu.makeMenu('sub420','sub42','<img src="menui/spacer.gif" width="5" height="12" border="0">Normal','')
	oCMenu.makeMenu('sub43','top4','','','','','8','menui/150break.gif','')
	oCMenu.makeMenu('sub44','top4','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_bold.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Bold','','','','','','','','','','','','editor.insertHTML();')
	oCMenu.makeMenu('sub45','top4','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_underline.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Underline','')
	oCMenu.makeMenu('sub46','top4','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_italic.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Italic','')
	oCMenu.makeMenu('sub47','top4','','','','','8','menui/150break.gif','')
	oCMenu.makeMenu('sub48','top4','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_subscript.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Subscript','')
	oCMenu.makeMenu('sub49','top4','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_superscript.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Superscript','')
	oCMenu.makeMenu('sub491','top4','','','','','8','menui/150break.gif','')
	oCMenu.makeMenu('sub492','top4','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_colors.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Colors','')
	oCMenu.makeMenu('sub493','top4','','','','','1','menui/150line.gif','')


oCMenu.makeMenu('top5','','<center>&nbsp;<u>P</u>aragraph</center>','mailto:test.html','','70','','','')
	oCMenu.makeMenu('sub50','top5','','','','','1','menui/150line.gif','')
	oCMenu.makeMenu('sub51','top5','<img src="menui/spacer.gif" width="5" height="16" border="0">Styles','')
		oCMenu.makeMenu('sub510','sub51','<img src="menui/spacer.gif" width="5" height="12" border="0">Standard','')
		oCMenu.makeMenu('sub511','sub51','<img src="menui/spacer.gif" width="5" height="12" border="0">Heading 1','')
		oCMenu.makeMenu('sub512','sub51','<img src="menui/spacer.gif" width="5" height="12" border="0">Heading 2','')
		oCMenu.makeMenu('sub513','sub51','<img src="menui/spacer.gif" width="5" height="12" border="0">Heading 3','')
		oCMenu.makeMenu('sub514','sub51','<img src="menui/spacer.gif" width="5" height="12" border="0">Heading 4','')
		oCMenu.makeMenu('sub515','sub51','<img src="menui/spacer.gif" width="5" height="12" border="0">Heading 5','')
		oCMenu.makeMenu('sub516','sub51','<img src="menui/spacer.gif" width="5" height="12" border="0">Heading 6','')
	oCMenu.makeMenu('sub52','top5','','','','','8','menui/150break.gif','')
	oCMenu.makeMenu('sub53','top5','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_alignleft.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Align Left','')
	oCMenu.makeMenu('sub54','top5','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_center.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Center','')
	oCMenu.makeMenu('sub55','top5','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_alignright.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Align Right','')
	oCMenu.makeMenu('sub56','top5','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_justify.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Justify','')
	oCMenu.makeMenu('sub57','top5','','','','','8','menui/150break.gif','')
	oCMenu.makeMenu('sub58','top5','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_olist.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Ordered List','')
	oCMenu.makeMenu('sub59','top5','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_unolist.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Unordered List','')
	oCMenu.makeMenu('sub591','top5','','','','','8','menui/150break.gif','')
	oCMenu.makeMenu('sub592','top5','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_iindent.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Increase Indent','')
	oCMenu.makeMenu('sub593','top5','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_dindent.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Decrease Indent','')
	oCMenu.makeMenu('sub594','top5','','','','','1','menui/150line.gif','')

oCMenu.makeMenu('top6','','<center>&nbsp;<u>T</u>ools</center>','mailto:test.html')
	oCMenu.makeMenu('sub60','top6','','','','','1','menui/150line.gif','')
	oCMenu.makeMenu('sub61','top6','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_spellcheck.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Check Spelling','')
	oCMenu.makeMenu('sub62','top6','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_autospellcheck.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Auto Spell Check','')
	oCMenu.makeMenu('sub63','top6','','','','','8','menui/150break.gif','')
	oCMenu.makeMenu('sub64','top6','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_windowmode.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Window Mode','')
	oCMenu.makeMenu('sub65','top6','<img src="menui/spacer.gif" width="5" border="0"><img src="menui/dd_showall.gif" border="0"><img src="menui/spacer.gif" width="8" border="0">Show All','')
	oCMenu.makeMenu('sub66','top6','','','','','1','menui/150line.gif','')

//Leave this line - it constructs the menu
oCMenu.co