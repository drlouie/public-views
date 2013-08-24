<form action="?" name="edit_link_form" id="edit_link_form" method="post" enctype="multipart/form-data">
<input type="hidden" name="act" value="edit_link" />
<input type="hidden" name="id_link" value="<?= $id_link?>" />
<input type="hidden" name="id" value="" />
<input type="hidden" name="done" value="1" />
<?
	if (!defined('INNER')) exit;

	$data = array();
	$id = $uId;

	if ($done)
	{
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
		$link_form['url']['empty'] = true;
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
				KRF_UpdateFormData('user_link', $link_form, $data, $id_link);
                $message = 'All data successfully saved';
            }
		}
	}
	else
	{
		$terminate = false;
		$fields = array();
		
		foreach($link_form as $key => $value)
		{
			if ($value['field'])
				$fields[$key] = $value['field'];
		}
		
		$db = $SQL->Query("SELECT title, url, intro, ordi, link_picture 
						FROM user_link WHERE id=$id_link");
		
		if ($db && $SQL->Numrows($db))
		{
			list($data['title'], $data['url'], $data['intro'], $data['ordi'], $ext) = $SQL->Fetchrow($db);
		}
		else $terminate = true;
		
		$errors = NULL;
	}
	
	/*if (($is_err || !$done)&&(!$terminate))
	{*/
		$link_form['url']['empty'] = true;
		$data['link_picture']['view'] = $main['files']['link_picture'].$id_link.'.'.$ext;
		
		$window['caption'] = 'Change link';
		$window['left'   ] = "<a class=\"menu\" href=\"#\" onclick=\"f=document.getElementById('edit_link_form'); f.act.value='links_user'; f.done.value='0'; f.submit()\" >&lt;&lt;&lt;&nbsp;Back</a>&nbsp;|&nbsp;";
		$window['inner'  ] = '<br /><span style="color:red">'.$message.'</span><br /><table width="100%" cellspacing="0" cellpadding="5">'.
						GenerateForm($link_form, $data, $errors).'</table>';
		$window['inner'  ] .= <<<BUTTONS
			<hr size="1"  width="100%" />
			<table width="100%" cellspacing="0" cellpadding="2">
			<tr>
			<td width="50%" align="left"><input type="submit" value="Save changes" style="width:50%" /></td>
			<td width="50%" align="right" ><input type="button" value="Cancel" style="width:50%" onclick="f=document.getElementById('edit_link_form'); f.act.value='links_user'; f.done.value='0'; f.submit()" /></td>
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