<!-- Sample JSP file --> <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">

<jsp:useBean id="purDropDownVO" class="org.kp.purchaser.vo.PurchaserDropDownVO" />
<% purDropDownVO = (org.kp.purchaser.vo.PurchaserDropDownVO)session.getAttribute("PurchaserDropDown");%>

<jsp:useBean id="amdInfoVO" class="org.kp.purchaser.vo.AmendmentInformationVO" />
<jsp:useBean id="amdPayeeVO" class="org.kp.purchaser.vo.AmendmentPayeeVO" />
<jsp:useBean id="euCmsnVO" class="org.kp.purchaser.vo.EUNonStdComsnSchdVO" />
<jsp:useBean id="amdAddrVO" class="org.kp.broker.vo.AddressVO" />
<jsp:useBean id="amdAgrVO" class="org.kp.broker.vo.AgreementVO" />
<jsp:useBean id="amdVO" class="org.kp.purchaser.vo.AmendmentVO" />

<jsp:useBean id="amdUtil" class="org.kp.purchaser.servlets.AmendmentUtil" />

<%
	amdInfoVO = (org.kp.purchaser.vo.AmendmentInformationVO) session.getAttribute("ModifiedAmendmentInfo");
%>

<HTML>
<HEAD>
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

.readonlyfields {
	background-color: silver;

	}

.listbox {
	COLOR : #000000; 
	font-family: Courier New;
	}


-->
</STYLE>
<TITLE>PUR 106 Administer Purchaser(Amendment)</TITLE>

<Script src="script/ValidateAmendment.js">
</Script>

