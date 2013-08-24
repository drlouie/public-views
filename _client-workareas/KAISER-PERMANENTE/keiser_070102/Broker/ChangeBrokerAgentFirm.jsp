<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML>
<jsp:useBean id="brokerVO"  class="org.kp.broker.vo.BrokerVO"  scope="session"></jsp:useBean>
<jsp:useBean id="agentVO"  class="org.kp.broker.vo.AgentVO"  scope="session"></jsp:useBean>
<HEAD>
<!-- <SCRIPT language="JavaScript1.1" src="/javascript/changeagenttofirm.js"></SCRIPT>-->
<META name="GENERATOR" content="IBM WebSphere Page Designer V3.5.3 for Windows">
<META http-equiv="Content-Style-Type" content="text/css">
<TITLE>Change Broker( Agent to Firm )</TITLE>
<LINK href="Master.css" rel="stylesheet" type="text/css">

<Script src="script/PrintScript.js">
</Script>


<Script language="JavaScript">

   //Added by Sathish on 11/20/2001 to set the Business Type

   function setValues() {

	document.agenttofirm.businessType.value = "";

	if ( "<%=brokerVO.getBusinessType()%>" != null ) {

		var bsnstype = "<%=brokerVO.getBusinessType()%>";

		if ( bsnstype == "SP" )
			bsnstype = "Sole Proprietor"; 
		else if ( bsnstype == "GP" )
			bsnstype = "General Partnership"; 
		else if ( bsnstype == "LP" )
			bsnstype = "Limited Partnership"; 
		else if ( bsnstype == "LL" )
			bsnstype = "LLP"; 
		else if ( bsnstype == "CC" )
			bsnstype = "Corporation (C)"; 
		else if ( bsnstype == "CS" )
			bsnstype = "Corporation (S)"; 
		else if ( bsnstype == "O" )
			bsnstype = "Other"; 
		else if ( bsnstype == "U" )
			bsnstype = "Unknown"; 

		document.agenttofirm.changeto_agent_businesstype.value = bsnstype;
	}

	document.agenttofirm.taxId.focus();

   }


   //Added by Sathish on 10/03 to call comments
   function callComments() {


	document.agenttofirm.sourceId1.value = document.agenttofirm.bid.value;
	/*
	document.agenttofirm.action="Comments/ComFrame.jsp";
	document.agenttofirm.submit();
	*/

	var url = 'Comments/CommentServlet?sourceId1='+document.agenttofirm.sourceId1.value+'&sourceId2=0&sourceId3=0&sourceInd=BKR&funType=DMGR';
	window.open(url, 'slideWindow',false,500,700);


   }

