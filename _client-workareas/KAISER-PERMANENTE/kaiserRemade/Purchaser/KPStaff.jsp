<!-- Sample JSP file --> <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
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
-->
</STYLE>
<TITLE>PUR100 Administer Purchaser (KP Staff)</TITLE>
<SCRIPT language="JavaScript">


function validateForm(theForm)
 {
 for(var i = 0 ; i < theForm.KPStaffList.length ; i++)
 	{
		theForm.ListValues.value+= theForm.KPStaffList.options[i].value;
		theForm.ListValues.value+="%";

	}	
}

var oldValue = "false";
var nameIK = "0000";
var indicator = "";
//var disableList = true;
function addToList(list,role,honor,first,middle,last,suffix,clicked)
 { 	
	if(clicked == "Add")
	{
		if(!validateIndividualField())
		{
			return false;
		}
	}

	if(role == "" && clicked == "Add")
		{
			alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.kpstaff.RoleTypeRequired")%>");
			return false; 
		}
	
	else if(first == "" && clicked == "Add")
		{
			alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.kpstaff.FirstNameRequired")%>");
			return false;
		}
	else if(last == "" && clicked == "Add")
		{
			alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.kpstaff.LastNameRequired")%>");
			return false;
		}
		

	var elementsMaxLength = new Array();
	var elementsText = new Array();
	var elementsValue = new Array();
	
        
