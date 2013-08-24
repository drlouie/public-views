<?php
require 'settings.php';
include 'header.inc';

print "<div align=\"center\">
  <center>
  <table border=\"0\" width=\"522\" height=\"151\">
    <tr>
      <td width=\"522\" height=\"38\" colspan=\"3\">
        <p align=\"center\"><font size=\"4\">Advanced Search</font></td>
    </tr>
    <tr><form action=search_price.php method=post>
      <td width=\"154\" height=\"28\">Price Range:</td>
      <td width=\"192\" height=\"28\">
          <p><select size=\"1\" name=\"price\">
            <option value=\"49000\">$0 - $49,000</option>
            <option value=\"49001\">$49,001 - $75,000</option>
            <option value=\"75001\">$75,001 - $125,000</option>
            <option value=\"125001\">$125,001 - $250,000</option>
            <option value=\"250001\">$250,001 - $500,000</option>
            <option value=\"500001\">$500,001 - $750,000</option>
            <option value=\"750001\">$750,001 and up</option>
          </select></p>
        
 </td>
      <td width=\"152\" height=\"28\"> 
        <input type=submit value=\"Search by Price\"></td>
    </form></tr>
    <tr><form action=search_features.php method=post>
      <td width=\"157\" height=\"21\">Features:</td>
      <td width=\"192\" height=\"21\"><input type=text name=features size=20></td>
      <td width=\"152\" height=\"21\"><input type=submit value=\"Search by Feature\"></td>
    </form></tr>
    <tr><form action=search_option.php method=post>
      <td width=\"157\" height=\"24\">Options</td>
      <td width=\"192\" height=\"24\"><input type=text name=option size=5> <select size=\"1\" name=\"option_type\">
          <option>Bedrooms</option>
          <option>Baths</option>
          <option>Half-Baths</option>
          <option>Square Feet</option>
          <option>Acres</option>
        </select></td>
      <td width=\"152\" height=\"24\"><input type=submit value=\"Search by Option\"></td>
    </form></tr>
    <tr><form action=search_mls.php method=post>
      <td width=\"157\" height=\"13\">MLS Number</td>
      <td width=\"192\" height=\"13\"><input type=text name=mls size=20></td>
      <td width=\"152\" height=\"13\"><input type=submit value=\"Search by MLS\"></td>
    </form></tr>
    <tr><form action=search_city.php method=post>
      <td width=\"157\" height=\"13\">City</td>
      <td width=\"192\" height=\"13\"><input type=text name=city size=20></td>
      <td width=\"152\" height=\"13\"><input type=submit value=\"Search by City\"></td>
    </form></tr>
    <tr><form action=search_state.php method=post>
      <td width=\"157\" height=\"13\">State or Providence</td>
      <td width=\"192\" height=\"13\"><input type=text name=state size=20></td>
      <td width=\"152\" height=\"13\"><input type=submit value=\"Search by State\"></td>
    </form></tr>
  </table>
  </center>
</div>\n";




include 'footer.inc';
?>
