function validateKPStaffForm(theForm)
 {
 for(var i = 0 ; i < theForm.KPStaffList.length ; i++)
 	{
		theForm.ListValues.value+= theForm.KPStaffList.options[i].value;
		theForm.ListValues.value+="%";

	}
	return true;
}