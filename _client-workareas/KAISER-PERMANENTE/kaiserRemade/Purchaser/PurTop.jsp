<!-- Sample JSP file --> <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML>
<jsp:useBean id="purDropDownVO" class="org.kp.purchaser.vo.PurchaserDropDownVO" />
<jsp:useBean id="purVO" class="org.kp.purchaser.vo.PurchaserVO" />
<jsp:useBean id="purInitVO" class="org.kp.purchaser.vo.PurchaserInitialVO" />
<%
		 	  purVO = (org.kp.purchaser.vo.PurchaserVO)session.getAttribute("ModifiedPurchaserInfo");
			  purInitVO = purVO.getPurchaserInitial();
%>
<HEAD>
<META name="GENERATOR" content="IBM WebSphere Page Designer V3.5.3 for Windows">
<META http-equiv="Content-Style-Type" content="text/css">
<STYLE>
<!--
.label {
	COLOR : #0033FF; 
	font-family: arial,verdana,sans-serif;
	font-size : 13px;
	font-weight : bold;
	font-style: normal;	
	}
.title
	{
	COLOR : #FFFFFF; 
	font-family: arial,verdana,sans-serif;
	font-size : 14px;
	font-weight : bold;
	font-style: normal;	

	}
.button {

	border : thick solid 0;
	background-color: #ffcc00;
	font-family: "verdana,Helvetica,Sans-serif";
	font-style : normal;
	font-weight : bold;
	color : #0033cc;
	}
IMG{
  color : olive;
   }

-->
</STYLE>
<TITLE>Broker Adminstration System Exchange</TITLE>
<%@ include file="script/validateGeneralInfoForm.js" %>
<%@ include file="script/validateAdminArrangmtForm.js" %>
<%@ include file="script/validateSellerForm.js" %>  
<!--  <SCRIPT src="/BASEWeb/Purchaser/script/validateGeneralInfoForm.js" >
</SCRIPT> --> 
<!-- fs <SCRIPT src="/BASEWeb/Purchaser/script/validateAdminArrangmtForm.js" >
</SCRIPT> -->
<SCRIPT src="/BASEWeb/Purchaser/script/validateKPStaffForm.js" >
</SCRIPT>
<SCRIPT src="/BASEWeb/Purchaser/script/validateKPStaffForm.js" >
</SCRIPT>
<SCRIPT src="/BASEWeb/Purchaser/script/validatePayeeForm.js" >
</SCRIPT>
<SCRIPT src="/BASEWeb/Purchaser/script/validateBORForm.js" >
</SCRIPT> 
<!-- <SCRIPT src="/BASEWeb/Purchaser/script/validateSellerForm.js" >
</SCRIPT> -->
<Script src="/BASEWeb/script/PrintScript.js">
</Script>


<SCRIPT language="Javascript" >
var states = new Array() ;
var countries = new Array();
function init()
{
	setPageTitle();
	<% purDropDownVO = (org.kp.purchaser.vo.PurchaserDropDownVO)session.getAttribute("PurchaserDropDown"); 
			java.util.Vector stateV = new java.util.Vector();
			stateV = purDropDownVO.getStatesValue();						
			for(int i = 0 ; i < stateV.size(); i++)
			{
		%>
					states[<%=i%>] = '<%=stateV.elementAt(i)%>';
		<%
			}
		 	java.util.Vector countryV = new java.util.Vector();
			countryV = purDropDownVO.getCountryValue();						
			for(int i = 0 ; i < countryV.size(); i++)
			{
		%>
				countries[<%=i%>] = '<%=countryV.elementAt(i)%>';
		<%
			}

		%>

            document.PurTop.PID.value = '<%=(String)session.getAttribute("PID")%>';
            document.PurTop.TPAID.value = '<%=(String)session.getAttribute("TPAID")%>'; 
 			document.PurTop.PurName.value = '<%=(String)session.getAttribute("PurchaserName")%>'; 
			document.PurTop.OrigEffectiveDate.value = '<%=(String)session.getAttribute("OrigEffDt")%>';
			document.PurTop.TerminationDate.value = '<%=(String)session.getAttribute("TermDt")%>'; 
			document.PurTop.Category.value = '<%=(String)session.getAttribute("Category")%>';
}	
		
