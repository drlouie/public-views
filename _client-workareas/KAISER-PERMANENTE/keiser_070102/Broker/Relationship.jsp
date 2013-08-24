<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">

<jsp:useBean id="relationshipVO"  class="org.kp.broker.vo.RelationshipVO"  scope="session"></jsp:useBean>
<HTML>
<HEAD>
<META name="GENERATOR" content="IBM WebSphere Page Designer V3.5.3 for Windows">
<TITLE>Relationship</TITLE>
<SCRIPT language="JavaScript">

   var enableList = false;

function validateForm(theForm)
 {	


var errorStatus = false;
var errorFields ='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("Please correct the following error(s):")%>'+'\n';
var todays = "";

     if(document.Relationship.primaryRole.value == ""  &&
	document.Relationship.secondaryBid.value == ""  &&
	document.Relationship.secBrokerName.value == ""  &&
	document.Relationship.secondaryRole.value == ""  &&
	document.Relationship.effectiveDate.value == ""  &&
	document.Relationship.endDate.value == "" )  {


}
else {


if(document.Relationship.primaryRole.value  == "")
   {
	errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Relation.PrimaryRoleReqd")%>'+'\n';
	errorStatus	= true;			
   }  
 
if(document.Relationship.secondaryBid.value  == "")
   {
	errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Relation.SecondaryBidReqd")%>'+'\n';
	errorStatus	= true;			
   }  else
   {
	checkBrokerID(theForm.secondaryBid.value);
   }
   
if(document.Relationship.secBrokerName.value  == "")
   {
	errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Relation.SecondaryBrokerName")%>'+'\n';
	errorStatus	= true;			
   }
   
if(document.Relationship.secondaryRole.value == "")
   {
	errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Relation.SecondaryRoleReqd")%>'+'\n';
	errorStatus	= true;			
   }  
  if(document.Relationship.effectiveDate.value  == "")
   {
	errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Relation.EffDateReqd")%>'+'\n';
 	errorStatus = true;		
   }else  
   {
          checkeffectiveDate(theForm.effectiveDate.value)  
	 
   }
/*	
  if(document.Relationship.endDate.value  == "")
   {
	errorFields+="endDate Missing \n";
 	errorStatus = true;		
   }else
*/

  if(document.Relationship.endDate.value  != "")
   {
        checkendDate(theForm.endDate.value)  
 	compareDate(theForm.effectiveDate.value,theForm.endDate.value);
   }

}
if (errorStatus == true)
{
	alert(errorFields);
	return false;
}
else
	return true;


function checkBrokerID(BrokerID)
 {
   var checkOK = "0123456789";
   var checkStr = BrokerID;
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
        errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+' BrokerID\n';
    	document.Relationship.secondaryBid.focus();
     }
		
 }//End of checkBrokerID function
function checkeffectiveDate(theDate) {
    var elmstr = theDate;
    if (elmstr.length != 10)
   	{
	   errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Relation.EffDateFormat")%>'+'\n';
	  return false ;	
	}
		 
    for (var i = 0; i < elmstr.length; i++) {
        if ((i < 2 && i > -1) ||
            (i > 2 && i < 5) || 
            (i > 5 && i < 10)) {
            if (elmstr.charAt(i) < "0" || 
                elmstr.charAt(i) > "9") {
		errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Relation.EffDateFormat")%>'+'\n';
		break;
		}
        }
        else if (elmstr.charAt(i) != "/") {
		errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Relation.EffDateFormat")%>'+'\n';
		return false ;	
		}
    }
    return true;
}// is date
  
function checkendDate(theDate) {
    var elmstr = theDate;
    if (elmstr.length != 10)
   	{
	   errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Relation.EndDateFormat")%>'+'\n';
	  return false ;	
	}
		 
    for (var i = 0; i < elmstr.length; i++) {
        if ((i < 2 && i > -1) ||
            (i > 2 && i < 5) || 
            (i > 5 && i < 10)) {
            if (elmstr.charAt(i) < "0" || 
                elmstr.charAt(i) > "9") {
		errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Relation.EndDateFormat")%>'+'\n';
		break;
		}
        }
        else if (elmstr.charAt(i) != "/") {
		errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Relation.EndDateFormat")%>'+'\n';
		return false ;	
		}
    }
    return true;
}// is date
function defaultValue() {
var date = new Date();
var d  = date.getDate();
var day = (d < 10) ? '0' + d : d;
var m = date.getMonth() + 1;
var month = (m < 10) ? '0' + m : m;
var yy = date.getYear();
var year = (yy < 1000) ? yy + 1900 : yy;

todays = (day + "/" + month + "/" + year);
//alert("today" + todays);	
}//defaultValue

