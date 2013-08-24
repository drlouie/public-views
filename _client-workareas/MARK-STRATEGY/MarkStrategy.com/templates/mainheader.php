
<html>
<head>
<title></title>
<link rel=stylesheet type=text/css href="styles.css">
</head>

<body>


<table width=100% style="background: #960018; " cellpadding=0 cellspacing=0 border=0>
<!-- Begin: Top photo and picture -->
<tr>
	<td width=1% valign=bottom>
	<table width=100% cellpadding=0 cellspacing=0 border=0>
	<tr>
		<td colspan=2><img src="images/pix.gif" width=1 height=12><br></td>
	</tr>
	<tr>
		<td><img src="images/pix.gif" width=10 heigth=1><br></td>		
		<td nowrap><img src="<?= $photo_img ?>"  border=0 alt="Portrait"><br></td>

	</tr>
	</table>
	</td>
                                                                                                     
	<td align=right style="background: #ffffff url(<?= $banner_img?>) no-repeat">
	</td>

</tr>
<!-- End: Top photo and picture -->

<tr>
<!-- Begin: Left menu and contacts -->
	<td valign=top>

	<table width=100% cellpadding=0 cellspacing=0 border=0>
	<tr class="text">
		<td width=10><img src="images/pix.gif" width=10 height=1><br></td>
		<td width=100%><b><?=$u_fname?> <?=$u_mname?> <?=$u_lname?> </b></td> 
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
			<td nowrap align=left class=text><?=$u_phone; ?> <?=$u_buy_homes; ?></td>
			<td nowrap width=100%><img src="imges/pix.gif" height=1 width=10></td>
		</tr>
		<? } ?>	
		
		<? if ($u_phone2 != "") { ?>
		<tr>
			<td nowrap class=text><b>Phone2:</b></td>
			<td width=4><img src="imges/pix.gif" height=1 width=4></td>
			<td nowrap align=left class=text><?=$u_phone2; ?></td>
			<td nowrap><img src="imges/pix.gif" height=1 width=10></td>
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

<? 
	$activeStyle = "style=\"background: #860116;\"";
	$passiveStyle = "class=text";

	$rURI = getenv("REQUEST_URI");
	$listingStyle = $passiveStyle;
	$byStyle = $passiveStyle;
	$sellStyle = $passiveStyle;
	$searchStyle = $passiveStyle;
	$aboutStyle = $passiveStyle;
	$contactStyle = $passiveStyle;
	$linksStyle = $passiveStyle;	

	if ($rURI == "" || $rURI == "/?")
		$listingStyle = $activeStyle;
	else if ($rURI == "/$order_form_href_nf")
		$byStyle = $activeStyle; 	
	else if ($rURI == "/$sell_form_href_nf")
		$sellStyle = $activeStyle; 	
	else if ($rURI == "/$contact_mls_href")
		$searchStyle = $activeStyle; 	
	else if ($rURI == "/index.php?act=links") // Links
		$linksStyle = $activeStyle; 	
	else if ($rURI == "/$info_href")
		$aboutStyle = $activeStyle; 	
	else if ($rURI == "/$contact_form_href")
		$contactStyle = $activeStyle; 	


	//echo "$rURI $contact_mls_href";
?>


	<tr>
		<td colspan=2>
		<table class="text" width=100% cellpadding=0 cellspacing=0 border=0>
<!-- Begin: Menu Item -->
		<tr style="background: #ffffff;">
			<td colspan=3><img src="images/pix.gif" height=1></td>
		</tr> 
		<tr <?=$listingStyle;?> >
			<td colspan=3><img src="images/pix.gif" height=3><br></td>		
		</tr>
		<tr <?=$listingStyle;?> >
			<td><img src="images/pix.gif" height=1 width=10></td>
			<td valign=middle>
			<a href="/?" class="text"><b>Featured Listings</b></a>
			</td>
			<td><img src="images/pix.gif" height=1 width=10></td>
		</tr>
		<tr <?=$listingStyle;?> >
			<td colspan=3><img src="images/pix.gif" height=3></td>		
		</tr>
<!-- End: Menu Item -->


<!-- Begin: Menu Item -->
		<tr style="background: #ffffff;">
			<td colspan=3><img src="images/pix.gif" height=1></td>
		</tr> 
		<tr <?=$byStyle;?> >
			<td colspan=3><img src="images/pix.gif" height=3><br></td>		
		</tr>
		<tr <?=$byStyle;?> >
			<td><img src="images/pix.gif" height=1 width=10></td>
			<td valign=middle>
			<a href="<?= $order_form_href_nf?>" target="_top" class="text"><b>Buying a Home</b></a>
			</td>
			<td><img src="images/pix.gif" height=1 width=10></td>
		</tr>
		<tr <?=$byStyle;?> >
			<td colspan=3><img src="images/pix.gif" height=3></td>		
		</tr>
<!-- End: Menu Item -->

<!-- Begin: Menu Item -->
		<tr style="background: #ffffff;">
			<td colspan=3><img src="images/pix.gif" height=1></td>
		</tr> 
		<tr <?=$sellStyle;?> >
			<td colspan=3 height=3><img src="images/pix.gif" height=3><br></td>		
		</tr>
		<tr <?=$sellStyle;?> >
			<td><img src="images/pix.gif" height=1 width=10></td>
			<td valign=middle>
			<a href="<?= $sell_form_href_nf?>" class="text"><b>Selling a Home</b></a>
			</td>
			<td><img src="images/pix.gif" height=1 width=10></td>
		</tr>
		<tr <?=$sellStyle;?> >
			<td colspan=3><img src="images/pix.gif" height=3></td>		
		</tr>
<!-- End: Menu Item -->

<!-- Begin: Menu Item -->
		<tr style="background: #ffffff;">
			<td colspan=3><img src="images/pix.gif" height=1></td>
		</tr> 
		<tr <?=$searchStyle;?> >
			<td colspan=3><img src="images/pix.gif" height=3><br></td>		
		</tr>
		<tr <?=$searchStyle;?> >
			<td><img src="images/pix.gif" height=1 width=10></td>
			<td valign=middle nowrap>
			<a href="<?= $contact_mls_href?>" class="text"><b>Home Search</b></a>
			</td>
			<td><img src="images/pix.gif" height=1 width=10></td>
		</tr>
		<tr <?=$searchStyle;?> >
			<td colspan=3><img src="images/pix.gif" height=3></td>		
		</tr>
<!-- End: Menu Item -->

<!-- Begin: Menu Item -->
		<tr style="background: #ffffff;">
			<td colspan=3><img src="images/pix.gif" height=1></td>
		</tr> 
		<tr class=text>
			<td colspan=3><img src="images/pix.gif" height=3><br></td>		
		</tr>
		<tr>
			<td><img src="images/pix.gif" height=1 width=10></td>
			<td valign=middle nowrap>
			<a href="/?act=link&url=<?= $taskbar[0]['url_nf']?>" class="text"><b>Home Financing</b></a>
			</td>
			<td><img src="images/pix.gif" height=1 width=10></td>
		</tr>
		<tr class=text>
			<td colspan=3><img src="images/pix.gif" height=3></td>		
		</tr>
<!-- End: Menu Item -->

<!-- Begin: Menu Item -->
		<tr style="background: #ffffff;">
			<td colspan=3><img src="images/pix.gif" height=1></td>
		</tr> 
		<tr <?=$linksStyle;?> >
			<td colspan=3><img src="images/pix.gif" height=3><br></td>		
		</tr>
		<tr <?=$linksStyle;?> >
			<td><img src="images/pix.gif" height=1 width=10></td>
			<td valign=middle>
			<a href="index.php?act=links" class="text"><b>Resource Center</b></a>
			</td>
			<td><img src="images/pix.gif" height=1 width=10></td>
		</tr>
		<tr <?=$linksStyle;?> >
			<td colspan=3><img src="images/pix.gif" height=3></td>		
		</tr>
<!-- End: Menu Item -->

<!-- Begin: Menu Item -->
		<tr style="background: #ffffff;">
			<td colspan=3><img src="images/pix.gif" height=1></td>
		</tr> 
		<tr <?=$aboutStyle;?> >
			<td colspan=3><img src="images/pix.gif" height=3></br></td>		
		</tr>
		<tr <?=$aboutStyle;?> >
			<td><img src="images/pix.gif" height=1 width=10></td>
			<td valign=middle>
			<a href="<?= $info_href?>" class="text"><b>About Me</b></a>
			</td>
			<td><img src="images/pix.gif" height=1 width=10></td>
		</tr>
		<tr <?=$aboutStyle;?> >
			<td colspan=3><img src="images/pix.gif" height=3></td>		
		</tr>
<!-- End: Menu Item -->

<!-- Begin: Menu Item -->
		<tr style="background: #ffffff;">
			<td colspan=3><img src="images/pix.gif" height=1></td>
		</tr> 
		<tr <?=$contactStyle;?> >
			<td colspan=3><img src="images/pix.gif" height=3><br></td>		
		</tr>
		<tr <?=$contactStyle;?> >
			<td><img src="images/pix.gif" height=1 width=10></td>
			<td valign=middle>
			<a href="<?= $contact_form_href?>" class="text"><b>Contact Me</b></a>
			</td>
			<td><img src="images/pix.gif" height=1 width=10></td>
		</tr>
		<tr <?=$contactStyle;?> >
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
		<td nowrap class=text>
		<?=str_replace("\n", "<br>", $u_address);?>
		</td>
	</tr>
	<tr style="background: #860116;">
		<td colspan=2><img src="images/pix.gif" height=24 width=1></td>
	</tr>
	
	</table>

	</td>
<!-- Begin: Left menu and contacts -->

<!-- Begin: Right content -->
	<td style="background: #ffffff" valign=top>
	<table width=100% cellpadding=0 cellspacing=0 border=0>
	<tr valign=top>
		<td colspan=2><img src="images/pix.gif" height=24 width=1></td>
	</tr>


                                                                  
