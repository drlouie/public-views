<!-- aaSample JSP file -->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML>
<jsp:useBean id="rollupVO" class="org.kp.base.rollup.vo.RollUpVO" />
<jsp:useBean id="rollupRelationVO" class="org.kp.base.rollup.vo.RollupRelationshipsVO" />
<jsp:useBean id="euVO" class="org.kp.base.rollup.vo.EnrollmentUnitsVO" />
<%
	java.util.Vector  rollupRelationV = new java.util.Vector();
	java.util.Vector  popupEuV   = new java.util.Vector();
	rollupVO = (org.kp.base.rollup.vo.RollUpVO)session.getAttribute("ModifiedRollup");
    rollupRelationV = (java.util.Vector)rollupVO.getRollupRelation();
    popupEuV = (java.util.Vector)session.getAttribute("EnrollmentUnits");

%>
<HEAD>
<META name="GENERATOR" content="IBM WebSphere Page Designer V3.5.3 for Windows">
<META http-equiv="Content-Style-Type" content="text/css">
<TITLE>Administer Rollup - Page 2</TITLE>
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
function checkPIDTPA( ID )
 {
   var checkOK = "0123456789";
   var checkStr = ID;
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
        return true;
     }
		
 }//End of checkBrokerID function
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
             
            
           /* if (  SelectedIndicator == "H" ||SelectedIndicator == "A"    )
        	{
           		     	alert( "<%= org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.DoNotModifyHistory")%>");
                        	return true;
	       	} */
	
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

	} // end of checkV