function compareDate(date1,date2) {

//defaultValue() ;


  var month1 = date1.substring(0,2);
  var day1 = date1.substring(3,5);
  var year1 = date1.substring(6,10);
  

  var month2 = date2.substring(0,2);
  var day2 = date2.substring(3,5);
  var year2 =date2.substring(6,10);
        
     if(year1 > year2)
	{
	errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Relation.EndDateLesserThanEff")%>'+'\n';
	return false;
	}

	if(year1 == year2)
	{
	if(month1 > month2)
	{
	
	errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Relation.EndDateLesserThanEff")%>'+'\n';
	return false;
	} 
	}
    if(year1 == year2 && month1 == month2 && day1 > day2)
	{
	
	errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Relation.EndDateLesserThanEff")%>'+'\n';
	return false;
	}  
}//end of compare date


}//End of validateForm function

   var oldNo = false;
   var listIndex = 0;

   var listUILength = 0;
   var listUIValues = new Array();


   // Function to hide list if there is no data to display
 
function addListHide1() {
addListHide();

<% 

String isName = "Y";
   isName = (String) session.getAttribute("isName");
    if(isName.equals("Y"))
   { 
 String secName = (String)session.getAttribute("brokerName");	
  org.kp.broker.vo.RelationshipVO brokerNameVO  = ( org.kp.broker.vo.RelationshipVO )session.getAttribute("brokerNameVO");	
%>
document.Relationship.secBrokerName.value = "<%=secName %>"  ;
document.Relationship.primaryRole.value = "<%=brokerNameVO.getPrimaryRole()%>" ;
document.Relationship.secondaryBid.value ="<%=brokerNameVO.getSecondaryBid() %>" 
document.Relationship.secondaryRole.value = "<%=brokerNameVO.getSecondaryRole()%>";
document.Relationship.effectiveDate.value ="<%=brokerNameVO.getEffectiveDate()%>" ;
document.Relationship.endDate.value = "<%=brokerNameVO.getEndDate()%>" ; 
document.Relationship.relId.value = "<%=brokerNameVO.getIdentifier()%>" ; 
document.Relationship.OldPrimaryIK.value = "<%=brokerNameVO.getOldPrimaryBid()%>";
document.Relationship.OldSecondaryIK.value = "<%=brokerNameVO.getOldSecondaryBid()%>";
document.Relationship.PrimarySecondaryIndicator.value = "<%=brokerNameVO.getPrimarySecondaryIndicator()%>";


<% }
     %> 
     
     addsecondaryRole();
	
}

