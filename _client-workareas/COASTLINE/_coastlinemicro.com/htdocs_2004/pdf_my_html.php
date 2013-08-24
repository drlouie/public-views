<?
//
// "$Id: pdf-o-matic.php,v 1.23 2003/01/03 17:08:20 mike Exp $"
//
// Convert a web page to PDF, or show a form to get the URL...
//
// Copyright 2001-2003 by Easy Software Products.  This code may be
// freely used, and distributed under the terms of the HTMLDOC
// software license.
//

// HTML functions for HTMLDOC pages...
//
// This include file contains the following functions:
//
//   htmldoc_header($title = "")
//   htmldoc_footer()
//
// Both just put out a standard web page header (<HTML><BODY>)
// and trailer (</BODY></HTML>) - provide your own implementation
// if you use this script, e.g.:
//
 function htmldoc_header($title = "")
 {
   print("<HTML><HEAD><TITLE>$title - Fooware</TITLE></HEAD><BODY>\n");
 }

 function htmldoc_footer()
 {
   print("</BODY></HTML>\n");
 }

// Globals...
global $HTTP_GET_VARS;
global $HTTP_HOST;
global $HTTP_REFERER;
global $PHP_SELF;


//
// 'show_form()' - Show a form for converting a URL to PDF.
//

function show_form() {
    global $PHP_SELF;

    print("<TABLE WIDTH=\"640\" CELLPADDING=0 CELLSPACING=0><TR><TD>\n");

    print("<H1>PDF-o-matic</H1>\n"
     ."<P>PDF-o-matic is a simple PHP script "
     ."(<A HREF=\"pdf-o-matic.php?source\">view source</A>) "
     ."that uses HTMLDOC to convert the web page of your choice. "
     ."Enter a URL to be converted to PDF and click on the "
     ."<VAR>Make PDF!</VAR> button:</P>\n"
         ."<FORM METHOD=\"GET\" ACTION=\"$PHP_SELF\">\n"
     ."<CENTER><INPUT TYPE=\"TEXT\" NAME=\"URL\" SIZE=\"40\" VALUE=\"http://\">\n"
     ."<INPUT TYPE=\"SUBMIT\" VALUE=\"Make PDF!\">\n"
     ."<INPUT TYPE=\"RESET\" VALUE=\"Clear URL\">\n");

    // The following hidden variable fixes a HUGE bug in Microsoft
    // Internet Destroyer (all versions) where MSIE ignores the
    // Content-Type field and instead uses the "extension" on the
    // end of the URL...

    print("<INPUT TYPE=\"HIDDEN\" NAME=\"FORMAT\" VALUE=\".pdf\">"
     ."</CENTER></FORM>\n");

    print("<P>Please make sure that your HTML code is error free and that all "
         ."the elements are supported with HTMLDOC. "
    ."<A HREF=\"htmldoc.html#HTMLREF\">Chapter 6</A> of the HTMLDOC "
    ."Users Manual lists the elements that are supported.</P>\n");

    print("<CENTER><TABLE BORDER BGCOLOR=\"#cccccc\">\n"
         ."<TR>"
         ."<TH ALIGN=\"RIGHT\">Server:</TH>"
     ."<TD>Dual 2.4GHz Xeon with 2GB RAM running Linux</TD>"
     ."</TR>\n"
         ."<TR>"
         ."<TH ALIGN=\"RIGHT\">Status:</TH><TD>");
    system("ps -A | awk '{print $4}' | grep htmldoc | wc -l");
    print("copies of HTMLDOC running<BR>System load average = ");
    system("uptime | awk '{printf(\"%.2f\", ($10 + $11 + $12) / 3)}'");
    print("</TD></TR>\n"
         ."</TABLE></CENTER>\n");

    print("</TD></TR></TABLE>\n");
}


//
// 'bad_url()' - See if the URL contains bad characters...
//

function bad_url($url) {
    // See if the URL starts with http: or https:...
    if (strncmp($url, "http://", 7) != 0 &&
    strncmp($url, "https://", 8) != 0) {
        return 1;
    }

    // Check for bad characters in the URL...
    $len = strlen($url);
    for ($i = 0; $i < $len; $i ++) {
        if (!strchr("~_*()/:%?+-&@;=,$.0123456789"
               ."abcdefghijklmnopqrstuvwxyz"
           ."ABCDEFGHIJKLMNOPQRSTUVWXYZ", $url[$i])) {
        return 1;
    }
    }

    return 0;
}

        
//
// 'topdf()' - Convert the named file/URL to PDF.
//

function topdf($filename, $options = "") {
    # Write the content type to the client...
    header("Content-Disposition: inline; filename=\"pdf-o-matic.pdf\"");
    flush();

    # Run HTMLDOC to provide the PDF file to the user...
    # Use the --no-localfiles option for enhanced security!
    passthru("htmldoc --no-localfiles --no-compression -t pdf14 --webpage --pagemode document "
            ."$options '$filename'");
}


//
// MAIN ENTRY - see if we have form data...
//

global $URL;

if ($argc && $argv[0] == "source") {
    // Show source...
    print("<HTML><HEAD><TITLE>Source of PDF-o-matic</TITLE></HEAD><BODY><PRE>\"pdf-o-matic.php\":");
    highlight_file("pdf-o-matic.php");
    print("</PRE></BODY></HTML>\n");
} else if ($HTTP_GET_VARS["URL"]) {
    // Yes, see if the URL is a valid URL and not a filename (security...)
    $url = $HTTP_GET_VARS["URL"];
    $options = "";
    $self    = "http://$HTTP_HOST$PHP_SELF";

    if (bad_url($url)) {
    // Write the standard header...
          htmldoc_header("PDF-o-matic - HTMLDOC");

    // Show a form for the URL...
    show_form();

    // Show an error message...
    print("<P><B>Error!</B></P>\n"
             ."<P>\"$url\" is not a valid URL. Unable to process!</P>\n");

    // Show the standard footer...
    htmldoc_footer();
    } else
    topdf($url, "--header ... --footer ... --size letter --left 0.5in");
} else {
    // Write the standard header...
    htmldoc_header("PDF-o-matic - HTMLDOC");

    // Show a form for the URL...
    show_form();

    // Show the standard footer...
    htmldoc_footer();
}

?>
