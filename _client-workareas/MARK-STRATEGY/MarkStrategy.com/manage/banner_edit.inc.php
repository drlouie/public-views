<form action="?" name="edit_banner_form" id="edit_banner_form" method="post" enctype="multipart/form-data">
<input type="hidden" name="act" value="banner_edit" />
<input type="hidden" name="id_banner" value="<?= $id_banner;?>" />
<input type="hidden" name="done" value="1" />
<?
	if (!defined('INNER')) exit;

	$data = array();
	if ($done)
	{
		foreach($banner_form as $key => $value)
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
		$is_err = KRF_CheckFormData($banner_form, $data, $errors);
		if (!$is_err)
		{
			$is_err = KRF_CheckBannerData($data, $errors, $SQL, $id_banner);
		}

		if (!$is_err)
		{
			KRF_UpdateFormData('banner', $banner_form, $data, $id_banner);

			$message = 'All data successfully saved';
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
		
		$db = $SQL->Query("SELECT name, banner FROM banner WHERE id=$id_banner");
		
		if ($db && $SQL->Numrows($db))
		{
			list($data['name'], $ext) = $SQL->Fetchrow($db);
		}
		else $terminate = true;
		
		$errors = NULL;
	}
	
	/*if (($is_err || !$done)&&(!$terminate))
	{*/
		$data['banner']['view'] = $main['files']['banner'].$id_banner.'.'.$ext;
				
		$window['caption'] = 'Change banner';
		$window['left'   ] = "<a class=\"menu\" href=\"#\" onclick=\"f=document.getElementById('edit_banner_form'); f.act.value='banner_lst'; f.done.value='0'; f.submit()\" >&lt;&lt;&lt;&nbsp;Back</a>&nbsp;|&nbsp;";
		$window['inner'  ] = '<br /><span style="color:red">'.$message.'</span><br /><table width="100%" cellspacing="0" cellpadding="5">'.
						GenerateForm($banner_form, $data, $errors).'</table>';
		$window['inner'  ] .= <<<BUTTONS
			<hr size="1"  width="100%" />
			<table width="100%" cellspacing="0" cellpadding="2">
			<tr>
			<td width="50%" align="left"><input type="submit" value="Save changes" style="width:50%" /></td>
			<td width="50%" align="right" ><input type="button" value="Cancel" style="width:50%" onclick="f=document.getElementById('edit_banner_form'); f.act.value='banner_lst'; f.done.value='0'; f.submit()" /></td>
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


