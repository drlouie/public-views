<!-- Sample JSP file -->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML>
<HEAD>
<META name="GENERATOR" content="IBM WebSphere Page Designer V3.5 for Windows">
<META http-equiv="Content-Style-Type" content="text/css">
<TITLE>
Test
</TITLE>
<script language="javascript">
 function check(click)
  {
	document.search.clicked.value = click;
	var bid = document.search.BID.value;
	var status = true;
	if(click == 'Search')
	{
	if(bid == "")
		{
			alert("Please Enter BID");
			status =  false;
		}
	}
	document.search.BID.focus();
	return status;
  }
</script>
</HEAD>
<BODY BGCOLOR="#FFFFFF">
<FORM name="search" method="post" action = "BrokerInquiryServlet" ><BR>
Enter BID : <INPUT size="12" type="text" maxlength="12" name="BID"><BR>
<BR>
<input type="hidden" name = "clicked" value="">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<INPUT type="IMAGE" src="images/search.gif" name="submit" value="" width="50" height="22" border="0" alt = "Search" onClick="return check(this.value);"> &nbsp;&nbsp;&nbsp;<INPUT type="IMAGE" src="images/addagent.gif" name="submit" value="AddAgent" width="50" height="22" border="0" alt = "AddAgent" onClick="return check(this.value);">&nbsp;&nbsp;&nbsp;&nbsp;<INPUT type="IMAGE" src="images/addfirm.gif" name="submit" value="AddFirm" width="50" height="22" border="0" alt = "AddFirm" onClick="return check(this.value);"></FORM>
</BODY>
</HTML>
