<?
	if (!defined('INNER')) exit;
?>
<form method="post" id="menu_form" action="?">
<input type="hidden" name="act" value="" />
<input type="hidden" name="mode" value="" />
<table width="100%" class="head"><tr><td width="100%" align="center">
<table><tr>
<td>|&nbsp;<a href="?act=default" class="menu">Edit personal info</a></td>
<td>|&nbsp;<a href="?act=supply_user" class="menu">Featured homes</a></td>
<td>|&nbsp;<a href="?act=taskbar" class="menu">Toolbar settings</a></td>
<td>|&nbsp;<a href="?act=sell" class="menu">View sellers</a></td>
<td>|&nbsp;<a href="?act=buy" class="menu">View buyers</a></td>
<td>|&nbsp;<a href="#" class="menu" onclick="f=document.getElementById('menu_form'); f.act.value='shedules'; f.submit();">Schedule</a></td>
<td>|&nbsp;<a href="?act=links_user" class="menu">Links</a></td>
<td>|&nbsp;<a href="?act=logout" class="menu" alt="logout">Logout</a></td>
<!--<td>|&nbsp;<a href="#" class="menu" onclick="f=document.getElementById('menu_form'); f.act.value='homes_csv'; f.mode.value='csv'; f.target='_blank'; f.submit();">Get data in CSV</a>&nbsp;|</td>-->
</tr></table>
</td></tr></table>
</form>
<br />