// ADD NEW ASSIGNEE (ONLY AFTER ADDITION OF LEAD TO SYSTEM)
			oCom.CommandText = "INSERT INTO LMSLeadAssignees (LeadNumber, UserID, UserTypeID, CreationDate) VALUES (10000016007, 7, 8, GETDATE()) "

// INSERT INTO STATE

			oCom.CommandText = "INSERT INTO LMSImport_StateTbl ( StateCode, StateName, TimeZone ) "
			oCom.CommandText = oCom.CommandText & "VALUES ( " & LeadNumber & ", " & CFirstName & ", " & CLastName & ") "
			
			
			
			