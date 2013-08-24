//Installation directions produced by http://www.dynamicdrive.com

Three steps to installing DHTML Magnifier on your page

STEP 1: Upload to your webpage directory ALL files in the zip except "example.htm" and "readme.txt".


STEP 2: Insert below code into the <HEAD> section of your page:

<script type="text/javascript">

/***********************************************
* DHTML Magnifier (Christian Patzer, cpatzer@REMOVETHISdjc.com)
* Script featured on Dynamicdrive.com DHTML code library
* Visit Dynamic Drive at http://www.dynamicdrive.com/ for full source code
***********************************************/

//if IE5.5+ (detected via window.createPopup)
if (window.createPopup)
document.write('<script src="zoom.js"><\/script>')

</script>


STEP 3: Insert the below code at the very END of your document, right above </BODY>:

<script laguage=javascript>
if (window.createPopup)
document.write("</tr></td></table>");
</script>


STEP 4: Finally, inside "zoom.js" above, make sure variable "iframeSrc" correctly points to the path of "zoom.html" You can open zoom.js using any text editor, some of which you can find here: http://download.com.com/3120-20-0.html?qt=text+editor&tg=dl-20

Enjoy the awesome script!

Tip: This script works best in a page with its content contained inside a table with an explicit width defined (ie: <table width=600>).


