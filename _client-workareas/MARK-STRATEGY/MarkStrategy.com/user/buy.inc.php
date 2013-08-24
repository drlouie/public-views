<form action="?" name="buyings_form" id="buyings_form" method="post">
<input type="hidden" name="act" value="buy" />
<input type="hidden" name="todo" value="" />
<input type="hidden" name="mode" value="" />
<?
	if (!defined('INNER')) exit;
	
	if ($todo == 'del')
	{
		foreach($buy as $bId => $v)
		{
			if ($v)
			{
				$SQL->Query("DELETE FROM buying WHERE id=$bId");
			}
		}
	}
	
	$window['caption'] = 'Buyers'.
		'&nbsp;|&nbsp;<a class=\'menu\' href="#" onclick="f=document.getElementById(\'buyings_form\'); f.act.value = \'buy_csv\'; f.target=\'_blank\'; f.mode.value=\'csv\'; f.submit(); f.target=\'\'; f.mode.value=\'\';">Get data in CSV</a>'.
		'&nbsp;|&nbsp;<a class=\'menu\' href="#" onclick="f=document.getElementById(\'buyings_form\'); f.act.value = \'buy_txt\'; f.target=\'_blank\'; f.mode.value=\'csv\'; f.submit(); f.target=\'\'; f.mode.value=\'\';">Get data in text</a>';
	$window['inner'  ] = '<br />'.KRF_showBuyings($id, $SQL);

	echo ShowWindow($window);
?>
</form>