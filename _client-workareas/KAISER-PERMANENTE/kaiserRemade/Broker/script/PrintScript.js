
function repeatprinthead(newWin,FromWhere)
{
	var name1 = FromWhere;
    
    newWin.document.writeln('<table align=center border=0 cellpadding=0 cellspacing=0 width="486" height="38">');
    newWin.document.writeln('<tbody>');
    newWin.document.writeln('<tr>');
    newWin.document.writeln('<td align=right noWrap>');
    newWin.document.writeln('<div align="center">');
    newWin.document.writeln('<h4><font class=f size=2><b><font size="5">'+  name1 +'</font></b></font>');
    newWin.document.writeln('</h4>');
    newWin.document.writeln('</div>');
    newWin.document.writeln('</td>');
    newWin.document.writeln('</tbody>');
    newWin.document.writeln('</table>');

    newWin.document.writeln('<hr color=#336699 size=1>');
    newWin.document.writeln('<a name=top></a>'); 
return false;
}
 
function callPrint()
{
    var name = document.title;
    var rcount = 0;
    var newWin = open('printTest.html','myDoc','');
    //newWin.focus();
    
    
    newWin.document.writeln('<html>');
    newWin.document.writeln('<body>');
    
  	newWin.document.writeln('<table border="0" width="931" cellpadding="0" cellspacing="0"> ');
	newWin.document.writeln('  <tr> ');
	newWin.document.writeln(' <td bgcolor="#FFFFFF" width="955"> ');
	newWin.document.writeln('      <div align="center"> ');
	newWin.document.writeln('        <center> ');
	newWin.document.writeln('        <table border="0" cellspacing="1" width="100%" bgcolor="#FFFFFF" height="65"> ');
	newWin.document.writeln('          <tr> ');
//	newWin.document.writeln('            <td width="156" height="61"><b><img border="0" src="../images/mainlogo.gif" width="155" height="55"></b></td> ');
	newWin.document.writeln('            <td width="171" height="61"> ');
	newWin.document.writeln('              </td> ');
	newWin.document.writeln('            <td bgcolor="#FFFFFF" width="453" height="61"></td> ');
	newWin.document.writeln('          </tr> ');
	newWin.document.writeln('        </table> ');
	newWin.document.writeln('        </center> ');
	newWin.document.writeln('      </div> ');
	newWin.document.writeln('    </td> ');
	newWin.document.writeln('  </tr> ');
	newWin.document.writeln('</table> ');  
    
    
    newWin.document.writeln('<table align=center border=0 cellpadding=0 cellspacing=0 width="486" height="38">');
    newWin.document.writeln('<tbody>');
    newWin.document.writeln('<tr>');
    newWin.document.writeln('<td align=right noWrap>');
    newWin.document.writeln('<div align="center">');
    newWin.document.writeln('<h4><font class=f size=2><b><font size="5">'+  name +'</font></b></font>');
    newWin.document.writeln('</h4>');
    newWin.document.writeln('</div>');
    newWin.document.writeln('</td>');
    //newWin.document.writeln('</tr>');
    
    newWin.document.writeln('</tbody>');
    newWin.document.writeln('</table>');

	      
    newWin.document.writeln('<hr color=#336699 size=1>');
    newWin.document.writeln('<a name=top></a>');
   var parentFrames = parent.frames.length;
   
if( parentFrames > 0 )
{

	for( var y=0; y < parent.frames.length; y++)
	{    
		if(y != 0 )
			{
				repeatprinthead(newWin,parent.frames[y].document.title);
				//alert("After printing frame title");
			}
		var frameName = parent.frames[y].name;
		for(var z=0; z<parent.frames[y].document.forms.length; z++)
		{     
			
 			for( var i = 0; i < parent.frames[y].document.forms[z].length ; i++ )
 			{
        		var name = parent.frames[y].document.forms[z].elements[i].name;
        		var value = parent.frames[y].document.forms[z].elements[i].value;
    
  				if (parent.frames[y].document.forms[z].elements[i].type == 'select-one')
   				{
     				
    				 if (parent.frames[y].document.forms[z].elements[i].size > 0 )
      				{   
          
       					newWin.document.writeln('<table  cellpadding=1 cellspacing=0 width=931>');
       					newWin.document.writeln('<tbody>');
     					newWin.document.writeln('<tr>');
       			        newWin.document.writeln('<td align=left width="900"><font ><b>'+name+'&nbsp;:&nbsp;</font> </td>');
				        newWin.document.writeln('</tr>');
				        rcount = rcount + 1;
				        var kk = "ks";
				        var ll = "lo";
				        for ( var k = 0; k < parent.frames[y].document.forms[z].elements[i].length ; k ++ )
				        {
				            var value = parent.frames[y].document.forms[z].elements[i].options[k].text;
				        
				               newWin.document.writeln('<td align=left width="900"><font size=2>'+value+'</font> </td>');
				               newWin.document.writeln('</tr>');
				        }
				       newWin.document.writeln('</tr>');
				       newWin.document.writeln('</table>');

     				}
   					else
    				{
         				 if (value != '') 
            			{
            			      value = parent.frames[y].document.forms[z].elements[i].options[0].text;
				              newWin.document.writeln('<table  cellpadding=1 cellspacing=0 width=931>');
					  	      newWin.document.writeln('<tbody>');
				      
				              newWin.document.writeln('<td align=left width="300"><font ><b>'+name +'</font> </td>');
				              newWin.document.writeln('<td align=left width="10"> <font ><b>&nbsp;:&nbsp;</font> </td>');
				              newWin.document.writeln('<td align=left width="450"> <font size=2>'+value+'</font> </td>');
				              newWin.document.writeln('</tr>');
				              newWin.document.writeln('</tbody>');
				              newWin.document.writeln('</table>');          
              		    } 
     			     }         
   			}
  			else if ( parent.frames[y].document.forms[z].elements[i].type == 'hidden' || parent.frames[y].document.forms[z].elements[i].type== 'button' || parent.frames[y].document.forms[z].elements[i].type== 'submit' || parent.frames[y].document.forms[z].elements[i].type=='checkbox' || parent.frames[y].document.forms[z].elements[i].type=='radio'  )
          	{
                //parent.frames[y].document.forms[z].elements[i].name = 'hidden';
            }
            else if (value != '') 
            {
               //alert(value);
               
               newWin.document.writeln('<table  cellpadding=1 cellspacing=0 width=931>');
	  	       newWin.document.writeln('<tbody>');
         
               newWin.document.writeln('<td align=left width="300"><font ><b>'+name +'</font> </td>');
               newWin.document.writeln('<td align=left width="10"> <font ><b>&nbsp;:&nbsp;</font> </td>');
               newWin.document.writeln('<td align=left width="450"> <font size=2>'+value+'</font> </td>');
               newWin.document.writeln('</tr>');
               newWin.document.writeln('</tbody>');
               newWin.document.writeln('</table>');          
            
             }
         
          }
          
    }
  }
  
}
else
{
for(var z=0; z<document.forms.length; z++)
{     
 for( var i = 0; i < parent.document.forms[z].length ; i++ )
 {
        var name = document.forms[z].elements[i].name;
        var value = document.forms[z].elements[i].value;
      
  if (document.forms[z].elements[i].type == 'select-one')
   {
     value = document.forms[z].elements[i].text;
     if (document.forms[z].elements[i].size > 0 )
      {   
          
       newWin.document.writeln('<table  cellpadding=1 cellspacing=0 width=931>');
       newWin.document.writeln('<tbody>');
    
        newWin.document.writeln('<tr>');
       
         //  newWin.document.writeln('<td align=right noWrap valign=top width="300"><font ><b>'+name+'&nbsp;:&nbsp;</b></font> </td>');\
        newWin.document.writeln('<td align=left width="900"><font ><b>'+name+'&nbsp;:&nbsp;</font> </td>');
        newWin.document.writeln('</tr>');
 
        var kk = "ks";
        var ll = "lo";
        //var flg = 0;
        for ( var k = 0; k < document.forms[z].elements[i].length ; k ++ )
        {
            var value = document.forms[z].elements[i].options[k].text;
        
               newWin.document.writeln('<td align=left width="900"><font size=2>'+value+'</font> </td>');
               //newWin.document.writeln('<td width="448"><font size=2>'+value+'</font> </td>');
               newWin.document.writeln('</tr>');
              
        }
       newWin.document.writeln('</tr>');
       newWin.document.writeln('</table>');

     }
   else
    {
          if (value != '') 
            {
              newWin.document.writeln('<table  cellpadding=1 cellspacing=0 width=931>');
	  	      newWin.document.writeln('<tbody>');
      
              newWin.document.writeln('<td align=left width="300"><font ><b>'+name +'</font> </td>');
              newWin.document.writeln('<td align=left width="10"> <font ><b>&nbsp;:&nbsp;</font> </td>');
              newWin.document.writeln('<td align=left width="450"> <font size=2>'+value+'</font> </td>');
              newWin.document.writeln('</tr>');
              newWin.document.writeln('</tbody>');
              newWin.document.writeln('</table>');          
    
             } 
     }         
   }
  else
         if ( document.forms[z].elements[i].type == 'hidden' || document.forms[z].elements[i].type== 'button' || document.forms[z].elements[i].type== 'submit' || document.forms[z].elements[i].type=='checkbox' || document.forms[z].elements[i].type=='radio'  )
           {
                //document.forms[z].elements[i].name = 'hidden';
            }
            else
             if (value != '') 
              {
               //alert(value);
               
               newWin.document.writeln('<table  cellpadding=1 cellspacing=0 width=931>');
	  	       newWin.document.writeln('<tbody>');
         
               newWin.document.writeln('<td align=left width="300"><font ><b>'+name +'</font> </td>');
               newWin.document.writeln('<td align=left width="10"> <font ><b>&nbsp;:&nbsp;</font> </td>');
               newWin.document.writeln('<td align=left width="450"> <font size=2>'+value+'</font> </td>');
               newWin.document.writeln('</tr>');
               newWin.document.writeln('</tbody>');
               newWin.document.writeln('</table>');          
            }
         
    }
}
}

newWin.document.writeln('<hr color=#336699 size=1>');
newWin.document.writeln('<table align=center cellpadding=0 cellspacing=0 width="100%">');
  newWin.document.writeln('<tbody>');
  newWin.document.writeln('<tr>');
    newWin.document.writeln('<td noWrap width="100%">');
      newWin.document.writeln('<div align="center"><font class="s">&copy; 2002 KP . All rights reserved.</font> </div>');
    newWin.document.writeln('</td>');
  newWin.document.writeln('</tr>');
  newWin.document.writeln('</tbody>');
newWin.document.writeln('</table>');

newWin.document.writeln('</body>');
newWin.document.writeln('</html>');

return false;
}
