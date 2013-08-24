<html>
<head>
<title></title>
<link rel=stylesheet type=text/css href="styles.css">
</head>

<body>

<table width=100% style="background: #960018; " cellpadding=0 cellspacing=0 border=0>

<tr>
<!-- Begin: Left menu and contacts -->
	<td valign=top>

	<table width=100% cellpadding=0 cellspacing=0 border=0>
	<tr class="text">
		<td width=10><img src="images/pix.gif" width=10 height=1><br></td>
		<td width=100%><span style="width: 135; overflow: hidden; text-overflow: ellipsis; " title="<?=$u_fname?> <?=$u_mname?> <?=$u_lname?>"><b><?=$u_fname?> <?=$u_mname?> <?=$u_lname?></b></span></td> 
	</tr>
	
	<tr>
		<td colspan=2><img src="imges/pix.gif" height=3><br></td>
	</tr>

	<tr style="background: #860116;">
		<td colspan=2><img src="imges/pix.gif" height=12 width=1></td>
	</tr>
	<tr class="contacts" style="background: #860116;"> 
		<td><img src="images/pix.gif" width=10 height=1></td>
		<td mowrap>
		<table width=100% class=text cellpadding=0 cellspacing=0 border=0>

		<? if ($u_phone != "") { ?>
		<tr>
			<td nowrap class=text><b>Office:</b></td>
			<td width=4><img src="imges/pix.gif" height=1 width=4></td>
			<td nowrap align=left class=text><?=$u_phone; ?></td>
			<td nowrap width=100%><img src="imges/pix.gif" height=1 width=10></td>
		</tr>
		<? } ?>			

		<? if ($u_fax != "") { ?>
		<tr>
			<td nowrap class=text><b>Fax:</b></td>
			<td width=4><img src="imges/pix.gif" height=1 width=4></td>
			<td nowrap align=left class=text><?=$u_fax; ?></td>
			<td nowrap><img src="imges/pix.gif" height=1 width=10></td>
		</tr>
		<? } ?>			

		<? if ($u_voicemail != "") { ?>
		<tr>
			<td nowrap class=text><b>Mobile:</b></td>
			<td width=4><img src="imges/pix.gif" height=1 width=4></td>
			<td nowrap align=left class=text><?=$u_voicemail; ?></td>
			<td nowrap><img src="imges/pix.gif" height=1 width=10></td>
		</tr>
		<? } ?>			

		<? if ($email_to != "") { ?>
		<tr>
			<td nowrap class=text><b>Email:</b></td>
			<td width=4><img src="imges/pix.gif" height=1 width=4></td>
			<td nowrap align=left class=text><a href="mailto: <?=$email_to; ?>" class="contacts">Email Me Now!</a></td>
			<td nowrap><img src="imges/pix.gif" height=1 width=10></td>
		</tr>
		<? } ?>			

		</table>

		</td>
	</tr>
	<tr style="background: #860116;">
		<td colspan=2><img src="images/pix.gif" height=24 width=1></td>
	</tr>


	<tr>
		<td colspan=2>
		<table class="text" width=100% cellpadding=0 cellspacing=0 border=0>
<!-- Begin: Menu Item -->
		<tr style="background: #ffffff;">
			<td colspan=3><img src="images/pix.gif" height=1></td>
		</tr> 
		<tr class=text >
			<td colspan=3><img src="images/pix.gif" height=3><br></td>		
		</tr>
		<tr class=text >
			<td><img src="images/pix.gif" height=1 width=10></td>
			<td valign=middle>
			<a href="/?" class="text" target="_top"><b>Featured Listings</b></a>
			</td>
			<td><img src="images/pix.gif" height=1 width=10></td>
		</tr>
		<tr class=text >
			<td colspan=3><img src="images/pix.gif" height=3></td>		
		</tr>
<!-- End: Menu Item -->


<!-- Begin: Menu Item -->
		<tr style="background: #ffffff;">
			<td colspan=3><img src="images/pix.gif" height=1></td>
		</tr> 
		<tr class=text >
			<td colspan=3><img src="images/pix.gif" height=3><br></td>		
		</tr>
		<tr class=text >
			<td><img src="images/pix.gif" height=1 width=10></td>
			<td valign=middle>
			<a href="<?= $order_form_href_nf?>" target="_top" class="text"><b>Buying a Home</b></a>
			</td>
			<td><img src="images/pix.gif" height=1 width=10></td>
		</tr>
		<tr class=text >
			<td colspan=3><img src="images/pix.gif" height=3></td>		
		</tr>
<!-- End: Menu Item -->

<!-- Begin: Menu Item -->
		<tr style="background: #ffffff;">
			<td colspan=3><img src="images/pix.gif" height=1></td>
		</tr> 
		<tr class=text >
			<td colspan=3 height=3><img src="images/pix.gif" height=3><br></td>		
		</tr>
		<tr class=text >
			<td><img src="images/pix.gif" height=1 width=10></td>
			<td valign=middle>
			<a href="<?= $sell_form_href_nf?>" class="text" target="_top"><b>Selling a Home</b></a>
			</td>
			<td><img src="images/pix.gif" height=1 width=10></td>
		</tr>
		<tr class=text >
			<td colspan=3><img src="images/pix.gif" height=3></td>		
		</tr>
