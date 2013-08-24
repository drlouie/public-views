<form action="?" name="edit_settings_form" id="add_user_form" method="post" enctype="multipart/form-data">
<input type="hidden" name="act" value="settings" />
<input type="hidden" name="done" value="1" />
<?
	if (!defined('INNER')) exit;

	$errors = array();
	$is_err = false;
	$terminate = false;
	if ($done)
	{
		$login  = trim($login );
		$passwd = trim($passwd);
		$passwd_confirm = trim($passwd_confirm);

		if (empty($login))
		{
			$is_err = true;
			$errors['login'] = 'login couldn\'t be empty';
		}

		if (empty($passwd))
		{
			$is_err = true;
			$errors['passwd'] = 'password couldn\'t be empty';
		}

		if ($passwd !== $passwd_confirm)
		{
			$is_err = true;
			$errors['passwd_confirm'] = 'confirmation and password must be the same';
		}

		if (!$is_err)
		{
			$SQL->Query("UPDATE admin SET login='$login', passwd='$passwd'");
			$terminate = true;
		}
	}
	else
	{
		$db = $SQL->Query('SELECT login, passwd FROM admin LIMIT 0,1');
		list($login, $passwd) = $SQL->Fetchrow($db);
	}

	if (!$terminate)
	{
		$form = <<<FORM
			<br />
			<table width="100%"><tr><td><nobr>New login: </nobr></td>
			<td width="70%" ><input style="width:100%" type="text" name="login" value="$login" /></td>
			<td width="30%"><nobr><span style="color:red">{$errors['login']}</span></nobr></td></tr>
			<tr><td><nobr>New password: </nobr></td>
			<td width="70%"><input style="width:100%" type="password" name="passwd" value="$passwd" /></td>
			<td width="30%"><nobr><span style="color:red">{$errors['passwd']}</span></nobr></td></tr>
			<tr><td><nobr>Confirm new password: </nobr></td>
			<td width="70%"><input style="width:100%" type="password" name="passwd_confirm" value="$passwd_confirm" /></td>
			<td width="30%"><nobr><span style="color:red">{$errors['passwd_confirm']}</span></nobr></td></tr>
			</table>
FORM;
		
		$window['caption'] = 'Administrator settings';
		$window['inner'  ] = $form;
		$window['inner'  ] .= <<<BUTTONS
		<br />
		<table width="100%">
		<tr><td width="50%"><input style="width:50%" type="submit" value="Save changes" /></td><td width="50%">&nbsp;</td></tr></table>
BUTTONS;

		echo ShowWindow($window);
	}
	else
	{
		echo '<script>document.location.href="'.$main['root.com'].'manage";</script>';
	}
?>
</form>