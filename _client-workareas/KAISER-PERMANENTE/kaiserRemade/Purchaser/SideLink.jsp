<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML>
<jsp:useBean id="purDropDownVO" class="org.kp.purchaser.vo.PurchaserDropDownVO" />
<HEAD>
<META name="GENERATOR" content="IBM WebSphere Page Designer V3.5.3 for Windows">
<TITLE></TITLE>
<%@ include file="script/validateGeneralInfoForm.js" %>
<%@ include file="script/validateAdminArrangmtForm.js" %>
<%@ include file="script/validateSellerForm.js" %>
<!-- <SCRIPT src="/BASEWeb/Purchaser/script/validateGeneralInfoForm.js" >
</SCRIPT> --> 
<!-- <SCRIPT src="/BASEWeb/Purchaser/script/validateAdminArrangmtForm.js" >
</SCRIPT> --> 
<SCRIPT src="/BASEWeb/Purchaser/script/validateKPStaffForm.js" >
</SCRIPT>
<SCRIPT src="/BASEWeb/Purchaser/script/validatePayeeForm.js" >
</SCRIPT>
<SCRIPT src="/BASEWeb/Purchaser/script/validateBORForm.js" >
</SCRIPT> 
<!-- <SCRIPT src="/BASEWeb/Purchaser/script/validateSellerForm.js" >
</SCRIPT> -->
<SCRIPT language="JavaScript">
<!--HPB_SCRIPT_CODE_40
function _HpbImgSwap(imgName, imgSrc)
{
  var appVer=parseInt(navigator.appVersion);
  var isNC=(document.layers && (appVer >= 4));
  var isIE=(document.all    && (appVer >= 4));

  if (isNC || isIE)
  {
    if (document.images)
    {
      var img = document.images[imgName];
      if (!img) img = _HpbImgFind(document, imgName);
      if (img) img.src = imgSrc;
    }
  }
}

function _HpbImgFind(doc, imgName)
{
  for (var i=0; i < doc.layers.length; i++)
  {
    var img = doc.layers[i].document.images[imgName];
    if (!img) img = _HpbImgFind(doc.layers[i], imgName);
    if (img) return img;
  }
  return null;
}

