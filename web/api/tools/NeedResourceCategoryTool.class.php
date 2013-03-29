<?php

	require_once("DatabaseTool.class.php");
	require_once("NeedResourceCategory.class.php");

	class NeedResourceCategoryTool
	{
		function GetAllNeedResourceCategories()
		{
			dprint( "GetAllNeedResourceCategories() Start." );
		
			try
			{
				$db = new DatabaseTool();

				$query = 'SELECT needresourcecategoryid,needresourcecategoryname FROM needresourcecategories';
				$mysqli = $db->Connect();
				$stmt = $mysqli->prepare($query);
				$results = $db->Execute($stmt);
			
				$needresourcecategories = array();
				foreach( $results as $row )
				{
					$needresourcecategory = new NeedResourceCategory();
					
					$needresourcecategory->needresourcecategoryid 	= $row['needresourcecategoryid'];
					$needresourcecategory->needresourcecategoryname = $row['needresourcecategoryname'];
				
					$needresourcecategories[] = $needresourcecategory;
				}
				
				$db->Close($mysqli, $stmt);
			}
			catch (Exception $e)
			{
				dprint( "Caught exception: " . $e->getMessage() );
			}
			
			dprint("GetAllNeedResourceCategories() Done.");
		
			return $needresourcecategories;
		}
	}

?>