<Script language="JavaScript">


	var AgrArray = new Array();
	var AgrStatusArray = new Array();

	var listIndex = 0;		

	function enableButtons(){
		document.Amendments.DateMailed.style.background = "white";				
		document.Amendments.DateMailed.onfocus = "";
		
		document.Amendments.FaxSignedReceived.style.background = "white";				
		document.Amendments.FaxSignedReceived.onfocus="";				
		
		document.Amendments.OrigSignedReceived.style.background = "white";		
		document.Amendments.OrigSignedReceived.onfocus="";
	}
	
	function disableButtons(){
		document.Amendments.DateMailed.style.background = "silver";				
		document.Amendments.DateMailed.blur();
		
		document.Amendments.FaxSignedReceived.style.background = "silver";				
		document.Amendments.FaxSignedReceived.blur();				
		
		document.Amendments.OrigSignedReceived.style.background = "silver";		
		document.Amendments.OrigSignedReceived.blur();
	}

	
	function editList() {
		document.Amendments.AmendmentList.style.background = "white";
	}

	function populateValues() {
	
		if(parent.tops.document.forms[0] != undefined )
			parent.tops.document.PurTop.dynamic.value = "PUR106 Administer Purchaser (Amendment)";
		document.forms[0].NonStandardComsnSched.style.visibility = "hidden";
		document.forms[0].AmendmentList.style.visibility = "hidden";
		
		document.forms[0].PayeeBID.value = "";
		document.forms[0].GenerateReprintReason.value = "";
		document.forms[0].AssociatedAgreement.value = "";
	
		populatePayeeBID();
		//populateNonStandardComsnSched();


	
	}
	
	function populatePayeeBID() {

		document.forms[0].PayeeBID.options.length = 0;

		<%
			java.util.Vector payeeVec = new java.util.Vector();
			if ( amdInfoVO.getAmendmentPayee() != null )
			payeeVec = amdInfoVO.getAmendmentPayee();
			
			for( int i=0; i<payeeVec.size(); i++ ) {
				amdPayeeVO = (org.kp.purchaser.vo.AmendmentPayeeVO) payeeVec.elementAt(i);
				
				//System.out.println( "Payee BID: "+amdPayeeVO.getPayeeBID() );
		%>
				var addoptions = new Option();
				addoptions.text = "<%=amdPayeeVO.getPayeeBID()%>";
				addoptions.value = "<%=amdPayeeVO.getPayeeBID()%>";
				
				document.forms[0].PayeeBID.options[document.forms[0].PayeeBID.options.length] = addoptions;
		<%
			}
			
			if ( payeeVec.size() < 1 ) {
		%>
				var addoptions = new Option();
				addoptions.text = "        ";
				addoptions.value = "";
				document.forms[0].PayeeBID.options[0] = addoptions;
		<%
			}
		%>		
		
		document.forms[0].PayeeBID.value = "";
		
		<%
			if ( session.getAttribute("PayeeBIDSelected") != null ) {
		%>	
				populatePayeeInfo(document.forms[0]);
		<%	
			}
		%>
			
			
	
	
	}
	


	function populatePayeeInfo(theForm) {
	
		<%
		
		java.util.Vector payeeInfoVec = new java.util.Vector();
		if ( amdInfoVO.getAmendmentPayee() != null )
			payeeInfoVec = amdInfoVO.getAmendmentPayee();
			
		for( int i=0; i<payeeInfoVec.size(); i++ ) {
				
			amdPayeeVO = (org.kp.purchaser.vo.AmendmentPayeeVO) payeeInfoVec.elementAt(i);
			//System.out.println( "Payee BID selected: "+amdPayeeVO.getPayeeBID() );
		
			if ( session.getAttribute("PayeeBIDSelected") != null ) {
		
		%>

				if ( "<%= amdPayeeVO.getPayeeBID() %>" == "<%=session.getAttribute("PayeeBIDSelected").toString()%>" ) {
				
				
					<%
						java.util.Vector euVec = new java.util.Vector();
						if ( amdPayeeVO.getEUNonStandardPrd() != null )
						euVec = amdPayeeVO.getEUNonStandardPrd();
						
						for( int m=0; m<euVec.size(); m++ ) {
							euCmsnVO = (org.kp.purchaser.vo.EUNonStdComsnSchdVO) euVec.elementAt(m);
							
					%>
							document.forms[0].NonStandardComsnSched.style.visibility = "";
							
							var addoptions = new Option();
							addoptions.text = "<%=euCmsnVO.getEUInfo()%>"+"  "+"<%=euCmsnVO.getComsnSchd()%>"+"  "+"<%=euCmsnVO.getPurchasedProduct()%>";
							addoptions.value = "<%=euCmsnVO.getEUInfo()%>"+"  "+"<%=euCmsnVO.getComsnSchd()%>"+"  "+"<%=euCmsnVO.getPurchasedProduct()%>";
							
							document.forms[0].NonStandardComsnSched.options[document.forms[0].NonStandardComsnSched.options.length] = addoptions;
					<%
						}
					%>
							
				
				
					theForm.PayeeBID.value = "<%= amdPayeeVO.getPayeeBID() %>";
					theForm.PayeeName.value = "<%= amdPayeeVO.getPayeeName() %>";
					theForm.PayeeStatus.value = "<%= amdPayeeVO.getPayeeStatus() %>";

					<% amdAddrVO = amdPayeeVO.getAddress();	%>

					theForm.Line1.value = "<%= amdAddrVO.getLine1() %>";
					theForm.Line2.value = "<%= amdAddrVO.getLine2() %>";
					theForm.Line3.value = "<%= amdAddrVO.getLine3() %>";
					theForm.MailStop.value = "<%= amdAddrVO.getMailStop() %>";															
					theForm.City.value = "<%= amdAddrVO.getCity() %>";
					theForm.State.value = "<%= amdAddrVO.getState() %>";
					theForm.Zip.value = "<%= amdAddrVO.getZip() %>";
					theForm.Country.value = "<%= amdAddrVO.getCountry() %>";
					theForm.County.value = "<%= amdAddrVO.getCounty() %>";
					theForm.Province.value = "<%= amdAddrVO.getProvince() %>";	
					
					
					//Populating Agreement for the PayeeBID
					<% 
					
						java.util.Vector agrVec = new java.util.Vector();
						
						if ( amdPayeeVO.getAgreement() != null )
							agrVec = amdPayeeVO.getAgreement();
						
						for ( int j=0; j<agrVec.size(); j++ ) {						
						
							amdAgrVO = (org.kp.broker.vo.AgreementVO) agrVec.elementAt(j);
							
					%>
					
							var agrEffDate = "<%=amdAgrVO.getEffectiveDate()%>";
							var agrEndDate = "<%=amdAgrVO.getEndDate()%>";
							var agrID = "<%=amdAgrVO.getAgrID()%>";
							var agrSgnIK = "<%=amdAgrVO.getSgnIK()%>";
							var agrSts = "<%=amdAgrVO.getStatus()%>";
							var agrHonor = "<%=amdAgrVO.getHonorific()%>";
							var agrFname = "<%=amdAgrVO.getFirstName()%>";
							var agrMname = "<%=amdAgrVO.getMiddleName()%>";
							var agrLname = "<%=amdAgrVO.getLastName()%>";
							var agrSfx = "<%=amdAgrVO.getSuffix()%>";
							
							
							var agrValue = agrEffDate;
							
							if ( agrEndDate != "" )
								agrValue = agrEffDate + " to "+agrEndDate;
								
							AgrArray[<%=j%>] = agrValue;
							
							var AgrStatusValue = "<%=amdAgrVO.getStatus()%>";
							AgrStatusArray[<%=j%>] = AgrStatusValue;

							var addAgr = new Option();
							addAgr.text = agrValue;
							addAgr.value = agrEffDate+":"+agrEndDate+":"+agrID+":"+agrSgnIK+":"+agrSts+":"+agrHonor+":"+agrFname+":"+agrMname+":"+agrLname+":"+agrSfx;
							
							theForm.AssociatedAgreement.options[theForm.AssociatedAgreement.options.length] = addAgr;
										
							<%
								if ( amdUtil.checkDateRange(amdAgrVO.getEffectiveDate(), amdAgrVO.getEndDate()) ) {
							%>				
									theForm.AssociatedAgreement.options[theForm.AssociatedAgreement.options.length-1].selected = true;
									
									theForm.AgreementStatus.value = "<%=amdAgrVO.getStatus()%>";
									theForm.Honorific.value = "<%=amdAgrVO.getHonorific()%>";
									theForm.FirstName.value = "<%=amdAgrVO.getFirstName()%>";
									theForm.MiddleName.value = "<%=amdAgrVO.getMiddleName()%>";
									theForm.LastName.value = "<%=amdAgrVO.getLastName()%>";
									theForm.Suffix.value = "<%=amdAgrVO.getSuffix()%>";
									theForm.AgrID.value = "<%=amdAgrVO.getAgrID()%>";
									theForm.SgnIK.value = "<%=amdAgrVO.getSgnIK()%>";
									theForm.AgrEffDate.value = "<%=amdAgrVO.getEffectiveDate()%>";
									theForm.AgrEndDate.value = "<%=amdAgrVO.getEndDate()%>";
									
							
							
							<%
								}
								else {
							%>

									theForm.AssociatedAgreement.value = "";

							<%
								}

								if ( session.getAttribute("AgrIDSelected") != null ) {
								
									int AgrID = Integer.parseInt(session.getAttribute("AgrIDSelected").toString());
									
									if ( amdAgrVO.getAgrID() == AgrID ) {
							%>
							
										theForm.AssociatedAgreement.options[theForm.AssociatedAgreement.options.length-1].selected = true;
										theForm.AgreementStatus.value = "SatValue: "+"<%=amdAgrVO.getStatus()%>";
										
										
						
							<%
							
									}
								}
							%>
						

					<%
						}
					%>
					
					
					//Populating Amendment based on the PayeeBID
					<% 
				
						java.util.Vector amdVec = new java.util.Vector();
										
						if ( amdPayeeVO.getAmendment() != null )
							amdVec = amdPayeeVO.getAmendment();
							
						for ( int k=0; k<amdVec.size(); k++ ) {						
											
							amdVO = (org.kp.purchaser.vo.AmendmentVO) amdVec.elementAt(k);
											
							
							//if ( amdAgrVO.getAgrID() == amdVO.getAgrID() ) {
					%>
										


								//alert( "inside the IF loop of AMD "+"<%=k%>" );
								
								var elementsMaxLength = new Array();
								var elementsText = new Array();
								var elementsValue = new Array();
						
						
								elementsText[0] = "<%=amdVO.getEffectiveDate()%>";
								elementsText[1] = "<%=amdVO.getEndDate()%>";
								elementsText[2] = "<%=amdVO.getGenerateReprintReason()%>";
								elementsText[3] = "<%=amdVO.getGeneratedDate()%>";
								elementsText[4] = "<%=amdVO.getReprintDate()%>";
								elementsText[5] = "<%=amdVO.getDateMailed()%>";
								elementsText[6] = "<%=amdVO.getFaxSignedReceivedDate()%>";
								elementsText[7] = "<%=amdVO.getFaxExpirationDate()%>";
								elementsText[8] = "<%=amdVO.getOriginalSignedReceivedDate()%>";
								elementsText[9] = "<%=amdVO.getIndicator()%>";

								elementsMaxLength[0] = 11;
								elementsMaxLength[1] = 11;
								elementsMaxLength[2] = 30;
								elementsMaxLength[3] = 11; 
								elementsMaxLength[4] = 11;
								elementsMaxLength[5] = 11;
								elementsMaxLength[6] = 13;
								elementsMaxLength[7] = 13; 
								elementsMaxLength[8] = 13;
								elementsMaxLength[9] = 6; 

							
								for(var i = 0 ; i < elementsMaxLength.length; i++) {
						
									if(elementsText[i].length < elementsMaxLength[i]) {
						
										for(j = elementsText[i].length ; j < elementsMaxLength[i]; j++)
											elementsText[i]+= " ";							
											
									}
									else
										elementsText[i] = elementsText[i].substring(0, elementsMaxLength[i]);
								}
								
								
								
								var amdText = elementsText[0] + "  " + elementsText[1] + "  " + elementsText[2] + "  " + elementsText[3] + "  " + elementsText[4] + "  " + elementsText[5] + "  " + elementsText[6] + "  " + elementsText[7] + "  " + elementsText[8] + "  " + elementsText[9];
								//var amdValue = "<%=amdVO.getEffectiveDate()%>"+":"+"<%=amdVO.getEndDate()%>"+":"+"<%=amdVO.getHonorific()%>"+":"+"<%=amdVO.getFirstName()%>"+":"+"<%=amdVO.getMiddleName()%>"+":"+"<%=amdVO.getLastName()%>"+":"+"<%=amdVO.getSuffix()%>"+":"+"<%=amdVO.getAmdID()%>"+":"+"<%=amdVO.getAgrID()%>"+":"+"<%=amdVO.getStatus()%>"+":"+"<%=amdVO.getIndicator()%>";
								var amdValue = "<%=amdVO.getEffectiveDate()%>"+":"+"<%=amdVO.getEndDate()%>"+":"+"<%=amdVO.getGenerateReprintReasonCode()%>"+":"+
												"<%=amdVO.getGeneratedDate()%>"+":"+"<%=amdVO.getReprintDate()%>"+":"+"<%=amdVO.getDateMailed()%>"+":"+
												"<%=amdVO.getFaxSignedReceivedDate()%>"+":"+"<%=amdVO.getFaxExpirationDate()%>"+":"+"<%=amdVO.getOriginalSignedReceivedDate()%>"+":"+
												"<%=amdVO.getHonorific()%>"+":"+"<%=amdVO.getFirstName()%>"+":"+"<%=amdVO.getMiddleName()%>"+":"+"<%=amdVO.getLastName()%>"+":"+"<%=amdVO.getSuffix()%>"+":"+
												"<%=amdVO.getAmdID()%>"+":"+"<%=amdVO.getAgrID()%>"+":"+"<%=amdVO.getStatus()%>"+":"+"<%=amdVO.getIndicator()%>";
								
								var addAmd = new Option();
								addAmd.text = amdText;
								addAmd.value = amdValue;
								
								theForm.AmendmentList.options[theForm.AmendmentList.options.length] = addAmd;
								theForm.AmendmentList.style.visibility = "";
								
										
					<%		
							//}
						}
					%>

					
					

				}
		<%
			}
		}
		%>
		
		if ( "<%=session.getAttribute("AmdErrorMessage")%>" == "Empty" || "<%=session.getAttribute("AmdErrorMessage")%>" == "null" ) {
		}
		else {
	
			<%
			if ( session.getAttribute("AmdWithError") != null ) {
	
				amdVO = ( org.kp.purchaser.vo.AmendmentVO ) session.getAttribute("AmdWithError"); 
			
			%>
	
	
				theForm.EffectiveDate.value = "<%=amdVO.getEffectiveDate()%>";
				theForm.EndDate.value = "<%=amdVO.getEndDate()%>";
				theForm.Honorific.value = "<%=amdVO.getHonorific()%>";
				theForm.FirstName.value = "<%=amdVO.getFirstName()%>";
				theForm.MiddleName.value = "<%=amdVO.getMiddleName()%>";
				theForm.LastName.value = "<%=amdVO.getLastName()%>";
				theForm.Suffix.value = "<%=amdVO.getSuffix()%>";
				theForm.AmdAgrID.value = "<%=amdVO.getAgrID()%>";
				theForm.AmdID.value = "<%=amdVO.getAmdID()%>";
				theForm.AmendmentStatus.value = "<%=amdVO.getStatus()%>";
				theForm.AgrEffDate.value = "<%=amdVO.getAgrEffDate()%>";
				theForm.AgrEndDate.value = "<%=amdVO.getAgrEndDate()%>";

				theForm.GenerateReprintReason.value = "<%=amdVO.getGenerateReprintReasonCode()%>";
				theForm.Generated.value = "<%=amdVO.getGeneratedDate()%>";
				theForm.LastReprint.value = "<%=amdVO.getReprintDate()%>";
				theForm.DateMailed.value = "<%=amdVO.getDateMailed()%>";
				theForm.FaxSignedReceived.value = "<%=amdVO.getFaxSignedReceivedDate()%>";
				theForm.FaxExpiration.value = "<%=amdVO.getFaxExpirationDate()%>";
				theForm.OrigSignedReceived.value = "<%=amdVO.getOriginalSignedReceivedDate()%>";

				populateAssociatedAgrValues(theForm);
				
				selectedAmdpopulatedWithError(theForm);
	
			<%
			}
			%>
	
	
			alert("Please correct the following error(s):\n"+"<%=session.getAttribute("AmdErrorMessage")%>");
			
	
		}

		
	}
	
	
	function selectPayeeInfo(theForm) {
	
		theForm.SelectedAction.value = "SelectPayee";
		theForm.submit();
	}
	
	
	
	
	function populateAssociatedAgrValues(theForm) {
	
		
		var agrIDFromAmd = theForm.AmdAgrID.value;
			

		for ( var agrVal=0; agrVal<theForm.AssociatedAgreement.length; agrVal++ ) {


			var agrValues = theForm.AssociatedAgreement.options[agrVal].value;
		
			var temp;
		
			var count = new Array();
			var splitData = new Array();
				
			var j = 0;
			
			for (var i=0; i < agrValues.length; i++) {
				temp = "" + agrValues.substring(i, i+1);
		
				if ( temp == (":" ) ) {
					count[j] = i;
					j++;
				}
				
			}
			count[j] = agrValues.length;
		
			var k = 0;
			for ( i=0; i < count.length; i++ ) {
				splitData[i] = agrValues.substring( k, count[i] );
		
				k = count[i]+1;
			}
		
		
			if ( splitData[2] == agrIDFromAmd ) {
			
				theForm.AssociatedAgreement.options[agrVal].selected = true;
				
				theForm.AgrEffDate.value = splitData[0];
				theForm.AgrEndDate.value = splitData[1];				
				theForm.AgrID.value = splitData[2];
				theForm.AgreementStatus.value = splitData[4];

				
				//need to populate SgnIk, AgrID etc.,
				break;
			
			}	
		
		
		
		
		}			
	
	
	}
	
	
	function populateAmdFields(theForm) {

		var listValues = theForm.AmendmentList.value;
		var listLength = theForm.AmendmentList.length;
	
		for( var m=0; m < listLength; m++ ) {
			if ( theForm.AmendmentList.options[m].selected == true ) {
				listIndex = m;
				break;
			}
		}
	
	
		var temp;
	
		var count = new Array();
		var splitData = new Array();
		//var splitNames = new Array();
			
		var j = 0;
		for (var i=0; i < listValues.length; i++) {
			temp = "" + listValues.substring(i, i+1);
	
			if ( temp == (":" ) ) {
				count[j] = i;
				j++;
			}
			
		}
		count[j] = listValues.length;
	
		var k = 0;
		for ( i=0; i < count.length; i++ ) {
			splitData[i] = listValues.substring( k, count[i] );
	
			k = count[i]+1;
		}
	
	
		if ( splitData[0] == undefined || splitData[1] == undefined || splitData[2] == undefined ) {
		
			alert( "Click on the Amendment you want to populate in the fields");
			return false;
		}
		else {
		
			/*
			if ( splitData[10] == "A" ) {
				alert( "Selected Amendment is VOIDED and it cannot be modified" );
				theForm.AmendmentList.options[m].selected = "";
			}
			else {
			*/
			


			
				theForm.EffectiveDate.value = splitData[0];
				theForm.EndDate.value = splitData[1];
				theForm.GenerateReprintReason.value = splitData[2];
				theForm.Generated.value = splitData[3];
				theForm.LastReprint.value = splitData[4];
				theForm.DateMailed.value = splitData[5];
				theForm.FaxSignedReceived.value = splitData[6];
				theForm.FaxExpiration.value = splitData[7];
				theForm.OrigSignedReceived.value = splitData[8];


				theForm.Honorific.value = splitData[9];
				theForm.FirstName.value = splitData[10];
				theForm.MiddleName.value = splitData[11];
				theForm.LastName.value = splitData[12];
				theForm.Suffix.value = splitData[13];
				theForm.AmdID.value = splitData[14];
				theForm.AmdAgrID.value = splitData[15];
				theForm.AmendmentStatus.value = splitData[16];
				theForm.Indicator.value = splitData[17];
				
				/*
				if ( theForm.Indicator.value == "A" ) {
				
					theForm.AmendmentStatus.style.background = "yellow";
				
				}
				*/
				
				populateAssociatedAgrValues(theForm);
				
				
				if ( theForm.AmdID.value > 0 && theForm.Generated.value != "" && theForm.Indicator.value != "A") {
					enableButtons();					
				}
				else {
					disableButtons();
				}
			//}
		
		}
		
	
	
	}
	
	
	function populateAssociatedAgr(theForm) {
	

		var agrIDFromAmd = theForm.AmdAgrID.value;
			
		var agrValues = theForm.AssociatedAgreement.value;
		
		var temp;
		
		var count = new Array();
		var splitData = new Array();
				
		var j = 0;
			
		for (var i=0; i < agrValues.length; i++) {
			temp = "" + agrValues.substring(i, i+1);
		
			if ( temp == (":" ) ) {
				count[j] = i;
				j++;
			}
				
		}
		count[j] = agrValues.length;
		
		var k = 0;
		for ( i=0; i < count.length; i++ ) {
			splitData[i] = agrValues.substring( k, count[i] );
			k = count[i]+1;
		}
		
		theForm.AgrEffDate.value = splitData[0];
		theForm.AgrEndDate.value = splitData[1];
		theForm.AgrID.value = splitData[2];
		theForm.AgreementStatus.value = splitData[4];
		theForm.Honorific.value = splitData[5];
		theForm.FirstName.value = splitData[6];
		theForm.MiddleName.value = splitData[7];		
		theForm.LastName.value = splitData[8];
		theForm.Suffix.value = splitData[9];
		
		//need to populate sgnIk, AgrID, EffDate, EndDate etc.,	
		
	}



	function addAmendment( theForm ) {
	
		
		if ( theForm.AmendmentStatus.value != "Void" && theForm.Indicator.value != "A") {
		
			if ( validateAmendment(theForm) ) {
			
				theForm.SelectedAction.value = "Add";
				theForm.submit();	
			}
		}
		else {
		
			if ( confirm( "Amendment being added is voided/archived. Adding this amendment will create a new record. Do you want to continue?") ) {

				if ( validateAmendment(theForm) ) {
					theForm.AmdID.value = "0";
					theForm.AmendmentStatus.value = "";	
					theForm.GenerateReprintReason.value = "";
					theForm.Generated.value = "";
					theForm.LastReprint.value = "";
					theForm.DateMailed.value = "";
					theForm.FaxSignedReceived.value = "";
					theForm.FaxExpiration.value = "";
					theForm.OrigSignedReceived.value = "";
						
					theForm.SelectedAction.value = "Add";
					theForm.submit();	
				}

			
			}
			else {
			
				populateValues();	
			}
		}
	
	
	}


	function deleteAmendment( theForm ) {
	
		if ( theForm.PayeeBID.value == "" )
			alert( "Select a Payee BID for which you want to delete an Amendment");		
		else if ( theForm.AssociatedAgreement.value == "" || theForm.EffectiveDate.value == "" )
			alert( "An Amendment has to be selected first, to be deleted from the list");
		else {
			theForm.SelectedAction.value = "Delete";
			theForm.submit();	
		}
	
	}
	
	
   function generateDocument(theForm) {

		var amdid = theForm.AmdID.value;
		var docname = theForm.Generated.value;

		var reason = theForm.GenerateReprintReason.value;

		if ( theForm.AmendmentStatus.value == "Void" ) {
			alert( "Cannot generate an Amendment for a Voided Record" );
			return false;
		}



		if ( reason != ""  ) {
	
			if ( amdid < 1 ) {
	
				if ( theForm.FirstName.value == "") {
					alert( "No valid data available for generating an Amendment. Please select the Amendment to be generated" );
				}
				else {
					if ( confirm( "Unsaved data has been detected. Generating an Amendment will cause this data to be saved. Do you want to proceed with the generation of Amendment?") ) {
	
						if ( validateAmendment(theForm) ) {
								
								theForm.SelectedAction.value="GenerateNew";
								theForm.action="AmendmentGenerate";
								theForm.submit();
						}
						else
							return false;
					}
				}
			}
			else if ( amdid > 0 && docname == "" ) {
	
				if ( validateAmendment(theForm) ) {

					theForm.action="AmendmentGenerate";
					theForm.SelectedAction.value="GenerateOld";
					theForm.submit();
				}
				else {
	
					return false;
				}
			}
			else if ( amdid > 0 && docname != "" ) {
					alert( "Amendment has already been generated for this Signatory on "+docname+". You can reprint the Amendment by clicking Reprint button");
			}
		}
		else {
			alert( "You must select Generate/Reprint Reason to generate an Amendment" );
		}

   }



   function reprintDocument(theForm) {

	var amdid = theForm.AmdID.value;
	var docname = theForm.Generated.value;

	var reason = theForm.GenerateReprintReason.value;


	if ( docname == "" && reason == "") {
		//alert('<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Agreement.SelectAgreementToReprint")%>');
		alert( "Select the Amendment to be reprinted.");

	}
	else if ( docname == "" ) {
		//alert('<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Agreement.GenerateAgreementFirst")%>');
		alert( "The Amendment has to be generated first");

	}

	else {


		if ( validateAmendment( theForm ) ) {

			theForm.SelectedAction.value="Reprint";
			theForm.action="AmendmentGenerate";
			theForm.submit();
		}
		else
			return false;


	}

   }



	function selectedAmdpopulatedWithError(theForm) {


		var listLength = theForm.AmendmentList.length;
	
		for( var m=0; m < listLength; m++ ) {

			var listValues = theForm.AmendmentList.options[m].value;

	
			var temp;
		
			var count = new Array();
			var splitData = new Array();
			//var splitNames = new Array();
				
			var j = 0;
			for (var i=0; i < listValues.length; i++) {
				temp = "" + listValues.substring(i, i+1);
		
				if ( temp == (":" ) ) {
					count[j] = i;
					j++;
				}
				
			}
			count[j] = listValues.length;
		
			var k = 0;
			for ( i=0; i < count.length; i++ ) {
				splitData[i] = listValues.substring( k, count[i] );
		
				k = count[i]+1;
			}
		
		
			if ( splitData[7] == theForm.AmdID.value ) {
			
				theForm.AmendmentList.options[m].selected = true;
				break;
			
			}
		}		
	
	
	}

	
	
