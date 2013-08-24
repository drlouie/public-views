<!-- Sample JSP file --> <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<%@ page import = "org.kp.base.util.BaseUtil,java.util.HashMap,org.kp.purchaser.vo.BrokerOfRecordVO" %>
<jsp:useBean id="payeeVO"  class="org.kp.purchaser.vo.PayeeVO"  scope="session"></jsp:useBean>
<jsp:useBean id="borVO"  class="org.kp.purchaser.vo.BrokerOfRecordVO"  scope="session"></jsp:useBean>
<HTML>
<HEAD>
<%@ include file="script/validatePayee.js" %>
<!-- fds<SCRIPT language="JavaScript1.1" src="/BASEWeb/Purchaser/script/validatePayee.js"></SCRIPT> -->
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
IMG{
  color : olive;
}

.pbttn {
	font-family: arial;
	font-size:13px;
	color:#ffffff;height: 26px;
	text-decoration: none;
	padding-left: 4px;
	padding-right: 4px;
	padding-top:2px;
	padding-bottom: 2px;	
	cursor: hand;
	background-color: #5662af;
	border-top-color: #4A4D7B;
	border-left-style: solid;
	border-left-width: 1px;
	font-weight: bold;
	border-top-style: solid;
	border-left-color: #4A4D7B;
	border-top-width: 1px;
	border-bottom-style: solid;
	border-bottom-width: 1px;
	border-right-style: solid;
	border-right-width: 1px;
	border-bottom-color: #4A4D7B;
	border-right-color: #4A4D7B;
	vertical-align: middle;
	text-align: center;
	}
