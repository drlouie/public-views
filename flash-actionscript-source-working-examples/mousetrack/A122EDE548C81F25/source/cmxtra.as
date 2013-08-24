// CMXtra application for Central
// Copyright 2003-2004 P.R. Newman, CommunityMX.com

#include "NetServices.as"
//#include "NetDebug.as"
#include "shared/interface.as"
#include "shared/functions.as"
#include "init.as"

// --------------------------------------------------
// Custom settings
// --------------------------------------------------

function initGrids(){
	// customize MDataGrid component on Search tab
	with(search_mc.search_dg){
		setBaseColor(0x0B7C8C);
		// create 4 columns in Search DataGrid
		setColumns("Cat", "sDate", "Title", "Author");
		
		var temp;
		temp = getColumnAt(0);
		temp.setWidth(25);
		temp.setCellSymbol("IconCellRenderer");
		temp.setHeaderSymbol("header");

		temp = getColumnAt(1);
		temp.setWidth(80);
		temp.setHeader("Date");
		temp.setSortable(false);
		
		temp = getColumnAt(3);
		temp.setWidth(105);
	}
	
	// customize MDataGrid component on Favorites tab
	with(fave_mc.fave_dg){
		setBaseColor(0x0B7C8C);
		// create 4 columns in Favorites DataGrid
		setColumns("Cat", "sDate", "Title", "Author");
		
		var temp;
		temp = getColumnAt(0);
		temp.setWidth(25);
		temp.setCellSymbol("IconCellRenderer");
		temp.setHeaderSymbol("header");

		temp = getColumnAt(1);
		temp.setWidth(80);
		temp.setHeader("Date");
		temp.setSortable(false);

		temp = getColumnAt(3);
		temp.setWidth(105);
	}
}

function initTabs(){
	myAcc.addItem("Articles", articles_mc);
	myAcc.addItem("Search", search_mc);
	myAcc.addItem("Favorites", fave_mc);

	gSelectedTab = articles_mc;
	// hide other tabs
	search_mc._visible = fave_mc._visible = false;
	
	myAcc.setChangeHandler("onTabSelect");
}

// set date range in MCalendar component
var range = new Object();
range.begin = new Date(2003, 2, 31);	// March 31, 2003
range.end = new Date(); 				// today
articles_mc.myCal.setDisplayRange(range);

// disable Saturdays and Sundays in MCalendar component
var dateFilter = new Object();
dateFilter.isSelectable = function(comp, dt){
	return !(dt.getDay() == 0 || dt.getDay() == 6);
}
articles_mc.myCal.setDateFilter(dateFilter);

// --------------------------------------------------
// Key listener for Articles and Search tabs
// --------------------------------------------------

var enterListener = new Object();
enterListener.onKeyUp = function(){
	var q1 = articles_mc.searchbox_mc.search_txt.getValue();
	var q2 = search_mc.find_mc.keywords_txt.getValue();
	var index = myAcc.getSelectedIndex();
	
	if(Key.getCode() == Key.ENTER && index == 0 && q1 != ""){
		// start search when Enter key is pressed
		doSearch(q1);
	}
	else if(Key.getCode() == Key.ENTER && index == 1 && q2 != ""){
		// start search when Enter key is pressed
		doSearch(q2);
	}
}
Key.addListener(enterListener);

// --------------------------------------------------
// Listener for AccordianTab component
// --------------------------------------------------

// AccordianTab listener
myAcc.addListener(this);

// triggered when the change begins
this.onAnimationStart = function(tab){
	toss_ic._visible = false;
}
// triggered when the change is complete
this.onAnimationDone = function(tab){
	var index = tab.getSelectedIndex();

	switch(index){
		case 0: toss_ic._x = 330; break;
		case 1: toss_ic._x = 400; break;
		case 2: toss_ic._x = 490; break;
	}
	toss_ic._visible = true;
}

// --------------------------------------------------
// Button handlers
// --------------------------------------------------

// Handler for "Search" MPushButton component on Articles tab
articles_mc.searchbox_mc.search_btn.onRelease = function(evtObj){
	var q = articles_mc.searchbox_mc.search_txt.getValue();
	doSearch(q);
}

// Handler for "Search" MPushButton component on Search tab
search_mc.find_mc.searchform_btn.onRelease = function(evtObj){
	var q = search_mc.find_mc.keywords_txt.getValue();
	doSearch(q);
}

