// Shared Object for CMXtra
// Copyright 2003-2004 P.R. Newman, CommunityMX.com

//-------------------------------------------------------------------
// Shared Object initialization
//-------------------------------------------------------------------

function initStorage(){
	gStorage = SharedObject.getLocal(gAppName);

	if(gStorage.data.favorites == undefined){
		// create gStorage Shared Object
		gStorage.data.favorites = new Array();
	}
}

//-------------------------------------------------------------------
// Shared Object functions
//-------------------------------------------------------------------

function saveFavorites(){
	// delete all favorites in Shared Object
	gStorage.data.favorites.splice(0);

	var len = gFavorites.getLength();
	
	for(var i=0; i<len; i++){
		var item = gFavorites.getItemAt(i);
		// add gFavorites LCDataProvider to Shared Object
		gStorage.data.favorites.push({dDate: item.dDate, sDate: item.sDate, title: item.title, author: item.author, link: item.link, cat: item.cat});
	}
// write Shared Object to disk
gStorage.flush();
}

function deleteStorage(){
	
	// loop through SO and delete every row (this works)
	for (var i in gStorage.data) {
		delete gStorage.data[i];
	}
}