-->
</STYLE>
<SCRIPT language="JavaScript">
function IsThisDateRangeCurrent(EffectiveDate,EndDate)
{
		 var Status = false;
		 var currentdate = document.PayeeBroker.CurrentDate.value;
		 if(EndDate == "")
		 	EndDate = "12/31/4000";
		 		
   	     var effmm = EffectiveDate.substring(0, 2);
         var effdd = EffectiveDate.substring(3, 5);
         var effyyyy = EffectiveDate.substring(6, 10);
         
         var endmm = EndDate.substring(0, 2);
         var enddd = EndDate.substring(3, 5);
         var endyyyy = EndDate.substring(6, 10);


   	 	 var curmm = currentdate.substring(0, 2);
         var curdd = currentdate.substring(3, 5);
         var curyyyy = currentdate.substring(6, 10);
 
		if ( endyyyy <= curyyyy ) 
		{
			if( endyyyy == curyyyy )
			{
				if( endmm <= curmm )
				{
					if( endmm == curmm )
					{
						if( enddd >= curdd )
						{
							Status = true;
						}
						else
							Status = false;
					}
					else
						Status = false;
				}
				else 
					Status = true;
			}
			else
				Status = false;
		}
		else
			Status = true;
			
		if(Status == true)
		{
			if( effyyyy >= curyyyy )
			{
				if( effyyyy == curyyyy )
				{
					if( effmm >= curmm )
					{
						if( effmm == curmm )
						{
							if(effdd > curdd )
							{
								Status = false;
							}
							else
								Status = true;
						}
						else
							Status = false;
					}
					else 
						Status = true;
					
				}
				else
					Status = false;
				
			}
			else 
				Status = true;
			
		}
	return Status;
}


 function addListHide()
 {
  	document.PayeeBroker.CurrentDate.value = "<%=(String)session.getAttribute("CurrentDate")%>";
 	disableform();
    document.PayeeBroker.displayBid.value="";
	document.PayeeBroker.payeeBrokerID.value="";
	<%
		String isName = "Y";
   		isName = (String) session.getAttribute("isName");
    	if(isName.equals("Y"))
   		{ 
  			org.kp.purchaser.vo.PayeeVO brokerNameVO  = ( org.kp.purchaser.vo.PayeeVO )session.getAttribute("payeeNameVO");	
	    %>
	enableform();
  
   	document.PayeeBroker.payeeName.value="<%=BaseUtil.asString(brokerNameVO.getPayeeName()) %>";
	document.PayeeBroker.borBrokerID.value="<%=brokerNameVO.getBorBrokerId() %>";
	document.PayeeBroker.displayBid.value="<%=brokerNameVO.getDisplayBid() %>";
	document.PayeeBroker.payeeBrokerID.value="<%=brokerNameVO.getPayeeBrokerId() %>";
	document.PayeeBroker.brokerStatus.value="<%=BaseUtil.asString(brokerNameVO.getBrokerStatus()) %>";
	document.PayeeBroker.effectiveDate.value = "<%=BaseUtil.asString(brokerNameVO.getEffectiveDate()) %>";
	document.PayeeBroker.endDate.value = "<%=BaseUtil.asString(brokerNameVO.getEndDate()) %>";
	document.PayeeBroker.payeeShare.value = "<%=BaseUtil.asString(brokerNameVO.getPayeeShare()) %>" ;
	document.PayeeBroker.payeeId.value = "<%=brokerNameVO.getIdentifier() %>" ;
	document.PayeeBroker.SortOrder.value="<%=brokerNameVO.getSortOrder()%>" ;
	document.PayeeBroker.statusIndicator.value ="<%=BaseUtil.asString(brokerNameVO.getStatusIndicator())%>";
	document.PayeeBroker.recordKey.value ="<%=brokerNameVO.getRecordKey()%>";
	document.PayeeBroker.pbrik.value ="<%=brokerNameVO.getPbrIk()%>";
	document.PayeeBroker.bprik.value ="<%=brokerNameVO.getBprIk()%>";
	document.PayeeBroker.defaultIndicator.value ="<%=BaseUtil.asString(brokerNameVO.getDefaultIndicator()) %>";
	<%
     }
    %>
	document.PayeeBroker.AddList.style.visibility = "hidden";
	var elementsMaxLength = new Array();
	var elementsText = new Array();
	elementsMaxLength[0] =28;
	elementsMaxLength[1] =11;
	elementsMaxLength[2] = 36;
	elementsMaxLength[3] = 11;
	elementsMaxLength[4] = 11; 
	elementsMaxLength[5] = 6;
	elementsMaxLength[6] = 1;
	<%
	HashMap map =(HashMap) session.getAttribute("PBRLIST");
	java.util.Vector payeeVec = new java.util.Vector();
	 payeeVec = (java.util.Vector) session.getAttribute("ModifiedPayee");
	int vecSize =payeeVec.size();
		for( int i=vecSize; i > 0; i-- ) {
		payeeVO = ( org.kp.purchaser.vo.PayeeVO ) payeeVec.elementAt(i-1);
			int j =1;
       BrokerOfRecordVO bVO =(BrokerOfRecordVO) map.get(Integer.toString(payeeVO.getBorBrokerId())+Integer.toString(payeeVO.getPbrIk())) ;
	   if(bVO == null || "A".equalsIgnoreCase(bVO.getStatusIndicator()))
	   		bVO =new BrokerOfRecordVO();
	    %>
      		document.PayeeBroker.AddList.style.visibility = "";
 			elementsText[0] = "<%=payeeVO.getBorBrokerId()+"("+ (BaseUtil.asString(payeeVO.getDefaultIndicator()).equalsIgnoreCase("Y")?"Default":"Non-Def")+")"%>" ; ;
			elementsText[1] = "<%=payeeVO.getPayeeBrokerId()%>" ;
			elementsText[2] = "<%=BaseUtil.asString(payeeVO.getPayeeName())%>";
			elementsText[3] = "<%=BaseUtil.asString(payeeVO.getEffectiveDate()) %>";
			elementsText[4] = "<%=BaseUtil.asString(payeeVO.getEndDate())%>";	
			elementsText[5] = "<%=BaseUtil.asString(payeeVO.getPayeeShare())%>";
			elementsText[6] = "<%=BaseUtil.asString(payeeVO.getStatusIndicator())%>";
		 if( elementsText[6] != "A" && elementsText[6] != "D" ) 
		 {
		  	if( IsThisDateRangeCurrent(elementsText[3],elementsText[4] ) )
		 		elementsText[6] = '***';
		 	else if( <%=payeeVO.getSortOrder()%> != 0 )
		 		elementsText[6] = "U"; 
		 	else 	 		
		 	   	elementsText[6] = "";
         }   	
		for(var i = 0 ; i < elementsMaxLength.length; i++)
		{	
			if(elementsText[i].length < elementsMaxLength[i])
				{	
					for(j = elementsText[i].length ; j < elementsMaxLength[i]; j++)
						{			
							elementsText[i]+= " ";							
						}
				}
			else
				elementsText[i] = elementsText[i].substring(0,elementsMaxLength[i]);
		}
		var addoptions = new Option();
	 	addoptions.text = elementsText[0] + "" + elementsText[1] + "" + elementsText[2] + ""+ elementsText[3] + "" +elementsText[4] +""+elementsText[5]+elementsText[6];  
		addoptions.value = "<%=payeeVO.getBorBrokerId()%>" + ":" + "<%=payeeVO.getPayeeBrokerId()%>" + ":" 
		+"<%=payeeVO.getPayeeName() %>" + ":" + "<%=payeeVO.getEffectiveDate() %>"+ ":"+ "<%=payeeVO.getEndDate()%>" 
		+ ":" + "<%=payeeVO.getPayeeShare()%>"+":"+"<%=payeeVO.getStatusIndicator()%>"+ ":" +"<%=payeeVO.getBrokerStatus()%>" + ":" + 
		"<%=payeeVO.getIdentifier()%>"+":"+"<%=payeeVO.getSortOrder()%>"+":"+"<%=payeeVO.getRecordKey()%>"+":"
		+"<%=payeeVO.getPbrIk()%>"+":"+"<%=payeeVO.getBprIk()%>"+":"+"<%=bVO.getBID()+" (" +bVO.getEffectiveDate()+"-"+bVO.getEndDate()+" )" %>"+":"+"<%=payeeVO.getDefaultIndicator()%>";
 

		document.PayeeBroker.AddList.options[document.PayeeBroker.AddList.options.length] = addoptions;			


		<%
		if( i == 0 ) {
		%>

		<%
		}
		%>
 			
		<%
		}
		%>
	<%

	String error = (String) session.getAttribute("ERROR");

	if ( ! error.equals("nothing") ) {
	isName = (String) session.getAttribute("isName");
  	org.kp.purchaser.vo.PayeeVO pyVO = (org.kp.purchaser.vo.PayeeVO) session.getAttribute("payVOError");
    if(isName.equals("E"))
	{
		%>
	
	document.PayeeBroker.payeeName.value="";
	document.PayeeBroker.borBrokerID.value="";
	document.PayeeBroker.displayBid.value="";
	document.PayeeBroker.payeeBrokerID.value="";
	document.PayeeBroker.brokerStatus.value="";
	document.PayeeBroker.effectiveDate.value = "";
	document.PayeeBroker.endDate.value = "";
	document.PayeeBroker.payeeShare.value = "" ;
	document.PayeeBroker.payeeId.value = "0" ;
	document.PayeeBroker.SortOrder.value="-10000" ;
	document.PayeeBroker.recordKey.value="0" ;
	document.PayeeBroker.statusIndicator.value ="";
	document.PayeeBroker.pbrik.value ="0";
	document.PayeeBroker.bprik.value ="0";
	document.PayeeBroker.displayBid.value="";
	document.PayeeBroker.defaultIndicator.value="";

	<% }
	else 
         {
		%>
	
	document.PayeeBroker.payeeName.value="<%=BaseUtil.asString(pyVO.getPayeeName())%>";
	document.PayeeBroker.borBrokerID.value="<%=pyVO.getBorBrokerId() %>";
	document.PayeeBroker.payeeBrokerID.value="<%=pyVO.getPayeeBrokerId() %>";
	document.PayeeBroker.brokerStatus.value="<%=BaseUtil.asString(pyVO.getBrokerStatus()) %>";
	document.PayeeBroker.effectiveDate.value = "<%=BaseUtil.asString(pyVO.getEffectiveDate()) %>";
	document.PayeeBroker.endDate.value = "<%=BaseUtil.asString(pyVO.getEndDate())%>";
	document.PayeeBroker.payeeShare.value = "<%=BaseUtil.asString(pyVO.getPayeeShare()) %>" ;
	document.PayeeBroker.payeeId.value = "<%=pyVO.getIdentifier() %>" ;
	document.PayeeBroker.SortOrder.value="<%=pyVO.getSortOrder()%>" ;
	document.PayeeBroker.recordKey.value ="<%=pyVO.getRecordKey()%>";
	document.PayeeBroker.statusIndicator.value ="<%=BaseUtil.asString(pyVO.getStatusIndicator())%>";
	document.PayeeBroker.pbrik.value ="<%=pyVO.getPbrIk()%>";
	document.PayeeBroker.bprik.value ="<%=pyVO.getBprIk()%>";
	document.PayeeBroker.displayBid.value ="<%=pyVO.getDisplayBid()%>";
	document.PayeeBroker.defaultIndicator.value ="<%=pyVO.getDefaultIndicator()%>";


	<% }
	//}
      %>		
	alert("<%=error %>");

	<%
		session.setAttribute("ERROR", "nothing");
	}
	%>
	document.PayeeBroker.AddList.disabled = true;
}

