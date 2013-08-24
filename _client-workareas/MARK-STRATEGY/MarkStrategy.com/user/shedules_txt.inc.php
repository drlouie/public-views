<?
	header("Content-type: text/plain");
	header("Content-Disposition: attachment; filename=schedules.txt");
	
	
	echo KRF_Shedulers2TXT($id, $SQL);
?>