function addListHide() {
	 //alert("inside addListHid");
//      	document.Relationship.AddList.style.visibility = "hidden";


	<!-- Added by Sathish to alert the user for entering incorrect Sec BrokerID -->	

	<%

	String error = (String) session.getAttribute("ERRORRelation");


	if (  !error.equals("nothing") ) {
	
	
		if ( session.getAttribute("RelErrorVO") != null ) {
			org.kp.broker.vo.RelationshipVO rVO = (org.kp.broker.vo.RelationshipVO) session.getAttribute("RelErrorVO");

	%>

			document.Relationship.primaryRole.value = "<%=rVO.getPrimaryRole()%>" ;
			document.Relationship.secondaryBid.value ="<%=rVO.getSecondaryBid() %>";
			document.Relationship.secondaryRole.value = "<%=rVO.getSecondaryRole()%>";
			document.Relationship.effectiveDate.value ="<%=rVO.getEffectiveDate()%>" ;
			document.Relationship.endDate.value = "<%=rVO.getEndDate()%>" ; 
			document.Relationship.relId.value = "<%=rVO.getIdentifier()%>" ; 
			document.Relationship.OldPrimaryIK.value = "<%=rVO.getOldPrimaryBid()%>";
			document.Relationship.OldSecondaryIK.value = "<%=rVO.getOldSecondaryBid()%>";		
			document.Relationship.PrimarySecondaryIndicator.value = "<%=rVO.getPrimarySecondaryIndicator()%>";

			//var userMessage = "BrokerId:"+  "<%=rVO.getSecondaryBid() %>"+ " does not exist. Please enter a valid Sec BrokerId";

		<%
		}
		%>
			

			//alert( "Secondary BrokerId you have typed in does not exist. Please enter a valid Sec BrokerId" );
		alert( "<%=session.getAttribute("ERRORRelation")%>" );

	<%
		session.setAttribute("ERRORRelation", "nothing");
	}
	%>


	<%
	java.util.Vector relVec = (java.util.Vector) session.getAttribute("ModifiedRelataion");
	int vecSize =relVec.size();

	for( int i=0; i<vecSize; i++ ) {
		relationshipVO = ( org.kp.broker.vo.RelationshipVO ) relVec.elementAt(i);
			int j =1;
         %>


     		document.Relationship.AddList.style.visibility = "";
 		
		var addoptions = new Option();


		var elementsMaxLength = new Array();
		var elementsText = new Array();
		var elementsValue = new Array();


		elementsText[0] = "<%=relationshipVO.getPrimaryRole()%>";
		elementsText[1] = "<%=relationshipVO.getSecondaryBid() %>";
		elementsText[2] = "<%=relationshipVO.getSecBrokerName()%>";
		elementsText[3] = "<%=relationshipVO.getSecondaryRole()%>";
		elementsText[4] = "<%=relationshipVO.getEffectiveDate()%>";
		elementsText[5] = "<%=relationshipVO.getEndDate()%>";
		elementsText[6] = "<%=relationshipVO.getIndicator()%>";
	

		elementsMaxLength[0] = 11;
		elementsMaxLength[1] = 11;
		elementsMaxLength[2] = 20
		elementsMaxLength[3] = 11; 
		elementsMaxLength[4] = 11;
		elementsMaxLength[5] = 11;
		elementsMaxLength[6] = 3;
	
		for(var i = 0 ; i < elementsMaxLength.length; i++) {

			if(elementsText[i].length < elementsMaxLength[i]) {

				for(j = elementsText[i].length ; j < elementsMaxLength[i]; j++)
					elementsText[i]+= " ";							
					
			}
			else
				elementsText[i] = elementsText[i].substring(0, elementsMaxLength[i]);
		}


		addoptions.text = elementsText[0] + " " + elementsText[1] + " " + elementsText[2] + " " + elementsText[3] + " " + elementsText[4] + " " + elementsText[5] + " " + elementsText[6];
		addoptions.value = "<%=relationshipVO.getPrimaryRole()%>" + ":" + "<%=relationshipVO.getSecondaryBid()%>" + ":" + "<%=relationshipVO.getSecBrokerName()%>"+ ":" + "<%=relationshipVO.getSecondaryRole()%>" + ":" + "<%=relationshipVO.getEffectiveDate()%>" + ":" + "<%=relationshipVO.getEndDate()%>"+":"+"<%=relationshipVO.getIdentifier()%>"+":"+"<%=relationshipVO.getIndicator()%>"+":"+"<%=relationshipVO.getPrimarySecondaryIndicator()%>"+":"+"<%=relationshipVO.getOldPrimaryBid() %>"+":"+"<%=relationshipVO.getOldSecondaryBid() %>";
 

		document.Relationship.AddList.options[document.Relationship.AddList.options.length] = addoptions;			

		listUIValues[listUILength] = addoptions.value;
		listUILength++;


		 oldNo = true;

		<%
		if( i == 0 ) {
		%>

/*
	document.Relationship.primaryRole.value = "" ;
	document.Relationship.secondaryBid.value = "" ;
	document.Relationship.secBrokerName.value = "";
	document.Relationship.secondaryRole.value = "";
	document.Relationship.effectiveDate.value = "";
	document.Relationship.endDate.value = "" ;
*/

		//disableform ();
		//	document.Relationship.secondaryBid.disabled =true ;
		<%
		}
		%>

		//document.Relationship.AddList.options[0].selected = true;

		document.Relationship.primaryRole.focus();

 			
		<%
		}
		%>
//document.Relationship.endDate.value = "12/31/4000" ;

}


// function to add primary role from db

     function addPrimaryRole() {


	document.Relationship.primaryRole.focus();

      //alert("rr"); 
      
    <%
	
	Vector relVect = (Vector) session.getAttribute("prirelation");
	int vectSize =relVect.size();
	
	 for(int i=0;i<relVect.size();i++) {
   %>
      var prioptions = new Option();
	var secoptions = new Option();
	var str = "<%= (String) relVect.elementAt(i) %>" ; 
 	prioptions.text = "<%= (String) relVect.elementAt(i) %>";
	prioptions.value = "<%= (String) relVect.elementAt(i) %>";
 	secoptions.text = "<%= (String) relVect.elementAt(i) %>";
	secoptions.value = "<%= (String) relVect.elementAt(i) %>";
//alert(prioptions.text + prioptions.value);
document.Relationship.primaryRole.options[document.Relationship.primaryRole.options.length]= prioptions;
document.Relationship.secondaryRole.options[document.Relationship.secondaryRole.options.length]= secoptions;
  <% } %>
 
document.Relationship.primaryRole.value = "";
document.Relationship.secondaryRole.value = "";

 }
// function to add  secondary role from db

