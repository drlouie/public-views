<?
	header("Content-type: text/plain");
	header("Content-Disposition: attachment; filename=featured_listings.csv");
	
	
	echo "\nAgent information\n";
	echo KRF_table2CSV('user', $user_form, $SQL, 
						array('logo' => 'img/logo/', 'photo' => 'img/photo/'), " where id = $id ");
	echo "\n\nFeatured homes listings\n";
	echo KRF_table2CSV('homes', $cfg_home_form, $SQL, 
						array('home_photo' => 'img/homes/'), " where id_user = $id ");
?>