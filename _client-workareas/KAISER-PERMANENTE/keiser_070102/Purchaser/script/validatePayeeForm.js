function validatePayeeForm(theForm)
{
 
 beforeSave();
function beforeSave()
{ 
 	enableform();
 	theForm.payeeBrokerID.disabled = false 
 	theForm.SelectedAction.value = "Save";
}
 

function enableform()
{
	if(theForm.isUpd.value == "yes")
	{
		//document.PayeeBroker.brokerID.disabled = true ;
	}
	else
	{
		//document.PayeeBroker.brokerID.disabled = false ;
	}

	//document.PayeeBroker.brokerName.disabled = false ;
	theForm.effectiveDate.disabled =false;
	theForm.endDate.disabled = false ;
	//document.PayeeBroker.borLetterRecvdDate.disabled = false ;
	theForm.brokerStatus.disabled = false;
}


return true;
}