function setTitlee(id)
{
var titles = new Array();
titles[0] = "PUR101 Administer Purchaser ( General Information )";
titles[1] = "PUR102 Administer Purchaser ( Administrative Arrangements )";
titles[2] = "PUR103 Administer Purchaser ( Seller Broker )";
titles[3] = "PUR104 Administer Purchaser ( Broker of Record )";
titles[4] = "PUR105 Administer Purchaser ( Payee Broker )";
titles[5] = "PUR106 Administer Purchaser ( KP Staff )";
titles[6] = "PUR107 Administer Purchaser ( Amendments )";
titles[7] = "PUR108 Administer Purchaser ( PID / PID_EU Relationships )";


if(id == "generalinformation")
	{		
		parent.tops.document.PurTop.dynamic.value = titles[0];
	}
else if(id == "administrativearrangements")
	{		
		parent.tops.document.PurTop.dynamic.value = titles[1];
	}
else if(id == "sellerbroker")
	{
		parent.tops.document.PurTop.dynamic.value = titles[2];
	}
else if(id == "brokerofrecord")
	{
		parent.tops.document.PurTop.dynamic.value = titles[3];
	}
else if(id == "payeebroker")
	{
		parent.tops.document.PurTop.dynamic.value = titles[4];
	}
else if(id == "kpstaff")
	{
		parent.tops.document.PurTop.dynamic.value = titles[5];
	}
else if(id == "amendments")
	{
		parent.tops.document.PurTop.dynamic.value = titles[6];
	}
else if(id == "pidpideurelationships")
	{
		parent.tops.document.PurTop.dynamic.value = titles[7];
	}
}
var states = new Array() ;
var countries = new Array();
function init()
{
		<% 	
		purDropDownVO = (org.kp.purchaser.vo.PurchaserDropDownVO)session.getAttribute("PurchaserDropDown"); 
			if(purDropDownVO != null )
			{
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
			}
		%>	
}			
<% String purIK = (String)session.getAttribute("PurIK");
if(purIK != null ) { %>
var formName = '';
var querystring = '';

function switchTab(name) {
	var status = true;
	formName = parent.display.document.forms[0].name;	
	//parent.display.document.forms[0].FromWhere.value = "1";

	status = callValidateForm(formName);
	switch(name) {
			case '1': 	callGeneralInfo();
						 //parent.display.document.forms[0].target = "_parent";
					  	break;
			case '2':	callAdminArrgmt();
						break;
			case '3': 	status = callSellerBroker();
						break;
			case '4': 	callBrokerOfRecord();
						break;
			case '5': 	callPayeeBroker(); 
						break;
			case '6': 	callKPStaff();
						break;
			case '7': 	callAmendments();
						break;
			case '8': 	callPidEuRelationships();						
		}		
	if(status) {
		    if(formName != "PurchaserEURelationship") 
			parent.display.document.forms[0].FromWhere.value = "1";
	 		parent.display.document.forms[0].WhereToGo.value = querystring;   	 		
   			parent.display.document.forms[0].submit(parent.display.document.forms[0]);	 
     	}
     
     return status;
}

function callValidateForm(formName)
{
	if(formName == "PurGeneralInformation")
	{		
		if(!validateGeneralForm( parent.display.document.forms[0] ) )
		
    		return false;		
  	}
    else if(formName == "AdministrativeArrgmt")
    {
    	if(!beforeSaveAdmin( parent.display.document.forms[0] ) )
			return false;
	}
    else if(formName == "KPStaff")
    {
    	if(!validateKPStaffForm( parent.display.document.forms[0] ) )
			return false;
	}
    else if(formName == "PayeeBroker")
    {
    	if(!validatePayeeForm( parent.display.document.forms[0] ) )
			return false;
	}
    else if(formName == "BrokerOfRecord")
    {
    	if(!validateBORForm( parent.display.document.forms[0] ) )
			return false;
	}
    else if(formName == "SellerBroker")
    {
    	if(!validateSellerForm( parent.display.document.forms[0] ) )
			return false;
	}
    else if(formName == "Amendments")
    {
    	/*
    	alert("Sorry,Under construction!");
		return false;
		*/
		return true;
    }
    else if(formName == "PurchaserEURelationship")
  	{  
    		parent.display.document.forms[0].FromWhere.value = "2";    		
    		return true;
  	}
    return true;
}
function callGeneralInfo()
{
    querystring = "/Purchaser/PurchaserGeneralInfoServlet?PurIK = "+<%= session.getAttribute("PurIK")%>+"&SelectedAction=";
   
}
function callAdminArrgmt()
{
	querystring = "/Purchaser/AdminArrangementsServlet?PurIK = "+<%= session.getAttribute("PurIK")%>+"&SelectedAction=";	
}
function callKPStaff()
{
	querystring = "/Purchaser/KPStaffServlet?PurIK = "+<%= session.getAttribute("PurIK")%>+"&SelectedAction="; 
}
function callPayeeBroker()
{
	querystring = "/Purchaser/PayeeBrokerServlet?PurIK = "+<%= session.getAttribute("PurIK")%>+"&SelectedAction=";
}
function callBrokerOfRecord()
{
	querystring = "/Purchaser/BrokerOfRecordServlet?PurIK="+<%= session.getAttribute("PurIK")%>+"&SelectedAction=";
}
function callSellerBroker()
{
   if( formName != "PurGeneralInformation" )
   {
    <% if( ((String)session.getAttribute("DirectSale")).equals("N") ) { %>
			querystring = "/Purchaser/SellerBrokerServlet?PurIK = "+<%=session.getAttribute("PurIK")%>+"&SelectedAction=";
			return true;
		<% } else {   %> 
			alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.seller.DirectSaleFlag")%>"); 
			return false;
	<% } %>
	}
    else
    {
   			querystring = "/Purchaser/SellerBrokerServlet?PurIK = "+<%= session.getAttribute("PurIK")%>+"&SelectedAction=";
			return true;
	}

}
function callAmendments()
{
	querystring ="/Purchaser/AmendmentServlet?PurIK = "+<%= session.getAttribute("PurIK")%>+"&SelectedAction=";

	/*
   alert("Sorry,Under construction!");
	return false;
	*/

	//querystring = "/Purchaser/underConstruction.html";
}
function callPidEuRelationships()
{
	querystring ="/Purchaser/PurchaserEURelationshipServlet?PurIK = "+<%= session.getAttribute("PurIK")%>+"&SelectedAction=";	
}
<% } %>
//-->
</SCRIPT>
<script language="javascript" src="../script/common_css.js"></script>
</HEAD>
<body bgcolor="#0B5F77" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" OnLoad="init();">
<a id="dynamicTitl"></a>
<TABLE>
    <TR>
      <TD>
       <TABLE cellpadding="0" cellspacing="1">
          <TR>
            <TD><IMG src="/BASEWeb/Purchaser/images/generalinformation_y.gif" width="137" height="36" border="0" name="generalinformation" alt="General Information" onclick="return switchTab(this.id);" id="1"></TD>
          </TR>
          <TR>
            <TD><IMG src="/BASEWeb/Purchaser/images/administrativearrangements_y.gif" width="137" height="36" border="0" name="administrativearrangements" alt="Administrative Arrangements" onclick="return switchTab(this.id);" id="2"></TD>
          </TR>
          <TR>
            <TD><IMG src="/BASEWeb/Purchaser/images/brokerofrecord_y.gif" width="137" height="36" border="0" name="brokerofrecord" alt="Broker Of Records" onclick="return switchTab(this.id);" id="4"></TD>
          </TR>
          <TR>
            <TD><IMG src="/BASEWeb/Purchaser/images/payeebroker_y.gif" width="137" height="36" border="0" name="payeebroker" alt="Payee Broker" onclick="return switchTab(this.id);" id="5"></TD>
          </TR>
          <TR>
            <TD><IMG src="/BASEWeb/Purchaser/images/sellerbroker_y.gif" width="137" height="36" border="0" name="sellerbroker" alt="Seller Broker" onclick="return switchTab(this.id);" id="3"></TD>
          </TR>
          <TR>
            <TD><IMG src="/BASEWeb/Purchaser/images/amendments_y.gif" width="137" height="36" border="0" name="amendments" alt="Amendments" onclick="return switchTab(this.id);" id="7"></TD>
          </TR>
          <TR>
            <TD><IMG src="/BASEWeb/Purchaser/images/pidpideurelationships_y.gif" width="137" height="36" border="0" name="pidpideurelationships" alt="PID / PID_EU Relationships" onclick="return switchTab(this.id);" id="8"></TD>
          </TR>
          <TR>
            <TD><IMG src="/BASEWeb/Purchaser/images/kpstaff_y.gif" width="137" height="36" border="0" name="kpstaff" alt="KP Staff" onclick="return switchTab(this.id);" id="6"></TD>
          </TR>
      </TABLE>
      </TD>
    </TR>
</TABLE>
</BODY>
</HTML>