function init()
{	
	DisableForm();
	
    //document.AdministerRollupRelationshipsForm.EUList.style.visibility = "hidden";
    document.AdministerRollupRelationshipsForm.CurrentDate.value = "<%=session.getAttribute("CurrentDate").toString()%>";
 	document.AdministerRollupRelationshipsForm.RollupNumber.value = '<%=rollupVO.getRollupNumber()%>';
 	document.AdministerRollupRelationshipsForm.RollupName.value = '<%=rollupVO.getRollupName()%>';
 	document.AdministerRollupRelationshipsForm.EffectiveDate.value = '<%=rollupVO.getEffectiveDate()%>';
 	document.AdministerRollupRelationshipsForm.EndDate.value = '<%=rollupVO.getEndDate()%>';
    <% 
			String errorMsg = (String) session.getAttribute("errorMsg"); 
 			if(!errorMsg.equals("Empty") ) 
 			{ 
 				rollupRelationVO = (org.kp.base.rollup.vo.RollupRelationshipsVO)session.getAttribute("MaintainOldValuesVO");
 				%>
 			    document.AdministerRollupRelationshipsForm.RREffectiveDate.value = '<%=rollupRelationVO.getEffectiveDate()%>';
 			    document.AdministerRollupRelationshipsForm.RREndDate.value       = '<%=rollupRelationVO.getEndDate()%>';
 			    document.AdministerRollupRelationshipsForm.EUName.value          = '<%=rollupRelationVO.getEUName()%>';
 			    document.AdministerRollupRelationshipsForm.PIDTPA.value           = '<%=rollupRelationVO.getPID()%>';
 			    document.AdministerRollupRelationshipsForm.EUDIV.value			= '<%=rollupRelationVO.getEUID()%>';
 			    document.AdministerRollupRelationshipsForm.Indicator.value   = '<%=rollupRelationVO.getIndicator()%>';
 			    document.AdministerRollupRelationshipsForm.SortOrder.value   = '<%=rollupRelationVO.getSortOrder()%>';
 			    document.AdministerRollupRelationshipsForm.PurIK.value      = '<%=rollupRelationVO.getPurIK()%>';
			    document.AdministerRollupRelationshipsForm.PeuIK.value      = '<%=rollupRelationVO.getPeuIK()%>';
 			    document.AdministerRollupRelationshipsForm.RerIK.value      = '<%=rollupRelationVO.getRerIK()%>';
 			   	alert("<%=errorMsg%>");
    			<% 
    	    } %>
        
 //       if(document.AdministerRollupRelationshipsForm.RollupRelationshipsList.length == 0 )
    	RollupRelationshipsDisplay();
    <% if(popupEuV.size() > 0 )
       {
     %>
     		GetEnrollmentUnits();
    <%
       }
    %>  
   
}
function RollupRelationshipsDisplay()
{
	var affectedSortOrder = "";
	var affectedRerIK = "";
    var affectedRecord = 0;
	document.AdministerRollupRelationshipsForm.RollupRelationshipsList.style.visibility = "hidden";
<% 
	int  recordPosition = 0; 	
	for( int i=rollupRelationV.size(); i > 0; i-- ) 
    {
        recordPosition = recordPosition+1;
 		rollupRelationVO = ( org.kp.base.rollup.vo.RollupRelationshipsVO )rollupRelationV.elementAt(i-1);
 %>
    	var elementsMaxLength = new Array();
		var elementsText = new Array();
		var elementsValue = new Array();
		elementsText[0] = '<%=rollupRelationVO.getPID()%>';
		elementsText[1] = '<%=rollupRelationVO.getEUID()%>';
		elementsText[2] = '<%=rollupRelationVO.getEUName()%>';
		elementsText[3] = '<%=rollupRelationVO.getEffectiveDate()%>';
		elementsText[4] = '<%=rollupRelationVO.getEndDate()%>';
		elementsText[5] = '<%=rollupRelationVO.getIndicator()%>';
		
		elementsMaxLength[0] = 18;
		elementsMaxLength[1] = 15;
		elementsMaxLength[2] = 49;
		elementsMaxLength[3] = 15
		elementsMaxLength[4] = 15;
		elementsMaxLength[5] = 1;
		
		 if( elementsText[5] != "A" && elementsText[5] != "D" ) 
		 {
		 	if(  <%=rollupRelationVO.getSortOrder()%> != 0 )
		 		elementsText[5] = "U"; 
		 	else if( IsThisDateRangeCurrent(elementsText[3],elementsText[4] ) )
		 		elementsText[5] = '***';
		 	else
		 	   	elementsText[5] = "";
         }   	
        
        	
       
         
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

	    document.AdministerRollupRelationshipsForm.RollupRelationshipsList.style.visibility = "";
		var addoptions = new Option();
		addoptions.text = elementsText[0]+ " " +elementsText[1]+ " " +elementsText[2]+ " " +elementsText[3]+" "+elementsText[4]+" "+elementsText[5];
		addoptions.value ="<%=rollupRelationVO.getPID()%>"+ "," +"<%=rollupRelationVO.getEUID()%>"+ "," +"<%=rollupRelationVO.getEUName()%>"+","+"<%=rollupRelationVO.getEffectiveDate()%>"+","+"<%=rollupRelationVO.getEndDate()%>"+","+"<%=rollupRelationVO.getIndicator()%>"+","+"<%=rollupRelationVO.getRerIK()%>"+","+"<%=rollupRelationVO.getPurIK()%>"+","+"<%=rollupRelationVO.getPeuIK()%>"+","+"<%=rollupRelationVO.getSortOrder()%>";
		document.AdministerRollupRelationshipsForm.RollupRelationshipsList.options[document.AdministerRollupRelationshipsForm.RollupRelationshipsList.options.length] = addoptions;
<%    	String error = (String) session.getAttribute("errorMsg"); 
 			if(!error.equals("Empty") ) 
 			{ 
 				String EditedSortOrder = (String) session.getAttribute("EditedSortOrder");
 				String EditedIK        = (String) session.getAttribute("EditedIK");
 			%>
 				affectedSortOrder = "<%=rollupRelationVO.getSortOrder()%>";
 				affectedRerIK     = "<%=rollupRelationVO.getRerIK()%>";
 				if( ( affectedSortOrder == '<%=EditedSortOrder%>') &&
 					( affectedRerIK    == '<%=EditedIK%>') )
 				{
 					  affectedRecord = '<%=recordPosition%>';
 				}
<% 			}
	
	} 
	 session.setAttribute("errorMsg","Empty"); %>
	if(affectedRecord != "")	
		document.AdministerRollupRelationshipsForm.RollupRelationshipsList.options[affectedRecord-1].selected = true;				
}

