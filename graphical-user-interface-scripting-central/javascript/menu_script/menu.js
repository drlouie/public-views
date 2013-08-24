<!-- Always hide for.. ehrm... for what? Hmm. Just always hide...
/*************************************************************
*	'JavaScript Menu' - version 1.0 (august 1998)
*	By Daniel Wentink
*	E-mail: dwentink@hotmail.com
*	Website: 'Cool Design Award' Homepage
*	URL: http://members.xoom.com/cool_design/
*************************************************************/

var infomenu=false;
var sitesmenu=false;
var clicked=false;
var laatste="search";

image = new Array(21);
for (times=0; times<21; times++) {
	image[times]=new Image();
}
image[0].src ="blank.gif";
image[1].src="sel-altavista.gif";
image[2].src="sel-award.gif";
image[3].src="sel-cool design.gif";
image[4].src="sel-informatie.gif";
image[5].src="sel-script.gif";
image[6].src="sel-sites.gif";
image[7].src="sel-website.gif";
image[8].src="sel-yahoo.gif";
image[9].src="sel-search.gif";
image[10].src="unsel-altavista.gif";
image[11].src="unsel-award.gif";
image[12].src="unsel-cool design.gif";
image[13].src="unsel-informatie.gif";
image[14].src="unsel-script.gif";
image[15].src="unsel-sites.gif";
image[16].src="unsel-website.gif";
image[17].src="unsel-yahoo.gif";
image[18].src="unsel-search.gif";
image[19].src="close-button-unsel.gif";
image[20].src="close-button-sel.gif";

function showinfomenu() {
	if (infomenu==true){
		document.images[8].src=image[0].src;
		document.images[9].src=image[0].src;
		document.images[2].src=image[13].src;
	}
	if (infomenu==false){
		document.images[8].src=image[14].src;
		document.images[9].src=image[16].src;
		document.images[2].src=image[4].src;
		document.images[12].src=image[0].src;
		document.images[13].src=image[0].src;
	}
	if (infomenu==false) {
		infomenu=true;
		clicked=true;}
	else {
		infomenu=false;
		clicked=false;}
}

function showsitesmenu() {
	if (sitesmenu==true){
		document.images[10].src=image[0].src;
		document.images[11].src=image[0].src;
		document.images[4].src=image[15].src;
		document.images[12].src=image[0].src;
		document.images[13].src=image[0].src;
	}
	if (sitesmenu==false){
		document.images[10].src=image[18].src;
		document.images[11].src=image[11].src;
		document.images[4].src=image[6].src;
	}
	if (sitesmenu==false) {
		sitesmenu=true;
		clicked=true;}
	else {
		sitesmenu=false;
		clicked=false;}
}

function checkinfomenu() {
	if (infomenu==false && clicked==true) {
		document.images[10].src=image[0].src;
		document.images[11].src=image[0].src;
		document.images[4].src=image[15].src;
		showinfomenu();	
		sitesmenu=false;
	}
}

function checksitesmenu() {
	if (sitesmenu==false && clicked==true) {
		document.images[8].src=image[0].src;
		document.images[9].src=image[0].src;
		document.images[2].src=image[13].src;
		showsitesmenu()
		infomenu=false;
	}
}

function showscript() {if (clicked==true && infomenu==true) document.images[8].src=image[5].src;}
function unshowscript() {if (clicked==true && infomenu==true) document.images[8].src=image[14].src;}
function showwebsite() {if (clicked==true && infomenu==true) document.images[9].src=image[7].src;}
function unshowwebsite() {if (clicked==true && infomenu==true) document.images[9].src=image[16].src;}

function showsearch() {
	if (clicked==true && sitesmenu==true) {
		document.images[10].src=image[9].src;
		document.images[12].src=image[10].src;
		document.images[13].src=image[17].src;
		document.images[11].src=image[11].src;
		laatste="search";
	}
}

function unshowsearch() {
	if (clicked==true && sitesmenu==true) {
		document.images[10].src=image[18].src;
		document.images[12].src=image[0].src;
		document.images[13].src=image[0].src;
	}
}

function showaward() {
	if (clicked==true && sitesmenu==true) {
		document.images[11].src=image[2].src;
		document.images[12].src=image[0].src;
		document.images[13].src=image[12].src;
		document.images[10].src=image[18].src;
		laatste="award";
	}
}
function unshowaward() {
	if (clicked==true && sitesmenu==true) {
		document.images[11].src=image[11].src;
		document.images[12].src=image[0].src;
		document.images[13].src=image[0].src;
	}
}

function showyahooorcooldesign() {
	if (laatste=="award" && sitesmenu==true) {
		document.images[11].src=image[2].src;
		document.images[12].src=image[0].src;
		document.images[13].src=image[3].src;
	}
	if (laatste=="search" && sitesmenu==true) {
		document.images[10].src=image[9].src;
		document.images[11].src=image[11].src;
		document.images[12].src=image[10].src;
		document.images[13].src=image[8].src;
	}		
}

function unshowyahooorcooldesign() {
	if (laatste=="award" && sitesmenu==true) document.images[13].src=image[12].src;
	if (laatste=="search" && sitesmenu==true) document.images[13].src=image[17].src;
}

function showaltavista() {
	if (laatste=="search" && sitesmenu==true) {
		document.images[10].src=image[9].src;
		document.images[11].src=image[11].src;
		document.images[12].src=image[1].src;
		document.images[13].src=image[17].src;
	}
}

function unshowaltavista() {
	if (laatste=="search" && sitesmenu==true) document.images[12].src=image[10].src;
}

function showpressedbutton() {document.images[1].src=image[20].src;}
function unshowpressedbutton() {document.images[1].src=image[19].src;}

function gotoyahooorcooldesign() {
	if (laatste=="search" && sitesmenu==true) {
		newwin=window.open("http://www.yahoo.com/");
	}
	if (laatste=="award" && sitesmenu==true) {
		newwin=window.open("http://members.xoom.com/cool_design/");
	}
}

// end of script-->