function addsecondaryRole(){
   //alert("inside seco role");
document.Relationship.secondaryRole.length=0;
   if(document.Relationship.primaryRole.value =="Employer")
	{
	 var secoptions1 = new Option();
	secoptions1.text="Employee";
	secoptions1.value="Employee";
			document.Relationship.secondaryRole.options[document.Relationship.secondaryRole.length]=secoptions1;
 //alert(document.Relationship.secondaryRole.options.length);
		}

   if(document.Relationship.primaryRole.value =="Parent")
	{
	
	 var secoptions1 = new Option();
	secoptions1.text="Child";
	secoptions1.value="Child";
	document.Relationship.secondaryRole.options[document.Relationship.secondaryRole.length]=secoptions1;
//alert(document.Relationship.secondaryRole.options.length);
		}
   if(document.Relationship.primaryRole.value =="Child")
	{
	
	 var secoptions1 = new Option();
	secoptions1.text="Parent";
	secoptions1.value="Parent";
	document.Relationship.secondaryRole.options[document.Relationship.secondaryRole.length]=secoptions1;
//alert(document.Relationship.secondaryRole.options.length);
		}

   if(document.Relationship.primaryRole.value =="Firm")
	{
	 var secoptions1 = new Option();
	secoptions1.text="Firm";
	secoptions1.value="Firm";
 	var secoptions2 = new Option();
	secoptions2.text="Agent";
	secoptions2.value="Agent";
	document.Relationship.secondaryRole.options[document.Relationship.secondaryRole.length]=secoptions1;
document.Relationship.secondaryRole.options[document.Relationship.secondaryRole.length]=secoptions2;
//alert(document.Relationship.secondaryRole.options.length);
		}

if(document.Relationship.primaryRole.value =="Agent")
	{
	 var secoptions1 = new Option();
	secoptions1.text="Firm";
	secoptions1.value="Firm";
 	var secoptions2 = new Option();
	secoptions2.text="Agent";
	secoptions2.value="Agent";
	document.Relationship.secondaryRole.options[document.Relationship.secondaryRole.length]=secoptions1;
document.Relationship.secondaryRole.options[document.Relationship.secondaryRole.length]=secoptions2;
//alert(document.Relationship.secondaryRole.options.length);
		}
if(document.Relationship.primaryRole.value =="Employee")
	{
	 var secoptions1 = new Option();
	secoptions1.text="Employer";
	secoptions1.value="Employer";
	document.Relationship.secondaryRole.options[document.Relationship.secondaryRole.length]=secoptions1;

//alert(document.Relationship.secondaryRole.options.length);
}

if(document.Relationship.primaryRole.value =="Peer")
	{
	 var secoptions1 = new Option();
	secoptions1.text="Peer";
	secoptions1.value="Peer";
	document.Relationship.secondaryRole.options[document.Relationship.secondaryRole.length]=secoptions1;

//alert(document.Relationship.secondaryRole.options.length);

}
if(document.Relationship.primaryRole.value =="Partner")
	{
	 var secoptions1 = new Option();
	secoptions1.text="Partner";
	secoptions1.value="Partner";
	document.Relationship.secondaryRole.options[document.Relationship.secondaryRole.length]=secoptions1;

//alert(document.Relationship.secondaryRole.options.length);

}

if(document.Relationship.primaryRole.value =="Holding Co.")
	{
	 var secoptions1 = new Option();
	secoptions1.text="Subsidiary";
	secoptions1.value="Subsidiary";
	document.Relationship.secondaryRole.options[document.Relationship.secondaryRole.length]=secoptions1;

//alert(document.Relationship.secondaryRole.options.length);

}
if(document.Relationship.primaryRole.value =="Subsidiary")
	{
	 var secoptions1 = new Option();
	secoptions1.text="Holding Co.";
	secoptions1.value="Holding Co.";
	document.Relationship.secondaryRole.options[document.Relationship.secondaryRole.length]=secoptions1;

//alert(document.Relationship.secondaryRole.options.length);

}

if(document.Relationship.primaryRole.value =="")
	{
	 var secoptions1 = new Option();
	secoptions1.text="           ";//"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
	secoptions1.value="";
	document.Relationship.secondaryRole.options[document.Relationship.secondaryRole.length]=secoptions1;

//alert(document.Relationship.secondaryRole.options.length);

}


}




  
  // Function add, modify and manipulate all the functionalities of the list
   function manipulateList( list, prirole, secbid, secname, secrole, effdt, expdt ) {

     if(document.Relationship.primaryRole.value == ""  &&
	document.Relationship.secondaryBid.value == ""  &&
	document.Relationship.secBrokerName.value == ""  &&
	document.Relationship.secondaryRole.value == ""  &&
	document.Relationship.effectiveDate.value == ""  &&
	document.Relationship.endDate.value == "" )  {


}
else {



     var flag =  validateForm(Relationship);
      if(!flag) return false;
	//alert( oldNo );
	//alert( listIndex );
	 enableform();
	document.Relationship.secondaryBid.disabled =false ;
	var errorStatus = false;
	var errorFields = "Please correct the following error(s):";
	var listLength = list.options.length;
	var prirole = prirole.value;
	var secbid = secbid.value;
	var secname = secname.value;
	var secrole = secrole.value;
	var effdt = effdt.value;
	var expdt = expdt.value;
	
	var optionstext = prirole + "-" + secbid  + "-" + secname + "-" + secrole + "-" + effdt + "-" + expdt  ;
	var optionsValue = prirole + "-" + secbid  + "-" + secname + "-" + secrole + "-" + effdt + "-" + expdt  ;


    

	if ( optionstext == "-------" ) {
		errorStatus = true;
		errorFields += "\n" + "You got to enter something to be added to the list";
	}

	if ( prirole == ""  ) {
		errorStatus = true;
		errorFields += "\n" + "Primary role  cannot be empty";
	}

	if ( secbid == ""  ) {
		errorStatus = true;
		errorFields += "\n" + "Secondary BrokerId  cannot be empty";
	}

	if ( effdt == "" ) {
		errorStatus = true;
		errorFields += "\n" + "Effective Date cannot be empty";
	}
	
/*
	if (expdt  == "" ) {
		errorStatus = true;
		errorFields += "\n" + "Expiration date cannot be empty";
	}
*/
	
	
	if ( errorStatus == true ) {
		alert( errorFields );
		return false;
	}
       else
	{
	submit_form();
	
	}	
	
		

        document.Relationship.AddList.style.visibility = ""; 

	var addoptions = new Option();
	addoptions.text = optionstext;
	addoptions.value = optionstext;


	if ( listLength == 0 ) {

		addFirstRow( list );
	}
	else if ( listLength > 0 && oldNo == false ) {
		addAtEnd( list );
	}
	else {
		modifyList( list, listIndex );

	}


	function addFirstRow(ilist) {
		document.Relationship.AddList.style.visibility = "";
		ilist.options[0]=addoptions;
		//ilist.options[0].selected = true;
	//	refresh();
		resetValue();

		document.Relationship.primaryRole.focus();
	}

	function addAtEnd( ilist ) {
		document.Relationship.AddList.style.visibility = "";
		ilist.options[listLength]=addoptions;
		//ilist.options[listLength].selected = true;
	//	refresh();
		resetValue();
		document.Relationship.primaryRole.focus();
	}

	function modifyList( ilist, ilistIndex ) {
		document.Relationship.AddList.style.visibility = "";
		ilist.options[listIndex]=addoptions;
		//ilist.options[listIndex].selected = true;
		//refresh();
		resetValue();
		document.Relationship.primaryRole.focus();
	}

	 function refresh() {
		document.Relationship.primaryRole.value = "";
		document.Relationship.secondaryBid.value = "";
		document.Relationship.secBrokerName.value = "";
		document.Relationship.secondaryRole.value = "";
		document.Relationship.effectiveDate.value = "";
		document.Relationship.endDate.value = "";



		oldNo = false;
	}


	 if(flag) return true;

      }
   }



   //Added by Sathish for delete functionality
   function deleteFromList() {

     	if(document.Relationship.primaryRole.value == ""  &&
		document.Relationship.secondaryBid.value == ""  &&
		document.Relationship.secBrokerName.value == ""  &&
		document.Relationship.secondaryRole.value == ""  &&
		document.Relationship.effectiveDate.value == ""  &&
		document.Relationship.endDate.value == "" )  {

		alert( '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.SelectRecordToDelete")%>' );
		//alert( "A relationship has to be selected first, to be deleted from the list" );
	}
	else {

		if ( document.Relationship.StatusIndicator.value == "D" ) {
			alert( '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.RecordMarkedDelete")%>' );
			//alert( "The selected relationship is already marked for delete" );
			document.Relationship.opmode.value="delete" ;
			Relationship.submit();
		}
		else {
			document.Relationship.opmode.value="delete" ;
			Relationship.submit();
		}

	}
   }



