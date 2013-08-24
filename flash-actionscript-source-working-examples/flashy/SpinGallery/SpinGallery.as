package {
	
	import flash.display.BitmapData;
	import flash.display.GradientType;
	import flash.display.Loader;
	import flash.display.Sprite;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.events.Event;
	import flash.events.IOErrorEvent; 
	import flash.events.MouseEvent; 
	import flash.events.SecurityErrorEvent; 
	import flash.filters.DropShadowFilter;
	import flash.geom.Matrix;
	import flash.net.URLLoader;
	import flash.net.URLRequest;
	import flash.text.TextField;
	import flash.text.TextFieldAutoSize;
	import flash.text.TextFormat;
	import flash.utils.getTimer;
		
	/**
	 * A gallery with a rotating carousel of thumbnails for images
	 * that spin into view when selected
	 */
	[SWF(width="600", height="450", backgroundColor="#A8A8AF")]
	public class SpinGallery extends Sprite {
		
		private var loader:ThumbLoader = new ThumbLoader();
		private var status:TextField = new TextField();
		private var canvas:RotateViewImage = new RotateViewImage();
		private var carousel:ImageCarousel = new ImageCarousel();
		private var bitmap:BitmapData;
		private static var statusShadow:DropShadowFilter = new DropShadowFilter(4.0, 45, 0x808088, 0.5, 4.0, 4.0, 1.0, 1, false, true);		
		
		/**
		 * Constructor
		 */
		public function SpinGallery() {
			
			// restrict stage scaling
			stage.align = StageAlign.TOP_LEFT;
			stage.scaleMode = StageScaleMode.NO_SCALE;
			
			// create/add assets
			drawBackground();
			setupStatusText();
			addChild(status);
			addChild(canvas);
			addChild(carousel);
			
			// set the target of the carousel to be the canvas
			// so thumbnails clicked can be loaded into the canvas
			carousel.target = canvas;
			
			// define loading listeners
			canvas.addEventListener(Event.OPEN, loadingImage);
			canvas.addEventListener(Event.COMPLETE, imageLoaded);
			loader.addEventListener(Event.COMPLETE, thumbsLoaded);
			
			// listener for previewing image meshes
			// when clicking the top left of the screen
			stage.addEventListener(MouseEvent.MOUSE_DOWN, renderMeshes);
			
			load("images.xml");
			
		}
		
		/**
		 * Load XML into the gallery
		 */
		public function load(url:String):void {
			setStatus("Loading thumbnails...");
			loader.load(new URLRequest(url));
		}
		
		/**
		 * Event handler; canvas image starting to load
		 */
		private function loadingImage(event:Event):void {
			setStatus("Loading "+RotateViewImage(event.target).name+"...");
		}
		
		/**
		 * Event handler; canvas image loaded
		 */
		private function imageLoaded(event:Event):void {
			setStatus("");
		}
		
		/**
		 * Event handler; thumbnails loaded
		 */
		private function thumbsLoaded(event:Event):void {
			setStatus("");
			if (loader.data.length) {
				
				// assign loaded thumbnails to carousel images 
				carousel.images = loader.data;
				
				// default canvas image to the first image
				// in the thumbnails loaded
				canvas.showImage(loader.data[0]);
			}
		}
		
		/**
		 * Draws the background of the application
		 */
		private function drawBackground():void {
			var w:Number = 600;
			var h:Number = 450;
			
			// 2 part gradient split in the center of the screen (ground and sky)
			var matrix:Matrix = new Matrix();
			matrix.createGradientBox(w, h, Math.PI/2, 0, 0);
			graphics.beginGradientFill(GradientType.LINEAR, [0x808088, 0xF8F8FF, 0x505058, 0xA8A8AF], [1,1,1,1], [0x00, 0x80, 0x80, 0xFF], matrix);
			graphics.drawRect(0, 0, w, h);
		}
		
		/**
		 * Defines the status text used to indicate loading
		 */
		private function setupStatusText():void {
			var format:TextFormat = status.getTextFormat();
			format.font = "_sans";
			format.size = 36;
			format.bold = true;
			format.italic = true;
			status.defaultTextFormat = format;
			status.autoSize = TextFieldAutoSize.LEFT;
			status.textColor = 0x505058;
			status.selectable = false;
			status.y = 190;
		}
		
		/**
		 * Sets the status message and applies shadow effect
		 */
		private function setStatus(msg:String):void {
			status.filters = [];
			status.text = msg;
			status.filters = [statusShadow];
		}
		
		/**
		 * Event handler; called when top left corner of app is clicked
		 * Toggles display of mesh lines in carousel and canvas
		 */
		private function renderMeshes(event:MouseEvent):void {
			if (mouseX < 5 && mouseY < 5){
				ImageMesh3D.showMesh = !ImageMesh3D.showMesh;
			}
		}
	}
}