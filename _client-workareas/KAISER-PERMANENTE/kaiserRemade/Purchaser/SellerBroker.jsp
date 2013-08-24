<!-- Sample JSP file -->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<%@taglib uri="BaseTags" prefix="BT"%>
<jsp:useBean id="sellerVO" class="org.kp.purchaser.vo.SellerVO" scope="session"></jsp:useBean>
<jsp:useBean id="nameVO" class="org.kp.purchaser.vo.BrokerNameVO" scope="session"></jsp:useBean>    
<% String salesDate = "";%>
<% String selectedAction = "";%>
<% String linkToBrokerInquiry = "";%>	
<HTML>
<HEAD>
<!-- <SCRIPT language="JavaScript1.1" src="/BASEWeb/Purchaser/script/validateSellerForm.js"></SCRIPT> -->
<META name="GENERATOR" content="IBM WebSphere Page Designer V3.5.3 for Windows">
<META http-equiv="Content-Style-Type" content="text/css">
<STYLE>
<!--
.label {
	COLOR: #0033FF;
	font-family: arial, verdana, sans-serif;
	font-size: 13px;
	font-weight: bold;
	font-style: normal;
}

.title {
	COLOR: #FF0000;
	font-family: arial, verdana, sans-serif;
	font-size: 14px;
	font-weight: bold;
	font-style: normal;
}

IMG {
	color: olive;
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

var listLength = 0;
var editMode = '';
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

	}
}
function populateList()
{

	var elementsMaxLength = new Array();
	var elementsText = new Array();	
	elementsMaxLength[0] = 12;
	elementsMaxLength[1] = 40; 
	elementsMaxLength[2] = 1;	
<%
	
	java.util.Vector sellers = (java.util.Vector) session.getAttribute("ModifiedSellers");	
	for( int i=sellers.size()-1; i>=0; i-- ) 
	{
		sellerVO = ( org.kp.purchaser.vo.SellerVO ) sellers.elementAt(i);
%>
	   
			elementsText[0] = "<%=sellerVO.getBrokerId() %>";
			elementsText[1] = "<%=sellerVO.getBrokerName()%>";			
			elementsText[2] = "<%=sellerVO.getStatusIndicator()%>";
			if(elementsText[2] == "C")
				elementsText[2] = " ";
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
		addoptions.text = " "+elementsText[0] + " " + elementsText[1] + " " + elementsText[2];  
		addoptions.value = "<%=sellerVO.getBrokerId() %>" + ":" + "<%=sellerVO.getBrokerName()%>"+":"+"<%=sellerVO.getStatusIndicator()%>"+ ":" + "<%=sellerVO.getIdentifier()%>";
		document.SellerBroker.SellerList.options[document.SellerBroker.SellerList.options.length] = addoptions;			
<%
	}
%>

		listLength = document.SellerBroker.SellerList.options.length;		
		if(listLength == 0 )		
		 	document.SellerBroker.SellerList.style.visibility = "hidden";
		 else
		 	document.SellerBroker.SellerList.style.visibility = "";
		 	
}//End of populateList()
function populateBrokerName()
{
	<%	
		nameVO  = ( org.kp.purchaser.vo.BrokerNameVO )session.getAttribute("BrokerNameVO");	
		
		if(nameVO != null)
		{		
	%>		
		document.SellerBroker.sellerBrokerID.value ="<%= nameVO.getBrokerID() %>";
		document.SellerBroker.sellerBrokerName.value="<%= nameVO.getBrokerName() %>";			
	<%		
		}
	%>
}
function populateForEdit( popList, popValue ) 
{
	if(popValue == "")
		return false;
	
	for( var m=0; m < popList.length; m++ ) {
		if ( popList.options[m].selected == true ) {
			document.SellerBroker.selectedIndex.value = m;
			break;
		}
	}	
	
	var temp;
	var count = new Array();
	var splitData = new Array();	
	var j = 0;
	for (var i=0; i < popValue.length; i++) 
	{		
		temp = "" + popValue.substring(i, i+1);

		if ( temp == (":" ) ) 
		{
			count[j] = i;
			j++;
		}
		
	}
	count[j] = popValue.length;

	var k = 0;
	for ( i=0; i < count.length; i++ ) {
		splitData[i] = popValue.substring( k, count[i] );
		k = count[i]+1;
	}

	/*if(splitData[2]=="A" || splitData[2]=="D")
		{
			alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.DoNotModifyHistory")%>");
			document.SellerBroker.sellerBrokerID.value = "";
			document.SellerBroker.sellerBrokerName.value = "";
			document.SellerBroker.sellerBrokerID.disabled = false;			
			return false;
		}
	else 
	{	*/	
		document.SellerBroker.sellerBrokerID.disabled = true;
		document.SellerBroker.sellerBrokerID.value = splitData[0];
		document.SellerBroker.sellerBrokerName.value = splitData[1];		
		document.SellerBroker.statusIndicator.value = splitData[2];		
		document.SellerBroker.sellerID.value =  splitData[3];
		//document.SellerBroker.selectedIndex.value= listIndex;
		document.SellerBroker.salesDate.value= document.SellerBroker.sellerSalesDate.value		
	/* }*/
	 
   
}//End of populateForEdit
function isSelectedRecordDeletedAlready(popList)
{
  	
      var IndexSelected= -1;      
	  for( var k = 0; k < popList.length; k++ )
		{
		 	if (popList.options[k].selected == true )
           		 {
               	      	IndexSelected = k;
                  	    if(IndexSelected < 0 && fromWhere=="Delete")
							{
								alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.EmptyDelete")%>");
								return true;
		 					}
			      
				}
	  }
    	
}//End of isSelectedRecordDeletedAlready

