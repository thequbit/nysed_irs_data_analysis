nysed_irs_data_analysis
=======================

**./api/get.php?what=value**

This is the simplest of the API's that allows for a simple query of what exists within various tables within the database.  The API returns an apiversion, type, errorcode, errortext, and results secontion in the JSON object reguardless of success.  Decode the errorcode field to deturmine success.

**errorcode decode:**
- 0: successful
- 1: invalid input, not successful

Note: there is some semi-useful text returned in the errortext field to help you decode what happened as well.

The API is used with a single propery passed in via the URL called 'what'.  Please note that any property returned as an ID is used internally in the database and is provided as an easy way for you to keep track of the data you are using.  It is NOT in anyway used by the governing bodies this data is supplied from.  If you reference a middle schol by it's schoolid, they will not know what you are talking about, and you will look silly ... and you should feel silly.

Here is the available 'what' values:

**County**
- what value: county
- example: ./api/get.php?what=county
- returns:

json:
	
	{
		"apiversion":"0.1",
		"type":"Counties",
		"errorcode":"0",
		"errortext":"Successful.",
		"results":
		[
			{
				"countyid":115,
				"countyname":"ALBANY",
				"geometry":" ... removed for example ... "
			},
			{
				"countyid":116,
				"countyname":"ALLEGANY",
				"geometry":" ... removed for example ... "
			},
			
			... etc
		]
	}
	
**District**
- what value: district
- example: ./api/get.php?what=district
- returns:

json:
	
	{
		"apiversion":"0.1",
		"type":"Districts",
		"errorcode":"0",
		"errortext":"Successful.",
		"results":
		[
			{
				"districtid":1394,
				"districtname":"Albany City School District"
			},
			{
				"districtid":1395,
				"districtname":"Berne-Knox-Westerlo Central School District"
			},
			
			... etc
		]
	}
	
**Event Type**
- what value: eventtype
- example: ./api/get.php?what=eventtype
- returns:

json:
	
	{
		"apiversion":"0.1",
		"type":"Event Types",
		"errorcode":"0",
		"errortext":"Successful.",
		"results":
		[
			{
				"eventtypeid":44,
				"eventtypename":"Homicide",
				"weaponrelated":1
			},
			{
				"eventtypeid":45,
				"eventtypename":"Forcible_Sex_Offenses",
				"weaponrelated":1
			},
	
			... etc
			
		]
	}
	
**Grade Organization**
- what value: gradeorganization
- example: ./api/get.php?what=gradeorganization
- returns:

json:
	
	{
		"apiversion":"0.1",
		"type":"Grade Organizations",
		"errorcode":"0",
		"errortext":"Successful.",
		"results":
		[
			{
				"gradeorganizationid":15,
				"gradeorganizationname":"Middle School"
			},
			{
				"gradeorganizationid":16,
				"gradeorganizationname":"Elementary"
			},
	
			... etc
		]
	}
	
**Needs Resource Category**
- what value: needresourcecategory
- example: ./api/get.php?what=needresourcecategory
- returns:
	
json:

	{
		"apiversion":"0.1",
		"type":"Need Resource Category",
		"errorcode":"0",
		"errortext":"Successful.",
		"results":
		[
			{
				"needresourcecategoryid":15,
				"needresourcecategoryname":"Charter School"
			},
			{
				"needresourcecategoryid":16,
				"needresourcecategoryname":"Urban\/Suburban High Needs"
			},
			
			... etc
			
		]
	
	}

**School Type**
- what value: schooltype
- example: ./api/get.php?what=schooltype
- returns:
	
json:

	{
		"apiversion":"0.1",
		"type":"School Type",
		"errorcode":"0",
		"errortext":"Successful.",
		"results":
		[
			{
				"schooltypeid":3,
				"schooltypename":"Charter School"
			},
			{
				"schooltypeid":4,
				"schooltypename":"Public"
			}
		]
	}




	

	