package {
	
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.DisplayObject;
	import flash.display.Loader;
	import flash.display.LoaderInfo;
	import flash.events.Event;
	import flash.events.EventDispatcher;
	import flash.events.IOErrorEvent;
	import flash.events.SecurityErrorEvent;
	import flash.net.URLLoader;
	import flash.net.URLRequest;
	
	/**
	 * Loads a group of thumbnails via XML. Thumbnails are accessible through the data array
	 */
	public class ThumbLoader extends EventDispatcher {
			
		public var data:Array = [];
		public var images:XMLList;
		public var loadInProgress:Boolean = false;
			
		private var xmlLoader:URLLoader = new URLLoader();
		private var loaders:Array = [];
		private var counter:int = 0;
			
		/**
		 * Constructor
		 */
		public function ThumbLoader() {
			
			// setup listeners for loading XML
			xmlLoader.addEventListener(Event.COMPLETE, xmlLoaded);
			xmlLoader.addEventListener(IOErrorEvent.IO_ERROR, xmlLoadError);
			xmlLoader.addEventListener(SecurityErrorEvent.SECURITY_ERROR, xmlLoadError);
		}
		
		/**
		 * Loads an XML file referencing thumbnails and full size images with a title
		 */
		public function load(request:URLRequest):void {
			
			// cleanup
			if (loadInProgress) {
				cleanupLoaders();
			}else{
				loadInProgress = true;
			}
			
			// default arrays
			loaders = [];
			data = [];
			
			// initiate loading process
			xmlLoader.load(request);
		}
		
		/**
		 * Event handler; called when XML has loaded
		 * Loads all thumbnails within the XML into loader objects
		 */
		private function xmlLoaded(event:Event):void {
			try {
				// get images list from the loaded XML file
				var imagesXML:XML = XML(xmlLoader.data);
				images = imagesXML.image;
				var container:Loader;
				var info:LoaderInfo;
				
				// loop through all the images in the XML
				for each (var image:XML in images){
					
					// make a new loader for each image
					// loading the thumbnail specified in the XML into that loader
					container = new Loader();
					info = container.contentLoaderInfo;
					info.addEventListener(Event.INIT, thumbLoaded);
					info.addEventListener(IOErrorEvent.IO_ERROR, thumbLoadError);
					info.addEventListener(SecurityErrorEvent.SECURITY_ERROR, thumbLoadError);
					container.load(new URLRequest(image.@thumbnailUrl));
					
					// add the data to the data array
					data.push(new ImageData(null, image.@url, image.@title));
					
					// add the loader to the loaders array (this also retains image order)
					loaders.push(container);
				}
				
				// set the counter to equal the number of images in the XML
				// when it reaches 0, that will mean all thumbs have loaded
				counter = loaders.length;
				
			}catch (err:Error) {
				
				// call xmlLoadError if there was an error from above
				xmlLoadError(event);
			}
		}
		
		/**
		 * Event handler; called when an error has occurred in loading the XML
		 * Signals the COMPLETE event as no other actions can be made without XML
		 */
		private function xmlLoadError(event:Event):void {
			dispatchEvent(new Event(Event.COMPLETE));
			loadInProgress = false;
		}
		
		/**
		 * Event handler; called when a thumbnail has loaded into a loader
		 */
		private function thumbLoaded(event:Event):void {
			
			// decrement counter for loaded thumbs
			counter--;
			try {
				
				// get loader and clean up listeners
				var container:Loader = Loader(event.target.loader);
				cleanupInfoListeners(container.contentLoaderInfo);
				
				// extract bitmapData from the loaded bitmap and assign it to the 
				// ImageData instance in the respective location of the data array
				data[loaders.indexOf(container)].bitmapData = Bitmap(container.content).bitmapData;
				
			}catch (err:Error) { }
			
			// check to see if all loaders have finnished
			// loading the all the thumbnails
			checkComplete();
		}
		
		/**
		 * Event handler; called when an error has occurred in loading a thumbnail
		 */
		private function thumbLoadError(event:Event):void {
			
			// decrement counter and check for load completion
			counter--;
			checkComplete();
		}
		
		/**
		 * Checks to see all thumbnails have loaded; if so, dispatch COMPLETE event
		 */
		private function checkComplete():void {
			if (loadInProgress && counter <= 0){
				dispatchEvent(new Event(Event.COMPLETE));
				loadInProgress = false;
			}
		}
		
		/**
		 * Closes all loader connections and removes loader listeners
		 */
		private function cleanupLoaders():void {
			for each(var container:Loader in loaders){
				try{
					container.close();
				}catch(err:Error){ }
				cleanupInfoListeners(container.contentLoaderInfo);
			}
		}
		
		/**
		 * Cleans up loader listeners
		 */
		private function cleanupInfoListeners(info:LoaderInfo):void {
			info.removeEventListener(Event.INIT, thumbLoaded);
			info.removeEventListener(IOErrorEvent.IO_ERROR, thumbLoadError);
			info.removeEventListener(SecurityErrorEvent.SECURITY_ERROR, thumbLoadError);
		}
	}
}