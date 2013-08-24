<%@ Page Language="VB" %>

<script runat="server">

    Sub Run_Launch_Sequence

		Dim CallCUID = Request.QueryString("u")
		Dim StatTo = Request.QueryString("st")
		Dim LeadNumber = Request.QueryString("ln")
		Dim EndUserID = Request.QueryString("eu")
		
		Dim saID = ""

		Dim CFirstNameS As String = Request.QueryString("f")
		Dim CLastNameS = Request.QueryString("l")
		Dim CAddress1S = Request.QueryString("a1")
		Dim CAddress2S = Request.QueryString("a2")
		Dim CCity = Request.QueryString("c")
		Dim CState = Request.QueryString("s")
		Dim CZip = Request.QueryString("z")

		Dim CHomeNumber = Request.QueryString("h")

		Dim CWorkNumber = Request.QueryString("w")
		' same as stat to
		Dim StatusID = Request.QueryString("st")

		Dim CFirstName As String = CFirstNameS.Replace("-", " ")
		Dim CLastName As String = CLastNameS.Replace("-", " ")
		Dim CAddress1 As String = CAddress1S.Replace("-", " ")
		Dim CAddress2 As String = CAddress2S.Replace("-", " ")
		
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

			' if works continue on with adding LA and SA
			oCom.CommandText = "INSERT INTO LMSLeadAssignees ( LeadNumber, UserID, UserTypeID, CreationDate) VALUES (" & LeadNumber & ", " & EndUserID & ", 7, GETDATE())"
			oCom.ExecuteNonQuery()

			oCom.CommandText = "	INSERT INTO LMSStatusAuditTbl (LeadNumber, CreationDate, StatusChangedFrom, StatusChangedTo, ChangedBy, UserTypeID) VALUES (" & LeadNumber & ", GETDATE(), 39, 48, " & CallCUID & ", 7) "
			oCom.ExecuteNonQuery()

			oCom.CommandText = "	INSERT INTO LMSStatusAuditTbl (LeadNumber, CreationDate, StatusChangedTo, StatusChangedTo, ChangedBy, UserTypeID) VALUES (" & LeadNumber & ", GETDATE(), 48, 38, " & CallCUID & ", 7) " & _
							   "SELECT @@IDENTITY As 'Identity'"
			Dim iID As Integer
			iID = oCom.ExecuteScalar()
			saID = iID.ToString()

			' finish by updating fields for this LID row
		  	oCom.CommandText = "UPDATE LMSMainDataTbl SET CFirstName = '" & CFirstName.ToString() & "', CLastName = '" & CLastName.ToString() & "', CAddress1 = '" & CAddress1.ToString() & "', CAddress2 = '" & CAddress2.ToString() & "', CCity = '" & CCity & "', CState = '" & CState & "', CZip = " & CZip & ", CHomeNumber = " & CHomeNumber & ", CWorkNumber = " & CWorkNumber & ", StatusID = '38', LastUpdateDate = GETDATE(), LastStatusAuditID = '" & saID & "' WHERE LeadNumber = '" &  LeadNumber & "'"
			oCom.ExecuteNonQuery()			
			
			
        catch

			' add LA and SA
			oCom.CommandText = "INSERT INTO LMSLeadAssignees ( LeadNumber, UserID, UserTypeID, CreationDate) VALUES (" & LeadNumber & ", " & EndUserID & ", 7, GETDATE())"
			oCom.ExecuteNonQuery()

			oCom.CommandText = "	INSERT INTO LMSStatusAuditTbl (LeadNumber, CreationDate, StatusChangedTo, ChangedBy, UserTypeID) VALUES (" & LeadNumber & ", GETDATE(), 38, " & CallCUID & ", 7) " & _
							   "SELECT @@IDENTITY As 'Identity'"
			Dim iID As Integer
			iID = oCom.ExecuteScalar()
			saID = iID.ToString()

			' finish by updating fields for this LID row
		  	oCom.CommandText = "UPDATE LMSMainDataTbl SET CFirstName = '" & CFirstName.ToString() & "', CLastName = '" & CLastName.ToString() & "', CAddress1 = '" & CAddress1.ToString() & "', CAddress2 = '" & CAddress2.ToString() & "', CCity = '" & CCity & "', CState = '" & CState & "', CZip = " & CZip & ", CHomeNumber = " & CHomeNumber & ", CWorkNumber = " & CWorkNumber & ", StatusID = '38', LastUpdateDate = GETDATE(), LastStatusAuditID = '" & saID & "' WHERE LeadNumber = '" &  LeadNumber & "'"
			oCom.ExecuteNonQuery()

			Dim errDesc = err.Description
			
        Finally
        	oDR = Nothing
        	oCom = Nothing
        	oConn.Close()
        	oConn = Nothing
        end try

		Response.Write(saID)

	End Sub
	

</script>



<%Run_Launch_Sequence()%>

