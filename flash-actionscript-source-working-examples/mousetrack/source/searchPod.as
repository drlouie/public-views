// CMXtra Search Pod
// Copyright 2003-2004 P.R. Newman, CommunityMX.com

#include "shared/interface.as"
#include "shared/functions.as"

//-------------------------------------------------------------------
// Globals
//-------------------------------------------------------------------

Central.tracer.appName = "cmxtra";	// for App Name Filter in Debug Panel

var gConsole;						// callback for the Console
var gOnline = false;				// whether we currently have a network connection

var gCom;							// LCService object to communicate with agent
var gLastSearch;					// LCDataProvider object
var gFavorites;						// LCDataProvider object

//-------------------------------------------------------------------
// Initialization
//-------------------------------------------------------------------

function onActivate(console, podID, viewerID, position, baseTabIndex, initialData)
{	
	// save references to the console and the ID of this pod
	gConsole = console;
	onNetworkChange(gConsole.isConnected());
	
	var uniqueID = podID + "_" + viewerID;

	// create LCDataProvider for search results (client)
	gLastSearch = Central.LCDataProvider.createClient(uniqueID, "cmx_search");
	// populate search_dg w/ LCDataProvider
	search_dg.setDataProvider(gLastSearch);
	// create LCDataProvider Client for favorites
	gFavorites = Central.LCDataProvider.createClient(uniqueID, "cmx_faves");
	
	// establish local connection to agent
	gCom = Central.LCService.createClient(CMXService, uniqueID, this, true);

	// set tooltips
	addFave_ic.tooltipText = "Add to Favorites";
	getURL_ic.tooltipText = "View Article";
	toss_btn.tooltipText = "Open CMXtra";
	
 	// disable icon buttons
	enableIcons(false);
}

function createClient_Result(clientObj)
{
	// get current query (if one exists) from LCService object
	gCom.getQuery();
}

function createClient_Status(clientObj)
{
   // The agent didn't start in time
   trace("Agent didn't start up in time for getQuery() call in pod");
}

function onNetworkChange(connected)
{
	trace("Search pod online: " + (connected ? "true" : "false"));
	gOnline = connected;
}

function onDeactivate()
{
	trace("Search pod deactivated");

	// remove global variables
	gConsole = null;
	gOnline = null;

	// close LCService network connection
	gCom.close();

	// close LCDataProviders
	gLastSearch.close();
	gFavorites.close();

	// remove Key listener
	Key.removeListener(enterListener);
}

// --------------------------------------------------
// Custom settings
// --------------------------------------------------

with(search_dg){
	// hide grid lines and headers
	showGridLines(false);
	showColumnHeaders(false);
	setBaseColor(0x0B7C8C);
	
	// create 2 columns in Search DataGrid
	var temp = new MGridColumn("Cat");
	temp.setWidth(10);
	temp.setCellSymbol("IconCellRenderer");
	addColumnAt(0, temp);
	
	temp = new MGridColumn("Title");
	temp.setWidth(160);
	temp.setCellSymbol("TitleCellRenderer");
	addColumnAt(1, temp);
}

//-------------------------------------------------------------------
// Event handlers
//-------------------------------------------------------------------

search_dg.setChangeHandler("onSelectGrid");
addFave_ic.setChangeHandler("onAddFave");
getURL_ic.setChangeHandler("onGetURL");

function onSelectGrid(evtObj){
	// clear results
	output_txt.text = "";

	if(gLastSearch.getItemAt(0).Title != "No results found."){
		enableIcons(true);
	}
}

function onAddFave(evtObj){
	var item = search_dg.getSelectedItem();
	var index = gFavorites.getIndexByKey("title", item.Title);
	
	// if not already added...
	if(index == -1){
		// add new favorite to LCDataProvider
		gFavorites.addItemAt(0,{dDate: item.dDate, sDate: item.sDate, title: item.Title, author: item.Author, link: item.Link, cat: item.Cat});
		output_txt.text = "Favorite added";
	}
	else{
		output_txt.text = "Already added";
	}
}

function onGetURL(){
	getURL(search_dg.getSelectedItem().Link);
}

search_btn.onRelease = function(){
	var query = search_txt.getValue();

	if(query != null){
		doSearch(query);
	}
}

toss_btn.onRelease = function(){	
	// launch main application
	gConsole.loadApplication(); 
}

// --------------------------------------------------
// Key listener
// --------------------------------------------------

enterListener = new Object();
enterListener.onKeyDown = function(){
	var query = search_txt.getValue();
	if(Key.getCode() == Key.ENTER && query != null){
		// start search when Enter key is pressed
		doSearch(query);
	}
}
Key.addListener(enterListener);

//-------------------------------------------------------------------
// Utility functions
//-------------------------------------------------------------------

function doSearch(query){
	// reset DataGrids
	gLastSearch.removeAll();
	gLastSearch.addItem({Title: "Searching..."});
	
 	// disable icon buttons
	enableIcons(false);
	// clear results
	output_txt.text = "";
	
	// call searchContent function in agent (server)
	gCom.searchContent(query);
}

function enableIcons(bln){
	var alpha = 40;
	if(bln) alpha = 100;
	
	getURL_ic.setEnabled(bln);
	getURL_ic._alpha = alpha;
	addFave_ic.setEnabled(bln);
	addFave_ic._alpha = alpha;
}

//-------------------------------------------------------------------
// Agent Communication
//-------------------------------------------------------------------

// Handle result from calling searchContent function on agent
function formatSearchResult(q){
	setQuery(q);
 	// disable icon buttons
	enableIcons(false);
}

// Handle result from calling getQuery function on agent
function setQuery(query){
	var len = gLastSearch.getLength();
		
	search_txt.setValue(query);

	if(search_txt.getValue() == null || search_txt.getValue() == ""){
		search_txt.setFocus(true);
	}

	// update text field
	if(len > 0){
		if(gLastSearch.getItemAt(0).Title != "No results found."){
			output_txt.text = len + " results";
		}
		else{
			output_txt.text = "No results found";
		}
	}	
}

//-------------------------------------------------------------------
// Pod Initialization
//-------------------------------------------------------------------

// let Central know we're ready
Central.initPod(this, this);