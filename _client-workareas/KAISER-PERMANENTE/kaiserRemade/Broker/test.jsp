<!-- Sample JSP file -->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML>
<HEAD><BASE href="file:///X:/Projects/base/STUDIO~1/test.jsp">
<META name="GENERATOR" content="IBM WebSphere Page Designer V3.5.3 for Windows">
<META http-equiv="Content-Style-Type" content="text/css">
<TITLE>
Put Your Title Here
</TITLE>
<script language = "javascript">
function makeMultiple()
{
	for(var i = 0 ; i < document.test.elements.length; i++)
		{
			if(document.test.elements[i].type == 'select-one')
				{
					var name = document.test.elements[i].name;					
					for(var j = 0 ; j < name.length; j++)
						{
							alert(name.length);
							alert(document.test.elements[i].options[j].value);
						}

				}
		}
	
	
}
</script>
</HEAD>

<BODY BGCOLOR="#FFFFFF">
<FORM name = "test" ><BR>
Name : <INPUT size="20" type="text" name="FName"><BR>
Enter your country :<SELECT  name="Country">
  <OPTION value="USA">USA</OPTION>
  <OPTION value="IND">IND</OPTION>
  <OPTION value="CAN">CAN</OPTION>
</SELECT><BR>
<INPUT type="submit" name="Click" value="Submit" onClick = "makeMultiple()"></FORM>
</BODY>
</HTML>
