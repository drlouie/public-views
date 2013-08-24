<?
	if (!defined('INNER')) exit;

	

        $db_conf = array(
                'user'   => 'robert_orange21',
                'passwd' => 'ora12nge',
                'host'   => 'localhost',
                'db'     => 'robert_orange21'
        );

	$main = array(
		'root.com'   => 'http://www.markstrategy.com/',
		'files' => array(
			'logo'   => '../img/logo/',
			'photo'  => '../img/photo/',
			'img'    => '../img/',
			'banner' => '../img/banner/',
			'home_photo'   => '../img/homes/',
			'link_picture' => '../img/links/')
	);
	
	
	$window = Array(
		'head_class'   => 'head',
		'border_class' => 'board',
		'in_class'     => 'inner',
		'l_line'       => 1,
		'r_line'       => 1,
		'd_line'       => 1,
		'r_space'      => 5,
		'l_space'      => 5,
		'd_space'      => 5,
		'caption'      => '',
		'menu'         => '',
		'inner'        => '');	
   //'menu'         => '<a href="?act=settings"><img alt="settings" border="0" src="'.$main['files']['img'].'icon-settings.gif" alt="" width="16" height="16" /></a>',


	$action_list = array(
		'login_form'  => 'login.inc.php',
		'default'     => 'main.inc.php',
		'users'       => 'main.inc.php',
		'add_user'    => 'add_user.inc.php',
		'edit_user'   => 'edit_user.inc.php',
		'settings'    => 'settings.inc.php',
		'homes_form'  => 'homes_form.inc.php',
		'supply_user' => 'supply.inc.php',
		'add_home'    => 'add_home.inc.php',
		'edit_home'   => 'edit_home.inc.php',
		'delete_home' => 'supply.inc.php',
		'users_csv'   => 'users_csv.inc.php',
		'homes_csv'   => 'homes_csv.inc.php',
		'toolbar'     => 'toolbar.inc.php',
		'taskbar'     => 'taskbar.inc.php',
		'banner_lst'  => 'banner.inc.php',
		'banner_add'  => 'banner_add.inc.php',
		'banner_edit'  => 'banner_edit.inc.php',
		'link_page'   => 'link_page.inc.php',
		
		'delete_link'  => 'links.inc.php',
		'links_user'   => 'links.inc.php',
		'add_link'     => 'links_add.inc.php',
		'edit_link'    => 'links_edit.inc.php',
		
		'logout'      => 'logout.inc.php');

	$toolbar_form = array(
		'caption' => array('caption' => 'Caption',
						'html_type' => 'text',
						'data_type' => 'text',
						'length'    => 255,
						'empty'     => false,
						'field'     => 'caption'),
		'url'    => array('caption' => 'URL',
						'html_type' => 'text',
						'data_type' => 'text',
						'length'    => 255,
						'empty'     => false,
						'field'     => 'url'));

	$user_form = array(
		'login' => array('caption'  => 'Login',
						'html_type' => 'text',
						'data_type' => 'text',
						'length'    => 64,
						'empty'     => false,
						'field'     => 'login'),

		'passwd' => array('caption' => 'Password',
        				'html_type' => 'password',
        				'data_type' => 'text',
						'length'   => 64,
						'empty'    => false,
						'field'    => 'passwd'),

		'domain' => array('caption'  => 'Domain',
						'html_type' => 'text',
						'data_type' => 'text',
						'length'    => 255,
						'empty'     => false,
						'field'     => 'domain'),

		'ttl' => array('caption' => 'Active until',
						'html_type' => 'date',
						'data_type' => 'date',
						'empty'     => true,
						'field'     => 'ttl'),

		'mls_id' => array('caption'  => 'MLS ID',
						'html_type' => 'text',
						'data_type' => 'text',
						'length'    => 255,
						'empty'     => false,
						'field'     => 'mls_id'),

		'fname' => array('caption'  => 'First name',
						'html_type' => 'text',
						'data_type' => 'text',
						'length'    => 255,
						'empty'     => false,
						'field'     => 'fname'),

		'lname' => array('caption' => 'Last name',
						'html_type' => 'text',
						'data_type' => 'text',
						'length'   => 255,
						'empty'    => false,
						'field'    => 'lname'),

		'mname' => array('caption' => 'Middle name',
						'html_type' => 'text',
						'data_type'     => 'text',
						'length'   => 255,
						'empty'    => true,
						'field'    => 'mname'),

		'phone' => array('caption' => 'Office phone',
						'data_type' => 'text',
						'html_type' => 'text',
						'length'   => 255,
						'empty'    => true,
						'field'    => 'phone'),

		'fax' => array('caption' => 'Fax number',
						'data_type'     => 'text',
						'html_type' => 'text',
						'length'   => 255,
						'empty'    => true,
						'field'    => 'fax'),
		
		'voice' => array('caption' => 'Mobile',
						'data_type'     => 'text',
						'html_type' => 'text',
						'length'   => 255,
						'empty'    => true,
						'field'    => 'voicemail'),

		'email' => array('caption' => 'E-mail',
						'data_type' => 'email',
						'html_type' => 'text',
						'length'   => 255,
						'empty'    => true,
						'field'    => 'email'),

		'address' => array('caption' => 'Address',
						'data_type' => 'text',
						'html_type' => 'textarea',
						'rows'     => 3,
						'empty'    => true,
						'field'    => 'address'),

		'buy_homes' => array('caption' => 'Buy homes',
						'data_type' => 'html',
						'html_type' => 'textarea',
						'rows'     => 3,
						'empty'    => true,
						'field'    => 'buy_homes'),

		'sell_homes' => array('caption' => 'Sell homes',
						'data_type' => 'html',
						'html_type' => 'textarea',
						'rows'     => 3,
						'empty'    => true,
						'field'    => 'sell_homes'),

		'slogan' => array('caption' => 'Slogan',
						'data_type' => 'html',
						'html_type' => 'textarea',
						'rows'     => 3,
						'empty'    => true,
						'field'    => 'slogan'),

		'photo' => array('caption' => 'Photo',
						'data_type' => 'file',
						'html_type' => 'file',
						'length'   => 255,
						'width'    => '',
						'height'   => '',
						'ask_width'    => '',
						'ask_height'   => '',
						'empty'    => true),

		'logo' => array('caption' => 'Logo',
						'data_type' => 'file',
						'html_type' => 'file',
						'ask_width'    => 135,
						'ask_height'   => 170,
						'length'   => 255,
						'empty'    => true),

		'info' => array('caption' => 'Personal information',
						'data_type' => 'text',
						'html_type' => 'textarea',
						'rows'     => 20,
						'empty'    => true,
						'field'    => 'info'));

	$banner_form = array (
		'name' => array('caption' => 'Name',
						'data_type' => 'text',
						'html_type' => 'text',
						'length'   => 255,
						'empty'    => false,
						'field'    => 'name'),

		'banner' => array('caption' => 'Picture',
						'data_type' => 'file',
						'html_type' => 'file',
						'width'    => 1200,
						'ask_width'    => 1200,
						'ask_height'   => 85,
						'empty'    => true));

	$check_form = array(
				'html'  => 'KRF_CheckText',
				'text'  => 'KRF_CheckText',
				'email' => 'KRF_validatemailboxname',
				'date'  => 'KRF_CheckDate',
				'file'  => 'KRF_CheckFile'
			);
?>