/* Added by Sabari on Jan.31.2002 */
     if ( honor == "" )
		honor = " ";
	if( middle == "" )
		middle = " ";
	if( suffix == "" )
		suffix = " ";
		

			
	elementsText[0] = role;
    elementsText[1] = honor;
	elementsText[2] = first;
	elementsText[3] = middle;	
	elementsText[4] = last;	
	elementsText[5] = suffix;	

	elementsMaxLength[0] = 15;
	elementsMaxLength[1] = 10;
	elementsMaxLength[2] = 20;
	elementsMaxLength[3] = 5; 
	elementsMaxLength[4] = 20;
	elementsMaxLength[5] = 11;


	if(role == "SE")
		elementsText[0] = "Sales Executive";	
	else if(role == "AM")
		elementsText[0] = "Account Manager";

	for(var i = 0 ; i < elementsMaxLength.length; i++)
		{	
			
			elementsValue[i] =  elementsText[i];	
			if(elementsText[i].length < elementsMaxLength[i])
				{	
					
						for(j = elementsText[i].length ; j < elementsMaxLength[i]; j++)
						{			
							elementsText[i]+= " ";							
						}
					
					
				}
			else
				elementsText[i] = elementsText[i].substring(0,elementsMaxLength[i] );
			
		}
			
	elementsValue[0] = role;
	var addInToList = new Option();

	if(clicked == "Add")
		{
			addInToList.text = elementsText[0]+" "+elementsText[1]+" "+elementsText[2]+" "+elementsText[3]+" "+elementsText[4]+" "+elementsText[5]+" "+"U";
			addInToList.value = elementsValue[0]+"-"+elementsValue[1]+"-"+elementsValue[2]+"-"+elementsValue[3]+"-"+elementsValue[4]+"-"+elementsValue[5]+"-"+nameIK+"-"+"U";
		}
	/*	
	if(clicked == "Add" && oldValue == "true")
		{
			addInToList.text = elementsText[0]+" "+elementsText[1]+" "+elementsText[2]+" "+elementsText[3]+" "+elementsText[4]+" "+elementsText[5]+" "+"";
			addInToList.value = elementsValue[0]+"-"+elementsValue[1]+"-"+elementsValue[2]+"-"+elementsValue[3]+"-"+elementsValue[4]+"-"+elementsValue[5]+"-"+nameIK+"-"+"C";
		}
	*/	
	else if (clicked == "Delete")
		{
			
			addInToList.text = elementsText[0]+" "+elementsText[1]+" "+elementsText[2]+" "+elementsText[3]+" "+elementsText[4]+" "+elementsText[5]+" "+"D";
			addInToList.value = elementsValue[0]+"-"+elementsValue[1]+"-"+elementsValue[2]+"-"+elementsValue[3]+"-"+elementsValue[4]+"-"+elementsValue[5]+"-"+nameIK+"-"+"D";
		}
	var listLength = document.KPStaff.KPStaffList.length;	
	if((indicator == "A" || indicator == "D") && clicked == "Add")
		{
			var empRoleCount = getValidEmployeeRoleCount(list,role);
			if(empRoleCount < 1 )
				{

					document.KPStaff.KPStaffList.style.visibility = "";
					document.KPStaff.KPStaffList.options[listLength] = addInToList;
				}
			else
				{
					alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.kpstaff.SameRoleType")%>"+elementsText[0]);
					//refresh();					
					return false;
				}
		}
	else if(indicator == "A" && clicked == "Delete")
		{
			alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.RecordDeletedSaved")%>");
			refresh();
			return false;
		}
	else if(indicator == "D" && clicked == "Delete")
	{
			alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.RecordDeleted")%>");
			refresh();
			return false;
	}
	else if(oldValue == "false" && clicked == "Add")
		{
			var empRoleCount = getValidEmployeeRoleCount(list,role);
			if(empRoleCount < 1 )
				{

					document.KPStaff.KPStaffList.style.visibility = "";				
					//document.KPStaff.KPStaffList.options[listLength] = addInToList;
					pushAllKPStaffOneStepDown(document.KPStaff.KPStaffList);
					document.KPStaff.KPStaffList.options[0] = addInToList;
				}
			else
				{
					alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.kpstaff.SameRoleType")%>"+elementsText[0]);					
					return false;
				}
		}
		
	else if (oldValue == "true" && clicked == "Add")
		{
			var empRoleCount = getValidEmployeeRoleCount(list,role);
			if(empRoleCount < 1)
				{
					document.KPStaff.KPStaffList.style.visibility = "";
					for(i = 0 ; i < listLength ; i++)
						{
							if(list.options[i].selected)
								{									
									document.KPStaff.KPStaffList.options[i] = addInToList;		
								}
						}						
					
				}
			else
				{
					alert(elementsText[0]+"<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.kpstaff.RoleTypeExists")%>");
					refresh();
					return false;
				}
		}	
			
	else if (oldValue == "true" && clicked == "Delete")
		{
			for(i = 0 ; i < listLength ; i++)
				{
					if(list.options[i].selected)
						{

							document.KPStaff.KPStaffList.options[i] = addInToList;		
							
						}
				}
		}
	else if (oldValue == "false" && clicked == "Delete")
		{
			alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.EmptyDelete")%>");
			refresh();
			return false;
		}	
	oldValue = "false";
	//disableList = false;
	document.KPStaff.KPStaffList.disabled = false;
	nameIK = "0000";
	refresh();	
	return false;
	
}
function pushAllKPStaffOneStepDown(list)
{	
	var extraRow = new Option();
	extraRow.text = '';
	extraRow.value = '';	
	list.options[list.options.length] = extraRow;						
					for(var j = list.options.length ; j >1 ; j--)  
						{	
							list.options[j-1].value = list.options[j-2].value;
							list.options[j-1].text = list.options[j-2].text;
											
						}										
}
function getValidEmployeeRoleCount(list,role)
 {
	var roleCount = 0;
 	for(i = 0 ; i < list.length ; i++)
			{
				if(!list.options[i].selected)	
				{
				var roleType = list.options[i].value;
				var indicatorStatus = roleType.substring(roleType.length,roleType.length-1)					
				if(roleType.substring(0,2) == role && ( indicatorStatus == "C" || indicatorStatus == "U") )
					roleCount++;
				}
			}				
	return roleCount;
 }

