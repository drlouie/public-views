<?
	if (!defined('INNER')) exit;
	
//echo 'hi there';
	include_once 'share/global.inc.php';
//echo 'hi there 2';
	include_once 'share/config.inc.php';
//echo 'hi there 3';
	include_once 'share/sql.inc.php';
//echo 'hi there 4';
	include_once 'share/design.inc.php';
//echo 'hi there 5';
	include_once 'share/lib.inc.php';
//echo 'hi there 6';
	include_once 'share/dynamic_form_hash.inc.php';
//echo 'hi there 7';
	include_once 'share/homes.inc.php';
//echo 'hi there 8';

	$SQL = new KRF_SQL(
		$db_conf['user'], 
		$db_conf['passwd'], 
		$db_conf['host'],
		$db_conf['db']);


    
	$arr = explode('.', strtr($HTTP_HOST, array('www.' => '')));
 
	$db = $SQL->Query("SELECT u.id, u.logo, u.photo, u.info,
							u.email, u.ttl, u.mls_id, u.domain,
							u.fname, u.lname, u.mname,
							u.phone, u.fax, u.voicemail, 
							u.address, u.slogan,
							b.id, b.banner
						FROM user AS u
						LEFT JOIN user_banner AS ub
						ON ub.id_user=u.id
						LEFT JOIN banner AS b
						ON b.id = ub.id_banner
						WHERE u.domain='{$arr[0]}' LIMIT 0,1");


	
	$found = false;
	if ($db && $SQL->Numrows($db))
	{
		list($uId, $logo, $photo, $personal_info, $email_to, $ttl, $mls_id,
			$domain, $u_fname, $u_lname, $u_mname,
			$u_phone, $u_fax, $u_voicemail, $u_address, $u_slogan,
			$id_banner, $banner_ext) = $SQL->Fetchrow($db);
        
		$logo_img  = $main['files']['logo' ].$uId.'.'.$logo;
		$photo_img = $main['files']['photo'].$uId.'.'.$photo;
		if (!$id_banner)
		{
			$db = $SQL->Query("SELECT id, banner FROM banner LIMIT 0,1");
			list($id_banner, $banner_ext) = $SQL->Fetchrow($db);
		}
		$banner_img = $main['files']['banner'].$id_banner.'.'.$banner_ext;

		$found = ($ttl > mktime());
		
		if ($ttl < mktime())
		{
			header("Location: {$main['root.com']}expired.php?id=$uId");
			exit;
		}
		
        
        if ($found)
        {
    	    $db = $SQL->Query("SELECT t.id, t.caption, t.url AS turl,
		    					u.url AS uurl
		    					FROM taskbar AS t
		    					LEFT JOIN user_taskbar AS u 
		    					ON t.id = u.id_menu AND u.id_user = $uId
		    					ORDER BY t.id");
	    	$taskbar = array();
	    	for($t=0; $t<$SQL->Numrows($db); $t++)
	    	{
	    		$taskbar[$t] = array();
	    		list(, $taskbar[$t]['caption'], $taskbar[$t]['default'], $u) = $SQL->Fetchrow($db);
	    		$taskbar[$t]['url'] = ($u) ? $u : $taskbar[$t]['default'];

	    		$taskbar[$t]['url_nf'    ] = strtr($taskbar[$t]['url'    ], array('http://' => ''));
	    		$taskbar[$t]['default_nf'] = strtr($taskbar[$t]['default'], array('http://' => ''));
	    	}
    	    
    	    
    	    
    	    if ($act == 'contact' || $act == 'contact_mls')
        	{
	        	if ($act == 'contact_mls')
	        	{
	        		$wizard_act = 'mls_list';
	        	}
	        	
	        	$is_err = true;
		        if ($done)
		        {
	    		   	$data = array();
					foreach($contact_form as $key => $value)
					{
						$data[$key] = $$key;
					}

					$is_err = KRF_CheckFormData($contact_form, $data, $errors);
					if (!$is_err)
					{
						$msg  = KRF_CreateFormMessage($contact_form, $data);
						$subj = 'Homeseek: Contact form';
                	    $email_from = $data['email'];
                    	$name_from  = $data['fname'].' '.$data['lname'];

	                    KRF_sendMessade($email_from, $name_from, $email_to, $subj, $msg);
					}
				}
        	
	        	
		        $inner = ($act == 'contact') ? 'templates/contact_form.inc.php' : 'templates/contact_short_form.inc.php';
		    }
        	else if ($act == 'order')
	        {
		        $is_err = true;
	    	    if ($done)
	        	{
	        		$f_data = array();
					foreach($order_form as $key => $value)
					{
						$f_data[$key] = $$key;
						$message[$key] = $order_form[$key][caption].": ".$$key;

					}


					$is_err = KRF_CheckFormData($order_form, $f_data, $errors);
					if (!$is_err)
					{
						$msg  = KRF_CreateFormMessage($order_form, $data);


						$subj = 'Homeseek: Buying a home';
	                    	$email_from = $data['email'];
	                    $name_from  = $data['fname'].' '.$data['lname'];

			$msg = join("<br>", $message);
    	                KRF_sendMessade($email_from, $name_from, $email_to, $subj, $msg);

    	                $insId = KRF_StoreFormData('buying', $order_form, $f_data);
    	                $date = mktime();
    	                $SQL->Query("UPDATE buying SET id_user = $uId, post_date = $date WHERE id=$insId");
    	                
					}
				}
				$inner = 'templates/order_form.inc.php';
		    }
		    else if ($act == 'sell')
		    {
		    	$is_err = true;
		    	$inner = 'templates/sell_form.inc.php';
	    	    if ($done)
	        	{
	        		$f_data = array();
			
					foreach($sell_form as $key => $value)
					{
						$f_data[$key] = $$key;

						if ($order_form[$key][caption] && $$key)
							$message[$key] = $order_form[$key][caption].": ".$$key;
					}

					$is_err = KRF_CheckFormData($sell_form, $f_data, $errors);
					if (!$is_err)
					{
						$msg  = KRF_CreateFormMessage($sell_form, $data);
						$subj = 'Homeseek: Selling a home';
                    	$email_from = $data['email'];
	                    $name_from  = $data['fname'].' '.$data['lname'];

			$msg = join("<br>", $message);
    	                KRF_sendMessade($email_from, $name_from, $email_to, $subj, $msg);

    	                $insId = KRF_StoreFormData('selling', $sell_form, $f_data);
    	                $date = mktime();
    	                $SQL->Query("UPDATE selling SET id_user = $uId, post_date = $date WHERE id=$insId");
					}
				}
		    }
		    else if ($act == 'supplies' || !$act)
		    {
				$inner = 'templates/supplies.inc.php';
		    }
		    else if ($act == 'home' || $act == 'home_print' || $act == 'shedule_form')
		    {
		    	$flds  = array();
		    	foreach($cfg_home_form as $k => $v)
		    	{
		    		$flds[] = $k;
		    	}
		    	
		    	$db  = $SQL->Query('SELECT id,'.implode(',', $flds)." FROM homes WHERE id = $id LIMIT 0,1");
		    	$row = $SQL->Fetcharray($db, 'assoc');

		    	foreach($cfg_home_form as $k => $v)
		    	{
		    		if ($v['data_type'] !== 'file')
		    		{
		    			$data[$k]['caption'] = $v['caption'];
			    		$data[$k]['value'  ] = $row[$k];
			    	}
			    	else
			    	{
			    		$data[$k]['caption'] = $v['caption'];
			    		$data[$k]['src'    ] = $main['files'][$k].$id.'.'.$row[$k];
			    		if (!file_exists($data[$k]['src'])) $data[$k]['src'] = 'img/homes/blank_home.jpg';
			    	}
		    	}

		    	$db = $SQL->Query("SELECT t.id, t.caption, t.url AS turl,
		    					u.url AS uurl
		    					FROM toolbar AS t
		    					LEFT JOIN user_toolbar AS u 
		    					ON t.id = u.id_menu AND u.id_home = $id
		    					ORDER BY t.id");
		    	$toolbar = array();
		    	for($t=0; $t<$SQL->Numrows($db); $t++)
		    	{
		    		$toolbar[$t] = array();
		    		list(, $toolbar[$t]['caption'], $toolbar[$t]['default'], $u) = $SQL->Fetchrow($db);
		    		$toolbar[$t]['url'] = ($u) ? $u : $toolbar[$t]['default'];

		    		$toolbar[$t]['url_nf'    ] = strtr($toolbar[$t]['url'    ], array('http://' => ''));
		    		$toolbar[$t]['default_nf'] = strtr($toolbar[$t]['default'], array('http://' => ''));
		    	}
				
				
				if ($act == 'home') 
				{
					$inner = 'templates/home.inc.php';
				}
				else if($act == 'home_print')
				{
					$inner = 'templates/home_print.inc.php';
				}
				else if ($done)
				{
					$f_data = array();
					foreach($shedule_form as $key => $value)
					{
						$f_data[$key] = $$key;
					}
                    $is_err = KRF_CheckFormData($shedule_form, $f_data, $errors);
                    if (!$is_err)
                    {
                    	$msg  = KRF_CreateFormMessage($shedule_form, $f_data);
						$subj = 'Homeseek: Schedule a showing';
                    	$email_from = $f_data['shedule_email'];
	                    $name_from  = $f_data['shedule_name'];

    	                KRF_sendMessade($email_from, $name_from, $email_to, $subj, $msg);
                    	
                    	$insId = KRF_StoreFormData('shedule', $shedule_form, $f_data);
                    	$SQL->Query("UPDATE shedule SET id_user = $uId, id_home = $id WHERE id=$insId");

                    	$inner = 'templates/home.inc.php';
                    }
                    else
                    {
				   		$inner = 'templates/shedule.inc.php';
				   	}
				}
				else
				{
					$inner = 'templates/shedule.inc.php';
				}
		    }
		    else if ($act == 'mls_list')
		    {
		    	$mls_src = 'http://idd.homeseekers.com/scripts/list.asp?_org_id=oc&_em=1&agent_public_id='.$mls_id;
		    	$inner   = 'templates/mls.inc.php';
		    }
		    else if ($act == 'search_form')
		    {
		    	$mls_src = 'http://idd.homeseekers.com/search.asp?org_id=oc&agent_public_id='.$mls_id;
		    	$inner   = 'templates/mls.inc.php';
		    }
		    else if ($act == 'personal_info')
		    {
		    	$inner = 'templates/inner.inc.php';
		    }
		    else if ($act == 'email_property')
		    {
		    	$inner = 'templates/email_property.inc.php';
		    }
		    else if ($act == 'mortgage')
		    {
		    	$inner = 'templates/mortgage.inc.php';
		    }
		    else if ($act == 'links')
		    {
		    	$db = $SQL->Query("SELECT id, title, url, intro, link_picture
		    					FROM user_link WHERE id_user = $uId ORDER BY ordi");

		    	
		    	$links = array();
		    	for ($i=0; $i<$SQL->Numrows($db); $i++)
		    	{
		    		$links[$i] = $SQL->Fetcharray($db, 'assoc');

		    		if (file_exists($path = $main['files']['link_picture'].$links[$i]['id'].'.'.$links[$i]['link_picture']))
		    		{
		    			$links[$i]['img'] = $path;
		    		}
		    		else
		    		{
						$links[$i]['img'] = '';
		    		}
		    	}
		    	
		    	$inner = 'templates/links.inc.php';
		    }

        	$shedule_form_href   = 'index.php?act=shedule_form&id=%s';
        	$contact_form_href   = 'index.php?act=contact';
        	//$mls_list_href       = 'index.php?act=contact_mls';
        	$contact_mls_href    = 'index.php?act=contact_mls';
        	$mortgage_href       = 'main.php?act=mortgage&price=%s';
        	$email_property_href = 'index.php?act=email_property&id=%s';
	        $order_form_href     = 'index.php?act=order';
	        $sell_form_href      = 'index.php?act=sell';
	        $supplies_href       = 'main.php?act=supplies';
	        $home_href           = 'main.php?act=home&id=%s';
	        $home_print_href     = 'main.php?act=home_print&id=%s';
	        $mls_list_href       = 'http://idd.homeseekers.com/scripts/list.asp?_org_id=oc&_em=1&agent_public_id='.$mls_id;
            $info_href           = 'index.php?act=personal_info';
	       /* $search_form_href    = 'http://idd.homeseekers.com/search.asp?org_id=oc&agent_public_id='.$mls_id; */

$search_form_href				="http://idd.homeseekers.com/search.asp?blnAdvancedSearch=true&_org_id=oc,gsb,mr,oca,claw,dam,bbva,dcar,sand,vv&_reg_id=socal&_ver=4&_lid=0&_pType=1&_account=idd&_new=1&_idd_yn=y&_agent_public_id=$mls_id";

        	$contact_form_href_nf   = 'index.php?act=contact';
        	$email_property_href_nf = 'index.php?act=email_property&id=%s';
	        $order_form_href_nf     = 'index.php?act=order';
	        $sell_form_href_nf      = 'index.php?act=sell';
	        $supplies_href_nf       = 'index.php?act=supplies';
	        $home_href_nf           = 'index.php?act=home&id=%s';
	        $mls_list_href_nf       = 'http://idd.homeseekers.com/scripts/list.asp?_org_id=oc&_em=1&agent_public_id='.$mls_id;
	        //$mls_list_href          = 'index.php?act=contact_mls';
            $info_href_nf           = 'index.php?act=personal_info';
	        $search_form_href_nf    = 'index.php?act=advsearch&org_id=oc&agent_public_id='.$mls_id;

			$found = true;
		}
    }
    else
    {
    	header("Location: {$main['root.com']}not_found.php");
		exit;
    }
?>
