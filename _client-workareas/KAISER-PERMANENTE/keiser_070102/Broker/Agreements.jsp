<!-- Sample HTML file --> <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">

<jsp:useBean id="Agr" class="org.kp.broker.vo.AgreementVO" />

<jsp:useBean id="brokerDropDownVO" class="org.kp.broker.vo.BrokerDropDownVO" />

<%
	brokerDropDownVO = (org.kp.broker.vo.BrokerDropDownVO)session.getAttribute("DropDowns");
%>

<HTML>
<HEAD>
<META name="GENERATOR" content="IBM WebSphere Page Designer V3.5 for Windows">
<TITLE>BRK101 Agreement Information</TITLE>


<%@ include file="script/ValidateAgreements.js" %>
  

<!--
<Script src="script/ValidateAgreements.js">
</Script>
-->

<Script language="JavaScript">

   var oldNo = false;
   var listIndex = 0;
   var listAgrLength = 0;
   var listNameValues = new Array();

   var enableList = false;
   var cmsnset = new Array();

   function populateFields() {


	if ( parent.BrokerMain.document.forms[0] != undefined ) {
	
		if ( parent.BrokerMain.document.forms[0].changeType[0].checked == true ) {
		
			document.forms[0].Honorific.value = parent.BrokerMain.document.forms[0].Honor.value;
			document.forms[0].FirstName.value = parent.BrokerMain.document.forms[0].FName.value;
			document.forms[0].LastName.value = parent.BrokerMain.document.forms[0].LName.value;			
			document.forms[0].MiddleName.value = parent.BrokerMain.document.forms[0].MName.value;			
			document.forms[0].Suffix.value = parent.BrokerMain.document.forms[0].Suffix.value;									
		}
	}




	<%  
			
		java.util.Vector agrCmsnSetstrtDt = new java.util.Vector();
		agrCmsnSetstrtDt = brokerDropDownVO.getCmsnSetStrtDt();
			
		for(int i = 0 ; i < agrCmsnSetstrtDt.size(); i++) {
	%>	
			cmsnset[<%=i%>] = '<%=agrCmsnSetstrtDt.elementAt(i)%>';
	<%
	}			
	%>

	document.AgreementsForm.Honorific.focus();

//		document.AgreementsForm.AddList.style.visibility = "hidden";
	document.AgreementsForm.AgrID.value = "0";

	document.AgreementsForm.BKRBID.value = "<%=session.getAttribute("BIDinSession")%>";

	document.AgreementsForm.ComsnSchedSet.value = "";
	document.AgreementsForm.GenerateReprintReason.value = "";
	<%
	java.util.Vector agrVec = (java.util.Vector) session.getAttribute("ModifiedAgreements");
	int vecSize = agrVec.size();

	
	for( int i=0; i<vecSize; i++ ) {

		Agr = ( org.kp.broker.vo.AgreementVO ) agrVec.elementAt(i);




	%>

		var effdate = "<%=Agr.getEffectiveDate()%>";
		var comsnschedset = "<%=Agr.getComsnSchedSet()%>";
		var reprintreason = "<%=Agr.getReprintReason()%>";

		var enddate = "<%=Agr.getEndDate()%>";
		var generated = "<%=Agr.getGenerated()%>";
		var datemailed = "<%=Agr.getDateMailed()%>";
		var faxsig = "<%=Agr.getFaxSigned()%>";
		var faxexp = "<%=Agr.getFaxExpiration()%>";
		var orgsig = "<%=Agr.getSigned()%>";
		var reprint = "<%=Agr.getReprintDate()%>";
		var stsind = "<%=Agr.getIndicator()%>";

		var reprintreasontext = "";


		if ( reprintreason == "101" )
			reprintreasontext = "New Document";
		else if ( reprintreason == "102" )
			reprintreasontext = "Signatory Change";
		else if ( reprintreason == "103" )
			reprintreasontext = "Broker Name Change";
		else if ( reprintreason == "104" )
			reprintreasontext = "Commission Schedule Effective Date Change";
		else if ( reprintreason == "105" )
			reprintreasontext = "Commission Schedule Set Change";
		else if ( reprintreason == "201" )
			reprintreasontext = "Lost";
		else if ( reprintreason == "202" )
			reprintreasontext = "Broker Requested Copy";
		else if ( reprintreason == "299" )
			reprintreasontext = "Other";



		
		//var agrText = effdate + "-" + enddate + "-" + comsnschedset + "-" + reprintreasontext + "-" + generated + "-" + datemailed + "-" + faxsig + "-" + faxexp + "-" + orgsig + "-" + reprint;


		var elementsMaxLength = new Array();
		var elementsText = new Array();
		var elementsValue = new Array();


		elementsText[0] = effdate;
		elementsText[1] = enddate;
		elementsText[2] = comsnschedset;
		elementsText[3] = reprintreasontext;
		elementsText[4] = generated;
		elementsText[5] = datemailed;
		elementsText[6] = faxsig;
		elementsText[7] = faxexp;
		elementsText[8] = orgsig;
		elementsText[9] = reprint;
		elementsText[10] = stsind;
		
	

		elementsMaxLength[0] = 11;
		elementsMaxLength[1] = 11;
		elementsMaxLength[2] = 11;
		elementsMaxLength[3] = 25; 
		elementsMaxLength[4] = 11;
		elementsMaxLength[5] = 11;
		elementsMaxLength[6] = 15;
		elementsMaxLength[7] = 11; 
		elementsMaxLength[8] = 15;
		elementsMaxLength[9] = 11; 
		elementsMaxLength[10] = 9;// Indicator has lot of spaces to compensate the spaces between the HTML elements above the list 
	
		for(var i = 0 ; i < elementsMaxLength.length; i++) {

			if(elementsText[i].length < elementsMaxLength[i]) {

				for(j = elementsText[i].length ; j < elementsMaxLength[i]; j++)
					elementsText[i]+= " ";							
					
			}
			else
				elementsText[i] = elementsText[i].substring(0, elementsMaxLength[i]);
		}


		//var agrText = elementsText[0] + "-" + elementsText[1] + "-" + elementsText[2] + "-" + elementsText[3] + "-" + elementsText[4] + "-" + elementsText[5] + "-" + elementsText[6] + "-" + elementsText[7] + "-" + elementsText[8] + "-" + elementsText[9] + "-" + elementsText[10];
		var agrText = elementsText[0] + " " + elementsText[1] + " " + elementsText[2] + " " + elementsText[3] + " " + elementsText[4] + " " + elementsText[5] + " " + elementsText[6] + " " + elementsText[7] + " " + elementsText[8] + " " + elementsText[9] + " " + elementsText[10];

		if ( enddate == "" )
			enddate = null;
		if ( reprintreason == "" )
			reprintreason = null;
		if ( generated == "" )
			generated = null;
		if ( datemailed == "" )
			datemailed = null;
		if ( faxsig == "" )
			faxsig = null;
		if ( faxexp == "" )
			faxexp = null;
		if ( orgsig == "" )
			orgsig = null;
		if ( reprint == "" )
			reprint = null;



		var honor = "<%=Agr.getHonorific()%>";
		var mname = "<%=Agr.getMiddleName()%>";
		var suffix = "<%=Agr.getSuffix()%>";

		if ( honor == "null" ) 
			honor = "";
		if ( mname == "null" )
			mname = "";
		if ( suffix == "null" )
			suffix = "";


		if ( enddate == "null" || enddate == "" )
			enddate = "";
		if ( faxsig == "null" || faxsig == "" )
			faxsig = "";


//		document.AgreementsForm.AgrID.value = "<%=Agr.getAgrID()%>";
		



		document.AgreementsForm.AddList.style.visibility = "";

		var agrValues = effdate + "-" + enddate + "-" + comsnschedset + "-" + reprintreason + "-" + generated + "-" + datemailed + "-" + faxsig + "-" + faxexp + "-" + orgsig + "-" + reprint;
		var addoptions = new Option();
		addoptions.text = agrText;
		addoptions.value = agrValues;

		document.AgreementsForm.AddList.options[<%=i%>] = addoptions;		
		document.AgreementsForm.BKRBID.value = "<%=Agr.getBrokerID()%>";	

		var nameValues = "<%=Agr.getHonorific()%>" + ":" + "<%=Agr.getFirstName()%>" + ":" + "<%=Agr.getMiddleName()%>" + ":" + "<%=Agr.getLastName()%>" + ":" + "<%=Agr.getSuffix()%>" + ":" + "<%=Agr.getAgrID()%>" + ":" + "<%=Agr.getStatus()%>" + ":" + stsind;
		listNameValues[<%=i%>] = nameValues;



		document.AgreementsForm.BKRBID.value = "<%=Agr.getBrokerID()%>"

	<%
	}//  end of for loop
	%>


	if ( "<%=session.getAttribute("ErrorMessage")%>" == "Empty" || "<%=session.getAttribute("ErrorMessage")%>" == "null" ) {
	}
	else {

		<%
		if ( session.getAttribute("AgrWithError") != null ) {

			Agr = ( org.kp.broker.vo.AgreementVO ) session.getAttribute("AgrWithError"); 
		
		%>

			document.AgreementsForm.EffectiveDate.value = "<%=Agr.getEffectiveDate()%>";
			document.AgreementsForm.EffectiveDate.disabled = true;
			document.AgreementsForm.EffectiveDate.style.background = "silver";
			
			document.AgreementsForm.EndDate.value = "<%=Agr.getEndDate()%>";
			document.AgreementsForm.Honorific.value = "<%=Agr.getHonorific()%>";
			document.AgreementsForm.FirstName.value = "<%=Agr.getFirstName()%>";
			document.AgreementsForm.MiddleName.value = "<%=Agr.getMiddleName()%>";
			document.AgreementsForm.LastName.value = "<%=Agr.getLastName()%>";
			document.AgreementsForm.Suffix.value = "<%=Agr.getSuffix()%>";
			document.AgreementsForm.AgrID.value = "<%=Agr.getAgrID()%>";
			document.AgreementsForm.AgreementStatus.value = "<%=Agr.getStatus()%>";

			document.AgreementsForm.GenerateReprintReason.value = "<%=Agr.getReprintReason()%>";
			document.AgreementsForm.Generated.value = "<%=Agr.getGenerated()%>";
			document.AgreementsForm.DateMailed.value = "<%=Agr.getDateMailed()%>";
			document.AgreementsForm.FaxSignedReceived.value = "<%=Agr.getFaxSigned()%>";
			document.AgreementsForm.FaxExpiration.value = "<%=Agr.getFaxExpiration()%>";
			document.AgreementsForm.OriginalSignedReceived.value = "<%=Agr.getSigned()%>";
			document.AgreementsForm.LastReprint.value = "<%=Agr.getGenerated()%>";


			var addcomsn = new Option();
			addcomsn.text = "<%=Agr.getComsnSchedSet()%>";
			addcomsn.value = "<%=Agr.getComsnSchedSet()%>";

			document.AgreementsForm.ComsnSchedSet.options[0] = addcomsn;
	
			enableList = true;
			document.AgreementsForm.AddList.style.background = "white";

		<%
		}
		%>


		alert("<%=session.getAttribute("ErrorMessage")%>");
		
		<%
			session.setAttribute("ErrorMessage","Empty");
		%>

	}



   }





