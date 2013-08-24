#!/usr/local/bin/perl -w

#######################################################################################################
# Company: NetMedia Solutions                                                                         #
# Date: Saturday, September 21, 2001                                                                  #
# Location: Los Angeles, California, United States of America                                         #
# Made By: Luis Rodriguez (drlouie)                                                                   #
# Email: drlouie@tstonramp.com                                                                        #
#                                                                                                     #
# USNightVision.com's dynamic date generator. Dynamically driven by DHTML, HTML, Perl and MySql      #
#                                                                                                     #
#######################################################################################################

require("parse_query.cgi");

# print "Content-type: text/html \n\n";

#select(STDOUT); $| = 1;
#print "Content-Type: application/pdf\n\n";
#$commandline = "apachectl restart";
#system($commandline);

	## loan app secure new window
	$losPages[0] = ("https://www.mortgage101.com/loan-app/startloan.asp?acctid=306998&refer=");
	## prequal app
	$losPages[1] = ("http://rws.mortgage101.com/templateroot/LeadForms/ZipCodeSearch.asp?p=americorplen&AcctID=306998");
	$losFProc[1] = ("http://rws.mortgage101.com/templateroot/LeadForms/");
	$laPagina[1] = ("Prequalification_Application.shtml");
	## current rates
	$losPages[2] = ("http://rws.mortgage101.com/templateroot/Rates/RatesheetDotNet.asp?PVLID=4868");
	$losFProc[2] = ("http://rws.mortgage101.com/templateroot/Rates/");
	$laPagina[2] = ("Current_Rates.shtml");
	$otraPagina1[2] = ("http://rws.mortgage101.com/data/connection/cnnRateRouter.asp?PVLID=4868");

	## imperfect **** BAD
	$losPages[3] = ("http://rws.mortgage101.com/content/template0/bcratesearch.asp?flag=SUBPRIME&p=&acctid=306998");
	$losFProc[3] = ("http://rws.mortgage101.com/content/template0/");
	$laPagina[3] = ("Imperfect_Credit.shtml");
	###> ARTICLES = no form
	## market snapshot
	$losPages[4] = ("http://rws.mortgage101.com/templateroot/Articles/MarketSnapshot.asp?PVLID=4868");
	$laPagina[4] = ("Market_Snapshot.shtml");
	## market commentary
	$losPages[5] = ("http://rws.mortgage101.com/templateroot/Articles/marketCommentary.asp?ArticleID=1197&PVLID=&AcctID=306998&P=americorplen");
	$laPagina[5] = ("Market_Commentary.shtml");
	## fixed mortg
	$losPages[6] = ("http://rws.mortgage101.com/templateroot/Articles/LoanPrograms.asp?ArticleID=1027&PVLID=&AcctID=306998&P=americorplen");
	$laPagina[6] = ("Fixed_Rate_Mortgage.shtml");
	## adjustible mortg
	$losPages[7] = ("http://rws.mortgage101.com/templateroot/Articles/Application.asp?PVLID=&AcctID=306998&P=americorplen");
	$laPagina[7] = ("Adjustible_Rate_Mortgage.shtml");
	## home line credit
	$losPages[8] = ("http://rws.mortgage101.com/templateroot/Articles/SecondMortgages.asp?ArticleID=1049&PVLID=&AcctID=306998&P=");
	$laPagina[8] = ("Home_Equity_Creditline.shtml");
	## interest Rates
	$losPages[9] = ("http://rws.mortgage101.com/templateroot/Articles/SecondMortgages.asp?ArticleID=1053&PVLID=&AcctID=306998&P=");
	$laPagina[9] = ("Interest_Rates.shtml");
	## Loan Costs
	$losPages[10] = ("http://rws.mortgage101.com/templateroot/Articles/SecondMortgages.asp?ArticleID=1052&PVLID=&AcctID=306998&P=");
	$laPagina[10] = ("Loan_Costs.shtml");
	## Payment Calculators
	$losPages[11] = ("http://rws.mortgage101.com/templateroot/Articles/SecondMortgages.asp?ArticleID=1051&PVLID=&AcctID=306998&P=");	
	$laPagina[11] = ("Payment_Calculations.shtml");
	## 2nd Mortgage Terms
	$losPages[12] = ("http://rws.mortgage101.com/templateroot/Articles/SecondMortgages.asp?ArticleID=1052&PVLID=&AcctID=306998&P=");
	$laPagina[12] = ("2nd_Mortgage_Terms.shtml");
	## Analyze Savings
	$losPages[13] = ("http://rws.mortgage101.com/templateroot/Articles/LoanPrograms.asp?ArticleID=1040&PVLID=&AcctID=306998&P=");
	$laPagina[13] = ("Analyze_Your_Savings.shtml");
	## Consider Other Mortgage Programs
	$losPages[14] = ("http://rws.mortgage101.com/templateroot/Articles/LoanPrograms.asp?ArticleID=1043&PVLID=&AcctID=306998&P=");
	$laPagina[14] = ("Consider_Other_Mortgage_Programs.shtml");
	## Deciding to Refinance
	$losPages[15] = ("http://rws.mortgage101.com/templateroot/Articles/LoanPrograms.asp?ArticleID=1044&PVLID=&AcctID=306998&P=");
	$laPagina[15] = ("Deciding_to_Refinance.shtml");
	## Get Some Cash
	$losPages[16] = ("http://rws.mortgage101.com/templateroot/Articles/LoanPrograms.asp?ArticleID=1118&PVLID=&AcctID=306998&P=");
	$laPagina[16] = ("Get_Some_Cash.shtml");
	## Paying Points for a Lower Rate
	$losPages[17] = ("http://rws.mortgage101.com/templateroot/Articles/LoanPrograms.asp?ArticleID=1041&PVLID=&AcctID=306998&P=");
	$laPagina[17] = ("Paying_Points_Lower_Rate.shtml");
	## Refinance Considerations
	$losPages[18] = ("http://rws.mortgage101.com/templateroot/Articles/Refinance.asp?ArticleID=1121&PVLID=&AcctID=306998&P=");
	$laPagina[18] = ("Refinance_Considerations.shtml");
	## Refinance Costs
	$losPages[19] = ("http://rws.mortgage101.com/templateroot/Articles/LoanPrograms.asp?ArticleID=1039&PVLID=&AcctID=306998&P=");
	$laPagina[19] = ("Refinance_Costs.shtml");
	## Refinance Once, Twice
	$losPages[20] = ("http://rws.mortgage101.com/templateroot/Articles/LoanPrograms.asp?ArticleID=1119&PVLID=&AcctID=306998&P=");
	$laPagina[20] = ("Refinance_Once_Twice.shtml");
	## Trade your ARM For A Fixed Rate
	$losPages[21] = ("http://rws.mortgage101.com/templateroot/Articles/LoanPrograms.asp?ArticleID=1117&PVLID=&AcctID=306998&P=");
	$laPagina[21] = ("Trade_ARM_Fixed_Rate.shtml");
	## Your Personal Taxes
	$losPages[22] = ("http://rws.mortgage101.com/templateroot/Articles/LoanPrograms.asp?ArticleID=1042&PVLID=&AcctID=306998&P=");
	$laPagina[22] = ("Your_Personal_Taxes.shtml");
	## How Much Can I Afford?
	$losPages[23] = ("http://rws.mortgage101.com/templateroot/Calculators/Afford.asp?PVLID=&AcctID=306998&P=americorplen");
	$losFProc[23] = ("http://rws.mortgage101.com/templateroot/Calculators/");
	$laPagina[23] = ("How_Much_Afford.shtml");
	## Payment Calculator
	$losPages[24] = ("http://rws.mortgage101.com/templateroot/Calculators/Payment.asp?PVLID=&AcctID=306998&P=americorplen");
	$losFProc[24] = ("http://rws.mortgage101.com/templateroot/Calculators/");
	$laPagina[24] = ("Payment_Calculator.shtml");
	## Should I Refinance?
	$losPages[25] = ("http://rws.mortgage101.com/templateroot/Calculators/Refinance.asp?PVLID=&AcctID=306998&P=americorplen");
	$losFProc[25] = ("http://rws.mortgage101.com/templateroot/Calculators/");	
	$laPagina[25] = ("Should_I_Refinance.shtml");	
	##Mortgage Dictionary
	$losPages[26] = ("http://rws.mortgage101.com/templateroot/Articles/Application.asp?PVLID=4868&ArticleID=1038");
	$laPagina[26] = ("Mortgage_Dictionary.shtml");

	##Mortgage Rates
