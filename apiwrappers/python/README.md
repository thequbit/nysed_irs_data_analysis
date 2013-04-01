nysed_irs_data_analysis
=======================

This is a place for very simple python wrappers to the web api's to allow you to pull data directly into your python program without having to interface with any messy CSV files.

GET Library
-----------

The get library is pretty simple.  It allows you to get data from the database that helps to describe the Violent and Disruptive Incidents, but not the incidents them selves.  This includes:

**Event Types**
- eg: Robery, Arson, Drug Possession, etc.
- api call: get_incidenttypes()

code:

	from getapi import get
	
	api = get()
	incidenttypes = api.get_incidenttypes()
	
	for incidenttype in incidenttypes:
        incidentid,incidentname,weaponrelated = incidenttype


**School Types**
- eg: Charter School, Public School, etc.
- api call: get_schooltypes()

code:

	from getapi import get
	
	api = get()
	schooltypes = api.get_schooltypes()
	
	for schooltype in schooltypes:
        schooltypeid,schooltypename = schooltype


**Grade Organizations**
- eg: Elementary School, Middle School, etc
- api call: get_gradeorganizations()

code:

	from getapi import get
	
	api = get()
	gradeorganizations = api.get_gradeorganizations()
	
	for gradeorganization in gradeorganizations:
        gradeorganizationid,gradeorganizationname = gradeorganization


**Need/Resource Category**
- eg: Average Needs, Low Needs, etc
- api call: get_needresourcecategories()

code:

	from getapi import get
	
	api = get()
	needresourcecategories = api.get_needresourcecategories()
	
	for needresourcecategory in needresourcecategories:
        needresourcecategoryid,needresourcecategoryname = needresourcecategory


**School Years in the Database**
- eg: 2010-2011, 2009-2010, etc
- api call: get_schoolyears()

code:

	from getapi import get
	
	api = get()
	needresourcecategories = api.get_schoolyears()
	
	for schoolyear in schoolyears:
        schoolyearid,schoolyearname = schoolyear
		

**Counties in NY**
- eg: NIAGARA, SENECA, etc
- api call: get_counties()

code:

	from getapi import get
	
	api = get()
	needresourcecategories = api.get_counties()
	
	for county in counties:
        countyid,countyname,geodata = county
		

**School Districts**
- eg: Hendrick Hudson Central School District, Hornell City School District, etc
- api call: get_districts()

code:

	from getapi import get
	
	api = get()
	needresourcecategories = api.get_districts()
	
	for district in districts:
        districtid,districtname,countyid = district


**Schools**
- eg: Attica Elementary School, Walter Panas High School, etc
- api call: get_schools()
- Note: This API call puts a lot of strain on the server, please use it sparingly (ie. call it once and create a local dictionary at the beginning of your script.  Thanks!)

code:

	from getapi import get
	
	api = get()
	needresourcecategories = api.get_schools()
	
	for school in schools:
        schoolid,schoolname,bedscode,enrollment,county,district,gradeorganization,needresourcecategory,schooltype = school

