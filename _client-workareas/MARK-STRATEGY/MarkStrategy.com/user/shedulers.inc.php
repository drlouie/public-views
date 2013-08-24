<form id="shedules_form" action="?" method="post">
<input type="hidden" name="act"  value="" />
<input type="hidden" name="todo" value="" />
<?
	if (!defined('INNER')) exit;

	if ($todo == 'del')
	{
		foreach($shedule as $sId => $v)
		{
			if ($v)
			{
				$SQL->Query("DELETE FROM shedule WHERE id=$sId AND id_user=$id");
				//echo "DELETE FROM shedule WHERE id=$sId AND id_user=$id<br />";
			}
		}
	}

	$window['caption'] = 'Schedules'.
		'&nbsp;|&nbsp;<a class="menu" target="_blank" href="?act=shedules_csv&mode=csv">Get data in CSV</a>'.
		'&nbsp;|&nbsp;<a class="menu" target="_blank" href="?act=shedules_txt&mode=csv">Get data in text</a>';
	$window['inner'  ] = KRF_showShedulers($id, $SQL);

	echo ShowWindow($window);
?>
</form>