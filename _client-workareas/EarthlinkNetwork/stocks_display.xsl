<?xml version='1.0'?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/TR/WD-xsl">
  <xsl:template match="/">
    <HTML>
	<head>
<STYLE type="text/css">
.table {width:45%;border:0}

.table2 {width:45%;border:0}

.stocks {text-indent:2%;font-family:helvetica;
font-size:20px;color:#ffffff;text-decoration:none;font-weight:bold;
width:50%;background-color:#6666CC;
}

.personalize {text-align:right;font-family:helvetica;letter-spacing:1px;
font-size:11.5px;color:#ffffff;text-decoration:underline;
width:50%;background-color:#6666CC; padding-right: 12.5px;
}

.topsymbol {align:left;font-family:helvetica;text-indent:2.5%;
font-size:10.5px;color:#000066;text-decoration:none;
width:25%;background-color:#F7F7F7;
}

.toprest {text-align:right;font-family:helvetica;
font-size:10.5px;color:#000066;text-decoration:underline;
width:25%;background-color:#E7E7E7; padding-right: 12.5px;
}

.myport {font-family:helvetica;text-indent:2%;
font-size:11px;font-weight:bold;color:#000066;text-decoration:underline;
background-color:#CCCCFF;width:50%;
}

.details {text-align:right;font-family:helvetica;height:22px;
font-size:11.5px;font-weight:bold;color:#000066;text-decoration:underline;
background-color:#CCCCFF;width:50%; padding-right: 12.5px;
}

.symbol {font-family:helvetica;text-indent:2.5%;background-color:#FFFFFF;
font-size:11.5px; color:#000066;text-decoration:underline;
}

.last {font-family:helvetica;text-indent:2.5%;letter-spacing:1px;
font-size:11.5px; color:#000000; padding-right: 12.5px;background-color:#F7F7F7;
}

.change {font-family:helvetica;text-indent:2.5%;letter-spacing:1px;
font-size:11.5px;color:#CE0031; padding-right: 12.5px;background-color:#F7F7F7;
}

.volume {font-family:helvetica;align:right;text-indent:2.5%;letter-spacing:1px;
font-size:11.5px; color:#000000; padding-right: 12.5px;background-color:#F7F7F7;
}

.symbol2 {font-family:helvetica;text-indent:2.5%;background-color:#F7F7F7;
font-size:11.5px; color:#000066;text-decoration:underline;
}

.last2 {font-family:helvetica;text-indent:2.5%;letter-spacing:1px;
font-size:11.5px; color:#000000; padding-right: 12.5px;background-color:#E7E7E7;
}

.change2 {font-family:helvetica;text-indent:2.5%;letter-spacing:1px;
font-size:11.5px;color:#CE0031; padding-right: 12.5px;background-color:#E7E7E7;
}

.volume2 {font-family:helvetica;align:right;text-indent:2.5%;letter-spacing:1px;
font-size:11.5px; color:#000000; padding-right: 12.5px;background-color:#E7E7E7;
}

.disclaimer {font-family:helvetica;text-decoration:underline;letter-spacing:1px;
font-size:10.5px; color:#000066; background-color:#CCCCFF
}

.text {font-family:helvetica;letter-spacing:1px;
font-size:10.5px; color:#000000; background-color:#CCCCFF;
}

.input {font-family:helvetica;align:left;valign:middle;padding-top:7px;width:100px;background-color:#CCCCFF;align:left;
font-size:11px; color:#000000; text-indent:1%;padding-bottom:3px;padding-left:17px
}

.input2 {background-color:#CCCCFF;align:left;
}

.pcquote {align:left;padding-left:20px;background-color:#CCCCFF;width:10%;height:31px;
}

.green {font-family:helvetica;text-indent:2.5%;letter-spacing:1px;
font-size:11.5px;color:#006531; padding-right: 12.5px;background-color:#E7E7E7;
}

