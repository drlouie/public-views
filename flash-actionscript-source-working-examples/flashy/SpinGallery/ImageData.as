package {
	
	import flash.display.BitmapData;
	
	/**
	 * Data container for information related to images
	 */
	public class ImageData {
		
		/**
		 * thumbnail bitmapData
		 */
		public var bitmapData:BitmapData;
			
		/**
		 * URL to the main image
		 */
		public var imageURL:String;
			
		/**
		 * Title of the image
		 */
		public var title:String;
			
		/**
		 * Constructor
		 */
		public function ImageData(bitmapData:BitmapData = null, imageURL:String = "", title:String = ""){
			this.bitmapData = bitmapData;
			this.imageURL = imageURL;
			this.title = title;
		}
	}
}