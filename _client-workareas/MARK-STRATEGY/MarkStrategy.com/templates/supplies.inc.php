<?
include "templates/mainheader.php";
?>                                                                                           

<?
	$db = $SQL->Query("SELECT id, subject, home_photo, state, city, address,notes FROM homes WHERE id_user=$uId");
	
	$ret = array();
	for ($i=0; $i<$SQL->Numrows($db); $i++)
	{
		list($id, $subject, $photo, $state, $city, $address,$notes) = $SQL->Fetchrow($db);
		$photo = (file_exists($tmp = "img/homes/$id.$photo")) ? $tmp : 'img/homes/blank_home.jpg';
		?>
<!-- Begin Content Item -->
	<tr valign=top>
		<td width=40><img src="images/pix.gif" height=1 width=40><br></td>
		<td>
		<table cellpadding=0 cellspacing=0 border=0>
		<tr>
			<td width=170 height=95><img src="<?= $photo?>"><br></td>
			<td width=40><img src="images/pix.gif" height=1 width=40></td>
			<td width=400 valign=top>
			<b style="color: #860116;"><?= str_replace('\"', '"', strtoupper($subject)); ?></b><br>
			<img src="images/pix.gif" height=10 width=1><br>
			<?= $city?>, <?= $state?><br>
			<?= $notes?><br>			
			<img src="images/pix.gif" height=10 width=1><br>
			<a href="/<?= sprintf($home_href_nf, $id)?>" style="color: #860116;"><b>Read More</b></a>
			</td>
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

		</table>
		</td>
	</tr>
<!-- Begin Content Item -->
		<?
	}
?>


<!-- Begin Content Item -->
	<tr valign=top>
		<td width=40><img src="images/pix.gif" height=1 width=40><br></td>
		<td>
		<table cellpadding=0 cellspacing=0 border=0>
		<tr>
			<td width=170 height=95><img src="<?= $logo_img?>" BORDER=0><br></td>
			<td width=40><img src="images/pix.gif" height=1 width=40></td>
			<td width=400 valign=middle align=center>
			<font size="+1"><b><?= $u_slogan?></b></font><br>
			<img src="images/pix.gif" height=10 width=1><br>
			</td>
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

		</table>
		</td>
	</tr>
<!-- Begin Content Item -->


<?
include "templates/mainfooter.php";

?>