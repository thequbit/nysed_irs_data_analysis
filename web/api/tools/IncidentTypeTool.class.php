<?php

	require_once("DatabaseTool.class.php");
	require_once("IncidentType.class.php");

	class IncidentTypeTool
	{
		function GetAllIncidentTypes()
		{
			dprint( "GetAllIncidentTypes() Start." );
		
			try
			{
				$db = new DatabaseTool();

				$query = 'SELECT incidenttypeid,incidenttypename,weaponrelated FROM incidenttypes';
				$mysqli = $db->Connect();
				$stmt = $mysqli->prepare($query);
				$results = $db->Execute($stmt);
			
				$incidenttypes = array();
				foreach( $results as $row )
				{
					$incidenttype = new IncidentType();
					
					$incidenttype->incidenttypeid 	= $row['incidenttypeid'];
					$incidenttype->incidenttypename = $row['incidenttypename'];
					$incidenttype->weaponrelated = $row['weaponrelated'];
				
					$incidenttypes[] = $incidenttype;
				}
				
				$db->Close($mysqli, $stmt);
			}
			catch (Exception $e)
			{
				dprint( "Caught exception: " . $e->getMessage() );
			}
			
			dprint("GetAllIncidentTypes() Done.");
		
			return $incidenttypes;
		}
	}
	
?>