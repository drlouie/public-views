/*
   Deluxe Menu Data File
   Created by Deluxe Tuner v3.2
   http://deluxe-menu.com
*/


// -- Deluxe Tuner Style Names
var itemStylesNames=["Top Item",];
var menuStylesNames=["Top Menu",];
// -- End of Deluxe Tuner Style Names

//--- Common
var isHorizontal=1;
var smColumns=1;
var smOrientation=1;
var dmRTL=0;
var itemCursor="default";
var itemTarget="_self";
var pressedItem=-2;
var statusString="link";
var blankImage="deluxe-menu.files/blank.gif";
var pathPrefix_img="";
var pathPrefix_link="";

//--- Dimensions
var menuWidth="";
var menuHeight="23px";
var smWidth="";
var smHeight="";

//--- Positioning
var absolutePos=0;
var posX="20px";
var posY="20px";
var topDX=0;
var topDY=1;
var DX=-5;
var DY=0;
var subMenuAlign="pleft";
var subMenuVAlign="top";

//--- Font
var fontStyle=["normal 10px Tahoma","normal 10px Tahoma"];
var fontColor=["#E4EDEF","#FFF4D5"];
var fontDecoration=["none","none"];
var fontColorDisabled="#6F9DAC";

//--- Appearance
var menuBackColor="#4E7785";
var menuBackImage="";
var menuBackRepeat="repeat";
var menuBorderColor="#558391";
var menuBorderWidth=1;
var menuBorderStyle="ridge";

//--- Item Appearance
var itemBackColor=["#4E7785","#588898"];
var itemBackImage=["",""];
var beforeItemImage=["",""];
var afterItemImage=["",""];
var beforeItemImageW="";
var afterItemImageW="";
var beforeItemImageH="";
var afterItemImageH="";
var itemBorderWidth=1;
var itemBorderColor=["#6093A4","#4E7785"];
var itemBorderStyle=["ridge","groove"];
var itemSpacing=2;
var itemPadding="3px";
var itemAlignTop="center";
var itemAlign="left";

//--- Icons
var iconTopWidth=16;
var iconTopHeight=16;
var iconWidth=16;
var iconHeight=16;
var arrowWidth=7;
var arrowHeight=7;
var arrowImageMain=["deluxe-menu.files/arrv_white.gif",""];
var arrowWidthSub=0;
var arrowHeightSub=0;
var arrowImageSub=["deluxe-menu.files/arr_white.gif",""];

//--- Separators
var separatorImage="";
var separatorWidth="100%";
var separatorHeight="3px";
var separatorAlignment="left";
var separatorVImage="";
var separatorVWidth="3px";
var separatorVHeight="100%";
var separatorPadding="0px";

//--- Floatable Menu
var floatable=0;
var floatIterations=6;
var floatableX=1;
var floatableY=1;
var floatableDX=15;
var floatableDY=15;

//--- Movable Menu
var movable=0;
var moveWidth=12;
var moveHeight=20;
var moveColor="#DECA9A";
var moveImage="";
var moveCursor="move";
var smMovable=0;
var closeBtnW=15;
var closeBtnH=15;
var closeBtn="";

//--- Transitional Effects & Filters
var transparency="100";
var transition=24;
var transOptions="gradientSize=0.4, wipestyle=1, motion=forward";
var transDuration=350;
var transDuration2=200;
var shadowLen=3;
var shadowColor="#B1B1B1";
var shadowTop=0;

//--- CSS Support (CSS-based Menu)
var cssStyle=0;
var cssSubmenu="";
var cssItem=["",""];
var cssItemText=["",""];

//--- Advanced
var dmObjectsCheck=0;
var saveNavigationPath=1;
var showByClick=0;
var noWrap=1;
var smShowPause=200;
var smHidePause=1000;
var smSmartScroll=1;
var topSmartScroll=0;
var smHideOnClick=1;
var dm_writeAll=1;
var useIFRAME=0;
var dmSearch=0;

