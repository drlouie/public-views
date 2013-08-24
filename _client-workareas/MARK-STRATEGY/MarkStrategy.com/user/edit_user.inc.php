<form action="?" name="edit_user_form" id="edit_user_form" method="post" enctype="multipart/form-data">
<input type="hidden" name="act" value="edit_user" />
<input type="hidden" name="id" value="<?= $id;?>" />
<input type="hidden" name="done" value="1" />
<?
	if (!defined('INNER')) exit;

	if ($done)
	{
		$data = array();
		foreach($user_form as $key => $value)
		{
			if ($value['data_type'] == 'file')
			{
				$name = $key.'_name';
				$type = $key.'_type';

				$data[$key]['name'] = $$name;
				$data[$key]['type'] = $$type;
				$data[$key]['file'] = $$key;

				if ($data[$key]['name'])
				{
					$last_dot = strrpos($data[$key]['name'], '.');
					$data[$key]['ext'] = substr($data[$key]['name'], $last_dot+1, strlen($data[$key]['name']) - $last_dot + 2);
				}
			}
			else $data[$key] = $$key;
		}
		$is_err = KRF_CheckFormData($user_form, $data, $errors);

		if (!$is_err)
		{
			$rep = KRF_CheckUserData($data, $id);
			if (!$rep['is_err'])
			{
				KRF_UpdateFormData('user', $user_form, $data, $id);
			}
			else
			{
				$is_err = true;
				if ($rep['login' ]) $errors['login' ] = 'user with such login already exists';
				if ($rep['domain']) $errors['domain'] = 'user with such domain already exists';
			}
		}
	}
	else
	{
		$terminate = false;
		$fields = array();
		foreach($user_form as $key => $value)
		{
			if ($value['field'])
				$fields[$key] = $value['field'];
		}
		
		$db = $SQL->Query("SELECT ".implode($fields, ',')." FROM user WHERE id=$id");
		
		if ($db && $SQL->Numrows($db))
		{
			$fetch_data = $SQL->Fetcharray($db, 'num');
			$i = 0;
			foreach($fields as $key => $value)
			{
				$data[$key] = $fetch_data[$i];
				$i++;
			}
		}
		else $terminate = true;
		
		$errors = NULL;
	}

	if (!$terminate)
	{
		$db = $SQL->Query("SELECT logo, photo FROM user WHERE id=$id");
		list($logo, $photo) = $SQL->Fetchrow($db);
		
		if ($logo)
		{
			$data['logo']['view'] = $main['files']['logo'].$id.'.'.$logo;
		}
		else $data['logo']['view'] = '';

		if ($photo)
		{
			$data['photo']['view'] = $main['files']['photo'].$id.'.'.$photo;
		}
		else $data['photo']['view'] = '';

		$window['caption'] = 'Personal information';
		$window['inner'  ] = '<br /><table width="100%" cellspacing="0" cellpadding="5">'.
						GenerateForm($user_form, $data, $errors).'</table>';
		$window['inner'  ] .= <<<BUTTONS
			<hr size="1" width="100%" />
			<table width="100%" cellspacing="0" cellpadding="2">
			<tr>
			<td width="50%" align="left"><input type="submit" value="Save changes" style="width:50%" /></td>
			<td width="50%" align="right">&nbsp;</td>
			</tr>
			</table>
BUTTONS;
		
		echo ShowWindow($window);
		
		?></form><?
	}
	else
	{
		echo '<script>document.location.href="'.$main['root.com'].'user/?act=login";</script>';
	}
?>


