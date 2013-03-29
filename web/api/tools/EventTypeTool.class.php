<?php

	require_once("DatabaseTool.class.php");
	require_once("EventType.class.php");

	class EventTypeTool
	{
		function GetAllEventTypes()
		{
			dprint( "GetAllEventTypes() Start." );
		
			try
			{
				$db = new DatabaseTool();

				$query = 'SELECT eventtypeid,eventtypename,weaponrelated FROM eventtypes';
				$mysqli = $db->Connect();
				$stmt = $mysqli->prepare($query);
				$results = $db->Execute($stmt);
			
				$eventtypes = array();
				foreach( $results as $row )
				{
					$eventtype = new EventType();
					
					$eventtype->eventtypeid 	= $row['eventtypeid'];
					$eventtype->eventtypename = $row['eventtypename'];
					$eventtype->weaponrelated = $row['weaponrelated'];
				
					$eventtypes[] = $eventtype;
				}
				
				$db->Close($mysqli, $stmt);
			}
			catch (Exception $e)
			{
				dprint( "Caught exception: " . $e->getMessage() );
			}
			
			dprint("GetAllEventTypes() Done.");
		
			return $eventtypes;
		}
	}
	
?>