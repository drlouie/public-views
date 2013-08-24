package {
	
	import flash.display.BitmapData;
	import flash.display.Graphics;
	import flash.geom.Matrix;

	/**
	 * Creates a mesh for distorting an image in 3D space
	 */
	public class ImageMesh3D {
		
		/**
		 * determines if lines are drawn illustrating
		 * the mesh used to render the image
		 */
		public static var showMesh:Boolean = false;
			
		/**
		 * Draws into the target graphics the bitmap provided within the 3D coordinates passed
		 * When used, the oneSided property can be either -1 or 1 where -1 represents one side of the
		 * image and 1 the other where only that side is drawn.  0 indicates that both sides are drawn
		 */	
		public static function draw(target:Graphics, bitmap:BitmapData, divsX:int, divsY:int, x1:Number, y1:Number, z1:Number, x2:Number, y2:Number, z2:Number, x3:Number, y3:Number, z3:Number, x4:Number, y4:Number, z4:Number, env:Environment3D, oneSided:int = 0):void {
			if (!bitmap) return;
			var w:Number = bitmap.width;
			var h:Number = bitmap.height;
			var dh:Number = divsY/h;
			var dw:Number = divsX/w;
			var countX:int = divsX + 1;
			var countY:int = divsY + 1;
			var index:int;
			var indexR:int;
			var pts:Array = [];
			var pt:_MeshPoint;
			var ptB:_MeshPoint;
			var ptC:_MeshPoint;
			var x:Number;
			var y:Number;
			var z:Number;
			var scale:Number;
			var factorX:Number;
			var factorY:Number;
			var spanX:Number;
			var spanY:Number;
			var spanZ:Number;
			var dx1:Number = x4 - x1;
			var dy1:Number = y4 - y1;
			var dz1:Number = z4 - z1;
			var dx2:Number = x3 - x2;
			var dy2:Number = y3 - y2;
			var dz2:Number = z3 - z2;
			var yi:int;
			var xi:int;
			
			// draw outlines if necessary
			if (showMesh) {
				target.lineStyle(1, 0xFF0000);
			}
			
			// loop through all points in the mesh starting with rows
			yi = countY;
			while(yi--){
				// row division
				factorY = yi/divsY;
				x = x1 + factorY*dx1;
				y = y1 + factorY*dy1;
				z = z1 + factorY*dz1;
				spanX = x2 + factorY*dx2 - x;
				spanY = y2 + factorY*dy2 - y;
				spanZ = z2 + factorY*dz2 - z;
				
				// loop through all columns in the current row
				xi = countX;
				while (xi--){
					// col division
					factorX = xi/divsX;
					scale = env.focalLength/(env.focalLength + z + factorX*spanZ);
					pt = new _MeshPoint(env.originX + scale*(x + factorX*spanX), env.originY + scale*(y + factorX*spanY), factorX*w, factorY*h);
					index = xi + yi*countX;
					pts[index] = pt;
					
					// draw triangles
					if (xi < divsX && yi < divsY) {
						indexR = index + countX;
						
						// right and bottom points of triangle
						ptB = pts[index + 1];
						ptC = pts[indexR];
						
						// check for one sided rendering
						if (oneSided){
							
							// check for one sided-ness on the default side
							if (((ptB.y - pt.y)/(ptB.x - pt.x) - (ptC.y - pt.y)/(ptC.x - pt.x) < 0) != (pt.x <= ptB.x == pt.x > ptC.x)){
								
								// 1 or -1 determines which side is rendered
								if (oneSided > 0){
									oneSided = 0;
								}else{
									
									// not this side, return
									return;
								}
							}else{
								if (oneSided < 0){
									oneSided = 0;
								}else{
									
									// not this side, return
									return;
								}
							}
						}
						
						// top left
						// a-d calcs for top left point
						// these may be used again for a bottom right triangle
						pt.a = dw*(ptB.x - pt.x);
						pt.b = dw*(ptB.y - pt.y);
						pt.c = dh*(ptC.x - pt.x);
						pt.d = dh*(ptC.y - pt.y);
						
						// draw triangle
						target.beginBitmapFill(bitmap, new Matrix(pt.a, pt.b, pt.c, pt.d, pt.x - pt.dx*pt.a - pt.dy*pt.c, pt.y - pt.dx*pt.b - pt.dy*pt.d), false, true);
						target.moveTo(pt.x, pt.y);
						target.lineTo(ptB.x, ptB.y);
						target.lineTo(ptC.x, ptC.y);
						target.endFill();
						
						// bottom right
						pt = pts[indexR + 1];
						
						// use existing a-d calcs if exist for points
						// otherwise define them now
						if (isNaN(ptC.a)){
							ptC.a = dw*(pt.x - ptC.x);
							ptC.b = dw*(pt.y - ptC.y);
						}
						if (isNaN(ptB.c)){
							ptB.c = dh*(pt.x - ptB.x);
							ptB.d = dh*(pt.y - ptB.y);
						}
						
						// draw triangle
						target.beginBitmapFill(bitmap, new Matrix(ptC.a, ptC.b, ptB.c, ptB.d, pt.x - pt.dx*ptC.a - pt.dy*ptB.c, pt.y - pt.dx*ptC.b - pt.dy*ptB.d), false, true);
						target.moveTo(pt.x, pt.y);
						target.lineTo(ptB.x, ptB.y);
						target.lineTo(ptC.x, ptC.y);
						target.endFill();
					}
				}
			}
		}
	}
}

/**
 * Represents a point in the mesh with additional matrix information (a-d)
 */
internal class _MeshPoint {
	
	public var x:Number;
	public var y:Number;
	public var dx:Number;
	public var dy:Number;
	public var a:Number;
	public var b:Number;
	public var c:Number;
	public var d:Number;
	
	public function _MeshPoint(x:Number, y:Number, dx:Number, dy:Number){
		this.x = x;
		this.y = y;
		this.dx = dx;
		this.dy = dy;
	}
}