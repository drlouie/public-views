<?
include "templates/mainheader.php";
	$month = array('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December');
	$time  = array('8:30' => '8:30 AM',
					"9:00" => '9:00 AM',
					"9:30" => '9:30 AM',
					"10:00" => '10:00 AM',
					"10:30" => '10:30 AM',
					"11:00" => '11:00 AM',
					"11:30" => '11:30 AM',
					"12:00" => '12:00 PM',
					"12:30" => '12:30 PM',
					"13:00" => '1:00 PM',
					"13:30" => '1:30 PM',
					"14:00" => '2:00 PM',
					"14:30" => '2:30 PM',
					"15:00" => '3:00 PM',
					"15:30" => '3:30 PM',
					"16:00" => '4:00 PM',
					"16:30" => '4:30 PM',
					"17:00" => '5:00 PM',
					"17:30" => '5:30 PM',
					"18:00" => '6:00 PM',
					"18:30" => '6:30 PM',
					"19:00" => '7:00 PM',
					"19:30" => '7:30 PM',
					"20:00" => '8:00 PM');
?>
<?
	if (!$done || $is_err)
	{
?>
<form method="post" action="?">
<input type="hidden" name="act"  value="shedule_form" />
<input type="hidden" name="done" value="1" />
<input type="hidden" name="id"   value="<?= $id?>"  />

	<tr valign=top>
		<td width=40><img src="images/pix.gif" height=1 width=40><br></td>
		<td>
		<b style="color: #860116;">SCHEDULE A SHOWING</b><br>
		</td>
	</tr>

	<tr>
		<td colspan=2><img src="images/pix.gif" height=15 width=1><br></td>
	</tr>

	<tr valign=top>
		<td width=40><img src="images/pix.gif" height=1 width=40><br></td>
		<td>
		<table cellpadding=0 cellspacing=0 border=0>
		<tr>
			<td><b>Name:</b></td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td valign=top>
			<input size="30" name="shedule_name" value="<?= $shedule_name?>" tabindex="1" maxlength="255" /> <span style="color:red"><?= $errors['shedule_name']?></span>
			</td>
		</tr>

		<tr>
			<td><b>E-Mail:</b></td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td><input size="30" name="shedule_email" value="<?= $shedule_email?>" tabindex="2" maxlength="255" /> <span style="color:red"><?= $errors['shedule_email']?></span></td>
		</tr>

		<tr>
			<td><b>Phone Number:</b></td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td><input size="30" name="shedule_phone" value="<?= $shedule_phone?>" tabindex="3" maxlength="255" /> <span style="color:red"><?= $errors['shedule_phone']?></span></td>
		</tr>

		<tr>
			<td>Preferred Date:</td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td>
			<select name="shedule_date[month]">
			<option value="">Month</option><option></option>
			<?
				foreach($month as $i => $m)
				{
					$n = $i + 1;
					$sel = ($shedule_date['month'] == $n) ? 'selected' : '';
					?><option value="<?= $n?>" <?= $sel?>><?= $m?></option><?
				}
			?>
			</select>
			<select name="shedule_date[day]"><option value="">Day</option><option></option>
			<?
				for($i=1; $i<32; $i++)
				{
					$sel = ($shedule_date['day'] == $i) ? 'selected' : '';
					?><option value="<?= $i?>" <?= $sel?>><?= $i?></option><?
				}
			?>
			</select> <span style="color:red"><?= $errors['shedule_date']?>
			</td>
		</tr>

		<tr>
			<td>Preferred Time:</td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td>
				<select name="shedule_date[time]" tabindex="5"><option value=":">Time</option><option value=":"></option>
					<?
						foreach($time as $i => $m)
						{
							$sel = ($shedule_date['time'] == $i) ? 'selected' : '';
							?><option value="<?= $i?>" <?= $sel?>><?= $m?></option><?
						}
					?>
				</select>
			</td>
		</tr>

		<tr>
			<td>Alternate Date:</td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td>
			<select name="shedule_date_alt[month]">
			<option value="">Month</option><option></option>
			<?
				foreach($month as $i => $m)
				{
					$n = $i + 1;
					$sel = ($shedule_date_alt['month'] == $n) ? 'selected' : '';
					?><option value="<?= $n?>" <?= $sel?>><?= $m?></option><?
				}
			?>
			</select>
			<select name="shedule_date_alt[day]"><option value="">Day</option><option></option>
			<?
				for($i=1; $i<32; $i++)
				{
					$sel = ($shedule_date_alt['day'] == $i) ? 'selected' : '';
					?><option value="<?= $i?>" <?= $sel?>><?= $i?></option><?
				}
			?>
			</select> <span style="color:red"><?= $errors['shedule_date_alt']?></span>			</td>
		</tr>

		<tr>
			<td>Alternate Time:</td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td>
				<select name="shedule_date_alt[time]" tabindex="5"><option value=":">Time</option><option value=":"></option>
					<?
						foreach($time as $i => $m)
						{
							$sel = ($shedule_date_alt['time'] == $i) ? 'selected' : '';
							?><option value="<?= $i?>" <?= $sel?>><?= $m?></option><?
						}
					?>
				</select>
			</td>
		</tr>

		<tr>
			<td valign=top>Comments:</td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td><textarea name="shedule_notes" rows="8" wrap="virtual" cols="30" tabindex="8"><?= $sheduled_notes?></textarea></td>
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
			<td colspan=3 align=center><input type='submit' value='Submit' /></td>
		</tr>

		<tr>
			<td colspan=3><img src="images/pix.gif" height=20 width=1><br></td>
		</tr>

		<tr>
			<td colspan=3 align=right><a href="<?= sprintf($home_href_nf, $id)?>" style="color: #860116;"><b>Back to the featured listing view</b></a><br></td>
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
		echo "Your request successfully saved. Thank you!";
	}
?>

<?
include "templates/mainfooter.php";
?>