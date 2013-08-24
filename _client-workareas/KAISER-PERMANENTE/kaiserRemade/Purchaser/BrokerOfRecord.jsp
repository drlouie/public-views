<!-- Sample JSP file --> <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<jsp:useBean id="brokerOfRecordVO"  class="org.kp.purchaser.vo.BrokerOfRecordVO"  scope="session"></jsp:useBean>

<HTML>
<HEAD>
<%@ include file="script/validateBOR.js" %>
<!-- oo <SCRIPT language="JavaScript1.1" src="/BASEWeb/Purchaser/script/validateBOR.js"></SCRIPT> -->
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
 

function addListHide()
 {
	 //disableform();
	 document.BrokerOfRecord.CurrentDate.value = "<%=session.getAttribute("CurrentDate").toString()%>";

	<%
String isName = "Y";
   isName = (String) session.getAttribute("isName");
    if(isName.equals("Y"))
   { 
 String secName = (String)session.getAttribute("brokerName");	
  org.kp.purchaser.vo.BrokerOfRecordVO brokerNameVO  = ( org.kp.purchaser.vo.BrokerOfRecordVO )session.getAttribute("brokerNameVO");	
     
	    %>
enableform();

document.BrokerOfRecord.brokerName.value="<%=brokerNameVO.getBrokerName() %>";
document.BrokerOfRecord.brokerID.value="<%=brokerNameVO.getBID() %>";
document.BrokerOfRecord.brokerStatus.value="<%=brokerNameVO.getBrokerStatus() %>";
	document.BrokerOfRecord.effectiveDate.value = "<%=brokerNameVO.getEffectiveDate() %>";
	document.BrokerOfRecord.endDate.value = "<%=brokerNameVO.getEndDate() %>";
	document.BrokerOfRecord.borLetterRecvdDate.value = "<%=brokerNameVO.getRecvdDate() %>" ;
	document.BrokerOfRecord.borId.value = "<%=brokerNameVO.getIdentifier() %>" ;
	document.BrokerOfRecord.SortOrder.value="<%=brokerNameVO.getSortOrder()%>" ;
	document.BrokerOfRecord.statusIndicator.value ="<%=brokerNameVO.getStatusIndicator()%>";


	<%
     }
    %>
	document.BrokerOfRecord.AddList.style.visibility = "hidden";

	var elementsMaxLength = new Array();
	var elementsText = new Array();
	elementsMaxLength[0] =12;
	elementsMaxLength[1] = 36;
	elementsMaxLength[2] = 10;
	elementsMaxLength[3] = 10; 
	elementsMaxLength[4] = 10;
	elementsMaxLength[5] = 1;

	<%
	java.util.Vector borVec = new java.util.Vector();
	borVec = (java.util.Vector) session.getAttribute("ModifiedBORNew");
	if(borVec==null)
	 borVec = (java.util.Vector) session.getAttribute("ModifiedBOR");
	int vecSize =borVec.size();
		for( int i=vecSize; i > 0; i-- ) {
		brokerOfRecordVO = ( org.kp.purchaser.vo.BrokerOfRecordVO ) borVec.elementAt(i-1);
			int j =1;
     
	    %>

      		document.BrokerOfRecord.AddList.style.visibility = "";
 			elementsText[0] = "<%=brokerOfRecordVO.getBID()%>" ;
			elementsText[1] = "<%=brokerOfRecordVO.getBrokerName() %>";
			elementsText[2] = "<%=brokerOfRecordVO.getEffectiveDate() %>";
			elementsText[3] = "<%=brokerOfRecordVO.getEndDate()%>";	
			elementsText[4] = "<%=brokerOfRecordVO.getRecvdDate()%>";
			elementsText[5] = "<%=brokerOfRecordVO.getStatusIndicator()%>";
			
		 if( elementsText[5] != "A" && elementsText[5] != "D" ) 
		 {
		 	if( IsThisDateRangeCurrent(elementsText[2],elementsText[3] ) )
		 		elementsText[5] = '***';
		 	else if( <%=brokerOfRecordVO.getSortOrder()%> != 0 )
		 		elementsText[5] = "U"; 
		 	else 	 		
		 	   	elementsText[5] = "";
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
		
	 	addoptions.text = elementsText[0] + " " + elementsText[1] + " " + elementsText[2] + " "+ elementsText[3] + " " +elementsText[4] +" "+elementsText[5];  
		addoptions.value =  "<%=brokerOfRecordVO.getBID()%>" + ":" + "<%=brokerOfRecordVO.getBrokerName() %>" + ":" + "<%=brokerOfRecordVO.getEffectiveDate() %>"+ ":"+ "<%=brokerOfRecordVO.getEndDate()%>" + ":" + "<%=brokerOfRecordVO.getRecvdDate()%>"+":"+"<%=brokerOfRecordVO.getStatusIndicator()%>"+ ":" +"<%=brokerOfRecordVO.getBrokerStatus()%>" + ":" + "<%=brokerOfRecordVO.getIdentifier()%>"+":"+"<%=brokerOfRecordVO.getSortOrder()%>";
 

		document.BrokerOfRecord.AddList.options[document.BrokerOfRecord.AddList.options.length] = addoptions;			

		 //oldNo = true;

		<%
		if( i == 0 ) {
		%>

	//document.BrokerOfRecord.brokerID.value = "" ;
	//document.BrokerOfRecord.brokerName.value = "" ;
	//document.BrokerOfRecord.effectiveDate.value = "";
	//document.BrokerOfRecord.endDate.value = "";
	//document.BrokerOfRecord.borLetterRecvdDate.value = "" ;
	//document.BrokerOfRecord.brokerStatus.value = "" ;



		<%
		}
		%>

	//	document.AdministrativeArrgmt.administrativeSystem.focus();

 			
		<%
		}
		%>
	<%

	String error = (String) session.getAttribute("ERROR");

	if ( ! error.equals("nothing") ) {
  	org.kp.purchaser.vo.BrokerOfRecordVO brVO = (org.kp.purchaser.vo.BrokerOfRecordVO) session.getAttribute("borVOError");
	    isName = (String) session.getAttribute("isName");
    			if(isName.equals("E"))
			{
			  %>
	 document.BrokerOfRecord.brokerID.value = "" ;
	 document.BrokerOfRecord.brokerName.value = "" ;
	 document.BrokerOfRecord.effectiveDate.value = "";
	 document.BrokerOfRecord.endDate.value = "";
	 document.BrokerOfRecord.borLetterRecvdDate.value = "" ;
	 document.BrokerOfRecord.brokerStatus.value = "" ;
	 document.BrokerOfRecord.borId.value = 0 ;
	 document.BrokerOfRecord.SortOrder.value="-10000" ;
	 document.BrokerOfRecord.statusIndicator.value ="" ;
	<% }
	else 
         {
		%>
	document.BrokerOfRecord.brokerID.value = "<%=brVO.getBID() %>" ;
	document.BrokerOfRecord.brokerName.value = "<%=brVO.getBrokerName() %>" ;
	document.BrokerOfRecord.effectiveDate.value = "<%=brVO.getEffectiveDate() %>";
	document.BrokerOfRecord.endDate.value = "<%=brVO.getEndDate() %>";
	document.BrokerOfRecord.borLetterRecvdDate.value = "<%=brVO.getRecvdDate() %>" ;
	document.BrokerOfRecord.brokerStatus.value = "<%=brVO.getBrokerStatus() %>" ;
	document.BrokerOfRecord.borId.value = "<%=brVO.getIdentifier() %>" ;
	document.BrokerOfRecord.SortOrder.value="<%=brVO.getSortOrder()%>" ;
	document.BrokerOfRecord.statusIndicator.value ="<%=brVO.getStatusIndicator()%>" ;
	<% }
      %>		
	alert("<%=error %>");

	<%
		session.setAttribute("ERROR", "nothing");
	}
	%>
	document.BrokerOfRecord.AddList.disabled = true;
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

	/*if( splitData[5]=="A" || splitData[5]=="D")
	{
	   alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.DoNotModifyHistory")%>");
	}
else {*/
		
	document.BrokerOfRecord.brokerID.value =splitData[0]  ;
	document.BrokerOfRecord.brokerName.value = splitData[1];
	document.BrokerOfRecord.effectiveDate.value = splitData[2];
	document.BrokerOfRecord.endDate.value = splitData[3];
	document.BrokerOfRecord.borLetterRecvdDate.value = splitData[4];
	document.BrokerOfRecord.statusIndicator.value = splitData[5];
	document.BrokerOfRecord.brokerStatus.value = splitData[6];
	document.BrokerOfRecord.borId.value =  splitData[7];
	document.BrokerOfRecord.SortOrder.value= splitData[8];
	document.BrokerOfRecord.isUpd.value="yes";
	document.BrokerOfRecord.brokerID.disabled = true ;

/*        } */
	 
   }



function disableform()
{
	document.BrokerOfRecord.brokerID.disabled = true ;
	//document.BrokerOfRecord.brokerName.disabled = true ;
	document.BrokerOfRecord.effectiveDate.disabled =true ;
	document.BrokerOfRecord.endDate.disabled = true ;
	document.BrokerOfRecord.borLetterRecvdDate.disabled = true ;
	//document.BrokerOfRecord.brokerStatus.disabled = true;
	 

}

function enableform(){
if(document.BrokerOfRecord.isUpd.value == "yes")
{
document.BrokerOfRecord.brokerID.disabled = true ;
}
else{
document.BrokerOfRecord.brokerID.disabled = false ;

	}


	document.BrokerOfRecord.brokerName.disabled = false ;
	document.BrokerOfRecord.effectiveDate.disabled =false;
	document.BrokerOfRecord.endDate.disabled = false ;
	document.BrokerOfRecord.borLetterRecvdDate.disabled = false ;
	document.BrokerOfRecord.brokerStatus.disabled = false;
	document.BrokerOfRecord.AddList.disabled = false;
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
       	errorStatus =  validate(document.BrokerOfRecord);
        if ( ! errorStatus )
            return false;
        errorStatus = isCurrentRecordExists( document.BrokerOfRecord.AddList,"Add" );
        if ( errorStatus )
           return false;
   		enableform();
 		document.BrokerOfRecord.brokerID.disabled = false;    
   		document.BrokerOfRecord.SelectedAction.value = 'Add';
   		document.BrokerOfRecord.submit();
}

function beforeSave( )
{
	enableform();
	document.BrokerOfRecord.brokerID.disabled = false; 
 	document.BrokerOfRecord.SelectedAction.value = "Save";
 	document.BrokerOfRecord.submit();
}

function beforeDelete( )
{
	if(document.BrokerOfRecord.AddList.length ==0)
		return false;
		
	errorStatus = isCurrentRecordExists( document.BrokerOfRecord.AddList,"Delete" );
    if (  errorStatus )
         return false;
         enableform();
         document.BrokerOfRecord.brokerID.disabled = false; 
       	 document.BrokerOfRecord.SelectedAction.value = "Delete";
       	 document.BrokerOfRecord.submit();
}

function selectName()
{

var errorStatus = false;
errorStatus =  validateBID(document.BrokerOfRecord);
        if (  errorStatus )
	{
 	 document.BrokerOfRecord.SelectedAction.value ="BrkName";
	BrokerOfRecord.submit();
	}
}

function IsThisDateRangeCurrent(EffectiveDate,EndDate)
{
		 var Status = false;
		 var currentdate = document.BrokerOfRecord.CurrentDate.value;
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
</SCRIPT>


<TITLE>PUR100 Administer Purchaser (BrokerOfRecord)</TITLE>
</HEAD>
<BODY bgcolor="#999999" OnLoad="init();addListHide() " >
<FORM  name="BrokerOfRecord" method="POST" action= "BrokerOfRecordServlet" target = "_parent">
<input type="hidden" name="borId" value="0">
                 	<input type="hidden" name="WhereToGo" value="" >
		  	<input type="hidden" name="FromWhere" value="0" >
			<input type="hidden" name="statusIndicator" value="">
			<input type="hidden" name="SelectedAction" value="">
			<input type="hidden" name="isUpd" value="" >
			<input type="hidden" name="brkName" value="" >
			<input type="hidden" name="SortOrder" value="-10000" >
			<input type="hidden" name="CurrentDate" value="" >
<SCRIPT>
function init()
{
	//parent.tops.document.PurTop.dynamic.value = "PUR104 Administer Purchaser ( Broker of Record )";
}
</SCRIPT>
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
                  <TD class="label">Broker Status</TD>
                  <TD><INPUT size="30" type="text" maxlength="30" name="brokerStatus" style="background-color : silver;" onFocus="this.blur()"></TD>
                  <TD></TD>
                  <TD></TD>
                  <TD align="right" colspan="2"></TD>
                                    <TD></TD>
                                    <td><IMG src="images/edit.gif" width="50" height="22" border="0" alt="Edit" onclick="enableform()"><IMG src="images/reset.gif" width="50" height="22" border="0" alt="Reset" onclick="document.BrokerOfRecord.reset();"></td>
             <TD> <!-- <INPUT type="IMAGE" src="/BASEWeb/Purchaser/images/save.gif" name="submitType" value="save" width="50" height="22" border="0" alt="Save" onClick="beforeSave()"> --></TD>
  
		</TR>
                <TR>		
                  <TD class="label" align="center">BOR Broker ID</TD>
                  <TD class="label" align="center" colspan="2">Broker Name</TD>
                  <TD class="label">Effective Date</TD>
                  <TD class="label" align="center">End Date</TD>
                  <TD class="label">BOR Letter Recv'd Date</TD>
                                    <TD class="label"></TD>
                                    <TD align="center" width="71"><INPUT size="20" type="button" maxlength="20" name="submitDelete" value="Delete" class="pbttn" onclick="return beforeDelete();"></TD>
                                   <!-- <TD><INPUT type="image" src="images/delete.gif" name="submitDelete" value="Delete" alt="Delete" onClick="beforeDelete();"></TD> -->
                </TR>
                <TR>
                  <TD align="center" class="label"><INPUT size="12" type="text" maxlength="12" name="brokerID" Onchange=" return selectName()" tabindex="1"></TD>

                  <TD align="center" colspan="2" class="label"><INPUT size="40" type="text" maxlength="40" name="brokerName" style="background-color : silver;" onFocus="this.blur()"></TD>
                  <TD align="center" class="label"><INPUT size="10" type="text" maxlength="10" name="effectiveDate" tabindex="2"></TD>
                  <TD><INPUT size="10" type="text" maxlength="10" name="endDate" tabindex="3"></TD>
                  <TD align="center"><INPUT size="10" type="text" maxlength="10" name="borLetterRecvdDate" tabindex="4"></TD>
                                    <TD class = "label">Indicator</TD>
                                   <!-- <TD><INPUT type = "image" src="images/add.gif" name="submitAdd" value="Add" alt="Add" onClick=" return beforeAdd()" tabindex="5"></TD> -->
                                   <TD align="center" width="71"><INPUT size="20" type="button" maxlength="20" name="submitAdd" value="  Add  " class="pbttn" onclick=" return beforeAdd()" tabindex="5"></TD>
                </TR>
              </TBODY>
            </TABLE>
            		<SELECT size="6" name="AddList" onclick="return popAgain(AddList,this.form.AddList.value)"   style='font-family : "Courier New";'></SELECT>
			</TD>
          </TR>
        </TBODY>
      </TABLE>
      </TD>
    </TR>
  </TBODY>
</TABLE>
<TABLE width="80%">
  <TBODY>
    <TR>
      <TD bgcolor="#999999"></TD>
    </TR>
  </TBODY>
</TABLE>
</FORM>
</BODY>
</HTML>