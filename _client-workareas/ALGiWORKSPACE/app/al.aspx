<%@ Page Language="VB" %>

<script runat="server">

    Sub Run_Launch_Sequence

		Dim LeadNumber = Request.QueryString("ln")

		Dim saID = ""

		Dim CFirstNameS As String = Request.QueryString("f")
		Dim CLastNameS = Request.QueryString("l")
		Dim CAddress1S = Request.QueryString("a1")
		Dim CAddress2S = Request.QueryString("a2")
		Dim CCityS = Request.QueryString("c")
		Dim CStateS = Request.QueryString("s")
		Dim CZip = Request.QueryString("z")

		Dim CHomeNumber = Request.QueryString("h")

		' same as stat to
		Dim CFirstName As String = CFirstNameS.Replace("-", " ")
		Dim CLastName As String = CLastNameS.Replace("-", " ")
		Dim CAddress1 As String = CAddress1S.Replace("-", " ")
		Dim CAddress2 As String = CAddress2S.Replace("-", " ")
		Dim CCity As String = CCityS.Replace("-", " ")
		Dim CState As String = CStateS.Replace("-", " ")

		Dim MortgageBalance1 = Request.QueryString("mf")
		Dim MortgageRate1 = Request.QueryString("rf")
		Dim MortgageBalance2 = Request.QueryString("ms")
		Dim MortgageRate2 = Request.QueryString("rs")
		Dim PropertyValue = Request.QueryString("pv")
		Dim CashOut = Request.QueryString("co")
		Dim CreditCardBalance = Request.QueryString("cb")

    	Dim oDR as System.Data.SQLClient.SQLDataReader
        Dim oCom As System.Data.SQLClient.SqlCommand
        Dim oConn as System.Data.SQLClient.SQLConnection

		LeadNumber = LeadNumber & "007"

        try
            oConn = New System.Data.SQLClient.SQLConnection ("server=localhost; initial catalog=MTG_Americor;uid=sa;pwd=lt4G-OY0409")
			oConn.Open()
			oCom = New System.Data.SQLClient.SqlCommand()
			oCom.Connection = oConn

			' try adding, error = more than likely LID already in table, update row as the catch
			oCom.CommandText = "INSERT INTO LMSMainDataTbl (LeadNumber, LastUpdateDate) VALUES ('" & LeadNumber & "', GETDATE());"
			oCom.ExecuteNonQuery()
			' if works (LEAD NOT AT LMS - NEW LEAD - SET EntryDate to 03/17/2006 1:58:00 [common current])

			' finish by updating fields for this LID row
		  	oCom.CommandText = "UPDATE LMSMainDataTbl SET CFirstName = '" & CFirstName.ToString() & "', CLastName = '" & CLastName.ToString() & "', CAddress1 = '" & CAddress1.ToString() & "', CAddress2 = '" & CAddress2.ToString() & "', CCity = '" & CCity.ToString() & "', CState = '" & CState.ToString() & "', CZip = " & CZip & ", CHomeNumber = " & CHomeNumber & ", PropertyValue = " & PropertyValue & ", MortgageBalance1 = " & MortgageBalance1 & ", Rate1 = " & MortgageRate1 & ", MortgageBalance2 = " & MortgageBalance2 & ", Rate2 = " & MortgageRate2 & ", LoanDesire = " & CashOut & ", CreditCardBal = " & CreditCardBalance & ", LastUpdateDate = GETDATE() WHERE LeadNumber = '" &  LeadNumber & "'"
			oCom.ExecuteNonQuery()


        catch

			' this is error catch for addition try of lead, so if this comes thru simple shield the error:
			' finish by updating fields for this LID row
		  	oCom.CommandText = "UPDATE LMSMainDataTbl SET CFirstName = '" & CFirstName.ToString() & "', CLastName = '" & CLastName.ToString() & "', CAddress1 = '" & CAddress1.ToString() & "', CAddress2 = '" & CAddress2.ToString() & "', CCity = '" & CCity.ToString() & "', CState = '" & CState.ToString() & "', CZip = " & CZip & ", CHomeNumber = " & CHomeNumber & ", PropertyValue = " & PropertyValue & ", MortgageBalance1 = " & MortgageBalance1 & ", Rate1 = " & MortgageRate1 & ", MortgageBalance2 = " & MortgageBalance2 & ", Rate2 = " & MortgageRate2 & ", LoanDesire = " & CashOut & ", CreditCardBal = " & CreditCardBalance & ", LastUpdateDate = GETDATE() WHERE LeadNumber = '" &  LeadNumber & "'"
			oCom.ExecuteNonQuery()

			Dim errDesc = err.Description

        Finally
        	oDR = Nothing
        	oCom = Nothing
        	oConn.Close()
        	oConn = Nothing
        end try

		Response.Write(LeadNumber)

	End Sub

</script>

<%Run_Launch_Sequence()%>