function GetEnrollmentUnits()
{
    document.AdministerRollupRelationshipsForm.EUList.style.visibility = "hidden";
	
<% 
	for( int i=0; i < popupEuV.size(); i++ ) 
    {
        euVO = ( org.kp.base.rollup.vo.EnrollmentUnitsVO )popupEuV.elementAt(i);
 %>
    	var elementsMaxLength = new Array();
		var elementsText = new Array();
		var elementsValue = new Array();
		elementsText[0] = '<%=euVO.getRowNum()%>';
		elementsText[1] = '<%=euVO.getPID()%>'+"-"+'<%=euVO.getEUID()%>';
		elementsText[2] = '<%=euVO.getEUName()%>';
		elementsText[3] = '<%=euVO.getEffectiveDate()%>';
		elementsText[4] = '<%=euVO.getEndDate()%>';
		
		elementsMaxLength[0] = 10;
		elementsMaxLength[1] = 22;
		elementsMaxLength[2] = 52;
		elementsMaxLength[3] = 16;
		elementsMaxLength[4] = 15;

		

		for(var i = 0 ; i < elementsMaxLength.length; i++)
		{	
						
			if(elementsText[i].length < elementsMaxLength[i])
			{	
					for(var j = elementsText[i].length ; j < elementsMaxLength[i]; j++)
					{		
							elementsText[i]+= " ";							
					}
					
				}
			
		}

	    document.AdministerRollupRelationshipsForm.EUList.style.visibility = "";
		var addoptions = new Option();
		addoptions.text = elementsText[0]+ " " +elementsText[1]+ " " +elementsText[2]+ " " +elementsText[3]+" "+elementsText[4];
		addoptions.value ="<%=euVO.getPID()%>"+ "," +"<%=euVO.getEUID()%>"+ "," +"<%=euVO.getEUName()%>"+","+"<%=euVO.getEffectiveDate()%>"+","+"<%=euVO.getEndDate()%>"+","+""+","+"0"+","+"<%=euVO.getPurIK()%>"+","+"<%=euVO.getPeuIK()%>"+","+"-10000";
		document.AdministerRollupRelationshipsForm.EUList.options[document.AdministerRollupRelationshipsForm.EUList.options.length] = addoptions;

<% 	}  %>
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
   /* if(tokenizedData[5] == "A")
	{
		alert("<%= org.kp.base.web.util.MessageUtil.getInstance().getText("rollup.noModifyOnHistory")%>");
		return false;
	} */
	document.AdministerRollupRelationshipsForm.PIDTPA.value = tokenizedData[0];
	document.AdministerRollupRelationshipsForm.EUDIV.value  = tokenizedData[1];
	document.AdministerRollupRelationshipsForm.EUName.value = tokenizedData[2];
	document.AdministerRollupRelationshipsForm.RREffectiveDate.value = tokenizedData[3];
	document.AdministerRollupRelationshipsForm.RREndDate.value =  tokenizedData[4];
	document.AdministerRollupRelationshipsForm.Indicator.value =  tokenizedData[5];
	document.AdministerRollupRelationshipsForm.RerIK.value =  tokenizedData[6];
	document.AdministerRollupRelationshipsForm.PurIK.value = tokenizedData[7];
	document.AdministerRollupRelationshipsForm.PeuIK.value = tokenizedData[8];
    document.AdministerRollupRelationshipsForm.SortOrder.value = tokenizedData[9];
	document.AdministerRollupRelationshipsForm.FromListBox.value = "Yes";
    
    
    document.AdministerRollupRelationshipsForm.PIDTPA.disabled = true;
	document.AdministerRollupRelationshipsForm.EUDIV.disabled = true;
} 
function BeforeAdd()
{
    EnableForm();
    if(document.AdministerRollupRelationshipsForm.PurIK.value == 0 )
    {
    	alert("<%= org.kp.base.web.util.MessageUtil.getInstance().getText("rollup.selectEUToAdd")%>");
    	return false;
    }
	var errorStatus = false;
	errorStatus = 	isCurrentRecordExists(document.AdministerRollupRelationshipsForm.RollupRelationshipsList,"Add");
	if(errorStatus)
		return false;
	errorStatus = checkDateValidation("RREffectiveDate",document.AdministerRollupRelationshipsForm.RREffectiveDate.value);
	if(errorStatus)
		return false;
	if(document.AdministerRollupRelationshipsForm.RREndDate.value != "")
	{
		errorStatus = checkDateValidation("RREndDate",document.AdministerRollupRelationshipsForm.RREndDate.value);
		if(errorStatus)
			return false;
	}
	document.AdministerRollupRelationshipsForm.EUName.disabled = false;
	document.AdministerRollupRelationshipsForm.SelectedAction.value = "Add";
 	document.AdministerRollupRelationshipsForm.submit();    
	
 
}
function BeforeDelete()
{
	EnableForm();
    var errorStatus = false;
    errorStatus = isCurrentRecordExists(document.AdministerRollupRelationshipsForm.RollupRelationshipsList,"Delete");
    if(errorStatus)
    	return false;
	document.AdministerRollupRelationshipsForm.SelectedAction.value = "Delete";
 	document.AdministerRollupRelationshipsForm.submit();    
}
function BeforeSave()
{
	EnableForm();
	document.AdministerRollupRelationshipsForm.SelectedAction.value = "Save";
 	document.AdministerRollupRelationshipsForm.submit();    
}
function BeforeGettingRollup(FromWhere)
{
var result = validateRollupID(document.AdministerRollupRelationshipsForm.RollupNumber.value)
	if(result == false)
		return false;

    EnableForm();
    if(FromWhere == "RollupNumber")
    {
    	if(document.AdministerRollupRelationshipsForm.RollupNumber.value != "")
    	{
    	 	document.AdministerRollupRelationshipsForm.SelectedAction.value = "Search";
			document.AdministerRollupRelationshipsForm.submit();
		}
    }
    else
    {
    	if(document.AdministerRollupRelationshipsForm.RollupName.value != "")
    	{
	    	document.AdministerRollupRelationshipsForm.SelectedAction.value = "Search";
			document.AdministerRollupRelationshipsForm.submit();
		}
    		
    }
    
	//alert("BeforeGettingRollup");
}
function BeforeGettingEnrollmentUnits()
{
 	
 	if(document.AdministerRollupRelationshipsForm.FilterSearch[0].checked == false && document.AdministerRollupRelationshipsForm.FilterSearch[1].checked == false  )
 	{
 	    alert("<%= org.kp.base.web.util.MessageUtil.getInstance().getText("rollup.enterSearchCriteria")%>");
 		return false;
 	} 	
	if(document.AdministerRollupRelationshipsForm.PIDTPA.value == "" ) //|| document.AdministerRollupRelationshipsForm.EUDIV.value == "" )
 	{
 		alert("<%= org.kp.base.web.util.MessageUtil.getInstance().getText("rollup.enterPIDEU")%>");
 		return false;
 	}
 	else
 	{
 		var errorStatus = false;
 		errorStatus = checkPIDTPA(document.AdministerRollupRelationshipsForm.PIDTPA.value);
 	 	if(document.AdministerRollupRelationshipsForm.EUDIV.value != "")
 	 		errorStatus = checkPIDTPA(document.AdministerRollupRelationshipsForm.EUDIV.value);
 	    if(errorStatus)
 	    {
 	    	alert("<%= org.kp.base.web.util.MessageUtil.getInstance().getText("rollup.invalidChars")%>"+"PIDTPA or EUDIV" );
 	    	return false;
 	     }
 	 }  
	EnableForm();	
	document.AdministerRollupRelationshipsForm.SelectedAction.value = "GetEnrollmentUnits";
	document.AdministerRollupRelationshipsForm.submit();
}
function CustomReset()
{
	document.AdministerRollupRelationshipsForm.reset();
	document.AdministerRollupRelationshipsForm.RollupRelationshipsList.style.visibility = "hidden";
}
function EnableForm()
{
	document.AdministerRollupRelationshipsForm.RollupNumber.disabled = false;
	document.AdministerRollupRelationshipsForm.RollupName.disabled = false;
	document.AdministerRollupRelationshipsForm.PIDTPA.disabled = false;
	document.AdministerRollupRelationshipsForm.EUDIV.disabled = false;
	document.AdministerRollupRelationshipsForm.RREffectiveDate.disabled = false;
	document.AdministerRollupRelationshipsForm.RREndDate.disabled = false;
}
function DisableForm()
{
	document.AdministerRollupRelationshipsForm.RollupNumber.disabled = true;
	document.AdministerRollupRelationshipsForm.RollupName.disabled = true;
	document.AdministerRollupRelationshipsForm.PIDTPA.disabled = true;
	document.AdministerRollupRelationshipsForm.EUDIV.disabled = true;
	document.AdministerRollupRelationshipsForm.RREffectiveDate.disabled = true;
	document.AdministerRollupRelationshipsForm.RREndDate.disabled = true;
}
function AllowEditing()
{
	EnableForm();
	document.AdministerRollupRelationshipsForm.PIDTPA.disabled = true;
	document.AdministerRollupRelationshipsForm.EUDIV.disabled = true;

}
function AllowSearching()
{
	EnableForm();
	document.AdministerRollupRelationshipsForm.PIDTPA.value = "";
	document.AdministerRollupRelationshipsForm.EUDIV.value = "";
	document.AdministerRollupRelationshipsForm.RREffectiveDate.value = "";
	document.AdministerRollupRelationshipsForm.RREndDate.value = "";
	document.AdministerRollupRelationshipsForm.EUName.value = "";
}
function IsThisDateRangeCurrent(EffectiveDate,EndDate)
{
		 var Status = false;
		 var currentdate = document.AdministerRollupRelationshipsForm.CurrentDate.value;
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

   	var sourceId1 = document.AdministerRollupRelationshipsForm.RollupNumber.value;
	var sourceId2 = document.AdministerRollupRelationshipsForm.PurIK.value;
	var sourceId3 = document.AdministerRollupRelationshipsForm.PeuIK.value;
	if(sourceId1 == '')
	{
		alert("<%= org.kp.base.web.util.MessageUtil.getInstance().getText("rollup.comment.noRollupNoFound")%>");		
		return false;
	}
	if(sourceId2 == '')
	{
		sourceId2 = '0';
		sourceId3 = '0';
	} 	 	
	var url = '../Comments/CommentServlet?sourceId1='+sourceId1+'&sourceId2='+sourceId2+'&sourceId3='+sourceId3+'&sourceInd=ROL&funType='+functionType;	
	window.open(url, 'slideWindow',false,500,700);
	
   }
