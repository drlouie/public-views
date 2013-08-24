/*
ShadowValidation
----------------

Generic Form Validation.
To activate this validation, add attributes to your form elements.
Attribute "validate" defines what type of validation you want.
Possible values for "validate" attribute:
	"not_empty" - element can't be empty.
	"integer" - element must have integer value.
	"number" - element must have numeric value.
	"email" - element value must be valid email address.
	[function name] - vaidate using your own function. see below for more details.
You can join more than one validation type by using the "|" character.
For example:
	<input type="text" name="myinput" validate="not_empty|number" />
	will force not empty and numeric value.
Attribute "msg" defines the message to display when validation fails.
For example:
	<input type="text" name="myinput" validate="not_empty|number" msg="please enter value|invalid value" />
	will show "please enter value" if value is empty and "invalid value" if not numeric.
By default, the message will appear next to the form element.
You can have the message appear as alert dialog by adding show_alert attribute to the form.
For example:
	<form show_alert="1" onsubmit="return Validate(this);">
	will show the messages as alerts.

Advanced:
	You can use your own function to validate the data.
	For this, write the function name as the value of "validate" attribute.
	For example:
		<input type="text" name="myinput" validate="MyValidate" />
	The function must get the form element as its parameter and return true if valid or false otherwise.


Written by:
	© Shadow Wizard, 2006

*/

function Validate(objForm) {
	var arrValidated=new Array();
	
	for (var i=0; i<objForm.elements.length; i++) {
		var element=objForm.elements[i];
		var elName=element.name;
		if ((!elName)||(elName.length == 0)||(arrValidated[elName]))
			continue;
		arrValidated[elName] = true;
		var validationType = element.getAttribute("validate");
		if ((!validationType)||(validationType.length == 0))
			continue;
		var strMessages=element.getAttribute("msg");
		if (!strMessages)
			strMessages = "";
		var arrMessages = strMessages.split("|");
		var arrValidationTypes = validationType.split("|");		
		for (var j=0; j<arrValidationTypes.length; j++) {
			var curValidationType = arrValidationTypes[j];
			var blnValid=true;
			switch (curValidationType) {
				case "not_empty":
					blnValid = ValidateNotEmpty(element);
					break;
				case "integer":
					blnValid = ValidateInteger(element);
					break;
				case "number":
					blnValid = ValidateNumber(element);
					break;
				case "email":
					blnValid = ValidateEmail(element);
					break;
				default:
					try {
						blnValid = eval(curValidationType+"(element)");
					}
					catch (ex) {
						blnValid = true;
					}
			}
			if (blnValid == false) {
				var message="invalid value for "+element.name;
				if ((j < arrMessages.length)&&(arrMessages[j].length > 0))
					message = arrMessages[j];
				InsertError(element, message);
				if ((typeof element.focus == "function")||(element.focus)) {
					element.focus();
				}
				return false;
			}
			else
				ClearError(element);
		}
		
	}
	
	return true;
}

function ValidateNotEmpty(objElement) {
	var strValue = GetElementValue(objElement);
	return (strValue.length > 0);
}

function ValidateInteger(objElement) {
	var strValue = GetElementValue(objElement);
	return (!isNaN(parseInt(strValue)));
}

function ValidateNumber(objElement) {
	var strValue = GetElementValue(objElement);
	return (!isNaN(parseFloat(strValue)));
}

function ValidateEmail(objElement) {
	var strValue = GetElementValue(objElement);
	if (strValue.length < 5)
		return false;
	var arrTemp=strValue.split("@");
	if (arrTemp.length != 2)
		return false;
	var strLeftPart = arrTemp[0];
	var strRightPart = arrTemp[1];
	if ((strLeftPart.length == 0)||(strRightPart.length == 0))
		return false;
	arrTemp = strRightPart.split(".");
	if (arrTemp.length < 2)
		return false;
	for (var i=0; i<arrTemp.length; i++) {
		if (arrTemp[i].length == 0)
			return false;
	}
	return true;
}

function GetElementValue(objElement) {
	var result="";
	switch (objElement.type) {
		case "text":
		case "hidden":
		case "textarea":
		case "password":
			result = objElement.value;
			break;
		case "select-one":
		case "select":
			if (objElement.selectedIndex >= 0)
				result = objElement.options[objElement.selectedIndex].value;
			break;
		case "radio":
		case "checkbox":
			for (var i=0; i<objElement.form.elements.length; i++) {
				if (objElement.form.elements[i].name == objElement.name) {
					if (objElement.form.elements[i].checked)
						result += objElement.form.elements[i].value+",";
				}
			}
			break;
	}
	return result;
}

function InsertError(element, strMessage) {
	if ((element.form.getAttribute("show_alert")) && (element.form.getAttribute("show_alert") != "0")) {
		alert(strMessage);
		return;
	}
	
	var strSpanID = element.name+"_val_error";
	var objSpan = document.getElementById(strSpanID);
	if (!objSpan) {
		if ((element.type == "radio")||(element.type == "checkbox")) {
			for (var i=0; i<element.form.elements.length; i++) {
				if (element.form.elements[i].name == element.name) {
					element = element.form.elements[i];
				}
			}
		}
		objSpan = document.createElement("span");
		objSpan.id = strSpanID;
		objSpan.className = "validation_error";
		var nodeAfter=0;
		var nodeParent = element.parentNode;
		for (var i=0; i<nodeParent.childNodes.length; i++) {
			if (nodeParent.childNodes[i] == element) {
				if (i < (nodeParent.childNodes.length-1))
					nodeAfter = nodeParent.childNodes[i+1];
				break;
			}
		}
		if ((!nodeAfter)&&(nodeParent.parentNode)) {
			nodeParent = nodeParent.parentNode;
			for (var i=0; i<nodeParent.childNodes.length; i++) {
				if (nodeParent.childNodes[i] == element.parentNode) {
					if (i < (nodeParent.childNodes.length-1))
						nodeAfter = nodeParent.childNodes[i+1];
					break;
				}
			}
		}
		if (nodeAfter)
			nodeParent.insertBefore(objSpan, nodeAfter);
		else
			document.body.appendChild(objSpan);
	}
	objSpan.innerHTML = strMessage;
}

function ClearError(element) {
	var strSpanID = element.name+"_val_error";
	var objSpan = document.getElementById(strSpanID);
	if (objSpan) {
		objSpan.innerHTML = "";
	}
}