<%@ Page Language="VB" %>

<script runat="server">
    Sub Run_Launch_Sequence

		Dim LeadNumber = Request.QueryString("ln")

    	Dim oDR as System.Data.SQLClient.SQLDataReader
        Dim oCom As System.Data.SQLClient.SqlCommand
        Dim oConn as System.Data.SQLClient.SQLConnection

		LeadNumber = LeadNumber & "007"

        try
            oConn = New System.Data.SQLClient.SQLConnection ("server=localhost; initial catalog=MTG_Americor;uid=sa;pwd=lt4G-OY0409")
			oConn.Open()
			oCom = New System.Data.SQLClient.SqlCommand()
			oCom.Connection = oConn
			
			oCom.CommandText = "INSERT INTO LMSMainDataTbl (LeadNumber) VALUES (" & LeadNumber & ") "
			oCom.ExecuteNonQuery()

        catch
	    	Dim errDesc = err.Description
        Finally
        	oDR = Nothing
        	oCom = Nothing
        	oConn.Close()
        	oConn = Nothing
        end try

       	Run_Update_Sequence()

		Response.Write(LeadNumber)

	End Sub


	sub Run_Update_Sequence

	
		Dim LeadNumber = Request.QueryString("ln")
		Dim CallCUID = Request.QueryString("u")
		Dim StatTo = Request.QueryString("st")

		Dim CFirstName = Request.QueryString("f")
		Dim CLastName = Request.QueryString("l")
		Dim CAddress1 = Request.QueryString("a1")
		Dim CAddress2 = Request.QueryString("a2")
		Dim CCity = Request.QueryString("c")
		Dim CState = Request.QueryString("s")
		Dim CZip = Request.QueryString("z")

		Dim CHomeNumber = Request.QueryString("h")

		Dim CWorkNumber = Request.QueryString("w")
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
		Dim LeadDate = "<!-- TODAYS DATE -->"
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
		Dim LastUpdateDate = "<!-- TODAYS DATE -->"
		Dim LastUpdatedBy = ""
		Dim DialerLastCall = ""
		Dim DialerLastResult = ""
		Dim DialerRetryCount = ""
		Dim LastStatusAuditID = ""
		Dim LastDialerLogID = ""

    	Dim oDR as System.Data.SQLClient.SQLDataReader
        Dim oCom As System.Data.SQLClient.SqlCommand
        Dim oConn as System.Data.SQLClient.SQLConnection

		LeadNumber = LeadNumber & "007"

    	Dim oDR2 as System.Data.SQLClient.SQLDataReader
        Dim oCom2 As System.Data.SQLClient.SqlCommand
        Dim oConn2 as System.Data.SQLClient.SQLConnection

        try
            oConn2 = New System.Data.SQLClient.SQLConnection ("server=localhost; initial catalog=MTG_Americor;uid=sa;pwd=lt4G-OY0409")
			oConn2.Open()
			oCom2 = New System.Data.SQLClient.SqlCommand()
			oCom2.Connection = oConn2
			
			oCom2.CommandText = "INSERT INTO LMSStatusAuditTbl (LeadNumber, CreationDate, StatusChangedTo, ChangedBy, UserTypeID) VALUES (" & LeadNumber & ", GETDATE(), " & StatTo & ", " & CallCUID & ", 7) "
			oCom2.ExecuteNonQuery()

			oCom2.CommandText = "INSERT INTO LMSLeadAssignees ( LeadNumber, UserID, UserTypeID, CreationDate) VALUES (" & LeadNumber & ", " & CallCUID & ", 7, GETDATE()) "
			oCom2.ExecuteNonQuery()

			oCom2.CommandText = "UPDATE LOW_PRIORITY LMSMainDataTbl SET " & _
				"CFirstName = '" & CFirstName & "', " & _
				"CLastName = '" & CLastName & "', " & _
				"CAddress1 = '" & CAddress1 & "', " & _
				"CAddress2 = '" & CAddress2 & "', " & _
				"CCity = '" & CCity & "', " & _
				"CState = '" & CState & "', " & _
				"CZip = '" & CZip & "', " & _
				"CHomeNumber = '" & CHomeNumber & "', " & _
				"CWorkNumber = '" & CWorkNumber & "', " & _
				"CEmail = '" & CEmail & "', " & _
				"CIncome = '" & CIncome & "', " & _
				"CRating = '" & CRating & "', " & _
				"BFirstName = '" & BFirstName & "', " & _
				"BLastName = '" & BLastName & "', " & _
				"BEmail = '" & BEmail & "', " & _
				"LeadSource = '" & LeadSource & "', " & _
				"Employer = '" & Employer & "', " & _
				"YearEmployed = '" & YearEmployed & "', " & _
				"EntryDate = '" & EntryDate & "', " & _
				"LastModDate = '" & LastModDate & "', " & _
				"OriginatorID = '" & OriginatorID & "', " & _
				"LeadDate = '" & LeadDate & "', " & _
				"TeleMKTName = '" & TeleMKTName & "', " & _
				"Soli = '" & Soli & "', " & _
				"LeadStatus = '" & LeadStatus & "', " & _
				"RemoveLead = '" & RemoveLead & "', " & _
				"BorSSN = '" & BorSSN & "', " & _
				"LeadSourceInfo = '" & LeadSourceInfo & "', " & _
				"CreditScore = '" & CreditScore & "', " & _
				"CellNumber = '" & CellNumber & "', " & _
				"AlternateNumber = '" & AlternateNumber & "', " & _
				"StatusID = '" & StatusID & "', " & _
				"PropertyTypeID = '" & PropertyTypeID & "', " & _
				"PurchasePrice = '" & PurchasePrice & "', " & _
				"YearAcquired = '" & YearAcquired & "', " & _
				"PropertyValue = '" & PropertyValue & "', " & _
				"MortgageBalance1 = '" & MortgageBalance1 & "', " & _
				"Rate1 = '" & Rate1 & "', " & _
				"Rate1TypeID = '" & Rate1TypeID & "', " & _
				"MonthlyPayment = '" & MonthlyPayment & "', " & _
				"MortgageBalance2 = '" & MortgageBalance2 & "', " & _
				"Rate2 = '" & Rate2 & "', " & _
				"Rate2TypeID = '" & Rate2TypeID & "', " & _
				"CallTime = '" & CallTime & "', " & _
				"TypeDesire = '" & TypeDesire & "', " & _
				"LoanDesire = '" & LoanDesire & "', " & _
				"LastFinanced = '" & LastFinanced & "', " & _
				"LTV = '" & LTV & "', " & _
				"NumberPaymentBehind = '" & NumberPaymentBehind & "', " & _
				"ISBehind = '" & ISBehind & "', " & _
				"IntendedFor = '" & IntendedFor & "', " & _
				"DateSent = '" & DateSent & "', " & _
				"IPAddress = '" & IPAddress & "', " & _
				"MessageCode = '" & MessageCode & "', " & _
				"I & _MortDate = '" & I & _MortDate & "', " & _
				"II & _MortDate = '" & II & _MortDate & "', " & _
				"InterestRate = '" & InterestRate & "', " & _
				"Terms = '" & Terms & "', " & _
				"CreditCardBal = '" & CreditCardBal & "', " & _
				"CashOut = '" & CashOut & "', " & _
				"LastUpdateDate = '" & LastUpdateDate & "', " & _
				"LastUpdatedBy = '" & LastUpdatedBy & "', " & _
				"DialerLastCall = '" & DialerLastCall & "', " & _
				"DialerLastResult = '" & DialerLastResult & "', " & _
				"DialerRetryCount = '" & DialerRetryCount & "', " & _
				"LastStatusAuditID = '" & LastStatusAuditID & "', " & _
				"LastDialerLogID = '" & LastDialerLogID & "' " & _
				"WHERE LeadNumber = '" &  LeadNumber & "' "

			oCom2.ExecuteNonQuery()


        catch
	    	Dim errDesc = err.Description
        Finally
        	oDR2 = Nothing
        	oCom2 = Nothing
        	oConn2.Close()
        	oConn2 = Nothing
        end try

		Response.Write("Updated: ")
	End Sub

</script>



<%Run_Launch_Sequence()%>