#	$losPages[27] = ("http://www.mortgage101.com/Articles/DailyRateSurvey.asp?state=california");
#	$laPagina[27] = ("Mortgage_Rates.shtml");
	


	
	
	$miPagina = $FORM{'pagina'};
	$url = $losPages[$miPagina];



use LWP::Simple;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
my $page = get ($url);

#$my2 = "http://www.americorlending.com/cgi-bin/getPage.cgi?pagina=2";
#if ($page =~ "$losPages[2]") { $page =~ s/$losPages[2]//gi; }


## remove header
@splitPage = split(/\n/,$page);

## create todaysRates.html file
# if ($miPagina eq "2") { require("getMainRates.cgi"); }

$csp = 0;
foreach $sp (@splitPage) {

	$url = "http://rws.mortgage101.com/templateroot/";
	$urlb = "/templateroot/";
	$sp =~ s/$urlb/$url/gi;

	$url2 = 'href="http://rws.mortgage101.com/';
	$url2b = 'href="/';
	$sp =~ s/$url2b/$url2/gi;	
	
	$widthb = ' width="760"';
	$sp =~ s/$widthb//gi;

	$tableAlign = '<table align="center" ';
	$tableAlignb = '<table ';
	$sp =~ s/$tableAlignb/$tableAlign/gi;

	$double ="http://rws.mortgage101.com";
	$sp =~ s/$double$double/$double/gi;

	$dbspc = "<BR><BR><BR><BR>";
	$sp =~ s/$dbspc//gi;
	
	$scriptI = "this.src='http://rws.mortgage101.com/images";
	$scriptIb = "this.src='/images";
	$sp =~ s/$scriptIb/$scriptI/gi;
	
	$iURL = '"http://rws.mortgage101.com/images/';
	$iURLb = '"/images/';
	$sp =~ s/$iURLb/$iURL/gi;

	
	if ($miPagina == 1) { 


		$formatT1 = '<table align="center" width="100%" border="0" cellspacing="0" cellpadding="0">';
		$formatT1r = '<table class="calcinputtable1" align="center" width="100%" border="0" cellspacing="0" cellpadding="0">';
		$sp =~ s/$formatT1/$formatT1r/gi;

		$formatT2 = '<table align="center" width="100%" border="0" cellspacing="0" cellpadding="2">';
		$formatT2r = '<table class="calcinputTitleBar" align="center" width="100%" border="0" cellspacing="0" cellpadding="2">';
		$sp =~ s/$formatT2/$formatT2r/gi;
	}

	if ($miPagina == 2) { 
		$formatT1 = '<table align="center" cellSpacing="0" cellPadding="3" width="600" align="center" border="0">';
		$formatT1r = '<table class="calcinputtable4" align="center" cellSpacing="0" cellPadding="3" width="600" align="center" border="0">';
		$formatT2 = ' cellspacing="0" cellpadding="3" border="0" bgcolor="#CCCCCC" width="600" style="font-weight:bold;">';
		$formatT2r = ' cellspacing="0" cellpadding="1" border="0" class="calcinputtable5" width="600" style="font-weight:bold;">';
		$formatT3 = 'style="FONT-WEIGHT: bold; FONT-SIZE: 18px"';
		$formatT3r = 'style="FONT-WEIGHT: bold; FONT-SIZE: 12px"';		 
		$sp =~ s/$formatT1/$formatT1r/gi;
		$sp =~ s/$formatT2/$formatT2r/gi;
		$sp =~ s/$formatT3/$formatT3r/gi;
		
	}
	
	elsif ($miPagina == 23) { 
		$sp =~ s/calcinputtable/calcinputtable2/gi; 
		
		$cit = 'width="100%" class="calcinputtable"';
		$citb = 'width="100%" class="calcinputtable2"';
		$sp =~ s/$citb/$cit/gi;
	}

	elsif ($miPagina == 24) { 
		$sp =~ s/calcinputtable/calcinputtable3/gi;
	}	
	
	elsif ($miPagina == 24) { 
		$sp =~ s/calcinputtable/calcinputtable3/gi;
	}

	
	
	## does not work for articles, no forms
	if ($miPagina != 4 && $miPagina != 5 && $miPagina != 6 && $miPagina != 7 && $miPagina != 8 && $miPagina != 9 && $miPagina != 10 && $miPagina != 11 && $miPagina != 12 && $miPagina != 13 && $miPagina != 14 && $miPagina != 15 && $miPagina != 16 && $miPagina != 17 && $miPagina != 18 && $miPagina != 19 && $miPagina != 20 && $miPagina != 21 && $miPagina != 22 && $miPagina != 26) { 
		$iFORM = 'onSubmit="popWindow(\'\',\'m101\',\'777\',\'550\',\'no\');" target="m101" action="' . $losFProc[$miPagina] . '';
		$iFORMb = 'action="';
		$sp =~ s/$iFORMb/$iFORM/gi;

	}

	$iSCRIPT = "<img src=\"../Americor_Lending_Images/spacer.gif\" border=\"0\">";
	$iSCRIPTb = 'Find Zip Code';
	$sp =~ s/$iSCRIPTb/$iSCRIPT/gi;


	
	### los internal urls
	$elURLp1 = 'document.location';
	$elURLp2 = 'hspace="6" align="absmiddle"';

	$elURLm1 = 'Apply Online';
	$elURLm2 = 'Interest Rates';
	$elURLm3 = 'Prequalify';
	$elURLm4 = 'Mortgage Dictionary';
	$elURLm5 = 'Market Snapshot';
	$elURLm6 = 'Market Commentary';
	$elURLm7 = 'Newsletter Signup';
	$elURLm8 = 'Contact Us';




	
	$startMenu = "<!--RWSBEGINHEADER-->";
	$endMenu = "<!--RWSENDHEADER-->";
	if ($sp =~ "$startMenu") { $beginCut = 1; }
	elsif ($sp =~ "$endMenu") { 
		$beginCut = 0;
		push(@myPage,"<LINK rel=\"stylesheet\" TYPE=\"text/css\" href=\"http://rws.mortgage101.com/templateroot/css/Template0.css\"><LINK rel=\"stylesheet\" TYPE=\"text/css\" href=\"http://rws.mortgage101.com/templateroot/css/Global.css\"><LINK rel=\"stylesheet\" TYPE=\"text/css\" href=\"http://rws.mortgage101.com/templateroot/css/DynamicStyles.aspx?PVLID=4868\">");
	}
	elsif ($beginCut eq "1") { $skipit = 1; }

	### los internal urls
	elsif ($sp =~ $elURLp1 && $sp =~ $elURLp2 && $sp =~ $elURLm1) { $skipit = 1; push(@myPage,"<td onclick=\"document.location='http://www.americorlending.com/Prequalification_Application.shtml'\"><nobr><img src=\"http://rws.mortgage101.com/templateroot/images/template0/icon_apply.gif\" alt=\"Apply Online\" width=\"21\" height=\"17\" hspace=\"6\" align=\"absmiddle\"><a href=\"http://www.americorlending.com/Prequalification_Application.shtml\">Apply Online</a></nobr></td>"); }
	elsif ($sp =~ $elURLp1 && $sp =~ $elURLp2 && $sp =~ $elURLm2) { $skipit = 1; push(@myPage,"<td onclick=\"document.location='http://www.americorlending.com/Current_Rates.shtml'\"><nobr><img src=\"http://rws.mortgage101.com/templateroot/images/template0/icon_rates.gif\" alt=\"Apply Online\" width=\"21\" height=\"17\" hspace=\"6\" align=\"absmiddle\"><a href=\"http://www.americorlending.com/Current_Rates.shtml\">Interest Rates</a></nobr></td>"); }
	elsif ($sp =~ $elURLp1 && $sp =~ $elURLp2 && $sp =~ $elURLm3) { $skipit = 1; push(@myPage,"<td onclick=\"document.location='http://www.americorlending.com/Prequalification_Application.shtml'\"><nobr><img src=\"http://rws.mortgage101.com/templateroot/images/template0/icon_prequal.gif\" alt=\"Prequalify\" width=\"21\" height=\"17\" hspace=\"6\" align=\"absmiddle\"><a href=\"http://www.americorlending.com/Prequalification_Application.shtml\">Prequalify</a></nobr></td>"); }
	elsif ($sp =~ $elURLp1 && $sp =~ $elURLp2 && $sp =~ $elURLm4) { $skipit = 1; push(@myPage,"<td onclick=\"document.location='http://www.americorlending.com/Mortgage_Dictionary.shtml'\"><nobr><img src=\"http://rws.mortgage101.com/templateroot/images/template0/icon_dictionary.gif\" alt=\"Mortgage Dictionary\" width=\"21\" height=\"17\" hspace=\"6\" align=\"absmiddle\"><a href=\"http://www.americorlending.com/Mortgage_Dictionary.shtml\">Mortgage Dictionary</a></nobr></td>"); }
	elsif ($sp =~ $elURLp1 && $sp =~ $elURLp2 && $sp =~ $elURLm5) { $skipit = 1; push(@myPage,"<td onclick=\"document.location='http://www.americorlending.com/Market_Snapshot.shtml'\"><nobr><img src=\"http://rws.mortgage101.com/templateroot/images/template0/icon_snapshot.gif\" alt=\"Market Snapshot\" width=\"21\" height=\"17\" hspace=\"6\" align=\"absmiddle\"><a href=\"http://www.americorlending.com/Market_Snapshot.shtml\">Market Snapshot</a></nobr></td>"); }
	elsif ($sp =~ $elURLp1 && $sp =~ $elURLp2 && $sp =~ $elURLm6) { $skipit = 1; push(@myPage,"<td onclick=\"document.location='http://www.americorlending.com/Market_Commentary.shtml'\"><nobr><img src=\"http://rws.mortgage101.com/templateroot/images/template0/icon_commentary.gif\" alt=\"Market Commentary\" width=\"21\" height=\"17\" hspace=\"6\" align=\"absmiddle\"><a href=\"http://www.americorlending.com/Market_Commentary.shtml\">Market Commentary</a></nobr></td>"); }	
	elsif ($sp =~ $elURLp1 && $sp =~ $elURLp2 && $sp =~ $elURLm7) { $skipit = 1; push(@myPage,""); }	
	elsif ($sp =~ $elURLp1 && $sp =~ $elURLp2 && $sp =~ $elURLm8) { $skipit = 1; push(@myPage,""); }	

	
	elsif ($sp =~ "_ctl0_HeadTag_MetaTags_TitleTag") { $skipit = 1; }
	elsif ($sp =~ "_ctl0_HeadTag_MetaTags_DescriptionTag") { $skipit = 1; }
	elsif ($sp =~ "_ctl0_HeadTag_MetaTags_KeywordsTag") { $skipit = 1; }
	elsif ($sp =~ "_ctl0_HeadTag_TemplateCSS") { $skipit = 1; }
	elsif ($sp =~ "_ctl0__ctl0_CompanyLogo") { $skipit = 1; push(@myPage,"<td height=\"1\"><img src=\"../Americor_Lending_Images/spacer.gif\"></td>"); }
	elsif ($sp =~ "<!DOCTYPE") { $skipit = 1; }
	elsif ($sp =~ "<HEAD>") { $skipit = 1; }
	elsif ($sp =~ "<\HEAD>") { $skipit = 1; }
	elsif ($sp =~ "<HTML>") { $skipit = 1; }
	elsif ($sp =~ "<body") { $skipit = 1; }
	elsif ($sp =~ "</body") { $skipit = 1; }
	elsif ($sp =~ "</HTML") { $skipit = 1; }

	
	else { 
		push(@myPage,"$sp");
	}
	
}


## script for document lower date
foreach $mpg (@myPage) { 
	
	print "$mpg";
}


#print "okay";
### <!--RWSBEGINHEADER-->
### <!--RWSENDHEADER-->

##return =true
1;