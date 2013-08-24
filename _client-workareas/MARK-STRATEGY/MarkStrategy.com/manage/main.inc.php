<form id="users_list_form" name="users_list_form" method="post">
<input type="hidden" name="act" value="users" />
<input type="hidden" name="todo" value="" />
<input type="hidden" name="id" value="" />
<?
	if (!defined('INNER')) exit;

	if ($todo == 'delete')
	{
		$fields = array();
		if (is_array($del))
		{
			foreach($del as $key => $value)
			{
				if ($value) 
				{
					$fields[] = $key;
				
					$db = $SQL->Query("SELECT logo, photo FROM user WHERE id=$key LIMIT 0,1");
					if ($db && $SQL->Numrows($db))
					{
						list($logo, $photo) = $SQL->Fetchrow($db);
						if ($logo)  @unlink($main['files']['logo' ].$key.'.'.$logo);
						if ($photo) @unlink($main['files']['photo'].$key.'.'.$photo);
					}
				}
			}

			if (count($fields))
			{
				$SQL->Query('DELETE FROM user WHERE id IN ('.implode($fields, ',').')');
			}
		}
	}
	
	$cnt = ShowUsers($window);
	//ShowUserMenu($cnt);
?>
</form>