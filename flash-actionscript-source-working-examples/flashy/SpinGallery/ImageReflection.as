package {
	
	import flash.display.BitmapData;
	import flash.display.BitmapDataChannel;
	import flash.display.Shape;
	import flash.display.GradientType;
	import flash.geom.Matrix;
	import flash.geom.Point;
	import flash.geom.Rectangle;
	
	/**
	 * Adds a reflection to an bitmap image extending a bitmap
	 * at the bottom with a faded relflection of itself
	 */
	public class ImageReflection {
		
		/**
		 * Returns a new bitmap representing the one passed with a reflection added
		 */
		public static function addReflection(bmp:BitmapData, reflectionHeight:Number = 100):BitmapData {
			if (!bmp) return null;
				
			// create the bitmap of the reflected version 
			var reflected:BitmapData = new BitmapData(bmp.width, bmp.height + reflectionHeight, true, 0x00000000);
			
			// copy the original bitmap into the reflection
			reflected.copyPixels(bmp, bmp.rect, new Point(0,0));
			
			// copy the reflection of the original bitmap into the reflected version  
			reflected.draw(bmp, new Matrix(1, 0, 0, -1, 0, bmp.height*2));
			
			// create a gradient for the relflection's fade out
			// in a shape display object
			var matrix:Matrix = new Matrix();
			matrix.createGradientBox(bmp.width, reflectionHeight, Math.PI/2, 0, 0);
			var gradientShape:Shape = new Shape();
			gradientShape.graphics.beginGradientFill(GradientType.LINEAR, [0x000000, 0x000000], [.4, 0], [0x00, 0xFF], matrix);
			gradientShape.graphics.drawRect(0, 0, bmp.width, reflectionHeight);
			gradientShape.graphics.endFill();
			
			// add the fade to a bitmap
			var gradientBmp:BitmapData = new BitmapData(bmp.width, reflectionHeight, true, 0x00000000);
			gradientBmp.draw(gradientShape);
			
			// apply the fade to the reflected bitmap
			reflected.copyChannel(gradientBmp, new Rectangle(0,0, gradientBmp.width, Math.min(bmp.height, gradientBmp.height)), new Point(0, bmp.height), BitmapDataChannel.ALPHA, BitmapDataChannel.ALPHA);
			return reflected;
		}
	}
}