function validateRollupID(value)
 { 
	var valid = "1234567890";	
	for (var i=0; i < value.length; i++) 
	  			{
					temp = "" + value.substring(i, i+1);
					if (valid.indexOf(temp) == "-1") 
     						{
							alert("<%= org.kp.base.web.util.MessageUtil.getInstance().getText("rollup.invalidChars")%>"+" Rollup ID");							
							return false;
       						break;
     						}
  				}
 }
</Script>
</HEAD>
<BODY bgcolor="#999999" text="#000000" OnLoad="init();">
<FORM name="AdministerRollupRelationshipsForm" action="AdministerRollupRelationshipsServlet" method="POST">
<TABLE width="913" cellpadding="0" cellspacing="0">
    <TBODY>
    <TR>
      <TD bgcolor="#ffcc00"><INPUT type="button" name="dynamic" value="ROL101-Administer Rollup - Page 2" class = "button"></TD>
      <TD class="title" align="right" bgcolor="#ffcc00"><A href="/BASEWeb/Purchaser/index.jsp" target="_parent"><IMG src="/BASEWeb/Purchaser/images/search.gif" width="68" height="22" border="0" alt="Search" ></A><IMG  src="/BASEWeb/Purchaser/images/save.gif" width="50" height="22" border="0" alt="Save" onclick="return BeforeSave()"><A href="http://localhost:8080/BASEWeb/Purchaser/mainmenu.html" target="_parent"><IMG src="/BASEWeb/Purchaser/images/exit.gif" width="50" height="22" border="0" alt="Exit" ></A><IMG src="/BASEWeb/Purchaser/images/print.gif" width="50" height="22" border="0" alt = "Print" onClick="callPrint();"><IMG src="/BASEWeb/Purchaser/images/comments.gif" width="86" height="22" border="0" alt = "Comments" onClick="callComments()"></TD>    
      </TR>
  </TBODY>
