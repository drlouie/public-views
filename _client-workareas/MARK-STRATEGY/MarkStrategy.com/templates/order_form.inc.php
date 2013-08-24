<?
include "templates/mainheader.php";
?>
<?
	$sql = "select buy_homes  from user where fname='$u_fname' and mname='$u_mname' and lname='$u_lname'";
	$result = mysql_query($sql);
	if ($result)
	{
		$data = mysql_fetch_array($result);
		$u_buy_homes = str_replace("\\'", "'", $data["buy_homes"]);
		$u_buy_homes = str_replace('\\"', '"', $u_buy_homes);

		$u_buy_homes = str_replace("\r\n", "<br>", $u_buy_homes); 		
		$u_buy_homes = str_replace("\n", "<br>", $u_buy_homes); 		

	}

	if (!$done || $is_err)
	{
		if (!$errors['fname']) $errors['fname'] = '(required)';
		if (!$errors['lname']) $errors['lname'] = '(required)';
		if (!$errors['email']) $errors['email'] = '(required)';
		if (!$errors['phone']) $errors['phone'] = '(required)';
?>

	<form id="order_form" method="post">
	<input type="hidden" name="act" value="order" />
	<input type="hidden" name="done" value="1" />

	
	<tr valign=top>
		<td width=40><img src="images/pix.gif" height=1 width=40><br></td>
		<td>
		<b style="color: #860116;">BUYING A HOME</b><br>
		</td>
	</tr>

	<tr>
		<td colspan=2><img src="images/pix.gif" height=15 width=1><br></td>
	</tr>

	<tr valign=top>
		<td width=40><img src="images/pix.gif" height=1 width=40><br></td>
		<td>
		<?=$u_buy_homes?>
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
			<td><input type="text" name="phone" size="20" value="<?= $phone?>" /> <span style="color:red"><?= $errors['phone']?></span></td>
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
			<option value=""></option>
			<?
			foreach($prop_types as $v => $c)
			{
				$sel = ($type == $v && $type !== '') ? 'selected' : '';
				?>
				<option value="<?= $v?>" <?= $sel?>><?= $c?></option>
			<?
			}
			?>
			</select> <span style="color:red"><?= $errors['type']?></span>
			</td>
		</tr>


		<tr>
			<td>Price Range:</td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td>
			<select name="price_min">
			<option value="no minimum">No Minimum</option>
			<?
			echo $price_min;
			echo $price_max;
			foreach($price_ranges as $v => $c)
			{
				$sel = ($price_min == $v && $price_min != 'no minimum') ? 'selected' : '';
				?>
				<option value="<?= $v?>" <?= $sel?>><?= $c?></option>
			<?
			}
			?>
			</select> <span style="color:red"><?= $errors['price_min']?></span></nobr> to 
			<select name="price_max">
			<option value="no maximum">No Maximum</option>
			<?
			foreach($price_ranges as $v => $c)
			{
				$sel = ($price_max == $v && $price_max != 'no maximum') ? 'selected' : '';
				?> 
				<option value="<?= $v?>" <?= $sel?>><?= $c?>.</option>
			<?
			}
			?>
			</select> <span style="color:red"><?= $errors['price_max']?></span>			
			</td>
		</tr>

		<tr>
			<td>Minimum Number Of Bedrooms:</td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td><input type="text" name="bedr" size="20" value="<?= $bedr?>" /> <span style="color:red"><?= $errors['bedr']?></span></nobr></td>
		</tr>

		<tr>
			<td>Minimum Number Of Bathrooms:</td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td><input type="text" name="bathr" size="20" value="<?= $bathr?>" /> <span style="color:red"><?= $errors['bathr']?></span></nobr></td>
		</tr>

		<tr>
			<td>Minimum Square Footage:</td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td><input type="text" name="square" value="<?= $square?>" size="20" /> <span style="color:red"><?= $errors['square']?></span></nobr></td>
		</tr>

		<tr>
			<td>How Soon Are You Looking To Buy:</td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td>
			<select name="soon">
			<?
			foreach($soons as $v => $c)
			{
				$sel = ($soon === $v) ? 'selected' : '';
				?>
				<option value="<?= $v?>" <?= $sel?>><?= $c?></option>
			<?
			}
			?>
			</select> <span style="color:red"><?= $errors['soon']?></span>
			</td>
		</tr>

		<tr>
			<td>Cities Desired:</td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td><textarea cols="20" rows="5" name="city_desired"><?= $city_desired?></textarea> <span style="color:red"><?= $errors['city_desired']?></span></nobr></td>
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
			<td>Address:</td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td><input type="text" name="address" size="20" value="<?= $address?>" /> <span style="color:red"><?= $errors['address']?></span></td>
		</tr>

		<tr>
			<td>City:</td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td><input type="text" name="city" size="20" value="<?= $city?>" /> <span style="color:red"><?= $errors['city']?></span></td>
		</tr>

		<tr>
			<td>State/Province:</td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td>
			<select name="state">
			<option value="state">State</option>
			<?
			foreach($states as $v => $c)
			{
				$sel = ($state === $v) ? 'selected' : '';
				?>
				<option value="<?= $v?>" <?= $sel?>><?= $c?></option>
			<? } ?>
			</select> <span style="color:red"><?= $errors['state']?></span>			
			</td>
		</tr>

		<tr>
			<td>Zip/Postal Code:</td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td><input type="text" name="zip" size="10" value="<?= $zip?>" /> <span style="color:red"><?= $errors['zip']?></span></nobr></td>
		</tr>

		<tr>
			<td>Questions Or Comments:</td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td><textarea name="notes" cols="20" rows="5"><?= $notes?></textarea> <span style="color:red"><?= $errors['notes']?></span></nobr></td>
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
			<td colspan=2 align=center><input style="width:50%" type="reset" value="Reset Information" /></td>
			<td align=center><input style="width:50%" type="submit" value="Send Information" /></td>
		</tr>

		<tr>
			<td colspan=3><img src="images/pix.gif" height=20 width=1><br></td>
		</tr>

		</table>

		</td>
	</tr>



<table>


</form>
<?
	}
	else
	{
		echo '<br><br><blockquote><h2>Your information was successfully submited. Thank you!</h2></blockquote>';
	}
?>

<?
include "templates/mainfooter.php";
?>