</Script>
</HEAD>
<BODY bgcolor="#999999" OnLoad="populateValues()">
<FORM name="Amendments" method="POST" action="AmendmentServlet" target="_parent">
<TABLE width="1131">
  <TBODY>
    <TR>
      <TD bgcolor="#999999">
            <TABLE border="1" width="1126">
        <TBODY>
          <TR>
            <TD class="title">
                        <TABLE width="1106">
              <TBODY>
                <TR>
                                    <TD align="right" class="label" valign="middle">Amendment Status
                  <INPUT type="hidden" name="FromWhere" value="0">
                  <INPUT type="hidden" name="WhereToGo" value="">
                  <INPUT type="hidden" name="SelectedAction" value="Save">
                  <INPUT type="hidden" name="AmdID" value="0">
                  <INPUT type="hidden" name="AmdAgrID" value="0">              
                  <INPUT type="hidden" name="AgrID" value="0">                  
                  <INPUT type="hidden" name="SgnIK" value="0"> 
                  <INPUT type="hidden" name="AgrEffDate" value="">
                  <INPUT type="hidden" name="AgrEndDate" value="">
                  <INPUT type="hidden" name="Indicator" value="">
                  </TD>
                                    <TD align="left"><INPUT size="20" type="text" maxlength="20" name="AmendmentStatus" readonly class="readonlyfields"></TD>
                                    <TD align="right" class="label" width="130">Payee Status</TD>
                                    <TD width="252"><INPUT size="41" type="text" maxlength="20" name="PayeeStatus" class="readonlyfields" readonly></TD>
                                    <TD width="150"></TD>
                                    <TD align="center" width="71"><INPUT size="20" type="button" maxlength="20" name="Generate" value="Generate" class="pbttn" OnClick="generateDocument(document.Amendments)"></TD>
                                    <TD align="center" width="76"><INPUT size="20" type="button" maxlength="20" name="Reprint" value="Reprint" class="pbttn" OnClick="reprintDocument(document.Amendments)"></TD>
                  <TD align="center" width="42"><INPUT size="20" type="button" maxlength="20" name="Edit" value="Edit" class="pbttn" onClick="editList()"></TD>
                  <TD align="center" width="60"><INPUT size="20" type="button" maxlength="20" name="Reset" value="Reset" class="pbttn" OnClick="selectPayeeInfo(document.forms[0])"></TD>
                <!--
                  <TD><IMG src="images/generate.gif" width="86" height="22" border="0" alt="Generate"></TD>
                  <TD><IMG src="images/reprint.gif" width="86" height="22" border="0" alt="Reprint"></TD>
                  <TD><IMG src="images/edit.gif" width="50" height="22" border="0" alt="Edit"></TD>
                  <TD><IMG src="images/reset.gif" width="50" height="22" border="0" alt="Reset"></TD>
                -->
                </TR>
                <TR>
                  <TD align="right" class="label">Payee BID</TD>
                  <TD align="left">
                  	<SELECT name="PayeeBID" OnChange="selectPayeeInfo(document.forms[0])">
                  		<!--<OPTION value="">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</OPTION>-->
                  	</SELECT>
                  </TD>
                                    <TD align="right" class="label" width="130">Payee Name</TD>
                                    <TD colspan="6"><INPUT size="83" type="text" maxlength="60" name="PayeeName" class="readonlyfields" readonly></TD>
                                </TR>
              </TBODY>
            </TABLE>
                        <FONT color="#cc0033">Amendment Authorized Signatory</FONT>
            <TABLE cellpadding="1" cellspacing="1">
              <TBODY>
                <TR>
                  <TD></TD>
                  <TD align="center" class="label">Honor</TD>
                  <TD align="center" class="label">First</TD>
                  <TD align="center" class="label">Middle</TD>
                  <TD align="center" class="label">Last</TD>
                  <TD align="center" class="label">Suffix</TD>
                </TR>
                <TR>
                  <TD class="label" align="right">Name</TD>
                  <TD align="center"><INPUT size="10" type="text" maxlength="10" name="Honorific"></TD>
                  <TD align="center"><INPUT size="30" type="text" maxlength="30" name="FirstName"></TD>
                  <TD align="center"><INPUT size="20" type="text" maxlength="20" name="MiddleName"></TD>
                  <TD align="center"><INPUT size="30" type="text" maxlength="30" name="LastName"></TD>
                  <TD align="center"><INPUT size="20" type="text" maxlength="20" name="Suffix"></TD>

                </TR>
                <!--
                <TR>
                  <TD class="label" align="right"></TD>
                  <TD colspan="5"></TD>
                </TR>
                -->
              </TBODY>
            </TABLE>
            <TABLE>
                            <TBODY>
                <TR>
                  <TD valign="top" height="188">
                                    <TABLE cellpadding="1" cellspacing="1">
                    <TBODY>
                      <TR>
                                                <TD align="center" class="label" valign="middle">Associated Agreement</TD>
                                                <TD align="center" class="label">Agreement Status</TD>
                      </TR>
                      <TR>
                        <TD align="center">
                        <SELECT name="AssociatedAgreement" OnChange="populateAssociatedAgr(document.forms[0])"></SELECT></TD>
                        <TD align="center"><INPUT name="AgreementStatus" class="readonlyfields" type="text" readonly size="15"></TD>
                      </TR>
                      <TR>
                        <TD colspan="2" height="135">
                                                <TABLE border="1" width="304">
                          <TBODY>
                            <TR>
                              <TD class="title"><FONT color="#cc0033">Non-Standard Commission Schedules(s)</FONT><BR>
                              <TABLE cellpadding="1" cellspacing="1">
                                <TBODY>
                                  <TR>
                                    <TD class="label">EU</TD>
                                    <TD class="label">Comsn Schedule</TD>
                                    <TD class="label">Purchased Product</TD>
                                  </TR>
		                          <TR>
									<TD colspan="3"><SELECT size="5" name="NonStandardComsnSched" class="readonlyfields"></SELECT>
				            		</TD>
								  </TR>
                                </TBODY>
                              </TABLE>
                              </TD>
                            </TR>
                          </TBODY>
                        </TABLE>
                                                </TD>
                      </TR>
                    </TBODY>
                  </TABLE>
                                    </TD>
                  <TD valign="top" width="554" height="188">
                  <TABLE border="1">
                    <TBODY>
                      <TR>
                        <TD class="title"><FONT color="#cc0033">Amendment Address</FONT><BR>
                                                <TABLE cellpadding="1" cellspacing="1">
                          <TBODY>
                            <TR>
                              <TD class="label" align="right">Line1</TD>
                                                            <TD colspan="6"><INPUT size="40" type="text" maxlength="40" name="Line1" class="readonlyfields" readonly></TD>
                                                            <TD class="label" valign="middle" align="center">M/S</TD>
                                                            <TD><INPUT size="15" type="text" maxlength="20" name="MailStop" class="readonlyfields" readonly></TD>
                            </TR>
                            <TR>
                              <TD class="label" align="right">Line2</TD>
                                                            <TD colspan="8"><INPUT size="40" type="text" maxlength="40" name="Line2" class="readonlyfields" readonly></TD>
                                                        </TR>
                            <TR>
                              <TD class="label" align="right">Line3</TD>
                                                            <TD colspan="8"><INPUT size="40" type="text" maxlength="40" name="Line3" class="readonlyfields" readonly></TD>
                                                        </TR>
                            <TR>
                              <TD class="label" align="right">City</TD>
                                                            <TD colspan="8"><INPUT size="40" type="text" maxlength="40" name="City" class="readonlyfields" readonly></TD>
                                                        </TR>
                            <TR>
                              <TD class="label" align="right">State</TD>
                              <TD class="label" align="left"><INPUT size="3" type="text" maxlength="2" name="State" class="readonlyfields" readonly>
                              </TD>
                              <TD class="label" align="right">Zip</TD>
                                                            <TD></TD>
                                                            <TD><INPUT size="11" type="text" maxlength="10" name="Zip" class="readonlyfields" readonly></TD>
                              <TD align="right" class="label">Country</TD>
                              <TD class="label" align="left"><INPUT size="5" type="text" maxlength="3" name="Country" class="readonlyfields" readonly>
                              </TD>
                              <TD colspan="2"></TD>
                            </TR>
                            <TR>
                                                            <TD colspan="3" align="center" class="label">County</TD>
                                                            <TD colspan="3"><INPUT size="23" type="text" maxlength="20" name="County" class="readonlyfields" readonly></TD>
                                                            <TD align="right" class="label">Province</TD>
                              <TD colspan="2"><INPUT size="20" type="text" maxlength="20" name="Province" class="readonlyfields" readonly></TD>
                            </TR>
                          </TBODY>
                        </TABLE>
                                                </TD>
                      </TR>
                    </TBODY>
                  </TABLE>
                  </TD>
                </TR>
              </TBODY>
                        </TABLE>
                        <TABLE cellpadding="1" cellspacing="1">
              <TBODY>
                <TR>
                  <TD align="center" class="label">Effective Date</TD>
                  <TD align="center" class="label">End Date</TD>
                  <TD align="center" class="label">Generate/Reprint Reason</TD>
                  <TD align="center" class="label">Generated</TD>
                  <TD align="center" class="label">Last Reprint</TD>
                  <TD align="center" class="label">Date Mailed</TD>
                  <TD align="center" class="label">Fax <BR>
                                    Signed/Received</TD>
                  <TD align="center" class="label">Fax <BR>
                                    Expiration</TD>
                                    <TD align="center" class="label" colspan="2">Orig Signed/Received</TD>
                                    <TD></TD>
				                    <TD align="center"><INPUT size="6" type="button" maxlength="10" name="Delete" value="Delete" class="pbttn"  OnClick="deleteAmendment(document.forms[0])"></TD>                                                                        
                                    <!--<TD><IMG src="images/delete.gif" width="55" height="22" border="0" alt="Delete"></TD>-->
                </TR>
                <TR>
                  <TD align="center"><INPUT size="10" type="text" maxlength="10" name="EffectiveDate"></TD>
                  <TD align="center"><INPUT size="10" type="text" maxlength="10" name="EndDate"></TD>
                  <TD align="center">
                  	<SELECT name="GenerateReprintReason">
						<%  java.util.Hashtable ht = new java.util.Hashtable();
    						ht = purDropDownVO.getGenerateReason();
    						java.util.Enumeration enum = ht.keys();
    						String name = "";
    						while ( enum.hasMoreElements() ) {
					            name = enum.nextElement().toString();
            
			            %>
			            <OPTION value="<%=name%>" ><%=ht.get(name).toString()%></OPTION>
						<%  }  %>
					</SELECT>
				  </TD>
                  <TD align="center"><INPUT size="10" type="text" maxlength="10" name="Generated" style="background-color : silver;" onfocus="this.blur()"></TD>
                  <TD align="center"><INPUT size="10" type="text" maxlength="10" name="LastReprint" style="background-color : silver;" onfocus="this.blur()"></TD>
                  <TD align="center"><INPUT size="10" type="text" maxlength="10" name="DateMailed" style="background-color : silver;" onfocus="this.blur()"></TD>
                  <TD align="center"><INPUT size="10" type="text" maxlength="10" name="FaxSignedReceived" style="background-color : silver;" onfocus="this.blur()"></TD>
                  <TD align="center"><INPUT size="10" type="text" maxlength="10" name="FaxExpiration" style="background-color : silver;" onfocus="this.blur()"></TD>
                  <TD align="center" colspan="2"><INPUT size="10" type="text" maxlength="10" name="OrigSignedReceived" style="background-color : silver;" onfocus="this.blur()"></TD>
				  <TD class="label">Indicator</TD>
				  <TD align="center"><INPUT size="20" type="button" maxlength="20" name="Add" value="  Add  " class="pbttn"  OnClick="addAmendment(document.forms[0])"></TD>                                    
                                    <!--<TD><IMG src="images/add.gif" width="56" height="22" border="0" alt="Add"></TD>-->
                </TR>
              </TBODY>
            </TABLE>
            
            		<SELECT size="3" name="AmendmentList" OnClick="populateAmdFields(document.forms[0])" OnKeyDown="populateAmdFields(document.forms[0])" OnKeyUp="populateAmdFields(document.forms[0])" OnKeyPress="populateAmdFields(document.forms[0])" class="listbox"></SELECT>
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