<form action="?" name="edit_user_form" id="add_user_form" method="post" enctype="multipart/form-data">
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

				$SQL->Query("DELETE FROM user_banner WHERE id_user = $id");
				$SQL->Query("INSERT INTO user_banner VALUES ($id, $id_banner)");

				$message = 'All data successfully saved';
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
			
			if ($mktime = $data['ttl'])
			{
				$data['ttl'] = array();
				$data['ttl']['day'  ] = date('j', $mktime);
				$data['ttl']['month'] = date('n', $mktime);
				$data['ttl']['year' ] = date('Y', $mktime);
			}
			else
			{
			    $data['ttl']['day'] = $data['ttl']['month'] = $data['ttl']['year'] = '';
			}

		}
		else $terminate = true;
		
		$errors = NULL;
	}

	if ($done)
	{
		$mktime = $data['ttl'];
		$data['ttl'] = array();
		$data['ttl']['day'  ] = date('j', $mktime);
		$data['ttl']['month'] = date('n', $mktime);
		$data['ttl']['year' ] = date('Y', $mktime);

		//var_dump($data);
	}
	

	/*if (($is_err || !$done)&&(!$terminate))
	{*/
		$db = $SQL->Query("SELECT logo, photo FROM user WHERE id=$id");
		list($logo, $photo) = $SQL->Fetchrow($db);
		
		if ($logo)
		{
			$data['logo']['view'] = $main['files']['logo'].$id.'.'.$logo;
		}

		if ($photo)
		{
			$data['photo']['view'] = $main['files']['photo'].$id.'.'.$photo;
		}
		
		$window['caption'] = 'Account information';
		$window['left'   ] = "<a class=\"menu\" href=\"#\" onclick=\"f=document.getElementById('add_user_form'); f.act.value='users'; f.done.value='0'; f.submit()\" >&lt;&lt;&lt;&nbsp;Back</a>&nbsp;|&nbsp;";
		$window['inner'  ] = '<br /><span style="color:red">'.$message.'</span><br /><table width="100%" cellspacing="0" cellpadding="5">'.
						GenerateForm($user_form, $data, $errors).'</table>';

		$window['inner'  ] .= '<table><td>Banner: </td><td><select name="id_banner">';
        
        $cur = $SQL->Query("SELECT id_banner FROM user_banner WHERE id_user=$id");
        if($cur && $SQL->Numrows($db))
        {
        	list($cur_id) = $SQL->Fetchrow($cur);
        }
        else $cur_is = 0;

        $db  = $SQL->Query("SELECT id,name FROM banner");
        for($i=0; $i<$SQL->Numrows($db); $i++)
        {
        	list($id_b, $name) = $SQL->Fetchrow($db);
        	$sel = ($id_b == $cur_id) ? 'selected' : '';
        	$window['inner'] .= "<option value=\"$id_b\" $sel>$name</option>";
        }
        $window['inner'] .= '</select></td></tr></table>';

		$window['inner'  ] .= <<<BUTTONS
			<hr size="1"  width="100%" />
			<table width="100%" cellspacing="0" cellpadding="2">
			<tr>
			<td width="50%" align="left"><input type="submit" value="Save changes" style="width:50%" /></td>
			<td width="50%" align="right" ><input type="button" value="Cancel" style="width:50%" onclick="f=document.getElementById('add_user_form'); f.act.value='users'; f.done.value='0'; f.submit()" /></td>
			</tr>
			</table>
BUTTONS;
		
		echo ShowWindow($window);
		
		?></form><?
	/*}
	else
	{
		echo '<script>document.location.href="'.$main['root.com'].'manage";</script>';
	}*/
?>