/*
   function callPrint() {

	document.agenttofirm.action="PrintServlet";
	document.agenttofirm.submit();

   }
*/
function printFunction() {

	callPrint();
}   
   
   
   function callExit() {

   	// DISABLE ALL Form Elements FROM THIS document
	var leTotal = document.forms[0].elements.length;
	for ( var i = 0 ; i <leTotal ; i++) {
		document.forms[0].elements[i].disabled = true;
	}

   	// HIDE ALL Form Elements
	var leTotal = document.agenttofirm.elements.length;
	for ( var i = 0 ; i <leTotal ; i++) {
		document.agenttofirm.elements[i].style.visibility = 'hidden';
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

			document.agenttofirm.SaveExitPage.value = "Yes";
			if ( validateForm(document.agenttofirm) ) {
				document.agenttofirm.target="_parent";
				document.agenttofirm.submit();
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
		var leTotal = document.agenttofirm.elements.length;
		for ( var i = 0 ; i <leTotal ; i++) {
			document.agenttofirm.elements[i].style.visibility = 'visible';
		}
	}

   
</Script>


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
<BODY bgcolor="#0B5F77" OnLoad="setValues()" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<Form name="agenttofirm"  method ="post" action="ChangeBrokerTypeServlet">
<!--<input type="hidden" name="action" value="">-->
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
              <nobr>BRK102 - Change Broker Type ( Agent to Firm)</nobr></font></td>
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
          <td height="37" width="398" align="center"> 
            <input type="image" name="submit" src="limages/msave_off.gif" width="52" height="37" border="0" onClick=" return validateForm(document.agenttofirm)">
            <a href="#" onMouseOver="javascript:mprint.src = image9.src;" onMouseOut="javascript:mprint.src = image10.src;" onClick="printFunction();"><img src="limages/mprint_off.gif" width="52" height="37" name="mprint" border="0"></a> 
            <a href="#" onMouseOver="javascript:mexit.src = image11.src;" onMouseOut="javascript:mexit.src = image12.src;" onClick="callExit()"><img src="limages/mexit_off.gif" width="52" height="37" name="mexit" border="0"></a><a href="#" onMouseOver="javascript:mcomments.src = image13.src;" onMouseOut="javascript:mcomments.src = image14.src;" onClick="callComments()"><img src="limages/mcomments_off.gif" width="66" height="37" name="mcomments" border="0"></a></td>
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
    <td colspan="3" valign="top"> 
      <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
        <tr> 
          <td width="35%" valign="top"> 
            <table width="180" border="0" cellspacing="0" cellpadding="0">
              <tr> 
                <td align="left" width="3" height="20"><img src="limages/tleft4.gif" width="3" height="24"></td>
                <td bgcolor="#E6E9F0" width="174"><font class="maintitle" id="theTitle"> 
                  <nobr> </nobr></font>
                  <table cellpadding="3" cellspacing="0" width="100%">
                    <tr bgcolor="#E6E9F0"> 
                      <td  width="50%" align="center"><font class="stitle">BID</font></td>
                      <td width="50%" align="center"><input size="10" type="text" maxlength="10" name="bid" value ="<%=brokerVO.getBID() %>" style="background-color : silver;" readonly class="input1"></td>
                    </tr>
                  </table>
                </td>
                <td "align="right" width="3" height="20"><img src="limages/tright4.gif" width="3" height="24"></td>
              </tr>
            </table>
          </td>
          <td valign="middle" width="65%" align="center"> 
            <input type="hidden" name="sourceInd" value="BKR">
            <input type="hidden" name="sourceId1" value="">
            <input type="hidden" name="sourceId2" value="0">
            <input type="hidden" name="sourceId3" value="0">
            <input type="hidden" name="GoTo" value="ChangeBrokerAgentFirm.jsp">
            <input type="hidden" name="SaveExitPage" value="No">
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
          <td width="455" height="20"><img src="limages/spacer.gif" border="0" width="1" height="5"></td>
          <td align="center" rowspan="2" valign="middle" width="110"><a href="#" onMouseOver="mreset.src = image1.src;" onMouseOut="javascript:mreset.src = image2.src;" onClick="clearForm(document.agenttofirm)"><img src="limages/mreset_off.gif" width="40" height="37" name="mreset" border="0"></a></td>
          <td align="right" width="275" height="20"> <img src="limages/spacer.gif" border="0" width="1" height="5"></td>
        </tr>
        <tr> 
          <td valign="top" width="455" align="left"> 
            <table width="455" border="0" cellspacing="0" cellpadding="0">
              <tr> 
                <td align="left" width="3" height="20"><img src="limages/tleft3.gif" width="3" height="20"></td>
                <td bgcolor="#E6E9F0" width="439" align="center"><font class="stitle">&nbsp;Existing 
                  Information </font></td>
                <td align="right" width="3" height="20"><img src="limages/tright3.gif" width="3" height="20"></td>
              </tr>
            </table>
            <table width="455" border="0" cellspacing="0" cellpadding="0">
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
                <td align="center" width="100%"> 
                  <table width="100%" border="0" cellspacing="0" cellpadding="0">
                    <tr> 
                      <td align="right" width="40%" height="15"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                      <td align="center" width="60%" height="15"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                    </tr>
                    <tr> 
                      <td align="right" width="40%"><nobr><font class="ComTitle">Broker 
                        Type </font>&nbsp; 
                        <input class="input1" size="10" type="text" maxlength="10" name="changeto_brokertype" value="Agent" readonly style="background-color : silver;">
                        </nobr></td>
                      <td align="center" width="60%"><nobr><font class="ComTitle">Business 
                        Type</font> 
                        <input class="input1" size="20" type="text" maxlength="20" name="changeto_agent_businesstype" value="" style="background-color : silver;" readonly>
                        </nobr></td>
                    </tr>
                    <tr> 
                      <td align="right" width="40%" height="15"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                      <td align="center" width="60%" height="15"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                    </tr>
                    <tr> 
                      <td align="right" width="40%"><nobr><font class="ComTitle">Tax 
                        ID </font>&nbsp; 
                        <input  class="input1" size="10" type="text" maxlength="10" name="changeto_agent_taxid" value="<%=brokerVO.getTaxID() %>" style="background-color : silver;" readonly>
                        </nobr> </td>
                      <td align="center" width="60%">&nbsp; </td>
                    </tr>
                    <tr> 
                      <td align="right" width="40%" height="15"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                      <td align="center" width="60%" height="15"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
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
              <tr> 
                <td width="1" bgcolor="#E6E9F0">&nbsp;</td>
                <td align="center"> 
                    <table cellpadding="0" cellspacing="0" width="100%">
                      <tbody> 
                      <tr> 
                        <td  rowspan="2" align="center" width="10%" bgcolor="#E6E9F0"><font class="stitle">Name</font></td>
                        <td  align="center" height="20" valign="bottom"><font class="ComTitle">Honor</font></td>
                        <td  align="center" height="20" valign="bottom"><font class="ComTitle">First</font></td>
                        <td  align="center" height="20" valign="bottom"><font class="ComTitle">Middle</font></td>
                        <td  align="center" height="20" valign="bottom"><font class="ComTitle">Last</font></td>
                        <td  align="center" height="20" valign="bottom"><font class="ComTitle">Suffix</font></td>
                      </tr>
                      <tr> 
                        <td align="center" height="30" valign="top"> 
                          <input class="input1" size="5" type="text"  maxlength="10" name="changeto_agent_honorific" value="<%=agentVO.getHonor() %> " style="background-color : silver;" readonly >
                        </td>
                        <td align="center" height="30" valign="top"> 
                          <input class="input1" size="15" type="text" maxlength="20" name="changeto_agent_firstname" value="<%=agentVO.getFirstName() %>"style="background-color : silver;" readonly>
                        </td>
                        <td align="center" height="30" valign="top"> 
                          <input class="input1" size="15" type="text" maxlength="10" name="changeto_agent_middle" value="<%=agentVO.getMiddleName() %>" style="background-color : silver;" readonly>
                        </td>
                        <td align="center" height="30" valign="top"> 
                          <input class="input1" size="15" type="text" maxlength="20" name="changeto_agent_lastname" value="<%=agentVO.getLastName() %>" style="background-color : silver;" readonly>
                        </td>
                        <td align="center" height="30" valign="top"> 
                          <input class="input1" size="10" type="text" maxlength="10" name="changeto_agent_suffix" value="<%=  agentVO.getSuffix() %>"style="background-color : silver;" readonly>
                        </td>
                      </tr>
                      <tr align="center" valign="bottom"> 
                        <td  height="15" bgcolor="#E6E9F0">&nbsp;</td>
                        <td  colspan="2" height="15"><font class="ComTitle">Title</font></td>
                        <td height="15">&nbsp;</td>
                        <td height="15" colspan="2"><font class="ComTitle">Familiar 
                          Name</font></td>
                      </tr>
                      <tr valign="top"> 
                        <td  align="center" height="25" bgcolor="#E6E9F0">&nbsp;</td>
                        <td  colspan="2" align="center" height="25"> 
                          <input class="input1" size="20" type="text" maxlength="20" name="changeto_agent_title" value="<%=  agentVO.getTitle() %> " style="background-color : silver;" readonly>
                        </td>
                        <td align="center" height="25">&nbsp; </td>
                        <td align="center" height="25" colspan="2">
                          <input class="input1" size="20" type="text" maxlength="20" name="chagneto_agent_familiarname" value="<%=  agentVO.getFamiliarName() %> " style="background-color : silver;" readonly>
                        </td>
                      </tr>
                      </tbody> 
                    </table>
                </td>
                <td width="1" bgcolor="#E6E9F0">&nbsp;</td>
              </tr>
              <tr> 
                <td height="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                <td height="1" bgcolor="#E6E9F0" width="398"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                <td height="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
              </tr>
            </table>
          </td>
          <td align="right" valign="top" width="275">
            <table width="275" border="0" cellspacing="0" cellpadding="0">
              <tr> 
                <td align="left" width="3" height="20"><img src="limages/tleft3.gif" width="3" height="20"></td>
                  <td bgcolor="#E6E9F0" width="269" align="center"><font class="stitle">&nbsp;New 
                    Information </font></td>
                <td align="right" width="3" height="20"><img src="limages/tright3.gif" width="3" height="20"></td>
              </tr>
            </table>
            <table width="275" border="0" cellspacing="0" cellpadding="0">
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
                <td align="center" width="100%"> 
                  <table width="100%" border="0" cellspacing="0" cellpadding="0">
                    <tr> 
                      <td align="center" width="60%" height="15"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                    </tr>
                    <tr> 
                      <td align="center" width="60%"><nobr><font class="ComTitle">Broker 
                        Type</font></nobr><nobr> 
                        <input class="input1" size="10" type="text"  name="brokerType" value="Firm" maxlength="10"  style="background-color : silver;"  readonly>
                        </nobr></td>
                    </tr>
                    <tr> 
                      <td align="center" width="60%" height="15"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
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
              <tr> 
                <td width="1" bgcolor="#E6E9F0">&nbsp;</td>
                <td align="center">
                    <table width="100%" border="0" cellspacing="0" cellpadding="0">
                      <tr> 
                        <td align="right" height="15"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                        <td align="left" width="100%" height="15">&nbsp;</td>
                    </tr>
                    <tr> 
                        <td align="right"><nobr><font class="ComTitle">Tax ID </font>&nbsp; 
                          </nobr></td>
                        <td align="left" width="100%"> 
                          <input class="input2" size="25" type="text" name="taxId" maxlength="9" tabindex="1">
                      </td>
                    </tr>
                    <tr> 
                        <td align="right" height="15"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                        <td align="left" width="100%" height="15">&nbsp;</td>
                    </tr>
                    <tr> 
                        <td align="right"><nobr><font class="ComTitle">Nam</font></nobr><nobr><font class="ComTitle">e 
                          </font>&nbsp; </nobr> </td>
                        <td align="left" width="100%"> 
                          <input class="input2" size="25" type="text" name="firmName" maxlength="30" tabindex="3">
                      </td>
                    </tr>
                    <tr> 
                        <td align="right" height="15"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                        <td align="left" width="100%" height="15">&nbsp;</td>
                    </tr>
                    <tr> 
                        <td align="right"><nobr><font class="ComTitle">Location</font>&nbsp; 
                          </nobr> </td>
                        <td align="left" width="100%"> 
                          <input class="input2" size="25" type="text" name="locName" maxlength="20" tabindex="4">
                      </td>
                    </tr>
                    <tr> 
                        <td align="right" height="15"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                        <td align="left" width="100%" height="15">&nbsp;</td>
                    </tr>
                    <tr> 
                        <td align="right"><nobr><font class="ComTitle">&nbsp;&nbsp;&nbsp;Business type</font>&nbsp;</nobr></td>
                        <td align="left" width="100%"> 
                          <select class="select2" name="businessType" tabindex="2">
                          <%
	java.util.Vector busiValue = (java.util.Vector) session.getAttribute("bsnsValue");
	java.util.Vector busiText = (java.util.Vector) session.getAttribute("bsnsText");
	for(int i=0;i<busiValue.size();i++){
   %>
                          <option value="<%=(String)busiValue.elementAt(i) %>"><%=(String)busiText.elementAt(i) %></option>
                          <%
  }
 %>
                        </select>
                      </td>
                    </tr>
                    <tr> 
                        <td align="right" height="15"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                        <td align="left" width="100%" height="15">&nbsp;</td>
                    </tr>
                  </table>
                </td>
                <td width="1" bgcolor="#E6E9F0">&nbsp;</td>
              </tr>
              <tr> 
                <td height="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                <td height="1" bgcolor="#E6E9F0" width="398"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                <td height="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
    </td>
    <td width="5">&nbsp;</td>
  </tr>
</table>


<script language="javascript">

function validateForm(theForm)
 {	
var errorStatus = false;
var errorFields ='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.ErrorMessagePrefix")%>'+'\n';

  if(document.agenttofirm.taxId.value == "")
   {
	errorFields +='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.TaxIDRequired")%>'+'\n';
	errorStatus = true;
   }	
  else
   {
   	checkTaxID(document.agenttofirm.taxId.value);
   }

if(document.agenttofirm.firmName.value == "")
   {
	errorFields +='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.FirmNameRequired")%>'+'\n';
	errorStatus	= true;			
   }  else
   {
	checkFirmName(document.agenttofirm.firmName.value);
   }
  if(document.agenttofirm.locName.value != "")
   {
   /*
	errorFields+="Location Name is a required field\n";
 	errorStatus = true;		
   }
  else
   {
   */
	checkLocName(document.agenttofirm.locName.value);
   }  


  if(document.agenttofirm.businessType.value == "")
   {
	errorFields +='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.BusinessTypeRequired")%>'+'\n';
 	errorStatus = true;		
   }


   if ( errorStatus == true )
   {
	alert(errorFields);
	return false;
   }
   else
	return true;



function checkTaxID(TaxID)
 {
   var checkOK = "0123456789";
   var checkStr = TaxID;
   var allValid = true;
   var decPoints = 0;
   var allNum = "";
   for (i = 0;  i < checkStr.length;  i++)
    {
     ch = checkStr.charAt(i);
     for (j = 0;  j < checkOK.length;  j++)
     if (ch == checkOK.charAt(j))
     break;
     if (j == checkOK.length)
      {
      	allValid = false;
      	break;
      }
     allNum += ch;
     }
    if (!allValid)
     {
		errorFields +='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+'Tax ID\n';
    	document.agenttofirm.taxId.focus();
    	errorStatus = true;
     }
	
    if (theForm.taxId.value.length<9)
     {
	errorFields +='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.TaxIDDigits")%>'+'\n';
	document.agenttofirm.taxId.focus();
	errorStatus = true;
     }
		
 }//End of checkTaxID function


function checkFirmName(field)
 {
  var valid = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";
  

for (var i=0; i < field.length; i++) 
 {
  temp = "" + field.substring(i, i+1);
  if (valid.indexOf(temp) == "-1") 
    {
	errorFields +='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+'Firm Name\n';
	document.agenttofirm.firmName.focus();
      break;
    }
 }
 }//End of checkFirstName function

function checkLocName(field)
 {
  var valid = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";
  

for (var i=0; i < field.length; i++) 
 {
  temp = "" + field.substring(i, i+1);
  if (valid.indexOf(temp) == "-1") 
    {
	errorFields +='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+'Location Name\n';
      document.agenttofirm.locName.focus();
	break;
    }
 }
 }//End of checkFirstLast function


}//End of validateForm function
function clearForm(form) {


          document.agenttofirm.taxId.value="";
	  document.agenttofirm.firmName.value ="";	
	  document.agenttofirm.locName.value ="";
	  document.agenttofirm.locName.value ="";	
          document.agenttofirm.businessType.value =""
          document.agenttofirm.taxId.text ="";
	  document.agenttofirm.firmName.text ="";	
	  document.agenttofirm.locName.text ="";
	  document.agenttofirm.locName.text ="";	
          document.agenttofirm.businessType.text =""
           
}


<!--

    function submit_form(action) {
        var form = document.form_agent;
		
	var error_text = "";
		
	form.action.value = action;
	form.submit();                
	  
    }
    
//-->
</script>

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