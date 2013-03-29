nysed_irs_data_analysis
=======================

This is a place for very simple python wrappers to the web api's to allow you to pull data directly into your python program without having to interface with any messy CSV files.

GET Library
-----------

The get library is pretty simple.  It allows you to get data from the database that helps to describe the Violent and Disruptive Incidents, but not the incidents them selves.  This includes:

**Event Types**
- eg: Robery, Arson, Drug Possession, etc.

**School Types**
- eg: Charter School, Public School, etc.

**Grade Organizations**
- eg: Elementary School, Middle School, etc

**Need/Resource Category**
- eg: Average Needs, Low Needs, etc

**School Years in the Database**
- eg: 2010-2011, 2009-2010, etc

**Counties in NY**
- eg: NIAGARA, SENECA, etc

**School Districts**
- eg: Hendrick Hudson Central School District, Hornell City School District, etc

**Schools**
- eg: Attica Elementary School, Walter Panas High School, etc
- Note: This API call puts a lot of strain on the server, please use it sparingly (ie. call it once and create a local dictionary at the beginning of your script.  Thanks!)

