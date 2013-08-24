<?php
// ========================================================
// http://www.sephiroth.it/tutorials/flashPHP/cellRenderer
// Alessandro Crugnola
// =======================================================

// custom object (for passing to Flash)
class oData{
	var $id, $available, $item, $preview, $quantity, $price, $total;
	function oData($id, $available, $item, $preview, $quantity, $price){
		$this->id        = $id;
		$this->available = $available;
		$this->item      = $item;
		$this->preview   = $preview;
		$this->quantity  = $quantity;
		$this->price     = $price;
		$this->total     = $price*$quantity;
	}
}

// main data array (array of objects)
$mainData = array();
$mainData[] = new oData(1,true,"Australia","AUS.jpg",1, 200);
$mainData[] = new oData(2,true,"Canada","CAN.jpg",2, 420);
$mainData[] = new oData(3,true,"Italy","ITA.jpg",3, 340);
$mainData[] = new oData(4,false,"Brazil","BRA.jpg",0, 100);
$mainData[] = new oData(5,true,"Austria","AUT.jpg",3, 200);

// print the serialized variables in 
// the correct ouput for flash
echo "output=" . urlencode(utf8_encode(serialize($mainData)));
?>