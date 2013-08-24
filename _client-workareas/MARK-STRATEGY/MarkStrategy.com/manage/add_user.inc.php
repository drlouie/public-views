<form action="?" name="add_user_form" id="add_user_form" method="post" enctype="multipart/form-data">
<input type="hidden" name="act" value="add_user" />
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
			$rep = KRF_CheckUserData($data);
			if (!$rep['is_err'])
			{
				$insId = KRF_StoreFormData('user', $user_form, $data);
				$SQL->Query("DELETE FROM user_banner WHERE id_user = $insId");
				$SQL->Query("INSERT INTO user_banner VALUES ($insId, $id_banner)");
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
		$data = $errors = NULL;
	}

	if ($is_err || !$done)
	{
		$window['caption'] = "<a class=\"menu\" href=\"#\" onclick=\"f=document.getElementById('add_user_form'); f.act.value='users'; f.done.value='0'; f.submit()\" >&lt;&lt;&lt;&nbsp;Back</a>&nbsp;|&nbsp;".'New account';
		//$window['menu'   ] = "<a class=\"menu\" href=\"#\" onclick=\"f=document.getElementById('add_user_form'); f.act.value='users'; f.done.value='0'; f.submit()\" >&lt;&lt;&lt;&nbsp;Back</a>";
		$window['inner'  ] = '<br /><table width="100%" cellspacing="0" cellpadding="5">'.
						GenerateForm($user_form, $data, $errors).'</table>';
		$window['inner'  ] = '<br /><span style="color:red">'.$message.'</span><br /><table width="100%" cellspacing="0" cellpadding="5">'.
						GenerateForm($user_form, $data, $errors).'</table>';

		$window['inner'  ] .= '<table><td>Banner: </td><td><select name="id_banner">';
        
        $db  = $SQL->Query("SELECT id,name FROM banner");
        for($i=0; $i<$SQL->Numrows($db); $i++)
        {
        	list($id_b, $name) = $SQL->Fetchrow($db);
        	$sel = ($id_b == $cur_id) ? 'selected' : '';
        	$window['inner'] .= "<option value=\"$id_b\" $sel>$name</option>";
        }
        $window['inner'] .= '</select></td></tr></table>';

		$window['inner'  ] .= <<<BUTTONS
			<hr width="100%" size="1"  />
			<table width="100%" cellspacing="0" cellpadding="2">
			<tr>
			<td width="50%" align="left"><input type="submit" value="Add account" style="width:50%" /></td>
			<td width="50%" align="right" ><input type="button" value="Cancel" style="width:50%" onclick="f=document.getElementById('add_user_form'); f.act.value='users'; f.done.value='0'; f.submit()" /></td>
			</tr>
			</table>
BUTTONS;
		
		echo ShowWindow($window);
		
		?></form><?
	}
	else
	{
		echo '<script>document.location.href="'.$main['root.com'].'manage/?act=edit_user&id='.$insId.'&message=Agent successfully added";</script>';
	}
?>


