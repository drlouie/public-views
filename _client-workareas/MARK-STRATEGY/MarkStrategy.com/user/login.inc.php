<?
	if (!defined('INNER')) exit;
	
	$window['menu'   ] = '';
	$window['caption'] = 'Agent login';
	$window['inner'] = <<<FORM
		<br />
		<span style="color:red">$message</span>
		<br />
		<form name="login_form" method="post" action="?">
		<input type="hidden" name="act" value="login" />
		<table>
		<tr>
			<td>login:</td>
			<td><input name="login" type="text" value="$login" /></td>
		</tr>
		<tr>
			<td>password:</td>
			<td><input name="passwd" type="password" value="" />&nbsp;&nbsp<input type="submit" value="enter >>>" /></td>
		</tr>
		</table>
		</form>
FORM;

	echo ShowWindow($window);
?>