//    Function add, modify and manipulate all the functionalities of the list
   function addToList( theForm ) {



	if ( theForm.Honorific.value == "" && theForm.FirstName.value == "" && 
			theForm.MiddleName.value == "" && theForm.LastName.value == "" && theForm.Suffix.value == "" && 
			theForm.EffectiveDate.value == "" && theForm.EndDate.value == "" && theForm.ComsnSchedSet.value == "" && 
			theForm.Generated.value == "" && theForm.DateMailed.value == "" && theForm.FaxSignedReceived.value == "" && 
			theForm.OriginalSignedReceived.value == "" )  {


	}
	else {

	      if ( validate( theForm ) ) {

			document.AgreementsForm.EffectiveDate.disabled = false;
			theForm.TypeChangeKey.value = "FromList";
			theForm.submit();

	     }//  end of if for validation
	}

   }//  end of function addToList



   function deleteFromList( theForm ) {

	if ( theForm.Honorific.value == "" && theForm.FirstName.value == "" && 
			theForm.MiddleName.value == "" && theForm.LastName.value == "" && theForm.Suffix.value == "" && 
			theForm.EffectiveDate.value == "" && theForm.EndDate.value == "" && theForm.ComsnSchedSet.value == "" && 
			theForm.Generated.value == "" && theForm.DateMailed.value == "" && theForm.FaxSignedReceived.value == "" && 
			theForm.OriginalSignedReceived.value == "" )  {


		if ( theForm.AddList.length > 0 )
			alert( '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.SelectRecordToDelete")%>' );
		else
			alert( '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.NoRecordToDelete")%>' );		

		//alert( "An agreement has to be selected first, to be deleted from the list" );
	}
	else {

		if ( theForm.StatusIndicator.value == "D" ) {
			alert('<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.RecordMarkedDelete")%>');
			//alert( "The selected Agreement is already marked for deletion" );
		}
		document.AgreementsForm.EffectiveDate.disabled = false;
		theForm.TypeChangeKey.value = "FromListDelete";
		theForm.submit();

	}



   }


   function checkEffDateOverlapping(theForm) {


	var selectedIndex = "-1";
	var effdate = theForm.EffectiveDate.value;

	var effDateStatus = true;

	for( var m=0; m < theForm.AddList.length; m++ ) {
		if ( theForm.AddList.options[m].selected == true ) {
			selectedIndex = m;
			break;
		}
	}



	for ( var x=0; x<theForm.AddList.length; x++ ) {
		
		if ( selectedIndex != x )  {

			var values = theForm.AddList.options[x].value;

			var temp;
			var count = new Array();
			var splitData = new Array();
		
			var j = 0;
			for (var i=0; i < values.length; i++) {
				temp = "" + values.substring(i, i+1);

				if ( temp == ("-" ) ) {
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

			var oldEffDate = splitData[0];

			if ( effdate == oldEffDate ) {

				alert( "Overlapping in EffectiveDate. Please change the Effective date you have entered" );
				effDateStatus = false;
				break;
			}
		}
	}

	if ( effDateStatus )
		return true;
	else
		return false;
		




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
	var splitNames = new Array();
		
	var j = 0;
	for (var i=0; i < values.length; i++) {
		temp = "" + values.substring(i, i+1);

		if ( temp == ("-" ) ) {
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


	if ( splitData[0] == undefined || splitData[1] == undefined || splitData[2] == undefined ) {
		alert('<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.SelectProperRecord")%>');
		//alert( "Click on the Agreement you want to populate on the fields");
		return false;
	}

	if ( splitData[1] == "null" ) {
		splitData[1] = "";
	}
	if ( splitData[3] == "null" ) {
		splitData[3] = "";
	}

	if ( splitData[4] == "null" ) {
		splitData[4] = "";
	}
	if ( splitData[5] == "null" ) {
		splitData[5] = "";
	}

	if ( splitData[6] == "null" ) {
		splitData[6] = "";
	}
	if ( splitData[7] == "null" ) {
		splitData[7] = "";
	}
	if ( splitData[8] == "null" ) {
		splitData[8] = "";
	}
	if ( splitData[9] == "null" ) {
		splitData[9] = "";
	}



	if ( splitData[3] == "New Document" )
			splitData[3] = "101";
	else if ( splitData[3] == "Signatory Change" )
			splitData[3] = "102";
	else if ( splitData[3] == "Broker Name Change" )
			splitData[3] = "103";
	else if ( splitData[3] == "Commission Schedule Effective Date Change" )
			splitData[3] = "104";
	else if ( splitData[3] == "Commission Schedule Set Change" )
			splitData[3] = "105";
	else if ( splitData[3] == "Lost" )
			splitData[3] = "201";
	else if ( splitData[3] == "Broker Requested Copy" )
			splitData[3] = "202";
	else if ( splitData[3] == "Other" )
			splitData[3] = "299";



	document.AgreementsForm.EffectiveDate.value = splitData[0];
	document.AgreementsForm.EndDate.value = splitData[1];
	//document.AgreementsForm.ComsnSchedSet.value = splitData[2];


	var addcomsn = new Option();
	addcomsn.text = splitData[2];
	addcomsn.value = splitData[2];

	document.AgreementsForm.ComsnSchedSet.options[0] = addcomsn;

	document.AgreementsForm.GenerateReprintReason.value = splitData[3];
	document.AgreementsForm.Generated.value = splitData[4];
	document.AgreementsForm.DateMailed.value = splitData[5];
	document.AgreementsForm.FaxSignedReceived.value = splitData[6];
	document.AgreementsForm.FaxExpiration.value = splitData[7];
	document.AgreementsForm.OriginalSignedReceived.value = splitData[8];
	document.AgreementsForm.LastReprint.value = splitData[9];

	

	var listNameV = listNameValues[listIndex];

	j=0;
	for ( i=0; i < listNameV.length; i++) {
		temp = "" + listNameValues[listIndex].substring(i, i+1);

		if ( temp == (":" ) ) {
			count[j] = i;
			j++;
		}
		
	}
	count[j] = listNameV.length;

	var k = 0;
	for ( i=0; i < listNameV.length; i++ ) {
		splitNames[i] = listNameValues[listIndex].substring( k, count[i] );

		k = count[i]+1;
	}



	if ( splitNames[0] == "null" ) {
		splitNames[0] = "";
	}
	if ( splitNames[2] == "null" ) {
		splitNames[2] = "";
	}
	if ( splitNames[4] == "null" ) {
		splitNames[4] = "";
	}
	if ( splitNames[5] == "" ) {
		splitNames[5] = "0";
	}


	document.AgreementsForm.Honorific.value = splitNames[0];
	document.AgreementsForm.FirstName.value = splitNames[1];
	document.AgreementsForm.MiddleName.value = splitNames[2];
	document.AgreementsForm.LastName.value = splitNames[3];
	document.AgreementsForm.Suffix.value = splitNames[4];
	document.AgreementsForm.AgrID.value = splitNames[5];
	document.AgreementsForm.AgreementStatus.value = splitNames[6];
	document.AgreementsForm.StatusIndicator.value = splitNames[7];


	if ( splitNames[5] > 0 ) {
		document.AgreementsForm.EffectiveDate.disabled = true;
		document.AgreementsForm.EffectiveDate.style.background = "silver";
	}
	else {
		document.AgreementsForm.EffectiveDate.disabled = false;	
		document.AgreementsForm.EffectiveDate.style.background = "white";
	}


	oldNo = true;
	

	}

   }


   function populateComsnSchd( effdate ) {

	var k = 0;
	
	document.AgreementsForm.ComsnSchedSet.length = 0;

	if ( effdate.value != "" ) {

		if ( checkForValidDate( effdate.name, effdate.value) ) {

			var effdt = (effdate.value).substring( 6,10 );
			var newdt="";

			for ( var i=0; i<cmsnset.length; i++ ) {
				newdt = cmsnset[i].substring( 6,10 );

				if ( effdt == newdt ) {

					var addcomsn = new Option();
					addcomsn.text = cmsnset[i];
					addcomsn.value = cmsnset[i];

					document.AgreementsForm.ComsnSchedSet.options[k] = addcomsn;
					k++;	

				}
			}
			if ( document.AgreementsForm.ComsnSchedSet.length < 1 ) {
				alert( '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Agreement.NoCmsnSched")%>' );
				//alert( "Please note that there is no Commission Schedule \n"+
					 //  "for the Effective date you have entered" );
			}
		}
	}


	document.AgreementsForm.ComsnSchedSet.value = "";


   }




	function checkForValidDate(datename, datevalue){


	 	var validdate = "1234567890/";
         	var err=0
         	var psj=0;
	      var a="";

         	a=datevalue;
		
	 	if (a.length != 10) {
			alert(  '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Invalid")%>'+datename );
			return false;
		}
		else {
			for (var i=0; i < a.length; i++) {
			temp = "" + a.substring(i, i+1);
				if (validdate.indexOf(temp) == "-1") {
					alert( '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+datename );
					return false;
				}
			}
		 }

   	       d = a.substring(0, 2)
      	 c = a.substring(2, 3)
         	 b = a.substring(3, 5)
         	 e = a.substring(5, 6)
         	 f = a.substring(6, 10)

 	       //basic error checking

      	 if (d<1 || d>12) {
			alert(  datename + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidMonth")%>' );
			return false;
		 }
         	 if (c != '/' || e != '/' ) {
			alert(  '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Invalid")%>'+datename );
			return false;
		 }
         	 if (b<1 || b>31) {
			alert( datename + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidDate")%>' );
			return false;
		 }
         	 if (f<1900 || f>4000) {
			alert( datename + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidYear")%>' );
			return false;
		 }

         	 // months with 30 days
         	 if (d==4 || d==6 || d==9 || d==11){
             	if (b==31) {
				alert(  '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.30DaysInAMonth")%>'+datename );
				return false;
			}
         	 }

	      // february, leap year
         	 if (d==2){
              	// feb
              	var g=parseInt(f/4)
              	if (isNaN(g)) {
				alert( '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.MonthForLeapYear")%>'+datename );
				return false;

	            }

             	if (b>29) {
				alert( '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.MonthDateNoMatch")%>'+datename );
				return false;
		 	}

             	if (b==29 && ((f/4)!=parseInt(f/4))) {
				alert( '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Invalid")%>'+datename );
				return false;
	       	}
		 }

		return true;

	} // end of checkValidation()




   function enableAll(theForm) {

	var agrid = theForm.AgrID.value;

	if ( agrid != "0" ) {

	   	var totalElements = theForm.elements.length;
		for ( var i = 0 ; i <totalElements ; i++) {
			
			if ( theForm.elements[i].name == "Generated" ||  theForm.elements[i].name == "FaxExpiration" || theForm.elements[i].name == "LastReprint" || theForm.elements[i].type == "button") {
 			}
			else {
				theForm.elements[i].style.background = "white";
				theForm.elements[i].onfocus = null;
			}
		}

		theForm.EffectiveDate.style.disabled = true;
		theForm.EffectiveDate.style.background = "silver";
	}


	enableList = true;
	theForm.AddList.style.background = "white";

   }


   function resetAgrForm(theForm) {

	/*
	var hbkrbid = theForm.BKRBID.value;
	var hagrid = theForm.AgrID.value;
	var hkey = theForm.TypeChangeKey.value;
	var hind = theForm.indicator.value;
	var hcitystzip = theForm.CityStZip.value;
	var hline1 = theForm.Line1.value;
	var hstsind = theForm.StatusIndicator.value;
	*/
	
	theForm.reset();
	populateFields();
	
	/*
	theForm.BKRBID.value = hbkrbid;
	theForm.AgrID.value = hagrid;
	theForm.TypeChangeKey.value = hkey;
	theForm.indicator.value = hind;
	theForm.CityStZip.value = hcitystzip;
	theForm.Line1.value = hline1;
	theForm.StatusIndicator.value = hstsind;
	*/
	
	

   }

   function generateDoc() {

	var agrid = document.AgreementsForm.AgrID.value;
	var docname = document.AgreementsForm.Generated.value;

	var reason = document.AgreementsForm.GenerateReprintReason.value;

	if ( reason != ""  ) {

		if ( agrid < 1 ) {

			if ( document.AgreementsForm.FirstName.value == "" ) {
				alert( '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Agreement.NoValidDataForPrinting")%>' );
				//alert( "No valid data available for printing. Please select the data to be printed" );
			}
			else {
				if ( confirm( '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Agreement.GenerateAgreement")%>') ){

					if ( validate( document.AgreementsForm ) ) {

							document.AgreementsForm.EffectiveDate.disabled = false;
							document.AgreementsForm.TypeChangeKey.value="SubmitPrint";
							document.AgreementsForm.action="AgreementGenerate";
							document.AgreementsForm.submit();
					}
					else
						return false;
				}
			}
		}
		else if ( agrid > 0 && docname == "" ) {

			if ( validate( document.AgreementsForm ) ) {
				document.AgreementsForm.Line1.value = parent.BrokerMain.document.forms[0].Line1.value+"   "+parent.BrokerMain.document.forms[0].MailStop.value;
				document.AgreementsForm.CityStZip.value = parent.BrokerMain.document.forms[0].City.value+"   "+parent.BrokerMain.document.forms[0].State.value+" - "+parent.BrokerMain.document.forms[0].Zip.value;

				document.AgreementsForm.EffectiveDate.disabled = false;
				document.AgreementsForm.action="AgreementGenerate";
				document.AgreementsForm.TypeChangeKey.value="SubmitPrint";
				document.AgreementsForm.submit();
			}
			else {

				return false;
			}
		}
		else if ( agrid > 0 && docname != "" ) {

			alert('<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Agreement.ReprintAgreementPrefix")%>'
					+docname+'.'+'<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Agreement.ReprintAgreementSuffix")%>');
			//alert( "Agreement has already been generated for this Signatory on "+docname+". You can reprint the Agreement by clicking Reprint button");
		}
	}
	else {
		alert('<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Agreement.SelectGenerateReprintReason")%>');
		//alert( "You must select Generate/Reprint Reason to generate an Agreement" );
	}

   }




   function reprintDoc() {

	var agrid = document.AgreementsForm.AgrID.value;
	var docname = document.AgreementsForm.Generated.value;

	var reason = document.AgreementsForm.GenerateReprintReason.value;


	if ( docname == "" && reason == "") {
		alert('<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Agreement.SelectAgreementToReprint")%>');
		//alert( "Select the agreement to be reprinted.");

	}
	else if ( docname == "" ) {
		alert('<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Agreement.GenerateAgreementFirst")%>');
		//alert( "The Agreement has to be generated first");

	}

	else {


		if ( validate( document.AgreementsForm ) ) {

			document.AgreementsForm.EffectiveDate.disabled = false;
			document.AgreementsForm.TypeChangeKey.value="RePrint";
			document.AgreementsForm.action="AgreementGenerate";
			document.AgreementsForm.submit();
		}
		else
			return false;


	}

   }
	
/*
	if ( reason != ""  ) {

		if ( agrid < 1 ) {

			if ( document.AgreementsForm.FirstName.value == "" ) {
				alert( "No valid data available for printing. Please select the data to be printed" );
			}
			else {
				if ( confirm( "Unsaved data has been detected. Generating an Agreement will cause this data to be saved. Do you want to proceed with the generation of Agreement?") ) {

					if ( validate( document.AgreementsForm ) ) {

						document.AgreementsForm.EffectiveDate.disabled = false;
						document.AgreementsForm.TypeChangeKey.value="SubmitPrint";
						document.AgreementsForm.action="AgreementGenerate";
						document.AgreementsForm.submit();
					}
					else
						return false;
				}
			}
		}
		else if ( agrid > 0 && docname == "" ) {

			if ( validate( document.AgreementsForm ) ) {
				document.AgreementsForm.Line1.value = parent.BrokerMain.document.forms[0].Line1.value+"   "+parent.BrokerMain.document.forms[0].MailStop.value;
				document.AgreementsForm.CityStZip.value = parent.BrokerMain.document.forms[0].City.value+"   "+parent.BrokerMain.document.forms[0].State.value+" - "+parent.BrokerMain.document.forms[0].Zip.value;

				document.AgreementsForm.EffectiveDate.disabled = false;
				document.AgreementsForm.action="AgreementGenerate";
				document.AgreementsForm.TypeChangeKey.value="SubmitPrint";
				document.AgreementsForm.submit();
			}
			else {

				return false;
			}
		}
		else if ( agrid > 0 && docname != "" ) {

			alert( "Agreement has already been generated for this Signatory on "+docname+". You can reprint the Agreement by clicking Reprint button");
		}
	}
	else {

		alert( "You must select Generate/Reprint Reason to generate an Agreement" );
	}


*/


</Script>


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
<BODY bgcolor="#0B5F77" OnLoad="setTimeout('populateFields()',1000);">

<FORM name="AgreementsForm" method="POST" action="AgreementsServlet" OnSubmit="return validate(document.AgreementsForm)">


  <table width="95%" border="0" cellspacing="0" cellpadding="2" align="center">
    <tr align="center" valign="middle"> 
      <td> 
        <table width="670" border="0" cellspacing="0" cellpadding="0">
          <tr> 
            <td align="left" width="3" height="20"><img src="limages/tleft3.gif" width="3" height="20"></td>
            <td bgcolor="#E6E9F0" width="332" align="left"><font class="stitle">&nbsp;&nbsp;&nbsp;Agreements</font></td>
            <td bgcolor="#E6E9F0" width="335" align="right"> 
              <input type="button" value="Generate" name="generate" onClick="generateDoc()" onFocus="this.blur()" class="lebotton">
              <input type="button" value="Reprint" name="reprint" onClick="reprintDoc()" class="lebotton">
              <input type="button" value="Edit" name="edit" class="lebotton" OnClick="enableAll(document.AgreementsForm)">
              <input type="button" value="Reset" name="button" OnClick="resetAgrForm(document.AgreementsForm)" class="lebotton">
            </td>
          </tr>
        </table>
        <table width="670" border="0" cellspacing="0" cellpadding="0">
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
            <td width="668"> 
              <table border="0" cellspacing="0" cellpadding="2" align="center" width="100%">
                <tr valign="bottom" align="left">
                  <td align="center" width="50" height="20"><font class="ComTitle">Status</font></td>
                  <td align="center" width="50" height="20"><font class="ComTitle">Honor</font></td>
                  <td align="center" width="75" height="20"><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>First</font></td>
                  <td align="center" width="75" height="20"><font class="ComTitle">Middle</font></td>
                  <td align="center" width="75" height="20"><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Last</font></td>
                  <td align="center" width="50" height="20"><font class="ComTitle">Suffix</font></td>
                  <td align="center" width="50" height="20">&nbsp;</td>
		      <INPUT TYPE="hidden" name="GenerateHidden" value="">
		      <INPUT type="hidden" name="BKRBID" value="">
		      <INPUT type="hidden" name="AgrID" value="0">
		      <INPUT type="hidden" name="TypeChangeKey" value="">
		      <INPUT type="hidden" name="Line1" value="">
		      <INPUT type="hidden" name="CityStZip" value="">
		      <INPUT type="hidden" name="indicator" value="0">
		      <INPUT type="hidden" name="StatusIndicator" value="">
		      <INPUT type="hidden" name="SaveExitPage" value="No">			
                </tr>
                <tr valign="bottom" align="left" bgcolor="#E6E9F0"> 
                  <td valign="middle" align="center" width="50"> 
                    <select name="AgreementStatus" onFocus="this.blur()" class="select1">
                            <OPTION selected></OPTION>
                            <%  
			
			java.util.Vector agrStatusText = new java.util.Vector();
			java.util.Vector agrStatusValue = new java.util.Vector();

			agrStatusText = brokerDropDownVO.getAgreementStatusText();		
			agrStatusValue = brokerDropDownVO.getAgreementStatusValue();		
			
			for(int i = 0 ; i < agrStatusText.size(); i++) {
			
		%>	
				<option value = '<%=agrStatusValue.elementAt(i)%>'><%=agrStatusText.elementAt(i)%></option>
		<%
			}			
		%>
                    </select>
                  </td>
                  <td valign="middle" align="center" width="50"> 
                    <input size="5" type="text" maxlength="10" name="Honorific" class="input2" tabindex="1">
                  </td>
                  <td valign="middle" align="center" width="75"> 
                    <input size="11" type="text" maxlength="25" name="FirstName" class="input2" tabindex="2">
                  </td>
                  <td valign="middle" align="center" width="75"> 
                    <input size="11" type="text" maxlength="25" name="MiddleName" class="input2" tabindex="3">
                  </td>
                  <td valign="middle" align="center" width="75"> 
                    <input size="11" type="text" maxlength="25" name="LastName" class="input2" tabindex="4">
                  </td>
                  <td valign="middle" align="center" width="50"> 
                    <input size="5" type="text" maxlength="20" name="Suffix" class="input2" tabindex="5">
                  </td>
                  <td valign="middle" align="center" width="50"><nobr> <a href="#" tabindex="29" OnClick="return addToList(document.AgreementsForm)" onMouseOver="javascript:add.src = image15.src;" onMouseOut="javascript:add.src = image16.src;"><img tabindex="14" src="limages/add_off.gif" width="50" height="19" border="0" alt="Add" name="add"></a></nobr></td>
                </tr>
              </table>
              <table border="0" cellspacing="0" cellpadding="2" align="center" width="100%">
                <tr valign="bottom" align="center"> 
                  <td width="100" height="20"><font class="ComTitle"><nobr><font style="color:#eb0000;font-size:11px">*</font>Effective Date</nobr></font></td>
                  <td width="100" height="20"><font class="ComTitle">End Date</font></td>
                  <td width="135" height="20"><font class="ComTitle"><nobr><font style="color:#eb0000;font-size:11px">*</font>Comsn Sched Set</nobr></font></td>
                  <td height="20"><font class="ComTitle">Generate/Reprint Report</font></td>
                </tr>
                <tr valign="bottom" align="center" bgcolor="#E6E9F0"> 
                  <td valign="middle" width="100"> 
                    <input size="11" type="text" maxlength="10" name="EffectiveDate" class="input2" tabindex="6" onBlur="populateComsnSchd(document.AgreementsForm.EffectiveDate)">
                  </td>
                  <td valign="middle" width="100"> 
                    <input size="11" type="text" maxlength="10" name="EndDate" class="input2" tabindex="7" >
                  </td>
                  <td valign="middle" width="135"> 
                    <select name="ComsnSchedSet" tabindex="8" class="select2">
                      <option value="">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</option>
                    </select>
                  </td>
                  <td valign="middle"> 
                    <select name="GenerateReprintReason" class="select2" tabindex="9" >
		<%  
			
			java.util.Vector genReasonText = new java.util.Vector();
			java.util.Vector genReasonValue = new java.util.Vector();

			genReasonText = brokerDropDownVO.getGenerateReasonText();		
			genReasonValue = brokerDropDownVO.getGenerateReasonValue();		
			
			for(int i = 0 ; i < genReasonText.size(); i++) {
			
		%>	
				<option value = '<%=genReasonValue.elementAt(i)%>'><%=genReasonText.elementAt(i)%></option>
		<%
			}			
		%>
                    </select>
                  </td>
                </tr>
              </table>  
              <table border="0" cellspacing="0" cellpadding="2" width="100%">
                <tr valign="bottom" align="center"> 
                  <td width="110" height="20"><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Generated</font></td>
                  <td width="80" height="20"><font class="ComTitle"><nobr>Date 
                    Mailed</nobr></font></td>
                  <td width="140" height="20"><font class="ComTitle"><nobr>Fax 
                    Signed/Recieved</nobr></font></td>
                  <td width="100" height="20"><font class="ComTitle"><nobr>Fax 
                    Expiration</nobr></font></td>
                  <td width="130" height="20"><font class="ComTitle"><nobr><font style="color:#eb0000;font-size:11px">*</font>Orig Signed/Recieved</nobr></font></td>
                  <td width="100" height="20"><font class="ComTitle"><nobr>Last 
                    Reprint </font></td>
                </tr>
                <tr valign="bottom" align="center"> 
                  <td valign="middle" width="110" bgcolor="#E6E9F0"> 
                    <input size="11" type="text" maxlength="10" name="Generated" class="input1" style="background-color : silver;" onFocus="this.blur()">
                  </td>
                  <td width="80" valign="middle" bgcolor="#E6E9F0"> 
                    <input size="11" type="text" maxlength="10" name="DateMailed" class="input1" tabindex="10" onFocus="this.blur()">
                  </td>
                  <td width="140" valign="middle" bgcolor="#E6E9F0"> 
                    <input size="11" type="text" maxlength="10" name="FaxSignedReceived" class="input1" tabindex="11"   onFocus="this.blur()">
                  </td>
                  <td width="100" valign="middle" bgcolor="#E6E9F0"> 
                    <input size="11" type="text" maxlength="10" name="FaxExpiration" class="input1" onFocus="this.blur()">
                  </td>
                  <td width="130" valign="middle" bgcolor="#E6E9F0"> 
                    <input size="11" type="text" maxlength="10" name="OriginalSignedReceived" class="input1" tabindex="12"  onFocus="this.blur()">
                  </td>
                  <td width="100" valign="middle" bgcolor="#E6E9F0"> 
                    <input size="11" type="text" maxlength="10" name="LastReprint" class="input1" tabindex="13" onFocus="this.blur()">
                  </td>
                </tr>
              </table>
              <table width="100%" border="0" cellspacing="0" cellpadding="2">
                <tr valign="bottom"> 
                  <td align="center" valign="middle">
                    <table width="100%" border="0" cellspacing="0" cellpadding="2">
                      <tr align="center" valign="bottom"> 
                        <td colspan="7"> 
                          <select size="3" name="AddList" onFocus="this.blur()" onClick="return popAgain( AddList, AddList.value)" class="multiselect3">
                          </select>
                        </td>
                      </tr>
                      <tr align="center" valign="bottom"> 
                        <td colspan="7"><a href="#" OnClick="deleteFromList(document.AgreementsForm)" onMouseOver="javascript:delsel.src = image17.src;" onMouseOut="javascript:delsel.src = image18.src;"><img src="limages/delsel_off.gif" width="138" height="19" border="0" alt="Delete Selected" name="delsel" vspace="0"></a> 
                        </td>
                      </tr>
                    </table>
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