function refresh()
 {
	document.KPStaff.Honorific.value = '';
	document.KPStaff.FirstName.value = '';
	document.KPStaff.MiddleName.value = '';
	document.KPStaff.LastName.value = '';
	document.KPStaff.Suffix.value = '';
	document.KPStaff.KPEmployeeRole.value = '';
	document.KPStaff.KPEmployeeRole.focus();
 }

function bringBackToEdit(list,val)
 { 	
	refresh();
	oldValue = "true";
	var pre=0;	
	var post = 0;
	var lastHyphenCount = 0;
	var noOfElements = 0;	
	var firstHyphen = 0 ; 
	var eValue = new Array();
	for( var j = 0 ; j < val.length ; j++)
  		{		
   		 	if(val.substring(j,j+1) =="-")
     				{
      					post=j;					
					eValue[noOfElements]=val.substring(pre,post);										
					lastHyphenCount = j+1;
					noOfElements++;
					firstHyphen++;
     				}
			if(firstHyphen >= 1)
				pre = post+1;  
			
		}
	eValue[noOfElements] = val.substring(lastHyphenCount,val.length);	
	nameIK = eValue[6];	
	indicator = eValue[7];//put first bz to avoid in displaying in the editable fields
	/*if(indicator == 'H')
		{
			alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.DoNotModifyHistory")%>");
			return false;
		}*/
	if(indicator == 'A' || indicator == "D" )
		{
			nameIK = "0000";
			//alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.DoNotModifyHistory")%>");
			//return false;
		} 
	if(eValue[0] != null)
		{
	if(eValue[1] == " ")
		eValue[1] = "";
	if(eValue[3] == " ")
		eValue[3] = "";
	if(eValue[5] == " ")
		eValue[5] = "";	
	document.KPStaff.KPEmployeeRole.value = eValue[0];
	document.KPStaff.Honorific.value = eValue[1];
	document.KPStaff.FirstName.value = eValue[2];
	document.KPStaff.MiddleName.value = eValue[3];
	document.KPStaff.LastName.value = eValue[4];
	document.KPStaff.Suffix.value = eValue[5];
		}
	
	
}
function validateIndividualField(name,value)
 {
alert(value);
	var Name = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";	
	var valid = "";
	if(name == "Honorific" || name == "FirstName" || name == "MiddleName" || name == "LastName" || name == "Suffix")
		{
			valid = Name;
		}
	if(valid.length > 1)
		{
	 		for (var i=0; i < value.length; i++) 
	  			{
					temp = "" + value.substring(i, i+1);
					if (valid.indexOf(temp) == "-1") 
     						{
							alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.InvalidChar")%>"+name);							
       						break;
     						}
  				}
 		}

 }//enf of validateIndividualField
	
/*
function hideList()
 {
	document.KPStaff.KPStaffList.style.visibility = "hidden";
	document.KPStaff.KPEmployeeRole.value = '';
	
 }
*/
function enableList()
 {	
	document.KPStaff.KPStaffList.disabled = false;	

	
 }

function init()
 {
		//parent.tops.document.PurTop.dynamic.value = "PUR106 Administer Purchaser ( KP Staff )";
 		document.KPStaff.KPEmployeeRole.value = "";
		document.KPStaff.KPStaffList.style.visibility = "hidden";
             
		<%
			java.util.Vector kpsText1 = new java.util.Vector();
			java.util.Vector kpsValue1 = new java.util.Vector();						
			kpsText1 = (java.util.Vector)session.getAttribute("KPStaffText");
			kpsValue1 = (java.util.Vector)session.getAttribute("KPStaffValue");
			if(kpsText1.size() != 0)
			{
		%>	  
			document.KPStaff.KPStaffList.style.visibility = "";
			document.KPStaff.KPStaffList.disabled = true;
		<%		
			}
		%>
                
		document.KPStaff.PurchaserIK.value = <%=(String)session.getAttribute("PurchaserIK")%>;
 }		
