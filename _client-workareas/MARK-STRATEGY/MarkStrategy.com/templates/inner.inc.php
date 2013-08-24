<?
include "templates/mainheader.php";
?>


	<tr valign=top>
		<td width=40><img src="images/pix.gif" height=1 width=40><br></td>
		<td><?= str_replace('\\\\\\', "", nl2br($personal_info)); ?></td>
	</tr>

	<tr>
		<td colspan=2><img src="images/pix.gif" height=5 width=1><br></td>
	</tr>
	<tr style="background: #cccccc">
		<td colspan=2><img src="images/pix.gif" height=1 width=1><br></td>
	</tr>
	<tr>
		<td colspan=2><img src="images/pix.gif" height=5 width=1><br></td>
	</tr>

	<tr valign=top>
		<td width=40><img src="images/pix.gif" height=1 width=40><br></td>
		<td><?= nl2br($u_address) ?></td>
	</tr>


<?
include "templates/mainfooter.php";
?>
