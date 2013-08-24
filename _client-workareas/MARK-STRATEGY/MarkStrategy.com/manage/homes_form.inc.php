<?
	if (!defined('INNER')) exit;

	if ($done && !is_array($f))
	{
		$f = array();
	}

	$DF = new KRF_dynamic_form('homes', $SQL, $f, $undeleting_fields);

	if ($DF)
	{
		$DF->ValidateForm();

		echo '<script>'.$DF->ShowJS().'</script>';
	
		$window['caption'] = 'Listing entry form';
		$window['inner'  ] = $DF->ShowAddingForm().'<hr size="1" width="100%" />';
		$window['inner'  ] .= $DF->ShowLayers();

		echo ShowWindow($window);

		echo "<br />".$DF->ShowMenu();
	}
?>