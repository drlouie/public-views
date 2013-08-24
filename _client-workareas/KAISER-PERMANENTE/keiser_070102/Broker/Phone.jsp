<!-- Sample JSP file -->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML>
<HEAD>

<SCRIPT language="javascript">
var oldNo = false;
var phoneIK = "1234";
function popList(list,type,ctry,area,num,ext,pref)  
 {   

	var errorStatus = false;
	var errorMessage = "";
	var countryCode = ctry
	var areaCode = area;
	var number	= num;
	var extension = ext;	
	var phoneExists = false;
	var prefText;
	var prefValue;
	var nonPrefText;
	var nonPrefValue;
	//checkAllValid(countryCode,areaCode,number,extension);
	var PhoneType ="";
	
	 listLength = list.options.length;


 	if( type == "B")
          PhoneType =" Business";
       else if ( type =="P")
          PhoneType = "    Pager";
       else if ( type == "M")
          PhoneType ="   Mobile";
       else if ( type == "R")
          PhoneType = "Residence";
       else if ( type == "F")
          PhoneType = "      Fax";

     	var prefered = pref;	

	var lastHyphen ;


if(prefered == false)
	{
		nonPrefText =PhoneType+":"+countryCode+"-"+areaCode+"-"+number+"-"+extension;
		nonPrefValue =type+":"+countryCode+"-"+areaCode+"-"+number+"-"+extension+"-"+phoneIK;
	//alert("Incomming is NonPrefered : "+nonPrefValue);
		lastHyphen = nonPrefValue

	}
	
if(prefered == true)	
	{	
		prefText = PhoneType+":"+countryCode+"-"+areaCode+"-"+number+"-"+extension+"*"		 
		prefValue =type+":"+countryCode+"-"+areaCode+"-"+number+"-"+extension+"*"+"-"+phoneIK;
	//alert("Incomming is Prefered : "+prefValue);
		lastHyphen = prefValue;	
	}

	var nonPrefNo = new Option();
	nonPrefNo.value = nonPrefValue;
	nonPrefNo.text = nonPrefText;

	var prefNo = new Option();
       prefNo.value = prefValue;
       prefNo.text = prefText;


	if(list.options.length == 0 )
		{	
		
			addFirstRow(list);
		}  	
	

	var tempFirstValue = list.options[0].value;
	var tempFirstText = list.options[0].text;	
	


	var tempSubValue = tempFirstValue;
	var tempTextLength = tempFirstText.length;

	

	var tempLastHyphen;
 	for( var j = 0 ; j < tempFirstValue.length ; j++)
  		{
   		 	if(tempFirstValue.substring(j,j+1) =="-")
     				{
      					tempLastHyphen=j;	
								
     				}
  		}
	var star = tempFirstValue.substring(tempLastHyphen,tempLastHyphen-1)
	//alert("Last digit is Star : "+star);

var nonStar = new Option();
var tempFirstPhoneIK = tempFirstValue.substring(tempLastHyphen);
alert("temp:"+tempFirstPhoneIK);
if(star == "*")
 {
	nonStar.value = tempFirstValue.substring(0,tempLastHyphen-1)+"-"+tempFirstPhoneIK;
	nonStar.text = tempFirstText.substring(0,tempTextLength-1);

	//alert("Non star value :"+nonStar.value);
 }
else
   {
	nonStar.value = tempFirstValue;
	nonStar.text = tempFirstText;
    }


//alert("NonStar is : "+nonStar.value +":"+nonStar.text);
	var extraRow = new Option();
	extraRow.value = " ";
	extraRow.text = " ";

	var found = false;
	

	if(prefered == true && oldNo == false && listLength >0)
		{	
		
			pushDown(list);			
		
		}	
	else if(prefered == false && oldNo == false && listLength >0)
		{	
				
					addAtLast(list);
		}
		
	
	else if(prefered == true && oldNo == true && listLength >0)
        {
        for(var i=0 ; i < list.options.length; i++) 
		{	
			if(list.options[i].selected && list.options[i] != "") 
          			{	
					
					list.options[i].value = "";
					list.options[i].text = "";					
   	   			}
				
		  }	
		sortList(list);
		oldNo = false;
         }
         else if(prefered == false && oldNo == true && listLength >0) 
	   {	
		modifyAtSame(list);
		oldNo = true;
          }

//---------------------------------------------
function sortList(ilist) 
	{
		alert("Sort called with value :" +nonStar.value+" text : "+nonStar.text);
		for(var i = 0; i < ilist.options.length; i++) 
			{
				if(ilist.options[i].value == "")  
					{	
						ilist.options[0].value = nonStar.value;
						ilist.options[0].text = nonStar.text;
						//ilist.options[0] = nonStar;
						for(var j = i; j > 0; j--)  
							{
								//alert("This is getting sorted : "+ilist.options[j - 1].value)
								ilist.options[j].value = ilist.options[j - 1].value;
								ilist.options[j].text = ilist.options[j - 1].text;
							}					
   					}
			}
	ilist.options[0] = prefNo;
	refresh();
       }
//----------------------------------------------------
function pushDown(ilist)
 {

	alert("Push called with value :" +nonStar.value+" text : "+nonStar.text);
	//alert("insdie push : "+nonStar.text)
	if(tempFirstText.substring(tempTextLength,tempTextLength-1)== "*")
				{
					
					ilist.options[listLength] = extraRow;						
					ilist.options[0].value = nonStar.value;
					ilist.options[0].text = nonStar.text;	
					//ilist.options[0] = nonStar;			
					for(var j = ilist.options.length ; j >1 ; j--)  
						{	
							ilist.options[j-1].value = ilist.options[j-2].value;
							ilist.options[j-1].text = ilist.options[j-2].text;
											
						}	
							ilist.options[0] = prefNo;														
							refresh();
   				}
			else	if(tempFirstText.substring(tempTextLength,tempTextLength-1)!= "*")
				{
							
					ilist.options[listLength] = extraRow;						
					for(var j = ilist.options.length ; j >1 ; j--)  
						{	
							ilist.options[j-1].value = ilist.options[j-2].value;
							ilist.options[j-1].text = ilist.options[j-2].text;
											
						}	
							ilist.options[0] = prefNo;														
							refresh();
							oldNo = false;					
   				}
	
 }

//------------------------------------------------------
function addFirstRow(ilist)
 {
//alert("Add at first called");
	if(prefered == true)
		{
			document.AgentCompleteSetup.PhoneList.style.visibility = "";
			ilist.options[0]=prefNo;
			refresh();
		}
	else if (prefered == false)
		{	
			
			document.AgentCompleteSetup.PhoneList.style.visibility = "";
		       ilist.options[0]=nonPrefNo;									
			refresh();			
		}
 }
//--------------------------------------------------------------------
function addAtLast(ilist)
  {	
//alert("Add at last called");
	document.AgentCompleteSetup.PhoneList.style.visibility = "";
	ilist.options[listLength] = nonPrefNo;
	refresh();

  }
//----------------------------------------------------------------------
function modifyAtSame(ilist)
 {	
//alert("Modify at same  called");
	for(var i=0 ; i < ilist.options.length; i++) 
		{
			if(ilist.options[i].selected) 
          			{
					document.AgentCompleteSetup.PhoneList.style.visibility = "";
					ilist.options[i] = nonPrefNo;
					refresh();
					found=true;
					oldNo = false;
					break;
					
   	   			}	
		  }

  }

function checkAllValid(iCountryCode,iAreaCode,iNumber,iExtension)
 {	
	if(  iAreaCode == "" || iNumber == "" || iExtension == "" )
		{
			//alert( "AreaCode, Number, Extensio should not be Null \n " );
			document.AgentCompleteSetup.CountryCode.focus();
			return false;			
		}
	else if( iAreaCode.length < 3 || iNumber.length < 7 || iExtension.length < 3)
		{
			//alert( "Check the Length of Numbers \n" );
			document.AgentCompleteSetup.CountryCode.focus();
			return false;
		}
	else if (iCountryCode == "")
		{
			countryCode = "   ";
		}
	else if(iCountryCode !="" && iCountryCode.length <3)
		{		
			//alert( "Check the Length of Numbers \n" );
			document.AgentCompleteSetup.CountryCode.focus();
			return false;
		}

	checkChar(iCountryCode);
	checkChar(iAreaCode);
	checkChar(iNumber);
	checkChar(iExtension);
 }

function checkChar(iValue)
  {	
	var valid = "0123456789 ";  

 	for (var i=0; i < iValue.length; i++) 
  		{
   			temp1 = "" + iValue.substring(i, i+1);
   			if (valid.indexOf(temp1) == "-1") 
     				{
       				//alert( "Phone Number should not have character \n" );
					document.AgentCompleteSetup.CountryCode.focus();
					return false;
       				break;
     				}
 		}
	
  }

function checkForExists(ilist,iPhone)
 	{
		for(var i=0 ; i < ilist.options.length; i++) 
			{
				if( ilist.options[i].value == iPhone)
					{	
						//alert("This phone no already exists in List \n");
						document.AgentCompleteSetup.CountryCode.focus();						
						phoneExists = true;
						return false;
						break;	
						
       					
					}
			}				

	}

function refresh()
	{
		document.AgentCompleteSetup.PhoneType.value = "B";
		document.AgentCompleteSetup.CountryCode.value = "";
		document.AgentCompleteSetup.AreaCode.value = "";
		document.AgentCompleteSetup.Number.value = "";
		document.AgentCompleteSetup.Ext.value = "";
		document.AgentCompleteSetup.CountryCode.focus();
		document.AgentCompleteSetup.Preference.checked =0;

	}

phoneIK = "0000";
//alert("Before end  Phone IK is :"+phoneIK);
return true;

	
}	// end of popList function