</TABLE>
<TABLE border="0" width="885">
        <TBODY>
          <TR>
                       <!--Commented By Sabari on Apr.27.2002 <TD valign="top" align="right" width="726"><A href="../Purchaser/PurchaserGeneralInfoServlet" target="_parent"><FONT size="3" face="Times New Roman">&gt;&gt;Admin Purchaser</FONT></A></TD> -->
                        <!-- <TD valign="top" align="right" width="639"><IMG src="/BASEWeb/EnrollmentUnit/images/save.gif" width="50" height="22" border="0" onclick="return BeforeSave()"></TD> -->
            <TD valign="top" align="right" rowspan="2" width="755"></TD>
            <TD align="right" width="120"><IMG src="/BASEWeb/EnrollmentUnit/images/edit.gif" width="50" height="22" border="0" onclick="return AllowEditing()"><IMG src="/BASEWeb/EnrollmentUnit/images/reset.gif" width="50" height="22" border="0" onclick="CustomReset()"></TD>
        </TR>
        <TR>
            <TD align="right" width="120"><A href="AdministerRollupServlet" target="_parent"><FONT size="3" face="Times New Roman">&gt;&gt;Rollup Page 1</FONT></A></TD>
        </TR>
        <TR>
            <!-- Commented By Sabari on Apr.27.2002 <TD valign="top" align="right" width="726"><A href="../EnrollmentUnit/EUGeneralInfoSerlvet" target="_parent"><FONT size="3" face="Times New Roman">&gt;&gt;Admin Enrollment Unit</FONT></A></TD> -->
                    </TR>
    </TBODY>
      </TABLE>
