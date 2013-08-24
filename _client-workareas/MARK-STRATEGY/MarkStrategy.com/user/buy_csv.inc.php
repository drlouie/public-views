<?
	header("Content-type: text/plain");
	header("Content-Disposition: attachment; filename=buyers.csv");
	
	
	echo KRF_table2CSV('buying', $order_form, $SQL, 
						array(), " where id_user = $id ");
?>