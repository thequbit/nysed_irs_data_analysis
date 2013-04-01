<?php

	require_once("DatabaseTool.class.php");
	require_once("District.class.php");

	class DistrictTool
	{
	
		function GetIncidentCounts($districtid)
		{
			dprint( "GetIncidentCounts() Start." );
		
			try
			{
				$db = new DatabaseTool();

				$query = 'select schoolyears.schoolyearname as schoolyear, sum(vadirincidents.incidentcount) as incidentcount from vadirincidents inner join schools on schools.schoolid = vadirincidents.schoolid inner join schoolyears on vadirincidents.schoolyearid = schoolyears.schoolyearid where schools.districtid = ? group by vadirincidents.schoolyearid';
				
				$mysqli = $db->Connect();
				$stmt = $mysqli->prepare($query);
				// bind to query before execution
				$stmt->bind_param("s",$districtid);
				$results = $db->Execute($stmt);
			
				$db->Close($mysqli, $stmt);
			}
			catch (Exception $e)
			{
				dprint( "Caught exception: " . $e->getMessage() );
			}
			
			dprint("GetIncidentCounts() Done.");
			
			return $results;
		}
	
		function GetIncidentCount($districtid, $schoolyearid)
		{
			dprint( "GetIncidentCount() Start." );
		
			try
			{
				$db = new DatabaseTool();

				$query = 'select sum(tmp.totalincidents) from ( select sum(vadirincidents.incidentcount) as totalincidents  from vadirincidents inner join schools on schools.schoolid = vadirincidents.schoolid where vadirincidents.schoolyearid = ? and schools.districtid = ? group by schools.schoolname) as tmp';
				
				$mysqli = $db->Connect();
				$stmt = $mysqli->prepare($query);
				// bind to query before execution
				$stmt->bind_param("ss",$schoolyearid,$districtid);
				$results = $db->Execute($stmt);
			
				$count = $results[0]['count'];
			
				$db->Close($mysqli, $stmt);
			}
			catch (Exception $e)
			{
				dprint( "Caught exception: " . $e->getMessage() );
			}
			
			dprint("GetIncidentCount() Done.");
			
			return $count;
		}
	
		function GetSchoolCount($districtid)
		{
			dprint( "GetSchoolCount() Start." );
		
			try
			{
				$db = new DatabaseTool();

				$query = 'select count(schoolid) as count from schools where districtid = ?';
				
				$mysqli = $db->Connect();
				$stmt = $mysqli->prepare($query);
				// bind school id to query before execution
				$stmt->bind_param("s",$districtid);
				$results = $db->Execute($stmt);
			
				$db->Close($mysqli, $stmt);
			}
			catch (Exception $e)
			{
				dprint( "Caught exception: " . $e->getMessage() );
			}
			
			dprint("GetSchoolCount() Done.");
			
			return $results;
		}
	
		function GetDistrictCount()
		{
			dprint( "GetDistrictCount() Start." );
		
			try
			{
				$db = new DatabaseTool();

				$query = 'select count(districtid) as count from districts';
				
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
			
			dprint("GetDistrictCount() Done.");
			
			return $count;
		}
	
		function GetAllDistricts()
		{
			dprint( "GetAllDistricts() Start." );
		
			try
			{
				$db = new DatabaseTool();

				$query = 'SELECT districtid,districtname FROM districts order by districtname';
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