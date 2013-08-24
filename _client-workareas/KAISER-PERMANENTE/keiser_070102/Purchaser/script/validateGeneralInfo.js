<SCRIPT Language="JavaScript1.1">
function callComments()
{ 
      var errorStatus = false;
	if( document.PurGeneralInformation.TerminationDate.value != "")
	{
		errorStatus = checkDateValidation( "TerminationDate",document.PurGeneralInformation.TerminationDate.value);
		if ( !errorStatus )
     		{
			if ( document.PurGeneralInformation.TempTermDate.value != document.PurGeneralInformation.TerminationDate.value )
			{ 
            		document.PurGeneralInformation.TempTermDate.value = document.PurGeneralInformation.TerminationDate.value;
				document.PurGeneralInformation.sourceId1.value = document.PurGeneralInformation.PurIK.value;
				var functionType = "DMGR";	
				var url = '../Comments/CommentServlet?sourceId1='+document.PurGeneralInformation.PurIK.value+'&sourceId2=0&sourceId3=0&sourceInd=PUR&funType='+functionType;												
				window.open(url, 'slideWindow',false,400,480);            
			}
		}
            else
		{
			document.PurGeneralInformation.TerminationDate.focus();
			return false;
		}
	}
      
}

function verifyCategory( )
{
	var subCatValue = document.PurGeneralInformation.SubCategory.value;
	var subCatName  ="";
      for(var i = 0; i < document.PurGeneralInformation.SubCategory.length; i++ )
	{
		if ( document.PurGeneralInformation.SubCategory[i].selected == true )
		{
			subCatName  = document.PurGeneralInformation.SubCategory[i].text;
 		}
	}
         var catValue = document.PurGeneralInformation.Category.value;
      if( catValue == 'Pre-Broker')
	{
		if ( subCatValue > 100 )
		{
		    alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.InvalidSubCategroyForPre")%>");
                   document.PurGeneralInformation.SubCategory.value = "10";
                   return false;
		}
        }
	else if (catValue == "Post-Broker" )
	{
		if ( subCatValue < 100 )
		{
		   alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.InvalidSubCategoryForPost")%>");
		   document.PurGeneralInformation.SubCategory.value = "110";
                   return false;
		}
        }

}
function disableform()
{
	document.PurGeneralInformation.OrigEffectiveDate.disabled = true ;
	document.PurGeneralInformation.TerminationDate.disabled = true ;
	document.PurGeneralInformation.Status.disabled = true ;
	document.PurGeneralInformation.RegionDivision.disabled = true ;
	document.PurGeneralInformation.Size.disabled = true ;
	document.PurGeneralInformation.IRSTaxID.disabled = true;
	document.PurGeneralInformation.StatusDate.disabled = true;
      document.PurGeneralInformation.CommissionCategoryList.disabled = true;
	if(document.PurGeneralInformation.Size.value == "LGS")
	{
      	for(var i=0; i<	document.PurGeneralInformation.Required.length; i++)
		{
     			document.PurGeneralInformation.Required[i].disabled = true;
			document.PurGeneralInformation.Received[i].disabled = true;
		}
	}
	else
	{
		document.PurGeneralInformation.Required.disabled = true;
		document.PurGeneralInformation.Received.disabled = true;
	}

      document.PurGeneralInformation.Line1.disabled = true;
	document.PurGeneralInformation.Line2.disabled = true;
	document.PurGeneralInformation.Line3.disabled = true;
	document.PurGeneralInformation.City.disabled = true;
	document.PurGeneralInformation.MailStop.disabled = true;
	document.PurGeneralInformation.State.disabled = true;
	document.PurGeneralInformation.Zip.disabled = true;
	document.PurGeneralInformation.Country.disabled = true;
	document.PurGeneralInformation.Area.disabled = true;
	document.PurGeneralInformation.Number.disabled = true;
	document.PurGeneralInformation.Ext.disabled = true;
	document.PurGeneralInformation.Honor.disabled = true;
	document.PurGeneralInformation.FName.disabled = true;
	document.PurGeneralInformation.MName.disabled = true;
	document.PurGeneralInformation.LName.disabled = true;
	document.PurGeneralInformation.Suffix.disabled = true;
	document.PurGeneralInformation.Title.disabled = true;

}
function enableform()
{
	document.PurGeneralInformation.OrigEffectiveDate.disabled = false ;
	document.PurGeneralInformation.TerminationDate.disabled = false ;
	document.PurGeneralInformation.Status.disabled = false ;
	document.PurGeneralInformation.RegionDivision.disabled = false ;
	document.PurGeneralInformation.Size.disabled = false ;
	document.PurGeneralInformation.IRSTaxID.disabled = false;
    document.PurGeneralInformation.Category.Focus = "";
	document.PurGeneralInformation.CommissionCategoryList.disabled = false;
	if(document.PurGeneralInformation.Size.value == "LGS")
	{
		for(var i=0; i<	document.PurGeneralInformation.Required.length; i++)
		{
     			document.PurGeneralInformation.Required[i].disabled = false;
			document.PurGeneralInformation.Received[i].disabled = false;
		}
	}
	else
	{
		document.PurGeneralInformation.Required.disabled = false;
		document.PurGeneralInformation.Received.disabled = false;
	}

    document.PurGeneralInformation.Line1.disabled = false;
	document.PurGeneralInformation.Line2.disabled = false;
	document.PurGeneralInformation.Line3.disabled = false;
	document.PurGeneralInformation.City.disabled = false;
	document.PurGeneralInformation.MailStop.disabled = false;
	if(document.PurGeneralInformation.State.value != "")
		document.PurGeneralInformation.State.disabled = false;
	else
		document.PurGeneralInformation.State.disabled = true;	
		document.PurGeneralInformation.Zip.disabled = false;
		document.PurGeneralInformation.Country.disabled = false;
		document.PurGeneralInformation.Area.disabled = false;
		document.PurGeneralInformation.Number.disabled = false;
		document.PurGeneralInformation.Ext.disabled = false;
		document.PurGeneralInformation.Honor.disabled = false;
		document.PurGeneralInformation.FName.disabled = false;
		document.PurGeneralInformation.MName.disabled = false;
		document.PurGeneralInformation.LName.disabled = false;
		document.PurGeneralInformation.Suffix.disabled = false;
		document.PurGeneralInformation.Title.disabled = false;
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

function beforeAdd()
{
      var errorStatus = false;
 	  errorStatus =  checkDateValidation( "EffectiveDate",document.PurGeneralInformation.EffectiveDate.value);
      if ( errorStatus )
           		return false;
      if (document.PurGeneralInformation.EndDate.value != "" )
	  {
      		errorStatus = checkDateValidation("EndDate",document.PurGeneralInformation.EndDate.value);
            	if ( errorStatus )
				return false;
	  }

 	errorStatus = isCurrentRecordExists( document.PurGeneralInformation.CommissionCategoryList,"Add" );
    		if ( errorStatus )
       		return false;

      enableform();
      document.PurGeneralInformation.StatusDate.disabled = false;
	  document.PurGeneralInformation.SelectedAction.value = 'Add';
      document.PurGeneralInformation.submit(); 
}

function beforeDelete( )
{
       
       var errorStatus = false;
       errorStatus = errorStatus = isCurrentRecordExists( document.PurGeneralInformation.CommissionCategoryList ,"Delete");
       if ( errorStatus )
           return false;
           
       enableform();
       document.PurGeneralInformation.StatusDate.disabled = false;    
       document.PurGeneralInformation.SelectedAction.value = "Delete";
       document.PurGeneralInformation.submit(); 
} 
function beforeSave( )
{
       document.PurGeneralInformation.SelectedAction.value = "Save";
}

function populateCategory( originaleffdate, regiondivision ) 
{
		var effdtmmddyy = originaleffdate.value;
		var regdiv =  regiondivision.value;
            var SCmm = '01';
            var SCdd = '01';
            var SCyyyy = '1995';
		var NCmm = '10';
            var NCdd = '01';
            var NCyyyy = '1996';
	      var category = 'k';
               
   	      var orgmm = effdtmmddyy.substring(0, 2);
         	var orgdd = effdtmmddyy.substring(3, 5);
         	var orgyyyy = effdtmmddyy.substring(6,10);
   	        if ( regdiv == 'SCR') 
              {
		     if ( orgyyyy <= SCyyyy )
                 {  
                          if ( orgyyyy < SCyyyy )
                             category = 'Pre-Broker';
                          else  if ( orgmm <= SCmm )
			  {
			    if ( orgmm < SCmm )
			       category = 'Pre-Broker';
			    else if ( orgdd < SCdd )
			         category = 'Pre-Broker';
			  }
                     }
                     if ( orgyyyy > SCyyyy )
		     {
	                 category = 'Post-Broker';
		     }
                     else if( orgyyyy == SCyyyy )
		     {
			 if ( orgmm > SCmm )
			    category = 'Post-Broker';
                         else if ( orgmm == SCmm )
			 {
			   if ( orgdd >= SCdd )
			      category = 'Post-Broker';
			 }
		     }
               
		}
		else if ( regdiv == 'NCR' ) 
		{
                        if ( orgyyyy <= NCyyyy )
                     	{
					if ( orgyyyy < NCyyyy )
						category = 'Pre-Broker';
        	                   else if ( orgmm <= NCmm )
					 { 
					  	if ( orgmm < NCmm )
						category = 'Pre-Broker';
                                        else if ( orgdd < NCdd )
                    	     	 		category = 'Pre-Broker';
                               }
                     	}

                     	if ( orgyyyy > NCyyyy )
                        {
	             	   category = 'Post-Broker';
                        }
                        else if ( orgyyyy == NCyyyy )
                        {
					if ( orgmm > NCmm )
                                  category = 'Post-Broker';
                                else if( orgmm == NCmm )
					  {
                                    if ( orgdd >= NCdd )
			   			category = 'Post-Broker';
                                }
			   		
		     		}
               
		}
document.PurGeneralInformation.Category.value = category;
if (category == "Pre-Broker" )
document.PurGeneralInformation.SubCategory.value = "10";
else
document.PurGeneralInformation.SubCategory.value = "110"
} // end of populateCategory

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
	}
}
function popIntoFields( popList, popValue ) 
{
	if(popValue == "")
		return false;
	var values = popValue;
	for( var m=0; m < popList.length; m++ )
      {
		if ( popList.options[m].selected == true )
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
	//tokenizedData[3] == "H" ||
   /* if( tokenizedData[3] == "A" || tokenizedData[3] == "D" )
	{
		alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.DoNotModifyHistory")%>");
		return false;
	} */
	document.PurGeneralInformation.SubCategory.value = tokenizedData[0];
	document.PurGeneralInformation.EffectiveDate.value =  tokenizedData[1];
	document.PurGeneralInformation.EndDate.value =  tokenizedData[2];
	document.PurGeneralInformation.StatusIndicator.value =  tokenizedData[3];
	document.PurGeneralInformation.CategoryIK.value =  tokenizedData[4];
      document.PurGeneralInformation.SortOrder.value = tokenizedData[5];
	if ( tokenizedData[3] == "C")
	         verifyCategory();


   } 
</SCRIPT>