function makeFormEditable()
{
	document.KPStaff.reset();
	document.KPStaff.KPEmployeeRole.value = "";
}
function validateIndividualField()
{
var errorStatus = false;
var errorFields ="";
	var theForm = document.KPStaff;
if ( theForm.Honorific.value != ""  ) 
	{
		validateIndividualField(theForm.Honorific.name,theForm.Honorific.value)
	}
if ( theForm.FirstName.value == ""  ) 
	{
		errorFields += "\n" + "<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Name.FirstNameMissing")%>";
		errorStatus = true;		
	}
else
	{
		validateIndividualField(theForm.FirstName.name,theForm.FirstName.value)
	}	
if ( theForm.MiddleName.value != ""  ) 
	{
		validateIndividualField(theForm.MiddleName.name,theForm.MiddleName.value)
	}
if ( theForm.LastName.value == ""  ) 
	{
		errorFields += "\n" + "<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Name.LastNameMissing")%>";
		errorStatus = true;		
	}
else
	{
		validateIndividualField(theForm.LastName.name,theForm.LastName.value)
	}
if ( theForm.Suffix.value != ""  ) 
	{
		validateIndividualField(theForm.Suffix.name,theForm.Suffix.value)
	}
 if (errorStatus == true)
   {
	alert( errorFields +  "\n" + "<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.ErrorMessagePrefix")%>"); 
	return false;
   }
return true;
function validateIndividualField(name,value)
 {	
	var Name = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";	
	var valid = "";
	if(name == "Honorific" || name == "FirstName" || name == "MiddleName" || name == "LastName" || name == "Suffix")
		{
			valid = Name;
		}
	if(valid.length > 1)
		{
	 		for (var i=0; i < value.length; i++) 
	  			{
					temp = "" + value.substring(i, i+1);
					if (valid.indexOf(temp) == "-1") 
     						{
							errorFields+="\n"+"<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.InvalidChar")%>"+name;	
							errorStatus = true;
							break;
     						}
  				}
 		}

 }//enf of validateIndividualField
}
</SCRIPT></HEAD>
<BODY bgcolor="#999999" onload = "init()">
<FORM name="KPStaff" method="post" onsubmit="return validateForm(KPStaff)" action="KPStaffServlet" target = "_parent">

