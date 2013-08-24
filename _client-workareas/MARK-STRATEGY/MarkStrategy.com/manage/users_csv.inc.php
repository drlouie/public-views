<?
	header("Content-type: text/plain");
	header("Content-Disposition: attachment; filename=agents.csv");
	
	
	echo KRF_table2CSV('user', $user_form, $SQL, 
						array('logo' => 'img/logo/', 'photo' => 'img/photo/'));
?>