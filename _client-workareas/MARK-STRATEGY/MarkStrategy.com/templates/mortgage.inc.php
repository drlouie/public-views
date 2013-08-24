<html>
<body>
<SCRIPT LANGUAGE="JavaScript">


function floor(number)
{
  return Math.floor(number*Math.pow(10,2))/Math.pow(10,2);
}

function dosum()
{
  var mi = document.temps.IR.value / 1200;
  var base = 1;
  var mbase = 1 + mi;
  for (i=0; i<document.temps.YR.value * 12; i++)
  {
    base *= mbase;
  }
  document.temps.PI.value = floor(document.temps.LA.value * mi / ( 1 - (1/base)))
}



</SCRIPT>
<h2>Mortgage calculator</h2><br />
<table width="100%" border="0" cellspacing="0" cellpadding="2">
<tr><FORM NAME="temps">
<td><TABLE BORDER=0 cellpadding="3" cellspacing="0">
                      <TD WIDTH=33% class="blue_8"> Length of loan:
                        <select NAME="YR">
                        <option value='10' Selected >10 years</option>          <option value='15'>15 years</option>          <option value='20'>20 years</option>          <option value='25'>25 years</option>          <option value='30'>30 years</option>          <option value='35'>35 years</option>          <option value='40'>40 years</option>
                        </select>
                      <TD WIDTH=33% class="blue_8"> Interest Rate: 
                        <select NAME="IR">
                        	<option value='4'>4%</option>
                        	<option value='4.125'>4.125%</option>
                        	<option value='4.25'>4.25%</option>
                        	<option value='4.375'>4.375%</option>
                        	<option value='4.5'>4.5%</option>
                        	<option value='4.625'>4.625%</option>
                        	<option value='4.75'>4.75%</option>
                        	<option value='4.875'>4.875%</option>
                        	<option value='5'>5%</option>
                        	<option value='5.125'>5.125%</option>
                        	<option value='5.25'>5.25%</option>
                        	<option value='5.375'>5.375%</option>
                        	<option value='5.5'>5.5%</option>
                        	<option value='5.625'>5.625%</option>
                        	<option value='5.75'>5.75%</option>
                        	<option value='5.875'>5.875%</option>
                        	<option value='6' Selected >6%</option>
                        	<option value='6.125'>6.125%</option>
                        	<option value='6.25'>6.25%</option>
                        	<option value='6.375'>6.375%</option>
                        	<option value='6.5'>6.5%</option>
                        	<option value='6.625'>6.625%</option>
                        	<option value='6.75'>6.75%</option>
                        	<option value='6.875'>6.875%</option>
                        	<option value='7'>7%</option>
                        	<option value='7.125'>7.125%</option>
                        	<option value='7.25'>7.25%</option>
                        	<option value='7.375'>7.375%</option>
                        	<option value='7.5'>7.5%</option>
                        	<option value='7.625'>7.625%</option><option value='7.75'>7.75%</option>          <option value='7.875'>7.875%</option>          <option value='8'>8%</option>          <option value='8.125'>8.125%</option>          <option value='8.25'>8.25%</option>          <option value='8.375'>8.375%</option>          <option value='8.5'>8.5%</option>          <option value='8.625'>8.625%</option>          <option value='8.75'>8.75%</option>          <option value='8.875'>8.875%</option>          <option value='9'>9%</option>          <option value='9.125'>9.125%</option>          <option value='9.25'>9.25%</option>          <option value='9.375'>9.375%</option>          <option value='9.5'>9.5%</option>          <option value='9.625'>9.625%</option>          <option value='9.75'>9.75%</option>          <option value='9.875'>9.875%</option>          <option value='10'>10%</option>          <option value='10.125'>10.125%</option>          <option value='10.25'>10.25%</option>          <option value='10.375'>10.375%</option>          <option value='10.5'>10.5%</option>          <option value='10.625'>10.625%</option>          <option value='10.75'>10.75%</option>          <option value='10.875'>10.875%</option>          <option value='11'>11%</option>
                        </select>
                      <TR> 
                      	<TD WIDTH=33% class="blue_8">List Price: 
                          <input type="TEXT" name="LA" onChange="dosum()" size="6" value="<?= $price?>">
                        <TD WIDTH=33% class="blue_8"> 
                          <input type="BUTTON" value="Calculate Now!" onClick="dosum()" class="button" name="BUTTON">
    </TABLE>
	<TABLE BORDER=0 cellspacing="0" cellpadding="3">
                      <TR>
                        <TD class="text" align="left"><b>Results::</b>
                        <TD>&nbsp;
                      <TR> 
                        <TD class="text" align="right">Monthly Prin + Int
                        <TD> 
                          <INPUT TYPE="TEXT" NAME="PI" SIZE="10">
      </TABLE>
</td></FORM></tr>
</table>
<br />
<center>
	<a href="javascript:self.close()">Close window</a>
</center>
</body>
</html>