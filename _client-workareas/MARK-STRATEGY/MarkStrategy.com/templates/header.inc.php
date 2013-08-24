<HTML>
<HEAD>
<TITLE><?=$u_fname?> <?=$u_mname?> <?=$u_lname?></TITLE>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=windows-1251">
 <style type="text/css"><!--
   .header {font-family:Tahoma, sans-serif; font-size: 12px; COLOR:#2FFFFF; padding-left:10; padding-right:5; font-weight:900 }
   .text {font-family:Tahoma,sans-serif; font-size: 10px; color:#ffffff; padding-left:20; padding-right:10 }
   .text2 {font-family:Verdana,sans-serif; font-size: 10px; color:#ffffff; padding-left:20; padding-right:10 }
    .news {font-family:Arial, sans-serif; font-size: 9px; color:#ffffff; padding-left:10; padding-right:5; font-weight:900; }
    .menu {font-family:Tahome;color:white;font-size:12px;font-weight:bold;}
   a:link{text-decoration: none; color:#ffffff}
  a:visited{text-decoration: none; color: #ffffff}
  a:hover{text-decoration: underline; color: #ffffff}
  a:active{text-decoration: none; color: #ffffff}
li {
	list-style : url(/images/pic.jpg);
}

--></style>
</HEAD>
<BODY BGCOLOR=#FFFFFF LEFTMARGIN=0 TOPMARGIN=0 MARGINWIDTH=0 MARGINHEIGHT=0 background="/images/bg.jpg">
<!-- ImageReady Slices (8-018a.psd) -->
<TABLE WIDTH=780 BORDER=0 CELLPADDING=0 CELLSPACING=0 align="center" height=100% bgcolor="ffffff">
	<TR>
	<td bgcolor=#000000 rowspan=100><img src="/images/spacer.gif" with=1></td>
		<TD WIDTH=780 HEIGHT=83 COLSPAN=12 style=background-image:url("/images/01.jpg");background-repeat:no-repeat; valign=middle; >
		<a href="?"><img src = "<?= $logo_img?>" border="0" height=79 /></a>
			<!--- IMG SRC="/images/01.jpg" WIDTH=780 HEIGHT=83 ALT="" --></TD>
<td bgcolor=#000000 rowspan=100><img src="/images/spacer.gif" with=1></td>			
	</TR>
	<TR>
		<TD WIDTH=93 HEIGHT=33 COLSPAN=2 style=background-image:url("/images/02.jpg");background-repeat:no-repeat; align=center >
			<A HREF="/"  class=menu >FEATURED<!--IMG SRC="/images/02.jpg" WIDTH=93 HEIGHT=33 BORDER=0 ALT=""--></A></TD>
		<TD WIDTH=86 HEIGHT=33 COLSPAN=2 style=background-image:url("/images/03.jpg");background-repeat:no-repeat; align=center >
			<A HREF="<?= $contact_form_href?>" class=menu >CONTACT
				<!--IMG SRC="/images/03.jpg" WIDTH=86 HEIGHT=33 BORDER=0 ALT="" --></A></TD>
		<TD WIDTH=95 HEIGHT=33 COLSPAN=3 style=background-image:url("/images/04.jpg");background-repeat:no-repeat; align=center >
			<A HREF="<?=$order_form_href?>" class=menu >ORDER FORM
				<!-- IMG SRC="/images/04.jpg" WIDTH=95 HEIGHT=33 BORDER=0 ALT="" --></A></TD>
		<TD WIDTH=98 HEIGHT=33 COLSPAN=2 style=background-image:url("/images/05.jpg");background-repeat:no-repeat; align=center >
			<A HREF="<?= $info_href?>"  class=menu >PROFILE
				<!-- IMG SRC="/images/05.jpg" WIDTH=98 HEIGHT=33 BORDER=0 ALT="" --></A></TD>
		<TD WIDTH=102 HEIGHT=33  style=background-image:url("/images/06.jpg");background-repeat:no-repeat; align=center >
			<A HREF="<?=$mls_list_href?>" class=menu >MLS
				<!-- IMG SRC="/images/06.jpg" WIDTH=102 HEIGHT=33 BORDER=0 ALT=""></A --></TD>
		<TD WIDTH=79 HEIGHT=33>
			<A HREF="#">
				<IMG SRC="/images/07.jpg" WIDTH=79 HEIGHT=33 BORDER=0 ALT=""></A></TD>
		<TD WIDTH=227 HEIGHT=33>
			<IMG SRC="/images/08.jpg" WIDTH=227 HEIGHT=33 ALT=""></TD>
	</TR>
	<TR>
		<TD WIDTH=77 HEIGHT=23>
			<A HREF="#">
				<IMG SRC="/images/09.jpg" WIDTH=77 HEIGHT=23 BORDER=0 ALT=""></A></TD>
		<TD WIDTH=89 HEIGHT=23 COLSPAN=2>
			<A HREF="#">
				<IMG SRC="/images/10.jpg" WIDTH=89 HEIGHT=23 BORDER=0 ALT=""></A></TD>
		<TD WIDTH=71 HEIGHT=23 COLSPAN=2>
			<A HREF="#">
				<IMG SRC="/images/11.jpg" WIDTH=71 HEIGHT=23 BORDER=0 ALT=""></A></TD>
		<TD WIDTH=76 HEIGHT=23 COLSPAN=3>
			<A HREF="#">
				<IMG SRC="/images/12.jpg" WIDTH=76 HEIGHT=23 BORDER=0 ALT=""></A></TD>
		<TD WIDTH=467 HEIGHT=23 COLSPAN=4>
			<IMG SRC="/images/13.jpg" WIDTH=467 HEIGHT=23 ALT=""></TD>
	</TR>
	<TR>
		<TD WIDTH=780 HEIGHT=54 COLSPAN=12>
			<IMG SRC="/images/14.jpg" WIDTH=780 HEIGHT=54 ALT=""></TD>
	</TR>
	<TR>
		<TD WIDTH=248 HEIGHT=100% valign="top" COLSPAN=6 background="/images/lbg.jpg">
<TABLE WIDTH=248 BORDER=0 CELLPADDING=0 CELLSPACING=0>
<form action=<?=$search_form_href?> method=post name=searchform >
<input type=hidden name=act value="mls_list" >
	<TR>
		<TD WIDTH=248 HEIGHT=44 COLSPAN=3>
			<IMG SRC="/images/a_15.jpg" WIDTH=248 HEIGHT=44 ALT=""></TD>
	</TR>
	<TR>
		<TD  COLSPAN=3 background="/images/a_17.jpg" WIDTH=248 HEIGHT=126 ALT="" valign="top">
		<div class="text" style="color:000000; font-size:11px; padding-left:25">
		<strong>
		Select property type<br>
		<select name="" STYLE="WIDTH:150">
	<option value="1" SELECTED>[search all]</option>
	<option value="2"></option>
	<option value="3"></option>
</select><br>
<br style="font-size:5px">
Price Range<br>
	<select name="" STYLE="WIDTH:120">
	<option value="1" SELECTED>[search all]</option>
	<option value="2"></option>
	<option value="3"></option>
</select><br><br style="font-size:5px">
City<br><br style="font-size:5px">

		<input type="text" style="width:120" value="">
		
		</strong>
		</div>
		</TD>
	</TR>
	<TR>
		<TD  background="/images/a_18.jpg" WIDTH=102 HEIGHT=40 ALT="">
		<div class="text" style="color:000000; font-size:11px; padding-left:25">
		<strong>
		State<br>
		<select name="" STYLE="WIDTH:60">
	<option value="1" SELECTED>--</option>
	<option value="2"></option>
	<option value="3"></option>
</select></div>
		</TD>
		<TD  background="/images/a_19.jpg" WIDTH=19 HEIGHT=40 ALT="">
		<div class="text" style="color:000000; font-size:11px; padding-right:0; padding-left:0">
		<strong>
		or<br></div>
		</TD>
		<TD   background="/images/a_20.jpg" WIDTH=127 HEIGHT=40 ALT="">
			<div class="text" style="color:000000; font-size:11px; padding-left:25">
		<strong>
		Zip<br>
		<select name="" STYLE="WIDTH:60">
	<option value="1" SELECTED>--</option>
	<option value="2"></option>
	<option value="3"></option>
</select></div>
		</TD>
	</TR>
	<TR>
		<TD WIDTH=248 HEIGHT=38 COLSPAN=3>
			<A HREF="#" onClick=document.elements.forms['search_form'].submit() >
				<IMG SRC="/images/a_21.jpg" WIDTH=248 HEIGHT=38 BORDER=0 ALT=""></A></TD>
	</TR>
	<TR>
		<TD WIDTH=248 HEIGHT=39 COLSPAN=3>
			<A HREF="<?= $search_form_href?>">
				<IMG SRC="/images/a_22.jpg" WIDTH=248 HEIGHT=39 BORDER=0 ALT=""></A></TD>
	</TR>
	<TR>
		<TD WIDTH=248 HEIGHT=57 COLSPAN=3>
			<IMG SRC="/images/a_23.jpg" WIDTH=248 HEIGHT=57 ALT=""></TD>
	</TR>
	<TR>
		<TD WIDTH=248 HEIGHT=173 COLSPAN=3 style=background-image:url('/images/a_24.jpg');background-repeat:no-repeat; align=center>
		<img src = "<?= $photo_img?>" width=150  />
			<!-- IMG SRC="/images/a_24.jpg" WIDTH=248 HEIGHT=173 ALT="" --></TD>
	</TR>
	</form>
</TABLE>
<br>
<div class="text" style="color:000000" align="center">
Call Me Toll Free:

</div>
<div class="text" style="color:000000; font-size:14px;" align="center" >
<strong><?=$u_phone?>

</strong>

<div class="text" style="color:000000" align="center">
Or send Me Fax:

</div>
		</div>
<div class="text" style="color:000000; font-size:14px;" align="center" >
<strong><?=$u_fax;?>

</strong>


		</div>
		<div class="text" style="color:000000" align="center">
Or <a href=mailto:<?=$email_to?> style=color:000000; >E-mail</a> me now!

</div>
</TD>
		<TD WIDTH=532 HEIGHT=100% valign="top" COLSPAN=6 style="padding:0">
		<TABLE  BORDER=0 CELLPADDING=0 CELLSPACING=0 align="center">
		<tr><td colspan=2><IMG SRC="/images/r1.jpg"  ALT=""></td></tr>
		</TABLE>
		<div class="text" style="color:000000; padding-right:20">

<!-- header -->