<TABLE border="1">
  <TBODY>
    <TR>
            <TD valign="top" nowrap height="49" width="855">
            <TABLE border="0" width="729">
           <TR>
                        <TD valign="middle" align="center" class="label" width="128">Rollup Number</TD>
                        <TD valign="middle" align="center" class="label" width="338">Roll-up Name</TD>
                        <TD valign="middle" align="center" class="label" width="120">Effective Date</TD>
                        <TD valign="middle" align="center" class="label" width="125">End Date</TD>
                    </TR>
       </TABLE border="0">
            <TABLE width="714">    
      <TR>
                        <TD width="85"><INPUT  size="17" type="text"  name="RollupNumber" onChange='return BeforeGettingRollup("RollupNumber");' tabindex="1"></TD>
                        <TD width="379"><INPUT  size="49" type="text"  name="RollupName" onChange='return BeforeGettingRollup("RollupName");' tabindex="2"></TD>
                        <TD width="118"><INPUT  size="16" type="text" maxlength="10" readonly name="EffectiveDate" style="background-color : silver;" tabindex="3"></TD>
                        <TD width="104"><INPUT class="input" size="12" type="text" maxlength="10" readonly name="EndDate" style="background-color : silver;" tabindex="4"></TD>
                        <!-- <TD class="label" colspan="2">Indicator</TD> -->
       </TABLE>
            </TD>
        </TABLE>
<% if( popupEuV.size() > 0 )
				  {
				%>
<TABLE border="1" width="861">
           			<TR>
            <TD valign="middle" align="center" class="label" width="78">Row Number</TD>
            <TD valign="middle" align="center" class="label" width="153">PID-EU</TD>
            <TD valign="middle" align="center" class="label" width="355">EU Name</TD>
            <TD valign="middle" align="center" class="label" width="114">Effective Date</TD>
            <TD valign="middle" align="center" class="label" width="127">End Date</TD>
        </TR>
       				</TABLE border="0">
<TABLE>    
      				<TR>
            <TD valign="top" height="95" width="852"><SELECT size="6" name="EUList" class="input" onclick="return popIntoFields(EUList,this.form.EUList.value)" style='font-family : "Courier New";'></SELECT></TD>
        </TR>
     			 </TABLE>
			<%  }   %>