function disableForm()
{
	document.SellerBroker.sellerSalesDate.disabled = true ;
	document.SellerBroker.sellerBrokerID.disabled = true ;	
	if(listLength > 0)
		document.SellerBroker.SellerList.disabled =true ;	
}

function enableForm()
{	

	document.SellerBroker.sellerSalesDate.disabled = false ;
	document.SellerBroker.sellerBrokerName.disabled =false ;
	document.SellerBroker.sellerBrokerID.disabled =false ;	
	if(listLength > 0)
		document.SellerBroker.SellerList.disabled =false ;
}
function makeFormEditable()
{

	document.SellerBroker.sellerSalesDate.disabled = false;	
	if(listLength > 0 )	
		{	
			document.SellerBroker.sellerBrokerID.disabled = false;		
			document.SellerBroker.SellerList.disabled = false ;
		}
	else 
		{
			document.SellerBroker.sellerBrokerID.disabled = false;
		}
	
	editMode = true;
	return false;
}

function makeNonEditableIfValueExits(bid)
{
	
	if(bid != null)
		{
			document.SellerBroker.sellerBrokerID.disabled = false;					
		}
	else
		{
			document.SellerBroker.sellerBrokerID.disabled = true;			
		}
	
}
function selectName()
{	
	if(!checkSellerBrokerID())
		return false;
	if(document.SellerBroker.sellerBrokerID.value == "" )
		{
			alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.seller.BrokerIdRequred")%>");
			return false;
		}
 	document.SellerBroker.SelectedAction.value  ="BkrName"; 	
	document.SellerBroker.submit();	
}
function beforeAdd()
{	
	if(!editMode)
		{
			//alert("You are in Non Editable Mode.");
			return false;
		}
	if(document.SellerBroker.sellerBrokerID.value == "" || document.SellerBroker.sellerBrokerName.value == "")
		{
			alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.seller.BrokerIdRequred")%>");
			return false;
		}
	else if(document.SellerBroker.sellerSalesDate.value == "")
		{
			alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.seller.SalesDateRequired")%>");
			return false;
		}
	enableForm();
	document.SellerBroker.SelectedAction.value = 'Add';
	document.SellerBroker.submit();	
}
function beforeDelete()
{
	if(!editMode)
		{
			//alert("You are in Non Editable Mode.");
			return false;
		}
	if(isCurrentRecordExists(document.SellerBroker.SellerList,"Delete")	)
		return false;
	if(document.SellerBroker.sellerBrokerID.value == "" )
		{
			alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.EmptyDelete")%>");
			return false;
		}
	if(document.SellerBroker.selectedIndex.value =="")
		{
			alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.EmptyDelete")%>");
			return false;
		}
	enableForm();
	//isSelectedRecordDeletedAlready( document.SellerBroker.SellerList); 
	document.SellerBroker.SelectedAction.value = 'Delete';
	document.SellerBroker.submit();	

}
function beforeSave( )
{
	enableForm();
   document.SellerBroker.SelectedAction.value = "Save";
   document.SellerBroker.submit();
}
function resetForm()
{
	document.SellerBroker.sellerBrokerID.disabled = false;	
	document.SellerBroker.reset();
	return false;
}
function checkSellerBrokerID() 
{	
	var value = document.SellerBroker.sellerBrokerID.value;		
	if(value == "")
		{
			alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.seller.BrokerIdRequred")%>");
			return false;
		}	
		var valid = "1234567890"; 
  		if(valid.length > 1) {
			 for (var i=0; i < value.length; i++) 
			 {
				temp = "" + value.substring(i, i+1);
				if (valid.indexOf(temp) == "-1") 
				{
			      	alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.seller.InvalidBrokerId")%>");			      	
			      	return false;			      
				}				
			}			
		}	
	return true;
}//end of checkSellerBrokerID
</SCRIPT>

<TITLE>PUR103 Administer Purchaser ( Seller Broker )</TITLE>
</HEAD>
<BODY bgcolor="#999999" OnLoad="init()">
<FORM name="SellerBroker" method="POST" action="SellerBrokerServlet" target = "_parent">

