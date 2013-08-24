// CMXtra Agent
// Copyright 2003-2004 P.R. Newman, CommunityMX.com

#include "shared/interface.as"
#include "shared/functions.as"
#include "favorites.as"

//-------------------------------------------------------------------
// Globals
//-------------------------------------------------------------------

Central.tracer.appName = "cmxtra";	// for App Name Filter in Debug Panel

var gAgentManager;					// callback to Central AgentManager API
var gAppName = "cmxtra";			// used by favorites.as
var gOnline = false;				// whether we currently have a network connection
var gQuery;							// latest search query string

var gCom;							// LCService object to communicate with apps and pods
var gLastSearch;					// LCDataProvider object
var gFavorites;						// LCDataProvider object
var gStorage;						// Shared Object for favorites

//-------------------------------------------------------------------
// Initialization
//-------------------------------------------------------------------

function onActivate(agentManager, agentID, initialData)
{
	gAgentManager = agentManager;
	onNetworkChange(gAgentManager.isConnected());
	
	// instantiate local communication service between this agent (server) and apps/pods (clients)
	gCom = Central.LCService.createServer(CMXService, this, true);
	
	// instantiate WebService object
  	var myWSDLUri = "http://www.communitymx.com/com/communitymx/centralSearch.cfc?wsdl";
  	this.myWebServiceObject = new WebService(myWSDLUri);
	
	// create an LCDataProvider instance for search results (server)
	gLastSearch = Central.LCDataProvider.createServer("cmx_search");
	
	// initialize Shared Object (favorites.as)
	initStorage();
	// create LCDataProvider Server for favorites
    gFavorites = Central.LCDataProvider.createServer("cmx_faves");
	// get initial data from local Shared Object
	gFavorites.setData(gStorage.data.favorites);
}

function onDeactivate()
{
	trace("CMXtra agent deactivated");

	// close LCService network connection
	gCom.close();
	
	// save gFavorites to Shared Object (favorites.as)
	saveFavorites();

	// remove global variables
	gAgentManager = null;
	gAppName = null;
	gOnline = null;
	gQuery = null;

	// close LCDataProviders
	gLastSearch.close();
	gFavorites.close();
}

function onNetworkChange(connected)
{
	trace("agent online: " + (connected ? "true" : "false"));

	gOnline = connected;
}

// Called by Central when the application is about to be uninstalled
function onUninstall()
{
	// delete Shared Object that stores favorites (favorites.as)
	deleteStorage();
}

//-------------------------------------------------------------------
// Main agent activity
//-------------------------------------------------------------------

function getQuery(){
	gCom.setQuery(gQuery);
}

function searchContent(query){	
	// set global gQuery variable
	gQuery = query;
	
	// Create DataProviderClass object
	var dp = new Central.DataProviderClass();
	
  	var myRequest = myWebServiceObject.searchContent(query); 
  	myRequest.onResult = function(result){
		
		// loop through result and create LCDataProviderClass object
		var len = result.data.length;
		for(var i=0; i<len; i++){
			var thisRow = result.data[i];
			
			// add rows to data provider
			dp.addItem({
					Title: thisRow[0],
					Link: thisRow[1],
					sDate: formatDate(thisRow[4], 1),
					dDate: thisRow[4],
					Author: thisRow[5],
					Cat: thisRow[6]
			});  
		}
				
		if(dp.getLength() > 0){
			// set DataProvider for LCDataProvider object
			gLastSearch.setData(dp);		
		}
		else{
			// clear search results
			gLastSearch.removeAll();
			// provide feedback if no results found
			gLastSearch.addItem({Title: "No results found."});
		}
		// call formatSearchResult function in app and pod using LCService object
		gCom.formatSearchResult(query);
  	}
	
  	myRequest.onFault = function(fault){
		// reset DataGrids
		gLastSearch.removeAll();

		gLastSearch.addItem({Title: "Error: Unable to connect"});
    	trace("Error: " + fault.faultstring);
  	}
}

//-------------------------------------------------------------------
// Agent Initialization
//-------------------------------------------------------------------

Central.initAgent(this, this);
