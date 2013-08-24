<form action="?" method="post" id="taskbar_form">
<input type="hidden" name="act" value="taskbar"  />
<input type="hidden" name="done" value="1"  />
<?
	if (!defined('INNER')) exit;

	$is_err = false;

	if (!is_array($url)) $url = array();
	if (!is_array($caption)) $caption = array();

	if ($done)
	{
		KRF_StoreTaskbarSettings($id, $uurl, $SQL);
	}

	
	if (!$done || $is_err)
	{
		$window['inner'  ] = '<br />'.
							KRF_ShowTaskbarForm($SQL, $uurl = (is_array($uurl)) ? $uurl : NULL, $id);
		
		$window['inner'  ] .=  <<<END
			<br /><hr size="1" width="100%" /><br />
			<input type="submit" value="Save changes" /><br />
END;


		$window['caption'] = 'Toolbar settings &nbsp;<span style="color:red">(leave blank if you want to use default url value else input url value with "http://" prefix)</span>';

		echo ShowWindow($window);
	}
	else
	{
		echo '<script>document.location.href="'.$main['root.com'].'user";</script>';
	}
?>
</form>