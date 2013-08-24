<?
	if (!defined('INNER')) exit;

	class KRF_SQL
    {
        var $dbname;
        var $dbhost;
        var $dbuser;
        var $dbpass;
        var $errmsg;
        var $con;
        
        function KRF_SQL($dbuser, $dbpass, $dbhost, $dbname)
        {
            $this->dbname = $dbname;
            $this->dbuser = $dbuser;
            $this->dbpass = $dbpass;
            $this->dbhost = $dbhost;

            $this->con = mysql_connect($dbhost, $dbuser, $dbpass);
            
            mysql_select_db($dbname, $this->con);
            
            return $this->con;
        }

        function Open()
        {
			$this->Close();
			$this->con = mysql_connect($dbhost, $dbuser, $dbpass);        
        }
        
        function Close()
        {
            return mysql_close($this->con);
        }

        function Errno()
        {
            return mysql_errno($this->con);
        }

        function ListTables()
        {
            $Ret = array();
            
            $res = mysql_list_tables ($this->dbname, $this->con);
            for ($i=0; $i<$this->Numrows($res); $i++)
            $Ret[] = mysql_tablename($res, $i);

            return $Ret;
        }

        

        function Query($query)
        {
            $res = @mysql_query($query, $this->con);
            $this->errmsg = '';

            if ($res === FALSE)
            {
                $this->errmsg = mysql_error($this->con);
            }

            return $res;
        }

        function Numrows($res)
        {
            return mysql_num_rows ($res);
        }

        function Freeresult($res)
        {
            return mysql_free_result ($res);
        }

        function Insertid()
        {
            return mysql_insert_id ($this->con);
        }

        function Fetchrow($res)
        {
            return mysql_fetch_row ($res);
        }

        function Fetcharray($res, $mode = 'both')
        {
            if ($mode !== 'both')
            	$mode = ($mode == 'assoc') ? MYSQL_ASSOC : MYSQL_NUM;
            else
            	$mode = MYSQL_BOTH;

            return mysql_fetch_array($res, $mode);
        }

        function ListTables1()
        {
        	$ret = array();
        	$db = $this->Query('SHOW TABLES');
        	for($i=0; $i<$this->Numrows($db); $i++)
        	{
        		list($ret[]) = $this->Fetchrow($db);
        	}

        	return $ret;
        }

        function TableExists($table_name)
        {
        	return in_array($table_name, $this->ListTables());
        }

        function ListFields($table_name)
        {
        	$ret = array();
        	
        	$db = $this->Query("describe $table_name");
        	for($i=0; $i<$this->Numrows($db); $i++)
        	{
        		list($ret[],,,,,) = $this->Fetchrow($db);
        	}
        	
        	return $ret;
        }
    };
?>