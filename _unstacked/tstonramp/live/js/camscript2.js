	function Timer() 
	{
		var nZeroMin;
		var nZeroSec;
		var nTime = new Date();
		var nHours = nTime.getHours();
		var nMinutes = nTime.getMinutes();
		var nSeconds = nTime.getSeconds();
		window.setTimeout("Timer()", 1000);
		if (nMinutes < 10) {
			nZeroMin = "0";
		} else {
			nZeroMin = "";
		}
		
		if (nSeconds < 10) {
			nZeroSec = "0";
		} else {
			nZeroSec = "";
		}
		document.CurrentTime.but1.value = " " + nHours + ":" + nZeroMin + nMinutes + ":" + nZeroSec + nSeconds;
	}
	
		function CountTimer() 
	{
		var nZeroSec;
		var nTime = new Date();
		var nSeconds = nTime.getSeconds();
		window.setTimeout("CountTimer()", 1000);
				
		if (nSeconds < 10) {
			nZeroSec = "0";
		} else {
			nZeroSec = "";
		}
		
		//if (nSeconds > 30) {
			//nSeconds = nSeconds - 30;
		//}
		document.CurrentTime.but1.value = " " + nZeroSec + nSeconds;
	}
	
	function refreshImage(intIdx, strURL, intRefresh)
	{
	        intIdx++;
	        document.images.camimage.src = strURL + "?" + intIdx;
	        var strCall = "refreshImage(" + intIdx + ",'" + strURL + "', " + intRefresh + ");";
	        //setTimeout(strCall, 10000);
			setTimeout(strCall, intRefresh);
	}


	function emailer(linkURL) 
	{
		remote=window.open("","emailer","height=350,width=550,scrollbars=yes");
		
		remote.location.href = linkURL;
		if (remote.opener == null) remote.opener = window;
		remote.opener.name = "Main";
	}

function openremoteWindow()
        {
        open ("private.htm","monica",
"height=210,width=310,scrollbars=0,resizable=yes,status=no,border=no")
        }