<?php
/********************************************************/
//   Anti-Flood Flash Mail Form v1.0					//
//	 by: Fayal GUENNAR									//
//	 creation: 09/08/07									//
//   Licence: GNU GPL 									//
//														//
//   http://www.myfayce.com 							//
//   webmaster@myfayce.com								//
/******************************************************************************/
/*

Licensed under the GNU General Public License (GPL)

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

******************************************************************************/

// script configuration
$admin_mail="webmaster@myfayce.com"; //mail admin
$today = idate("U");
$timelimit = 120;

//for the contact.swf file
$webmaster_name="&webmaster_name= Mr. GUENNAR Fayal&";
$webmaster_phone="&webmaster_phone= 00 31 777 777 777&";
$webmaster_mail="&webmaster_mail=webmaster@myfayce.com&";
$webmaster_location="&webmaster_location=Amsterdam, NL&";

//Messages to flash
$err1 = "&returnMe=no flood please! &";
$err2 = "&returnMe=invalid email adress&";

$msg1 = "&returnMe=email sent.Thank you!&";
$msg2 = "&returnMe=error: retry later&";

//Now we fill the flash


echo $webmaster_name."<br>";
echo $webmaster_phone."<br>";
echo $webmaster_mail."<br>";
echo $webmaster_location."<br>";

//antiflood system/////////////////////////////////////////////////////////////////////////////
function AFwriteXML($ip,$date){

	$xdoc = new DomDocument;
	$xdoc->Load('antiflood.xml');


	$element_mailers = $xdoc->getElementsByTagName("mailers")->item(0);

	$element_mailer = $xdoc->createElement("mailer");
	$element_mailer = $element_mailers->appendChild($element_mailer);


	$element_ip = $xdoc->createElement("ip");
	$element_ip = $element_mailer->appendChild($element_ip);
	$texte_ip = $xdoc->createTextNode($ip);
	$texte_ip = $element_ip->appendChild($texte_ip);

	$element_time = $xdoc->createElement("time");
	$element_time = $element_mailer->appendChild($element_time);
	$texte_time = $xdoc->createTextNode($date);
	$texte_time = $element_time->appendChild($texte_time);




	$test = $xdoc->save("antiflood.xml");

}

function AFcheckXML($adress){
	global $today;
	global $timelimit;
	//search for the ip adress in the XML
	//if ip found and date less than timelimit return 0
	//else return 1

	$doc = new DOMDocument();
	$doc->load( 'antiflood.xml' );

	$mailers = $doc->getElementsByTagName( "mailer" );
	foreach( $mailers as $mailer ){

		$ips = $mailer->getElementsByTagName( "ip" );
		$ip = $ips->item(0)->nodeValue;

		$times = $mailer->getElementsByTagName( "time" );
		$time = $times->item(0)->nodeValue;

		settype($time, "integer");
		$diff= $today - $time;

		if(($ip==$adress) and ($diff<$timelimit)){
			return 0;

		}
	}

	return 1;

}
////End of function definitions

if (isset($_POST["mailit"])) {
	$_POST["mailit"]=trim(stripslashes($_POST["mailit"]));
}

if($_POST["mailit"]){

	if(!AFcheckXML($_SERVER['REMOTE_ADDR'])){

		echo $err1;
	}
	else{



		//end of Antiflood system///////////////////////////////////////////////////////////////////////
		//we fetch variables from contact.swf

		if (isset($_POST["nom"])) {
			$_POST["nom"]=trim(stripslashes($_POST["nom"]));
		}
		if (isset($_POST["email"])) {
			$_POST["email"]=trim(stripslashes($_POST["email"]));
		}
		if (isset($_POST["msg"])) {
			$_POST["msg"]=trim(stripslashes($_POST["msg"]));
		}

		// init controle vars

		$email_ok= 0;

		// checking mail validity

		if (!ereg("[[:alnum:]]+@[[:alnum:]]+\.[[:alnum:]]+",  $_POST["email"])) {

			echo $err2;
		}
		else{



			// We send the mail


			$lemail=
			"_______________________________________________________________________"."\n\n".
			"Name: ".$_POST["nom"]."\n".
			"eMail: ".$_POST["email"]."\n".
			"Message:\n".$_POST["msg"]."\n\n".
			"_______________________________________________________________________"."\n\n".
			"Mail sent from:"."\n".
			"IP: ". $_SERVER['REMOTE_ADDR']."\n".
			"Browser: ". $_SERVER['HTTP_USER_AGENT']."\n\n";

			//securisation fonctions
			function saut_ligne1($_SL1)
			{
				$patternssl1[0] = '/\n/';
				$replacementstsl1[0] = "<linejump>";
				return preg_replace($patternssl1,$replacementstsl1,$_SL1);
			}
			function saut_ligne2($_SL2)
			{
				$patternssl2[0] = '/<linejump>/';
				$replacementstsl2[0] = "\n";
				return preg_replace($patternssl2,$replacementstsl2,$_SL2);
			}
			function securise($_stringt)
			{
				$patternst[0] = '/BCC:/';
				$patternst[1] = '/CC:/';
				$patternst[2] = '/bcc:/';
				$patternst[3] = '/cc:/';
				$patternst[4] = '/bcc/';
				$patternst[5] = '/cc/';
				$replacementst[0] = 'erreur';
				$replacementst[1] = 'erreur';
				$replacementst[2] = 'erreur';
				$replacementst[3] = 'erreur';
				$replacementst[4] = 'erreur';
				$replacementst[5] = 'erreur';
				return preg_replace($patternst,$replacementst,$_stringt);
			}


			$entete = "From: ".$_POST["nom"]." <".$_POST["email"].">\n";
			$entete .= "MIME-Version: 1.0";
			$message=saut_ligne1($lemail);
			$message_envoye=saut_ligne2($message);
			if (@mail($admin_mail,"msg de ".$_POST["nom"]." << myfayce.com",securise($message_envoye),$entete)){
				// mail envoyé
				echo $msg1;
				$email_ok = 1;
				AFwriteXML($_SERVER['REMOTE_ADDR'],$today);

			}
			else{
				echo $msg2;
			}


		}
	}
}
?>