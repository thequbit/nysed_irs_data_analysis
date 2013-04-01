<?php

	$apiversion = "0.1";

	require_once("./tools/EventTool.class.php");
	
	$action = $_GET["action"];

	$errorcode = 0;
	$errortext = "Successful";

	switch($action)
	{
		case "byschoolid":
			$type = "Events By School ID";
			$id = $_GET["schoolid"];
			if( $id != "" && is_numeric($id) )
			{
				$tool = new EventTool();
				$result = $tool->GetEventCountsBySchoolId($id);
			}
			else
			{
				$errorcode = 2;
				$errortext = "Invalid Secondary Input.";
				$result = array();
			}
			break;
		
		case "byschoolname":
			$type = "Events By School Name";
			$name = $_GET["schoolname"];
			if( $name != "" )
			{
				$tool = new EventTool();
				$result = $tool->GetEventCountsBySchoolName($name);
			}
			else
			{
				$errorcode = 2;
				$errortext = "Invalid Secondary Input.";
				$result = array();
			}
			break;
		
		case "":
		default:
			// invalid
			$type = "Invalid Type";
			$errorcode = 1;
			$errortext = "Invalid Input.";
			break;
	}

	// json-a-fy the responce ... 
	$jsonResult = json_encode($result);
	
	// ... and send it
	echo '{"apiversion":"' . $apiversion . '","type":"' . $type . '","errorcode":"' . $errorcode . '","errortext":"' . $errortext . '","results":' . $jsonResult . '}';

?>