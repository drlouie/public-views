// Interface for CMXtra
// Copyright 2003-2004 P.R. Newman, CommunityMX.com

// Interface across the agent (server) and application/pods (clients)

if(CMXService == null)
{
	CMXService = new Object();
	CMXService.name = "CMXService";
	CMXService.interfaces = new Object();

	// callable functions in clients (app, search pod)
	CMXService.interfaces.Client = ["formatSearchResult", "setQuery"];

	// callable functions in server (agent)
	CMXService.interfaces.Server = ["searchContent", "getQuery"];
}
