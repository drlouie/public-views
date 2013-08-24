<?
include "templates/mainheader.php";
?>
<?
	$sql = "select sell_homes from user where fname='$u_fname' and mname='$u_mname' and lname='$u_lname'";
	$result = mysql_query($sql);
	if ($result)
	{
		$data = mysql_fetch_array($result);
		$u_sell_homes = $data["sell_homes"];


		$u_sell_homes = str_replace("\\'", "'", $u_sell_homes);
		$u_sell_homes = str_replace('\\"', '"', $u_sell_homes);

		$u_sell_homes = str_replace("\r\n", "<br>", $u_sell_homes); 		
		$u_sell_homes = str_replace("\n", "<br>", $u_sell_homes); 		

	}


	if (!$done || $is_err)
	{
		if (!$errors['fname']) $errors['fname'] = '(required)';
		if (!$errors['lname']) $errors['lname'] = '(required)';
		if (!$errors['email']) $errors['email'] = '(required)';
		if (!$errors['client_phone']) $errors['client_phone'] = '(required)';
?>
	<form id="order_form" method="post">
	<input type="hidden" name="act" value="sell" />
	<input type="hidden" name="done" value="1" />

	<tr valign=top>
		<td width=40><img src="images/pix.gif" height=1 width=40><br></td>
		<td>
		<b style="color: #860116;">SELLING A HOME</b><br>
		</td>
	</tr>

	<tr>
		<td colspan=2><img src="images/pix.gif" height=15 width=1><br></td>
	</tr>

	<tr valign=top>
		<td width=40><img src="images/pix.gif" height=1 width=40><br></td>
		<td>
		<?=$u_sell_homes?>
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
			<td><b>First Name:</b></td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td><input type="text" name="fname" size="20" value="<?= $fname?>" /> <span style="color:red"><?= $errors['fname']?></td>
		</tr>

		<tr>
			<td><b>Last Name:</b></td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td><input type="text" name="lname" size="20" value="<?= $fname?>" /> <span style="color:red"><?= $errors['lname']?></td>
		</tr>

		<tr>
			<td><b>E-Mail:</b></td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td><input type="text" name="email" size="20" value="<?= $fname?>" /> <span style="color:red"><?= $errors['email']?></td>
		</tr>

		<tr>
			<td><b>Phone:</b></td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td><input type="text" name="client_phone" size="20" value="<?= $client_phone?>" /> <span style="color:red"><?= $errors['client_phone']?></td>
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
			<td>Type Of Property:</td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td>
			<select name="type">
			<?
			foreach($prop_types as $v => $c)
			{
				$sel = ($type === $v) ? 'selected' : '';
				?>
				<option value="<?= $v?>" <?= $sel?>><?= $c?></option>
			<? } ?> </select> <span style="color:red"><?= $errors['type']?></span>
			</td>
		</tr>

		<tr>
			<td>Desired Sales Price:</td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td>
			<select name="price">
			<option value=""></option>
			<?
			foreach($price_ranges as $v => $c)
			{
				$sel = ($price == $v && $price != '') ? 'selected' : '';
				?>
				<option value="<?= $v?>" <?= $sel?>><?= $c?></option>
			<? } ?>
			</select> <span style="color:red"><?= $errors['price']?></span>
			</td>
		</tr>

		<tr>
			<td>Number Of Bedrooms:</td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td><input type="text" name="bedr" size="20" value="<?= $bedr?>" /> <span style="color:red"><?= $errors['bedr']?></td>
		</tr>

		<tr>
			<td>Number Of Bathrooms:</td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td><input type="text" name="bathr" size="20" value="<?= $bathr?>" /> <span style="color:red"><?= $errors['bathr']?></td>
		</tr>

		<tr>
			<td>Square Footage:</td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td><input type="text" name="square" size="20" value="<?= $square?>" /> <span style="color:red"><?= $errors['square']?></td>
		</tr>

		<tr>
			<td>Address:</td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td><input type="text" name="home_address" size="20" value="<?= $home_address?>" /> <span style="color:red"><?= $errors['home_address']?></td>
		</tr>

		<tr>
			<td>City:</td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td><input type="text" name="home_city" size="20" value="<?= $home_city?>" /> <span style="color:red"><?= $errors['home_city']?></td>
		</tr>

		<tr>
			<td>State:</td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td>
			<select name="home_state">
			<option value="state">State</option>
			<?
			foreach($states as $v => $c)
			{
				$sel = ($home_state === $v) ? 'selected' : '';
				?><option value="<?= $v?>" <?= $sel?>><?= $c?></option>
			<? } ?>
			</select> <span style="color:red"><?= $errors['home_state']?></span>
			</td>
		</tr>

		<tr>
			<td>Zip:</td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td><input type="text" name="home_zip" size="20" value="<?= $home_zip?>" /> <span style="color:red"><?= $errors['home_zip']?></td>
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
			<td>Questions Or Comments:</td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td><textarea name="notes" cols="20" rows="5"><?= htmlspecialchars($notes)?></textarea> <span style="color:red"><?= $errors['notes']?></span></td>
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
			<td colspan=2 align=center><input style="width:70%" type="reset" value="Reset Information" /></td>
			<td align=center><input style="width:70%" type="submit" value="Send Information" /></td>
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
		echo '<br><br><blockquote><h2>Your information was successfully submited. Thank you!</h2></blockquote>';
	}
?>
<p>
<p>
<p>
<?
include "templates/mainfooter.php";
?>