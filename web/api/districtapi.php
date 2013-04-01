<?php

	$apiversion = "0.1";

	require_once("./tools/TimeTool.class.php");

	require_once("./tools/DistrictTool.class.php");
	require_once("./tools/District.class.php");
	
	$action = $_GET['action'];

	// default error code set to success
	$errorcode = 0;
	$errortext = "Successful.";

	$t = new TimeTool();
	$t->Mark();
	
	switch($action)
	{
		case "getall":
			$type = "Get All District";
			$tool = new DistrictTool();
			$result = $tool->GetAllDistricts();
			break;
			
		case "schoolcount":
			$type = "Get School Count within District";
			$id = $_GET["districtid"];
			if( $id != "" && is_numeric($id) )
			{
				$tool = new DistrictTool();
				$result = $tool->GetSchoolCount($id);
			}
			else
			{
				$errorcode = 2;
				$errortext = "Invalid DistrictID Input.";
				$result = array();
			}
			break;
			
		/*
		case "incidentcount":
			$type = "Get Total Incident Count For District";
			$id = $_GET["districtid"];
			if( $id != "" && is_numeric($id) )
			{
				$tool = new DistrictTool();
				$result = $tool->GetIncidentCount();
			}
			else
			{
				$errorcode = 2;
				$errortext = "Invalid DistrictID Input.";
				$result = array();
			}
			break;
		*/
		
		case "incidentcounts":
			$type = "Get District Event Counts";
			$id = $_GET["districtid"];
			if( $id != "" && is_numeric($id) )
			{
				$tool = new DistrictTool();
				$result = $tool->GetIncidentCounts($id);
			}
			else
			{
				$errorcode = 2;
				$errortext = "Invalid District ID Input.";
				$result = array();
			}
			break;
			
		case "":
		default:
			$type = "Invalid Action";
			$errorcode = 1;
			$errortext = "Invalid 'action' Input.";
			break;
	}

	$t->Mark();
	$getTime = $t->TimeTaken();
	
	// json-a-fy the results
	$jsonResult = json_encode($result);
	
	// ... and send it
	echo '{"apiversion":"' . $apiversion . '","querytime":"' . $getTime . '","type":"' . $type . '","errorcode":"' . $errorcode . '","errortext":"' . $errortext . '","results":' . $jsonResult . '}';


?>