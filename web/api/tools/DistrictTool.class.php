<?php

	require_once("DatabaseTool.class.php");
	require_once("District.class.php");

	class DistrictTool
	{
		function GetAllDistricts()
		{
			dprint( "GetAllDistricts() Start." );
		
			try
			{
				$db = new DatabaseTool();

				$query = 'SELECT districtid,districtname FROM districts';
				$mysqli = $db->Connect();
				$stmt = $mysqli->prepare($query);
				$results = $db->Execute($stmt);
			
				$districts = array();
				foreach( $results as $row )
				{
					$district = new District();
					
					$district->districtid 	= $row['districtid'];
					$district->districtname = $row['districtname'];
					$district->countyid = $row['countyid'];
				
					$districts[] = $district;
				}
				
				$db->Close($mysqli, $stmt);
			}
			catch (Exception $e)
			{
				dprint( "Caught exception: " . $e->getMessage() );
			}
			
			dprint("GetAllDistricts() Done.");
		
			return $districts;
		}
	}

?>