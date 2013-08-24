<form id="homes_form" method="post" action="?" />
<input type="hidden" name="act" value="" />
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

	$window['caption']  = 'Featured home listings';
	$window['caption'] .= '&nbsp;|&nbsp;<a href="#" class="menu" onclick="f=document.getElementById(\'homes_form\'); f.act.value=\'add_home\'; f.submit();">Add featured listing</a>';
    $window['inner'  ]  = KRF_ShowHomes($uId, $show_fields, $cfg_home_form, $SQL);

    echo ShowWindow($window);
?>
