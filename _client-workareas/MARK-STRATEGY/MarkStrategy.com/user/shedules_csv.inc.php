<?
	header("Content-type: text/plain");
	header("Content-Disposition: attachment; filename=schedules.csv");
	
	
	echo KRF_Shedulers2CSV($id, $SQL);
?>