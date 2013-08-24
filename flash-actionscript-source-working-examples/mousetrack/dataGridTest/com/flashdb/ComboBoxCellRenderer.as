//****************************************************************************
// Flash-db Cellrenderer Tutorial
//****************************************************************************

import mx.core.UIComponent
import mx.controls.ComboBox

class com.flashdb.ComboBoxCellRenderer extends UIComponent
{

	var combo : MovieClip;
	var listOwner : MovieClip; // the reference we receive to the list
	var getCellIndex : Function; // the function we receive from the list
	var	getDataLabel : Function; // the function we receive from the list
	
	function ComboBoxCellRenderer()
	{
	}

	function createChildren(Void) : Void
	{	
		//Creates a ComboBox object and listen to changes
		combo = createObject("ComboBox", "Combo", 1, {styleName:this, owner:this});
		combo.addEventListener("change", this);
		size();
	}

	// note that setSize is implemented by UIComponent and calls size(), after setting
	// __width and __height
	function size(Void) : Void
	{
		combo.setSize(150, 20);
		combo._x = (__width-150)/2;
		combo._y = (__height-20)/2;
	}

	function setValue(str:String, item:Object, sel:Boolean) : Void
	{	//Get values from the dataProvider
		//item.Model is an array of labels/data pairs
		combo._visible = (item!=undefined);
		combo.dataProvider = item.Model;
	}

	function getPreferredHeight(Void) : Number
	{
		return 16;
	}

	function getPreferredWidth(Void) : Number
	{
		return 20;
	}
	// This re-build the dataProvider, the selected item
	// as the first in the array
	function reorder(datos:Array, choice:String):Array {
		var index:Number = 0
		var newArray = new Array()
		for(var i=0; i<datos.length; i++){		
			if(datos[i].label!=choice){
				index++
				newArray[index] = datos[i]
			} else newArray[0] = datos[i]
		}	
		return newArray
	}

	function change()	
	{
		//Refresh the dataProvider and save value in ModelName and 
		//ModelVal columns for later retrieve
		listOwner.dataProvider.editField(getCellIndex().itemIndex, getDataLabel(), reorder(combo.dataProvider, combo.selectedItem.label));
		listOwner.dataProvider.editField(getCellIndex().itemIndex, getDataLabel()+"Name", combo.selectedItem.label);		
		listOwner.dataProvider.editField(getCellIndex().itemIndex, getDataLabel()+"Val", combo.selectedItem.data);				
	}

}
