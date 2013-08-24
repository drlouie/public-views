 <!-- Sample HTML file --> <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">

<jsp:useBean id="BkrUtil" class="org.kp.broker.servlets.BrokerUtil" />
<jsp:useBean id="payAmt" class="org.kp.broker.vo.PaymentAmountVO" />

<jsp:useBean id="pay" class="org.kp.broker.vo.PaymentControlVO" />
<jsp:useBean id="brokerDropDownVO" class="org.kp.broker.vo.BrokerDropDownVO" />

<%
	brokerDropDownVO = (org.kp.broker.vo.BrokerDropDownVO)session.getAttribute("DropDowns");
%>

<HTML>
<HEAD>
<META name="GENERATOR" content="IBM WebSphere Page Designer V3.5.3 for Windows">
<TITLE>Payment Controls</TITLE>

<%@ include file="script/ValidatePayment.js" %>


<Script language="JavaScript">

   var oldNo = false;
   var listIndex = 0;

   var listUILength = 0;
   var listUIValues = new Array();
   var listNameValues = new Array();
   var listNameOriginal = new Array();

   var PayDDID = new Array();
   var NameDDID = new Array();

   var enableList = false;

   function disableDDEnroll() {
	document.PaymentControlsForm.DDEnroll.disabled = true;

   }
   
   
   function enableAllFields() {
   
		for ( var i = 0 ; i <document.PaymentControlsForm.elements.length; i++) {
			
			if ( document.PaymentControlsForm.elements[i].name == "MinPaymentDefault" ||  document.PaymentControlsForm.elements[i].name == "PaymentAppDefault" || document.PaymentControlsForm.elements[i].name == "MinPaymentOverride"  || document.PaymentControlsForm.elements[i].name == "PaymentAppOverride"  || document.PaymentControlsForm.elements[i].name == "PaymentMethod" || document.PaymentControlsForm.elements[i].type == "button") {
 			}
			else {
				document.PaymentControlsForm.elements[i].style.background = "white";
				document.PaymentControlsForm.elements[i].disabled = false;
			}
		}
		enableList = true;
		//document.PaymentControlsForm.AddList.style.background = "silver";
   
   }
   
   
   function disableAllFields() {
   
		for ( var i = 0 ; i <document.PaymentControlsForm.elements.length; i++) {
			
			if ( document.PaymentControlsForm.elements[i].name == "MinPaymentDefault" 
				||  document.PaymentControlsForm.elements[i].name == "PaymentAppDefault" 
				|| document.PaymentControlsForm.elements[i].name == "MinPaymentOverride"  
				|| document.PaymentControlsForm.elements[i].name == "PaymentAppOverride"  
				|| document.PaymentControlsForm.elements[i].name == "PaymentMethod" 
				|| document.PaymentControlsForm.elements[i].type == "hidden"
				|| document.PaymentControlsForm.elements[i].type == "button") {
 			}
			else {
				document.PaymentControlsForm.elements[i].style.background = "silver";
				document.PaymentControlsForm.elements[i].disabled = true;
			}
		}
		enableList = false;
   
   
   }
   

   function populateFields() {

	var transtype = "";
	var accttype = "";

//	document.PaymentControlsForm.AddList.style.visibility = "hidden";
	document.PaymentControlsForm.PayID.value = "0";
	disableAllFields();

	document.PaymentControlsForm.BKRBID.value = "<%=session.getAttribute("BIDinSession")%>";

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

	java.util.Vector payVec = (java.util.Vector) session.getAttribute("ModifiedPaymentControl");
	int vecSize = payVec.size();

	for( int i=0; i<vecSize; i++ ) {

		pay = ( org.kp.broker.vo.PaymentControlVO ) payVec.elementAt(i);


	%>
		

		    document.PaymentControlsForm.AddList.style.visibility = "";
			var addoptions = new Option();

			var elementsMaxLength = new Array();
			var elementsText = new Array();
			var elementsValue = new Array();

			elementsText[0] = "<%=pay.getTransactionType()%>";
			elementsText[1] = "<%=pay.getRoutingNo()%>";
			elementsText[2] = "<%=pay.getAccountNo()%>";
			elementsText[3] = "<%=pay.getAccountType()%>";
			elementsText[4] = "<%=pay.getSigned()%>";
			elementsText[5] = "<%=pay.getReceived()%>";
			elementsText[6] = "<%=pay.getSubmitted()%>";
			elementsText[7] = "<%=pay.getPreNote()%>";
			elementsText[8] = "<%=pay.getIndicator()%>";

			elementsMaxLength[0] = 7;
			elementsMaxLength[1] = 10;
			elementsMaxLength[2] = 13;
			elementsMaxLength[3] = 10; 
			elementsMaxLength[4] = 11;
			elementsMaxLength[5] = 11;
			elementsMaxLength[6] = 11;
			elementsMaxLength[7] = 11; 
			elementsMaxLength[8] = 3; 
	
			for(var i = 0 ; i < elementsMaxLength.length; i++) {

				if(elementsText[i].length < elementsMaxLength[i]) {

					for(j = elementsText[i].length ; j < elementsMaxLength[i]; j++)
						elementsText[i]+= " ";							
					
				}
				else
					elementsText[i] = elementsText[i].substring(0, elementsMaxLength[i]);
			}




			addoptions.text = elementsText[0] + " " + elementsText[1] + " " + elementsText[2]+ " " + elementsText[3] + " " + elementsText[4] + " " + elementsText[5] + " " + elementsText[6] + " " + elementsText[7] + " " + elementsText[8];
			addoptions.value = "<%=pay.getTransactionType()%>" + "-" + "<%=pay.getRoutingNo()%>" + "-" + "<%=pay.getAccountNo()%>"+ "-" + "<%=pay.getAccountType()%>" + "-" + "<%=pay.getSigned()%>" + "-" + "<%=pay.getReceived()%>" + "-" + "<%=pay.getSubmitted()%>" + "-" + "<%=pay.getPreNote()%>" + "-" + "<%=pay.getIndicator()%>";

			document.PaymentControlsForm.AddList.options[document.PaymentControlsForm.AddList.options.length] = addoptions;			
	
			listUIValues[listUILength] = addoptions.value;
			listNameValues[listUILength] = "<%=pay.getHonorific()%>" + ":" + "<%=pay.getFirstName()%>" + ":" + "<%=pay.getMiddleName()%>" + ":" + "<%=pay.getLastName()%>" + ":" + "<%=pay.getSuffix()%>" + ":" + "<%=pay.getDirectDepositID()%>" + ":" + "<%=pay.getDocumentName()%>" + ":" +"<%=pay.getPaymentOverride()%>"+ ":" +"<%=pay.getApprovalOverride()%>";

			listNameOriginal[listUILength] = "<%=pay.getHonorific()%>" + "-" + "<%=pay.getFirstName()%>" + "-" + "<%=pay.getMiddleName()%>" + "-" + "<%=pay.getLastName()%>" + "-" + "<%=pay.getSuffix()%>";

			listUILength++;

			//oldNo = true;

			<%
			if( i == 0 ) {
			%>
			
				document.PaymentControlsForm.MinPaymentDefault.value = "<%=pay.getPaymentDefault()%>";
				document.PaymentControlsForm.PaymentAppDefault.value = "<%=pay.getApprovalDefault()%>";				
				
				document.PaymentControlsForm.MinPaymentOverride.value = "<%=pay.getPaymentOverride()%>";
				document.PaymentControlsForm.PaymentAppOverride.value = "<%=pay.getApprovalOverride()%>";
				document.PaymentControlsForm.PaymentMethod[1].checked = true;
				enableAllFields();
				enableList = false;
				document.PaymentControlsForm.AddList.style.background = "silver";

			<%
			}
			%>

	<%
	}
	%>

	document.PaymentControlsForm.TransactionType.value = "";
	document.PaymentControlsForm.AccountType.value = "";

	document.PaymentControlsForm.MinPaymentDefault.value = "<%=session.getAttribute("PayDflt")%>";
	document.PaymentControlsForm.PaymentAppDefault.value = "<%=session.getAttribute("AppDflt")%>";				
	
	document.PaymentControlsForm.MinPaymentOverride.value = "<%=session.getAttribute("PayAmt")%>";
	document.PaymentControlsForm.PaymentAppOverride.value = "<%=session.getAttribute("AppAmt")%>";
	


	if ( "<%=session.getAttribute("AppDflt")%>" != "" ) {
		document.PaymentControlsForm.PaymentAppDefault.value = "<%=BkrUtil.formatDollarAmount(session.getAttribute("AppDflt").toString())%>";
	}

	if ( "<%=session.getAttribute("PayDflt")%>" != "" ) {
		document.PaymentControlsForm.MinPaymentDefault.value = "<%=BkrUtil.formatDollarAmount(session.getAttribute("PayDflt").toString())%>";
	}


	if ( "<%=session.getAttribute("PayAmtErrorMessage")%>" == "null" || "<%=session.getAttribute("PayAmtErrorMessage")%>" == "" ) {
	}
	else {
	
		<%
			if ( session.getAttribute("PayAmtWithError") != null ) {
				payAmt = (org.kp.broker.vo.PaymentAmountVO) session.getAttribute("PayAmtWithError");
		
		%>
		
			
			document.PaymentControlsForm.MinPaymentOverride.value = "<%=payAmt.getPaymentOverride()%>";
			document.PaymentControlsForm.PaymentAppOverride.value = "<%=payAmt.getApprovalOverride()%>";
			
			if ( parent.LeftNav.document.forms[0]!= undefined )
				parent.LeftNav.document.forms[0].indicator.value = "4";	
			

		
		
		<%
			}
			
		%>
	
		alert( "<%=session.getAttribute("PayAmtErrorMessage")%>" );	
	}
	
	
	
	
	document.PaymentControlsForm.MinPaymentOverride.focus();

   }


   function submitForm() {

		document.PaymentControlsForm.AddList.disabled = false;
		document.PaymentControlsForm.TransactionType.disabled = false;
		document.PaymentControlsForm.AccountType.disabled = false;


	if (validate ( document.PaymentControlsForm ) ) {

		document.PaymentControlsForm.TypeChangeKey.value = "Submit";
		document.PaymentControlsForm.submit();
	}

   }

   function AddToList(theForm) {



	if ( theForm.AddList.length < 1 ) {

		var paytypelength = theForm.PaymentMethod.length;
		var paytype="";

		for ( var i=0; i < paytypelength; i++ ) {
	
			if (theForm.PaymentMethod[i].checked) {
				paytype = theForm.PaymentMethod[i].value;
				break;
			}
		}

		if ( paytype != "Check" ) {	


			if ( theForm.Honorific.value == "" && theForm.FirstName.value == "" && theForm.LastName.value == "" && 
				theForm.MiddleName.value == "" && theForm.Suffix.value == "" &&  theForm.TransactionType.value == "" && 
			 	theForm.RoutingNo.value == "" &&  theForm.AccountType.value == "" &&  theForm.AccountNo.value == "" && 
		 		theForm.SignedDate.value == "" &&  theForm.ReceivedDate.value == "" &&  theForm.EcomDate.value == "" && 
		 		theForm.PreNoteDate.value == "" ) {

			}
			else {
	
				if (validate ( document.PaymentControlsForm ) ) {


					if ( checkForDuplicateAccount() ) {

						var payid = document.PaymentControlsForm.PayID.value;

						if ( payid == "" )
							document.PaymentControlsForm.PayID.value = "0";

						document.PaymentControlsForm.TypeChangeKey.value = "FromList";
						document.PaymentControlsForm.submit();
					}
				}

			}//end of else
	
		}
	
	}
	else {
	
		var payID = document.PaymentControlsForm.PayID.value;
		
		if ( payID == "" || payID == 0 ) {
			alert('<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Payment.DDSetup")%>');
			//alert( "Only one Direct Deposit setup is allowed" );
		}
		else {
		
	
			if (validate ( document.PaymentControlsForm ) ) {

				document.PaymentControlsForm.TypeChangeKey.value = "FromList";
				document.PaymentControlsForm.submit();

			}
		
		}
			
	}

   }


   function deleteFromList(theForm) {

	var paytypelength = theForm.PaymentMethod.length;
	var paytype="";

	for ( var i=0; i < paytypelength; i++ ) {
	
		if (theForm.PaymentMethod[i].checked) {
			paytype = theForm.PaymentMethod[i].value;
			break;
		}
	}

	if ( paytype != "Check" ) {	


	if ( theForm.Honorific.value == "" && theForm.FirstName.value == "" && theForm.LastName.value == "" && 
		theForm.MiddleName.value == "" && theForm.Suffix.value == "" &&  theForm.TransactionType.value == "" && 
		 theForm.RoutingNo.value == "" &&  theForm.AccountType.value == "" &&  theForm.AccountNo.value == "" && 
		 theForm.SignedDate.value == "" &&  theForm.ReceivedDate.value == "" &&  theForm.EcomDate.value == "" && 
		 theForm.PreNoteDate.value == "" ) {


		if ( theForm.AddList.length > 0 )
			alert('<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.SelectRecordToDelete")%>');
		else
			alert('<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.NoRecordToDelete")%>');

	}
	else {

		if ( theForm.StatusIndicator.value == "D" ) {
			alert('<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.RecordMarkedDelete")%>');
			theForm.TypeChangeKey.value = "FromListDelete";
			theForm.submit();

		}
		else {

			theForm.TypeChangeKey.value = "FromListDelete";
			theForm.submit();
		}
	
	}
	
	}

   }


   function checkForDuplicateAccount() {

	var selectedIndex = "-1";
	var addListLength = document.PaymentControlsForm.AddList.options.length;

	for( var m=0; m < addListLength; m++ ) {
		if ( document.PaymentControlsForm.AddList.options[m].selected == true ) {
			selectedIndex = m;
			break;
		}
	}

	var accno = document.PaymentControlsForm.AccountNo.value;

	var NewAccNo = "";
	var PayValues = "";
	var PayStatus = true;

	var splitData = new Array();
       
	for ( var k=0; k<addListLength; k++ ) {
		
	
		if ( selectedIndex != k )  {

			PayValues = document.PaymentControlsForm.AddList.options[k].value;

			var j = 0;
			var count = new Array();
			for (var i=0; i < PayValues.length; i++) {
				temp = "" + PayValues.substring(i, i+1);

				if ( temp == ("-" ) ) {
					count[j] = i;
					j++;
				}
		
			}
			count[j] = PayValues.length;

			var x = 0;
			for ( i=0; i < count.length; i++ ) {
				splitData[i] = PayValues.substring( x, count[i] );
				x = count[i]+1;
			}
	
			NewAccNo = splitData[2];

			if ( accno == NewAccNo ) {
				var message = '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Payment.DuplicateDDSetup")%>';
				alert( message );
				PayStatus = false;
				break;
			}
		}

	}

	if ( PayStatus)
		return true;
	else
		return false;

   }



   function checkDDForm( paymentmethod ) {

	if ( paymentmethod == "DirectDeposit" ) {
		document.PaymentControlsForm.DDEnroll.disabled = "";
    	}
	else
		document.PaymentControlsForm.DDEnroll.disabled = true;

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
	
	
	if ( splitData[1] == undefined || splitData[2] == undefined || splitData[3] == undefined) {
	
		alert('<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.SelectProperRecord")%>');
		//alert( "Click the record you want to populate in the fields" );
	}
	else {	
			
			
			
			if ( splitData[0] == "Add" ) {
				document.PaymentControlsForm.TransactionType.options[0].selected = true;
			}
			else if ( splitData[0] == "Change" ) {
				document.PaymentControlsForm.TransactionType.options[1].selected = true;
			}
			else if ( splitData[0] == "Delete" ) {
				document.PaymentControlsForm.TransactionType.options[2].selected = true;
			}
		
			document.PaymentControlsForm.RoutingNo.value = splitData[1];
			document.PaymentControlsForm.AccountNo.value = splitData[2];
		
			if ( splitData[3] == "Checking" ) {
				document.PaymentControlsForm.AccountType.options[0].selected = true;
			}
			else if ( splitData[3] == "Savings" ) {
				document.PaymentControlsForm.AccountType.options[1].selected = true;
			}
		
			document.PaymentControlsForm.SignedDate.value = splitData[4];
			document.PaymentControlsForm.ReceivedDate.value = splitData[5];
			document.PaymentControlsForm.EcomDate.value = splitData[6];
			document.PaymentControlsForm.PreNoteDate.value = splitData[7];
			document.PaymentControlsForm.StatusIndicator.value = splitData[8];
		
		
		
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
			if ( splitNames[4] == "null" ) {
				splitNames[4] = "";
			}
		
		
			document.PaymentControlsForm.Honorific.value = splitNames[0];
			document.PaymentControlsForm.FirstName.value = splitNames[1];
			document.PaymentControlsForm.MiddleName.value = splitNames[2];
			document.PaymentControlsForm.LastName.value = splitNames[3];
			document.PaymentControlsForm.Suffix.value = splitNames[4];
			document.PaymentControlsForm.PayID.value = splitNames[5];	
			document.PaymentControlsForm.DocumentName.value = splitNames[6];
			//document.PaymentControlsForm.MinPaymentOverride.value = splitNames[7];
			//document.PaymentControlsForm.PaymentAppOverride.value = splitNames[8];
		
		
		
			/*
			if ( splitNames[6] == "DIRDPST" )
				document.PaymentControlsForm.PaymentMethod[1].checked = 1;
			else 
				document.PaymentControlsForm.PaymentMethod[0].checked = 1;
			*/
			oldNo = true;
		}

	}
	
   }


   function resetPayForm(theForm) {

	var paytypelength = theForm.PaymentMethod.length;
	var paytype="";

	for ( var i=0; i < paytypelength; i++ ) {
	
		if (theForm.PaymentMethod[i].checked) {
			paytype = theForm.PaymentMethod[i].value;
			break;
		}
	}


	var paydflt = theForm.MinPaymentDefault.value;
	var appdflt = theForm.PaymentAppDefault.value;

	if ( paytype != "Check" ) {	


		var hbkrbid = theForm.BKRBID.value;
		var hline1 = theForm.Line1.value;
		var hcitystzip = theForm.CityStZip.value;
		var hpayid = theForm.PayID.value;
		var hdocname = theForm.DocumentName.value;
		var hkey = theForm.TypeChangeKey.value;
		var hind = theForm.indicator.value;
		var stsind = theForm.StatusIndicator.value;


		theForm.reset();



		theForm.BKRBID.value = hbkrbid;
		//theForm.Line1.value = hline1;
		//theForm.CityStZip.value = hcitystzip;
		theForm.PayID.value = 0;//hpayid;
		//theForm.DocumentName.value = hdocname;
		//theForm.TypeChangeKey.value = hkey;
		//theForm.indicator.value = hind;
		//theForm.StatusIndicator.value = stsind;
		theForm.TransactionType.value = "";
		theForm.AccountType.value = "";
		theForm.PaymentMethod[1].checked = true;

		
	}
	
	theForm.MinPaymentDefault.value = paydflt;
	theForm.PaymentAppDefault.value = appdflt;
	theForm.MinPaymentOverride.value = "<%=session.getAttribute("PayAmt")%>";
	theForm.PaymentAppOverride.value = "<%=session.getAttribute("AppAmt")%>";
	

   }


   function enablePayForm(theForm) {

	var payid = theForm.PayID.value;
	
	var paytypelength = theForm.PaymentMethod.length;
	var paytype="";

	for ( var i=0; i < paytypelength; i++ ) {
	
		if (theForm.PaymentMethod[i].checked) {
			paytype = theForm.PaymentMethod[i].value;
			break;
		}
	}

	//if ( payid != "0" ) {
	if ( paytype != "Check" ) {	

	   	var totalElements = theForm.elements.length;
		for ( var i = 0 ; i <totalElements ; i++) {
			
			if ( theForm.elements[i].name == "MinPaymentDefault" ||  theForm.elements[i].name == "PaymentAppDefault" || theForm.elements[i].name == "MinPaymentOverride"  || theForm.elements[i].name == "PaymentAppOverride"  || theForm.elements[i].name == "PaymentMethod" || theForm.elements[i].type == "button") {
 			}
			else {
				theForm.elements[i].style.background = "white";
				theForm.elements[i].onfocus = null;
			}
		}
		
		enableList = true;
		theForm.AddList.style.background = "white";
	}

   }

   function genDoc() {



	var payid = document.PaymentControlsForm.PayID.value;
	var paytypelength = document.PaymentControlsForm.PaymentMethod.length;
	var paytype="";

	var docname = document.PaymentControlsForm.DocumentName.value;

	for ( var i=0; i < paytypelength; i++ ) {
	
		if (document.PaymentControlsForm.PaymentMethod[i].checked) {
			paytype = document.PaymentControlsForm.PaymentMethod[i].value;
			break;
		}
	}

	if ( paytype == "DirectDeposit" ) {




		if ( payid < 1 ) {

			if ( document.PaymentControlsForm.FirstName.value == "" ) {
				alert('<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Payment.NoValidDataForPrinting")%>');
				//alert( "No valid data available for printing. Please select the data to be printed" );
			}
			else {
			
				if ( document.PaymentControlsForm.AddList.length < 1 ) {
			
				if ( confirm( '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Payment.DDEnrollment")%>') ) {

					if ( validate( document.PaymentControlsForm ) ) {

						document.PaymentControlsForm.TypeChangeKey.value="SubmitPrint";
						document.PaymentControlsForm.action="DDEnrollment";
						document.PaymentControlsForm.submit();
					}
					else
						return false;
				}
				else {


				}
				
				}
				else {
					
					var AddListLength = document.PaymentControlsForm.AddList.length;
					var ListValue = false;
					
					for ( var i=0; i < AddListLength; i++ ) {
	
						if (document.PaymentControlsForm.AddList.options[i].selected) {
							ListValue = true;
							break;
						}
					}

					if ( ListValue ) {

						if ( validate( document.PaymentControlsForm ) ) {

							document.PaymentControlsForm.TypeChangeKey.value="SubmitPrint";
							document.PaymentControlsForm.action="DDEnrollment";
							document.PaymentControlsForm.submit();
						}
						else
							return false;
					}
					else
						alert( '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Payment.DDSetup")%>');
					
					
				}
			}
		}
		else {
		
			if ( document.PaymentControlsForm.FirstName.value == "" || document.PaymentControlsForm.LastName.value == "" ) {
				alert('<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Payment.NoValidDataForPrinting")%>');
				//alert( "No valid data available for printing. Please select the data to be printed" );
			}
			else {

			if ( validate( document.PaymentControlsForm ) ) {
				document.PaymentControlsForm.Line1.value = parent.BrokerMain.document.forms[0].Line1.value+"   "+parent.BrokerMain.document.forms[0].MailStop.value;
				document.PaymentControlsForm.CityStZip.value = parent.BrokerMain.document.forms[0].City.value+"   "+parent.BrokerMain.document.forms[0].State.value+" - "+parent.BrokerMain.document.forms[0].Zip.value;

				document.PaymentControlsForm.action="DDEnrollment";
				document.PaymentControlsForm.TypeChangeKey.value="SubmitPrint";
				document.PaymentControlsForm.submit();
			}
			else {

				return false;
			}
			}
		}
	}
	else {

		alert('<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Payment.PayMethodDD")%>');
		//alert( "Payment Method should be Direct Deposit to generate DD Enrollment Form" );
	}

   }

