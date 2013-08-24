<SCRIPT Language="JavaScript1.1">   
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

	/*if( splitData[6] == "A" || splitData[6] == "D" )
	{
		alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.DoNotModifyHistory")%>");
		return false;
	}
else { */

	 document.AdministrativeArrgmt.administrativeSystem.value = splitData[0];
	 document.AdministrativeArrgmt.administrator.value = splitData[1];
	 document.AdministrativeArrgmt.billingFrequency.value = splitData[2];
	 document.AdministrativeArrgmt.effDate.value = splitData[3];
	 document.AdministrativeArrgmt.endDate.value = splitData[4];
	 document.AdministrativeArrgmt.adminrelId.value = splitData[5]; 
	 document.AdministrativeArrgmt.statusIndicator.value = splitData[6]; 
	document.AdministrativeArrgmt.SortOrder.value = splitData[7]; 

/*        } */
	oldNo = true;

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




function disableform()
{
	document.AdministrativeArrgmt.PID.disabled = true ;
	document.AdministrativeArrgmt.TPAID.disabled = true ;
	document.AdministrativeArrgmt.purchaserName.disabled =true ;
	document.AdministrativeArrgmt.administrativeSystem.disabled = true ;
	document.AdministrativeArrgmt.administrator.disabled = true ;
	document.AdministrativeArrgmt.billingFrequency.disabled = true;
	document.AdministrativeArrgmt.effDate.disabled = true;
}

function enableform(){
	document.AdministrativeArrgmt.PID.disabled = false ;
	document.AdministrativeArrgmt.TPAID.disabled = false ;
	document.AdministrativeArrgmt.purchaserName.disabled = false ;
	document.AdministrativeArrgmt.administrativeSystem.disabled = false ;
	document.AdministrativeArrgmt.administrator.disabled = false ;
	document.AdministrativeArrgmt.billingFrequency.disabled = false;
	document.AdministrativeArrgmt.effDate.disabled = false;
	document.AdministrativeArrgmt.AddList.disabled = false;
}

 
function selectAdministartor()
{
   	var count=0;	
    var adsysValue =  document.AdministrativeArrgmt.administrativeSystem.value  ;   
	var adminid = new Array();
	var adminds = new Array();
	<%  	
		int count =0;
		java.util.Vector adminidV = new java.util.Vector();
		java.util.Vector admindsV = new java.util.Vector();
	 	java.util.Hashtable administrator =  purchaserDropDownVO.getAdministrators();
		java.util.Enumeration enum1    = administrator.keys();
		int m =0;
		while(enum1.hasMoreElements())  { 
		String aValue =(String) enum1.nextElement();
		%>
			adminid["<%=m%>"] = "<%=aValue %>";
			adminds["<%=m%>"] = "<%=(String)administrator.get(aValue) %>";
		<%
		   m++;
		 } 
		%>
		 for(var j = 0 ; j < adminid.length ; j++)
		{
			 
 	        if(adsysValue ==adminid[j])
		 {
		  count = j;
		  break;		
		 }			
		}
		  
document.AdministrativeArrgmt.administrator.value=adminds[count] ;
// document.AdministrativeArrgmt.administrator.value= "California Service Center";
  }
function beforeAdd()
{
         	var errorStatus = false;
			errorStatus =  validate( document.AdministrativeArrgmt);
            if ( ! errorStatus )
           	return false;
        	errorStatus = isCurrentRecordExists( document.AdministrativeArrgmt.AddList,"Add" );
       		if ( errorStatus )
            return false;
     		enableform();      
			document.AdministrativeArrgmt.SelectedAction.value = 'Add';
			document.AdministrativeArrgmt.submit();

}


function beforeDelete( )
{
   			if(document.AdministrativeArrgmt.AddList.length ==0)
			return false;
			errorStatus = isCurrentRecordExists( document.AdministrativeArrgmt.AddList,"Delete" );
       		if (  errorStatus )
         	return false;
   			enableform();
       		document.AdministrativeArrgmt.SelectedAction.value = "Delete";
       		document.AdministrativeArrgmt.submit();
}

function adminReset()
{
    document.AdministrativeArrgmt.reset();
	document.AdministrativeArrgmt.administrativeSystem.value = "" ;
	document.AdministrativeArrgmt.administrator.value = "" ;
	document.AdministrativeArrgmt.billingFrequency.value = "";
	/*document.AdministrativeArrgmt.effDate.value = "";
	document.AdministrativeArrgmt.endDate.value ="";
	document.AdministrativeArrgmt.statusIndicator.value ="";
	document.AdministrativeArrgmt.SortOrder.value ="-1000";
	document.AdministrativeArrgmt.adminrelId.value ="0";*/

}
</SCRIPT>