<TABLE border="1" width="%">
  <TBODY>
    <TR>
      <TD>
      <TABLE>
        <TBODY>
          <TR>
            <TD>
            <TABLE width="%" cellpadding="1" cellspacing="1">
              <TBODY>
                <TR>
                  <TD></TD>
                  <TD></TD>
                  <TD></TD>
                  <TD colspan="3" align="right"><!-- <INPUT type="image" src="/BASEWeb/Purchaser/images/save.gif" name="submit" width="50" height="22" border="0" alt = "Save"> --></TD>
                                    <TD align="right"><IMG src="images/edit.gif" width="50" height="22" border="0" alt="Edit" onclick="enableList()"></TD>
                                    <TD align="left"><IMG src="images/reset.gif" width="50" height="22" border="0" alt="Reset" onclick = "makeFormEditable()"></TD>
                                </TR>
                <TR>
                  <TD><INPUT type="hidden" name="PurchaserIK" value="">
		      <INPUT type="hidden" name="WhereToGo" value="">
		      <INPUT type="hidden" name="FromWhere" value="0">
		      <INPUT type="hidden" name="SelectedAction" value="FromJSP"></TD>
                  <TD colspan="2" class="label"></TD>
                  <TD align="center" colspan="3" class="label"></TD>
                                    <TD></TD>
                                    <TD align="left"></TD>
                                </TR>
                <TR>
                  <TD class="label">KP Employee Role</TD>
                  <TD class="label" align="center">Honor</TD>
                  <TD align="center" class="label">First</TD>
                  <TD align="center" class="label">Middle</TD>
                  <TD align="center" class="label">Last</TD>
                  <TD align="center" class="label">Suffix</TD>
                                    <TD></TD>
                                    <TD align="center" width="71"><INPUT size="20" type="button" maxlength="20" name="Delete" value="Delete" class="pbttn" onclick="addToList(document.KPStaff.KPStaffList,document.KPStaff.KPEmployeeRole.value,document.KPStaff.Honorific.value,document.KPStaff.FirstName.value,document.KPStaff.MiddleName.value,document.KPStaff.LastName.value,document.KPStaff.Suffix.value,this.value)"></TD>
                                   <!--  <TD><IMG src="images/delete.gif" alt="Delete" value="Delete" onclick="addToList(document.KPStaff.KPStaffList,document.KPStaff.KPEmployeeRole.value,document.KPStaff.Honorific.value,document.KPStaff.FirstName.value,document.KPStaff.MiddleName.value,document.KPStaff.LastName.value,document.KPStaff.Suffix.value,this.value)"></TD> -->
                                </TR>
                <TR>
                  <TD><SELECT name="KPEmployeeRole" tabindex="1">
                                        <OPTION value="SE">Sales Executive</OPTION>
                                        <OPTION value="AM">Account Manager</OPTION>
                                    </SELECT></TD>
                  <TD><INPUT type="hidden" name="ListValues" value=""><INPUT size="9" type="text" name="Honorific" maxlength="10" style='font-family : "Courier New";' tabindex="2"></TD>
                  <TD align="right"><INPUT size="20" type="text" maxlength="25" name="FirstName" tabindex="3" style='font-family : "Courier New";' ></TD>
                  <TD><INPUT size="5" type="text" maxlength="25" name="MiddleName" tabindex="4" style='font-family : "Courier New";' ></TD>
                  <TD><INPUT size="20" type="text" maxlength="25" name="LastName" tabindex="5" style='font-family : "Courier New";'></TD>
                  <TD><INPUT size="10" type="text" maxlength="20" name="Suffix" tabindex="6" style='font-family : "Courier New";'></TD>
                                    <TD class = "label">Indicator</TD>
                                    <TD align="center" width="71"><INPUT size="20" type="button" maxlength="20" name="Add" value="Add" class="pbttn" onclick="return addToList(document.KPStaff.KPStaffList,document.KPStaff.KPEmployeeRole.value,document.KPStaff.Honorific.value,document.KPStaff.FirstName.value,document.KPStaff.MiddleName.value,document.KPStaff.LastName.value,document.KPStaff.Suffix.value,this.value)" tabindex="7"></TD>
                                    <!-- <TD align="left"><INPUT type = "image" src="images/add.gif" value="Add" width="50" height="22" border="0" alt="Add" onclick="return addToList(document.KPStaff.KPStaffList,document.KPStaff.KPEmployeeRole.value,document.KPStaff.Honorific.value,document.KPStaff.FirstName.value,document.KPStaff.MiddleName.value,document.KPStaff.LastName.value,document.KPStaff.Suffix.value,this.value)" tabindex="7"></TD> -->
                                </TR>
              </TBODY>
            </TABLE>
            </TD>
          </TR>
        </TBODY>
      </TABLE>
      <TABLE>
        <TBODY>
          <TR>
            <TD><SELECT size="6" name="KPStaffList" onclick="bringBackToEdit(KPStaffList,this.form.KPStaffList.value)" style='font-family : "Courier New";'>		
		<%
			java.util.Vector kpsText = new java.util.Vector();
			java.util.Vector kpsValue = new java.util.Vector();						
			kpsText = (java.util.Vector)session.getAttribute("KPStaffText");
			kpsValue = (java.util.Vector)session.getAttribute("KPStaffValue");
				
			if(kpsText != null)
			{			
			for(int i = 0 ; i < kpsText.size(); i++)
				{	
		%>
			
			<option value = '<%=kpsValue.elementAt(i)%>'><%=kpsText.elementAt(i)%></option>
			
		<%
				}
			}				
		%>				
</SELECT></TD>
          </TR>
        </TBODY>
      </TABLE>
      <BR>
      <BR>
      <BR>
      </TD>
    </TR>
  </TBODY>
</TABLE>
</FORM>
</BODY>
</HTML>