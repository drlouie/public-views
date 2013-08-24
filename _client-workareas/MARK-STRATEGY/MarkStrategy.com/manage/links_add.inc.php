<form action="?" name="add_link_form" id="add_link_form" method="post" enctype="multipart/form-data">
<input type="hidden" name="act" value="add_link" />
<input type="hidden" name="id"  value="<?= $id?>" />
<input type="hidden" name="done" value="1" />
<?
	if (!defined('INNER')) exit;

	if ($done)
	{
		$data = array();
		foreach($link_form as $key => $value)
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
		$is_err = KRF_CheckFormData($link_form, $data, $errors);

		if (!$is_err)
		{
			if (trim($data['ordi']) == '') $data['ordi'] = 0;

			if (!is_numeric($data['ordi']) || $data['ordi'] < 0)
			{
				$is_err = true;
				$errors['ordi'] = 'this field must be numerical, greater than zero';
			}
			else
			{
				$insId = KRF_StoreFormData('user_link', $link_form, $data);
				$SQL->Query("UPDATE user_link SET id_user = $id WHERE id=$insId");
			}
		}
	}
	else
	{
		$data = $errors = NULL;
	}

	if ($is_err || !$done)
	{
		$agent = KRF_getAgent($id, $SQL);

		$window['caption'] = "<a class=\"menu\" href=\"#\" onclick=\"f=document.getElementById('add_link_form'); f.act.value='links_user'; f.done.value='0'; f.submit()\" >&lt;&lt;&lt;&nbsp;Back</a>&nbsp;|&nbsp;".
				'New link for '."<b>{$agent['fname']} {$agent['mname']} {$agent['lname']}</b>";
		//$window['menu'   ] = "<a class=\"menu\" href=\"#\" onclick=\"f=document.getElementById('add_user_form'); f.act.value='users'; f.done.value='0'; f.submit()\" >&lt;&lt;&lt;&nbsp;Back</a>";
		$window['inner'  ] = '<br /><span style="color:red">'.$message.'</span><br /><table width="100%" cellspacing="0" cellpadding="5">'.
						GenerateForm($link_form, $data, $errors).'</table>';

		$window['inner'  ] .= <<<BUTTONS
			<hr width="100%" size="1"  />
			<table width="100%" cellspacing="0" cellpadding="2">
			<tr>
			<td width="50%" align="left"><input type="submit" value="Add link" style="width:50%" /></td>
			<td width="50%" align="right" ><input type="button" value="Cancel" style="width:50%" onclick="f=document.getElementById('add_link_form'); f.act.value='links_user'; f.done.value='0'; f.submit()" /></td>
			</tr>
			</table>
BUTTONS;
		
		echo ShowWindow($window);
		
		?></form><?
	}
	else
	{
		echo '<script>document.location.href="'.$main['root.com'].'manage/?act=edit_link&id='.$id.'&id_link='.$insId.'&message=Link successfully added";</script>';
	}
?>