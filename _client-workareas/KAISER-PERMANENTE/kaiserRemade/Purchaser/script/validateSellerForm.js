<SCRIPT Language="JavaScript1.1">
function validateSellerForm(theForm)
{	
	theForm.SelectedAction.value = "Save";
	theForm.sellerSalesDate.disabled = false ;
	theForm.sellerBrokerName.disabled =false ;
	theForm.sellerBrokerID.disabled =false ;		
	theForm.SellerList.disabled =false ;
	
	var errorFields = "";
	var errorStatus = false;
	
	if ( theForm.salesDate.value == "" && theForm.SellerList.length > 0) {
		errorFields += "\n" + "<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.seller.SalesDateRequired")%>";
		errorStatus = true;
	}
	else if(theForm.SellerList.length > 0){
		checkDateValidation( theForm.sellerSalesDate.name, theForm.sellerSalesDate.value );		
	}	
     
	if (errorStatus==true) {
		alert( errorFields );
	     	return false;
	}
	else {
	
		return true;
	}
	function checkDateValidation(datename, datevalue){
	 		var validdate = "1234567890/";
         	var err=0;
         	var psj=0;
	      	var a="";
        	a=datevalue;
		
	 	if (a.length != 10) {
			errorFields += "\n" +  '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Invalid")%>'+datename;
			errorStatus = true;
			return false;
		}
		else {
			for (var i=0; i < a.length; i++) {
			temp = "" + a.substring(i, i+1);
				if (validdate.indexOf(temp) == "-1") {
					errorFields += "\n" +  '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+datename;
					errorStatus = true;
					return false;
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
			return false;
		 }
         	 if (c != '/' || e != '/' ) {
			errorFields += "\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Invalid")%>'+datename;
			errorStatus = true;
			return false;
		 }
         	 if (b<1 || b>31) {
			errorFields += "\n" + datename + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidDate")%>';
			errorStatus = true;
			return false;
		 }
       
         
         
         	 if (f<1900 || f>4000) {
			errorFields += "\n" + datename +  '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidYear")%>';
			errorStatus = true;
			return false;
		 }



         	 // months with 30 days
         	 if (d==4 || d==6 || d==9 || d==11){
             	if (b==31) {
				errorFields += "\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.30DaysInAMonth")%>'+datename;
				errorStatus = true;
				return false;
			}
         	 }


	      // february, leap year
         	 if (d==2){
              	// feb
              	var g=parseInt(f/4)
              	if (isNaN(g)) {
				errorFields += "\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.MonthForLeapYear")%>'+datename;
				errorStatus = true;
				return false;
	            }

             	if (b>29) {
				errorFields += "\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.MonthDateNoMatch")%>'+datename;
				errorStatus = true;
				return false;
		 	}

             	if (b==29 && ((f/4)!=parseInt(f/4))) {
				errorFields += "\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Invalid")%>'+datename;
				errorStatus = true;
				return false;
	       	}
		 }
		 

	} // end of checkValidation()

}
</SCRIPT>