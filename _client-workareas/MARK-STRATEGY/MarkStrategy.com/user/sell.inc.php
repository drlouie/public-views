<form action="?" name="sellings_form" id="sellings_form" method="post">
<input type="hidden" name="act" value="sell" />
<input type="hidden" name="todo" value="" />
<input type="hidden" name="mode" value="" />
<?
	if (!defined('INNER')) exit;
	
	if ($todo == 'del')
	{
		foreach($sell as $sId => $v)
		{
			if ($v)
			{
				$SQL->Query("DELETE FROM selling WHERE id=$sId");
			}
		}
	}
	
	$window['caption'] = 'Sellers'.
		'&nbsp;|&nbsp;<a class=\'menu\' href="#" onclick="f=document.getElementById(\'sellings_form\'); f.act.value = \'sell_csv\'; f.target=\'_blank\'; f.mode.value=\'csv\'; f.submit(); f.target=\'\'; f.mode.value=\'\';">Get data in CSV</a>'.
		'&nbsp;|&nbsp;<a class=\'menu\' href="#" onclick="f=document.getElementById(\'sellings_form\'); f.act.value = \'sell_txt\'; f.target=\'_blank\'; f.mode.value=\'csv\'; f.submit(); f.target=\'\'; f.mode.value=\'\';">Get data in text</a>';
	$window['inner'  ] = '<br />'.KRF_showSellings($id, $SQL);

	echo ShowWindow($window);
?>
</form>