function beforeSubmit1()
{
        if( parent.display.document.forms[0].name == "PurGeneralInformation" )
	{
        	if(!validateGeneralForm( parent.display.document.forms[0] ) )
                  return false;
            //added by sathish
            else
            	parent.display.document.forms[0].target = "_parent";
		
        }
        else if(parent.display.document.forms[0].name == "AdministrativeArrgmt" )
	{
        	if(!beforeSaveAdmin( parent.display.document.forms[0] ) )
		    return false;
	}
	else if(parent.display.document.forms[0].name == "KPStaff" )
	{		
		if(!validateKPStaffForm( parent.display.document.forms[0] ) )
			return false;
	}
	else if(parent.display.document.forms[0].name ==  "PayeeBroker" )
	{
		
		if(!validatePayeeForm( parent.display.document.forms[0] ) )
			return false;
	}
	else if(parent.display.document.forms[0].name == "BrokerOfRecord" )
	{
		if(!validateBORForm( parent.display.document.forms[0] ) )
			return false;
	}
	else if(parent.display.document.forms[0].name == "SellerBroker" )
	{		
		if(!validateSellerForm( parent.display.document.forms[0] ) )
			return false;
	}
		
        parent.display.document.forms[0].submit( parent.display.document.forms[0] );
return false;
       
}
function doNotRedirect()
{
	return false;
}

function printFunction() {

	callPrint();
}
var functionType = '';	
function callComments() 
{  		
   	var sourceId1 = "<%= session.getAttribute("PurIK")%>";
   	functionType = getFunctionType();   	
	var url = '../Comments/CommentServlet?sourceId1='+sourceId1+'&sourceId2=0&sourceId3=0&sourceInd=PUR&funType='+functionType;
	window.open(url, 'slideWindow',false,500,700);
   }
