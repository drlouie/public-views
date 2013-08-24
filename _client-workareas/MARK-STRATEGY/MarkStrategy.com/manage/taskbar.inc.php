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
		$errmsg = array();
		foreach($caption as $tId => $c)
		{
			$caption[$tId] = $c = trim($c);
			$url[$tId] = $u = trim($url[$tId]);

			if ($u === '')
			{
				$is_err = true;
				$errmsg[$tId]['url'] = '(required)';
			}

			if ($c === '')
			{
				$is_err = true;
				$errmsg[$tId]['caption'] = '(required)';
			}
		}

		if (!$is_err)
		{
			foreach($caption as $tId => $c)
			{
				$u = $url[$tId];

				$SQL->Query("UPDATE taskbar SET caption='$c', url='$u' WHERE id = $tId");
			}
		}
	}

	
	if (!$done || $is_err)
	{
		$ret = '<br /><table width="100%">';
		$db = $SQL->Query("SELECT id,caption,url FROM taskbar");
		for($i=0; $i<$SQL->Numrows($db); $i++)
		{
			list($tId, $tCap, $tUrl) = $SQL->Fetchrow($db);

			$cap = ($caption[$tId]) ? $caption[$tId] : $tCap;
			$u   = ($url[$tId]) ? $url[$tId] : $tUrl;

			$red_c = ($is_err && $errmsg[$tId]['caption']) ? $errmsg[$tId]['caption'] : '(required)';
			$red_u = ($is_err && $errmsg[$tId]['url'    ]) ? $errmsg[$tId]['url'    ] : '(required)';

			$red_c = '';
			$n = $i+1;

	        $ret .= <<<ITEM
    		    <tr><td valign="center"><nobr>&nbsp;$n.&nbsp;</nobr></td><td width="100%">
		        <fieldset>
        		<table width="100%">
		        <tr><td><nobr>Caption: </nobr></td>
        			<td width="100%" align="left">
        				<b>$cap</b>
        				<input type="hidden" value="$cap" name="caption[$tId]" style="width:100%" />
        			</td>
		        	<td><nobr><span style="color:red">$red_c</span></nobr></td></tr>
        		<tr><td><nobr>URL: </nobr></td>
		        	<td width="100%"><input type="text" value="$u" name="url[$tId]" style="width:100%" /></td>
        			<td><nobr><span style="color:red">$red_u</span></nobr></td></tr></table>
		        </fieldset></td></tr>
        		<tr><td colspan="2">&nbsp;</td></tr>
ITEM;
		}
		$ret .= <<<END
			</table><br />
			<input type="submit" value="Save changes" /><br />
END;


		$window['caption'] = 'Toolbar settings';
		$window['inner'  ] = $ret;

		echo ShowWindow($window);
	}
	else
	{
		echo '<script>document.location.href="'.$main['root.com'].'manage";</script>';
	}
?>
</form>