function popAgain( popList, popValue ) {

	if(popValue == "")
		return false;
	var values = popValue;

	for( var m=0; m < popList.length; m++ ) {
		if ( popList.options[m].selected == true ) {
			listIndex = m;
			break;
		}
	}


	var temp;

	var count = new Array();
	var splitData = new Array();
		
	var j = 0;
	for (var i=0; i < values.length; i++) {
		temp = "" + values.substring(i, i+1);

		if ( temp == (":" ) ) {
			count[j] = i;
			j++;
		}
		
	}
	count[j] = values.length;

	var k = 0;
	for ( i=0; i < count.length; i++ ) {
		splitData[i] = values.substring( k, count[i] );
		k = count[i]+1;
	}

	/*if( splitData[6]=="A" || splitData[6]=="D")
	{
	alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.DoNotModifyHistory")%>");
	}
else {*/
		
	document.PayeeBroker.borBrokerID.value = splitData[0]  ;
	document.PayeeBroker.payeeBrokerID.value = splitData[1]  ;
	document.PayeeBroker.payeeName.value = splitData[2]  ;
	document.PayeeBroker.effectiveDate.value = splitData[3]  ;
	document.PayeeBroker.endDate.value = splitData[4]  ;
	document.PayeeBroker.payeeShare.value = splitData[5]   ;
	document.PayeeBroker.statusIndicator.value = splitData[6]  
	document.PayeeBroker.brokerStatus.value = splitData[7]  ;
	document.PayeeBroker.payeeId.value = splitData[8]   ;
	document.PayeeBroker.SortOrder.value = splitData[9]  ;
	document.PayeeBroker.recordKey.value = splitData[10]  ;
	document.PayeeBroker.pbrik.value =splitData[11];
	document.PayeeBroker.bprik.value =splitData[12];
	document.PayeeBroker.displayBid.value = splitData[13]  ;
	document.PayeeBroker.defaultIndicator.value = splitData[14]  ;
	document.PayeeBroker.isUpd.value="Y";
	disableform();

/*        } */
	 
   }

