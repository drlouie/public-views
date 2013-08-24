<?xml version='1.0'?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/TR/WD-xsl">
  <xsl:template match="/">
    <HTML>
	<head>
<STYLE type="text/css">
.table {width:44%;border:0}

.stocks {text-indent:2%;font-family:helvetica;
font-size:20px;color:#ffffff;text-decoration:none;font-weight:bold;
width:50%;background-color:#6666CC;
}

.personalize {text-align:right;font-family:helvetica;letter-spacing:1px;
font-size:11.5px;color:#ffffff;text-decoration:underline;
width:50%;background-color:#6666CC;
}

.topsymbol {align:left;font-family:helvetica;text-indent:2.5%;
font-size:11.5px;color:#000066;text-decoration:none;
width:25%;background-color:#F7F7F7;
}

.toprest {text-align:right;font-family:helvetica;
font-size:11.5px;color:#000066;text-decoration:underline;
width:25%;background-color:#E7E7E7;
}

.myport {font-family:helvetica;text-indent:2%;
font-size:11.5px;font-weight:bold;color:#000066;text-decoration:underline;
background-color:#CCCCFF;width:50%;
}

.details {text-align:right;font-family:helvetica;height:22px;
font-size:11.5px;font-weight:bold;color:#000066;text-decoration:underline;
background-color:#CCCCFF;width:50%;
}

.symbol {font-family:helvetica;text-indent:2.5%;
font-size:11.5px; color:#000066;text-decoration:underline;
}

.last {font-family:helvetica;text-indent:2.5%;letter-spacing:1px;
font-size:11.5px; color:#000000;
}

.change {font-family:helvetica;text-indent:2.5%;letter-spacing:1px;
font-size:11.5px; color:#2b6988;
}

.volume {font-family:helvetica;align:right;text-indent:2.5%;letter-spacing:1px;
font-size:11.5px; color:#000000;
}

</STYLE>
</head>
      <BODY>
        <TABLE cellspacing="0" class="table">
          <TR>
            <TD colspan="2" class="stocks">stocks</TD>
            <TD colspan="2" class="personalize">personalize</TD>
          </TR>
          <TR>
            <TD colspan="2" class="myport">My Portfolios</TD>
            <TD colspan="2" class="details">Details Page</TD>
          </TR>
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
        </TABLE>
      </BODY>
    </HTML>
  </xsl:template>
</xsl:stylesheet>