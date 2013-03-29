<?php

	require_once("DatabaseTool.class.php");
	require_once("SchoolType.class.php");

	class SchoolTypeTool
	{
		function GetAllSchoolTypes()
		{
			dprint( "GetAllSchoolTypes() Start." );
		
			try
			{
				$db = new DatabaseTool();

				$query = 'SELECT schooltypeid,schooltypename FROM schooltypes';
				$mysqli = $db->Connect();
				$stmt = $mysqli->prepare($query);
				$results = $db->Execute($stmt);
			
				$schooltypes = array();
				foreach( $results as $row )
				{
					$schooltype = new SchoolType();
					
					$schooltype->schooltypeid 	= $row['schooltypeid'];
					$schooltype->schooltypename = $row['schooltypename'];
				
					$schooltypes[] = $schooltype;
				}
				
				$db->Close($mysqli, $stmt);
			}
			catch (Exception $e)
			{
				dprint( "Caught exception: " . $e->getMessage() );
			}
			
			dprint("GetAllSchoolTypes() Done.");
		
			return $schooltypes;
		}
	}

?>