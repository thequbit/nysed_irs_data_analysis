<?php

	require_once("DatabaseTool.class.php");
	require_once("SchoolHybrid.class.php");

	class SchoolTool
	{
		function GetAllHybridSchools()
		{
			dprint( "GetAllHybridSchools() Start." );
		
			try
			{
				$db = new DatabaseTool();

				$query = 'select ';
				$query = $query . 'schools.schoolid, schools.schoolname, schools.bedscode, schools.enrollment, counties.countyname as county, districts.districtname as district, gradeorganizations.gradeorganizationname as gradeorganization, needresourcecategories.needresourcecategoryname as needresourcecategory, schooltypes.schooltypename as schooltype ';
				$query = $query . 'from schools ';
				$query = $query . 'inner join districts on districts.districtid = schools.districtid ';
				$query = $query . 'inner join counties on counties.countyid = districts.countyid ';
				$query = $query . 'inner join gradeorganizations on gradeorganizations.gradeorganizationid = schools.gradeorganizationid ';
				$query = $query . 'inner join needresourcecategories on needresourcecategories.needresourcecategoryid = schools.needresourcecategoryid ';
				$query = $query . 'inner join schooltypes on schooltypes.schooltypeid = schools.schooltypeid ';
				
				$mysqli = $db->Connect();
				$stmt = $mysqli->prepare($query);
				$results = $db->Execute($stmt);
			
				$schools = array();
				foreach( $results as $row )
				{
					$school = new SchoolHybrid();
					
					$school->schoolid 				= $row['schoolid'];
					$school->schoolname 			= $row['schoolname'];
					$school->bedscode 				= $row['bedscode'];
					$school->enrollment 			= $row['enrollment'];
					$school->county 				= $row['county'];
					$school->district 				= $row['district'];
					$school->gradeorganization 		= $row['gradeorganization'];
					$school->needresourcecategory 	= $row['needresourcecategory'];
					$school->schooltype 			= $row['schooltype'];
				
					$schools[] = $school;
				}
				
				$db->Close($mysqli, $stmt);
			}
			catch (Exception $e)
			{
				dprint( "Caught exception: " . $e->getMessage() );
			}
			
			dprint("GetAllSchools() Done.");
			
			return $schools;
		}
	}

?>