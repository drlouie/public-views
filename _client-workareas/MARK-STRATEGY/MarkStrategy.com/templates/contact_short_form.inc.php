<?
include "templates/mainheader.php";
?>

<?
	if (!$done || $is_err)
	{
?>
	<form id="contact_form" method="post" action="?">
	<input type="hidden" name="act" value="<?= $act?>" />
	<input type="hidden" name="done" value="1" />
	<input type="hidden" name="wizard_act"  value="<?= $wizard_act?>" />

	<tr valign=top>
		<td width=40><img src="images/pix.gif" height=1 width=40><br></td>
		<td>
		<b style="color: #860116;">SEARCH THE ENTIRE HOME MARKET NOW!</b><br>
		</td>
	</tr>

	<tr>
		<td colspan=2><img src="images/pix.gif" height=15 width=1><br></td>
	</tr>

	<tr valign=top>
		<td width=40><img src="images/pix.gif" height=1 width=40><br></td>
		<td>
		<table cellpadding=0 cellspacing=4 border=0>
		<tr>
			<td><b>Name:</b></td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td><input type="text" name="fname" size="20" value="<?= $fname?>" /> <span style="color:red"><?= $errors['fname']?></td>
		</tr>

		<tr>
			<td><b>Phone:</b></td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td><input type="text" name="phone" size="20" value="<?= $phone?>" /> <span style="color:red"><?= $errors['phone']?></td>
		</tr>

		<tr>
			<td><b>Email:</b></td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td><input type="text" name="email" size="20" value="<?= $email?>" /> <span style="color:red"><?= $errors['email']?></td>
		</tr>


		<tr>
			<td colspan=3><img src="images/pix.gif" height=5 width=1><br></td>
		</tr>
		<tr style="background: #cccccc">
			<td colspan=3><img src="images/pix.gif" height=1 width=1><br></td>
		</tr>
		<tr>
			<td colspan=3><img src="images/pix.gif" height=5 width=1><br></td>
		</tr>

		<tr>
			<td colspan=2 align=center><input Xstyle="width:95%" type="submit" value="Submit Information" /></td>
		</tr>

		<tr>
			<td colspan=3><img src="images/pix.gif" height=20 width=1><br></td>
		</tr>

		</table>
		</td>
	</tr>

	</form>
<?
	}
	else
	{
		echo 'E-mail message with your contact was successfully sent to the agent. Thank you!';
		
		if ($wizard_act)
		{
			echo '<script>top.document.location.href = "'.$search_form_href_nf.'";</script>';
		}
	}
?>
<p>
<p>
<?
include "templates/mainfooter.php";
?>