// Handler for Previous arrow
articles_mc.datenav_mc.prev_btn.onRelease = function(evtObj){
	
	// get selected date from MCalendar component
	var chosen_date = articles_mc.myCal.getSelectedItem();
	var today = new Date();

	if(chosen_date == undefined || chosen_date == "undefined"){
		chosen_date = today;
	}
	
	if(chosen_date.getDay() == 1){
		// it's Monday - go to Friday
		chosen_date.setDate(chosen_date.getDate()-3);
	}
	else{
		// go to yesterday
		chosen_date.setDate(chosen_date.getDate()-1);
	}
		
	// synch MCalendar component (and make FR call)
	articles_mc.myCal.setSelectedItem(chosen_date);
	articles_mc.myCal.setDisplayedMonth(chosen_date);

	updateStatus("Loading articles...", true);
}

// Handler for Next arrow
articles_mc.datenav_mc.next_btn.onRelease = function(evtObj){
	
	// get selected date from MCalendar component
	var chosen_date = articles_mc.myCal.getSelectedItem();
	var today = new Date();
	
	if(chosen_date == undefined || chosen_date == "undefined"){
		chosen_date = today;
	}
	
	if(chosen_date.getDay() == 5){
		// it's Friday - go to Monday
		chosen_date.setDate(chosen_date.getDate()+3);
	}
	else{
		// go to tomorrow
		chosen_date.setDate(chosen_date.getDate()+1);
	}

	// synch MCalendar component (and make FR call)
	articles_mc.myCal.setSelectedItem(chosen_date);
	articles_mc.myCal.setDisplayedMonth(chosen_date);

	updateStatus("Loading articles...", true);
}

// Handler for Show Pod icon
toss_ic.onRelease = function(){

	var podList = gShell.getPods();

	// returns array of open pods for this app
	// regardless of whether the console is open
	var activePods = gShell.getViewedPods();
	
	if(activePods[0] == null){
		gShell.viewPod(podList[0].id);		
	}
}

// --------------------------------------------------
// Event handlers
// --------------------------------------------------

// change handler for MAccordianTab component
function onTabSelect(tab){
	var tabClip = tab.getSelectedItem().data;
	var tabLabel = tab.getSelectedItem().label;

  	gSelectedTab._visible = false;
    tabClip._visible = true;
	// set global reference to selected tab
    gSelectedTab = tabClip;

	switch(tabLabel){
		case "Articles":
			updateStatus("Community MX", false);
			break;
		case "Search":
			// set focus to search text box if empty
			if(search_mc.find_mc.keywords_txt.getValue() == null){
				search_mc.find_mc.keywords_txt.setFocus(true);
			}
			updateStatus(gSearchStatus, gSearching);
			break;
		case "Favorites":
			updateStatus(gFaveStatus, false);
			break;
	}
}

// change handler for MDataGrid components
function onGridSelect(grid){
	var itm = grid.getSelectedItem();

	if(grid._name == "search_dg"){
		// if search returns results
		if(itm.Title != "No results found."){
			enableIcons(true, "Search");
		}
	}
	else if(grid._name == "fave_dg"){
			enableIcons(true, "Favorites");
	}
}

// change handler for View Article icons
function onGetURL(evtObj){
	if(evtObj._name == "getURL_ic"){
		// Search tab
		var itm = search_mc.search_dg.getSelectedItem();
		if(itm.Link != ""){
			getURL(itm.Link);
		}
	}
	else if(evtObj._name == "fgetURL_ic"){
		// Favorites tab
		var itm = fave_mc.fave_dg.getSelectedItem();
		if(itm.Link != ""){
			getURL(itm.Link);
		}	
	}
}

// Articles tab

// this function makes Flash Remoting call
function onCalendarChange(evtObj){
	var selItem = evtObj.getSelectedItem();
	// call getContentByDate method in CFC
	searchService.getContentByDate(contentByDateRes, formatDate(selItem,1));
	// add message to status bar
	updateStatus("Loading articles...", true);
}

function viewArticle(evtObj){
	var obj = evtObj._name; // e.g., gif_0
	var index = obj.substr(obj.length-1, 1); // returns 0
	var article = gArticles_rs.getItemAt(index);
	getURL("http://www.communitymx.com/category.cfm?catid=" + article.CatID, "_blank");
}

function addFave(evtObj){
	var obj = evtObj._name; // e.g., icon_0
	var index = obj.substr(obj.length-1, 1); // returns 0
	var article = gArticles_rs.getItemAt(index);
	// add favorite to gFavorites LCDataProvider object
	addFavorite({dDate: article.PubDate, sDate: formatDate(article.PubDate, 1), title: article.Title, author: article.AuthorName, link: "http://www.communitymx.com/abstract.cfm?cid=" + article.CID, cat: article.Category});
}