function resetForm()
{
	document.PayeeBroker.reset();
	document.PayeeBroker.displayBid.value= "" ;
	enableform(); 

}

function disableform()
{
	document.PayeeBroker.displayBid.disabled = true ;
	document.PayeeBroker.payeeBrokerID.disabled = true ;
	document.PayeeBroker.effectiveDate.disabled =true ;
	document.PayeeBroker.endDate.disabled = true ;
	document.PayeeBroker.payeeShare.disabled = true ;

}
function enableEditform(){

if(document.PayeeBroker.isUpd.value =="Y")
	{
	document.PayeeBroker.effectiveDate.disabled =false ;
	document.PayeeBroker.endDate.disabled = false ;
	document.PayeeBroker.payeeShare.disabled = false ;
	}
	else
	{
	enableform();
	}

}


function enableform(){
	document.PayeeBroker.displayBid.disabled = false ;
	document.PayeeBroker.payeeBrokerID.disabled = false ;
	document.PayeeBroker.effectiveDate.disabled =false ;
	document.PayeeBroker.endDate.disabled = false ;
	document.PayeeBroker.payeeShare.disabled = false ;
	document.PayeeBroker.AddList.disabled = false;

}

 


function isCurrentRecordExists(popList,fromWhere)
{
  	var values = "";
      var IndexSelected= -1 ;
      var SelectedIndicator="";
	for( var m=0; m < popList.length; m++ )
     	{
		values = popList.options[m].value;
            for( var k = 0; k < popList.length; k++ )
		{
			 var selectedValue = popList.options[k].text;
			 if (popList.options[k].selected == true )
           		 {
                	      	IndexSelected = k;
			        SelectedIndicator = selectedValue.substring(selectedValue.length - 1,selectedValue.length );
			    
                              if(fromWhere=="Delete")
					{
					      if(SelectedIndicator == "A" )
						{
                                     
							alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.RecordDeletedSaved")%>");
							return true;
						}
						else if(SelectedIndicator == "D")
						{
                                     
							alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.RecordDeleted")%>");
							return true;
						}
					}
                 	 }
		}
	      if(IndexSelected < 0 && fromWhere=="Delete")
		{
				alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.EmptyDelete")%>");
				return true;
		 }

        
		var temp;
		var count = new Array();
		var tokenizedData = new Array();
		var j = 0;
		for (var i=0; i < values.length; i++)
        	{
			temp = "" + values.substring(i, i+1);
			if ( temp == (":" ) )
                	{
				count[j] = i;
				j++;
			}
		
		}
		count[j] = values.length;
		var k = 0;
		for ( i=0; i < count.length; i++ ) 
       	 	{
		    tokenizedData[i] = values.substring( k, count[i] );
		    k = count[i]+1;
	    	}

            	
	}
}





