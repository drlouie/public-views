<form action="?" name="add_home_form" id="add_home_form" method="post" enctype="multipart/form-data">
<input type="hidden" name="act" value="add_home" />
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
			$insId = KRF_StoreFormData('homes', $cfg_home_form, $data);
			$SQL->Query("UPDATE homes SET id_user = $uId WHERE id=$insId");

			KRF_StoreToolbarSettings($insId, $url, $SQL);
		}
	}
	else
	{
		$data = $errors = NULL;
	}

	if ($is_err || !$done)
	{
		$window['caption']  = 'New featured listing';
		$window['left'   ]  = '<a href="#" class="menu" onclick="f=document.getElementById(\'add_home_form\'); f.act.value=\'supply_user\'; f.done.value=0; f.submit()">&lt;&lt;&lt;&nbsp;Back</a>&nbsp;|&nbsp;';
		$window['inner'  ]  = '<br /><table width="100%" cellspacing="0" cellpadding="5">'.
						GenerateForm($cfg_home_form, $data, $errors).'</table>';

		$window['inner'  ] .= '<br /><b>Taskbar settings</b>&nbsp;<span style="color:red">(leave blank if you want to use default url value else input url value with "http://" prefix)</span><br />'.
							KRF_ShowToolbarForm($SQL, $url = (is_array($url)) ? $url : NULL);

		$window['inner'  ] .= <<<BUTTONS
			<hr size="1" width="100%" />
			<table width="100%" cellspacing="0" cellpadding="2">
			<tr>
			<td width="50%" align="left" ><input type="submit" value="Add featured listing" style="width:50%" /></td>
			<td width="50%" align="right"><input type="button" value="Cancel" style="width:50%" onclick="f=document.getElementById('add_home_form'); f.act.value='supply_user'; f.done.value='0'; f.submit()" /></td>
			</tr>
			</table>
BUTTONS;
		
		echo ShowWindow($window);
		
		?></form><?
	}
	else
	{
		echo '<script>document.location.href="'.$main['root.com'].'user/?act=edit_home&id='.$id.'&id_home='.$insId.'&message=Home was successfully added";</script>';
	}
?>