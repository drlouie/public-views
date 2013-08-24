<?
	if (!defined('INNER')) exit;


        $db_conf = array(
                'user'   => 'robert_orange21',
                'passwd' => 'ora12nge',
                'host'   => 'localhost',
                'db'     => 'robert_orange21'
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

	$main = array(
		'root.com'   => 'http://www.markstrategy.com/',
		'files' => array(
			'logo'  => '../img/logo/',
			'photo' => '../img/photo/',
			'home_photo' => '../img/homes/',
			'link_picture' => '../img/links/')
	);

	$action_list = array(
		'login_form' => 'login.inc.php',
		'default'    => 'edit_user.inc.php',
		'edit_user'  => 'edit_user.inc.php',
		'supply_user'  => 'supply.inc.php',
		'delete_home'  => 'supply.inc.php',
		'add_home'     => 'add_home.inc.php',
		'edit_home'    => 'edit_home.inc.php',
		'homes_csv'    => 'homes_csv.inc.php',
		'shedules'    => 'shedulers.inc.php',
		'taskbar'     => 'taskbar.inc.php',
		'sell'        => 'sell.inc.php',
		'buy'         => 'buy.inc.php',
		'sell_csv'    => 'sell_csv.inc.php',
		'buy_csv'     => 'buy_csv.inc.php',
		'sell_txt'    => 'sell_txt.inc.php',
		'buy_txt'     => 'buy_txt.inc.php',
		'shedules_csv' => 'shedules_csv.inc.php',
		'shedules_txt' => 'shedules_txt.inc.php',

		'delete_link'  => 'links.inc.php',
		'links_user'   => 'links.inc.php',
		'add_link'     => 'links_add.inc.php',
		'edit_link'    => 'links_edit.inc.php',

		'logout'      => 'logout.inc.php');

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

		'slogan' => array('caption' => 'Slogan',
						'data_type' => 'html',
						'html_type' => 'textarea',
						'rows'     => 3,
						'empty'    => true,
						'field'    => 'slogan'),

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

		'photo' => array('caption' => 'Photo',
						'data_type' => 'file',
						'html_type' => 'file',
						'width'    => '',
						'height'   => '',
						'ask_width'    => '',
						'ask_height'   => '',
						'length'   => 255,
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

	$check_form = array(
				'html'  => 'KRF_CheckText',
				'text'  => 'KRF_CheckText',
				'email' => 'KRF_validatemailboxname',
				'file'  => 'KRF_CheckFile'
			);
?>
