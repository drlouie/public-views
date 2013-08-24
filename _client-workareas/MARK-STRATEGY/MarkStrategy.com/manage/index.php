<?
	define('INNER', TRUE);

	include 'lib/init.inc.php';
	if ($mode !== 'csv') include 'design/header.inc.php';

	if (file_exists($action_list[$act]))
	{
		if ($action_list[$act] != 'login.inc.php')
		{
			if ($mode !== 'csv' && $act !== 'logout') include 'lib/menu.inc.php';
		}

		$db = $SQL->Query("alter table user add column buy_homes text");
		$db = $SQL->Query("alter table user add column sell_homes text");
		
		include ($action_list[$act]);
	}
	else
	{
		include 'login.inc.php';
	}

	if ($mode !== 'csv') include 'design/footer.inc.php';

	$SQL->Close();
?>