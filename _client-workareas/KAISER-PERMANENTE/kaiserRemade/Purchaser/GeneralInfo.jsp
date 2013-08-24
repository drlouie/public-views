<!-- Sample JSP file --> <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML>
<jsp:useBean id="purVO" class="org.kp.purchaser.vo.PurchaserVO" />
<jsp:useBean id="catPurVO" class="org.kp.purchaser.vo.PurchaserVO" />
<jsp:useBean id="addrVO" class="org.kp.purchaser.vo.AddressVO" />
<jsp:useBean id="purDropDownVO" class="org.kp.purchaser.vo.PurchaserDropDownVO" />
<jsp:useBean id="catVO" class="org.kp.purchaser.vo.CommissionCategoryVO" />
<jsp:useBean id="rdVO" class="org.kp.purchaser.vo.RequiredDocumentVO" />
<jsp:useBean id="phnVO" class="org.kp.purchaser.vo.PhoneVO" />
<jsp:useBean id="purInitVO" class="org.kp.purchaser.vo.PurchaserInitialVO" />
<jsp:useBean id="ownerVO" class="org.kp.purchaser.vo.OwnerRepresentativeVO" />
<jsp:useBean id="rDocVO" class="org.kp.purchaser.vo.RequiredDocumentVO" />
<%
    purVO = (org.kp.purchaser.vo.PurchaserVO)session.getAttribute("ModifiedPurchaserInfo");
    purDropDownVO = (org.kp.purchaser.vo.PurchaserDropDownVO)session.getAttribute("PurchaserDropDown");
    catPurVO = (org.kp.purchaser.vo.PurchaserVO)session.getAttribute("ModifiedCategory");
    purInitVO = purVO.getPurchaserInitial();
    addrVO = purVO.getAddress();
    phnVO = purVO.getPhone();
    ownerVO = purVO.getOwnerRepresentative();
    java.util.Vector rDoc  =  new java.util.Vector();
    rDoc = purVO.getRequiredDocuments();
   
%>
<HEAD>
<META name="GENERATOR" content="IBM WebSphere Page Designer V3.5.3 for Windows">
<META http-equiv="Content-Style-Type" content="text/css">
<STYLE>
<!--
.label {
	COLOR : #0033FF; 
	font-family: arial,verdana,sans-serif;
	font-size : 11px;
	font-weight : bold;
	font-style: normal;	
	}