<TABLE border="0" width="868">
<TR>
            <TD width="750" height="46">
            <TABLE>
                <TBODY>
                    <TR>
                        <TD class = "label"><INPUT type="radio" name="FilterSearch" value="PIDEU" onclick="AllowSearching()"> PID / EU </TD>
                        <TD class = "label"><INPUT type="radio" name="FilterSearch" value="TPADIV" onclick="AllowSearching()" > TPA / DIV</TD>
                        <TD align="center" width="71"><INPUT size="20" type="button" maxlength="20" name="Delete" value="Get Enrollment Units" class="pbttn" onclick="return BeforeGettingEnrollmentUnits()"></TD>
                        <!-- <TD><IMG src="images/getenrollmentunits.gif" width="158" height="22" border="0" onclick="return BeforeGettingEnrollmentUnits()"></TD> -->
                    </TR>
                </TBODY>
            </TABLE>
            </TD>
            <TD width="108" align="right" height="46"></TD>
        </TR>
</TABLE>
<TABLE width="826" border="0">
        <TBODY>
          <TR>
            <TD valign="middle" align="center" class="label" width="121"> PID / TPA</TD>
            <TD valign="middle" align="center" class="label" width="113">EU / Division</TD>
            <TD valign="middle" align="center" class="label" width="333">Enrollment Unit Name</TD>
            <TD valign="middle" align="center" class="label" width="99">Effective Date</TD>
            <TD valign="middle" align="center" class="label" width="84">End Date</TD>
            <TD valign="middle" align="center" width="61"></TD>
            <TD align="center" width="71"><INPUT size="20" type="button" maxlength="20" name="Delete" value="Delete" class="pbttn" onclick="return BeforeDelete();"></TD>
            <!-- <TD valign="middle" align="center" width="61"><IMG src="/BASEWeb/EnrollmentUnit/images/delete.gif" width="58" height="22" border="0" onclick="return BeforeDelete()"></TD> -->
        </TR>
          <TR>
            <TD width="121"><INPUT  size="15" type="text"  name="PIDTPA" tabindex="5" maxlength="15"></TD>
            <TD width="113"><INPUT  size="15" type="text"  name="EUDIV" tabindex="6"></TD>
            <TD width="333"><INPUT  size="47" type="text" readonly name="EUName" style="background-color : silver;" ></TD>
            <TD width="99"><INPUT  size="13" type="text" maxlength="10" name="RREffectiveDate" tabindex="7"></TD>
            <TD width="84"><INPUT  size="11" type="text" maxlength="10" name="RREndDate" tabindex="8"></TD>
            <TD class="label" width="61">Indicator</TD>
            <TD align="center" width="71"><INPUT size="20" type="button" maxlength="20" name="Add" value="  Add  " class="pbttn" onclick=" return BeforeAdd()" tabindex="9"></TD>
            <!-- <TD class="label" width="61"><IMG src="/BASEWeb/EnrollmentUnit/images/add.gif" onclick="return BeforeAdd()" width="57" height="22" border="0"></TD> -->
        </TR>
        </TBODY>
      </TABLE>
<input type="hidden" name="PurIK" value="0" >
            <input type="hidden" name="PeuIK" value="0" >
            <input type="hidden" name="EUEffectiveDate" value="01/01/2001" >
            <input type="hidden" name="EUEndDate" value="" >
		  	<input type="hidden" name="SelectedAction" value="" >
            <input type="hidden" name="RerIK" value="0" >
            <input type="hidden" name="Indicator" value="" >
			<input type="hidden" name="sourceId1" value="0" >
			<input type="hidden" name="sourceId2" value="0" >
			<input type="hidden" name="sourceId3" value="0" >
			<input type="hidden" name="sourceInd" value="EU" >
            <input type="hidden" name="SortOrder" value="-10000" >
            <input type="hidden" name="WhereToGo" value="" >
		  	<input type="hidden" name="FromWhere" value="0" >
            <input type="hidden" name="message" value="" >
            <input type="hidden" name="CurrentDate" value="" >
            <input type="hidden" name="FromListBox" value="No" >
<TABLE width="44">
      <TR>
      	<TD>
      <SELECT size="7" name="RollupRelationshipsList" class="input" onClick="return popIntoFields(RollupRelationshipsList,this.form.RollupRelationshipsList.value)"  style='font-family : "Courier New";' ></SELECT> 
       </TD>
       </TR>
       </TABLE>
<!-- </TD>
     </TR>
  </TBODY>
</TABLE> -->
</FORM>
</BODY>
</HTML><B></B>