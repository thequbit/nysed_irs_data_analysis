<?php

	require_once("DatabaseTool.class.php");
	require_once("SchoolYear.class.php");

	class SchoolYearTool
	{
	
		function GetAllSchoolYears()
		{
			dprint( "GetAllSchoolYears() Start." );
		
			try
			{
				$db = new DatabaseTool();

				$query = 'SELECT schoolyearid,schoolyearstart,schoolyearname FROM schoolyears';
				$mysqli = $db->Connect();
				$stmt = $mysqli->prepare($query);
				$results = $db->Execute($stmt);
			
				$schoolyears = array();
				foreach( $results as $row )
				{
					$schoolyear = new SchoolYear();
					
					$schoolyear->schoolyearid 	= $row['schoolyearid'];
					$schoolyear->schoolyearstart = $row['schoolyearstart'];
					$schoolyear->schoolyearname = $row['schoolyearname'];
				
					$schoolyears[] = $schoolyear;
				}
				
				$db->Close($mysqli, $stmt);
			}
			catch (Exception $e)
			{
				dprint( "Caught exception: " . $e->getMessage() );
			}
			
			dprint("GetAllSchoolYears() Done.");
		
			return $schoolyears;
		}
	}

?>