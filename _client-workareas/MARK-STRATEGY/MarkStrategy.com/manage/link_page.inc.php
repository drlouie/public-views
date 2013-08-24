<form action="?" name="link_page_form" id="link_page_form" method="post">
<input type="hidden" name="act" value="link_page" />
<input type="hidden" name="done" value="1" />
<?
	if (!defined('INNER')) exit;
     	

	$db = $SQL->Query('SELECT source FROM link_page LIMIT 0,1');
	if (!$db || !$SQL->Numrows($db))
	{
		$SQL->Query("INSERT INTO link_page VALUES ('')");

		$db_s = '';
	}
	else
	{
		list($db_s) = $SQL->Fetchrow($db);
	}

	$source = (!$done) ? $db_s : addslashes(trim($source));

	if ($done)
	{
		$SQL->Query("UPDATE link_page SET source = '$source'");
	}
	
	if (!$done)
	{
		$source = stripslashes($source);
		$form = <<<FORM
			<br />
			<table width="100%">
			<tr><td width="100%">Page source</td></tr>
			<tr><td width="10%">
			<textarea style="width:100%" rows="50" name="source">$source</textarea>
			</td></tr></table>
FORM;
		
		$window['caption'] = 'Links page';
		$window['inner'  ] = $form;
		$window['inner'  ] .= <<<BUTTONS
		<br />
		<input type="submit" value="Save changes" />
BUTTONS;

		echo ShowWindow($window);
	}
	else
	{
		echo '<script>document.location.href="'.$main['root.com'].'manage";</script>';
	}
?>
</form>