//--- AJAX-like Technology
var dmAJAX=0;
var dmAJAXCount=0;
var ajaxReload=0;

//--- Dynamic Menu
var dynamic=0;

//--- Keystrokes Support
var keystrokes=0;
var dm_focus=1;
var dm_actKey=113;

//--- Sound
var onOverSnd="";
var onClickSnd="";

var itemStyles = [
    ["itemWidth=94px","itemHeight=21px","itemBackColor=transparent,transparent","itemBackImage=deluxe-menu.files/btn_cyan.gif,deluxe-menu.files/btn_cyan2.gif","itemBorderWidth=0","fontStyle='bold 10px Tahoma','bold 10px Tahoma'","fontColor=#FFFFFF,#FFFFFF"],
];
var menuStyles = [
    ["menuBackColor=transparent","menuBorderWidth=0","itemSpacing=0","itemPadding=5px 6px 5px 6px","smOrientation=undefined"],
];

var menuItems = [

    ["Home","testlink.html", "", "", "", "", "0", "0", "", "", "", ],
    ["Product Info","", "", "", "", "", "0", "", "", "", "", ],
        ["|Features","testlink.html", "", "", "", "", "", "", "", "", "", ],
        ["|Installation","", "", "", "", "", "", "", "", "", "", ],
            ["||Description of Files","testlink.html", "", "", "", "", "", "", "", "", "", ],
            ["||How To Setup","testlink.html", "", "", "", "", "", "", "", "", "", ],
        ["|Parameters Info","testlink.html", "", "", "", "", "", "", "", "", "", ],
        ["|Dynamic Functions","testlink.html", "", "", "", "", "", "", "", "", "", ],
        ["|Supported Browsers","", "", "", "", "", "", "", "", "", "", ],
            ["||Windows OS","", "", "", "", "", "", "", "", "", "", ],
            ["||Internet Explorer","", "", "", "", "", "", "", "", "", "", ],
            ["||Firefox","", "", "", "", "", "", "", "", "", "", ],
            ["||Mozilla","", "", "", "", "", "", "", "", "", "", ],
            ["||Netscape","", "", "", "", "", "", "", "", "", "", ],
            ["||Opera","", "", "", "", "", "", "", "", "", "", ],
            ["||MAC OS","", "", "", "", "", "", "", "", "", "", ],
            ["||Firefox","", "", "", "", "", "", "", "", "", "", ],
            ["||Safari","", "", "", "", "", "", "", "", "", "", ],
            ["||Internet Explorer","", "", "", "", "", "", "", "", "", "", ],
            ["||Unix/Linux OS","", "", "", "", "", "", "", "", "", "", ],
            ["||Firefox","", "", "", "", "", "", "", "", "", "", ],
            ["||Konqueror","", "", "", "", "", "", "", "", "", "", ],
    ["Samples","", "", "", "", "", "0", "", "", "", "", ],
        ["|Sample 1","testlink.html", "", "", "", "", "", "", "", "", "", ],
        ["|Sample 2 is Disabled","testlink.html", "", "", "", "_", "", "", "", "", "", ],
        ["|Sample 3","testlink.html", "", "", "", "", "", "", "", "", "", ],
        ["|Sample 4","testlink.html", "", "", "", "", "", "", "", "", "", ],
        ["|Sample 5","testlink.html", "", "", "", "", "", "", "", "", "", ],
        ["|Sample 6","testlink.html", "", "", "", "", "", "", "", "", "", ],
        ["|Sample 7","testlink.html", "", "", "", "", "", "", "", "", "", ],
        ["|Sample 8","testlink.html", "", "", "", "", "", "", "", "", "", ],
        ["|Sample 9","testlink.html", "", "", "", "", "", "", "", "", "", ],
    ["Purchase","http://deluxe-menu.com/order-purchase.html", "", "", "", "_blank", "0", "", "", "", "", ],
    ["Contact Us","testlink.htm", "", "", "", "", "0", "", "", "", "", ],
];

dm_init();