</Script>


<!--Dynamic CSS Javascript-->
<script language="javascript" src="script/common_css.js"></script>



<script language="Javascript">
<!--
//MOUSEOVER IMAGE PRELOAD

//mreset
// // // MOUSE OVER
image1 = new Image();
image1.src = "limages/sreset_ov.gif";
// // // MOUSE OFF
image2 = new Image();
image2.src = "limages/sreset_off.gif";

//medit
image3 = new Image();
image3.src = "limages/sedit_ov.gif";
image4 = new Image();
image4.src = "limages/sedit_off.gif";

//-->
</script>


</HEAD>
<BODY bgcolor="#0B5F77" OnLoad="setTimeout('populateFields()',500)">

<FORM name="PaymentControlsForm" method="POST" action="PaymentControlsServlet" OnSubmit="submitForm()">



  <table width="95%" border="0" cellspacing="0" cellpadding="2" align="center">
    <tr align="center" valign="middle"> 
      <td> 
        <table width="670" border="0" cellspacing="0" cellpadding="0">
          <tr> 
            <td align="left" width="3" height="20"><img src="limages/tleft3.gif" width="3" height="20"></td>
            <td bgcolor="#E6E9F0" width="332" align="left"><font class="stitle">&nbsp;&nbsp;&nbsp;Payment 
              Controls </font></td>
            <td bgcolor="#E6E9F0" width="335" align="right"> 
              <input type="button" value="DD Enroll Form" name="DDEnroll" class="lebotton" onClick="return genDoc()">
              <input type="button" value="Edit" name="edit" class="lebotton" onClick="enablePayForm(document.PaymentControlsForm)">
              <input type="button" value="Reset" name="button" onClick="resetPayForm(document.PaymentControlsForm)" class="lebotton">
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
              <table cellspacing="0" cellpadding="0" bordercolor="#E6E9F0" border="1">
                <tbody> 
                <tr> 
                  <td width="150" bgcolor="#E6E9F0">&nbsp;</td>
                  <td valign="bottom" width="150" bgcolor="#E6E9F0" align="center"><font class="stitle">Minimum 
                    Payment</font></td>
                  <td valign="bottom" bgcolor="#E6E9F0" align="center" width="150"><font class="stitle">Payment 
                    Approval</font></td>
                  <td valign="bottom" align="center" bgcolor="#E6E9F0" width="218"><font class="stitle">Payment 
                    Method</font></td>
                </tr>
                <tr> 
                  <td align="right" width="150" bgcolor="#E6E9F0"><font class="stitle">Default</font></td>
                  <td width="150" align="center"> 
                    <input size="10" type="text" maxlength="10" name="MinPaymentDefault" class="input1" readonly>
                  </td>
                  <td align="center" width="150"> 
                    <input class="input1" size="10" type="text" maxlength="10" name="PaymentAppDefault" readonly>
                  </td>
                  <td rowspan="2" colspan="4" align="center"><font class="ComTitle"><nobr><input type="radio" name="PaymentMethod" value="Check" checked tabindex="3" onClick="checkDDForm(this.value);disableAllFields()"><font class="ComTitle">Check&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="radio" name="PaymentMethod" value="DirectDeposit" onClick="checkDDForm(this.value);enableAllFields()" class="ComTitle">Direct Deposit</nobr></font>
		<INPUT type="hidden" name="BKRBID" value="<%=session.getAttribute("BIDinSession")%>">
		<INPUT type="hidden" name="Line1" value="">
		<INPUT type="hidden" name="CityStZip" value="">
		<INPUT type="hidden" name="PayID" value="">
		<INPUT type="hidden" name="DocumentName" value="">
		<INPUT type="hidden" name="TypeChangeKey" value=""> 
		<INPUT type="hidden" name="indicator" value="0">
		<INPUT type="hidden" name="StatusIndicator" value="">
		<INPUT type="hidden" name="SaveExitPage" value="No">	
                  </td>
                </tr>
                <tr> 
                  <td align="right" width="150" bgcolor="#E6E9F0"><font class="stitle">Override 
                    $</font></td>
                  <td width="150" align="center"> 
                    <input class="input2" size="10" type="text" maxlength="10" name="MinPaymentOverride" tabindex="1">
                  </td>
                  <td align="center" width="150"> 
                    <input class="input2" size="10" type="text" maxlength="10" name="PaymentAppOverride" tabindex="2">
                  </td>
                </tr>
                </tbody> 
              </table>
              <table cellspacing="0" cellpadding="0">
                <tbody> 
                <tr valign="bottom"> 
                  <td width="125" height="25"></td>
                  <td  align="center" width="50" height="25"><font class="ComTitle">Honor</font></td>
                  <td  align="center" width="100" height="25"><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>First</font></td>
                  <td  align="center" width="100" height="25"><font class="ComTitle">Middle</font></td>
                  <td  align="center" width="100" height="25"><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Last</font></td>
                  <td  align="center" width="100" height="25"><font class="ComTitle">Suffix</font></td>
                  <td  align="center" width="98" height="25">&nbsp;</td>
                </tr>
                <tr bgcolor="#E6E9F0"> 
                  <td width="125" align="center" ><font class="stitle">Signatory 
                    -></font></td>
                  <td  align="center" width="50"> 
                    <input size="4" type="text" maxlength="10" name="Honorific" tabindex="4" class="input1">
                  </td>
                  <td width="100" align="center"> 
                    <input class="input1" size="10" type="text" maxlength="30" name="FirstName" tabindex="5">
                  </td>
                  <td width="100" align="center"> 
                    <input class="input1" size="10" type="text" maxlength="10" name="MiddleName" tabindex="6">
                  </td>
                  <td width="100" align="center"> 
                    <input class="input1" size="10" type="text" maxlength="30" name="LastName" tabindex="7">
                  </td>
                  <td width="100" align="center"> 
                    <input class="input1" size="10" type="text" maxlength="10" name="Suffix" tabindex="8">
                  </td>
                  <td width="98">&nbsp;</td>
                </tr>
                </tbody> 
              </table>
              <table cellspacing="1" cellpadding="0">
                <tbody> 
                <tr valign="bottom"> 
                  <td  align="center" height="25"><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>TransType</font></td>
                  <td  align="center" height="25"><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Routing#</font></td>
                  <td  align="center" height="25"><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Account #</font></td>
                  <td  align="center" height="25"><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Acct Type</font></td>
                  <td  align="center" height="25"><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Signed</font></td>
                  <td  align="center" height="25"><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Received</font></td>
                  <td  align="center" height="25"><font class="ComTitle">Submitted</font></td>
                  <td  align="center" height="25"><font class="ComTitle">Pre-note</font></td>
                  <td width="100" height="25" align="center"> 
                    <input type="button" value="  Add   " name="Add" class="lebotton" OnClick="AddToList(document.PaymentControlsForm)">
                  </td>
                </tr>
                <tr> 
                  <td align="center"> 
                    <select name="TransactionType" tabindex="9" class="select1">
                      <option value="A" selected>Add</option>
                      <option value="C">Change</option>
                      <option value="D">Delete</option>
                    </select>
                  </td>
                  <td align="center">
                    <input class="input1" size="11" type="text" maxlength="9" name="RoutingNo" tabindex="10">
                  </td>
                  <td align="center">
                    <input class="input1" size="11" type="text" maxlength="16" name="AccountNo" tabindex="11">
                  </td>
                  <td align="center"> 
                    <select name="AccountType" tabindex="12" class="select1">
		<% 
			
			java.util.Vector payAcctTypeText = new java.util.Vector();			
			java.util.Vector payAcctTypeValue = new java.util.Vector();

			payAcctTypeText = brokerDropDownVO.getPayAcctText();									
			payAcctTypeValue = brokerDropDownVO.getPayAcctValue();		
						
			for(int i = 0 ; i < payAcctTypeText.size(); i++) {
		%>
								
				<OPTION value="<%=payAcctTypeValue.elementAt(i)%>"><%=payAcctTypeText.elementAt(i)%></OPTION>
		<%
			}
		%>
                    </select>
                  </td>
                  <td>
                    <input class="input1" size="11" type="text" maxlength="10" name="SignedDate" tabindex="13">
                  </td>
                  <td align="center">
                    <input class="input1" size="11" type="text" maxlength="10" name="ReceivedDate" tabindex="14">
                  </td>
                  <td align="center">
                    <input class="input1" size="11" type="text" maxlength="10" name="EcomDate" tabindex="15">
                  </td>
                  <td align="center">
                    <input class="input1" size="11" type="text" maxlength="10" name="PreNoteDate" tabindex="16">
                  </td>
                  <td width="100" align="center"> 
                    <input type="button" value="Delete" name="Delete" class="lebotton" onClick="deleteFromList(document.PaymentControlsForm)"></td>
                </tr>
                </tbody> 
              </table>
              <select size="3" name="AddList"  OnClick="return popAgain( AddList, this.form.AddList.value)" OnKeyPress="return popAgain( AddList, this.form.AddList.value)" OnKeyUp="return popAgain( AddList, this.form.AddList.value)" OnKeyDown="return popAgain( AddList, this.form.AddList.value)" class="multiselect2">
              </select>
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