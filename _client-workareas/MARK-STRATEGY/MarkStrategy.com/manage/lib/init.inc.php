<?
	if (!defined('INNER')) exit;
	
	include '../share/global.inc.php';
	include 'lib/config.inc.php';
	include 'lib/dynamic_form.inc.php';

	include '../share/sql.inc.php';
	include '../share/design.inc.php';
	include '../share/lib.inc.php';
	include '../share/dynamic_form_hash.inc.php';
	include '../share/homes.inc.php';
	
	$SQL = new KRF_SQL(
					$db_conf['user'], 
					$db_conf['passwd'], 
					$db_conf['host'],
					$db_conf['db']);

	$sname = session_name('manage');
	session_start();
	session_register('sKey');

	if ((! $logged_on = ($sKey == crypt(session_id(), session_id()))) || ($act == 'login'))
	{
		if ($act == 'login') $message = 'Incorrect login or password';
		
		$db = $SQL->Query("SELECT * FROM admin WHERE login='$login' AND passwd = '$passwd' LIMIT 0,1");
		if ($db && $SQL->Numrows($db))
		{
			$sname = session_name('manage');
			session_start();
			session_register('sKey');
			$sKey = crypt(session_id(), session_id());

            $logged_on = true;
            $act = 'default';
		}
		else
		{
			$act = 'login_form';
		}
    }
	else
	{
    	$act = (!$logged_on) ? 'login_form' : $act;
    	if (!$act) $act = 'default';
    }
?>
