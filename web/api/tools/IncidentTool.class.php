<?php

	require_once("DatabaseTool.class.php");
	require_once("IncidentHybrid.class.php");

	class IncidentTool
	{
		function GetIncidentCountsBySchoolId($schoolid)
		{
			dprint( "GetIncidentCountsBySchoolId() Start." );
			
			try
			{
				$db = new DatabaseTool();

				$query = 'SELECT ';
				$query = $query . 'incidents.incidentid as incidentid, incidents.incidentcount as incidentcount, incidenttypes.incidenttypename as incidentname, incidents.withweapon as withweapon, schoolyears.schoolyearname as schoolyear, schools.schoolname as schoolname ';
				$query = $query . 'FROM incidents ';
				$query = $query . 'inner join incidenttypes on incidents.incidenttypeid = incidenttypes.incidenttypeid ';
				$query = $query . 'inner join schools on incidents.schoolid = schools.schoolid ';
				$query = $query . 'inner join schoolyears on incidents.schoolyearid = schoolyears.schoolyearid ';
				$query = $query . 'WHERE incidents.schoolid = ?';

				$mysqli = $db->Connect();
				$stmt = $mysqli->prepare($query);
				// bind school id to query before execution
				$stmt->bind_param("s",$schoolid);
				$results = $db->Execute($stmt);
			
				$incidents = array();
				foreach( $results as $row )
				{
					$incident = new IncidentHybrid();
				
					$incident->incidentid		= $row['incidentid'];
					$incident->incidentcount	= $row['incidentcount'];
					$incident->incidentname	= $row['incidentname'];
					$incident->withweapon	= $row['withweapon'];
					$incident->schoolyear	= $row['schoolyear'];
					$incident->schoolname	= $row['schoolname'];
				
					$incidents[] = $incident;
				}
				
				$db->Close($mysqli, $stmt);
			}
			catch (Exception $e)
			{
				dprint( "Caught exception: " . $e->getMessage() );
			}
			
			dprint("GetIncidentCountsBySchoolId() Done.");
		
			return $incidents;
		}
		
		function GetIncidentCountsBySchoolName($schoolname)
		{
			dprint( "GetIncidentCountsBySchoolId() Start." );
			
			try
			{
				$db = new DatabaseTool();

				$query = 'SELECT ';
				$query = $query . 'incidents.incidentid as incidentid, incidents.incidentcount as incidentcount, incidenttypes.incidenttypename as incidentname, incidents.withweapon as withweapon, schoolyears.schoolyearname as schoolyear, schools.schoolname as schoolname ';
				$query = $query . 'FROM incidents ';
				$query = $query . 'inner join incidenttypes on incidents.incidenttypeid = incidenttypes.incidenttypeid ';
				$query = $query . 'inner join schools on incidents.schoolid = schools.schoolid ';
				$query = $query . 'inner join schoolyears on incidents.schoolyearid = schoolyears.schoolyearid ';
				$query = $query . 'WHERE schools.schoolname = ?';

				$mysqli = $db->Connect();
				$stmt = $mysqli->prepare($query);
				// bind school id to query before execution
				$stmt->bind_param("s",$schoolname);
				$results = $db->Execute($stmt);
			
				$incidents = array();
				foreach( $results as $row )
				{
					$incident = new IncidentHybrid();
				
					$incident->incidentid		= $row['incidentid'];
					$incident->incidentcount	= $row['incidentcount'];
					$incident->incidentname	= $row['incidentname'];
					$incident->withweapon	= $row['withweapon'];
					$incident->schoolyear	= $row['schoolyear'];
					$incident->schoolname	= $row['schoolname'];
				
					$incidents[] = $incident;
				}
				
				$db->Close($mysqli, $stmt);
			}
			catch (Exception $e)
			{
				dprint( "Caught exception: " . $e->getMessage() );
			}
			
			dprint("GetIncidentCountsBySchoolId() Done.");
		
			return $incidents;
		}
	}

?>