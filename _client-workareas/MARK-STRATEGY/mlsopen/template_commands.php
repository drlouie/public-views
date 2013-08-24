<b><u><a name="main">Main Template Commands:</a></u></b>
<br><br>
#mls# - This is the MLS Number<br>
#image1# - This is the main image<br>
#user_img_path# - This is the http://... path to your images<br>
#title# - This is the title of your listing<br>
#short_description# - This is the short description<br>
#price# - The listing price.<br>
#status# - This is the listing status.  The defult is a NULL value but can be Sold, For Rent, etc.<br>
#bedrooms# - This is the number of bedrooms in your listing.<br>
#baths# - This is the number of full bath rooms.<br>
#half_baths# - This is the number of half baths.<br>
#sqf# - This is the total square feet for your listing.<br>
#acres# - This is the total arces for your listing.<br>
#house_type# - IE: Ranch, Town Home, etc. This is the classification.<br>
#property_city# - The city where the propery is located.<br>
#property_state# - The state where the property is located.<br>
#property_zip# - The zip code of the property.<br>
#detailed_url# - This is the URL to the details page.<br>
<br><br>
So you might want to make custom HTML code using the above #codename# to create a custome template.
<br>
<b>Example:</b><br>
<textarea cols=65 rows=7>
<TABLE>
<TR><TD>MLS Number: #mls#</TD></TR>
<TR><TD>Title: #title#</TD></TR>
<TR><TD>Image: <IMG SRC="#user_img_path##image1#"></TD></TR>
<TR><TD><A HREF="#detailed_url#">More Details</A></TD></TR>
</TABLE></textarea>
<br><br>
<b><u><a name="detailed">Detailed Template Commands:</a></u></b>
<br><br>
#mls# - This is the MLS Number<br>
#image1..10# - This is the listing images. IE: #image1# #image2# #image3# .. #image10#<br>
#user_img_path# - This is the http://... path to your images<br>
#realtor_name# - The realtor or propery listing name.<br>
#realtor_phone# - The realtor or property listing phone number.<br>
#realtor_email# - The realtor or property listing email address.<br>
#title# - This is the title of your listing<br>
#short_description# - This is the short description<br>
#detailed_description# - This is the details on the listing.<br>
#price# - The listing price.<br>
#status# - This is the listing status.  The defult is a NULL value but can be Sold, For Rent, etc.<br>
#baths# - This is the number of full bath rooms.<br>
#half_baths# - This is the number of half baths.<br>
#sqf# - This is the total square feet for your listing.<br>
#acres# - This is the total arces for your listing.<br>
#house_type# - IE: Ranch, Town Home, etc. This is the classification.<br>
#property_address# - The address to the listing.<br>
#property_city# - The city where the propery is located.<br>
#property_state# - The state where the property is located.<br>
#property_zip# - The zip code of the property.<br>
#url# - More detailed external URL.<br>
#virtual_tour# - External virtual tour.<br>
#map# - Exteral map.<br>
#feature1..40# - This is the features 1 through 40. IE: #feature1# #feature2# .. #feature40#<br>
<br>
<b>Example:</b><br>
<textarea cols=65 rows=9>
<TABLE>
<TR><TD>MLS Number: #mls#</TD></TR>
<TR><TD>Title: #title#</TD></TR>
<TR><TD>Image: <IMG SRC="#user_img_path##image1#"></TD></TR>
<TR><TD>Feature: #feature1# #feature2# #feature3#</TD></TR>
<TR><TD>More Images: <IMG SRC="#user_img_path##image2#"></TD></TR>
</TABLE></textarea>


