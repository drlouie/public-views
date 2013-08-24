Dynamic Page Flip v2
--------------------

Steve Palmer
steve@76design.com
August 22, 2006

*With full credit to Macc at IpariGrafika (http://www.iparigrafika.hu/pageflip) for the brilliant page flipping engine on which this is based


New Features
------------

(Please refer to included XML file to see examples)

Ability to specify which pages must be preloaded before the book starts (others will preload in the background)
	<page src="pages/anim1.swf" preLoad="true" />


Ability to specify a function to run after a page is torn out (limit of 5 paramters)
	<page src="pages/page2.jpg" canTear="true" afterTear="loadMovie,'pages/spread.swf',_root.topSpread" />


Ability to have a "spread" (i.e. a single page that spans two pages)
	<page src="pages/spread.swf" isSpread="true" preLoad="true" />
	<page src="pages/spread.swf" isSpread="true" preLoad="true" />
	
	* Make sure your spread spans two consecutive pages and doesn't start on an odd page 
	  (i.e. pages 8,9 = good   pages 9,10 = bad)
	

Ability to place a "page" that precedes the book (ideal for instructions, tips, or help)
	<content prepage="pages/prepage.swf">


Ability to have pages perform actions when they're turned to:
	Place functions called onVisible and onInvisible in your page SWFs.
	(i.e.
		function onVisible() {
			trace("Just turned to this page!");
			}
		
		function onInvisible() {
			trace("Just left this page!");
			}
	)


	
Notes
-----

To include video, please refer to the sample file (video.fla) in the /pages folder.  The video doesn't have to be embedded on the timeline as I've shown (dynamically loading an FLV or SWF would work fine too) but the key is that the video CAN'T start on the first frame.  This WILL cause problems.  I'd recommend using the onVisible and onInvisible functions mentioned above to control the video playback.
