<?php

	require_once("DatabaseTool.class.php");
	require_once("EventHybrid.class.php");

	class EventTool
	{
		function GetEventCountsBySchoolId($schoolid)
		{
			dprint( "GetEventCountsBySchoolId() Start." );
			
			try
			{
				$db = new DatabaseTool();

				$query = 'SELECT ';
				$query = $query . 'events.eventid as eventid, events.eventcount as eventcount, eventtypes.eventtypename as eventname, events.withweapon as withweapon, schoolyears.schoolyearname as schoolyear, schools.schoolname as schoolname ';
				$query = $query . 'FROM events ';
				$query = $query . 'inner join eventtypes on events.eventtypeid = eventtypes.eventtypeid ';
				$query = $query . 'inner join schools on events.schoolid = schools.schoolid ';
				$query = $query . 'inner join schoolyears on events.schoolyearid = schoolyears.schoolyearid ';
				$query = $query . 'WHERE events.schoolid = ?';

				$mysqli = $db->Connect();
				$stmt = $mysqli->prepare($query);
				// bind school id to query before execution
				$stmt->bind_param("s",$schoolid);
				$results = $db->Execute($stmt);
			
				$events = array();
				foreach( $results as $row )
				{
					$event = new EventHybrid();
				
					$event->eventid		= $row['eventid'];
					$event->eventcount	= $row['eventcount'];
					$event->eventname	= $row['eventname'];
					$event->withweapon	= $row['withweapon'];
					$event->schoolyear	= $row['schoolyear'];
					$event->schoolname	= $row['schoolname'];
				
					$events[] = $event;
				}
				
				$db->Close($mysqli, $stmt);
			}
			catch (Exception $e)
			{
				dprint( "Caught exception: " . $e->getMessage() );
			}
			
			dprint("GetEventCountsBySchoolId() Done.");
		
			return $events;
		}
		
		function GetEventCountsBySchoolName($schoolname)
		{
			dprint( "GetEventCountsBySchoolId() Start." );
			
			try
			{
				$db = new DatabaseTool();

				$query = 'SELECT ';
				$query = $query . 'events.eventid as eventid, events.eventcount as eventcount, eventtypes.eventtypename as eventname, events.withweapon as withweapon, schoolyears.schoolyearname as schoolyear, schools.schoolname as schoolname ';
				$query = $query . 'FROM events ';
				$query = $query . 'inner join eventtypes on events.eventtypeid = eventtypes.eventtypeid ';
				$query = $query . 'inner join schools on events.schoolid = schools.schoolid ';
				$query = $query . 'inner join schoolyears on events.schoolyearid = schoolyears.schoolyearid ';
				$query = $query . 'WHERE schools.schoolname = ?';

				$mysqli = $db->Connect();
				$stmt = $mysqli->prepare($query);
				// bind school id to query before execution
				$stmt->bind_param("s",$schoolname);
				$results = $db->Execute($stmt);
			
				$events = array();
				foreach( $results as $row )
				{
					$event = new EventHybrid();
				
					$event->eventid		= $row['eventid'];
					$event->eventcount	= $row['eventcount'];
					$event->eventname	= $row['eventname'];
					$event->withweapon	= $row['withweapon'];
					$event->schoolyear	= $row['schoolyear'];
					$event->schoolname	= $row['schoolname'];
				
					$events[] = $event;
				}
				
				$db->Close($mysqli, $stmt);
			}
			catch (Exception $e)
			{
				dprint( "Caught exception: " . $e->getMessage() );
			}
			
			dprint("GetEventCountsBySchoolId() Done.");
		
			return $events;
		}
	}

?>