// function to reset values

function resetValue() {
	var addoptions = new Option();
	addoptions.text = "";
	addoptions.value = "";

	var hsubmit = document.Relationship.submitField.value;
	var hopmode = document.Relationship.opmode.value;
	var haddmode = document.Relationship.addmode.value;
	var hrelid = document.Relationship.relId.value;
	var hbrkName = document.Relationship.brkName.value;
	var hprole = document.Relationship.hprimaryRole.value;
	var hsrole = document.Relationship.hsecondaryRole.value;
	var hsecbid = document.Relationship.hsecondaryBid.value;
	var hsbname = document.Relationship.hsecBrokerName.value;
	var heffdate = document.Relationship.heffectiveDate.value;
	var henddate = document.Relationship.hendDate.value;
	var hbkrbid = document.Relationship.bkrbid.value;
	var hind = document.Relationship.indicator.value;
	var hkey = document.Relationship.TypeChangeKey.value;
	var hstsind = document.Relationship.StatusIndicator.value;

	var prole = document.Relationship.primaryRole.value;
	var srole = document.Relationship.secondaryRole.value;

	document.Relationship.reset();

	document.Relationship.submitField.value = hsubmit;
	document.Relationship.opmode.value = hopmode;
	document.Relationship.addmode.value = haddmode;
	document.Relationship.relId.value = hrelid;
	document.Relationship.brkName.value = hbrkName;
	document.Relationship.hprimaryRole.value = hprole;
	document.Relationship.hsecondaryRole.value = hsrole;
	document.Relationship.hsecondaryBid.value = hsecbid;
	document.Relationship.hsecBrokerName.value = hsbname;
	document.Relationship.heffectiveDate.value = heffdate;
	document.Relationship.hendDate.value = henddate;
	document.Relationship.bkrbid.value = hbkrbid;
	document.Relationship.indicator.value = hind;
	document.Relationship.TypeChangeKey.value = hkey;
	document.Relationship.StatusIndicator.value = hstsind;

	document.Relationship.primaryRole.value = prole;
	document.Relationship.secondaryRole.value = srole;





/*
		document.Relationship.primaryRole.value = "";
		document.Relationship.secondaryBid.value = "";
		document.Relationship.secBrokerName.value = "";
		document.Relationship.secondaryRole.value = "";
		document.Relationship.effectiveDate.value = "";
		document.Relationship.endDate.value = "";
		 
		document.Relationship.primaryRole.text = "";
		document.Relationship.secondaryBid.text = "";
		document.Relationship.secBrokerName.text = "";
		document.Relationship.secondaryRole.text = "";
		document.Relationship.effectiveDate.text = "";
		document.Relationship.endDate.text = "";
*/		 
		 
	}


   function popAgain( popList, popValue ) {


	if ( enableList ) {

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
	
	
	if ( splitData[1] == undefined || splitData[2] == undefined || splitData[3] == undefined) {
		alert('<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.SelectProperRecord")%>' );
		//alert( "Click on the Relationship you want to populate in the fields" );
	}
	else {	
	
       addPrimaryRole();
	document.Relationship.primaryRole.value = splitData[0];
	document.Relationship.secondaryBid.value = splitData[1];
	document.Relationship.secBrokerName.value = splitData[2];
	document.Relationship.secondaryRole.value = splitData[3];
	document.Relationship.effectiveDate.value = splitData[4];
	document.Relationship.endDate.value = splitData[5];
	document.Relationship.relId.value = splitData[6];
	document.Relationship.StatusIndicator.value = splitData[7];
	document.Relationship.PrimarySecondaryIndicator.value = splitData[8];	
	document.Relationship.OldPrimaryIK.value = splitData[9];		
	document.Relationship.OldSecondaryIK.value = splitData[10];			

    //  alert(document.Relationship.secBrokerName.value = splitData[2]);
	oldNo = true;
	if(document.Relationship.secBrokerName.value=="" ){
	document.Relationship.secondaryBid.disabled =false ;
	}
	else
	{
	document.Relationship.secondaryBid.disabled =false ;
	}
addsecondaryRole();
document.Relationship.secondaryRole.value = splitData[3];

	}
	}
	
	//disableform() ;
   }