.input {
	COLOR : #0033FF; 
	font-family: arial,verdana,sans-serif;
	font-size : 12px;
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
.test{
	font-family: arial,verdana,sans-serif;
	font-size:11px;
	font-weight : bold;
	background: #999999;
	border-bottom: 0px solid #104A7B;
	border-right: 0px solid #104A7B;
	border-left: 0px solid #AFC4D5;
	border-top:0px solid #AFC4D5;
	color:#0033FF;
	height:19px;
	text-decoration:none;	
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
<TITLE>PUR100 Administer Purchaser (General Information)</TITLE>
<%@ include file="script/validateGeneralInfo.js" %>
<!--  <SCRIPT language="JavaScript1.1" src="/BASEWeb/Purchaser/script/validateGeneralInfo.js"></SCRIPT> -->
<SCRIPT language="JavaScript1.1" >
function customReset()
{
        
	document.PurGeneralInformation.reset();
	init();
}
</SCRIPT>
<SCRIPT>
function decideToVisibleRequiredDocuments(val)
{	
	for(var count = 1 ; count < document.PurGeneralInformation.Required.length ; count++)
		{
			//alert(document.PurGeneralInformation.Required[count].value);
			if(val == "SBU")
				{
					document.PurGeneralInformation.Required[count].style.visibility = "hidden";	
					document.PurGeneralInformation.Received[count].style.visibility = "hidden";		
					document.PurGeneralInformation.ReqRec[count].style.visibility = "hidden";								
				}
			else if(val =="LGS")
				{
					document.PurGeneralInformation.Required[count].style.visibility = "";	
					document.PurGeneralInformation.Received[count].style.visibility = "";	
					document.PurGeneralInformation.ReqRec[count].style.visibility = "";				
				}
		}
		requiredDocumentDisplay();
	/*
	if(val == "SBU")
		{
			document.PurGeneralInformation.Required1.style.visibility = "hidden";
		}
	else if(val =="LGS")
		{
			document.PurGeneralInformation.Required1.style.visibility = "";
		}
	*/		
}
</SCRIPT>      
</HEAD>
<BODY bgcolor="#999999"  onload="init();" >
<SCRIPT language="javascript">
var states = new Array() ;
var canadianStates = new Array();
function init()
	{	
      		
                <% 
			java.util.Vector stateV = new java.util.Vector();
			stateV = purDropDownVO.getStatesValue();						
			for(int i = 0 ; i < stateV.size(); i++)
				{
		%>
					states[<%=i%>] = '<%=stateV.elementAt(i)%>';
		<%
				}
		%>	
              
        <% 
		java.util.Vector canSt = new java.util.Vector();
		canSt = purDropDownVO.getCanadianStates();	 					
		for(int i = 0 ; i < 3; i++){
	%>
			canadianStates[<%=i%>] = '<%=canSt.elementAt(i)%>';
	<%}%>		    
	    document.PurGeneralInformation.Country.value = '<%=addrVO.getCountry()%>';     			
	    setState(document.PurGeneralInformation);
     
			
                   document.PurGeneralInformation.CurrentDate.value = "<%=session.getAttribute("CurrentDate").toString()%>";
                        document.PurGeneralInformation.TempTermDate.value = '<%=purInitVO.getTerminationDate()%>';
                       
			document.PurGeneralInformation.Status.value = '<%=purInitVO.getStatus()%>';
                        document.PurGeneralInformation.RegionDivision.value = '<%=purInitVO.getRegion()%>';
			
			<% 
			String errorMsg = (String) session.getAttribute("errorMsg"); 
 			if(!errorMsg.equals("Empty") ) { %>
			alert("<%=errorMsg%>");
                        <% session.setAttribute("errorMsg","Empty"); } %>

                       	document.PurGeneralInformation.Size.value = '<%=purInitVO.getSize()%>';
                        document.PurGeneralInformation.Country.value = '<%=addrVO.getCountry() %>';
                        document.PurGeneralInformation.DirectSale.value= '<%=purVO.getDirectSale()%>';
                        populateCategory( document.PurGeneralInformation.OrigEffectiveDate,document.PurGeneralInformation.RegionDivision);
			if(document.PurGeneralInformation.Category.value == "Post-Broker")
			 document.PurGeneralInformation.SubCategory.value = "110";
			else
			  document.PurGeneralInformation.SubCategory.value = "10";
                        
                        if(document.PurGeneralInformation.CommissionCategoryList.length == 0 )
                        	categoryDisplay();
                        decideToVisibleRequiredDocuments('<%= purInitVO.getSize()%>');
                        //requiredDocumentDisplay();
                        
			//parent.tops.PurTop.Category.value = document.PurGeneralInformation.Category.value;
                        //document.PurGeneralInformation.SizeDisplay.value='<%=purInitVO.getSize()%>';
			 disableform();
			  //parent.tops.document.PurTop.dynamic.value = "PUR101 Administer Purchaser ( General Information )";
 }
function setState( theForm ) {
	
		var country = theForm.Country.value;
		if ( country == "USA" ) {
		
			for ( var i=0; i<states.length; i++ ) {
				var addstate = new Option();
				addstate.text = states[i];
				addstate.value = states[i];
				theForm.State.options[i] = addstate;				
			}
			theForm.State.disabled = false;	
			theForm.State.value = '';
		}

		else if ( country == "CAN" ) {

			theForm.State.length = 0;

			for ( var i=0; i<canadianStates.length; i++ ) {
				var addstate = new Option();
				addstate.text = canadianStates[i];
				addstate.value = canadianStates[i];
				theForm.State.options[i] = addstate;				
			}
			theForm.State.disabled = false;
			theForm.State.value = '';			
		}
		else {

			theForm.State.length = 0;				
			theForm.State.disabled = true;
		}
		theForm.State.value = '<%=addrVO.getState()%>';
	}
function requiredDocumentDisplay()
{
      var count = document.PurGeneralInformation.Received.length;
      <%  for(int i = 0; i < rDoc.size() ; i++)
          { 
	   	rDocVO = (org.kp.purchaser.vo.RequiredDocumentVO)rDoc.elementAt(i);	
                String shrtName = rDocVO.getShortName();
                String receivedDoc = rDocVO.getReceivedDoc();
                String requiredDoc = rDocVO.getRequiredDoc();      
                                 
         %> 	       
     
          	   	for(var k=0;k<count; k++)
  				{   
                                	if(document.PurGeneralInformation.Received[k].value == "<%=shrtName%>" )
					{
                                      		<% if ( receivedDoc.equals("Y") )
 					 	   { %>
                                        		document.PurGeneralInformation.Received[k].checked = 1;
                                      		<% } if ( requiredDoc.equals("Y") )
                                           	     {
                                              		 %>document.PurGeneralInformation.Required[k].checked = 1;
                                       		<%   }  %>
					}
	  			
				}
			
     <%     }
	    if (rDoc.size() == 0 )
	    {
		    %> for(var l=0; l < count; l++ )
		       {
				document.PurGeneralInformation.Required[l].checked = 1;
		       }
	<%  }       %>
}
function categoryDisplay()
{
	document.PurGeneralInformation.CommissionCategoryList.style.visibility = "hidden";	
	document.PurGeneralInformation.CategoryToTop.value = document.PurGeneralInformation.Category.value;
	//alert("name "+parent.tops.document.PurTop);
	var topObject = parent.tops.document.PurTop;
	if( topObject == "[object]")//!= undefined )//
	{
		parent.tops.document.PurTop.Category.value = document.PurGeneralInformation.Category.value;
	}
<%	java.util.Vector catV = new java.util.Vector();
 	if ( catPurVO == null )
	 	 catV = (java.util.Vector) purVO.getCommissionCategories();
        else
		 catV = (java.util.Vector) catPurVO.getCommissionCategories();
	for( int i=catV.size(); i > 0; i-- ) 
        {
 		catVO = ( org.kp.purchaser.vo.CommissionCategoryVO ) catV.elementAt(i-1);
%>
                var subCategory = '';
                for ( var k = 0 ; k < document.PurGeneralInformation.SubCategory.length ; k++ )
		{
			if ( document.PurGeneralInformation.SubCategory[k].value == "<%=catVO.getSubCategory()%>" )
			{
                             subCategory = document.PurGeneralInformation.SubCategory[k].text;
			}
		}



	var elementsMaxLength = new Array();
	var elementsText = new Array();
	var elementsValue = new Array();
	elementsText[0] = document.PurGeneralInformation.Category.value;	
	elementsText[1] = subCategory;
	elementsText[2] = "<%=catVO.getEffectiveDate()%>";
	elementsText[3] = "<%=catVO.getEndDate()%>";	
	elementsText[4] = "<%=catVO.getStatusIndicator()%>";	
	//elementsText[5] = suffix;	
	
	
		 if( elementsText[4] != "A" && elementsText[4] != "D" ) 
		 {
		  	//alert("this is inside this"+<%=catVO.getSortOrder()%>);
		 	if( IsThisDateRangeCurrent(elementsText[2],elementsText[3] ) )
		 	{
		 	    if(topObject == "[object]") //!= undefined ) //
		 	    {
		 	   		parent.tops.document.PurTop.Category.value = subCategory;		 	   		
		 	   		document.PurGeneralInformation.CategoryToTop.value = subCategory;
		 	   	}
		 		elementsText[4] = '***';
		 	}
		 	else if( <%=catVO.getSortOrder()%> != 0 )
		 		elementsText[4] = "U"; 
		 	else 	 		
		 	   	elementsText[4] = "";
         }   	
	

	elementsMaxLength[0] = 15;
	elementsMaxLength[1] = 52;
	elementsMaxLength[2] = 11;
	elementsMaxLength[3] = 11; 
	elementsMaxLength[4] = 1;
	//elementsMaxLength[5] = 20;


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

	      	document.PurGeneralInformation.CommissionCategoryList.style.visibility = "";
		var addoptions = new Option();
		//addoptions.text = elementsText[0]+ " " +elementsText[1]+ " " +elementsText[2]+ " " +elementsText[3]+ " " +elementsText[4];
		addoptions.text = elementsText[1]+ " " +elementsText[2]+ " " +elementsText[3]+ " " +elementsText[4];
		//addoptions.text = document.PurGeneralInformation.Category.value+ "-" + subCategory + "-" + "<%=catVO.getEffectiveDate()%>" + "-" + "<%=catVO.getEndDate()%>" + "-" + "<%=catVO.getStatusIndicator()%>" ;
		addoptions.value =  "<%=catVO.getSubCategory()%>" + "," + "<%=catVO.getEffectiveDate()%>"+ "," + "<%=catVO.getEndDate()%>" + "," + "<%=catVO.getStatusIndicator()%>" + "," + "<%=catVO.getCategoryIK()%>"+","+"<%=catVO.getSortOrder()%>";
		document.PurGeneralInformation.CommissionCategoryList.options[document.PurGeneralInformation.CommissionCategoryList.options.length] = addoptions;
        <% 
         }
        %>
        
}
function displayDocuments()
{
	document.PurGeneralInformation.SelectedAction.value = "DisplayDocs";
        document.PurGeneralInformation.submit();
}

function IsThisDateRangeCurrent(EffectiveDate,EndDate)
{
		 var Status = false;
		 var currentdate = document.PurGeneralInformation.CurrentDate.value;
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

<FORM name="PurGeneralInformation" method="post" action="PurchaserGeneralInfoServlet" onSubmit="return validateForm(PurGeneralInformation)" target="_parent">
<input type="hidden" name="CategoryToTop" value="">
<input type="hidden" name="PID" value="<%=purInitVO.getPID()%>" >
                  <input type="hidden" name="TPAID" value="<%=purInitVO.getTPAID()%>" >
		 <input type="hidden" name="PurIK" value="<%=purInitVO.getPurIK()%>" >
		  <input type="hidden" name="SelectedAction" value="" >
                  <input type="hidden" name="CategoryIK" value="0" >
                  <input type="hidden" name="StatusIndicator" value="" >
		<input type="hidden" name="sourceId1" value="0" >
		<input type="hidden" name="sourceId2" value="0" >
		<input type="hidden" name="sourceId3" value="0" >
		<input type="hidden" name="sourceInd" value="PUR" >
                  <input type="hidden" name="SortOrder" value="-10000" >
                  <input type="hidden" name="WhereToGo" value="" >
		  <input type="hidden" name="FromWhere" value="0" >
                  <input type="hidden" name="message" value="" >
	          <input type="hidden" name="TempTermDate" value="" >
		  <input type="hidden" name="SizeDisplay" value="" >
		  <input type="hidden" name="CurrentDate" value="">
		  
<TABLE width="80%">
  <TBODY>
    <TR>
      <TD bgcolor="#999999">
       <TABLE cellpadding="1" cellspacing="1">
        <TBODY>
           <TR>
            <TD align="right" class="label">Orig Effective Date</TD>
            <TD align="left"><INPUT size="10" type="text" maxlength="10" name="OrigEffectiveDate" value="<%=purInitVO.getOrigEffectiveDate()%>" onBlur="populateCategory(OrigEffectiveDate,this.form.RegionDivision)" tabindex="1"></TD>
            <TD class="label" align="right">Termination Date</TD>
            <TD class="label" align="left"><INPUT size="10" type="text" maxlength="10" name="TerminationDate" value="<%=purInitVO.getTerminationDate()%>" Onchange="return callComments();"></TD>
            <TD class="label" align="right">Status</TD>
            <TD align="left"><SELECT name="Status">
<%  java.util.Hashtable ht = new java.util.Hashtable();
    ht = purDropDownVO.getStatus();
    java.util.Enumeration enum = ht.keys();
    String name = "";
    while ( enum.hasMoreElements() )
    {
              name = enum.nextElement().toString();
            
              %><OPTION value="<%=name%>" ><%=ht.get(name).toString()%></OPTION>
<%  }  %>
            </SELECT></TD>
            <TD class="label">Status Date</TD>
            <TD><INPUT size="10" type="text" maxlength="10" name="StatusDate" value="<%=purInitVO.getStatusDate()%>"></TD>
	    <!-- <TD align="right"><INPUT type="IMAGE" src="/BASEWeb/Purchaser/images/save.gif" name="submitType" value="save" width="50" height="22" border="0" alt="Save"  onClick="beforeSave()"></TD>-->
            <TD align="right"><IMG src="images/edit.gif" width="50" height="22" border="0" onClick="enableform()" ></TD>
            <TD align="right"><IMG src="images/reset.gif" width="50" height="22" border="0" onClick="customReset();"></TD>
          </TR>
          <TR>
            <TD class="label" align="right">Region / Division</TD>
            <TD align="left">
	      <SELECT name="RegionDivision" onChange="populateCategory(this.form.OrigEffectiveDate,RegionDivision)" tabindex="2">
<%  ht = null;
    enum  = null;
    ht = purDropDownVO.getRegionDivision();
    enum = ht.keys();
    while ( enum.hasMoreElements() )
    {
              name = enum.nextElement().toString();
              %><OPTION value="<%=name%>" ><%=ht.get( name )%></OPTION>
<%  }  %>
            </SELECT></TD>
            <TD class="label" align="right">Sales Unit</TD>
            <TD align="left">
   
              <SELECT name="Size" tabindex="3" onchange = "decideToVisibleRequiredDocuments(this.value)">
<%  ht = null;
    enum = null;
    ht = purDropDownVO.getSalesUnit();
    enum = ht.keys();
    while ( enum.hasMoreElements() )
    {
             name = enum.nextElement().toString();
              %><OPTION value="<%=name%>" ><%=ht.get( name )%></OPTION>
<%  }  %>  				
            </SELECT></TD>
            <TD class="label" align="left" colspan="2">IRS Tax ID <INPUT size="12" type="text" maxlength="9" name="IRSTaxID" value="<%=purVO.getTaxID()%>" tabindex="4"></TD>
            <TD id ="testing" class = "label">Direct Sale</TD>
            <TD><SELECT name="DirectSale">
            <option value="Y">Yes</option>
            <option value="N" selected>No</option>
            </SELECT></TD>
            <TD align="right"></TD>
            <TD align="right"></TD>
          </TR>
        </TBODY>
      </TABLE>
      <TABLE width="100%">
        <TBODY>
          <TR>
            <TD class="title" width="499">
                        <TABLE border="1" width="40%">
              <TBODY>
                <TR>
                  <TD class="title" width="535"><FONT color="#cc0033">Commission Category</FONT><BR>
                                    <TABLE cellpadding="1" cellspacing="1" width="40%">
              <TBODY>
                <TR>
                  <TD align="center" class="label">Category</TD>
                  <TD align="center" class="label">Sub-Category</TD>
                  <TD align="center" class="label">Effective Date</TD>
                  <TD align="center" class="label">End Date</TD>
                                                <TD></TD>
                                                <TD align="center" width="71"><INPUT size="20" type="button" maxlength="20" name="submitDelete" value="Delete" class="pbttn" onclick="return beforeDelete();"></TD>
                                                <!-- <TD><IMG src="images/delete.gif" name="submitDelete"  alt="Delete" onClick=" return beforeDelete()"></TD> -->
                </TR>
                <TR>
                        <TD><INPUT size="20" type="text" maxlength="20" name="Category" style="background-color : silver;" onFocus="this.blur()"></TD>
                        <TD>
		    <SELECT name="SubCategory" onChange=" return verifyCategory()" tabindex="5">
		   
<%  ht = null;
    enum = null;
    ht = purDropDownVO.getCategory();
    enum = ht.keys();
    while ( enum.hasMoreElements() )
    {
             name = enum.nextElement().toString();
             
                    %>
                                                    <OPTION value="<%=name%>" selected><%=ht.get( name )%></OPTION>
                                                    <%  }  %>
                                                </SELECT></TD>
                        <TD><INPUT  size="10" type="text" maxlength="10" name="EffectiveDate" tabindex="6"></TD>
                        <TD><INPUT size="10" type="text" maxlength="10" name="EndDate"></TD>
                                                <TD class = "label">Indicator</TD>
                                                <!-- <TD> <INPUT type="IMAGE" src="/BASEWeb/Purchaser/images/add.gif" name="submitAdd" value="Add" width="50" height="22" border="0" alt="Add" onClick=" return beforeAdd()"> 
<IMG src="images/add.gif" name="submitAdd" width="50"  alt="Add" onClick=" return beforeAdd()"></TD> -->
<TD align="center" width="71"><INPUT size="20" type="button" maxlength="20" name="submitAdd" value="  Add  " class="pbttn" onclick=" return beforeAdd()" tabindex="7"></TD>

                </TR>
                                        </TBODY>
                  </TABLE>
                                    <TABLE>
                                        <TBODY>
                                            <TR>
                                                <TD><SELECT name="CommissionCategoryList" size="3" onclick="return popIntoFields(CommissionCategoryList,this.form.CommissionCategoryList.value)" style='font-family : "Courier New";'></SELECT></TD>
                                            </TR>
                                        </TBODY>
                                    </TABLE>
                                    </TD>
                </TR>
              </TBODY>
            </TABLE>
                        </TD>
            <TD valign="top" class="title" width="441">
            <TABLE border="1" width="100%">
              <TBODY>
                <TR>
                  <TD class="title" width="304"><FONT color="#cc0033" >Required Documents</FONT><BR>
            <font size = "-1">Required &nbsp;&nbsp; &nbsp;Received</font><BR>
            <FONT class="label">

	    
            
            <INPUT type="checkbox" name="Required" value="PA" tabindex="9"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<INPUT type="checkbox" name="Received" value="PA"> <INPUT class="test" size="30" type="text" name="ReqRec" value=" Purchase Advice" style="background-color: #999999">&nbsp;<BR>
            <INPUT type="checkbox" name="Required" value="QUOTE" tabindex="9"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<INPUT type="checkbox"  name="Received" value="QUOTE"> &nbsp;<INPUT class="test" size="30" type="text" name="ReqRec" value="Rate Quote" style="background-color: #999999"><BR>
            <INPUT type="checkbox" name="Required" value="EXHIBITK" readonly tabindex="10">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<INPUT type="checkbox" name="Received" value="EXHIBITK" > <INPUT class="test" size="30" type="text" name="ReqRec" value=" Exhibit" style="background-color: #999999">&nbsp;<BR>
                 <nobr><INPUT type="checkbox"  name="Required" value="INFORCE" tabindex="11"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<INPUT type="checkbox"  name="Received" value="INFORCE"> &nbsp;<INPUT class="test" size="30" type="text" name="ReqRec" value="In Force Commission Form" style="background-color: #999999"><BR>
                  <nobr><INPUT type="checkbox"  name="Required" value="BORLTR" tabindex="12"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<INPUT type="checkbox"  name="Received" value="BORLTR"> &nbsp;<INPUT class = "test" size="30" type="text" name="ReqRec" value="Out of Pocket Commn Letter" style="background-color: #999999"><BR>
               </FONT>
                                    <BR>
                                    </TD>
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
            <TD class="title"><FONT color="#cc0033">Address</FONT><BR>
            <TABLE cellpadding="1" cellspacing="1">
              <TBODY>
                <TR>
                  <TD class="label" align="right">Line1</TD>
                  <TD colspan="5"><INPUT size="40" type="text" maxlength="40" name="Line1" value="<%=addrVO.getLine1()%>" tabindex="13"></TD>
                  <TD class="label" colspan="2">Mail Stop</TD>
                  <TD colspan="2"><INPUT size="20" type="text" maxlength="20" name="MailStop" value="<%=addrVO.getMailStop()%>" tabindex="14"></TD>
                </TR>
                <TR>
                  <TD class="label" align="right">Line2</TD>
                 <TD colspan="5"><INPUT size="40" type="text" maxlength="40" name="Line2" value="<%=addrVO.getLine2()%>" tabindex="15"></TD>
                  <TD colspan="2"></TD>
                  <TD colspan="2"></TD>
                </TR>
                <TR>
                  <TD class="label" align="right">Line3</TD>
                  <TD colspan="5"><INPUT size="40" type="text" maxlength="40" name="Line3" value="<%=addrVO.getLine3()%>" tabindex="16"></TD> 
                  <TD colspan="2"></TD>
                  <TD colspan="2"></TD>
                </TR>
                <TR>
                  <TD class="label" align="right">City</TD>
                  <TD colspan="5"><INPUT size="40" type="text" maxlength="40" name="City" value="<%=addrVO.getCity()%>" tabindex="17"></TD>
                  <TD colspan="4" rowspan="2" align="right">
                  <TABLE border="1">
                    <TBODY>
                      <TR>
                        <TD class="title"><FONT color="#cc0033">Phone</FONT><BR>
                        <TABLE cellpadding="1" cellspacing="1">
                          <TBODY>
                            <TR>
                              <TD class="label">Area</TD>
                              <TD class="label">Number</TD>
                              <TD class="label">Ext</TD>
                            </TR>
                            <TR>
                              <TD><INPUT size="3" type="text" maxlength="3" name="Area" value="<%= checkForZero(phnVO.getAreaCode())%>" tabindex="21"></TD>
                              <TD><INPUT size="7" type="text" maxlength="7" name="Number" value="<%= checkForZero(phnVO.getNumber())%>" tabindex="22"></TD>
                              <TD><INPUT size="3" type="text" maxlength="3" name="Ext" value="<%= checkForZero(phnVO.getExtension())%>" tabindex="23"></TD>
                              	
								<%! private String checkForZero(int val)
									{	
										return (val > 0)?String.valueOf(val):"";
									}
								%>                              
                            </TR>
                          </TBODY>
                        </TABLE>
                        </TD>
                      </TR>
                    </TBODY>
                  </TABLE>
                  </TD>
                </TR>
                <TR>
                  <TD class="label" align="right">State</TD>
                  <TD><SELECT name="State" tabindex="18"></SELECT></TD>
                  <TD class="label" align="right">Zip</TD>
                  <TD><INPUT size="9" type="text" maxlength="9" name="Zip" value="<%=addrVO.getZip()%>" tabindex="19"></TD>
                  <TD class="label" align="right">Country</TD>
                  <TD><SELECT name="Country" OnChange="setState(document.PurGeneralInformation)" tabindex="20">
                  <%  
	 				java.util.Vector countryValue =  purDropDownVO.getCountryValue();
	 				java.util.Vector countryName =  purDropDownVO.getCountryText();
					int length   = countryValue.size();
				for(int k=0;k< length; k++)  { %>
				<OPTION value="<%= (String)countryValue.elementAt(k) %>" ><%= (String)countryValue.elementAt(k) %></OPTION>
				
					<%
					}
					%>
                  </SELECT></TD>
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
            <TD class="title"><FONT color="#cc0033">Owner / Representative</FONT>
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
                  <TD align="center"><INPUT size="10" type="text" maxlength="10" name="Honor" value="<%=ownerVO.getHonorific()%>" tabindex="24"></TD>
                  <TD align="center"><INPUT size="30" type="text" maxlength="30" name="FName" value="<%=ownerVO.getFirstName()%>" tabindex="25"></TD>
                  <TD align="center"><INPUT size="20" type="text" maxlength="20" name="MName" value="<%=ownerVO.getMiddleName()%>" tabindex="26"></TD>
                  <TD align="center"><INPUT size="30" type="text" maxlength="30" name="LName" value="<%=ownerVO.getLastName()%>" tabindex="27"></TD>
                  <TD align="center"><INPUT size="20" type="text" maxlength="20" name="Suffix" value="<%=ownerVO.getSuffix()%>" tabindex="28"></TD>
                </TR>
                <TR>
                  <TD class="label" align="right">Title</TD>
                  <TD colspan="5"><INPUT size="40" type="text" maxlength="40" name="Title" value="<%=ownerVO.getTitle()%>" tabindex="29"></TD>
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
</FORM>
</BODY>
</HTML><U></U>