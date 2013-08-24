<?
	header("Content-type: text/plain");
	header("Content-Disposition: attachment; filename=buyers.txt");
	
	
	echo KRF_table2TXT('buying', $order_form, $SQL, 
						array(), " where id_user = $id ");
?>