.breaker {align:left;bgcolor:#ffffff;height:1px;colspan:4}
</STYLE>
</head>
      <BODY>
<DIV width="45%" height="500px" style="position:absolute;left:0px;top:0px">
        <TABLE cellspacing="0" class="table" width="100%">
          <TR>
            <TD colspan="2" class="stocks">stocks</TD>
            <TD colspan="2" class="personalize">personalize<img src="arrow.gif" /></TD> 
         </TR>
          <TR>
            <TD colspan="2" class="myport">My Portfolios</TD>
            <TD colspan="2" class="details">Details Page</TD>
          </TR>
			<TR>
              <TD class="breaker"></TD>
            </TR>
</TABLE>
        <TABLE cellspacing="0" class="table" width="100%" height="106px">
	  <TR>
            <TD class="topsymbol">Symbol</TD>
            <TD class="toprest">Last</TD>
            <TD class="toprest">Change</TD>
            <TD class="toprest">Volume</TD>
          </TR>
          <xsl:for-each select="stocks_data/stock">
            <TR>
              <TD align="left" class="symbol"><xsl:value-of select="symbol"/></TD>
              <TD align="right" class="last"><xsl:value-of select="last"/></TD>
              <TD align="right" class="change"><xsl:value-of select="change"/></TD>
	     	  <TD align="right" class="volume"><xsl:value-of select="volume"/></TD>
            </TR>
          </xsl:for-each>
          <xsl:for-each select="stocks_data/stock2">
            <TR>
              <TD align="left" class="symbol2"><xsl:value-of select="symbol"/></TD>
              <TD align="right" class="last2"><xsl:value-of select="last"/></TD>
              <TD align="right" class="green"><xsl:value-of select="change"/></TD>
	     	  <TD align="right" class="volume2"><xsl:value-of select="volume"/></TD>
            </TR>
          </xsl:for-each>
          <xsl:for-each select="stocks_data/stock3">
            <TR>
              <TD align="left" class="symbol"><xsl:value-of select="symbol"/></TD>
              <TD align="right" class="last"><xsl:value-of select="last"/></TD>
              <TD align="right" class="change"><xsl:value-of select="change"/></TD>
	     	  <TD align="right" class="volume"><xsl:value-of select="volume"/></TD>
            </TR>
          </xsl:for-each>
          <xsl:for-each select="stocks_data/stock4">
            <TR>
              <TD align="left" class="symbol2"><xsl:value-of select="symbol"/></TD>
              <TD align="right" class="last2"><xsl:value-of select="last"/></TD>
              <TD align="right" class="change2"><xsl:value-of select="change"/></TD>
	     	  <TD align="right" class="volume2"><xsl:value-of select="volume"/></TD>
            </TR>
          </xsl:for-each>
          <xsl:for-each select="stocks_data/stock5">
            <TR>
              <TD align="left" class="symbol"><xsl:value-of select="symbol"/></TD>
              <TD align="right" class="last"><xsl:value-of select="last"/></TD>
              <TD align="right" class="change"><xsl:value-of select="change"/></TD>
	     	  <TD align="right" class="volume"><xsl:value-of select="volume"/></TD>
            </TR>
          </xsl:for-each>
            </TABLE>
		<TABLE cellspacing="0" class="table" height="15px" width="100%">
			<TR>
              <TD class="input" width="33%">Enter a symbol or company name:</TD>
			  <TD class="input2" width="66%"><INPUT TYPE="text" NAME="NAME" SIZE="6" style="height:19px"/><img src="break.gif"/><INPUT TYPE="button" VALUE="Get Quote" NAME="NAME" SIZE="7"/></TD>
            </TR>
			<TR>
              <TD class="breaker"></TD>
            </TR>
            </TABLE>
		<TABLE cellspacing="0" class="table2" height="31px" width="100%" align="center">
			<TR>
	          <TD class="pcquote" width="33%" align="right"><img src="pcquote.gif"/></TD>
          <xsl:for-each select="stocks_data/stock6">
              <TD class="text" width="66%" align="center"><xsl:value-of select="text"/><font class="disclaimer"/><xsl:value-of select="disclaimer"/></TD>
          </xsl:for-each>
            </TR>
        </TABLE>
		</DIV>
      </BODY>
    </HTML>
  </xsl:template>
</xsl:stylesheet>