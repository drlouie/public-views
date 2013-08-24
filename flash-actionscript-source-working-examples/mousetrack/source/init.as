// CMXtra app initialization
// Copyright 2003-2004 P.R. Newman, CommunityMX.com

//-------------------------------------------------------------------
// Globals
//-------------------------------------------------------------------

Central.tracer.appName = "cmxtra";	// for App Name Filter in Debug Panel

var gShell;
var gOnline = false;				// whether we currently have a network connection
var gFaveStatus;					// global variable for Favorites status bar
var gSearchStatus = "Community MX";	// global variable for Search status bar
var gSearching = false;				// Boolean indicating if user is searching
var gSelectedTab;					// Boolean indicating if user is searching
var gArticles_rs;					// global RecordSet object for Articles tab

var gCom; 							// LCService object to communicate with agent
var gLastSearch;					// LCDataProvider object
var gFavorites;						// LCDataProvider object

//-------------------------------------------------------------------
// Initialization
//-------------------------------------------------------------------

// Called by Central once your application has loaded
function onActivate(shell, appID, shellID, baseTabIndex, initialData)
{
	// keep a reference to Central shell
	gShell = shell;
	onNetworkChange(gShell.isConnected());
			
	var uniqueID = appID + "_" + shellID;

	// establish local connection to agent
	gCom = Central.LCService.createClient(CMXService, uniqueID, this, true);

 	// disable icon buttons
	enableIcons(false, "all");
	// format DataGrids before setting data providers
	initGrids();
	// populate MAccordianTab component
    initTabs();
	
	// create LCDataProvider for search results (client)
	gLastSearch = Central.LCDataProvider.createClient(uniqueID, "cmx_search");
	search_mc.search_dg.setDataProvider(gLastSearch);
	// create LCDataProvider Client for favorites
	gFavorites = Central.LCDataProvider.createClient(uniqueID, "cmx_faves");
	// populate fave_dg w/ LCDataProvider
	fave_mc.fave_dg.setDataProvider(gFavorites);
		
	// create listener for gFavorites LCDataProvider object
	faveListener = new Object();
	faveListener.modelChanged = function(evtObj){ 
		var len = gFavorites.getLength();
		
		// set global gFaveStatus variable
		if(len == 1){
			gFaveStatus = "You have 1 favorite";
		}
		else{
			gFaveStatus = "You have " + len + " favorites";
		}
		// if Favorites tab is selected
		if(myAcc.getSelectedIndex() == 2){
			// update Favorites status bar
			updateStatus(gFaveStatus);
		}
	}
	gFavorites.addListener(faveListener);

	// hide Next and Previous arrows
	articles_mc.datenav_mc.prev_btn._visible = articles_mc.datenav_mc.next_btn._visible = false;
		
	// set tooltips
	search_mc.getURL_ic.tooltipText = fave_mc.fgetURL_ic.tooltipText = "View Article";
	search_mc.addFave_ic.tooltipText = "Add to Favorites";
	
	// show barber pole
	updateStatus("Loading articles...", true);
}

function createClient_Result(clientObj)
{
	// get current query (if one exists) from LCService object
	gCom.getQuery();
}

function createClient_Status(sclientObj)
{
   // The agent didn't start in time
   trace("Agent didn't start up in time for getQuery() call in app");
}

function onNetworkChange(connected)
{
	trace("app online: " + (connected ? "true" : "false"));
	
	gOnline = connected;
}

// Called by Central when the application is about to be unloaded/closed
function onDeactivate()
{
	trace("CMXtra app deactivated");

	// close LCService network connection
	gCom.close();

	// remove global variables
	gShell = null;
	gOnline = null;
	gFaveStatus = null;
	gSearchStatus = null;
	gSearching = null;
	gSelectedTab = null;
	gArticles_rs = null;
	
	// remove Flash Remoting variables
	inited = null;
	gatewayUrl = null;
	gateway_conn = null;
	searchService = null;
	today_date = null;
	
	// remove Key listener
	Key.removeListener(enterListener);

	// remove Favorites listener
	gFavorites.removeListener(faveListener);

	// remove AccordianTab listener
	myAcc.removeListener(this);

	// close LCDataProviders
	gLastSearch.close();
	gFavorites.close();
}

// Called when the application is resized. The application should resize itself accordingly
function onResize()
{	
	var bounds = gShell.getBounds();
}

// Called by Central to determine the Maximum size your application can be resized to.
// If there is no need to specify a  maximum size, you can remove this method.
function getMaximumSize()
{
	// set the properties below to your Maximum size.
	return {width:550, height:450};
}

// Called by Central to determine the Minimum size your application can be resized to.
// If there is no need to specify a  minimum size, you can remove this method.
function getMinimumSize()
{
	// set the properties below to your Maximum size.
	return {width:550, height:450};
}

// Called by Central when the application is about to be un-installed
function onUninstall()
{
	trace("Uninstalling CMXtra");
}

//-------------------------------------------------------------------
// App Initialization
//-------------------------------------------------------------------

// This tells Central that your application is ready to be displayed.
// Central calls the onActivate function after this call.
Central.initApplication(this, this);