// Search tab

function onAddFave(evtObj){
	var itm = search_mc.search_dg.getSelectedItem();
	// call addFavorite function
	addFavorite(itm);
}

// Favorites tab

function onDelFave(evtObj){
	var itm = fave_mc.fave_dg.getSelectedItem();
	// call removeFavorite function
	removeFavorite(itm.Title);
}

//-------------------------------------------------------------------
// Agent Communication
//-------------------------------------------------------------------

// Handle result from calling searchContent function on agent
function formatSearchResult(q){
	setQuery(q);
	// disable icon buttons until a row is selected
	enableIcons(false, "Search");
	
	// change searching flag to false
	gSearching = false;
	// close dialog box
	closeDialog();
	// select Search tab
	myAcc.setSelectedIndex(1);
}

// Handle result from calling getQuery function on agent
function setQuery(query){
	var len = gLastSearch.getLength();
	
	articles_mc.searchbox_mc.search_txt.setValue(query); 
	search_mc.find_mc.keywords_txt.setValue(query);
		
	if(len > 0){
		if(gLastSearch.getItemAt(0).Title != "No results found."){
			gSearchStatus = "Found " + len + " matches for \"" + query + "\"";
		}
		else{
			gSearchStatus = "No results found.";
		}			
	}
}

function doSearch(q){
	// open dialog box
	showDialog("Searching for <b>" + q + "</b>...", "Searching Community MX", false);
	
	// this slows things down so it's out:
	// clear LCDataProvider (and grids)
	//gLastSearch.removeAll();
	//gLastSearch.addItem({Title: "Searching..."});
		
	// set Search status bar variable
	gSearchStatus = "Searching for \"" + q + "\"...";
	updateStatus(gSearchStatus, true);
	// flag that we're searching
	gSearching = true;
	// call searchContent function in agent (server)
	gCom.searchContent(q);
}

// --------------------------------------------------
// Utility functions
// --------------------------------------------------

function populateScollpane(rs){
	// populate global gArticles_rs RecordSet object
	gArticles_rs = rs;
	var len = rs.getLength();
	var contentDate = rs.getItemAt(0).PubDate;
	var link_str;

	// look for line breaks
	var re1 = new RegExp("\\r\\n");
	var re2 = new RegExp("<br>", "i");
	// format links
	var re3 = new RegExp("<a ", "i");
	var re4 = new RegExp("</a>", "i");

	with(articles_mc){
		// format today's date
		datenav_mc.date_txt.text = formatDate(contentDate,0);
		// clear scrollpane content by reloading container mc
		sp.setScrollContent("container");
		// move scrollbar to top
		sp.setScrollPosition(0, 0);
		// get reference to container movie clip
		var ref = sp.getScrollContent();
	
		for(var i=0; i<len; i++){
			var article = rs.getItemAt(i);
			var abstract_str = article.Abstract;			
			// apply regular expressions to abstract
			abstract_str = re1.replace(abstract_str, "\r");
			abstract_str = re2.replace(abstract_str, "");
			abstract_str = re3.replace(abstract_str, "<font color=\"#006699\"><a ");
			abstract_str = re4.replace(abstract_str, "</a></font>");
			
			if(i>0){
				// if more than 1 article, duplicate cont movie clip
				ref.cont0.duplicateMovieClip("cont"+i, i);
			}
			// create a reference to cont movie clip
			var cont = ref["cont"+i];
			cont._y = (ref["cont"+(i-1)]._y + ref["cont"+(i-1)]._height);
			
			// attach img movie clip (gif_0, gif_1)
			// to attach more than 1 movie to cont, 
			// you have to specify different depths
			var temp = cont.attachMovie("img", "gif_"+i, 100+i);
			temp._y = temp._x = 10;
			// add category icon to local cache:
			var gifUrl = "http://www.communitymx.com/images/large" + article.prefix + "icon.gif";
			if(!gShell.inLocalInternetCache(gifUrl)){
			   gShell.addToLocalInternetCache(gifUrl);
			}
			// inside the img movie clip is loader_mc
			// otherwise, tooltipText doesn't work
			temp.loader_mc.loadMovie(gifUrl);
 			temp.toolTipText = article.Category;
			temp.onRelease = function(){
				// call viewArticle function
				_parent.viewArticle(this);
			}
			
			// attach Add to Favorites icon
			var temp2 = cont.attachMovie("MIconButtonSymbol", "icon_"+i, i);
			temp2.setIcon("icon_bookmark_add");
			temp2.toolTipText = "Add to Favorites";
			temp2._y = cont.byline_txt._y;
			temp2._x = 10;
			temp2.setChangeHandler("addFave", this);

			if(article.PID.indexOf(",") == -1){
				// if only one author
				link_str = "by <font color=\"#006699\"><a href=\"http://www.communitymx.com/author.cfm?cid=" + article.PID + "\" target=\"blank\" id=\"" + article.PID + "\">" + article.AuthorName + "</a></font><br><br>";
			}
			else{
				// two or more authors - call makeByline function
				link_str = makeByline(article.AuthorName, article.PID);
			}
	
			// format text fields
			cont.headline_txt.autoSize = true;
			cont.byline_txt.autoSize = true;
			cont.content_txt.autoSize = true;
			cont.headline_txt.htmlText = "<p><b><font color=\"#003366\"><a href=\"http://www.communitymx.com/abstract.cfm?cid=" + article.CID + "\" target=\"blank\">" + article.Title + "</a></font></b></p>";
			cont.byline_txt.htmlText = link_str;
			cont.content_txt.htmlText = "<p>" + abstract_str + "</p>";		
		}
	// refresh ScrollPane component after changing its size
	sp.refreshPane();
	}
}

