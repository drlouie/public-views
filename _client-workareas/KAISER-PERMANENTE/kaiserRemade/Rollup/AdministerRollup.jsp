<!-- Sample JSP file -->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML>
<jsp:useBean id="rollUpVO" class="org.kp.base.rollup.vo.RollUpVO" />
<%
	java.util.Vector  rollupV = new java.util.Vector();
    rollupV = (java.util.Vector)session.getAttribute("ModifiedAdministerRollup");

%>
<HEAD>
<META name="GENERATOR" content="IBM WebSphere Page Designer V3.5.3 for Windows">
<META http-equiv="Content-Style-Type" content="text/css">
<TITLE>Administer Rollup</TITLE>
<STYLE>
<!--
.label {
	COLOR : #0033FF; 
	font-family: arial,verdana,sans-serif;
	font-size : 12px;
	font-weight : bold;
	font-style: normal;	
	}
.input {
	COLOR : #000000; 
	font-family: verdana, arial, sans-serif;
	font-size : 12px;
	font-weight : normal;
	font-style: normal;	
	}
.caption {
	COLOR : #003333; 
	font-family: verdana, arial, sans-serif;
	font-size : 11px;
	font-weight : bold;
	font-style: normal;	
	}
.submit {
	COLOR : #0000; 
	font-family: verdana, arial, sans-serif;
	font-size : 12px;
	font-weight : bold;
	font-style: normal;	
	}


.title {
	COLOR : #cc3333; 
	font-family: arial,verdana,sans-serif;
	font-size : 11px;
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
<Script src="/BASEWeb/script/PrintScript.js">
</Script>
<Script language="JavaScript">
var CmsnSched = new Array();
var ProdCat   = new Array();
var CmsnStatus = new Array();
var ProdName   = new Array();
function validateForm(name,value)
{
	var RollupName = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";
	var RollupNumber  = "1234567890";
	var valid = "";
	var temp = "";
	
	if(name == "RollupNumber")
		valid = RollupNumber;
	if(name == "RollupName")
		valid = RollupName;
		

	if(valid.length > 1)
	{
 		for (var i=0; i < value.length; i++) 
  		{
   			temp = "" + value.substring(i, i+1);
   			if (valid.indexOf(temp) == "-1") 
     		{
     			alert("<%= org.kp.base.web.util.MessageUtil.getInstance().getText("rollup.invalidChars")%>"+name);
       			return true;
     		}
  		}
 	}
 	return false;	
}
function isSelectionRight(popList,fromWhere)
{
  	  var values = "";
      var IndexSelected= -1 ;
      var SelectedIndicator="";


        for( var k = 0; k < popList.length; k++ )
		{
                   var selectedValue = popList.options[k].text;
			 if (popList.options[k].selected == true )
           	 {
                	IndexSelected = k;
                    SelectedIndicator = document.AdministerRollupForm.Indicator.value;//selectedValue.substring(selectedValue.length - 1,selectedValue.length );
                    if(SelectedIndicator == "C")
                    {
                    	alert("<%= org.kp.base.web.util.MessageUtil.getInstance().getText("rollup.cantDelete")%>");
                    	return true;
                   	}
                    if(fromWhere=="Delete")
					{
					      if(SelectedIndicator == "A" )
						{
         					alert("<%= org.kp.base.web.util.MessageUtil.getInstance().getText("rollup.alreadyArchived")%>");
							return true;
						}
						else if(SelectedIndicator == "D")
						{
         					alert("<%= org.kp.base.web.util.MessageUtil.getInstance().getText("rollup.alreadyDeleted")%>");
							return true;
						}
					}
              }
		}
	      if(IndexSelected < 0 && fromWhere=="Delete")
		{
				alert("<%= org.kp.base.web.util.MessageUtil.getInstance().getText("rollup.selectAnyThingToDelete")%>");
				return true;
		 }
      

}
function checkDateValidation(datename, datevalue){
  	
	mainCheckDateValidation :
	if( datename != "")
	{
	    var errorStatus = false;
        var errorFields = '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.ErrorMessagePrefix")%>';
	 	var validdate = "1234567890/";
         	var err=0;
         	var psj=0;
	      var a="";

         	a=datevalue;
		
		
	 	if (a.length != 10) {
			errorFields += "\n" +  '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Invalid")%>'+datename;
			errorStatus = true;
			break mainCheckDateValidation;
		}
		else {
			for (var i=0; i < a.length; i++) {
			temp = "" + a.substring(i, i+1);
				if (validdate.indexOf(temp) == "-1") {
					errorFields += "\n" +  '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+datename;
					errorStatus = true;
					break mainCheckDateValidation;
				}
			}
		 }

   	       d = a.substring(0, 2);
      	 c = a.substring(2, 3);
         	 b = a.substring(3, 5);
         	 e = a.substring(5, 6);
         	 f = a.substring(6, 10);

 	       //basic error checking

      	 if (d<1 || d>12) {
			errorFields += "\n" + datename + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidMonth")%>';
			errorStatus = true;
			break mainCheckDateValidation;
		 }
         	 if (c != '/' || e != '/' ) {
			errorFields += "\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Invalid")%>'+datename;
			errorStatus = true;
			break mainCheckDateValidation;
		 }
         	 if (b<1 || b>31) {
			errorFields += "\n" + datename + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidDate")%>';
			errorStatus = true;
			break mainCheckDateValidation;
		 }
       
         
         
         	 if (f<1900 || f>4000) {
			errorFields += "\n" + datename +  '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidYear")%>';
			errorStatus = true;
			break mainCheckDateValidation;
		 }



         	 // months with 30 days
         	 if (d==4 || d==6 || d==9 || d==11){
             	if (b==31) {
				errorFields += "\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.30DaysInAMonth")%>'+datename;
				errorStatus = true;
				break mainCheckDateValidation;
			}
         	 }


	      // february, leap year
         	 if (d==2){
              	// feb
              	var g=parseInt(f/4)
              	if (isNaN(g)) {
				errorFields += "\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.MonthForLeapYear")%>'+datename;
				errorStatus = true;
				break mainCheckDateValidation;
	            }

             	if (b>29) {
				errorFields += "\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.MonthDateNoMatch")%>'+datename;
				errorStatus = true;
				break mainCheckDateValidation;
		 	}

             	if (b==29 && ((f/4)!=parseInt(f/4))) {
				errorFields += "\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Invalid")%>'+datename;
				errorStatus = true;
				break mainCheckDateValidation;
	       	}
		 }
		
		}