function beforeAdd()
{
        var errorStatus = false;
       	errorStatus =  validate(document.PayeeBroker);
        if ( ! errorStatus )
            return false;
        errorStatus = isCurrentRecordExists( document.PayeeBroker.AddList,"Add" );
        if ( errorStatus )
           return false;
    enableform();
	document.PayeeBroker.payeeBrokerID.disabled = false   
	document.PayeeBroker.SelectedAction.value = 'Add';
	document.PayeeBroker.submit();
}

function beforeSave( )
{
	enableform();
	document.PayeeBroker.payeeBrokerID.disabled = false 
 	document.PayeeBroker.SelectedAction.value = "Save";
 	document.PayeeBroker.submit();
}

function beforeDelete( )
{
	if(document.PayeeBroker.AddList.length ==0)
		return false;
	
	errorStatus = isCurrentRecordExists( document.PayeeBroker.AddList,"Delete" );
       if (  errorStatus )
         return false;
      	enableform();
		document.PayeeBroker.payeeBrokerID.disabled = false   
       	document.PayeeBroker.SelectedAction.value = "Delete";
       	document.PayeeBroker.submit();
}

function selectName()
{
	 var errorStatus = false;
 	 errorStatus =  validateBID(document.PayeeBroker);
      if (  errorStatus )
	  {
		 	 document.PayeeBroker.SelectedAction.value ="BrkName";
			 PayeeBroker.submit();
	  }
}


</SCRIPT>


<TITLE>PUR100 Administer Purchaser (Payee)</TITLE>
</HEAD>
<BODY bgcolor="#999999" OnLoad="init();addListHide()" >
<FORM  name="PayeeBroker" method="POST" action= "PayeeBrokerServlet"  target = "_parent">
<input type="hidden" name="payeeId" value="0">
		        <INPUT type="hidden" name="WhereToGo" value="">
		        <INPUT type="hidden" name="FromWhere" value="0">
			<input type="hidden" name="statusIndicator" value="">
			<input type="hidden" name="SelectedAction" value="">
			<input type="hidden" name="isUpd" value="" >
			<input type="hidden" name="brkName" value="" >
			<input type="hidden" name="recordKey" value="0" >
			<input type="hidden" name="CurrentDate" value="" >
			<input type="hidden" name="pbrik" value="0" >
			<input type="hidden" name="bprik" value="0" >
			<input type="hidden" name="borBrokerID" value="0" >
			<input type="hidden" name="defaultIndicator" value="" >
			<input type="hidden" name="SortOrder" value="-10000" >
<SCRIPT>
function init()
{
	//parent.tops.document.PurTop.dynamic.value = "PUR105 Administer Purchaser ( Payee Broker )";
}
</SCRIPT>
<TABLE width="80%">
  <TBODY>
    <TR>
      <TD>
      <TABLE width="100%" cellpadding="0" cellspacing="0" bgcolor="#999999">
        <TBODY>
          <TR>
            <!-- <TD class="title" bgcolor="#ffcc00"><FONT color="#0033cc">PUR 105 Administer Purchaser(Payee)</FONT></TD> -->
             <!-- <TD class="title" align="right" bgcolor="#ffcc00"><IMG src="/BASEWeb/Purchaser/images/search.gif" width="72" height="22" border="0" alt="Search"><INPUT type="IMAGE" src="/BASEWeb/Purchaser/images/save.gif" name="submitType" value="save" width="50" height="22" border="0" alt="Save" onClick="beforeSave()"><IMG src="/BASEWeb/Purchaser/images/exit.gif" width="50" height="22" border="0" alt="Exit"><IMG src="/BASEWeb/Purchaser/images/print.gif" width="50" height="22" border="0" alt="Print"><IMG src="/BASEWeb/Purchaser/images/comments.gif" width="86" height="22" border="0" alt="Comments"></TD> -->
          </TR>
        </TBODY>
      </TABLE>
      </TD>
    </TR>
  </TBODY>
