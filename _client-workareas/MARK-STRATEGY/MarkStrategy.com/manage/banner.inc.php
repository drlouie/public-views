<form action="?" name="banner_form" id="banner_form" method="post" enctype="multipart/form-data">
<input type="hidden" name="act" value="banner_lst" />
<input type="hidden" name="todo" value="" />
<?
	if (!defined('INNER')) exit;

	if ($todo == 'del' && is_array($banner))
	{
		foreach($banner as $id_b => $d)
		{
			if ($d)
			{
				$db = $SQL->Query("SELECT banner FROM banner WHERE id=$id_b");
				if ($db && $SQL->Numrows($db))
				{
					list($ext) = $SQL->Fetchrow($db);
					$SQL->Query("DELETE FROM banner WHERE id=$id_b");
					@unlink($main['files']['banner'].$id_b.'.'.$ext);
				}
			}
		}
	}

	$window['caption']  = 'Banners list';
	$window['caption'] .= <<<MENU
	&nbsp;|&nbsp;<a class="menu" href="?act=banner_add">Add banner</a>
MENU;
	$window['inner'  ]  = KRF_showBanners($SQL);
	$window['inner'  ] .= <<<BUTTONS
	<input type="button" value="Delete selected items" onclick="if (window.confirm('Are you sure to delete selected items?')) {f=document.getElementById('banner_form'); f.todo.value='del'; f.submit();}" />
BUTTONS;

	echo ShowWindow($window);
?>
</form>
