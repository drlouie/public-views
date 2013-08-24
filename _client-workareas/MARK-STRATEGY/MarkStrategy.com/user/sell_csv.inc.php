<?
	header("Content-type: text/plain");
	header("Content-Disposition: attachment; filename=sellers.csv");
	
	
	echo KRF_table2CSV('selling', $sell_form, $SQL, 
						array(), " where id_user = $id ");
?>