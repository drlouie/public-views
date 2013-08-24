<!-- Sample JSP file -->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
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


-->
</STYLE>
<TITLE>
PUR100 Administer Purchaser (Initial Setup)
</TITLE>
</HEAD>

<BODY BGCOLOR="#FFFFFF">
<FORM>
<TABLE width="80%">
  <TBODY>
    <TR>
      <TD bgcolor="#999999">
      <TABLE width="100%" cellpadding="0" cellspacing="0">
        <TBODY>
          <TR>
            <TD class="title" bgcolor="#ffcc00"><FONT color="#0033cc">PUR 100 Administer Purchaser ( Initial Setup )</FONT></TD>
            <TD class="title" align="right" bgcolor="#ffcc00"><IMG src="images/search.gif" width="72" height="22" border="0"><IMG src="images/save.gif" width="50" height="22" border="0"><IMG src="images/print.gif" width="50" height="22" border="0"><IMG src="images/exit.gif" width="50" height="22" border="0"><IMG src="images/comments.gif" width="86" height="22" border="0"></TD>
          </TR>
        </TBODY>
      </TABLE>
      <TABLE cellpadding="1" cellspacing="1" width="100%">
        <TBODY>
          <TR>
            <TD  align="right" class="label">Orig Effective Date</TD>
            <TD align="left">
            <INPUT size="10" type="text" maxlength="10" name="OrigEffectiveDate">
            </TD>
            <TD class="label" align="right">Termination Date</TD>
            <TD align="left">
            <INPUT size="10" type="text" maxlength="10" name="TerminationDate">
            </TD>
            <TD class="label" align="right">Status</TD>
            <TD align="left">
            <SELECT name="Status">
              <OPTION value="P" selected>Pending</OPTION>
              <OPTION value="A">Active</OPTION>
              <OPTION value="O">Obsolete/Expired</OPTION>
              <OPTION value="V">Void</OPTION>
            </SELECT>
            </TD>
            <TD align="right"><IMG src="images/edit.gif" width="50" height="22" border="0"></TD>
            <TD align="right"><IMG src="images/reset.gif" width="50" height="22" border="0"></TD>
          </TR>
          <TR>
            <TD class="label" align="right">Region / Division</TD>
            <TD align="left">
            <SELECT name="RegionDivision">
              <OPTION value="CAL">California</OPTION>
              <OPTION value="NCR">Northern California</OPTION>
              <OPTION value="SCR" selected>Southern California</OPTION>
            </SELECT>
            </TD>
            <TD class="label" align="right">Size (LOB)</TD>
            <TD align="left">
            <SELECT name="Size">
              <OPTION value="LGS" selected>Large Group Sales</OPTION>
              <OPTION value="SGU">Small Group Sales</OPTION>
            </SELECT>
            </TD>
            <TD class="label" align="right">Status Date</TD>
            <TD align="left">
            <INPUT size="10" type="text" maxlength="10" name="StatusDate">
            </TD>
            <TD align="right"></TD>
            <TD align="right"></TD>
          </TR>
          <TR>
            <TD class="label" align="center">PID</TD>
            <TD class="label" align="center">TPA ID</TD>
            <TD class="label" align="left" colspan="3">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name</TD>
            <TD align="right"></TD>
            <TD align="right"></TD>
            <TD align="right"></TD>
          </TR>
          <TR>
            <TD align="center">
            <INPUT size="20" type="text" maxlength="20" name="PID">
            </TD>
            <TD align="center">
            <INPUT size="20" type="text" maxlength="20" name="TPAID">
            </TD>
            <TD colspan="3" align="left">
            <INPUT size="40" type="text" maxlength="40" name="Name">
            </TD>
            <TD align="right"></TD>
            <TD align="right"></TD>
            <TD align="right"></TD>
          </TR>
        </TBODY>
      </TABLE>
      <TABLE cellpadding="1" cellspacing="1" width="80%">
        <TBODY>
          <TR>
            <TD align="center" class = "label">Administration System</TD>
            <TD align="center" class = "label">Administrator</TD>
            <TD align="center" class = "label">Billing Frequency</TD>
            <TD align="center" class = "label">Effective Date</TD>
            <TD align="center" class = "label">End Date</TD>
            <TD><IMG src="images/delete.gif" width="58" height="22" border="0"></TD>
          </TR>
          <TR>
            <TD align="center"><SELECT name="AdministrativeSystem">
              <OPTION value="Aries">HPS N/S</OPTION>
              <OPTION value="KPFS" selected>Foundation System</OPTION>
            </SELECT></TD>
            <TD align="center"><SELECT name="Administrator">
              <OPTION value="HPS">Health Plan Services</OPTION>
              <OPTION value="CSC" selected>California Service Center</OPTION>
            </SELECT></TD>
            <TD align="center"><SELECT name="BillingFrequency">
              <OPTION value="TBD" selected>TBD</OPTION>
            </SELECT></TD>
            <TD align="center"><INPUT size="10" type="text" maxlength="10" name="effDate"></TD>
            <TD align="center"><INPUT size="10" type="text" maxlength="10" name="endDate"></TD>
            <TD><IMG src="images/add.gif" width="50" height="22" border="0"></TD>
          </TR>
          <TR>
            <TD colspan="6"><TEXTAREA rows="11" cols="93"></TEXTAREA></TD>
          </TR>
        </TBODY>
      </TABLE>
      </TD>
    </TR>
  </TBODY>
</TABLE>
</FORM>
</BODY>
</HTML>