endOfCheckDateValidation :		
		 if ( errorStatus )
        	alert( errorFields );
    	return errorStatus; 

	} // end of checkValidation()
function init()
{	
        document.AdministerRollupForm.CurrentDate.value = "<%=session.getAttribute("CurrentDate").toString()%>";
    <% 
			String errorMsg = (String) session.getAttribute("errorMsg"); 
 			if(!errorMsg.equals("Empty") ) 
 			{ 
 				rollUpVO = (org.kp.base.rollup.vo.RollUpVO)session.getAttribute("MaintainOldValuesVO");
 				%>
 			    document.AdministerRollupForm.EffectiveDate.value = '<%=rollUpVO.getEffectiveDate()%>';
 			    document.AdministerRollupForm.EndDate.value       = '<%=rollUpVO.getEndDate()%>';
 			    //GetDropDown();
 			    var nameOptions = new Option();
				document.AdministerRollupForm.RollupNumber.value = '<%=rollUpVO.getRollupNumber()%>';
				if(<%=rollUpVO.getRollupIK()%> != 0 )
					document.AdministerRollupForm.RollupNumber.disabled = true;
				document.AdministerRollupForm.RollupName.value = '<%=rollUpVO.getRollupName()%>';
 			    document.AdministerRollupForm.Indicator.value = '<%=rollUpVO.getIndicator()%>';
 			    document.AdministerRollupForm.SortOrder.value = '<%=rollUpVO.getSortOrder()%>';
 			    document.AdministerRollupForm.RollupIK.value = '<%=rollUpVO.getRollupIK()%>';
  			  	alert("<%=errorMsg%>");
    			<% 
    	    } %>
  
          rollupDisplay();
          DisableForm();
}
function rollupDisplay()
{
    var affectedRecord = 0;
	document.AdministerRollupForm.ARList.style.visibility = "hidden";
	
<% 
	int  recordPosition = 0; 
	for( int i=rollupV.size(); i > 0; i-- ) 
    {
        recordPosition = recordPosition+1;
 		rollUpVO = ( org.kp.base.rollup.vo.RollUpVO )rollupV.elementAt(i-1);
 %>
    	var elementsMaxLength = new Array();
		var elementsText = new Array();
		var elementsValue = new Array();
		elementsText[0] = "<%=rollUpVO.getRollupNumber()%>";
		elementsText[1] = "<%=rollUpVO.getRollupName()%>";
		elementsText[2] = "<%=rollUpVO.getEffectiveDate()%>";
		elementsText[3] = "<%=rollUpVO.getEndDate()%>";
		elementsText[4] = "<%=rollUpVO.getIndicator()%>";
		
		
		
		if( elementsText[4] != "A" && elementsText[4] != "D" ) 
		 {
		 	if( <%=rollUpVO.getSortOrder()%> <  0 || <%=rollUpVO.getSortOrder()%> > 0 )
		 		elementsText[4] = 'U';
		 	else if( IsThisDateRangeCurrent(elementsText[2],elementsText[3] ) )
		 		elementsText[4] = '***';
		 	else 		 		
		 	   	elementsText[4] = "";
         }   	
		
		elementsMaxLength[0] = 28;
		elementsMaxLength[1] = 40;
		elementsMaxLength[2] = 20;
		elementsMaxLength[3] = 25; 
		elementsMaxLength[4] = 1;
		
		
		

		for(var i = 0 ; i < elementsMaxLength.length; i++)
		{	
						
			if(elementsText[i].length < elementsMaxLength[i])
			{	
					for(var j = elementsText[i].length ; j < elementsMaxLength[i]; j++)
					{		
							elementsText[i]+= " ";							
					}
					
				}
			else
				elementsText[i] = elementsText[i].substring(0,elementsMaxLength[i]);
		}

	    document.AdministerRollupForm.ARList.style.visibility = "";
		var addoptions = new Option();
		addoptions.text = elementsText[0]+ " " +elementsText[1]+ " " +elementsText[2]+ " " +elementsText[3]+" "+elementsText[4];
		addoptions.value ="<%=rollUpVO.getRollupNumber()%>"+ "," +"<%=rollUpVO.getRollupName()%>"+ "," +"<%=rollUpVO.getEffectiveDate()%>"+ ","+"<%=rollUpVO.getEndDate()%>"+","+"<%=rollUpVO.getIndicator()%>"+","+"<%=rollUpVO.getRollupIK()%>"+","+"<%=rollUpVO.getSortOrder()%>";
		document.AdministerRollupForm.ARList.options[document.AdministerRollupForm.ARList.options.length] = addoptions;
<%    	String error = (String) session.getAttribute("errorMsg"); 
 			if(!error.equals("Empty") ) 
 			{ 
 				String EditedSortOrder = (String) session.getAttribute("EditedSortOrder");
 				String EditedIK        = (String) session.getAttribute("EditedIK");
 			%>
 				affectedSortOrder = "<%=rollUpVO.getSortOrder()%>";
 				affectedEppIK     = "<%=rollUpVO.getRollupIK()%>";
 				if( ( affectedSortOrder == '<%=EditedSortOrder%>') &&
 					( affectedEppIK    == '<%=EditedIK%>') )
 				{
 					  affectedRecord = '<%=recordPosition%>';
 				}
<% 			}
	
	} 
	 session.setAttribute("errorMsg","Empty"); %>
	if(affectedRecord != "")	
		document.AdministerRollupForm.ARList.options[affectedRecord-1].selected = true;				
}