//--------------------------------------------------------------------




//-------------------------------------------------------------------------

function bringBack(box,val)
  {		

	var count=0;
	var lastHyphen = 0;
 	for( var j = 0 ; j < val.length ; j++)
  		{
   		 	if(val.substring(j,j+1) ==":")
     				{
      					count=j+1;
					break;
     				}
  		}
 	for( var j = 0 ; j < val.length ; j++)
  		{
   		 	if(val.substring(j,j+1) =="-")
     				{
      					lastHyphen=j+1;					
     				}
  		}


	var type=0;
	var country=0;
	var area=0;
	var no=0;
	var ext=0;
	var pref = 0;
	var fChar= val.substring(0,1);
	
	for(var fchar = 0 ; fchar < val.length ; fchar++)
		{
			if(val.substring(fchar,fchar+1) !=" ")
				{
					fChar = val.substring(fchar,fchar+1);
					break;
				}
		}

	if(fChar =="P")
 		{
			type="P";
		}
	else if(fChar=="B")
	 	{
			type = "B";
		}
	else if(fChar=="F")
		{
			type = "F";
		}
       else if(fChar =="M")
		{
			type = "M";
		}
	else if (fChar =="R")
		{
			type = "R";
		}

 	country = val.substring(count,count+3);
 	area = val.substring(count+4,count+7);
 	no = val.substring(count+8,count+15);
 	ext = val.substring(count+16,count+19);
	pref = val.substring(lastHyphen-1,lastHyphen-2);
	phoneIK = val.substring(lastHyphen,val.length);

alert("The phoneIK is :"+phoneIK);
 	document.AgentCompleteSetup.PhoneType.value = type;
	document.AgentCompleteSetup.CountryCode.value = country;
	document.AgentCompleteSetup.AreaCode.value = area;
	document.AgentCompleteSetup.Number.value = no;
	document.AgentCompleteSetup.Ext.value = ext;
	
	
	if(pref == "*")
		{
			document.AgentCompleteSetup.Preference.checked = 1;
			oldNo = true;
		}	
	else
		{
	  		document.AgentCompleteSetup.Preference.checked = 0;
			oldNo = true;
		} 

}
function prompt()
{

	for(var count = 0 ; count < document.AgentCompleteSetup.PhoneList.options.length ; count++)
	alert("Count:"+count+"  :"+document.AgentCompleteSetup.PhoneList.options[count].value);
}
</script>
<META name="GENERATOR" content="IBM WebSphere Page Designer V3.5 for Windows">
<META http-equiv="Content-Style-Type" content="text/css">
<TITLE></TITLE>
</HEAD>

