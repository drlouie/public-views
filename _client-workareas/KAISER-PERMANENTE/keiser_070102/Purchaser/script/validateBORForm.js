function validateBORForm(theForm)
{

beforeSave();

function beforeSave( )
{
	enableform();
	theForm.brokerID.disabled = false 
 	theForm.SelectedAction.value = "Save";
}



function enableform()
{
	if(theForm.isUpd.value == "yes")
	{
		theForm.brokerID.disabled = true ;
	}
	else
	{
		theForm.brokerID.disabled = false ;
	}


	theForm.brokerName.disabled = false ;
	theForm.effectiveDate.disabled =false;
	theForm.endDate.disabled = false ;
	theForm.borLetterRecvdDate.disabled = false ;
	theForm.brokerStatus.disabled = false;

}
return true;
}