function popIntoFields( popList, popValue ) 
{

	var values = popValue;
	for( var m=0; m < popList.length; m++ )
    {
		if( popList.options[m].selected == true )
        {
			listIndex = m;
			break;
		}
	}


	var temp;
	var count = new Array();
	var tokenizedData = new Array();
	var j = 0;
	for (var i=0; i < values.length; i++)
    {
		temp = "" + values.substring(i, i+1);
		if ( temp == ("," ) )
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
   /* if(tokenizedData[6] == "H")
	{		
		alert("<%= org.kp.base.web.util.MessageUtil.getInstance().getText("rollup.noModifyOnHistory")%>");
		return false;
	} */
	
	document.AdministerRollupForm.RollupNumber.value = tokenizedData[0];
	if(tokenizedData[5] != 0 )
		document.AdministerRollupForm.RollupNumber.disabled = true;
	else
		document.AdministerRollupForm.RollupNumber.disabled = false;
		
	document.AdministerRollupForm.RollupName.value = tokenizedData[1];
	document.AdministerRollupForm.EffectiveDate.value = tokenizedData[2];
	document.AdministerRollupForm.EndDate.value = tokenizedData[3];
	document.AdministerRollupForm.Indicator.value =  tokenizedData[4];
	document.AdministerRollupForm.RollupIK.value =  tokenizedData[5];
    document.AdministerRollupForm.SortOrder.value = tokenizedData[6];
	document.AdministerRollupForm.FromListBox.value = "Yes";
 
} 
function BeforeAdd()
{
    var errorStatus = false;
    errorStatus = checkDateValidation("EffectiveDate",document.AdministerRollupForm.EffectiveDate.value);
    if(errorStatus)
    	return false;
    if(document.AdministerRollupForm.RollupName.value != "")
    {
    	errorStatus = validateForm("RollupName",document.AdministerRollupForm.RollupName.value);
    	if(errorStatus)
    		return false;
    }
    else
    {
    	alert("<%= org.kp.base.web.util.MessageUtil.getInstance().getText("rollup.enterName")%>");
    	return false;
    }
    if(document.AdministerRollupForm.EndDate.value != "")	
	    errorStatus = checkDateValidation("EndDate",document.AdministerRollupForm.EndDate.value);
	if(errorStatus)
		return false;
		
	if(document.AdministerRollupForm.RollupNumber.value == "")
	{
		alert("<%= org.kp.base.web.util.MessageUtil.getInstance().getText("rollup.enterRollupNo")%>");
		return false;
	}
    else
    {
    	errorStatus = validateForm("RollupNumber",document.AdministerRollupForm.RollupNumber.value)
    	if(errorStatus)
    		return false;
    }
    	EnableForm();
    document.AdministerRollupForm.SelectedAction.value = "Add";
	document.AdministerRollupForm.submit();
}
function BeforeDelete()
{
	var errorStatus = false;
	errorStatus = isSelectionRight(document.AdministerRollupForm.ARList,"Delete");
	if(errorStatus)
		return false;
	EnableForm();	
  	document.AdministerRollupForm.SelectedAction.value = "Delete";
	document.AdministerRollupForm.submit();
}
function BeforeSave()
{
	EnableForm();
	document.AdministerRollupForm.SelectedAction.value = "Save";
	document.AdministerRollupForm.submit();
}
function EnableForm()
{
	document.AdministerRollupForm.RollupNumber.disabled = false;

}
function DisableForm()
{
	document.AdministerRollupForm.ARList.disabled = true;
}
function AllowEditing()
{
    if(document.AdministerRollupForm.RollupNumber.value == "")
    	document.AdministerRollupForm.RollupNumber.disabled = false;
	document.AdministerRollupForm.ARList.disabled = false;
	
}
function IsThisDateRangeCurrent(EffectiveDate,EndDate)
{
		 var Status = false;
		 var currentdate = document.AdministerRollupForm.CurrentDate.value;
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
function callComments() 
{ 
	var functionType = 'RLSHP';	

   	var sourceId1 = document.AdministerRollupForm.RollupNumber.value;
	var sourceId2 = '0';
	var sourceId3 = '0';
	if(sourceId1 == '')
	{
		alert("No Rollup Number found to add a comments..");
		return false;
	}	 	
	var url = '../Comments/CommentServlet?sourceId1='+sourceId1+'&sourceId2='+sourceId2+'&sourceId3='+sourceId3+'&sourceInd=ROL&funType='+functionType;	
	window.open(url, 'slideWindow',false,500,700);
	
   }
</Script>
</HEAD>
<BODY bgcolor="#999999" text="#000000" OnLoad="init();">
<FORM name="AdministerRollupForm" action="AdministerRollupServlet" method="POST">
 <input type="hidden" name="SelectedAction" value="" >
            <input type="hidden" name="RollupIK" value="0" >
            <input type="hidden" name="Indicator" value="" >
			<input type="hidden" name="sourceId1" value="0" >
			<input type="hidden" name="sourceId2" value="0" >
			<input type="hidden" name="sourceId3" value="0" >
			<input type="hidden" name="sourceInd" value="EU" >
            <input type="hidden" name="SortOrder" value="0" >
            <input type="hidden" name="WhereToGo" value="" >
		  	<input type="hidden" name="FromWhere" value="0" >
            <input type="hidden" name="message" value="" >
            <input type="hidden" name="CurrentDate" value="" >
            <input type="hidden" name="FromListBox" value="No" >
<TABLE width="100%" cellpadding="0" cellspacing="0">
    <TBODY>
    <TR>
      <TD bgcolor="#ffcc00"><INPUT type="button" name="dynamic" value="ROL100-Administer Rollup - Page 1" class = "button"></TD>
      <TD class="title" align="right" bgcolor="#ffcc00"><A href="/BASEWeb/Purchaser/index.jsp" target="_parent"><IMG src="/BASEWeb/Purchaser/images/search.gif" width="68" height="22" border="0" alt="Search" ></A><IMG  src="/BASEWeb/Purchaser/images/save.gif" width="50" height="22" border="0" alt="Save" onclick="return BeforeSave()"><A href="/BASEWeb/BaseMainMenu.htm"  target="_parent"><IMG src="/BASEWeb/Purchaser/images/exit.gif" width="50" height="22" border="0" alt="Exit"></a><IMG src="/BASEWeb/Purchaser/images/print.gif" width="50" height="22" border="0" alt = "Print" onClick="callPrint();"><IMG src="/BASEWeb/Purchaser/images/comments.gif" width="86" height="22" border="0" alt = "Comments" onclick = "callComments()"></TD>    
      </TR>
  </TBODY>
</TABLE>
<TABLE border="1" width="100%">
  <TBODY>
    <TR>
            <TD valign="top" nowrap width="851" height="217">
            <TABLE border="0" width="901">
        <TBODY>
          <TR>
            <!--<TD valign="top" align="right" width="639"><IMG src="/BASEWeb/Rollup/images/print.gif" width="50" height="22" border="0" onClick='CallPrint()'></TD> -->
            <!-- <TD valign="top" align="right" width="639"><IMG src="/BASEWeb/Rollup/images/save.gif" width="50" height="22" border="0" onclick="return BeforeSave()">-->
                        <TD rowspan="2"></TD>
                        <TD width="474" align="right"><A href="AdministerRollupRelationshipsServlet" target="_parent"><FONT size="3" face="Times New Roman">&gt;&gt;Rollup Page 2</FONT></A></TD>
                    </TR>
                    <TR>
                        <TD width="474" align="right"><IMG src="/BASEWeb/Rollup/images/edit.gif" onclick="return AllowEditing()" width="50" height="22" border="0"><IMG src="/BASEWeb/Rollup/images/reset.gif" onclick=" document.AdministerRollupForm.reset();" width="50" height="22" border="0"><BR>
                        </TD>
                    </TR>
                </TBODY>
      </TABLE>
            <TABLE border="0" width="765">
        <TBODY>
          <TR>
                        <TD valign="middle" align="center" class="label" width="120">Rollup Number</TD>
                        <TD valign="middle" align="center" class="label" width="68"></TD>
                        <TD valign="middle" align="center" class="label" width="293">Rollup Name</TD>
                        <TD valign="middle" align="center" class="label" width="131">Effective Date</TD>
                        <TD valign="middle" align="center" class="label" width="91">End Date</TD>
                        <TD align="center" width="71"><INPUT size="20" type="button" maxlength="20" name="Delete" value="Delete" class="pbttn" onclick="return BeforeDelete();"></TD>
                        <!-- <TD valign="middle" align="right" colspan="3"><IMG src="/BASEWeb/Rollup/images/delete.gif" width="58" height="22" border="0" onclick="return BeforeDelete()"></TD> -->
                    </TR>
          <TR>
                        <TD><INPUT class="input" size="15" type="text" name="RollupNumber" maxlength="15"></TD>
                        <TD class = "label">XXXXXXX</TD>
                        <TD><INPUT class="input" size="43" type="text" name="RollupName"></TD>
                        <TD><INPUT class="input" size="13" type="text" maxlength="10" name="EffectiveDate" ></TD>
                        <TD><INPUT class="input" size="11" type="text" maxlength="10" name="EndDate" ></TD>
                        <TD class = "label">Indicator</TD>
                        <TD align="center" width="71"><INPUT size="20" type="button" maxlength="20" name="Add" value="  Add  " class="pbttn" onclick=" return BeforeAdd()"></TD>
                        <!-- <TD align="right"><IMG src="/BASEWeb/Rollup/images/add.gif" onclick="return BeforeAdd()" width="57" height="22" border="0"></TD> -->
                       
          </TR>
        </TBODY>
      </TABLE>
            <SELECT size="6" name="ARList" class="input" onclick="return popIntoFields(ARList,this.form.ARList.value)" style='font-family : "Courier New";' ></SELECT>
      </TD>
        </TR>
  </TBODY>
</TABLE>
</FORM>
</BODY>
</HTML>