<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<HTML>
<HEAD>
<META name="GENERATOR" content="IBM WebSphere Studio">
<TITLE>Broker Adminstration System Exchange</TITLE>
<Script src="/BASEWeb/script/PrintScript.js"></Script>
<SCRIPT>
var purchaser = new Array();
	var eu = new Array();
	var rollup = new Array();
function selectSecondaryType(primaryValue)
{
	
	document.PurchaserInquiry.SearchCriteria.value = '';	
	disableNameSearchParameter();		
	switch(primaryValue)
		{
			case '1': 	populatePurchaser();populateSecondary(purchaser);
						break;
			case '2':	populateEU();populateSecondary(eu);
						break;
			case '3':	populateRollUp();populateSecondary(rollup);
						break;
						
		}
		
	document.PurchaserInquiry.SearchCriteria.focus();		
}
function populateSecondary(secondarySelection)
	{	
		removeAllElementsInSecondayType();
		for(var count = 0 ; count < secondarySelection.length ; count++)
			{				
				var secOption = new Option();
				secOption.text = secondarySelection[count];
				secOption.value = count+1;
				document.PurchaserInquiry.SearchBy.options[count] = secOption;				
			}								

					
	}
function removeAllElementsInSecondayType()
	{	
		document.PurchaserInquiry.SearchBy.options.length = 1;
	}
function populatePurchaser()
{
	purchaser[0] = "PID    ";
	purchaser[1] = "TPA ID  ";
	purchaser[2] = "Name  ";
	purchaser[3] = "Tax ID";
}
function populateEU()
{
	eu[0] = "PID EU    ";
	eu[1] = "EU-DIV    ";
	eu[2] = "Name  ";
	eu[3] = "Tax ID";
}
function populateRollUp()
{
	rollup[0] = "ID    ";
	rollup[1] = "Name  ";	
}	
function makeNameSearchParameter(selected)
{			
	var searchFor = document.PurchaserInquiry.SearchFor.value;
	document.PurchaserInquiry.SearchCriteria.value = '';
	if(selected != '3' && searchFor != '3')
		{
			document.PurchaserInquiry.NameSearchParameter[0].disabled = true;
			document.PurchaserInquiry.NameSearchParameter[1].disabled = true;
		}
	else if(selected != '2' && searchFor == '3')
		{
			document.PurchaserInquiry.NameSearchParameter[0].disabled = true;
			document.PurchaserInquiry.NameSearchParameter[1].disabled = true;
		}
	else 
		{
			document.PurchaserInquiry.NameSearchParameter[0].disabled = false;
			document.PurchaserInquiry.NameSearchParameter[1].disabled = false;
		}
		
	document.PurchaserInquiry.SearchCriteria.focus();		
}
function disableNameSearchParameter()
{
	document.PurchaserInquiry.NameSearchParameter[0].disabled = true;
	document.PurchaserInquiry.NameSearchParameter[1].disabled = true;
}
function enableNameSearchParameter()
{	
	document.PurchaserInquiry.NameSearchParameter[0].disabled = false;
	document.PurchaserInquiry.NameSearchParameter[1].disabled = false;
}
function checkEnteredValue(entered)
{
	var ID_TaxID = "0123456789";
	var Name = "abcdefghijklmanopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";
	var valid = "";
	var validNo = document.PurchaserInquiry.SearchBy.value;
	var searchFor = document.PurchaserInquiry.SearchFor.value;
	if(document.PurchaserInquiry.SearchCriteria.value == '')
		{
			alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.inquiry.SearchCriteriaMissing")%>");
			document.PurchaserInquiry.SearchCriteria.focus();
			return false;
		}
	if(searchFor !=3)
	{
	 if(validNo == 1 || validNo == 2 || validNo == 4)
		valid = ID_TaxID;
	 else if(validNo == 3)
		valid = Name;	
	}
	else if(searchFor == 3)
	{
	 if(validNo == 1)
	 	valid = ID_TaxID
	 else if(validNo == 2)
	 	valid = Name;	
	}
	if(valid.length > 1)
	{
	 for (var i=0; i < entered.length; i++) 
	  {
	   temp = "" + entered.substring(i, i+1);
	   if (valid.indexOf(temp) == "-1") 
	     {
	       alert('" '+entered+' "'+"<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.inquiry.SearchIsNotValid")%>");
	       document.PurchaserInquiry.SearchCriteria.value = '';
	       document.PurchaserInquiry.SearchCriteria.focus();
	       return false;	
	       break;       
	     }
	  }
	 }
	return true;
}
function printFunction() {

	callPrint();
}
</SCRIPT>
<script language="javascript" src="../script/common_css.js"></script>
<script language="Javascript">
<!--
//MOUSEOVER IMAGE PRELOAD
//mprint
image9 = new Image();
image9.src = "../limages/mprint_ov.gif";
image10 = new Image();
image10.src = "../limages/mprint_off.gif";
//mexit
image11 = new Image();
image11.src = "../limages/mexit_ov.gif";
image12 = new Image();
image12.src = "../limages/mexit_off.gif";