<INPUT type="hidden" name="salesDate" value="0"> 
<INPUT type="hidden" name="brokerID" value="0"> 
<INPUT type="hidden" name="brokerName" value="0"> 
<INPUT type="hidden" name="statusIndicator" value=""> 
<INPUT type="hidden" name="sellerID" value="0"> 
<INPUT type="hidden" name="selectedIndex" value=""> 
<INPUT type="hidden" name="SelectedAction" value=""> 
<INPUT type="hidden" name="WhereToGo" value=""> 
<INPUT type="hidden" name="FromWhere" value="0"> 
<INPUT type="hidden" name="SortOrder" value="0">

<SCRIPT>
function init()
{	
	//parent.tops.document.PurTop.dynamic.value = "PUR103 Administer Purchaser ( Seller Broker )";
	editMode = true;
	<%
		salesDate = (String)session.getAttribute("SalesDate");
	 	selectedAction = (String)session.getAttribute("SelectedAction");
	 	String bkrNameFound = (String)session.getAttribute("BrokerNameFound"); 	 
	 	//String salesDateWithInRange = (String)session.getAttribute("SalesDateWithInRange");
	 	if(selectedAction != null)
	 	{
	 	if(selectedAction.equals("BkrName"))
	 	{
	 		if(bkrNameFound.equals("Yes"))
	 		{
	 		linkToBrokerInquiry = "";
	%>			
	 		populateBrokerName();
	 <%
	 		}
	 		else if(bkrNameFound.equals("No"))
	 		{
	 			linkToBrokerInquiry = "<A href = '../BrokerInquiryFrame.htm' target='_parent'>Click here</A> to Setup a Broker";
	 		}
	 %> 		
	 		populateList();	 		
	<%
		}
	 	else if(selectedAction.equals("Add"))
	 	{	
	 %>		
	 		populateList();	
				
	<%
		}
		else if(selectedAction.equals("Delete"))	
		{
	%>
			populateList();
	<%
		}	
		else if(selectedAction.equals("Save"))
		{
	%>
			editMode = false;
			populateList();
			disableForm();
	<%
		}
		}
		else if(selectedAction == null)
		{
	%>
		editMode = false;
		populateList();
		disableForm();
	<%
		}
	%>
<BT:BaseErrorAlert />
}
</SCRIPT>


<TABLE border="1" width = "80%">
    <TBODY>
        <TR>
            <TD>
            <TABLE width="100%">
                <TBODY>
                    <TR>
                        <TD bgcolor="#999999" class ="title"><B><%= linkToBrokerInquiry%></B></TD>
                    </TR>
                    <TR>
                        <TD bgcolor="#999999">
                        <TABLE width="100%" cellpadding="1" cellspacing="1">
                            <TBODY>
                                <TR>
                                    <TD class="label" width="77" colspan="2">Sales Date</TD>
                                    <TD rowspan="2"></TD>
                                    <TD rowspan="2"></TD>
                                    <TD align="right" rowspan="2"><INPUT type = "image" src="images/edit.gif" name = "Edit" alt="Edit" onclick="return makeFormEditable()" tabindex="6"><INPUT type = "image" src="images/reset.gif"  name = "Reset"  alt="Reset" onclick="return resetForm()" tabindex="7"></TD>
                                </TR>
                                <TR>
                                    <TD class="label" width="77"><INPUT size="10" type="text" maxlength="10" name="sellerSalesDate" tabindex="1" value="<%= salesDate%>"></TD>
                                    <TD width="182"></TD>
                                </TR>
                            </TBODY>
                        </TABLE>
                        <TABLE width="80%">
                            <TBODY>
                                <TR>
                                    <TD class="label" align="center"><nobr>Seller Broker ID</nobr></TD>
                                    <TD align="center" class="label">Seller Broker Name</TD>
                                    <TD width="101"></TD>
                                    <TD align="center" width="71"><INPUT size="20" type="button" maxlength="20" name="submitDelete" value="Delete" class="pbttn" onclick="return beforeDelete();"></TD>
                                    <!-- <TD width="38"><INPUT type="image" src="images/delete.gif" name="submitDelete" value="Delete" alt="Delete" onclick=" return beforeDelete();" tabindex="5"></TD> -->
                                </TR>
                                <TR>
                                    <TD><INPUT size="12" type="text" maxlength="12" name="sellerBrokerID" tabindex="2" onclick = "makeNonEditableIfValueExits(this.value)"></TD>
                                    <TD align="center"><INPUT size="40" type="text" maxlength="45" name="sellerBrokerName" style="background-color: silver" onfocus="return selectName()" readonly tabindex="3"></TD>
                                    <TD class="label" width="101" align="center">Indicator</TD>
                                    <TD align="center" width="71"><INPUT size="20" type="button" maxlength="20" name="Add" value="  Add  " class="pbttn" onclick=" return beforeAdd()" tabindex="4"></TD>
                                    <!-- <TD width="38"><INPUT type="image" src="images/add.gif" name="submitAdd" value="Add"  alt="Add" onclick="return beforeAdd();" tabindex="4"></TD> -->
                                </TR>
                            </TBODY>
                        </TABLE>
                      
                        <SELECT size="6" name="SellerList" onclick="return populateForEdit(SellerList,this.form.SellerList.value)" style='font-family : "Courier New";' tabindex="8"></SELECT> <BR>                        
                        
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