//function to check effdt between primary broker


// function for date validation

// function for disable
	function disableform() {

	document.Relationship.primaryRole.disabled =true;
	document.Relationship.secondaryBid.disabled =true ;
	document.Relationship.secBrokerName.disabled =true ;
	document.Relationship.secondaryRole.disabled  =true ;
	document.Relationship.effectiveDate.disabled =true ;
	document.Relationship.endDate.disabled =true ;  
  }
  
	function enableform() {

	document.Relationship.primaryRole.disabled =false;
	document.Relationship.secondaryBid.disabled =true ;
	document.Relationship.secBrokerName.disabled =false ;
	document.Relationship.secondaryRole.disabled  =false ;
	document.Relationship.effectiveDate.disabled=false;
	document.Relationship.endDate.disabled =false ;  

        enableList = true;
	document.Relationship.AddList.style.background = "white";
  }

function test(){
var t = validationFinal();
alert("yyyy" + t);
}

function validationFinal() {
//alert("inside---1");
var flag = false;
     if(document.Relationship.primaryRole.value !=""  ||
	document.Relationship.secondaryBid.value !="" ||
	document.Relationship.secBrokerName.value !="" || 
	document.Relationship.secondaryRole.value  !="" ||  
	document.Relationship.effectiveDate.value !="" ||  
	document.Relationship.endDate.value !="" )
{
 	flag = validateForm(Relationship);
	if(!flag) 
	return false; 
}
return flag;			
}//validationFinal 



 function changeMode()
{
var flag = true;
document.Relationship.opmode.value="save" ;

     if(document.Relationship.primaryRole.value !=""  ||
	document.Relationship.secondaryBid.value !="" ||
	document.Relationship.secBrokerName.value !="" || 
	document.Relationship.secondaryRole.value  !="" ||  
	document.Relationship.effectiveDate.value !="" ||  
	document.Relationship.endDate.value !="" )
{
 	flag = validateForm(Relationship);
	if(!flag) 
	return false; 
}
	


}