//-->
</script>
</HEAD>
<body bgcolor="#0B5F77" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" OnLoad="disableNameSearchParameter();init();parent.window.resizeTo(860,412);">
<FORM name = "PurchaserInquiry"  method = "post" action = "PurchaserInquiryServlet" target = "_parent" onsubmit = "return checkEnteredValue(SearchCriteria.value)">
<jsp:useBean id="searchVO" class="org.kp.purchaser.vo.PurchaserInquirySearchVO"/> 

<SCRIPT>
var searchFor = '';
function init()
{
	
	<%
	searchVO = (org.kp.purchaser.vo.PurchaserInquirySearchVO)session.getAttribute("Search");	
	
	String searchCriteria = "";
	if((String)session.getAttribute("FormatedSearchCriteria") != null)
		searchCriteria = (String)session.getAttribute("FormatedSearchCriteria");	
	if(searchVO != null)
	{		
	%>
		searchFor = '<%= searchVO.getSearchFor()%>';		
		loadSearchBy();		
		document.PurchaserInquiry.SearchFor.value = '<%= searchVO.getSearchFor()%>';
		document.PurchaserInquiry.SearchBy.value = '<%= searchVO.getSearchBy()%>';		
		document.PurchaserInquiry.SearchCriteria.value = '<%= searchVO.getSearchCriteria()%>';		
		
	<%

		if(!searchVO.getNameSearchParameter().equals(""))
			{
	%>
				enableNameSearchParameter();
	<%			
			}
	}
	%>
	
	document.PurchaserInquiry.SearchCriteria.focus();
	
}
function loadSearchBy()
{	
	switch(searchFor)
		{
			case '1': 	populatePurchaser();populateSecondary(purchaser);
						break;
			case '2':	populateEU();populateSecondary(eu);
						break;
			case '3':	populateRollUp();populateSecondary(rollup);						
		}
}
function resetForm()
{
	document.PurchaserInquiry.reset();
	selectSecondaryType("1");	
	return false
	/*
	init();	
	return false;
	*/
}
function constructHref()
{
	var purIK = parent.details.document.PurchaserInquiry.purIK.value;	
	if(purIK == 0)
		{
			alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.inquiry.SelectPurchaser")%>");
			return false;
		}
	else
		{
			var href = "../EnrollmentUnit/EnrollmentUnitInitialServlet?PurIK="+purIK;	
			return href;
		}
}
</SCRIPT>
  <table width="850" border="0" cellspacing="0" cellpadding="0" align="center">
    <tr> 
      <td width="5" valign="top"><img src="../limages/spacer.gif" border="0" width="5" height="5"></td>
      <td width="300" valign="top"><img src="../limages/spacer.gif" border="0" width="5" height="5"></td>
      <td width="390"><img src="../limages/spacer.gif" border="0" width="5" height="5"></td>
      <td width="110"><img src="../limages/spacer.gif" border="0" width="5" height="5"></td>
      <td width="5"><img src="../limages/spacer.gif" border="0" width="5" height="5"></td>
    </tr>
    <tr> 
      <td width="5" valign="top">&nbsp;</td>
      <td width="340" valign="top"> 
        <table width="340" border="0" cellspacing="0" cellpadding="0">
          <tr> 
            <td align="left" width="3" height="20"><img src="../limages/tleft4.gif" width="3" height="24"></td>
            <td bgcolor="#E6E9F0" width="334"><font class="maintitle">PRI000 Purchaser / Rollup Inquiry</font></td>
            <td align="right" width="3" height="20"><img src="../limages/tright4.gif" width="3" height="24"></td>
          </tr>
        </table>
      </td>
      <td width="390" valign="top"> <br>
        <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
          <tr> 
            <td bgcolor="#E6E9F0" width="100%"><img src="../limages/spacer.gif" border="0" width="1" height="1"></td>
          </tr>
        </table>
      </td>
      <td width="106" align="right"> 
        <table width="110" border="0" cellspacing="0" cellpadding="0">
          <tr> 
            <td bgcolor="#E6E9F0"><img src="../limages/spacer.gif" border="0" width="1" height="1"></td>
            <td bgcolor="#E6E9F0" width="398"><img src="../limages/spacer.gif" border="0" width="1" height="1"></td>
            <td bgcolor="#E6E9F0"><img src="../limages/spacer.gif" border="0" width="1" height="1"></td>
          </tr>
          <tr> 
            <td width="1" bgcolor="#E6E9F0"><img src="../limages/spacer.gif" border="0" width="1" height="1"></td>
            <td height="37" width="108" align="center"> <a href="#" onMouseOver="javascript:mprint.src = image9.src;" onMouseOut="javascript:mprint.src = image10.src;" onClick="printFunction();"><img src="../limages/mprint_off.gif" width="52" height="37" name="mprint" border="0"></a> 
              <a href="#" onMouseOver="javascript:mexit.src = image11.src;" onMouseOut="javascript:mexit.src = image12.src;" onClick="parent.window.close();"><img src="../limages/mexit_off.gif" width="52" height="37" name="mexit" border="0"></a></td>
            <td width="1" bgcolor="#E6E9F0"><img src="../limages/spacer.gif" border="0" width="1" height="1"></td>
          </tr>
          <tr> 
            <td height="1" bgcolor="#E6E9F0"><img src="../limages/spacer.gif" border="0" width="1" height="1"></td>
            <td height="1" bgcolor="#E6E9F0" width="398"><img src="../limages/spacer.gif" border="0" width="1" height="1"></td>
            <td height="1" bgcolor="#E6E9F0"><img src="../limages/spacer.gif" border="0" width="1" height="1"></td>
          </tr>
        </table>
      </td>
      <td width="5">&nbsp;</td>
    </tr>
  </table>
  <table width="100%" cellpadding="0" cellspacing="0">
    <tbody> 
    <tr align="center"> 
      <td height="25" valign="bottom"><font class="ComTitle">Search For</font></td>
      <td id="SearchParameter" height="25" valign="bottom"><font class="ComTitle">Name 
        Search Parameter</font></td>
      <td class="label" height="25" valign="bottom"><font class="ComTitle">Search 
        By</font></td>
      <td class="label" height="25" valign="bottom"><font class="ComTitle">Search 
        Criteria</font></td>
      <td>&nbsp; </td>
    </tr>
    <tr> 
      <td align="center" bgcolor="#E6E9F0"> 
        <select name="SearchFor" class="select2" onChange="selectSecondaryType(this.value)" tabindex="1">
          <option value="1" selected>Purchaser</option>
          <option value="2">Enrollment Unit</option>
          <option value="3">Roll - up</option>
        </select>
      </td>
      <td align="center" bgcolor="#E6E9F0"><nobr> 
        <input type="radio" name="NameSearchParameter" value="1" checked tabindex="2">
        <font class="radiotext2">Contains</font>&nbsp;&nbsp;&nbsp;&nbsp; 
        <input type="radio" name="NameSearchParameter" value="2">
        <font class="radiotext2">Starts With</font></nobr></td>
      <td align="center" bgcolor="#E6E9F0">
        <select name="SearchBy" onChange="makeNameSearchParameter(this.value)" tabindex="3" class="select2">
          <option value="1" selected>PID </option>
          <option value="2">TPA ID </option>
          <option value="3">Name </option>
          <option value="4">Tax ID</option>
        </select>
      </td>
      <td align="center" bgcolor="#E6E9F0"> 
        <input size="40" type="text" name="SearchCriteria" maxlength="50" tabindex="4" class="input2">
      </td>
      <td align="center" bgcolor="#E6E9F0"> 
        <input type="submit" value="Search" class="lebotton" tabindex="4" name="submit2">
        <input type="button" name="Reset" value="Reset" class="lebotton" onClick="return this.href = resetForm()">
      </td>
    </tr>
    </tbody> 
  </table>
  <table width="100%" cellpadding="0" cellspacing="0">
    <tbody> 
    <tr> 
      <td colspan="4" align="right" height="45"> 
        <input type="button" name="AddR" value="Add Rollup" class="lebotton" onClick='javascript:parent.location.href="../Rollup/AdministerRollupServlet";'>
        <input type="button" name="AddR" value="Add Purchaser" class="lebotton" onClick='javascript:parent.location.href="PurchaserInitialServlet";'>
        <input type="button" name="AddR" value="Add EU" class="lebotton" onClick="return this.href=constructHref()">
      </td>
    </tr>
    <tr bgcolor = "#ffffff"> 
      <td colspan="4" align="center" class="maintitle" bgcolor="#E6E9F0" height="25" valign="middle" style="color:#EB0000"><%= searchCriteria%></td>
    </tr>
    </tbody> 
  </table>
  <table width="100%" border="0" cellspacing="0" cellpadding="0">
    <tr> 
      <td height="4"><img src="../limages/spacer.gif" height="4" width="100" border="0"></td>
    </tr>
    <tr bgcolor="#E6E9F0" height="2"> 
      <td><img src="../limages/spacer.gif" height="2" width="100" border="0"></td>
    </tr>
  </table>
  </FORM>
</BODY>
</HTML>
