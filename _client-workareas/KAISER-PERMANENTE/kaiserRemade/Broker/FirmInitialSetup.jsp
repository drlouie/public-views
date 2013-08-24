<!-- Sample HTML file --> <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<jsp:useBean id="brokerDropDownVO" class="org.kp.broker.vo.BrokerDropDownVO" />
<%
	brokerDropDownVO = (org.kp.broker.vo.BrokerDropDownVO)session.getAttribute("DropDowns");
%>

<HTML>
<HEAD>
<META name="GENERATOR" content="IBM WebSphere Page Designer V3.5.3 for Windows">
<META http-equiv="Content-Style-Type" content="text/css">
<TITLE>Broker Administration System Exchange</TITLE>
<LINK href="Master.css" rel="stylesheet" type="text/css">

<%@ include file="script/FirmInitialRequired.js" %>

<!--
<SCRIPT src="script/FirmInitialRequired.js">
</SCRIPT>
-->
<Script src="script/PrintScript.js">
</Script>

<SCRIPT language="javascript">
function tinFormat(tin)
 {
  if(tin.length == 9)
   {
     document.FirmInitialSetup.TaxID_H.value = tin;	
     document.FirmInitialSetup.TaxID.size=11;
     document.FirmInitialSetup.TaxID.maxlength=11;
     var Formatedtin = "";
     for(var i = 0 ; i < tin.length ; i++)
      {
        if(i ==3)
	  {
          	Formatedtin+="-";
		Formatedtin+=tin.substring(i, i+1)
	  }
        else if(i ==5)
         { 
		Formatedtin+="-";
           	Formatedtin+=tin.substring(i, i+1)
          }		

  	 else
         Formatedtin+=tin.substring(i, i+1);
	}	
	document.FirmInitialSetup.TaxID.value=Formatedtin; 
    }
 }

</SCRIPT>

<SCRIPT language="javascript">
var states = new Array() ;
var canadianStates = new Array();
function init()
	{		

		<%		
			java.util.Vector state = new java.util.Vector();
									
			state = brokerDropDownVO.getState();
			
			for(int i = 0 ; i < state.size(); i++)
			{
		%>	
			
			states[<%=i%>] = '<%=state.elementAt(i)%>';
		<%
			}
		%>


	<% 
		java.util.Vector canSt = new java.util.Vector();
		canSt = brokerDropDownVO.getCanadianStates();						
		for(int i = 0 ; i < canSt.size(); i++){
	%>
			canadianStates[<%=i%>] = '<%=canSt.elementAt(i)%>';
	<%}%>	


			document.FirmInitialSetup.Status.disabled = true;
			document.FirmInitialSetup.Status.value = '';
			document.FirmInitialSetup.StatusReason.disabled = true;
			document.FirmInitialSetup.StatusReason.value = '';
			document.FirmInitialSetup.BrokerCategory.disabled = true;
			document.FirmInitialSetup.BrokerCategory.value = '';
			document.FirmInitialSetup.BrokerCategoryYear.value = '';
			document.FirmInitialSetup.BrokerCategoryYear.disabled = true;

			//Added by Sathish on Oct 18,2001
			document.FirmInitialSetup.TaxID.focus();
			document.FirmInitialSetup.Country.value = 'USA';
			
			setState( document.FirmInitialSetup );
		
	}


/*
function callPrint() {

	document.FirmInitialSetup.action = "PrintServlet";
	document.FirmInitialSetup.submit();

}
*/

function printFunction() {

	callPrint();
}

   function callSearch() {

		document.FirmInitialSetup.action="SearchServlet";
		document.FirmInitialSetup.submit();

   }


   function callExit() {

   	// DISABLE ALL Form Elements FROM THIS document
	var leTotal = document.forms[0].elements.length;
	for ( var i = 0 ; i <leTotal ; i++) {
		document.forms[0].elements[i].disabled = true;
	}

   	// HIDE ALL Form Elements
	var leTotal = document.FirmInitialSetup.elements.length;
	for ( var i = 0 ; i <leTotal ; i++) {
		document.FirmInitialSetup.elements[i].style.visibility = 'hidden';
	}

	
	if (document.getElementById) {  // DOM3 = IE5, NS6
		document.getElementById('hidepage2').style.visibility = 'visible';
	}
	else {
		if (document.layers) {  // Netscape 4
			document.hidepage2.visibility = 'visible';
		}
		else {  // IE 4
			document.all.hidepage2.style.visibility = 'visible';
		}
	}


   }


