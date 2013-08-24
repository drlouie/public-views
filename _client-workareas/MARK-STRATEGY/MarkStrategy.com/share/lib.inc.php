<?
	function KRF_CheckBannerData(&$data, &$errors, &$SQL, $id)
	{
		if (!$id) $id = 0;
		
		$db = $SQL->Query("SELECT id FROM banner WHERE id<>$id AND name='{$data['name']}'");
		if ($db && $SQL->Numrows($db))
		{
			$errors['name'] = 'the banner with such name is already exists';

			return true;
		}
		return false;
	}
	
	function KRF_CheckDate(&$field, &$date_arr)
	{
		$cur_year = date('Y');
		
		$report = Array (
							'is_err' => false,
							'errmsg' => false,
							'mktime' => false,
							'day'    => false, 
							'month'  => false, 
							'year'   => false, 
							'hour'   => false, 
							'min'    => false
						);

		
		$limits = Array (
							'day'   => array(1,31),
							'month' => array(1,12),
							'year'  => array(0,false),
							'hour'  => array(0,23),
							'min'   => array(0,60)
						);

		if ($field['is_time'])
		{
			if (!$date_arr['time']) $date_arr['time'] = ' : ';

			list($date_arr['hour'], $date_arr['min']) = explode(':', $date_arr['time']);
		}

		$is_empty = true;
		
		foreach($date_arr as $key => $value)
		{
			$date_arr[$key] = trim($value);
			if (!empty($date_arr[$key]) && $key != 'time') $is_empty = false;
		}
		
		if ($is_empty)
		{
			if ($field['empty'])
			{
				$date_arr = 0;
				return array ('is_err' => false, 'mktime' => 0);
			}
			else
			{
				return array('is_err' => true, 'errmsg' => 'date couldn\'t be empty');
			}
		}

		if ($field['cur_year']) $date_arr['year'] = $cur_year;
		
		foreach($date_arr as $key => $value)
		{
			if ($key !== 'time')
			{
				if (!is_numeric($value))
				{
					$report['errmsg'] = 'invalid date';
					$report['is_err'] = true;
				}
				else
				{
					$value = (int)($value);
					$date_arr[$key] = $value;
					
					$up   = $limits[$key][1];
					$down = $limits[$key][0];
					if ($value < $down || ($up !== false && $value > $up))
					{
						$report['errmsg'] = 'invalid date';
						$report['is_err'] = true;
					}
				}
			}
		}

		if (!$report['is_err'])
		{
			if ($date_arr['year'] < 31) $year+=2000;
			else if ($date_arr['year'] < 100) $year+=1900;
			
			if (!checkdate($date_arr['month'],$date_arr['day'],$date_arr['year']))
			{
				$report['is_err'] = true;
				$report['errmsg'] = 'invalid date';
				return $report;
			}
			
			$date_arr = $report['mktime'] = mktime ( $date_arr['hour'], 
			                             $date_arr['min'], 
			                             0,
			                             $date_arr['month'],
			                             $date_arr['day'], 
			                             $date_arr['year']);
		}
		return $report;
	}

	function KRF_check_email($email)
	{
		return preg_match ('/^[a-zA-Z0-9][a-zA-Z0-9\-\.\_]{0,62}[\@]([a-zA-Z0-9\-]{1,62}[\.]){2,}$/', "$email.");	
	}
	
	function KRF_validatemailboxname(&$field, &$email)
	{
		$email = trim($email);

		if (empty($email))
		{
			if ($field['empty']) return array ('is_err' => false);
			else return array ('is_err' => true, 'errmsg' => "(required)");
		}
		
		$ret = array ('is_err' => !(strlen ($email) < 255 &&
		preg_match ('/^[a-zA-Z0-9][a-zA-Z0-9\-\.\_]{0,62}[\@]([a-zA-Z0-9\-]{1,62}[\.]){2,}$/', "$email.")));

		if ($ret['is_err']) $ret['errmsg'] = 'invalid e-mail';

		return $ret;
	}

	function KRF_CheckText(&$field, &$data)
	{
		$data = trim($data);

		if (empty($data))
		{
			if ($field['empty']) return array ('is_err' => false);
			else return array ('is_err' => true, 'errmsg' => "(required)");	
		}

		if ($field['length'] && strlen > $field['length'])
			return array ('is_err' => true, 'errmsg' => "too long text (more than {$field['length']} characters)");

		return array ('is_err' => false);
	}

	function KRF_CheckFile(&$field, &$data)
	{
		if (empty($data['file']) || !file_exists($data['file']))
		{
			if ($field['empty']) return array ('is_err' => false);
			else return array ('is_err' => true, 'errmsg' => "file must be specified");
		}

		return array ('is_err' => false);
	}

	function KRF_CheckFormData(&$form, &$data, &$errors)
	{
		global $check_form;
		
		$is_err = false;
		foreach($form as $key => $field)
		{
			$rep = $check_form[$field['data_type']]($field, $data[$key]);
			
			if ($rep['is_err'])
			{
				$is_err = true;
				$errors[$key] = $rep['errmsg'];
			}
		}

		return $is_err;
	}

	function KRF_StoreFormData($table, &$form, &$data)
	{
		global $SQL, $main;


		$fields = array();
		$values = array();
		$files  = array();

		foreach ($form as $key => $field)
		{
			if ($field['data_type'] != 'file') $data[$key] = addslashes($data[$key]);

			if ($field['field'])
			{
				$fields[] = $field['field'];
				$values[] = "'{$data[$key]}'";
			}

			if ($field['data_type'] == 'file' && file_exists($data[$key]['file']))
			{
				$files[$key] = $data[$key];
			}
		}
		$fields = implode(',', $fields);
		$values = implode(',', $values);

		$SQL->Query("INSERT INTO $table ($fields) VALUES ($values)");
		
		$id = $SQL->Insertid();

		if (is_array($files))
		{
			foreach($files as $key => $file)
			{
				$SQL->Query("UPDATE $table SET $key='{$file['ext']}' WHERE id = $id");
				
				@copy($file['file'], $main['files'][$key].$id.'.'.$file['ext']);
				@unlink($file['file']);
			}
		}

		return $id;
	}

	function KRF_UpdateFormData($table, &$form, &$data, $id)
	{
		global $SQL, $main;


		$set = array();
		$files  = array();

		foreach ($form as $key => $field)
		{
			if ($field['field'])
			{
				$set[] = $field['field']."='{$data[$key]}'";
			}

			if ($field['data_type'] == 'file' && file_exists($data[$key]['file']))
			{
				$files[$key] = $data[$key];
			}
		}
		$set = implode(',', $set);

		$SQL->Query("UPDATE $table SET $set WHERE id = $id");
		
		if (is_array($files))
		{
			foreach($files as $key => $file)
			{
				$db = $SQL->Query("SELECT $key FROM $table WHERE id = $id");
				list($ext) = $SQL->Fetchrow($db);
				if ($ext)
				{
					@unlink($main['files'][$key].$id.'.'.$ext);
				}


				$SQL->Query("UPDATE $table SET $key='{$file['ext']}' WHERE id = $id");
				
				@copy($file['file'], $main['files'][$key].$id.'.'.$file['ext']);
				@unlink($file['file']);
			}
		}
	}

	function KRF_CheckUserData(&$data, $id = 0)
	{
		global $SQL;

		$rep = array('is_err' => false, 'login' => false, 'domain' => false);
		
		$db = $SQL->Query("SELECT id FROM user 
							WHERE login = '{$data['login']}' AND 
								id <> $id LIMIT 0,1");
		
		if ($db && $SQL->Numrows($db))
		{
			$rep['is_err'] = $rep['login'] = true;
		}

		$db = $SQL->Query("SELECT id FROM user 
							WHERE domain = '{$data['domain']}' AND 
								id <> $id LIMIT 0,1");

		if ($db && $SQL->Numrows($db))
		{
			$rep['is_err'] = $rep['domain'] = true;
		}

		return $rep;
	}

	function KRF_sendMessade($from_email, $from_name, $to_email, 
		   						$message_subject, $message_text, $type='html')
	{
		$subject   = convert_cyr_string ($message_subject , 'w', 'k');
		$mailbody  = convert_cyr_string ($message_text, 'w', 'k');
		$from_name = convert_cyr_string ($from_name, 'w', 'k');

		$headers  = "MIME-Version: 1.0\r\n";
		if ($type == 'text')
		{
			$mailbody = preg_replace ('/<br\s*>/i', "\n", $mailbody);
			$mailbody = preg_replace ('/<p\s*>/i', "\n", $mailbody);
			$mailbody = strip_tags($mailbody);

			$headers .= "Content-type: text/plain; charset=KOI8-R\r\n";
		}
		else
			$headers .= "Content-type: text/html; charset=KOI8-R\r\n";
        
        $headers .= "From: $from_name <$from_email>\r\n";

		mail($to_email, $subject, $mailbody, $headers);	
	}

	function KRF_CreateFormMessage(&$form, &$data)
	{
		$msg  = '<table>';
		foreach($form as $key => $value)
		{
			$data[$key] = trim($data[$key]);
			if ($data[$key])
			{
				$msg .= '<tr><td><b>'.$value['caption'].'</b></td><td>'.$data[$key].'</td></tr>';
			}
		}
		$msg .= '</table>';

		return $msg;
	}

	function KRF_ShowToolbarForm(&$SQL, &$url, $id_home = NULL)
	{
		if (!$data || !is_array($data)) $data = array();

		$where_home = ($id_home) ? " AND u.id_home = $id_home " : ' AND id_home=0 ';
		$ret = '<table width="100%">';
		$db = $SQL->Query("SELECT t.id, t.caption, t.url AS turl,
							u.url AS uurl
						FROM toolbar AS t
						LEFT JOIN user_toolbar AS u
						ON u.id_menu = t.id $where_home");
		for ($i=0; $i<$SQL->Numrows($db); $i++)
		{
			$n = $i+1;
			list($tId, $tCap, $tUrl, $uUrl) = $SQL->Fetchrow($db);

			$u = ($uUrl) ? $uUrl : '';
			if ($url !== NULL) $u = $url[$tId];
			
	        $ret .= <<<ITEM
    		    <tr><td valign="center"><nobr>&nbsp;$n.&nbsp;<a href="$tUrl" target="_blank">$tCap:</a>&nbsp;</nobr></td>
		           	<td width="100%"><input type="text" value="$u" name="url[$tId]" style="width:100%" /></td>
		        </tr>
ITEM;
		}
		$ret .= '</table>';

		return $ret;
	}

	function KRF_ShowTaskbarForm(&$SQL, &$url, $id_user = NULL)
	{
		if (!$data || !is_array($data)) $data = array();

		$where_home = ($id_user) ? " AND u.id_user = $id_user " : ' AND id_user=0 ';
		$ret = '<table width="100%">';
		$db = $SQL->Query("SELECT t.id, t.caption, t.url AS turl,
							u.url AS uurl
						FROM taskbar AS t
						LEFT JOIN user_taskbar AS u
						ON u.id_menu = t.id $where_home");
		
		for ($i=0; $i<$SQL->Numrows($db); $i++)
		{
			$n = $i+1;
			list($tId, $tCap, $tUrl, $uUrl) = $SQL->Fetchrow($db);

			$u = ($uUrl) ? $uUrl : '';
			if ($url !== NULL) $u = $url[$tId];
			
	        $ret .= <<<ITEM
    		    <tr><td valign="center"><nobr>&nbsp;$n.&nbsp;<a href="$tUrl" target="_blank">$tCap:</a>&nbsp;</nobr></td>
		           	<td width="100%"><input type="text" value="$u" name="uurl[$tId]" style="width:100%" /></td>
		        </tr>
ITEM;
		}
		$ret .= '</table>';

		return $ret;
	}

	function KRF_StoreTaskbarSettings($id_user, &$url, &$SQL)
	{
		$SQL->Query("DELETE FROM user_taskbar WHERE id_user = $id_user");
		if (is_array($url))
		{
			foreach($url as $tId => $u)
			{
				if ($u !== '')
				{
					$SQL->Query("INSERT INTO user_taskbar (id_user, id_menu, url) 
								VALUES ($id_user, $tId, '$u')");
				}
			}
		}
	}

	function KRF_StoreToolbarSettings($id_home, &$url, &$SQL)
	{
		$SQL->Query("DELETE FROM user_toolbar WHERE id_home = $id_home");
		if (is_array($url))
		{
			foreach($url as $tId => $u)
			{
				if ($u !== '')
				{
					$SQL->Query("INSERT INTO user_toolbar (id_home, id_menu, url) 
								VALUES ($id_home, $tId, '$u')");
				}
			}
		}
	}
	
	
	function KRF_Shedulers2CSV($id, &$SQL)
	{
		global $main, $HTTP_HOST;

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
        $ret = 'id;id_home;name;email;phone;preffered date;alternate date;notes;address;city;state;zip;home photo'."\n";
		for ($i=0; $i<$SQL->Numrows($db); $i++)
		{
			list($sId, $id_home, $name, $email, $phone, $d1, $d2, 
				$notes, $addr, $city, $state, $zip, $photo) = $SQL->Fetchrow($db);
			$d1 = ($d1) ? date('F j, Y, g:i a', $d1) : '';
			$d2 = ($d2) ? date('F j, Y, g:i a', $d2) : '';
			$home_photo = "{$main['files']['home_photo']}$id_home.$photo";
			
			$ret .= "$sId;$id_home;\"".strtr($name, array('"' => '""'))."\";$email;$phone;$d1;$d2;".
					'"'.strtr($notes, array('"' => '""')).'";'.
					'"'.strtr($addr, array('"' => '""')).'";'.
					'"'.strtr($city, array('"' => '""')).'";'.
					'"'.strtr($state, array('"' => '""')).'";'.
					'"'.strtr($zip, array('"' => '""')).'";'.
					"http://$HTTP_HOST/img/homes/$id_home.$photo\n";
			
		}

		return $ret;
	}

	function KRF_Shedulers2TXT($id, &$SQL)
	{
		global $main, $HTTP_HOST;

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
        $ret = "\r\n";
		for ($i=0; $i<$SQL->Numrows($db); $i++)
		{
			list($sId, $id_home, $name, $email, $phone, $d1, $d2, 
				$notes, $addr, $city, $state, $zip, $photo) = $SQL->Fetchrow($db);
			$d1 = ($d1) ? date('F j, Y, g:i a', $d1) : '';
			$d2 = ($d2) ? date('F j, Y, g:i a', $d2) : '';
			$home_photo = "http://$HTTP_HOST/img/homes/$id_home.$photo";

			$ret .= "Home: $addr, $city, $state $zip\r\nPhoto: $home_photo\r\n\r\n";
			$ret .= "Client:\r\n";
			$ret .= "\tName: $name\r\n\tE-mail: $email\r\n\tPhone: $phone\r\n\tPreferred date: $d1\r\n\tAlternate date: $d2\r\n";
			$ret .= "-------------------------------------------------------------------------------------------------------\r\n\r\n";
		}

		return $ret;
	}
	
	
	function KRF_table2CSV($table, &$fields, &$SQL, $f_path = NULL, $where = NULL)
    {
		global $HTTP_HOST;
		$files_path = array();
		if (is_array($f_path))
		{
			foreach($f_path as $key => $v)
			{
				$files_path[$key] = 'http://'.$HTTP_HOST.'/'.$f_path[$key].'%s.%s';
			}
		}
		
		$flds = 'id';
		$ret  = '"id"';
		
		if (!is_array($fields) || !count($fields)) return FALSE;
		
		foreach ($fields as $key => $v)
		{
			$ret  .= ';"'.strtr($v['caption'], array('"' => '""')).'"';
			$flds .= ($v['field']) ? ','.$v['field'] : ','.$key;
		}
		$ret .= "\n";

		if ($where == NULL)  $where = '';
		$db = $SQL->Query("SELECT $flds FROM $table $where");
		if (!$db || !($cnt = $SQL->Numrows($db))) return $ret;

		for ($i=0; $i<$cnt; $i++)
		{
			$row = $SQL->Fetcharray($db, 'num');
			$j   = 1;
			$ret .= $row[0];
			foreach ($fields as $key => $v)
			{
				if ($v['data_type'] == 'date')
				{
					$ret  .= ';"'.date("d.m.Y", $row[$j]).'"';
				}
				else if ($v['data_type'] !== 'file')
				{
					$ret  .= ';"'.strtr($row[$j], array('"' => '""')).'"';
				}
				else
				{
					$ret  .= ';"'.sprintf($files_path[$key], $row[0], $row[$j]).'"';
				}
				$j++;
			}
			$ret .= "\n";
		}

		return $ret;
	}

	function KRF_table2TXT($table, &$fields, &$SQL, $f_path = NULL, $where = NULL)
    {
		global $HTTP_HOST;
		$files_path = array();
		if (is_array($f_path))
		{
			foreach($f_path as $key => $v)
			{
				$files_path[$key] = 'http://'.$HTTP_HOST.'/'.$f_path[$key].'%s.%s';
			}
		}
		
		$flds = '';
				
		if (!is_array($fields) || !count($fields)) return FALSE;
		
		foreach ($fields as $key => $v)
		{
			$flds .= ($v['field']) ? $v['field'].',' : $key.',';
		}
		$flds = substr($flds, 0, -1);
		
		if ($where == NULL)  $where = '';
		$db = $SQL->Query("SELECT $flds FROM $table $where");
		if (!$db || !($cnt = $SQL->Numrows($db))) return $ret;

		for ($i=0; $i<$cnt; $i++)
		{
			$row = $SQL->Fetcharray($db, 'num');
			$j   = 0;
			foreach ($fields as $key => $v)
			{
				if ($v['data_type'] == 'date')
				{
					$ret .= $v['caption'].': '.date("d.m.Y", $row[$j])."\r\n";
				}
				else if ($v['data_type'] !== 'file')
				{
					$ret .= $v['caption'].': '.$row[$j]."\r\n";
				}
				else
				{
					$ret .= $v['caption'].': '.sprintf($files_path[$key], $row[0], $row[$j])."\r\n";
				}
				$j++;
			}
			$ret .= "---------------------------------------------------------------------------------------------------------------------\r\n";
		}

		return $ret;
	}
?>
