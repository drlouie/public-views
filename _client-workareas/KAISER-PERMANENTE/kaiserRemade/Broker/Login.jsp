<!-- Sample HTML file -->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML>
<HEAD>
<META name="GENERATOR" content="IBM WebSphere Page Designer V3.5 for Windows">
<META http-equiv="Content-Style-Type" content="text/css">
<TITLE>
Broker Administration system Exchange - Login Page
</TITLE>
<LINK href="theme/Master.css" rel="stylesheet" type="text/css">
<STYLE>
<!--
.lable {
	COLOR : #0067FF; 
	font-family: verdana,arial,helvetica;
	font-size : 11px;
	font-weight : bold;
	font-style: normal;	
	}
.input {
	COLOR : #000000; 
	font-family: verdana, arial, sans-serif;
	font-size : 11px;
	font-weight : normal;
	font-style: normal;	
	}
.title {
	COLOR : #FF6633; 
	font-family: verdana, arial, sans-serif;
	font-size : 12px;
	font-weight : bold;
	font-style: normal;	
	}
IMG{
  color : olive;
}
TABLE{
  background-color : ;
}
-->
</STYLE>
<SCRIPT language="JavaScript">

function validateForm(form)
	{
		var username = document.login.username.value;
		var password = document.login.password.value;
		var status = false;
	if(username =="")
		{
		alert("Enter the Username");
		document.login.username.focus();
		}
	else if ( password =="")
		{
		alert("Enter the Password");
		document.login.password.focus();
		}
	else if (username.length < 4 && password.length < 4)
		{
		alert("Username and Password should be atleast 4 characters");
		document.login.username.focus();
		}
	else if (username.length < 4)
		{
		alert("Username should be atleast 4 characters");
		document.login.username.focus();
		}
	else if (password.length < 4)
		{
		alert("Password should be atleast 4 characters");
		document.login.password.value = "";
		document.login.password.focus();
		}
	
	else
		status= true;
	return status;
	}
</SCRIPT>
</HEAD>

<BODY link="#0033cc" alink="#0033cc" vlink="#0033cc" BGCOLOR="#FFFFFF">
<TABLE width="100%">
  <TBODY>
    <TR>
      <TD colspan="2" align="center"><IMG src="images/mainlogo.gif" width="200" height="74" border="0"></TD>
    </TR>
    <TR>
      <TD colspan="2"></TD>
    </TR>
  </TBODY>
</TABLE>
<CENTER>
<TABLE width="50%">
  <TBODY>
    <TR>
<!--     <TD align="center" style="background-color : white;color : navy;"><B><IMG src="welcome2.gif" width="200" height="25" border="0"></B></TD> -->
	<TD align="center"><H2>Welcome to</H2></TD>
    </TR>
    <TR>
      <TD align="center"><H1><FONT color="#333333">BASE</FONT></H1>



</TD>
    </TR>
  </TBODY>
</TABLE>
</CENTER>
<CENTER><BR>

</CENTER>
<CENTER>
<form name="login" method="post" action="LoginServlet" onsubmit = " return validateForm()">
<TABLE width="629" cellspacing="2">
  <TBODY>
    <TR>
      <TD></TD>
      <TD></TD>
      <TD></TD>
      <TD></TD>
    </TR>
    <TR>
      <TD rowspan="3"></TD>
      <TD rowspan="3" width="82" align="center"><IMG src="images/commssion1.gif" width="150" height="88" border="0"></TD>
      <TD>
      <TABLE border="0" cellpadding="2" cellspacing="0" width="40%">
    <tr>
      <td valign="top" width=1%>
      <TABLE bgcolor="#a0b8c8" border="0" cellpadding="2" cellspacing="0" width="240">
<tr><td>

<table bgcolor="#eeeeee" border="0" cellpadding="2" cellspacing="0" width="100%"> 
<tr>
                        <TD bgcolor="#ffffff">
                        <TABLE border="0" cellspacing="3" cellpadding="3" bgcolor="#000000">
<tr bgcolor="eeeeee">
                              <TD width="214" align="center"> <font face="arial"><b>Existing users</b></font><br>
<font face="arial" size="-1">&nbsp;Enter your ID and password to sign in&nbsp; </font>
                        <TABLE border="0" cellpadding="4" cellspacing="0" width="40%">
<tr> <td align="right">
<form name="login" method="post" action="LoginServlet" onsubmit="return validateForm();">
<table border="0" cellpadding="2" cellspacing="0">
<tr> <td align="right" nowrap><font face="arial" size="-1">User ID:</font></td>
<td><INPUT name="username" size="17" maxlength="32" tabindex="1" type="text"></td>
</tr>
<tr> <td align="right" nowrap><font face="arial" size="-1">Password:</font></td>
<td><INPUT name="password" type="password" size="17" maxlength="32" tabindex="2"></td></tr>
                                </table> 

</td></tr>
                          </TABLE>
                              <INPUT type="image" src="images/signin1.gif" border="0" name="submit" value="join" tabindex="3" alt="Join"></TD>
                            </tr>
                    </TABLE>
                        </TD>

                      </tr></table>
</td></tr></TABLE>
<script language = "javascript">
<!--
document.login.username.focus();
//-->
</script>

      </td>
    </tr>
  </TABLE>
      </TD>
      <TD></TD>
    </TR>
    <TR>
      <TD></TD>
      <TD></TD>
    </TR>
    <TR>
      <TD></TD>
      <TD></TD>
    </TR>
    <TR>
      <TD></TD>
      <TD></TD>
      <TD></TD>
      <TD></TD>
    </TR>
    <TR>
      <TD></TD>
      <TD colspan="2" align="center"><FONT FACE="Arial, Helvetica, sans-serif" SIZE="-2"><IMG src="images/smalllogo.gif" width="81" height="23" border="0"> 
    copyright
    2001 Kaiser Permanente California. Please read our disclaimer.</FONT></TD>
      <TD></TD>
    </TR>
  </TBODY>

</TABLE>
</form>
</CENTER>

</BODY>
</HTML>
