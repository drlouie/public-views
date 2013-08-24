<%@ Page Language="VB" %>


<script runat="server">
    
	Sub Page_Data
    	
	Dim oDR as System.Data.SQLClient.SQLDataReader
        Dim oCom As System.Data.SQLClient.SqlCommand
        Dim oConn as System.Data.SQLClient.SQLConnection

		
        try
            oConn = New System.Data.SQLClient.SQLConnection ("server=localhost; initial catalog=MTG_Americor;uid=sa;pwd=lt4G-OY0409")
			oConn.Open()
			oCom = New System.Data.SQLClient.SqlCommand()
			oCom.Connection = oConn

			oCom.CommandText = "SELECT DISTINCT LMSEmployeesTbl.FirstName, LMSEmployeesTbl.LastName, LMSEmployeesTbl.UserID, LMSEmployeesTbl.CreationDate FROM LMSUserStatusesTbl  INNER JOIN LMSEmployeesTbl ON LMSEmployeesTbl.UserID = LMSUserStatusesTbl.UserID AND LMSUserStatusesTbl.UserTypeID = '1' AND (LMSEmployeesTbl.CurrentEmployee = 'Y') AND (LMSEmployeesTbl.LastName <> '5006') AND (LMSEmployeesTbl.LastName <> 'Ex Employee') AND (LMSEmployeesTbl.LastName <> 'Admin') AND (LMSEmployeesTbl.LastName <> 'Manager') ORDER BY LMSEmployeesTbl.CreationDate"

			oDR = oCom.ExecuteReader()
			While oDR.Read
	    		Response.Write(oDR.Item("LastName") & "%%%%%" & oDR.Item("FirstName") & "%%%%%" & oDR.Item("UserID") & vbCrLf)

			End While
        catch
            Response.Write("Error:" & err.Description)
        Finally

        	oDR = Nothing
        	oCom = Nothing
        	oConn.Close()
        	oConn = Nothing
        end try

    
	End Sub
</script>



<%Page_Data()%>