function saveLEFORM(cual) {
		if (cual == "Yes") {
			// hide layer
			hideIT();

			document.FirmInitialSetup.SaveExitPage.value = "Yes";
			if ( validateForm( document.FirmInitialSetup) ) {
				document.FirmInitialSetup.target="_parent";
				document.FirmInitialSetup.submit();
			}
		}
		else if (cual == "No") {
			parent.window.close();
		}
		else { 
			hideIT();
		}

	}

	function hideIT() {
		// HIDE LAYER
		if (document.getElementById) {  // DOM3 = IE5, NS6
			document.getElementById('hidepage2').style.visibility = 'hidden';
		}
		else {
			if (document.layers) {  // Netscape 4
				document.hidepage2.visibility = 'hidden';
			}
			else {  // IE 4
				document.all.hidepage2.style.visibility = 'hidden';
			}
		}
			

	   	// ENABLE ALL Form Elements FROM THIS document
		var leTotal = document.forms[0].elements.length;
		for ( var i = 0 ; i <leTotal ; i++) {
			document.forms[0].elements[i].disabled = false;
		}

  		// SHOW ALL Form Elements
		var leTotal = document.FirmInitialSetup.elements.length;
		for ( var i = 0 ; i <leTotal ; i++) {
			document.FirmInitialSetup.elements[i].style.visibility = 'visible';
		}
	}


	function setState( theForm ) {
	
		var country = theForm.Country.value;
		
		
		if ( country == "USA" ) {
			theForm.State.length = 0;		
			for ( var i=0; i<states.length; i++ ) {
				var addstate = new Option();
				addstate.text = states[i];
				addstate.value = states[i];
				theForm.State.options[i] = addstate;				
			}
			theForm.State.disabled = false;
			theForm.State.value = "";
		}
		else if ( country == "CAN" ) {
			theForm.State.length = 0;		
			for ( var i=0; i<canadianStates.length; i++ ) {
				var addstate = new Option();
				addstate.text = canadianStates[i];
				addstate.value = canadianStates[i];
				theForm.State.options[i] = addstate;				
			}
			theForm.State.disabled = false;
			theForm.State.value = "";			
		}
		else {
				theForm.State.length = 0;		
				theForm.State.disabled = true;
		}

	}



</SCRIPT>

<!-- START Additions by drlouie-->
<!--Dynamic CSS Javascript-->
<script language="javascript" src="script/common_css.js">
</script>

<script language="Javascript">
<!--
//MOUSEOVER IMAGE PRELOAD

//mreset
// // // MOUSE OVER
image1 = new Image();
image1.src = "limages/mreset_ov.gif";
// // // MOUSE OFF
image2 = new Image();
image2.src = "limages/mreset_off.gif";

//medit
image3 = new Image();
image3.src = "limages/medit_ov.gif";
image4 = new Image();
image4.src = "limages/medit_off.gif";
//msearch
image5 = new Image();
image5.src = "limages/msearch_ov.gif";
image6 = new Image();
image6.src = "limages/msearch_off.gif";
//msave
image7 = new Image();
image7.src = "limages/msave_ov.gif";
image8 = new Image();
image8.src = "limages/msave_off.gif";
//mprint
image9 = new Image();
image9.src = "limages/mprint_ov.gif";
image10 = new Image();
image10.src = "limages/mprint_off.gif";
//mexit
image11 = new Image();
image11.src = "limages/mexit_ov.gif";
image12 = new Image();
image12.src = "limages/mexit_off.gif";
//mcomments
image13 = new Image();
image13.src = "limages/mcomments_ov.gif";
image14 = new Image();
image14.src = "limages/mcomments_off.gif";


//add button
image15 = new Image();
image15.src = "limages/add_ov.gif";
image16 = new Image();
image16.src = "limages/add_off.gif";
//delete selected button
image17 = new Image();
image17.src = "limages/delsel_ov.gif";
image18 = new Image();
image18.src = "limages/delsel_off.gif";
//-->
</script>


<style type="text/css">
#leTitle {position:absolute; z-index:2001; top:10px; left: 15px; }
</style>

<!--End Additions by drlouie-->

