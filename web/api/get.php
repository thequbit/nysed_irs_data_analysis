<?php

	$apiversion = "0.1";

	require_once("./tools/CountyTool.class.php");
	require_once("./tools/County.class.php");

	require_once("./tools/DistrictTool.class.php");
	require_once("./tools/District.class.php");

	require_once("./tools/EventTypeTool.class.php");
	require_once("./tools/EventType.class.php");

	require_once("./tools/GradeOrganizationTool.class.php");
	require_once("./tools/GradeOrganization.class.php");

	require_once("./tools/NeedResourceCategoryTool.class.php");
	require_once("./tools/NeedResourceCategory.class.php");

	require_once("./tools/SchoolTypeTool.class.php");
	require_once("./tools/SchoolType.class.php");

	require_once("./tools/SchoolTool.class.php");
	require_once("./tools/SchoolHybrid.class.php");
	
	require_once("./tools/SchoolYearTool.class.php");
	require_once("./tools/SchoolYear.class.php");

	// pull what we are getting from the POST
	$what = $_GET['what'];

	// default error code set to success
	$errorcode = 0;
	$errortext = "Successful.";

	// get the array of what the user wanted
	switch($what)
	{
		case "county":
			$type = "Counties";
			$tool = new CountyTool();
			$result = $tool->GetAllCounties();
			break;
			
		case "district":
			$type = "Districts";
			$tool = new DistrictTool();
			$result = $tool->GetAllDistricts();
			break;
			
		case "eventtype":
			$type = "Event Types";
			$tool = new EventTypeTool();
			$result = $tool->GetAllEventTypes();
			break;
			
		case "gradeorganization":
			$type = "Grade Organizations";
			$tool = new GradeOrganizationTool();
			$result = $tool->GetAllGradeOrganizations();
			break;
			
		case "needresourcecategory":
			$type = "Need Resource Category";
			$tool = new NeedResourceCategoryTool();
			$result = $tool->GetAllNeedResourceCategories();
			break;
			
		case "schooltype":
			$type = "School Type";
			$tool = new SchoolTypeTool();
			$result = $tool->GetAllSchoolTypes();
			break;
		
		case "schoolyear":
			$type = "School Years Available";
			$tool = new SchoolYearTool();
			$result = $tool->GetAllSchoolYears();
			break;
		
		case "school":
			$type = "School";
			$tool = new SchoolTool();
			$result = $tool->GetAllHybridSchools();
			break;
			
		case "":
		default:
			$type = "Invalid Type";
			$errorcode = 1;
			$errortext = "Invalid 'what' Input.";
			break;
	}
	
	// json-a-fy the responce ... 
	$jsonResult = json_encode($result);
	
	// ... and send it
	echo '{"apiversion":"' . $apiversion . '","type":"' . $type . '","errorcode":"' . $errorcode . '","errortext":"' . $errortext . '","results":' . $jsonResult . '}';

?>