// Make a clickable link out of some text, given the text and a location 
function makeByline(theText, theLink) {
  var temp = "by ";
  // define array of author names
  var authors_array = theText.split(",");
  // define array of Partner IDs
  var pids_array = theLink.split(",");
  var len = pids_array.length;
  
  for (var i=0; i<len; i++){
	  temp += "<font color=\"#006699\"><a href=\"http://www.communitymx.com/author.cfm?cid=";
	  temp += pids_array[i];
	  temp += "\" target=\"_blank\">" + authors_array[i] + "</a></font> & ";
  }
  // strip trailing ampersand
  temp = temp.substring(0, temp.length-2);
  temp += "<br><br>";
  return temp;
}

// create data provider for DialogBox component
var db_dp = new Central.dataProviderClass();
// set linkage ID of dialog movie clip
db_dp.addItem({data: "dialogmc"});

function showDialog(msg, title, closable){
	// make room for close_pb
	var dbH = (closable) ? 200 : 180;
	var tween = (closable) ? 5 : 0;
	
	// remove dialog box, just in case
	db_mc.removeMovieClip();
	this.attachMovie("MDialogBoxSymbol", "db_mc", 50);
	db_mc.setDataProvider(db_dp);
	// the setSize method will prevent the 
	// dialog box from automatically resizing
	// to fit its content movie clip
	db_mc.setSize(250, dbH, tween);
	db_mc.showClose(closable);
	db_mc.setIsModal(true);
	db_mc.setTitle(title);
	db_mc._x = 150;
	db_mc._y = 150;
	db_mc.onClosed = function(){
		closeDialog();
	}
	var ref = db_mc.getSelectedContent();
	// add msg to MDialogBox component
	ref.alert_txt.htmlText = (closable) ? msg : "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + msg;
	//ref.alert_txt.autoSize = true;
	ref.ants._visible = !closable;
	ref.close_pb._visible = closable;
	ref.close_pb.onRelease = function(){
		closeDialog();
	}
}

function closeDialog(){
	db_mc.setIsModal(false);
	db_mc.removeMovieClip();
}

function enableIcons(bln, tab){
	var alpha = 40;
	if(bln) alpha = 100;
	
	switch(tab){
		case "Search":
			search_mc.getURL_ic.setEnabled(bln);
			search_mc.getURL_ic._alpha = alpha;
			search_mc.addFave_ic.setEnabled(bln);
			search_mc.addFave_ic._alpha = alpha;
			break;
		case "Favorites":
			fave_mc.fgetURL_ic.setEnabled(bln);
			fave_mc.fgetURL_ic._alpha = alpha;
			fave_mc.delFave_ic.setEnabled(bln);
			fave_mc.delFave_ic._alpha = alpha;
			break;
		default:
			// change all icons
			search_mc.getURL_ic.setEnabled(bln);
			search_mc.getURL_ic._alpha = alpha;
			search_mc.addFave_ic.setEnabled(bln);
			search_mc.addFave_ic._alpha = alpha;
			fave_mc.fgetURL_ic.setEnabled(bln);
			fave_mc.fgetURL_ic._alpha = alpha;
			fave_mc.delFave_ic.setEnabled(bln);
			fave_mc.delFave_ic._alpha = alpha;
	}
}

