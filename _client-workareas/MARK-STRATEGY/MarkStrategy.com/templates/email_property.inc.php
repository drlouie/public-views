<?
include "templates/mainheader.php";
?>
<?
	$is_err = false;
	$errmsg = array('email_to' => '(required)', 'email_from' => '(required)');

	if ($done)
	{
		$email_prop_to   = trim($email_prop_to  );
		$email_prop_from = trim($email_prop_from);

		$subj_prop = trim($subj_prop);
        $msg_prop  = trim($msg_prop );

        if ($email_prop_to == '')
        {
        	$is_err = true;
            $errmsg['email_to'] = '(required)';
        }
        else
        {
        	$email_to_arr = explode(',', $email_prop_to);
        	
        	foreach($email_to_arr as $k => $v)
        	{
        		$v = $email_to_att[$k] = trim($v);
        		if (!KRF_check_email($v))
        		{
        			$is_err = true;
        			$errmsg['email_to'] = 'invalid email';
        		}
        	}
        }

        if ($email_prop_from == '')
        {
        	$is_err = true;
            $errmsg['email_from'] = '(required)';
        }
        else if (!KRF_check_email($email_prop_from))
        {
        	$is_err = true;
   			$errmsg['email_from'] = 'invalid email';	
        }

        if (!$is_err)
        {
        	
        	//echo "From email:$email_prop_from<br />";
        	$href = "http://$HTTP_HOST/".sprintf($home_href, $id);
        	
        	$msg = <<<MESSAGE
        	$msg_prop <br /><hr size="1" wdth="100%" /><br />
        	Here is a property you might be interested in.<br />
        	[<a href="$href">$href</a>]<br />
        	Thank you,<br />
        	<a href="http://$HTTP_HOST">$HTTP_HOST</a>
MESSAGE;
        	foreach($email_to_arr as $v)
        	{
        		KRF_sendMessade($email_prop_from, '', $v, 
		   						$subj_prop, $msg, 'html');
        	}

        	if ($copy_prop)
            {
        		KRF_sendMessade($email_prop_from, '', $email_prop_from, 
		   						$subj_prop, $msg, 'html');
        	}
        }
	}

	if (!$done || $is_err)
	{
?>
<form method='post' action='?'>
<input type="hidden" name="done" value="1" />
<input type="hidden" name="act" value="email_property" />
<input type="hidden" name="id"  value="<?= $id?>" />

	<tr valign=top>
		<td width=40><img src="images/pix.gif" height=1 width=40><br></td>
		<td>
		<b style="color: #860116;">EMAIL PROPERTY</b><br>
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
			<td><b>Email To:</b></td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td valign=top>
			Separate multiple addresses by commas (,)<br>
			<input type='text' size='30' maxlength='100' name='email_prop_to' value="<?= $email_prop_to?>" /> <font color='red'><?= $errmsg['email_to']?></font>
			</td>
		</tr>

		<tr>
			<td><b>Your Email:</b></td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td><input type='text' size='30' maxlength='40' name="email_prop_from" value="<?= $email_prop_from?>" /> <font color='red'><?= $errmsg['email_from']?></font></td>
		</tr>

		<tr>
			<td>&nbsp</td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td><input class="check" type='checkbox' name='copy_prop' value="1" <?= ($copy) ? 'checked' : ''?> /> Send me a copy as well</td>
		</tr>

		<tr>
			<td>Subject:</td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td><input type='text' size='30'  maxlength='100' name='subj_prop' value='<?= $subj_prop?>'></td>
		</tr>

		<tr>
			<td>Subject:</td>
			<td width=40><img src="images/pix.gif" width=40 height=1><br></td>
			<td>The link will be added to the end of your message.<br><textarea name='msg_prop' cols='40' rows='6'><?= $msg_prop?></textarea></td>
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


<?
	}
	else
	{
		echo 'E-mail message with information about selected property was successfully sent. Thank you!';
	}
?>
<?
include "templates/mainfooter.php";
?>