// CMXtra Favorites Pod
// Copyright 2003-2004 P.R. Newman, CommunityMX.com

//-------------------------------------------------------------------
// Globals
//-------------------------------------------------------------------

Central.tracer.appName = "cmxtra";	// for App Name Filter in Debug Panel

var gConsole;						// callback for the Console
var gOnline = false;				// whether we currently have a network connection
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

	// create LCDataProvider Client for favorites
	gFavorites = Central.LCDataProvider.createClient(uniqueID, "cmx_faves");
	// populate fave_dg w/ LCDataProvider
	fave_dg.setDataProvider(gFavorites);
	
	// create listener for gFavorites LCDataProvider object
	faveListener = new Object();
	faveListener.modelChanged = function(evtObj){
		var len = gFavorites.getLength();
			
		if(len != 1){
			output_txt.text = len + " favorites";
		}
		else{
			output_txt.text = "1 favorite";
		}
	}
	gFavorites.addListener(faveListener);

	// set tooltips
	getURL_ic.tooltipText = "View Article";
	toss_btn.tooltipText = "Open CMXtra";
	
 	// disable icon buttons
	enableIcons(false);
}

function onNetworkChange(connected)
{
	trace("Favorites pod online: " + (connected ? "true" : "false"));
	gOnline = connected;
}

function onDeactivate()
{
	trace("Favorites pod deactivated");

	// remove global variables
	gConsole = null;
	gOnline = null;
	// remove Favorites listener
	gFavorites.removeListener(faveListener);
	// close LCDataProvider
	gFavorites.close();
}

// --------------------------------------------------
// Custom settings
// --------------------------------------------------

with(fave_dg){
	// hide grid lines and headers
	showGridLines(false);
	showColumnHeaders(false);
	setBaseColor(0x0B7C8C);
	
	// create 2 columns in Favorites DataGrid
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

fave_dg.setChangeHandler("onSelectGrid");
deleteFave_ic.setChangeHandler("onDeleteFave");
getURL_ic.setChangeHandler("onGetURL");

function onSelectGrid(evtObj){
	if(gFavorites.getItemAt(0).Title != "No favorites."){
		enableIcons(true);
	}
}

function onDeleteFave(){
	var index = fave_dg.getSelectedIndex();
	
	gFavorites.removeItemAt(index);
}

function onGetURL(){
	getURL(fave_dg.getSelectedItem().Link);
}

toss_btn.onRelease = function(){	
	// launch main application
	gConsole.loadApplication(); 
}

//-------------------------------------------------------------------
// Utility functions
//-------------------------------------------------------------------

function enableIcons(bln){
	var alpha = 40;
	if(bln) alpha = 100;
	
	getURL_ic.setEnabled(bln);
	getURL_ic._alpha = alpha;
	deleteFave_ic.setEnabled(bln);
	deleteFave_ic._alpha = alpha;
}

//-------------------------------------------------------------------
// Pod Initialization
//-------------------------------------------------------------------

// let Central know we're ready
Central.initPod(this, this);