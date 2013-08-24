<form action="?" name="add_banner_form" id="add_banner_form" method="post" enctype="multipart/form-data">
<input type="hidden" name="act" value="banner_add" />
<input type="hidden" name="done" value="1" />
<?
	if (!defined('INNER')) exit;

	$banner_form['banner']['empty'] = false;
	if ($done)
	{
		$data = array();
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
			$is_err = KRF_CheckBannerData($data, $errors, $SQL, 0);
		}

		if (!$is_err)
		{
			$insId = KRF_StoreFormData('banner', $banner_form, $data);
			//$SQL->Query("UPDATE banner SET id_user = $id WHERE id=$insId");
		}
	}
	else
	{
		$data = $errors = NULL;
	}

	if ($is_err || !$done)
	{
		$window['caption'] = '<a href="?act=banner_lst" class="menu">&lt;&lt;&lt;&nbsp;Back</a>&nbsp;|&nbsp;New banner';
		$window['inner'  ] = '<br /><table width="100%" cellspacing="0" cellpadding="5">'.
						GenerateForm($banner_form, $data, $errors).'</table>';
		$window['inner'  ] .= <<<BUTTONS
		<hr width="100%" size="1" />
		<table width="100%" cellspacing="0" cellpadding="2">
			<tr>
			<td width="50%" align="left"><input type="submit" value="Add banner" style="width:50%" /></td>
			<td width="50%" align="right" ><input type="button" value="Cancel" style="width:50%" onclick="f=document.getElementById('add_banner_form'); f.act.value='banner_lst'; f.done.value='0'; f.submit()" /></td>
			</tr>
			</table>
BUTTONS;
		
		echo ShowWindow($window);
		?></form><?
	}
	else
	{
		echo '<script>document.location.href="'.$main['root.com'].'manage/?act=banner_lst&id_banner='.$insId.'&message=Banner successfully added";</script>';
	}
?>
</form>