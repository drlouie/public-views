<?
	$url_address=str_replace(" ","+",$data['address']['value']);
	$exclude = array('address', 'subject');
?>
<h2>Agent</h2><br />
<table><tr>
<td>
<?
	if (file_exists($photo_img))
	{
		?><img src="<?= $photo_img?>" /><?
	}
?>
</td>
<td width="20">&nbsp;</td>
<td valign="top">
<p><b><?= $u_fname.' '.$u_mname.' '.$u_lname?></b></p>
<?
	if ($u_phone) echo "<p>Phone: <b>$u_phone</b></p>";
	if ($u_phone2) echo "<p>Phone2: <b>$u_phone2</b></p>";
	if ($u_fax) echo "<p>Fax: <b>$u_fax</b></p>";
	if ($u_voicemail) echo "<p>Mobile: <b>$u_voicemail</b></p>";
	if ($email_to) echo "<p><a href='mailto:$email_to'>$email_to</a></p>";
?>
</td></tr></table>
<br /><br /><br />
<h2>Information</h2>
<table width="100%">
<tr><td><img src = "<?= $data['home_photo']['src']?>" /></td>
<td width="20"><img src="" alt="" width="20" height="0" /></td>
<td width="100%" valign="top">
<br /><h3><?= $data['subject']['value']?></h3>
<table>
<?
	foreach($data as $k => $v)
	{
		if ($v['value'] && !in_array($k, $exclude))
		{
			?><tr><td><?= $v['caption']?>: </td><td><b><?= $v['value']?></b></td></tr><?
		}
	}
?>
</table>
</td></tr>
<tr><td colspan="3"><?= $data['notes']['value']?></td></tr>
</table>
<br/>

<br/>
<center><a href=javascript:window.print() ><B>Print</B></a><img src="" width="40" alt="" height="0" /><a href=javascript:self.close() ><B>Close this window</B></a></center>
<br><br><br><br><br>