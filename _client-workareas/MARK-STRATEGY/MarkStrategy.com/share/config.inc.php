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

	$main = array (
		'root.com'   => 'http://markstrategy.com/',
		'files' => array(
			'banner' => 'img/banner/',
			'logo'   => 'img/logo/',
			'photo'  => 'img/photo/',
			'home_photo'   => 'img/homes/',
			'link_picture' => 'img/links/')
	);

	$contact_form = array(
	    'email' => array('caption' => 'E-mail',
						'data_type' => 'email',
						'html_type' => 'text',
						'length'   => 255,
						'empty'    => false),
		
		'fname' => array('caption'  => 'First name',
						'html_type' => 'text',
						'data_type' => 'text',
						'length'    => 255,
						'empty'     => false),

		'lname' => array('caption' => 'Last name',
						'html_type' => 'text',
						'data_type' => 'text',
						'length'   => 255,
						'empty'    => true),

		'notes' => array('caption' => 'Question or Comments',
						'data_type' => 'text',
						'html_type' => 'textarea',
						'rows'     => 5,
						'empty'    => true),

		'address' => array('caption' => 'Address',
						'data_type' => 'text',
						'html_type' => 'textarea',
						'rows'     => 3,
						'empty'    => true),

		'phone' => array('caption' => 'Office phone',
						'data_type' => 'text',
						'html_type' => 'text',
						'length'   => 255,
						'empty'    => false),

		'fax' => array('caption' => 'Fax number',
						'data_type'     => 'text',
						'html_type' => 'text',
						'length'   => 255,
						'empty'    => true),
		
		'city' => array('caption' => 'City',
						'data_type' => 'text',
						'html_type' => 'text',
						'length'   => 255,
						'empty'    => true),

		'state' => array('caption' => 'State',
						'data_type' => 'text',
						'html_type' => 'text',
						'length'   => 255,
						'size'     => 10,
						'empty'    => true),

		'zip' => array('caption' => 'Zip',
						'data_type' => 'text',
						'html_type' => 'text',
						'length'   => 255,
						'size'     => 10,
						'empty'    => true));
?>
