<?                                                                                                                   
$url = urldecode($url);
$url = str_replace("$","&",$url);

$exclude = array('contact_mls', "home", "email_property", "shedule_form", "order", "sell", "personal_info", "links", "contact");
//($act!="home")&&($act!="email_property")&&($act!="shedule_form")&&($act!="order")&&($act!="sell")&&($act!="personal_info")&&($act!="links")&&($act!="contact")
if (($act!="")&&(!in_array($act, $exclude))){
?>
<frameset rows="130, *" frameborder=0 border=0>
	<frame src="http://<?= $HTTP_HOST?>/main.php?target=top" name="top" noresize scrolling="no">
	<frameset cols="200, *" frameborder=0 border=0>
		<frame src="http://<?= $HTTP_HOST?>/main.php?target=left" name="right" noresize scrolling="yes">
		<frameset rows="45, *" frameborder=0 border=0>
			<frame src="/templates/rtop.html" noresize scrolling="no">
<?
if ($act=="mls_list"){
	define('INNER', true);
	include 'share/init.inc.php';
	if ($found)
	{

?>
			<frame src="<?= $mls_list_href?>" name="main" noresize scrolling="yes">
<?
	}
}else if ($act=="search"){
$my_query="http://idd.homeseekers.com/scripts/list.asp?";
while (list($key,$value)=each($_GET)){
if ($key!="act") $my_query.="$key=$value&";
}
?>
			<frame src="<?= $my_query?>" name="main" noresize scrolling="yes">
<?

}else if ($act=="advsearch"){

//$my_query="http://idd.homeseekers.com/search.asp?org_id=oc&";
$my_query="http://idd.homeseekers.com/search.asp?blnAdvancedSearch=true&_org_id=oc&_ver=4&_lid=0&_pType=1&_account=idd&_new=1&_idd_yn=y&";
while (list($key,$value)=each($_GET)){
if ($key!="act") $my_query.="$key=$value&";
}
?>
			<frame src="<?= $my_query?>" name="main" noresize scrolling="yes">
<?

}elseif($act=="link"){
?>
			<frame src="http://<?= $url?>" name="main" noresize scrolling="yes">
<?

}else{

?>
			<frame src="http://<?= $HTTP_HOST?>/main.php?act=<?= $act?>&id=<?= $id?>" name="main" noresize scrolling="yes">
<?
}
?>
		</frameset>
	</frameset>	
	<!-- frame src="bottom.html" noresize scrolling="no" -->
</frameset>
<?
}else{

	define('INNER', true);
	include 'share/init.inc.php';
	if ($found)
	{
switch ($act){
case "home": include "templates/home.inc.php";
break;
case "email_property": include "templates/email_property.inc.php";
break;
case "shedule_form": include "templates/shedule.inc.php";
break;
case "order": include "templates/order_form.inc.php";
break;
case "sell": include "templates/sell_form.inc.php";
break;
case "personal_info": include "templates/inner.inc.php";
break;
case "links": include "templates/links.inc.php";
break;
case "contact_mls": include "templates/contact_short_form.inc.php";
break;
case "contact": include "templates/contact_form.inc.php";
break;

default: include "templates/supplies.inc.php";
}
	}

}
?>
