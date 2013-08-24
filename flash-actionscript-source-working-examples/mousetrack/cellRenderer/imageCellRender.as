import mx.core.UIComponent;
class imageCellRender extends UIComponent {
	var img:MovieClip;
	var url:String;
	var listOwner:MovieClip;
	// the reference we receive to the list
	var getCellIndex:Function;
	// the function we receive from the list
	var getDataLabel:Function;
	// the function we receive from the list
	function IconCellRenderer() {
	}
	function createChildren(Void):Void {
		//img = createObject("imageCont", "Img", 1, {styleName:this, owner:this});
		size();
	}
	function setValue(str:String, item:Object, sel:Boolean):Void {
		img._visible = (item[getDataLabel()] != undefined);
		//We move the head to the label matching 
		//current cell value
		if(item[getDataLabel()] != this.url){
			img.loadMovie(item[getDataLabel()]);
			this.onEnterFrame = function(){
				if(img.getBytesLoaded() >= img.getBytesTotal() && img.getBytesTotal() > 4 && img._width > 4){
					this.url = item[getDataLabel()]
					delete this.onEnterFrame;
				}
			}
		}
	}
	function size(Void) : Void
	{
		img._y = (img._height/2) - 2
	}	
}
