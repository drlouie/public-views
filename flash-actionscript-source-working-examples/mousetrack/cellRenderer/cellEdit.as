on (cellEdit) {
	var sel = this.selectedIndex
	var data = this.getItemAt(sel)
	var price:Number = data.price
	var quantity:Number = data.quantity
	data.total = price*quantity
	data.available = data.quantity > 0
}
on (cellPress) {
	var sel = this.selectedIndex
	var data = this.getItemAt(sel)	
	if(data.available  == false and data.quantity > 0){
		data.quantity = 0
	} else if(data.available == true and data.quantity == 0){
		data.quantity = 1
	}
	var price:Number = data.price
	var quantity:Number = data.quantity
	data.total = price*quantity	
}