<!-- End: Menu Item -->

<!-- Begin: Menu Item -->
		<tr style="background: #ffffff;">
			<td colspan=3><img src="images/pix.gif" height=1></td>
		</tr> 
		<tr class=text >
			<td colspan=3><img src="images/pix.gif" height=3><br></td>		
		</tr>
		<tr class=text >
			<td><img src="images/pix.gif" height=1 width=10></td>
			<td valign=middle nowrap>
			<a href="<?= $contact_mls_href?>" class="text" target="_top"><b>Home Search</b></a>
			</td>
			<td><img src="images/pix.gif" height=1 width=10></td>
		</tr>
		<tr class=text >
			<td colspan=3><img src="images/pix.gif" height=3></td>		
		</tr>
<!-- End: Menu Item -->

<!-- Begin: Menu Item -->
		<tr style="background: #ffffff;">
			<td colspan=3><img src="images/pix.gif" height=1></td>
		</tr> 
		<tr style="background: #860116;">
			<td colspan=3><img src="images/pix.gif" height=3><br></td>		
		</tr>
		<tr style="background: #860116;">
			<td><img src="images/pix.gif" height=1 width=10></td>
			<td valign=middle nowrap>
			<a href="/?act=link&url=<?= $taskbar[0]['url_nf']?>" class="text" target="_top"><b>Home Financing</b></a>
			</td>
			<td><img src="images/pix.gif" height=1 width=10></td>
		</tr>
		<tr style="background: #860116;">
			<td colspan=3><img src="images/pix.gif" height=3></td>		
		</tr>
<!-- End: Menu Item -->

<!-- Begin: Menu Item -->
		<tr style="background: #ffffff;">
			<td colspan=3><img src="images/pix.gif" height=1></td>
		</tr> 
		<tr class=text >
			<td colspan=3><img src="images/pix.gif" height=3><br></td>		
		</tr>
		<tr class=text >
			<td><img src="images/pix.gif" height=1 width=10></td>
			<td valign=middle>
			<a href="index.php?act=links" target="_top" class="text"><b>Resource Center</b></a>
			</td>
			<td><img src="images/pix.gif" height=1 width=10></td>
		</tr>
		<tr class=text >
			<td colspan=3><img src="images/pix.gif" height=3></td>		
		</tr>
<!-- End: Menu Item -->

<!-- Begin: Menu Item -->
		<tr style="background: #ffffff;">
			<td colspan=3><img src="images/pix.gif" height=1></td>
		</tr> 
		<tr class=text >
			<td colspan=3><img src="images/pix.gif" height=3></br></td>		
		</tr>
		<tr class=text >
			<td><img src="images/pix.gif" height=1 width=10></td>
			<td valign=middle>
			<a href="<?= $info_href?>" target="_top" class="text"><b>About Me</b></a>
			</td>
			<td><img src="images/pix.gif" height=1 width=10></td>
		</tr>
		<tr class=text >
			<td colspan=3><img src="images/pix.gif" height=3></td>		
		</tr>
<!-- End: Menu Item -->

<!-- Begin: Menu Item -->
		<tr style="background: #ffffff;">
			<td colspan=3><img src="images/pix.gif" height=1></td>
		</tr> 
		<tr class=text >
			<td colspan=3><img src="images/pix.gif" height=3><br></td>		
		</tr>
		<tr class=text >
			<td><img src="images/pix.gif" height=1 width=10></td>
			<td valign=middle>
			<a href="<?= $contact_form_href?>" target="_top" class="text"><b>Contact Me</b></a>
			</td>
			<td><img src="images/pix.gif" height=1 width=10></td>
		</tr>
		<tr class=text >
			<td colspan=3><img src="images/pix.gif" height=3></td>		
		<tr>
<!-- End: Menu Item -->

		<tr style="background: #ffffff;">
			<td colspan=3><img src="images/pix.gif" height=1></td>
		</tr> 

		<tr class=text>
			<td colspan=3><img src="images/pix.gif" height=40 width=1></td>
		</tr> 

		</table>
		</td>
	</tr>


	<tr style="background: #860116;">
		<td colspan=2><img src="imges/pix.gif" height=24 width=1></td>
	</tr>
	<tr class="contacts" style="background: #860116;"> 
		<td><img src="images/pix.gif" width=10 height=1></td>
		<td nowrap  class=text>
		<span style="width: 165; overflow: hidden; text-overflow: ellipsis; " title="<?=$u_address;?>">
		<?=str_replace("\n", "<br>", $u_address);?>
		</span>
		</td>
	</tr>
	<tr style="background: #860116;">
		<td colspan=2><img src="images/pix.gif" height=24 width=1></td>
	</tr>
	
	</table>

	</td>
<!-- End: Left menu and contacts -->


</tr>

</table>

<table>
<tr>
	<td>
	Copyright &copy; 2004<br> <?=$u_fname?> <?=$u_mname?> <?=$u_lname?>
	</td>
</tr>
</table>

</body>

</html>