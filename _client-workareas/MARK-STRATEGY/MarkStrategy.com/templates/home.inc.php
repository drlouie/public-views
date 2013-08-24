<?
include "templates/mainheader.php";

	$url_address=str_replace(" ","+",$data['address']['value']);
	$url_city=str_replace(" ","+",$data['city']['value']);
	$exclude = array('address', 'subject', 'notes');

?>

	<tr valign=rop align=center>
		<td colspan=2>
		<a href="index.php?act=link&url=list.realestate.yahoo.com/re/neighborhood/search.html?sa=<?= $url_address?>$csz=<?= $url_city?>+<?= $data['state']['value']?>+<?= $data['zip']['value']?>" style="color: #860116;"><b>Community Info</b></a>
		|
		<a href="index.php?act=link&url=<?= str_replace("&","$",$toolbar[0]['url_nf'])?>" style="color: #860116;"><b><?= $toolbar[0]['caption']?></b></a>
		|
		<a href="<?= sprintf($email_property_href, $id)?>" style="color: #860116;"><b>Email This Property</b></a>
		</td>
	</tr>

	<tr valign=rop align=center>
		<td colspan=2>
		<a href="<?= sprintf($home_print_href, $id)?>" target="_blank" style="color: #860116;"><b>Print This Property</b></a>
		|
		<a href="index.php?act=link&url=www.mortgage-calc.com/mortgage/flap.html" target="_top" style="color: #860116;"><b>Mortgage Calculator</b></a>
		|
		<a href="<?= sprintf($shedule_form_href, $id)?>" style="color: #860116;"><b>Schedule Showing</b></a>
		|
		<a href="index.php?act=link&url=<?=  str_replace("&","$",$toolbar[1]['url_nf'])?>" style="color: #860116;"><b><?= $toolbar[1]['caption']?></b></a>
		</td>
	</tr>

	<tr align=center>
		<td colspan=2><img src="images/pix.gif" width=1 height=20><br></td>
	</tr>

	<tr valign=top>
		<td width=40><img src="images/pix.gif" height=1 width=40><br></td>
		<td>
		<table cellpadding=0 cellspacing=0 border=0>
		<tr>
			<td width=170 height=95 valign=top><img src="<?= $data['home_photo']['src']?>"><br></td>
			<td width=40><img src="images/pix.gif" height=1 width=40></td>
			<td width=400 valign=top>
			<b style="color: #860116;"><?= str_replace('\"', '"', strtoupper($data['subject']['value']) );?></b><br>
			<img src="images/pix.gif" height=10 width=1><br>
			<?	
			foreach($data as $k => $v)
			{
				if ($v['value'] && !in_array($k, $exclude))
				{
					echo "$v[caption]: <b>$v[value]</b><br>";
				}
			}
			?>
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

		<tr>
			<td colspan=3 align=right><a href="javascript:history.go('-1');" style="color: #860116;"><b>Back To Featured Listings</b></a><br></td>
		</tr>

		</table>
		</td>
	</tr>



<?
include "templates/mainfooter.php";
?>