</HEAD>
<BODY bgcolor="#0B5F77" onload="init()" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<FORM name="FirmInitialSetup" method="post" onsubmit="return validateForm(FirmInitialSetup);" action="FirmInitialSetup">
  <table width="850" border="0" cellspacing="0" cellpadding="0" align="center">
    <tr> 
      <td width="5" valign="top"><img src="limages/spacer.gif" border="0" width="5" height="5"></td>
      <td width="300" valign="top"><img src="limages/spacer.gif" border="0" width="5" height="5"></td>
      <td width="200"><img src="limages/spacer.gif" border="0" width="5" height="5"></td>
      <td width="300"><img src="limages/spacer.gif" border="0" width="5" height="5"></td>
      <td width="5"><img src="limages/spacer.gif" border="0" width="5" height="5"></td>
    </tr>
    <tr> 
      <td width="5" valign="top">&nbsp;</td>
      <td width="350" valign="top"> 
        <table width="380" border="0" cellspacing="0" cellpadding="0">
          <tr> 
            <td align="left" width="3" height="20"><img src="limages/tleft4.gif" width="3" height="24"></td>
            <td bgcolor="#E6E9F0" width="374"><font class="maintitle" id="theTitle"> 
              <nobr>BKR 200 - Broker Administer Firm (Initial Setup)</nobr></font></td>
            <td "align="right" width="3" height="20"><img src="limages/tright4.gif" width="3" height="24"></td>
          </tr>
        </table>
      </td>
      <td width="200" valign="top"><br>
        <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
          <tr> 
            <td bgcolor="#E6E9F0" width="100%"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
          </tr>
        </table>
      </td>
      <td width="300" align="right"> 
        <table width="300" border="0" cellspacing="0" cellpadding="0">
          <tr> 
            <td bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
            <td bgcolor="#E6E9F0" width="398"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
            <td bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
          </tr>
          <tr> 
            <td width="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
            <td height="37" width="398" align="center"> <a href="#" onMouseOver="javascript:msearch.src = image5.src;" onMouseOut="javascript:msearch.src = image6.src;" onClick="callSearch()"><img src="limages/msearch_off.gif" width="52" height="37" name="msearch" border="0"></a> 
              <input type="image" name="submit" src="limages/msave_off.gif" width="52" height="37" border="0">
              <a href="#" onMouseOver="javascript:mprint.src = image9.src;" onMouseOut="javascript:mprint.src = image10.src;" onClick="printFunction();"><img src="limages/mprint_off.gif" width="52" height="37" name="mprint" border="0"></a> 
              <a href="#" onMouseOver="javascript:mexit.src = image11.src;" onMouseOut="javascript:mexit.src = image12.src;" onClick="callExit()"><img src="limages/mexit_off.gif" width="52" height="37" name="mexit" border="0">
              <input type="hidden" name="GoTo" value="FirmInitialSetup.jsp">
              <input type="hidden" name="SaveExitPage" value="No">
              </a></td>
            <td width="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
          </tr>
          <tr> 
            <td height="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
            <td height="1" bgcolor="#E6E9F0" width="398"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
            <td height="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
          </tr>
        </table>
      </td>
      <td width="5">&nbsp;</td>
    </tr>
    <tr> 
      <td width="5" valign="top">&nbsp;</td>
      <td colspan="3" valign="top" height="35"> 
        <table width="125" border="0" cellspacing="0" cellpadding="0">
          <tr> 
            <td bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
            <td bgcolor="#E6E9F0" width="398"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
            <td bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
          </tr>
          <tr> 
            <td width="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
            <td height="20" width="198" align="center"> 
              <input type="radio" name="BrokerType" value="I" disabled>
              <font class="ComTitle">Agent</font> 
              <input type="radio" checked name="BrokerType" value="O">
              <font class="ComTitle">Firm</font></td>
            <td width="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
          </tr>
          <tr> 
            <td height="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
            <td height="1" bgcolor="#E6E9F0" width="398"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
            <td height="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
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
          <tr align="center"> 
            <td width="48" align="center"><font class="ComTitle">BID</font></td>
            <td width="75"><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Tax 
              ID</font></td>
            <td width="192" align="center"><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Status</font></td>
            <td width="125" align="center"><font class="ComTitle">Status Reason</font></td>
            <td width="71" align="center"><font class="ComTitle">Date</font></td>
            <td width="154">&nbsp;</td>
            <td width="56" align="center"><font class="ComTitle">BCY</font></td>
            <td width="119" align="center"><font class="ComTitle">Broker Category</font></td>
          </tr>
          <tr align="left" valign="middle" bgcolor="#E6E9F0"> 
            <td width="48" align="center"> 
              <input size="6" type="text" maxlength="12" name="BID" class="input1" readonly>
            </td>
            <td width="75" align="center"> 
              <input size="11" type="text" maxlength="9" class="input2" name="TaxID" tabindex="1">
              <input type="HIDDEN" name="TaxID_H" value="">
            </td>
            <td width="192" align="center"> 
              <select name="Status" class="select1">
                <option value="">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</option>
              </select>
            </td>
            <td width="125" align="center"> 
              <select name="StatusReason" class="select1">
                <option value="">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</option>
              </select>
            </td>
            <td width="71" align="center"> 
              <input size="11" type="text" maxlength="10" name="statusdate" class="input1" readonly>
            </td>
            <td width="154">&nbsp;</td>
            <td width="56" align="center"> 
              <select name="BrokerCategoryYear" class="select1">
                <option value="">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</option>
              </select>
            </td>
            <td width="119" align="center"> 
              <select name="BrokerCategory" class="select1">
                <option value=""></option>
                <option value="Regular">Regular</option>
                <option value="Prefered">Prefered</option>
              </select>
            </td>
          </tr>
        </table>
      </td>
      <td width="5">&nbsp;</td>
    </tr>
  </table>
  <table width="800" border="0" cellspacing="0" cellpadding="0" align="center">
    <tr> 
      <td width="5" valign="top">&nbsp;</td>
      <td colspan="3" valign="top"> 
        <table width="790" border="0" cellspacing="0" cellpadding="1">
          <tr align="center"> 
            <td><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Name</font></td>
            <td><font class="ComTitle">Location</font></td>
          </tr>
          <tr align="center" bgcolor="#E6E9F0"> 
            <td> 
              <input size="60" type="text" maxlength="80" name="FirmName" tabindex="2" class="input2">
            </td>
            <td> 
              <input size="40" type="text" maxlength="40" name="Location" tabindex="3" class="input2">
            </td>
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
        <table width="840" border="0" cellspacing="0" cellpadding="0">
          <tr> 
            <td width="355" height="20"><img src="limages/spacer.gif" border="0" width="1" height="5"></td>
            <td align="center" rowspan="2" valign="middle" width="110"><a href="#" onMouseOver="mreset.src = image1.src;" onMouseOut="javascript:mreset.src = image2.src;" onclick="document.FirmInitialSetup.reset();return false;"><img src="limages/mreset_off.gif" width="40" height="37" name="mreset" border="0"></a></td>
            <td align="right" width="375" height="20"><img src="limages/spacer.gif" border="0" width="1" height="5"></td>
          </tr>
          <tr> 
            <td valign="top" width="355" align="left"> 
              <table width="355" border="0" cellspacing="0" cellpadding="0">
                <tr> 
                  <td align="left" width="3" height="20"><img src="limages/tleft3.gif" width="3" height="20"></td>
                  <td bgcolor="#E6E9F0" width="349" align="center"><font class="stitle">&nbsp;Primary 
                    Payment Address</font></td>
                  <td align="right" width="3" height="20"><img src="limages/tright3.gif" width="3" height="20"></td>
                </tr>
              </table>
              <table width="355" border="0" cellspacing="0" cellpadding="0">
                <tr> 
                  <td><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                  <td width="398"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                  <td><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                </tr>
                <tr> 
                  <td bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                  <td bgcolor="#E6E9F0" width="398"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                  <td bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                </tr>
                <tr> 
                  <td width="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                  <td align="center"> 
                    <table width="353" border="0" cellspacing="0" cellpadding="2">
                      <tr valign="bottom"> 
                        <td align="center" width="176" valign="middle" height="27"><font class="ComTitle">Eff 
                          Date</font> 
                          <input size="8" type="text" maxlength="10" name="addresseffectivedate" class="input1" readonly>
                        </td>
                        <td align="center" valign="middle"><nobr><font class="ComTitle">Mail 
                          Stop#</font></nobr></td>
                        <td align="left" colspan="3" valign="middle"> 
                          <input size="8" type="text" maxlength="15" name="MailStop" tabindex="5" class="input2">
                        </td>
                      </tr>
                      <tr valign="bottom"> 
                        <td align="right" width="176" height="27"><nobr><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Line 
                          1</font>&nbsp; 
                          <input size="20" type="text" maxlength="50" name="Line1" tabindex="4" class="input2">
                          </nobr> </td>
                        <td width="75" height="27" align="right"><font class="ComTitle">State</font></td>
                        <td width="37" height="27"> 
                          <select name="State" tabindex="9" class="select2">
                            <option value="">&nbsp;&nbsp;&nbsp;</option>
                          </select>
                        </td>
                        <td height="27" valign="bottom" align="right" width="20"><font class="ComTitle">Zip</font></td>
                        <td width="52" height="27"> 
                          <input size="5" type="text" maxlength="10" name="Zip" tabindex="10" class="input2">
                        </td>
                      </tr>
                      <tr valign="bottom"> 
                        <td align="right" width="176"><nobr><font class="ComTitle">Line 
                          2</font>&nbsp; 
                          <input size="20" type="text" maxlength="50" name="Line2" tabindex="6" class="input2">
                          </nobr></td>
                        <td width="75" align="right"><font class="ComTitle">County</font></td>
                        <td width="187" colspan="3"> 
                          <input size="20" type="text" maxlength="20" name="County" tabindex="12" class="input2">
                        </td>
                      </tr>
                      <tr valign="bottom"> 
                        <td align="right" width="176"><nobr><font class="ComTitle">Line 
                          3</font>&nbsp; 
                          <input size="20" type="text" maxlength="50" name="Line3" tabindex="7" class="input2">
                          </nobr> </td>
                        <td width="75" align="right"><font class="ComTitle">Country</font></td>
                        <td width="187" colspan="3"> 
                          <select name="Country" tabindex="11" onChange="setState( document.FirmInitialSetup)" class="select2">
                            <% 
			
			java.util.Vector country = new java.util.Vector();
			country = brokerDropDownVO.getCountry();		
			
			for(int i = 0 ; i < country.size(); i++)
				{
		%>
                            <option value = '<%=country.elementAt(i)%>'><%=country.elementAt(i)%></option>
                            <%
				}			
		%>
                          </select>
                        </td>
                      </tr>
                      <tr valign="bottom"> 
                        <td align="right" width="176"><nobr><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>City</font>&nbsp; 
                          <input size="20" type="text" maxlength="50" name="City" tabindex="8" class="input2">
                          </nobr> </td>
                        <td width="75" align="right"><font class="ComTitle">Province</font></td>
                        <td width="187" colspan="3"> 
                          <input size="20" type="text" maxlength="20" name="Province" tabindex="13" class="input2">
                        </td>
                      </tr>
                      <tr valign="bottom"> 
                        <td align="right" width="176"><img src="limages/spacer.gif" border="0" width="5" height="5"></td>
                        <td colspan="4"><img src="limages/spacer.gif" border="0" width="5" height="5"></td>
                      </tr>
                    </table>
                  </td>
                  <td width="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                </tr>
                <tr> 
                  <td height="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                  <td height="1" bgcolor="#E6E9F0" width="398"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                  <td height="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                </tr>
              </table>
            </td>
            <td align="right" valign="top" width="375">&nbsp; </td>
          </tr>
        </table>
      </td>
      <td width="5">&nbsp;</td>
    </tr>
  </table>
  </FORM>

<!-- FOR SAVING THIS FORM -->
<div id="hidepage2" style="position: absolute; left:0px; top:0px; background-color: #0B5F77; layer-background-color: #0B5F77; height: 100%; width: 100%;visibility:hidden">
<TABLE align="center" height="100%">
    <TBODY>
        <TR>
            <TD valign="middle" align="center"><img src="limages/alert.gif" border="0" vspace="15"><br><FONT class="stitle2" style="font-size:12px;">Do you want to save any unsaved information for the form named above?</FONT><br><br><form name="URLer2"><INPUT type="button" name="Yes" value="Yes" OnClick="saveLEFORM('Yes');" class="lebotton2">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<INPUT type="button" name="No" value="No" OnClick="saveLEFORM('No');" class="lebotton2" style="font-size:12px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<INPUT type="button" name="Cancel" value="Cancel" OnClick="saveLEFORM('Cancel');" class="lebotton2" style="font-size:12px;"></form></TD>
        </TR>
    </TBODY>
</TABLE>
</div> 

</BODY>
</HTML>