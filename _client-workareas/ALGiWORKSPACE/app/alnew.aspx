<%@ Page Language="VB" %>


<script runat="server">
    Sub Run_Launch_Sequence

		Dim LeadNumber = Request.QueryString("ln")
		Dim CFirstName = Request.QueryString("f")
		Dim CLastName = Request.QueryString("l")
		Dim CAddress1 = Request.QueryString("a1")
		Dim CAddress2 = Request.QueryString("a2")
		Dim CCity = Request.QueryString("c")
		Dim CState = Request.QueryString("s")
		Dim CZip = Request.QueryString("z")
		Dim CHomeNumber = Request.QueryString("h")
		Dim CWorkNumber = ""
		Dim CEmail = Request.QueryString("e")
		Dim CIncome = ""
		Dim CRating = ""
		Dim BFirstName = ""
		Dim BLastName = ""
		Dim BEmail = ""
		Dim LeadSource = "555"
		Dim Employer = ""
		Dim YearEmployed = ""
		Dim EntryDate = Request.QueryString("ed")
		Dim LastModDate = ""
		Dim OriginatorID = ""
		Dim LeadDate = <!-- TODAYS DATE -->
		Dim TeleMKTName = ""
		Dim Soli = ""
		Dim LeadStatus = ""
		Dim RemoveLead = ""
		Dim BorSSN = ""
		Dim LeadSourceInfo = ""
		Dim CreditScore = ""
		Dim CellNumber = Request.QueryString("cn")
		Dim AlternateNumber = Request.QueryString("an")
		Dim StatusID = Request.QueryString("cs")
		Dim PropertyTypeID = Request.QueryString("pt")
		Dim PurchasePrice = Request.QueryString("pp")
		Dim YearAcquired = Request.QueryString("ya")
		Dim PropertyValue = Request.QueryString("pv")
		Dim MortgageBalance1 = Request.QueryString("mb1")
		Dim Rate1 = Request.QueryString("mr1")
		Dim Rate1TypeID = Request.QueryString("rt1")
		Dim MonthlyPayment = Request.QueryString("mp")
		Dim MortgageBalance2 = Request.QueryString("mb2")
		Dim Rate2 = Request.QueryString("mr2")
		Dim Rate2TypeID = Request.QueryString("rt2")
		Dim CallTime = Request.QueryString("ct")
		Dim TypeDesire = Request.QueryString("td")
		Dim LoanDesire = Request.QueryString("ld")
		Dim LastFinanced = Request.QueryString("lf")
		Dim LTV = Request.QueryString("ltv")
		Dim NumberPaymentBehind = ""
		Dim ISBehind = ""
		Dim IntendedFor = ""
		Dim DateSent = ""
		Dim IPAddress = ""
		Dim MessageCode = ""
		Dim I_MortDate = Request.QueryString("md1")
		Dim II_MortDate = Request.QueryString("md2")
		Dim InterestRate = Request.QueryString("ir")
		Dim Terms = ""
		Dim CreditCardBal = Request.QueryString("cb")
		Dim CashOut = Request.QueryString("co")
		Dim LastUpdateDate = <!-- TODAYS DATE -->
		Dim LastUpdatedBy = ""
		Dim DialerLastCall = ""
		Dim DialerLastResult = ""
		Dim DialerRetryCount = ""
		Dim LastStatusAuditID = ""
		Dim LastDialerLogID = ""

		
    	Dim oDR as System.Data.SQLClient.SQLDataReader
        Dim oCom As System.Data.SQLClient.SqlCommand
        Dim oConn as System.Data.SQLClient.SQLConnection

        try
            oConn = New System.Data.SQLClient.SQLConnection ("server=localhost; initial catalog=MTG_Americor;uid=sa;pwd=lt4G-OY0409")
			oConn.Open()
			oCom = New System.Data.SQLClient.SqlCommand()
			oCom.Connection = oConn



					oCom.CommandText = "INSERT INTO LMSMainDataTbl ( "
					oCom.CommandText = oCom.CommandText & "	LeadNumber, CFirstName, CLastName, CAddress1, CAddress2, "
					oCom.CommandText = oCom.CommandText & "	CCity, CState, CZip, CHomeNumber, CWorkNumber, "
					oCom.CommandText = oCom.CommandText & "	CEmail, CIncome, CRating, BFirstName, BLastName, "
					oCom.CommandText = oCom.CommandText & "	BEmail, LeadSource, Employer, YearEmployed, EntryDate, "
					oCom.CommandText = oCom.CommandText & "	LastModDate, OriginatorID, LeadDate, TeleMKTName, Soli, "
					oCom.CommandText = oCom.CommandText & "	LeadStatus, RemoveLead, BorSSN, LeadSourceInfo, CreditScore, "
					oCom.CommandText = oCom.CommandText & "	CellNumber, AlternateNumber, StatusID, PropertyTypeID, PurchasePrice, "
					oCom.CommandText = oCom.CommandText & "	YearAcquired, PropertyValue, MortgageBalance1, Rate1, Rate1TypeID, "
					oCom.CommandText = oCom.CommandText & "	MonthlyPayment, MortgageBalance2, Rate2, Rate2TypeID, CallTime, "
					oCom.CommandText = oCom.CommandText & "	TypeDesire, LoanDesire, LastFinanced, LTV, NumberPaymentBehind, ISBehind, "
					oCom.CommandText = oCom.CommandText & "	IntendedFor, DateSent, IPAddress, MessageCode, I_MortDate, II_MortDate, "
					oCom.CommandText = oCom.CommandText & "	InterestRate, Terms, CreditCardBal, CashOut, LastUpdateDate, "
					oCom.CommandText = oCom.CommandText & "	LastUpdatedBy, DialerLastCall, DialerLastResult, DialerRetryCount, LastStatusAuditID, "
					oCom.CommandText = oCom.CommandText & "	LastDialerLogID"
					oCom.CommandText = oCom.CommandText & ")"

					oCom.CommandText = oCom.CommandText & "VALUES ("
					oCom.CommandText = oCom.CommandText & "	" & LeadNumber & ", " & CFirstName & ", " & CLastName & ", " & CAddress1 & ", " & CAddress2 & ", "
					oCom.CommandText = oCom.CommandText & "	" & CCity & ", " & CState & ", " & CZip & ", " & CHomeNumber & ", " & CWorkNumber & ", "
					oCom.CommandText = oCom.CommandText & "	" & CEmail & ", " & CIncome & ", " & CRating & ", " & BFirstName & ", " & BLastName & ", "
					oCom.CommandText = oCom.CommandText & "	" & BEmail & ", " & LeadSource & ", " & Employer & ", " & YearEmployed & ", " & EntryDate & ", "
					oCom.CommandText = oCom.CommandText & "	" & LastModDate & ", " & OriginatorID & ", " & LeadDate & ", " & TeleMKTName & ", " & Soli & ", "
					oCom.CommandText = oCom.CommandText & "	" & LeadStatus & ", " & RemoveLead & ", " & BorSSN & ", " & LeadSourceInfo & ", " & CreditScore & ", "
					oCom.CommandText = oCom.CommandText & "	" & CellNumber & ", " & AlternateNumber & ", " & StatusID & ", " & PropertyTypeID & ", " & PurchasePrice & ", "
					oCom.CommandText = oCom.CommandText & "	" & YearAcquired & ", " & PropertyValue & ", " & MortgageBalance1 & ", " & Rate1 & ", " & Rate1TypeID & ", "
					oCom.CommandText = oCom.CommandText & "	" & MonthlyPayment & ", " & MortgageBalance2 & ", " & Rate2 & ", " & Rate2TypeID & ", " & CallTime & ", "
					oCom.CommandText = oCom.CommandText & "	" & TypeDesire & ", " & LoanDesire & ", " & LastFinanced & ", " & LTV & ", " & NumberPaymentBehind & ", " & ISBehind & ", "
					oCom.CommandText = oCom.CommandText & "	" & IntendedFor & ", " & DateSent & ", " & IPAddress & ", " & MessageCode & ", " & I_MortDate & ", " & II_MortDate & ", "
					oCom.CommandText = oCom.CommandText & "	" & InterestRate & ", " & Terms & ", " & CreditCardBal & ", " & CashOut & ", " & LastUpdateDate & ", "
					oCom.CommandText = oCom.CommandText & "	" & LastUpdatedBy & ", " & DialerLastCall & ", " & DialerLastResult & ", " & DialerRetryCount & ", " & LastStatusAuditID & ", "
					oCom.CommandText = oCom.CommandText & "	" & LastDialerLogID"
					oCom.CommandText = oCom.CommandText & ")"
			oCom.CommandText = "INSERT INTO LMSImport_StateTbl ( StateCode, StateName, TimeZone ) VALUES ( " & fn & ", " & fn & ", 1) "
			oCom.ExecuteNonQuery()
        catch
	    	Dim errDesc = err.Description
            	Run_Update_Sequence()
        Finally
        	oDR = Nothing
        	oCom = Nothing
        	oConn.Close()
        	oConn = Nothing
        end try

		Response.Write(fn)
    
	End Sub
	
	sub Run_Update_Sequence
		Response.Write("Updated: ")
	End Sub

</script>



<%Run_Launch_Sequence()%>