function submit_form()
{
document.Relationship.opmode.value="add" ;
Relationship.submit();
}

function addSecondaryName()
{

	//Added by Sathish for validating Secondary BID

	var secBID = document.Relationship.secondaryBid.value;
	var mainBID = "<%=session.getAttribute("BIDinSession")%>";

     if ( secBID != "" ) {

	if ( checkSecBid(secBID) ) {

		if ( secBID == mainBID ) {
			alert('<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Relation.PrimaryBIDEqualtoSecBID")%>');
			//alert( "The Secondary BrokerId should not be equal to Primary BrokerID");
			document.Relationship.secondaryBid.value = "";
			document.Relationship.secondaryBid.focus();		
			return false;		

		}
		else {
			document.Relationship.brkName.value="name" ;
			document.Relationship.hprimaryRole.value = document.Relationship.primaryRole.value ;
			document.Relationship.hsecondaryRole.value = document.Relationship.secondaryRole.value ;
			document.Relationship.hsecBrokerName.value = document.Relationship.secBrokerName.value ;
			document.Relationship.heffectiveDate.value = document.Relationship.effectiveDate.value ;
			document.Relationship.hendDate.value = document.Relationship.endDate.value ; 
			Relationship.submit();
		}
	}
    }
}


//Added by sathish to validate the secondary bid
function checkSecBid(validvalue) {

	var valid = "1234567890";

	var bidstatus = true;

	for (var i=0; i < validvalue.length; i++) {
		temp = "" + validvalue.substring(i, i+1);
		if (valid.indexOf(temp) == "-1") {
	      	alert( '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+'Secondary BrokerID' );
			document.Relationship.secondaryBid.value = "";
			bidstatus = false;
	      		break;
		}
	}

	if ( bidstatus )
		return true;
	else 	
		return false;

}


</SCRIPT>



<!--Dynamic CSS Javascript-->
<script language="javascript" src="script/common_css.js"></script>



<script language="Javascript">
<!--
//MOUSEOVER IMAGE PRELOAD

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



</HEAD>

<BODY bgcolor="#0B5F77" OnLoad="addPrimaryRole();addListHide1() ">
<FORM name="Relationship" method="POST"   ACTION="RelationshipServlet" >





  <table width="95%" border="0" cellspacing="0" cellpadding="2" align="center">
    <tr align="center" valign="middle"> 
      <td> 
        <table width="670" border="0" cellspacing="0" cellpadding="0">
          <tr> 
            <td align="left" width="3" height="20"><img src="limages/tleft3.gif" width="3" height="20"></td>
            <td bgcolor="#E6E9F0" width="332" align="left"><font class="stitle">&nbsp;&nbsp;&nbsp;Relationships</font></td>
            <td bgcolor="#E6E9F0" width="335" align="right"> 
              <input type="button" value="Edit" name="Edit" class="lebotton" onClick="enableform()">
              <input type="button" value="Reset" name="button" onclick="resetValue()" class="lebotton">
            </td>
          </tr>
        </table>
        <table border="0" cellspacing="0" cellpadding="0" width="670">
          <tr> 
            <td><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
            <td><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
            <td ><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
          </tr>
          <tr> 
            <td bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
            <td bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
            <td bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
          </tr>
          <tr> 
            <td width="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
            <td width="668"> 
              <table width="100%" border="0" cellpadding="0" cellspacing="0">
                <tbody> 
                <tr> 
                  <td align="center" bgcolor="#E6E9F0" width="150" height="30"><font class="stitle">Primary Broker</font></td>
                  <td colspan="4" align="center" height="30"><font class="ComTitle">Secondary 
                    Broker</font></td>
                  <td colspan="3" align="right" height="30">&nbsp;</td>
                </tr>
                <tr> 
                  <td align="center" bgcolor="#E6E9F0" width="150"><font class="stitle"><font style="color:#eb0000;font-size:11px">*</font>Relationship Role</font></td>
                  <td align="center"><font class="ComTitle">Broker ID</font></td>
                  <td align="center"><font class="ComTitle">Broker Name</font></td>
                  <td align="center"><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Relationship Role</font></td>
                  <td align="center"><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Effective </font></td>
                  <td align="center"><font class="ComTitle">Expired</font></td>
                  <td>&nbsp;</td>
                </tr>
                <tr> 
                  <td align="center" bgcolor="#E6E9F0" width="150"> 
                    <select name="primaryRole" class="select2" tabindex="1" Onchange ="addsecondaryRole()">
                    </select>
                  </td>
                  <td align="center" bgcolor="#E6E9F0"> 
                    <input class="input2" size="10" type="text" maxlength="10" name="secondaryBid" tabindex="2" onBlur="addSecondaryName()" >
                  </td>
                  <td align="center" bgcolor="#E6E9F0"> 
                    <input class="input2" size="15" type="text" maxlength="30" name="secBrokerName"  readonly style="background-color : silver;">
                  </td>
                  <td align="center" bgcolor="#E6E9F0"> 
                    <select name="secondaryRole" class="select2" tabindex="3">
                    </select>
                  </td>
                  <td align="center" bgcolor="#E6E9F0"> 
                    <input class="input2" size="11" type="text" maxlength="10" name="effectiveDate" tabindex="4"  >
                  </td>
                  <td align="center" bgcolor="#E6E9F0"> 
                    <input class="input2" size="11" type="text" maxlength="10" name="endDate"  tabindex="5"  >
                  </td>
                  <td bgcolor="#E6E9F0"><a href="#" tabindex="29" OnClick=" return manipulateList(Relationship.AddList,Relationship.primaryRole,Relationship.secondaryBid, Relationship.secBrokerName, Relationship.secondaryRole, Relationship.effectiveDate, Relationship.endDate);submit_form()" onMouseOver="javascript:add.src = image15.src;" onMouseOut="javascript:add.src = image16.src;"><img src="limages/add_off.gif" width="50" height="19" border="0" alt="Add" name="add"></a></td>
                </tr>
                </tbody> 
              </table>
              <table width="100%" border="0" cellspacing="0" cellpadding="2">
                <tr align="center" valign="bottom"> 
                  <td colspan="7"> 
                    <select size="3" name="AddList" onclick="return popAgain(AddList,this.form.AddList.value)"   OnKeyPress="return popAgain(AddList,this.form.AddList.value)" OnKeyUp="return popAgain(AddList,this.form.AddList.value)" OnKeyDown="return popAgain(AddList,this.form.AddList.value)" class="multiselect3">
                    </select>
                  </td>
                </tr>
                <tr align="center" valign="bottom"> 
                  <td colspan="7"><a href="#" OnClick="deleteFromList()" onMouseOver="javascript:delsel.src = image17.src;" onMouseOut="javascript:delsel.src = image18.src;"><img src="limages/delsel_off.gif" width="138" height="19" border="0" alt="Delete Selected" name="delsel" vspace="0"></a>
	<INPUT type="hidden" name="InsertValues">
	<INPUT type="hidden" name="UpdateValues">
	<INPUT type="hidden" name="CheckUpdateValues">
        <input type="hidden" name="action" value="">
        <input type="hidden" name="submitField" value="save">
	<input type="hidden" name="opmode" value="">
	<input type="hidden" name="addmode" value="">
	<input type="hidden" name="relId" value="0">
	<input type="hidden" name="brkName" value="">
       
	 <input type="hidden" name="hprimaryRole" value="">
	<input type="hidden" name="hsecondaryRole" value="">
	<input type="hidden" name="hsecondaryBid" value="">
	<input type="hidden" name="hsecBrokerName" value="">
	<input type="hidden" name="heffectiveDate" value="0">
	<input type="hidden" name="hendDate" value="">
	<input type="hidden" name="bkrbid" value="<%=session.getAttribute("BIDinSession")%>">
	<input type="hidden" name="indicator" value="0">
	<input type="hidden" name="TypeChangeKey" value="">

	<input type="hidden" name="StatusIndicator" value="">
	<input type="hidden" name="PrimarySecondaryIndicator" value="">
	<input type="hidden" name="OldPrimaryIK" value="0">
	<input type="hidden" name="OldSecondaryIK" value="0">	
	<INPUT type="hidden" name="SaveExitPage" value="No">		
                  </td>
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
    </tr>
  </table>




</FORM>
</BODY>
</HTML>