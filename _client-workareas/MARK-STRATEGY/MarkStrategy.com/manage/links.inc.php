<form id="links_form" method="post" action="?" />
<input type="hidden" name="act" value="" />
<input type="hidden" name="mode" value="" />
<input type="hidden" name="id"  value="<?= $id?>" />
<input type="hidden" name="id_link"  value="" />
<?
	if (!defined('INNER')) exit;

	
	if ($act == 'delete_link')
	{
		if (is_array($link))
		{
			foreach($link as $k => $d)
			{
				if($d)
				{
					$db = $SQL->Query("SELECT link_picture FROM user_link WHERE id=$k");
					if ($db && $SQL->Numrows($db))
					{
						list($ext) = $SQL->Fetchrow($db);
			
						@unlink($main['files']['link_picture'].$k.'.'.$ext);
						$SQL->Query("DELETE FROM user_link WHERE id = $k");
					}
				}
			}
		}
	}

	$agent = KRF_getAgent($id, $SQL);
	
	$window['caption']  = "Links list for <b>{$agent['fname']} {$agent['mname']} {$agent['lname']}</b>";
	$window['caption'] .= '&nbsp;|&nbsp;<a href="#" class="menu" onclick="f=document.getElementById(\'links_form\'); f.act.value=\'add_link\'; f.submit();">Add link</a>';
	//$window['caption'] .= '&nbsp;|&nbsp;<a href="#" class="menu" onclick="f=document.getElementById(\'homes_form\'); f.act.value=\'homes_csv\'; f.mode.value=\'csv\'; f.target=\'_blank\'; f.submit();">Get features listings in CSV</a>';
    $window['inner'  ] = KRF_showLinks($SQL, $id);
    $window['left'   ] = '<a href="?act=users" class="menu">&lt;&lt;&lt;&nbsp;Back</a>&nbsp;|&nbsp;';

    echo ShowWindow($window);
?>
</form>