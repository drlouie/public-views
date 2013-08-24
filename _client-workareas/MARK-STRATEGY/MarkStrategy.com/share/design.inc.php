<?
	if (!defined('INNER')) exit;

	function KRF_showLinks(&$SQL, $id_user)
	{
		global $main;

		$db = $SQL->Query("SELECT id, ordi, title, url, intro, link_picture
						FROM user_link WHERE id_user=$id_user ORDER BY ordi");
		if (!$db || !($cnt = $SQL->Numrows($db))) 
		{
			$ret = <<<EMPTY
        	<table width="100%"><tr><td width="100%" align="center">
        	The list of links is empty!
        	</td></tr></table>
EMPTY;
			return $ret;
		}

        $ret = '<table width="100%">';
        $num = 0;
        for ($i=0; $i<$cnt; $i++)
        {
			list ($id, $ordi, $title, $url, $intro, $ext) = $SQL->Fetchrow($db);
			
			if (!$ordi) $ordi = 0;

			$img = (file_exists("{$main['files']['link_picture']}$id.$ext")) ? "<img src=\"{$main['files']['link_picture']}$id.$ext\" />" : "";

			$ret .= <<<ITEM
				<tr><td colspan="3">
				<b>$ordi</b>&nbsp;<input class="check" type="checkbox" name="link[$id]" value="1" onclick="d=document.getElementById('n$id'); d.className=(d.className == 'tbold') ? 'tnorm' : 'tbold';" />&nbsp;
				<span class="tnorm" id="n$id">
					<a href="#" onclick="f=document.getElementById('links_form'); f.act.value='edit_link'; f.action='?'; f.id_link.value='$id'; f.submit();">$title</a>
					&nbsp;&nbsp;
					<a href="$url"> $url </a>
				</span>
				</td></tr>
				<tr><td valign="top">$img</td><td width="5">&nbsp;</td>
				<td valign="top" align="left" width="100%">$intro</td></tr>
				<tr><td colspan="3" width="100%"><hr size="1" width="100%" /></td></tr>
ITEM;
        }
        $ret .= '</table>';

		$ret .= "<input type=\"button\" value=\"Delete selected links\"  onclick=\"if (window.confirm('Are you sure to delete selected links?')) {f=document.getElementById('links_form'); f.act.value='delete_link'; f.submit();}\" /></td>";
        return $ret;
	}
	
	function KRF_showBanners(&$SQL)
	{
		global $main;
		$db  = $SQL->Query('SELECT count(id) FROM banner');

		if ($db) list($cnt) = $SQL->Fetchrow($db);
		else $cnt = 0;
        
        if (!$cnt)
        {
        	$ret = <<<EMPTY
        	<table width="100%"><tr><td width="100%" align="center">
        	The list of banners is empty!
        	</td></tr></table>
EMPTY;
			return $ret;
        }

        $ret = '<table width="100%">';
        $db  = $SQL->Query('SELECT id, name, banner FROM banner');
        for ($i=0; $i<$cnt; $i++)
        {
			list ($id, $name, $ext) = $SQL->Fetchrow($db);
			$check = '';
			if ($i > 0)
			{
				$check = <<<CHECK
					<input class="check" type="checkbox" name="banner[$id]" value="1" onclick="d=document.getElementById('n$id'); d.className=(d.className == 'tbold') ? 'tnorm' : 'tbold';" />
CHECK;
			}
			$ret .= <<<ITEM
				<tr><td>
				$check&nbsp;
				<span class="tnorm" id="n$id"><a href="?act=banner_edit&id_banner=$id"> $name </a></span>
				</td></tr>
				<tr><td width="100%"><img src="{$main['files']['banner']}$id.$ext" width="600" /></td></tr>
				<tr><td width="100%"><hr size="1" width="100%" /></td></tr>
ITEM;
        }
        $ret .= '</table>';
        return $ret;
	}
	
	function KRF_showBuyings($id, &$SQL)
	{
		$db  = $SQL->Query("SELECT count(id) FROM buying WHERE id_user = $id");
		list($cnt) = $SQL->Fetchrow($db);

		if (!$cnt) return <<<EMPTY
		<table width="100%"><tr><td width="100%">There are not sellings</td></tr></table>
EMPTY;
		
		$db = $SQL->Query("SELECT id,
							post_date,
							fname,
							lname,
							email,
							type,
							price_min,
							price_max,
							bedr,
							bathr,
							square,
							soon,
							city_desired,
							phone,
							address,
							city,
							state,
							zip,
							notes
						FROM buying
						WHERE id_user = $id
						ORDER BY post_date");
		$ret = '<table width="100%">';
		for ($i=0; $i<$cnt; $i++)
		{
			list($bId, $post_date, $fname, $lname, $email, $type, $price_min, $price_max,
			$bedr, $bathr, $square, $soon, $city_desired, $phone,
			$addr, $city, $state, $zip, $notes) = $SQL->Fetchrow($db);

			$date = date('F j, Y, g:i a', $post_date);
			$notes = strip_tags($notes);

			$ret .= <<<ITEM
				<tr><td valign="middle"><input class="check" type="checkbox" name="buy[$bId]" value="1" onclick="s=document.getElementById('d$bId'); s.className = (s.className == 'tnorm') ? 'tbold' : 'tnorm';" /><nobr><span class="tnorm" id="d$bId">&nbsp;$date&nbsp;</span></nobr></td>
				<td width="47%" valign="top">
				<fieldset style="height:100%"><legend>Client info</legend>
				<table width="100%">
					<tr><td><nobr>Name: </nobr></td><td width="100%"><b>$fname $lname</b></td></tr>
					<tr><td><nobr>E-mail: </nobr></td><td width="100%"><b>$email</b></td></tr>
					<tr><td><nobr>Phone: </nobr></td><td width="100%"><b>$phone</b></td></tr>
					<!--<tr><td><nobr>Address: </nobr></td><td width="100%"><b>$addr, $city, $state $zip</b></td></tr>-->
					<tr><td><nobr>Notes: </nobr></td><td width="100%"><b>$notes</b></td></tr>
				</table>
				</fieldset></td><td width="5">&nbsp;</td>
				<td width="47%" height="100%" valign="top">
				<fieldset style="height:100%"><legend>Property info</legend>
				<table width="100%">
					<tr><td><nobr>Type: </nobr></td><td width="100%"><b>$type</b></td></tr>
					<tr><td><nobr>Bedrooms: </nobr></td><td width="100%"><b>$bedr</b></td></tr>
					<tr><td><nobr>Bathrooms: </nobr></td><td width="100%"><b>$bathr</b></td></tr>
					<tr><td><nobr>Square: </nobr></td><td width="100%"><b>$square</b></td></tr>
					<tr><td><nobr>City desired: </nobr></td><td width="100%"><b>$city_desired</b></td></tr>
					<tr><td colspan="2">Price from <b>$price_min</b> to <b>$price_max</b></td></tr>
					<tr><td colspan="2">How soon are looking to buy: <b>$soon</b></td></tr>
				</table>
				</fieldset>
				</td></tr><tr><td colspan="4"><hr size="1" width="100%" /></td></tr>
ITEM;
		}
		$ret .= '</table>';
		$ret .= <<<BUTTONS
		<br />
		<input type="button" value="Delete selected items" onclick="if(window.confirm('Are you sure to delete selected items?')) {f=document.getElementById('buyings_form');f.act.value='buy';f.todo.value='del';f.submit();}" />
BUTTONS;

		return $ret;
	}
	
	
	function KRF_showSellings($id, &$SQL)
	{
		$db  = $SQL->Query("SELECT count(id) FROM selling WHERE id_user = $id");
		list($cnt) = $SQL->Fetchrow($db);

		if (!$cnt) return <<<EMPTY
		<table width="100%"><tr><td width="100%">There are not sellings</td></tr></table>
EMPTY;
		
		$db = $SQL->Query("SELECT id,
							post_date,
							fname,
							lname,
							email,
							type,
							price,
							bedr,
							bathr,
							square,
							home_address,
							home_city,
							home_state,
							home_zip,
							client_phone,
							client_address,
							client_city,
							client_state,
							client_zip,
							notes
						FROM selling
						WHERE id_user = $id
						ORDER BY post_date");
		$ret = '<table width="100%">';
		for ($i=0; $i<$cnt; $i++)
		{
			list($sId, $post_date, $fname, $lname, $email, $type, $price, $bedr, $bathr,
			$square, $h_addr, $h_city, $h_state, $h_zip,
			$c_phone, $c_addr, $c_city, $c_state, $c_zip, $notes) = $SQL->Fetchrow($db);

			$date = date('F j, Y, g:i a', $post_date);
			$notes = strip_tags($notes);

			$ret .= <<<ITEM
				<tr><td valign="middle"><input class="check" type="checkbox" name="sell[$sId]" value="1" onclick="s=document.getElementById('d$sId'); s.className = (s.className == 'tnorm') ? 'tbold' : 'tnorm';" /><nobr><span class="tnorm" id="d$sId">&nbsp;$date&nbsp;</span></nobr></td>
				<td width="47%" valign="top">
				<fieldset style="height:100%"><legend>Client info</legend>
				<table width="100%">
					<tr><td><nobr>Name: </nobr></td><td width="100%"><b>$fname $lname</b></td></tr>
					<tr><td><nobr>E-mail: </nobr></td><td width="100%"><b>$email</b></td></tr>
					<tr><td><nobr>Phone: </nobr></td><td width="100%"><b>$c_phone</b></td></tr>
					<!--<tr><td><nobr>Address: </nobr></td><td width="100%"><b>$c_addr, $c_city, $c_state $c_zip</b></td></tr>-->
					<tr><td><nobr>Notes: </nobr></td><td width="100%"><b>$notes</b></td></tr>
				</table>
				</fieldset></td><td width="5">&nbsp;</td>
				<td width="47%" height="100%" valign="top">
				<fieldset style="height:100%"><legend>Property info</legend>
				<table width="100%%">
					<tr><td><nobr>Type: </nobr></td><td width="100%"><b>$type</b></td></tr>
					<tr><td><nobr>Price: </nobr></td><td width="100%"><b>$price</b></td></tr>
					<tr><td><nobr>Bedrooms: </nobr></td><td width="100%"><b>$bedr</b></td></tr>
					<tr><td><nobr>Bathrooms: </nobr></td><td width="100%"><b>$bathr</b></td></tr>
					<tr><td><nobr>Square: </nobr></td><td width="100%"><b>$square</b></td></tr>
					<tr><td><nobr>Address: </nobr></td><td width="100%"><b>$h_addr, $h_city, $h_state $h_zip</b></td></tr>
				</table>
				</fieldset>
				</td></tr><tr><td colspan="4"><hr size="1" width="100%" /></td></tr>
ITEM;
		}
		$ret .= '</table>';
		$ret .= <<<BUTTONS
		<br />
		<input type="button" value="Delete selected items" onclick="if(window.confirm('Are you sure to delete selected items?')) {f=document.getElementById('sellings_form');f.act.value='sell';f.todo.value='del';f.submit();}" />
BUTTONS;

		return $ret;
	}
	
	function KRF_showShedulers($id, &$SQL)
	{
		global $main;

		$db = $SQL->Query("SELECT s.id, s.id_home, 
							s.name, s.email, s.phone,
							s.date_pref, s.date_alt,
							s.notes, 
							h.address, h.city, h.state, h.zip, h.home_photo
						FROM shedule AS s
						LEFT JOIN homes AS h
						ON h.id = s.id_home
						WHERE s.id_user = $id
						ORDER BY s.date_pref, s.date_alt");
        $ret = '<table>';
		for ($i=0; $i<$SQL->Numrows($db); $i++)
		{
			list($sId, $id_home, $name, $email, $phone, $d1, $d2, 
				$notes, $addr, $city, $state, $zip, $photo) = $SQL->Fetchrow($db);
			if ($d1)
			{
				$d1 = '<tr><td>Preferred Date: </td><td><b>'.date('F j, Y, g:i a', $d1).'</b></td></tr>'; 
			}
			else
			{
				$d1 = '';
			}

			if ($d2)
			{
				$d2 = '<tr><td>Alternate Date: </td><td><b>'.date('F j, Y, g:i a', $d2).'</b></td></tr>'; 
			}
			else
			{
				$d2 = '';
			}

			if ($notes)
			{
				$comments = "<tr><td>Comments :</td><td><b>$notes</b></td></tr>";
			}
			else
			{
				$comments = '';
			}
			$ret .= <<<ITEM
			<tr><td valign="middle"><input class="check" type="checkbox" name="shedule[$sId]" value="1" />&nbsp;</td>
			<td><img src="{$main['files']['home_photo']}$id_home.$photo" /><br />
			$addr, $city, $state $zip
			</td>
			<td width="5">&nbsp;</td>
			<td valign="middle" align="left">
			<table>
			$d1
			$d2
			<tr><td>Client name :</td><td><b>$name</b></td></tr>
			<tr><td>Client email:</td><td><b>$email</b></td></tr>
			<tr><td>Client phone:</td><td><b>$phone</b></td></tr>
			$comments
			</table>
			</td>
			</tr>
ITEM;
		}

		if (!$i)
		{
			$ret .= '<tr><td width="100%" align="center">There is a no schedules</td></tr>';
		}
		$ret .= '</table>';

		if($i)
		{
			$ret .= <<<BUTTONS
				<br /><hr size="1"	width="100%" /><br />
				<input type="button" value="Delete selected items" onclick="if (window.confirm('Are you sure to delete selected items?')) {f=document.getElementById('shedules_form'); f.act.value='shedules'; f.todo.value='del'; f.action='?'; f.submit();}" />
BUTTONS;
		}

		return $ret;
	}
	
	function KRF_getAgent($id, &$SQL)
	{
		$db = $SQL->Query("select * from user where id=$id LIMIT 0,1");
        if ($db && $SQL->Numrows($db))
        {
        	return $SQL->Fetcharray($db, 'assoc');
        }

        return NULL;
	}
	
	function KRF_ShowHomes($id, &$form, &$gform, &$SQL)
	{
		global $main;

		$ret = '<table><tr><td></td><td></td><td></td>';
        foreach($form as $v)
        {
        	$ret .= "<td><b>{$gform[$v]['caption']}</b></td>";
        }
        $ret .= '<td></td><td></td></tr>';
        
        $db = $SQL->Query("SELECT id,home_photo,".implode(',', $form)." FROM homes WHERE id_user = $id");
        for($i=0; $i<$SQL->Numrows($db); $i++)
        {
        	$row = $SQL->Fetcharray($db, 'num');
        	$ret .= '<tr><td><input onclick="f=document.getElementById(\'s'.$row[0].'\'); f.className=(f.className==\'tbold\') ? \'tnorm\' : \'tbold\';" class="check" type="checkbox" name="del['.$row[0].']" value="1" /><img src="" alt="" width="5" height="0" border="0" /></td>';
        	
        	$photo = "{$main['files']['home_photo']}{$row[0]}.{$row[1]}";
        	if(!file_exists($photo))
        	{
        		$photo = "{$main['files']['home_photo']}blank_home.jpg";
        	}
        	$ret .= "<td><img src=\"$photo\" border=\"0\" /></td>".'<td><img src="" alt="" width="5" height="0" border="0" /></td>';
			
			$ret .= "<td valign=\"middle\"><a href=\"#\" onclick=\"javascript:f=document.getElementById('homes_form'); f.act.value='edit_home'; f.id_home.value = {$row[0]}; f.submit();\"><span id=\"s{$row[0]}\" class=\"tnorm\">{$row[2]}</span></a>";
        	for($j=3; $j<count($row); $j++)
        	{
        		$ret .= ",</td><td valign=\"middle\">&nbsp;{$row[$j]}";
        	}
        	
        	$ret .= <<<RIGHT
        		</td><td width="20"></td>
RIGHT;
        	$ret .= '</tr>';
        }
        $ret .= '</table>';

        if ($i)
        {
        	$ret .= '<hr size="1" width="100%" />';
        	$ret .= '<input type="button" value="Delete selected homes" onclick="if (window.confirm(\'Are you sure to delete selected homes?\')) {f=document.getElementById(\'homes_form\'); f.act.value=\'delete_home\'; f.submit();}"  />';

        	return $ret;
        }

        $ret = <<<EMPTY
        <table width="100%"><tr><td width="100%" aling="center">No features listings have been added as yet. 
        <a href="?act=add_home&id=$id">Add featured listing</a>
        </td></tr></table>
        
EMPTY;

        return $ret;
	}
	
	function ShowWindow($set)
	{
		$ret = <<<TABLE
			<table width="100%" cellspacing="0" cellpadding="1">
			<tr width="100%" height="30px">
				<td class="{$set['border_class']}"></td>
				<td class="{$set['head_class']}"><img src="" alt="" width="{$set['l_space']}" height="0" /></td>
				<td class="{$set['head_class']}">
					<nobr>{$set['left']}{$set['caption']}</nobr>
				</td>
				<td width="100%" align="right" class="{$set['head_class']}">{$set['menu']}</td>
				<td class="{$set['head_class']}"><img src="" alt="" width="{$set['r_space']}" height="0" /></td>
				<td class="{$set['border_class']}"></td>
			</tr>
			<tr width="100%">
				<td class="{$set['border_class']}"><img src="" alt="" width="{$set['l_line']}" height="0" /></td>
				<td class="{$set['in_class']}"><img src="" alt="" width="{$set['l_space']}" height="0" /></td>
				<td colspan="2" width="100%" valign="middle" class="{$set['in_class']}">{$set['inner']}</td>
				<td class="{$set['in_class']}"><img src="" alt="" width="{$set['r_space']}" height="0" /></td>
				<td class="{$set['border_class']}"><img src="" alt="" width="{$set['r_line']}" height="0" /></td>
			</tr>
			<tr width="100%">
				<td class="{$set['border_class']}"><img src="" alt="" width="{$set['l_line']}" height="0" /></td>
				<td class="{$set['in_class']}" width="100%" colspan="4"><img src="" alt="" width="0" height="{$set['d_space']}" /></td>
				<td class="{$set['border_class']}"><img src="" alt="" width="{$set['r_line']}" height="0" /></td>
			</tr>
			<tr width="100%">
				<td class="{$set['border_class']}" width="100%" colspan="6"><img src="" alt="" width="0" height="{$set['d_line']}" /></td>
			</tr>
			</table>
TABLE;
		return $ret;
	}

	function ShowUsers(&$window)
	{
		global $SQL, $HTTP_HOST;

		$users = <<<BEG
			<br /><table cellspacing="0" cellpaddind="2">
BEG;
	
		$db = $SQL->Query('SELECT id, fname, lname, mname, email, domain 
							FROM user 
							ORDER BY fname, mname, lname');
		
		for ($i=0; $i<$SQL->Numrows($db); $i++)
		{
			list($id, $fname, $lname, $mname, $email, $domain) = $SQL->Fetchrow($db);

			$users .= <<<USER
			<tr><td><input class="check" type="checkbox" name="del[$id]" value="1" border="0" onclick="s = document.getElementById('s$id'); s.className = (s.className == 'tbold') ? 'tnorm' : 'tbold';" /></td><td width="5">&nbsp;</td>
			<td><a href="#" onclick="javascipt:f=document.getElementById('users_list_form'); f.act.value='edit_user'; f.todo.value=''; f.id.value='$id'; f.submit();"><span class="tnorm" id="s$id">$fname  $mname  $lname</span></a></td>
			<td>&nbsp;[<a href="#" onclick="javascipt:f=document.getElementById('users_list_form'); f.act.value='supply_user'; f.todo.value=''; f.id.value='$id'; f.submit();">view featured listings</a>]</td>
			<td>&nbsp;[<a href="#" onclick="javascipt:f=document.getElementById('users_list_form'); f.act.value='links_user'; f.todo.value=''; f.id.value='$id'; f.action='?'; f.submit();">links page</a>]</td>
			<td>&nbsp;[<a href="http://$domain.$HTTP_HOST" target="_blank">go to website</a>]</td>
			<td>&nbsp;[<a href="http://$HTTP_HOST/user/" target="_blank">login as user</a>]</td></tr>
USER;
		}
	
		$del = true;
		if (!$i)
		{
			$del = false;
			$users .= '<tr width="100%"><td align="center" width="100%">List of users is empty</td></tr>';
		}
		$users .= '</table>';
		
		if ($i)
		{
			$users .= "<hr size=\"1\" width=\"100%\" />";
			$users .= "<input type=\"button\" value=\"Delete selected users\"  onclick=\"if (window.confirm('Are you sure to delete selected accounts?')) {f=document.getElementById('users_list_form'); f.act.value='users'; f.todo.value='delete'; f.submit();}\" /></td>";
		}
    
		$window['caption'] = 'Agents';
		$window['inner'  ] = $users;
    
		echo ShowWindow($window);

		return $i;
	}

	function ShowUserMenu($cnt)
	{
		?><br /><table width="100%" cellspacing="0" cellpadding="2" class="head">
		<tr width="100%"><td width="50%"><input style="width:50%" type="button" value="Add account" onclick="f=document.getElementById('users_list_form'); f.act.value='add_user'; f.todo.value=''; f.submit();" /></td><?	
		if ($cnt)
		{
			?><td width="50%" align="right"><input style="width:50%" type="button" value="Delete selected users"  onclick="f=document.getElementById('users_list_form'); f.act.value='users'; f.todo.value='delete'; f.submit();" /></td><?
		}
		else
		{
			?><td width="50%">&nbsp;</td><?
		}

		?></tr></table><?
	}

	function GenerateForm(&$form, $data = NULL, $errors = NULL)
	{
		$f = '';
		if ($data == NULL) $data = array();
		if ($errors == NULL) $errors = array();

		foreach($form as $key => $value)
		{
			
			$err = ($errors[$key]) ? "<nobr><span style=\"color:red\">{$errors[$key]}</span></nobr>" : '';
			if ($value['html_type'] == 'text')
				$data[$key] = stripslashes(strtr($data[$key], array('"' => '&quot;')));
			switch ($value['html_type']) 
			{
    			case 'text':
    			case 'password':
					$style = ($value['size']) ? "size=\"{$value['size']}\"" : "style=\"width:100%\"";
					
					$req   = (!$value['empty']) ? '(required)' : '';
					$req   = ($err == '') ? $req : $err;
					
					$f .= <<<TEXT
						<tr><td><nobr>{$value['caption']}:</nobr></td><td width="80%">
								<input type="{$value['html_type']}" value="{$data[$key]}" name="$key" $style />
							</td><td>$req</td></tr>
TEXT;
		        break;

			    case 'textarea':
					$style  = ($value['rows']) ? " rows=\"{$value['rows']}\"" : '';
					$style .= ($value['cols']) ? " cols=\"{$value['cols']}\"" : " style=\"width:100%\"";

					$req   = (!$value['empty']) ? '(required)' : '';
					$req   = ($err == '') ? $req : $err;

					$f .= "<tr><td colspan=\"2\">{$value['caption']}:</td></tr><tr><td colspan=\"2\">
								<textarea name=\"$key\" $style>".htmlspecialchars($data[$key]).
								"</textarea></td><td>$req</td></tr>";			        
		        break;

			    case 'date':
			    	$f .= "<tr><td>{$value['caption']}:</td><td>";

			    	$req   = (!$value['empty']) ? '(required)' : '';
					$req   = ($err == '') ? $req : $err;
			    	
			    	$f .= <<<DATE
			    	<table>
			    	<tr><td>m.</td><td><input type="text" size="2" value="{$data[$key]['month']}" name="{$key}[month]" /></td><td width="10px"></td>
			    	<td>d.</td><td><input type="text" size="2" value="{$data[$key]['day']}" name="{$key}[day]" /></td><td width="10px"></td>
			    	<td>y.</td><td><input type="text" size="5" value="{$data[$key]['year']}" name="{$key}[year]" /></td><td width="10px"></td>
			    	</table>
DATE;
					
					$f .= '</td><td>'.$req.'</td></tr>';
			    break;
			    case 'select':
			    	$req = (!$value['empty']) ? '(required)' : '';
			    	$opt = '';
			    	foreach($value['values'] as $v)
			    	{
			    		$sel  = ($data[$key] == $v) ? 'selected' : '';
			    		$opt .= "<option value=\"$v\" $sel>$v</option>";
			    	}
					$f .= <<<SELECT
						<tr><td><nobr>{$value['caption']}:</nobr></td><td width="80%">
								<select name="$key">$opt</select>
							</td><td>$req</td></tr>
SELECT;

			    break;
			    case 'file':
			    	$style = ($value['size']) ? "size=\"{$value['size']}\"" : 'style="width:100%"';
					
					$req   = (!$value['empty']) ? '(required)' : '';
					$req   = ($err == '') ? $req : $err;

					$file = '';
					if ($data[$key]['view'])
					{
						$width  = ($value['width' ]) ? 'width ="'.$value['width' ].'"' : '';
						$height = ($value['height']) ? 'height="'.$value['height'].'"' : '';
						$file = "<img $width $height src=\"{$data[$key]['view']}\" border=\"0\" />";
						//$pref = '<a href="'.$data[$key]['view'].'" target="_blank">';
						//$post = '</a>';
					}
					$ask_width  = ($value['ask_width' ]) ? $value['ask_width' ] : '*';
					$ask_height = ($value['ask_height']) ? $value['ask_height'] : '*';


					$f .= <<<FILE
						<tr><td colspan="3"><nobr>$file</nobr></td></tr>
						<tr><td><nobr>{$value['caption']} : </nobr></td>
							<td width="80%" valing="top">
								<span style="color:red">(recomended size <b>$ask_width x $ask_height</b>)</span><br />
								<input type="file" name="$key" $style />
							</td><td valign="middle">$req</td></tr>
						<tr><td colspan="3"><br /></td></tr>
FILE;
			    break;
		 	}
		}

		return $f;
	}
?>