function updateStatus(msg, loading){
	if(loading){
		// show barber pole
		gShell.setProgress(-1);
	}
	else{
		// hide barber pole
		gShell.setProgress(0);
	}
	gShell.setStatus(msg);
}

// --------------------------------------------------
// Functions for modifying LCDataProvider (gFavorites)
// --------------------------------------------------

function addFavorite(item){
	var index = gFavorites.getIndexByKey("title", item.title);
	
	// if not already added...
	if (index == -1){
		// add new Favorite to LCDataProvider object
		gFavorites.addItemAt(0,{dDate: item.dDate, sDate: item.sDate, title: item.Title, author: item.Author, link: item.Link, cat: item.Cat});
		// show Favorites tab
		myAcc.setSelectedIndex(2);
		// select new favorite in grid 
		fave_mc.fave_dg.setSelectedIndex(0);
	}
	else{
		showDialog("You have already added this to your favorites.", "Community MX", true);
	}
}

function removeFavorite(title){
	var index = gFavorites.getIndexByKey("title", title);
	
	gFavorites.removeItemAt(index);
	
	// disable icon buttons
	enableIcons(false, "Favorites");
}

// --------------------------------------------------
// Flash Remoting responder object
// --------------------------------------------------

// create responder object
var contentByDateRes = new Object();
// returns a RecordSet object from CFC to Flash
contentByDateRes.onResult = function(rs){
	
	updateStatus("Community MX", false);
		
	var now_date = new Date();
	var start_date = new Date(2003, 2, 31);
	var totalRecords = rs.getLength();
	var contentDate = rs.getItemAt(0).PubDate;
	
	var isSaturday = now_date.getDay() == 6;
	var isSunday = now_date.getDay() == 0

	var yesterday_date = new Date();
	yesterday_date.setDate(yesterday_date.getDate()-1);

	var twodaysago_date = new Date();
	twodaysago_date.setDate(twodaysago_date.getDate()-2);

	// to compare dates for equality, you have to convert them to strings
	var lastSaturday = isSaturday && formatDate(contentDate,1) == formatDate(yesterday_date,1);
	var lastSunday = isSunday && formatDate(contentDate,1) == formatDate(twodaysago_date,1);
	
	if(formatDate(contentDate,1) == formatDate(now_date,1)){
		// if it's today, hide next btn
		articles_mc.datenav_mc.next_btn._visible = false;
	}
	else if(lastSaturday || lastSunday){
		// hide next button if it's last Saturday or Sunday before new week
		articles_mc.datenav_mc.next_btn._visible = false;
	}
	else{
		articles_mc.datenav_mc.next_btn._visible = true;
	}
	
	if(formatDate(contentDate,1) == formatDate(start_date,1)){
		// if it's March 31, hide prev_btn
		articles_mc.datenav_mc.prev_btn._visible = false;
	}
	else{
		articles_mc.datenav_mc.prev_btn._visible = true;
	}
			
	if(totalRecords > 0){		
		populateScollpane(rs);
	}
	else{
		// this shouldn't happen:
		showDialog("No articles found.", "Community MX", true);
	}
}

// this is only returned if there's an error
contentByDateRes.onStatus = function(status){
	showDialog("Unable to connect. Please try again later.", "Connection Error", true);
	updateStatus("Connection Error", false);	
}

System.onStatus = contentByDateRes.onStatus;

// --------------------------------------------------
// Flash Remoting initialization
// --------------------------------------------------

if (inited == null){

	// do this code only once
	var inited = true;
		
	// set the gateway URL variable
	var gatewayUrl = "http://www.communitymx.com/flashservices/gateway";
	
   	// set the default gateway URL
	NetServices.setDefaultGatewayUrl(gatewayUrl);
	
	// create the gateway connection
	var gateway_conn = NetServices.createGatewayConnection();

	// get a reference to the proxy service
	var searchService = gateway_conn.getService("com.communitymx.centralSearch");

	var today_date = new Date();

	if(today_date.getDay() == 6){
		// it's Saturday - go back 1 day
		today_date.setDate(today_date.getDate()-1);
	}
	else if(today_date.getDay() == 0){
		// it's Sunday - go back 2 days
		today_date.setDate(today_date.getDate()-2);
	}

	// synch MCalendar component (doesn't make FR call, for some reason)
	articles_mc.myCal.setSelectedItem(today_date);

	// call Flash Remoting service
	searchService.getContentByDate(contentByDateRes, formatDate(today_date,1));
}
