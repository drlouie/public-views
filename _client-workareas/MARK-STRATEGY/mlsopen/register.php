<?php
require 'settings.php';
include 'header.inc';

?>

<br><center><b><?php echo "$site_name";?> User Registration</b></center>
<br><center>Please submit the form below to start listing your properties on <?php echo "$site_name";?>.<br>Please note fields marked with a <font color=red><b>*</b></font> are required fields.</center><br>
<div align=center>
<table>
<form action=welcome.php method=post>
<tr><td>Name:</td><td><input type=text name=u_name size=40><font color=red><b>*</b></font></td></tr>
<tr><td>Company:</td><td><input type=text name=u_company size=40></td></tr>
<tr><td>Address:</td><td><input type=text name=u_address size=40><font color=red><b>*</b></font></td></tr>
<tr><td>City:</td><td><input type=text name=u_city size=40><font color=red><b>*</b></font></td></tr>
<tr><td>State:</td><td><input type=text name=u_state size=40><font color=red><b>*</b></font></td></tr>
<tr><td>Zip Code:</td><td><input type=text name=u_zip size=40><font color=red><b>*</b></font></td></tr>
<tr><td>Country:</td><td><input type=text name=u_country size=40><font color=red><b>*</b></font></td></tr>
<tr><td>Email Address:</td><td><input type=text name=u_email size=40><font color=red><b>*</b></font></td></tr>
<tr><td>Phone Number:</td><td><input type=text name=u_phone size=40><font color=red><b>*</b></font></td></tr>
<tr><td>Desired User Name:</td><td><input type=text name=uname size=40><font color=red><b>*</b></font></td></tr>
<tr><td>Password:</td><td><input type=password name=upass size=40><font color=red><b>*</b></font></td></tr>
</table></div>
<center>By registering with <?php echo "$site_name";?> you agree to the <a href=terms.html>Terms and Conditions</a></center><br>
<center><input type=submit value="Register with <?php echo "$site_name";?>"></center>
</form>

<?php
include 'footer.inc';
?>
