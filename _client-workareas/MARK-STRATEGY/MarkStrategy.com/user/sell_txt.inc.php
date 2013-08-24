<?
	header("Content-type: text/plain");
	header("Content-Disposition: attachment; filename=sellers.txt");
	
	
	echo KRF_table2TXT('selling', $sell_form, $SQL, 
						array(), " where id_user = $id ");
?>