<BODY BGCOLOR="#FFFFFF">
<form name = "AgentCompleteSetup" onsubmit="prompt()">
<table><tbody>
<tr><tr><td>
<INPUT type="hidden" name="PhoneNumbers"><SELECT name="PhoneType" tabindex="5">
                          <OPTION value="B" selected>Business</OPTION>
                          <OPTION value="M">Mobile</OPTION>
                          <OPTION value="R">Residence</OPTION>
                          <OPTION value="P">Pager</OPTION>
                          <OPTION value="F">Fax</OPTION>
                        </SELECT></TD>
                              <TD align="center"><INPUT size="3" type="text" maxlength="3" name="CountryCode" tabindex="6"></TD>
                              <TD align="center"><INPUT size="3" type="text" maxlength="3" name="AreaCode" tabindex="7"></TD>
                              <TD align="center"><INPUT size="7" type="text" maxlength="7" name="Number" tabindex="8"></TD>
                              <TD align="center"><INPUT size="3" type="text" maxlength="3" name="Ext" tabindex="9"></TD>
                              <TD align="center"><INPUT type="checkbox" name="Preference" tabindex="10"></TD>
                              <TD></TD>
      <TD><INPUT type="button" name="add" value="Add" onclick="popList(AgentCompleteSetup.PhoneList,AgentCompleteSetup.PhoneType.value,AgentCompleteSetup.CountryCode.value,AgentCompleteSetup.AreaCode.value,
AgentCompleteSetup.Number.value,AgentCompleteSetup.Ext.value,AgentCompleteSetup.Preference.checked)"></TD>
    </TR>
                          </TBODY>
                        </TABLE>
                        <BR>
                        <SELECT size="5" name="PhoneList" onclick="bringBack(PhoneList,this.form.PhoneList.value)" style='font-family : "Courier New";'>
  <OPTION value="F:111-111-1111111-111-9001" selected> Fax:111-111-1111111-111</OPTION>
  <OPTION value="M:222-222-2222222-222-9002"> Mobile:222-222-2222222-222</OPTION>
  <OPTION value="B:333-333-3333333-333-9003"> Business:333-333-3333333-333</OPTION>
</SELECT><BR>
<INPUT type="submit" name="submit" value="Submit"></form>


</BODY>
</HTML>
