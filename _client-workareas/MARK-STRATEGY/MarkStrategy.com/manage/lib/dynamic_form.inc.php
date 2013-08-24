<?
	if (!defined('INNER')) exit;

	class KRF_dynamic_form
	{
		var $SQL;
		var $table;
		var $types;
		var $form;
		var $adding_form = '';
		var $js = '';
		var $max = 20;
		var $out_file = '../share/dynamic_form_hash.inc.php';
		var $variable = 'home_form';
		var $config_name = 'cfg_home_form';
		var $undeleting_fields;
		
		function KRF_dynamic_form($table='', &$SQL, $form = FALSE, $undeleting_fields = NULL, $max = 20)
		{
		    if (!$table) return NULL;
		    if (!$SQL) return NULL;

		    
		    $this->SQL   = $SQL;
            $this->table = $table;

            if (is_numeric($max) && $max>0) $this->max = $max;

		    $this->types = array();
		    $this->types['html'] = array('text', 'textarea', 'select', 'checkbox', 'file');

		    if (!is_array($undeleting_fields)) $this->undeleting_fields = Array();
		    else $this->undeleting_fields = $undeleting_fields;
            
		    if (is_array($form)) $this->form = $form;
		    else $this->ReadForm();

		    if (!is_array($this->form)) $this->form = array();

		    if (!$SQL->TableExists($table))
		    {
		    	$query = "CREATE TABLE $table (id integer not NULL primary key auto_increment, id_user integer not NULL";
		    	foreach($this->form as $v)
		    	{
	    			$type = ($v['type'] == 'textarea') ? 'TEXT' : 'VARCHAR(255)';
	    			$query .= ",{$v['field']} $type";
		    	}
		    	$query .= ')';
		    	$SQL->Query($query);	
		    }
		    else
		    {
		    	$flds_old = $SQL->ListFields($table);
		    	unset($flds_old[0]);
		    	unset($flds_old[1]);
		    	$flds_new = array();
		    	$flds_new_types = array();
		    	
		    	foreach($this->form as $v)
		    	{
		    		$flds_new[] = $v['field'];
			    	$flds_new_types[] = $v['type'];
                }
                		    	
		    	foreach($flds_old as $v)
		    	{
					if (!in_array($v, $flds_new) && !in_array($v, $this->undeleting_fields))
					{
						$SQL->Query("ALTER TABLE $table DROP $v");
					}
		    	}

		    	for($i=0; $i<count($flds_new); $i++)
		    	{
	    			$query  = "ALTER TABLE $table ADD ";
	    			$type   = ($flds_new_types[$i] == 'textarea') ? 'TEXT' : 'VARCHAR(255)';
	    			$query .= "{$flds_new[$i]} $type";

	    			$SQL->Query($query);
		    	}
		    }

		    $this->ValidateForm();
		    $this->WriteForm();
		    
		    $this->adding_form = <<<FORM
		    <table width="100%"><form id="add_form" method="post" action="?">
		    <tr><td><nobr>Caption: </nobr></td>
		    <td width="90%"><input style="width:100%" type="text" name="caption" value="" /></td></tr>
		    <tr><td><nobr>Field name: </nobr></td>
		    <td width="90%"><input style="width:100%" type="text" name="fld_name" value="" /></td></tr>
		    <tr><td><nobr>Field type: </nobr></td>
		    <td width="90%"><select name="type">
FORM;
			foreach($this->types['html'] as $value)
			{
				$this->adding_form .= "<option value=\"$value\">$value</option>";
			}
			$this->adding_form .=<<<BUTTONS
			<tr><td colspan="2"><input type="button" value="Add field" onclick="DF_add_field()" /></td></tr>
BUTTONS;
			$this->adding_form .= '</form></table>';

			$flds = 'Array();';
			foreach($this->form as $key => $value)
			{
				$ordi = $key + 1;
				$flds .=  "flds[$key] = Array();\nflds[$key]['field'] = '{$value['field']}';\nflds[$key]['caption'] = '{$value['caption']}';\nflds[$key]['type'] = '{$value['type']}';\n";
				$flds .=  (!in_array($value['field'], $this->undeleting_fields)) ? "flds[$key]['del'] = true;\n" : "flds[$key]['del'] = false;\n";
				$flds .= "flds[$key]['values'] = Array();\n";
				$flds .= "flds[$key]['order' ] = $ordi;";
				if (is_array($value['values']))
				{
					foreach($value['values'] as $k => $v)
					{
						$flds .= "flds[$key]['values'][$k] = '$v';\n";
					}
				}
			}

			$up  = 'Q W E R T Y U I O P A S D F G H J K L Z X C V B N M É Ö Ó Ê Å Í Ã Ø Ù Ç Õ Ú Ô Û Â À Ï Ð Î Ë Ä Æ Ý ß × Ñ Ì È Ò Ü Á Þ ¨';
			$low = 'q w e r t y u i o p a s d f g h j k l z x c v b n m é ö ó ê å í ã ø ù ç õ ú ô û â à ï ð î ë ä æ ý ÿ ÷ ñ ì è ò ü á þ ¸';

			$up = explode(' ', $up);
			$low = explode(' ', $low);

			$regs = '';
			foreach($up as $key => $v)
			{
				$regs .= "new_str = new_str.replace(/$v/g,'{$low[$key]}');\n";
			}
			
			
			$this->js = <<<JS
			var cur_id = 1;
			var max_id = $this->max;
			var flds   = $flds
			
			
			function DF_tolower(str)
			{
				new_str = new String(str);
				$regs	
				return new_str;
			}
			
			function DF_trim(str)
			{
				new_str = new String(str);

				l = new_str.length;
				if (!l) return '';

				while(' ' == new_str.substr(0,1))
				{
					new_str = new String(new_str.substr(1,l-1));
					l--;
				}

				l = new_str.length;
                if (!l) return '';

                while (' ' == new_str.substr(l-1,1))
                {
                	new_str = new String(new_str.substr(0,l-1));
					l--;
                }

                l = new_str.length;
                if (!l) return '';
                				
				old_len = new_str.length + 1;
                				
				while (old_len > new_str.length)
				{
					old_len = new_str.length;
					new_str = new_str.replace(/  /g,' ');
				}
				return new_str;
			}
			
			function DF_add_field()
			{
				f = document.getElementById('add_form');
				f.caption.value = DF_trim(f.caption.value);
				f.fld_name.value = DF_tolower(DF_trim(f.fld_name.value));

				fld = new String(f.fld_name.value);
				cap = new String(f.caption.value);

				is_err  = false;
				err_msg = '';

				if (!cap.length)
				{
					is_err = true;
					err_msg += '(Caption required)\\n';
				}

				if (!fld.length)
				{
					is_err = true;
					err_msg += '(required)\\n';
                }

				if (is_err)
				{
					alert(err_msg);
					return;
				}

				for (i in flds)
				{
					if (flds[i]['field'] == f.fld_name.value)
					{
						alert('Field with such name is already exists!\\n');
						return;
					}
				}

				if (cur_id >= max_id)
				{
					alert('Too many fields! Please, click to the <Save form> button.');
				}

				flds[flds.length] =  Array();
				flds[flds.length-1]['caption'] = cap;
				flds[flds.length-1]['field'  ] = fld;
				flds[flds.length-1]['del'    ] = true;
				flds[flds.length-1]['type'   ] = f.type.value;
				flds[flds.length-1]['order'  ] = flds.length;
				flds[flds.length-1]['values' ] = Array();

				f.reset();

				DF_ShowFields();
			}

			function DF_checkItem(id)
			{
				
				d = document.getElementById('s'+id);
				d.className = (d.className == 'tnorm') ? 'tbold' : 'tnorm';
			}

			function DF_addValue(id)
			{
				f = document.getElementById('fields_form'); 
				v = f['v'+id].value;

				if (v == '')
				{
					alert('Value required!');
					return;
				}

				flds[id-1]['values'][flds[id-1]['values'].length] = v;
				DF_ShowFields();
			}

			function DF_delValue(id)
			{
				f = document.getElementById('fields_form'); 
				s = f['sel'+id];

				fl = Array();

				if (!s.options.length) return;

				
				for (i=0; i<s.options.length; i++)
				{
					if (!s.options[i].selected)					
					{
						fl[fl.length] = flds[id-1]['values'][i];
					}
				}
                flds[id-1]['values'] = fl;

				DF_ShowFields();
			}
			
			
			function DF_ShowFields()
			{
				for (i=1; i<=max_id; i++)
				{
					document.getElementById(''+i+'').innerHTML = '';
				}
				
				cur_id = 1;
				for (i in flds)
				{
					if (cur_id > max_id) return;
                    
					check = (flds[i]['del']) ? '<input class="check" type="checkbox" border="0" id="c'+cur_id+'" onclick="DF_checkItem('+cur_id+')" />&nbsp;' : '';
					
					html  = '<fieldset><table><tr><td>'+check+'</td><td><span class="tnorm" id="s'+cur_id+'">';
					html += 'Order: <input type="text" size="2" id="order'+cur_id+'" value="'+cur_id+'" /><br />';
					html += 'Caption: <b>'+flds[i]['caption']+'</b><br />Field name: <b>'+flds[i]['field']+'</b><br />Type: <b>'+flds[i]['type']+'</b>';
					
					if (flds[i]['type'] == 'select')
					{
						html += '<img src="" alt="" width="70" height="0" border="0" /><select id="sel'+cur_id+'">';
						for (j=0; j<flds[i]['values'].length; j++)
						{
							html += '<option value="'+j+'">'+flds[i]['values'][j]+'</option>';
						}                           
						html += '</select>&nbsp;<input type="button" value="Del value" onclick="DF_delValue('+cur_id+')" />&nbsp;<input type="text" id="v'+cur_id+'" />&nbsp;<input type="button" value="Add value" onclick="DF_addValue('+cur_id+')" />';
					}
                    html += '</span></td></tr></table></fieldset>';

					document.getElementById(''+cur_id+'').innerHTML = html;

					cur_id++;
				}
			}

			function DF_SaveForm()
			{
				html  = '<form id="submit_form" action="?" method="post"><input type="hidden" name="act" value="homes_form" /><input type="hidden" name="done" value="1" />';

				f = document.getElementById('fields_form'); 
				order = Array();
				for (j=1; j < cur_id; j++)
				{
					o = f['order'+j];
					ind = parseInt(o.value);
					if (isNaN(ind))
					{
						alert('All order values must be numerical!');
						return;
					}

					for (k=0; k<j-1; k++)
					{
						if (order[k] == ind)
						{
							alert('All order values must be different!');
							return;
						}
					}

					order[j-1] = ind;
				}
				
				id = 0;
				for (i in flds)
				{
					id++;
					html += '<input type="hidden" name="f['+i+'][field]" value="'+flds[i]['field']+'">';
					html += '<input type="hidden" name="f['+i+'][caption]" value="'+flds[i]['caption']+'">';
					html += '<input type="hidden" name="f['+i+'][type]" value="'+flds[i]['type']+'">';
					html += '<input type="hidden" name="f['+i+'][order]" value="'+f['order'+id].value+'">';

					if (flds[i]['type'] == 'select')
					{
						for (j in flds[i]['values'])
						{
							html += '<input type="hidden" name="f['+i+'][values]['+j+']" value="'+flds[i]['values'][j]+'">';
						}
					}
				}
				html += '</form>';

				d = document.getElementById('hidden_div');
				d.innerHTML  = html;

				document.getElementById('submit_form').submit();
			}

			function DF_DeleteFields()
			{
				f = document.getElementById('fields_form');

				flds_new = Array();
				id = 1;
				for (i=1; i<cur_id; i++)
				{
					if (!f['c'+i] || !f['c'+i].checked)
					{
						flds_new[id-1] =  flds[i-1];
						id++;
					}
				}

				flds = flds_new;
				DF_ShowFields();
			}
JS;
			return true;
		}

		function OrderForm()
		{
			for ($i=0; $i<count($this->form); $i++)
			{
				for ($k=0; $k<count($this->form) - $i - 1; $k++)
				{
					if ((int)$this->form[$k]['order'] > (int)$this->form[$k+1]['order'])
					{
						$tmp = $this->form[$k];
						$this->form[$k]   = $this->form[$k+1];
						$this->form[$k+1] = $tmp;
					}
				}
			}
		}
		
		function ReadForm()
		{
			include($this->out_file);
            $this->form = ${$this->variable};
		}

		function WriteForm()
		{
			$src = "<? \$".$this->variable."=Array(";
			$cfg = '$'.$this->config_name.'=Array(';
			foreach($this->form as $key => $value)
			{
				
				if ($value['type'] == 'textarea') $html_type =  'textarea';
				else if ($value['type'] == 'file') $html_type = 'file';
				else if ($value['type'] == 'select') $html_type = 'select';
				else $html_type = 'text';

				$data_type = ($value['type'] == 'file') ? 'file' : 'text';
				$field = ($value['type'] == 'file') ? '' : "'field' => '{$value['field']}',";
				
				$cfg .= "'{$value['field']}' => Array('rows' => 5, 'order' => {$value['order']}, 'caption' => '{$value['caption']}', $field  'empty' => true, 'length' => 255, 'html_type' => '$html_type', 'data_type' => '$data_type', 'values' => Array(";
				$src .= "$key => Array('order' => {$value['order']}, 'caption' => '{$value['caption']}', 'field' => '{$value['field']}', 'type' => '{$value['type']}', 'values' => Array(";
				if (is_array($value['values']))
				{
					foreach ($value['values'] as $v)
					{
						$src .= "'$v',";
						$cfg .= "'$v',";
					}
				}
				$src .= ')),';
				$cfg .= ')';
				if ($value['type'] == 'file')
				{
					$cfg .= ",'ask_width' => 135, 'ask_height' => 110";
				}
				$cfg .= '),';
			}
			$src .= ");\n$cfg);?>";

			$fp = fopen($this->out_file, 'w');
			fwrite($fp, $src);
			fclose($fp);
		}
		
		function GetFields()
		{
			$db = $this->SQL->Query('describe '.$this->table);
			$ret = array();
			for ($i=0; $i<$this->SQL->Numrows($db); $i++)
			{
				$ret[] = $this->SQL->Fetcharray($db, 'num');
            }
            
            return $ret;
		}

		function ValidateForm()
		{
			$flds = $this->GetFields();
			$new  = array();
			for ($i=2; $i<count($flds); $i++)
			{
				for ($j=0; $j<count($this->form) && $this->form[$j]['field'] != $flds[$i][0]; $j++);

				if ($j<count($this->form) && $this->form[$j]['field'] == $flds[$i][0])
				{
					$new[] = $this->form[$j];
					
					if ($flds[$i][0] == 'text') $new[count($new) - 1] = 'textarea';
				}
				else
				{
					$type = ($flds[$i][1] == 'text') ? 'textarea' : 'text';
					$new[] = array('caption' => $flds[$i][0], 'field' => $flds[$i][0], 'type' => $type);
				}
			}

			$this->form = $new;
			$this->OrderForm();
		}
		
		function ShowMenu()
		{
			return <<<MENU
				<table width="100%" class="head"><tr>
				<td width="50%"><input onclick="DF_SaveForm()" type="button" value="Save form" style="width:50%" /></td>
				<td width="50%" align="right"><input onclick="if (window.confirm('Are you sure to delete selected fields?')) DF_DeleteFields()" type="button" value="Delete selected fields" style="width:50%" /></td>
				</tr></table>
MENU;
		}

		function ShowLayers()
		{
			$ret = '<table width="100%"><form id="fields_form" action="?" method="post"><input type="hidden" value="0" name="count" /><input type="hidden" name="done" value="1" />';
			
			for ($i=1; $i<=$this->max; $i++)
			{
				$ret .= "<tr><td width=\"100%\"><div id=\"$i\"></div></td></tr>\n";	
			}

			$ret .= '</form></table>';
			$ret .= '<div id="hidden_div" style="display:none"></div>';
			$ret .= '<script>DF_ShowFields();</script>';

			return $ret;
		}

		function ShowAddingForm()
		{
			return $this->adding_form;
		}

		function ShowJS()
		{
			return $this->js;
		}
	}
?>