function getFunctionType()
{	
	if( parent.display.document.forms[0].name == "PurGeneralInformation" )
	{        	
		return "DMGR";
    }
    else if(parent.display.document.forms[0].name == "AdministrativeArrgmt" )
	{
        return "ADMINARNG";
	}
	else if(parent.display.document.forms[0].name == "KPStaff" )
	{		
		return "KPSTAFF";
	}
	else if(parent.display.document.forms[0].name ==  "PayeeBroker" )
	{
		return "PAYEBKR";		
	}
	else if(parent.display.document.forms[0].name == "BrokerOfRecord" )
	{
		return "BOR";
	}
	else if(parent.display.document.forms[0].name == "SellerBroker" )
	{
		return "SELLBKR";		
	}
	else if(parent.display.document.forms[0].name == "PurchaserEURelationship" )
	{
		return "ENRLUNTRLT";		
	}
}
function setPageTitle()
{
	var title = "<%=(String)session.getAttribute("Destination")%>";
	if(title == "GeneralInfo.jsp")
		document.PurTop.dynamic.value = "PUR101 Administer Purchaser ( General Information )";
	else if(title == "AdministrativeArrgmt.jsp")
		document.PurTop.dynamic.value = "PUR102 Administer Purchaser ( Adminstrative Arrangements )";
	else if(title == "BrokerOfRecord.jsp")
		document.PurTop.dynamic.value = "PUR103 Administer Purchaser ( Broker of Record )";
	else if(title == "PayeeBroker.jsp")
		document.PurTop.dynamic.value = "PUR104 Administer Purchaser ( Payee Borker )";
	else if(title == "SellerBroker.jsp")
		document.PurTop.dynamic.value = "PUR105 Administer Purchaser ( Seller Broker )";
	else if(title == "Amendments.jsp")
		document.PurTop.dynamic.value = "PUR106 Administer Purchaser ( Amendment )";
	else if(title == "PUrchaserEURelationship.jsp")
		document.PurTop.dynamic.value = "PUR107 Administer Purchaser ( PID / PID-EU Relationships )";
	else if(title == "KPStaff.jsp")
		document.PurTop.dynamic.value = "PUR108 Administer Purchaser ( KP Staff )";	
	
}
</SCRIPT>
<script language="javascript" src="../script/common_css.js"></script>
</HEAD>
<BODY bgcolor="#0B5F77" onLoad="init();" scroll="no">
<FORM name="PurTop" onSubmit= "return beforeSubmit1();">
  <table width="850" border="0" cellspacing="0" cellpadding="0" align="center">
    <tr> 
      <td width="5" valign="top"><img src="../limages/spacer.gif" border="0" width="5" height="5"></td>
      <td width="300" valign="top"><img src="../limages/spacer.gif" border="0" width="5" height="5"></td>
      <td width="200"><img src="../limages/spacer.gif" border="0" width="5" height="5"></td>
      <td width="300"><img src="../limages/spacer.gif" border="0" width="5" height="5"></td>
      <td width="5"><img src="../limages/spacer.gif" border="0" width="5" height="5"></td>
    </tr>
    <tr> 
      <td width="5" valign="top">&nbsp;</td>
      <td width="25" valign="top">&nbsp;<div id="leTitle">&nbsp;</div>
      </td>
      <td width="100%" valign="top"><br>
        <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
          <tr> 
            <td bgcolor="#E6E9F0" width="100%"><img src="../limages/spacer.gif" border="0" width="1" height="1"></td>
          </tr>
        </table>
      </td>
      <td width="300" align="right"> 
        <table width="300" border="0" cellspacing="0" cellpadding="0">
          <tr> 
            <td bgcolor="#E6E9F0"><img src="../limages/spacer.gif" border="0" width="1" height="1"></td>
            <td bgcolor="#E6E9F0" width="398"><img src="../limages/spacer.gif" border="0" width="1" height="1"></td>
            <td bgcolor="#E6E9F0"><img src="../limages/spacer.gif" border="0" width="1" height="1"></td>
          </tr>
          <tr> 
            <td width="1" bgcolor="#E6E9F0"><img src="../limages/spacer.gif" border="0" width="1" height="1"></td>
            <td height="37" width="398" align="center"><a href="/BASEWeb/Purchaser/PurchaserInquiry.jsp" target="_parent" onMouseOver="javascript:msearch.src = image5.src;" onMouseOut="javascript:msearch.src = image6.src;"><img src="../limages/msearch_off.gif" width="52" height="37" name="msearch" border="0"></a> 
              <input type="image" name="submit" src="../limages/msave_off.gif" width="52" height="37" border="0">
              <a href="#" onMouseOver="javascript:mprint.src = image9.src;" onMouseOut="javascript:mprint.src = image10.src;" onClick="printFunction();"><img src="../limages/mprint_off.gif" width="52" height="37" name="mprint" border="0"></a> 
              <a href="#" onMouseOver="javascript:mexit.src = image11.src;" onMouseOut="javascript:mexit.src = image12.src;" onClick="parent.window.close();"><img src="../limages/mexit_off.gif" width="52" height="37" name="mexit" border="0"></a><a href="#" onMouseOver="javascript:mcomments.src = image13.src;" onMouseOut="javascript:mcomments.src = image14.src;" onClick="callComments()"><img src="../limages/mcomments_off.gif" width="66" height="37" name="mcomments" border="0"></a></td>
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
  <table width="850" border="0" cellspacing="0" cellpadding="0" align="center">
    <tr> 
      <td width="5" valign="top">&nbsp;</td>
      <td colspan="3" valign="top"> 
        <table width="840" border="0" cellspacing="0" cellpadding="1">
          <tr align="center" valign="bottom"> 
            <td width="110" align="center" height="25"><font class="ComTitle">PID</font></td>
            <td width="110" height="25"><font class="ComTitle">TPA ID</font></td>
            <td width="200" align="center" height="25"><font class="ComTitle">Name</font></td>
            <td width="110" align="center" height="25"><font class="ComTitle">Orig 
              Eff Date</font></td>
            <td width="110" align="center" height="25"><font class="ComTitle">Termination 
              Date</font></td>
            <td width="200" height="25"><font class="ComTitle">Category / Sub-Category</font></td>
          </tr>
          <tr align="left" bgcolor="#E6E9F0"> 
            <td width="110" align="center" valign="middle"> 
              <input size="15" type="text" name="PID" class="input1" onFocus="this.blur()" maxlength="15">
            </td>
            <td width="110" align="center" valign="middle"> 
              <input size="15" type="text" name="TPAID" class="input1" onFocus="this.blur()" maxlength="15">
            </td>
            <td width="200" align="center" valign="middle"> 
              <input size="30" type="text" name="PurName" class="input1"  onFocus="this.blur()">
            </td>
            <td width="110" align="center" valign="middle"> 
              <input size="10" type="text" maxlength="10" name="OrigEffectiveDate" class="input1" onFocus="this.blur()">
            </td>
            <td width="110" align="center" valign="middle"> 
              <input size="10" type="text" maxlength="10" name="TerminationDate" class="input1" onFocus="this.blur()" >
            </td>
            <td align="center" width="200" valign="middle"> 
              <input size="30" type="text" maxlength="50" name="Category" class="input1" onFocus="this.blur()">
            </td>
          </tr>
        </table>
      </td>
      <td width="5">&nbsp;</td>
    </tr>
    <tr> 
      <td width="5" valign="top" height="30">&nbsp;</td>
      <td colspan="3" valign="middle" align="right" height="45"> 
        <input type="button" name="AddRU" value="Admin Rollup" class="lebotton" onClick='javascript:parent.location.href="../Rollup/AdministerRollupServlet";'>
        <input type="button" name="AddEU" value="Admin EU" class="lebotton" onClick='javascript:parent.location.href="../Purchaser/PurchaserInquiry.jsp";'>
      </td>
      <td width="5" height="30">&nbsp;</td>
    </tr>
  </table>
  <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
    <tr bgcolor="#E6E9F0" height="2"> 
      <td><img src="../limages/spacer.gif" height="2" width="100" border="0"></td>
    </tr>
  </table>
  <INPUT type="hidden" name="dynamic" value="">
</FORM>
</BODY>
</HTML>