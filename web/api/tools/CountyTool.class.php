<?php

	require_once("DatabaseTool.class.php");
	require_once("County.class.php");

	class CountyTool
	{
	
		function GetCountyCount()
		{
			dprint( "GetCountyCount() Start." );
		
			try
			{
				$db = new DatabaseTool();

				$query = 'select count(countyid) as count from counties';
				
				$mysqli = $db->Connect();
				$stmt = $mysqli->prepare($query);
				$results = $db->Execute($stmt);
			
				$count = $results[0]['count'];
			
				$db->Close($mysqli, $stmt);
			}
			catch (Exception $e)
			{
				dprint( "Caught exception: " . $e->getMessage() );
			}
			
			dprint("GetCountyCount() Done.");
			
			return $count;
		}
	
		function GetAllCounties()
		{
			dprint( "GetAllCounties() Start." );
		
			try
			{
				$db = new DatabaseTool();

				$query = 'SELECT countyid,countyname,geometry FROM counties';
				$mysqli = $db->Connect();
				$stmt = $mysqli->prepare($query);
				$results = $db->Execute($stmt);
			
				$counties = array();
				foreach( $results as $row )
				{
					$county = new County();
					
					$county->countyid 	= $row['countyid'];
					$county->countyname = $row['countyname'];
					$county->geometry	= $row['geometry'];
				
					$counties[] = $county;
				}
				
				$db->Close($mysqli, $stmt);
			}
			catch (Exception $e)
			{
				dprint( "Caught exception: " . $e->getMessage() );
			}
			
			dprint("GetAllCounties() Done.");
		
			return $counties;
		}
	}

?>