</TABLE>
<TABLE border="1">
  <TBODY>
    <TR>
      <TD>
      <TABLE width="80%">
        <TBODY>
          <TR>
            <TD bgcolor="#999999">
            <TABLE width="100%" cellpadding="1" cellspacing="1">
              <TBODY>
                <TR>
                  <TD class="label" colspan="2" align="right">Broker Status</TD>
                  <TD><INPUT size="30" type="text" maxlength="30" name="brokerStatus" style="background-color : silver;" onFocus="this.blur()" ></TD>
                  <TD></TD>
                  <TD></TD>
		     	<td></td>
                                    <TD align="right" colspan="3">
		   <IMG src="images/edit.gif" width="50" height="22" border="0" alt="Edit" onclick="enableEditform()"><IMG src="images/reset.gif" width="50" height="22" border="0" alt="Reset" onclick="document.PayeeBroker.reset();"></TD>
                                    <TD></TD>
                </TR>
                <TR>
                  <TD class="label" align="center">BOR Broker ID</TD>
                  <TD class="label" align="center">Payee Broker ID</TD>
                  <TD class="label" align="center" colspan="2">Payee Name</TD>
                  <TD class="label" align="center">Effective Date</TD>
                  <TD class="label" align="center">End Date</TD>
                  <TD class="label">Payee Share</TD>
                                    <TD class="label"></TD>
                                    <TD align="center" width="71"><INPUT size="20" type="button" maxlength="20" name="submitDelete" value="Delete" class="pbttn" onclick="return beforeDelete();"></TD>
                                    <!-- <TD><INPUT type="image" src="images/delete.gif" name="submitDelete"  alt="Delete" onClick="beforeDelete();"></TD> -->
                </TR>
                <TR>
                  <TD align="center" class="label"><SELECT name="displayBid" tabindex="1">
                 	<%
			java.util.Vector borIDVec = new java.util.Vector();
			borIDVec = (java.util.Vector) session.getAttribute("allBorIds");     
			int borIDVecSize =borIDVec.size();
			for( int i=0; i<borIDVecSize; i++ ) {
			borVO = ( org.kp.purchaser.vo.BrokerOfRecordVO) borIDVec.elementAt(i);

	   			 %>
				<OPTION value= "<%=borVO.getBID()+" (" +borVO.getEffectiveDate()+"-"+borVO.getEndDate()+" )" %>" > <%=borVO.getBID()+" (" +borVO.getEffectiveDate()+"-"+borVO.getEndDate()+" )" %></OPTION>

			<%
				}
		       %>			
                  </SELECT></TD>
                  <TD align="center" class="label"><INPUT size="12" type="text" maxlength="12" name="payeeBrokerID" Onchange=" return selectName()" tabindex="2"></TD>
                  <TD align="center" colspan="2" class="label"><INPUT size="40" type="text" maxlength="40" name="payeeName" style="background-color : silver;" onFocus="this.blur()"></TD>
                  <TD align="center" class="label"><INPUT size="10" type="text" maxlength="10" name="effectiveDate" tabindex="3"></TD>
                  <TD><INPUT size="10" type="text" maxlength="10" name="endDate" tabindex="4"></TD>
                  <TD><INPUT size="3" type="text" maxlength="3" name="payeeShare" tabindex="5"></TD>
                                    <TD class = "label">Indicator</TD>
                                    <TD align="center" width="71"><INPUT size="20" type="button" maxlength="20" name="submitAdd" value="  Add  " class="pbttn" onclick=" return beforeAdd()" tabindex="6"></TD>
                                    <!-- <TD><INPUT type = "image" src="images/add.gif" name="submitAdd" value="Add"  alt="Add" onClick=" return beforeAdd()" tabindex="6"></TD> -->
                </TR>
              </TBODY>
            </TABLE>
                        <SELECT size="6" name="AddList" onclick="return popAgain(AddList,this.form.AddList.value)"   style='font-family : "Courier New";' class="input"></SELECT>
 		<BR>
            </TD>
          </TR>
        </TBODY>
      </TABLE>
      </TD>
    </TR>
  </TBODY>
</TABLE>
</FORM>
</BODY>
</HTML>