/* Scripting & Interfacing by DRL [DrLouie] (aka: LouieRd / dba: NMS [NetMedia Solutions]) - FOR business use by: SOE (Sony Online Entertainment) - OR portfolio use by: DRL !!! NO EXCEPTIONS !!! - REPURPOSING, RECONSTRUCTING, REDEPLOYMENT IS STRICLY PROHIBITED! */
var s=10;var mih='';var mit='';var iid='5376';var sac='135';tx=new Image();tx.src="images/theX.gif";tp=new Image();tp.src="images/thePlus.gif";tt1=new Image();tt1.src="images/tableTopper.gif";itb1=new Image();itb1.src="images/innerTableBottomer.gif";tb1=new Image();tb1.src="images/tableBottomer.gif";tbm1=new Image();tbm1.src="images/tableBackgroundMarble.jpg";var d=document;var mhsf="";var mdl1="";var lay1="";var startY="";function parseHTML(title,content){mit=title;mih=content;stw();}function lp(){var dm=d.leDetails;dm.Rewind();dm.SetVariable("_root.dataBox.htmlText",mih);dm.Play();}function loadHTML(){lp();}function ktw(){d.getElementById("detailsLayer").style.height=20+'px';}function stw(){d.getElementById("sizeFinder").innerHTML=mih;mhsf=d.getElementById("sizeFinder").offsetHeight+10;d.getElementById("titleBar").innerHTML=mit;lt();}function lt(){mdl1=d.getElementById("detailsLayer");lay1=d.getElementById("detailsLayer").style;startY=mdl1.offsetHeight;toggledetailsTab1();}function toggledetailsTab1(){if(mdl1.offsetHeight<=startY||mdl1.offsetHeight<=sac){td1d();}else if(mdl1.offsetHeight>=mhsf){td1u();}else{var dn=1;}}function td1d(){nyp=mdl1.offsetHeight+s;mdl1.style.height=nyp+'px';if(mdl1.offsetHeight<=mhsf){setTimeout("td1d()",1);}else{d.images.controlButton.src=tx.src;}}function td1u(){nyp=mdl1.offsetHeight-s;mdl1.style.height=nyp+'px';if(mdl1.offsetHeight>sac){setTimeout("td1u()",1);}else{d.images.controlButton.src=tp.src;}}