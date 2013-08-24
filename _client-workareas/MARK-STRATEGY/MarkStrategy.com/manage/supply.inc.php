<form id="homes_form" method="post" action="?" />
<input type="hidden" name="act" value="" />
<input type="hidden" name="mode" value="" />
<input type="hidden" name="id"  value="<?= $id?>" />
<input type="hidden" name="id_home"  value="" />
<?
	if (!defined('INNER')) exit;

	
	if ($act == 'delete_home')
	{
		if (is_array($del))
		{
			foreach($del as $k => $d)
			{
				if($d)
				{
					$db = $SQL->Query("SELECT home_photo FROM homes WHERE id=$k");
					if ($db && $SQL->Numrows($db))
					{
						list($ext) = $SQL->Fetchrow($db);
			
						@unlink($main['files']['home_photo'].$k.'.'.$ext);
						$SQL->Query("DELETE FROM homes WHERE id = $k");
						$SQL->Query("DELETE FROM user_toolbar WHERE id_home = $k");
					}
				}
			}
		}
	}

	$agent = KRF_getAgent($id, $SQL);

	
	$window['caption']  = "Featured listings for <b>{$agent['fname']} {$agent['mname']} {$agent['lname']}</b>";
	$window['caption'] .= '&nbsp;|&nbsp;<a href="#" class="menu" onclick="f=document.getElementById(\'homes_form\'); f.act.value=\'add_home\'; f.submit();">Add featured listing</a>';
	//$window['caption'] .= '&nbsp;|&nbsp;<a href="#" class="menu" onclick="f=document.getElementById(\'homes_form\'); f.act.value=\'homes_csv\'; f.mode.value=\'csv\'; f.target=\'_blank\'; f.submit();">Get features listings in CSV</a>';

    $window['inner'  ] = KRF_ShowHomes($id, $show_fields, $cfg_home_form, $SQL);
    $window['inner'] = str_replace('\"', '"', $window['inner']);

    $window['left'   ] = '<a href="?act=users" class="menu">&lt;&lt;&lt;&nbsp;Back</a>&nbsp;|&nbsp;';



    echo ShowWindow($window);


?>
</form>
