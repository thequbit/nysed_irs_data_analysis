<?php

	require_once("DatabaseTool.class.php");
	require_once("GradeOrganization.class.php");

	class GradeOrganizationTool
	{
		function GetAllGradeOrganizations()
		{
			dprint( "GetAllGradeOrganizations() Start." );
		
			try
			{
				$db = new DatabaseTool();

				$query = 'SELECT gradeorganizationid,gradeorganizationname FROM gradeorganizations';
				$mysqli = $db->Connect();
				$stmt = $mysqli->prepare($query);
				$results = $db->Execute($stmt);
			
				$gradeorganizations = array();
				foreach( $results as $row )
				{
					$gradeorganization = new GradeOrganization();
					
					$gradeorganization->gradeorganizationid 	= $row['gradeorganizationid'];
					$gradeorganization->gradeorganizationname = $row['gradeorganizationname'];
				
					$gradeorganizations[] = $gradeorganization;
				}
				
				$db->Close($mysqli, $stmt);
			}
			catch (Exception $e)
			{
				dprint( "Caught exception: " . $e->getMessage() );
			}
			
			dprint("GetAllGradeOrganizations() Done.");
		
			return $gradeorganizations;
		}
	}

?>