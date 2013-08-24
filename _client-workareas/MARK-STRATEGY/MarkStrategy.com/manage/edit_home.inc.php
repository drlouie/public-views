<form action="?" name="edit_home_form" id="add_home_form" method="post" enctype="multipart/form-data">
<input type="hidden" name="act" value="edit_home" />
<input type="hidden" name="id" value="<?= $id;?>" />
<input type="hidden" name="id_home" value="<?= $id_home;?>" />
<input type="hidden" name="done" value="1" />
<?
	if (!defined('INNER')) exit;

	if ($done)
	{
		$data = array();
		foreach($cfg_home_form as $key => $value)
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
		$is_err = KRF_CheckFormData($cfg_home_form, $data, $errors);

		if (!$is_err)
		{
			KRF_UpdateFormData('homes', $cfg_home_form, $data, $id_home);

			$message = 'All data successfully saved';
		}
	}
	else
	{
		$terminate = false;
		$fields = array();
		foreach($cfg_home_form as $key => $value)
		{
			if ($value['field'])
				$fields[$key] = $value['field'];
		}
		
		$db = $SQL->Query("SELECT ".implode($fields, ',')." FROM homes WHERE id=$id_home");
		
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

	/*if (($is_err || !$done)&&(!$terminate))
	{*/
		$db = $SQL->Query("SELECT home_photo FROM homes WHERE id=$id_home");
		list($photo) = $SQL->Fetchrow($db);
		
		if ($photo)
		{
			//$data['home_photo'] = Array();
			$data['home_photo']['view'] = $main['files']['home_photo'].$id_home.'.'.$photo;
		}
		
		$agent = KRF_getAgent($id, $SQL);

		$window['caption'] = "Featured listing for <b>{$agent['fname']} {$agent['mname']} {$agent['lname']}</b>";
		$window['left'   ] = '<a href="#" class="menu" onclick="f=document.getElementById(\'add_home_form\'); f.act.value=\'supply_user\'; f.done.value=0; f.submit()">&lt;&lt;&lt;&nbsp;Back</a>&nbsp;|&nbsp;';
		$window['inner'  ] = '<br /><span style="color:red">'.$message.'</span><br /><table width="100%" cellspacing="0" cellpadding="5">'.
						GenerateForm($cfg_home_form, $data, $errors).'</table>';
		
		$window['inner'  ] .= <<<BUTTONS
			<hr size="1" width="100%" />
			<table width="100%" cellspacing="0" cellpadding="2">
			<tr>
			<td width="50%" align="left"><input type="submit" value="Save changes" style="width:50%" /></td>
			<td width="50%" align="right" ><input type="button" value="Cancel" style="width:50%" onclick="f=document.getElementById('add_home_form'); f.act.value='supply_user'; f.done.value='0'; f.submit()" /></td>
			</tr>
			</table>
BUTTONS;
		echo ShowWindow($window);
		
		?></form><?
	/*}
	else
	{
		echo '<script>document.location.href="'.$main['root.com'].'manage/?act=supply_user&id='.$id.'";</script>';
	}*/
?>