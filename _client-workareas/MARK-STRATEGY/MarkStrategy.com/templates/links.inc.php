<?
include "templates/mainheader.php";
?>
<?
	foreach($links as $l)
	{
		$img   = ($l['img']) ? '<img src="'.$l['img'].'" />' : '';
		echo <<<LINK
	<tr valign=top>
		<td width=40><img src="images/pix.gif" height=1 width=40><br></td>
		<td>
		<table cellpadding=0 cellspacing=0 border=0>
		<tr>
			<td width=170 height=95>$img<br></td>
			<td width=40><img src="images/pix.gif" height=1 width=40></td>
			<td width=400 valign=top>
LINK;
			if ( trim($l['url']) )
				echo "<a href=\"{$l['url']}\" style=\"color: #860116;\"><b>{$l['title']}</b></a><br>";
			else
				echo "<b>{$l['title']}</b>";

			echo <<<LINK
			<img src="images/pix.gif" height=10 width=1><br>
			{$l['intro']}
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



LINK;
	}

include "templates/mainfooter.php";
?>