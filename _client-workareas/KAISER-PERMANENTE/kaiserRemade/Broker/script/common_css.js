var da = (document.all) ? 1 : 0;
var ns4 = ((navigator.userAgent.indexOf("Mozilla") != -1) && (navigator.userAgent.indexOf("4.") != -1)  && (navigator.userAgent.indexOf("MSIE") == -1));
var ns6 = ((navigator.userAgent.indexOf("Netscape") != -1) && (navigator.userAgent.indexOf("6.") != -1));

	if (ns6) with (document) { 
		writeln('<' + 'style type="text/css">');
		writeln('.maintitle { color:#0B5F77; font-family:verdana,arial,helvetica; font-size:11.5px; font-weight:bold }'); 
		writeln('.radiotext { color:#ffffff; font-family:verdana,arial,helvetica; font-size:9px; text-decoration:none }'); 
		writeln('.radiotext2 { color:#0B5F77; font-family:verdana,arial,helvetica; font-size:9px; text-decoration:none; font-weight:bold; }'); 
		writeln('.stitle { color:#0B5F77; font-family:verdana,arial,helvetica; font-size:10px; font-weight:bold }'); 
		writeln('.stitle2 { color:#FFFFFF; font-family:verdana,arial,helvetica; font-size:10px; font-weight:bold }'); 
		writeln('.stitle3 { color:#0B5F77; font-family:verdana,arial,helvetica; font-size:9px; }'); 
		writeln('.ComTitle { color:#FFFFFF; font-family:verdana,arial,helvetica; font-size:10px; font-weight:bold } '); 
		writeln('.select1 { color:#000000; font-family:verdana,arial,helvetica; font-size:10px; height:16px; background-color:#B9B9B9; }'); 
		writeln('.input1 { color:#000000; font-family:verdana,arial,helvetica; font-size:10px; height:18px; background-color:#B9B9B9; }'); 
		writeln('.select2 { color:#000000; font-family:verdana,arial,helvetica; font-size:10px; height:16px; background-color:#FFFFFF; }'); 
		writeln('.input2 { color:#000000; font-family:verdana,arial,helvetica; font-size:10px; height:18px; background-color:#FFFFFF; }'); 
		writeln('.multiselect { color:#000000; background-color:#B9B9B9; width:365px; font-family : verdana,arial,helvetica; font-size : 10px; }'); 
		writeln('.multiselect2 { color:#000000; background-color:#ffffff; width:650px; font-family : verdana,arial,helvetica; font-size : 10px; }'); 
		writeln('.multiselect3 { color:#000000; background-color:#B9B9B9; width:650px; font-family : verdana,arial,helvetica; font-size : 10px; }'); 
		writeln('.menulinks { text-decoration:none; color:#333366; font-family:verdana,arial,helvetica; font-size:10px; font-weight:bold }'); 
		writeln('.lebotton { background-color:#E6E9F0; color:#003B65; font-family:Verdana, Arial, Helvetica; font-size:10px;font-weight:bold }'); 
		writeln('.lebotton2 { background-color:#0B5F77; color:#E6E9F0; font-family:Verdana, Arial, Helvetica; font-size:12px;font-weight:bold }'); 
		writeln('.lebotton3 { background-color:#E6E9F0; color:#003B65; font-family:Verdana, Arial, Helvetica; font-size:14px;font-weight:bold; height:30px; width:75px; }'); 
		writeln('</style>');
	}



	else with (document) {
		writeln('<' + 'style type="text/css">');
		writeln('body { scrollbar-face-color:#E6E9F0; scrollbar-highlight-color:#E6E9F0; scrollbar-shadow-color:#0B5F77; scrollbar-3dlight-color: 0B5F77; scrollbar-arrow-color:0B5F77; scrollbar-track-color:#E6E9F0; scrollbar-darkshadow-color:#0B5F77; }'); 
		writeln('.maintitle { color:#0B5F77; font-family:verdana,arial,helvetica; font-size:11.5px; font-weight:bold }'); 
		writeln('.radiotext { color:#ffffff; font-family:verdana,arial,helvetica; font-size:9px; text-decoration:none }');
		writeln('.radiotext2 { color:#0B5F77; font-family:verdana,arial,helvetica; font-size:9px; text-decoration:none; font-weight:bold;  }');
		writeln('.stitle { color:#0B5F77; font-family:verdana,arial,helvetica; font-size:10.5px; font-weight:bold }'); 
		writeln('.stitle2 { color:#FFFFFF; font-family:verdana,arial,helvetica; font-size:10.5px; font-weight:bold }'); 
		writeln('.stitle3 { color:#0B5F77; font-family:verdana,arial,helvetica; font-size:9px; }'); 
		writeln('.ComTitle { color:#FFFFFF; font-family:verdana,arial,helvetica; font-size:10.5px; font-weight:bold }'); 
		writeln('.select1 { color:#000000; font-family:verdana,arial,helvetica; font-size:10.5px; height:20px; background-color:#B9B9B9; }'); 
		writeln('.input1 { color:#000000; font-family:verdana,arial,helvetica; font-size:10.5px; height:18px; background-color:#B9B9B9; }'); 
		writeln('.select2 { color:#000000; font-family:verdana,arial,helvetica; font-size:10.5px; height:20px; background-color:#FFFFFF; }'); 
		writeln('.input2 { color:#000000; font-family:verdana,arial,helvetica; font-size:10.5px; height:18px; background-color:#FFFFFF; }'); 
		writeln('.button1 { color:#0B5F77; font-family:verdana,arial,helvetica; font-size:10.5px; height:18px; font-weight:bold; background-color:#E6E9F0; }'); 
		writeln('.multiselect { color:#000000; background-color:#B9B9B9; width:365px; font-family : verdana,arial,helvetica; font-size : 10px; }'); 
		writeln('.multiselect2 { color:#000000; background-color:#ffffff; width:650px; font-family : verdana,arial,helvetica; font-size : 10px; }'); 
		writeln('.multiselect3 { color:#000000; background-color:#B9B9B9; width:650px; font-family : verdana,arial,helvetica; font-size : 10px; }'); 
		writeln('.menulinks { text-decoration:none; color:#333366; font-family:verdana,arial,helvetica; font-size:10.5px; font-weight:bold }'); 
		writeln('.lebotton { background-color:#E6E9F0; color:#003B65; font-family:Verdana, Arial, Helvetica; font-size:10.5px;font-weight:bold }'); 
		writeln('.lebotton2 { background-color:#0B5F77; color:#E6E9F0; font-family:Verdana, Arial, Helvetica; font-size:12px;font-weight:bold }'); 
		writeln('.lebotton3 { background-color:#E6E9F0; color:#003B65; font-family:Verdana, Arial, Helvetica; font-size:14px;font-weight:bold; height:30px; width:75px; }'); 
		writeln('</style>');
	}