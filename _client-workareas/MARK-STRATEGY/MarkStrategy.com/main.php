<?
	define('INNER', true);
	
	include 'share/init.inc.php';

	if ($found)
	{
		if ($target == 'top')
		{
			include 'templates/top_frame.inc.php';
		}
		else if ($target == 'left')
		{
			include 'templates/right_frame.inc.php';
		}
		else if ($target == 'bottom')
		{
			include 'templates/bottom_frame.inc.php';
		}
		else 
		{
			include 'templates/main_frame.inc.php';
		}
	}
	else
	{
		include 'templates/not_found.inc.php';		
	}
?>