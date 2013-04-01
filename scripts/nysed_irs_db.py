import sys

import MySQLdb as mdb
import _mysql as mysql

class dbhelper:

	__dbhost = ""
	__dbname = ""
	__dbuser = ""
	__dbpass = ""

	__con = False

	def __init__(self):
		self.__load_credentials__()

	def __load_credentials__(self):
		
        	# read in credentials file
		lines = tuple(open('mysqlcreds.txt', 'r'))
	
		# set our local values
	        self.__dbhost = lines[0].strip()
		self.__dbname = lines[1].strip()
		self.__dbuser = lines[2].strip()
		self.__dbpass = lines[3].strip()

		self.__con = mdb.connect(host=self.__dbhost, user=self.__dbuser, passwd=self.__dbpass, db=self.__dbname)


	##############################
	#
	# Create Functions
	#
	#

	def create_county(self, countyname):

		with self.__con:
			cur = self.__con.cursor()
			cur.execute("INSERT INTO counties(countyname) VALUES(%s)", countyname)
			cur.close()

	def create_district(self, districtname, countyid):

                with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("INSERT INTO districts(districtname,countyid) VALUES(%s,%s)", (districtname, countyid))
			cur.close()

	def create_gradeorganization(self, gradeorganizationname):

                with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("INSERT INTO gradeorganizations(gradeorganizationname) VALUES(%s)", gradeorganizationname)
			cur.close()

	def create_needresourcecategory(self, needresourcecategoryname):

                with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("INSERT INTO needresourcecategories(needresourcecategoryname) VALUES(%s)", needresourcecategoryname)
			cur.close()
                

	def create_schooltype(self, schooltypename):

                with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("INSERT INTO schooltypes(schooltypename) VALUES(%s)", schooltypename)
		        cur.close()
                

	def create_schoolyear(self, schoolyearstart, schoolyearname):

		with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("INSERT INTO schoolyears(schoolyearstart,schoolyearname) VALUES(%s,%s)", (schoolyearstart,schoolyearname))
                        cur.close()


	def create_school(self, schoolname, bedscode, enrollment, countyid, districtid, gradeorganizationid, needresourcecategoryid, schooltypeid):

                with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("INSERT INTO schools(schoolname, bedscode, enrollment, countyid, districtid, gradeorganizationid, needresourcecategoryid, schooltypeid) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)", (schoolname, bedscode, enrollment, countyid, districtid, gradeorganizationid, needresourcecategoryid, schooltypeid))
		        cur.close()
                
	def create_incidenttype(self, incidenttypename, weaponrelated):

                with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("INSERT INTO incidenttypes(incidenttypename,weaponrelated) VALUES(%s,%s)", (incidenttypename,weaponrelated))
		        cur.close()
                
	
	def create_incident(self, incidentcount, schoolyearid, withweapon, incidenttypeid, schoolid):

		# sanitize inputs
		if incidentcount == "":
			incidentcount = 0

		with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("INSERT INTO vadirincidents(incidentcount,schoolyearid,withweapon,incidenttypeid,schoolid) VALUES(%s,%s,%s,%s,%s)", (incidentcount,schoolyearid,withweapon,incidenttypeid,schoolid) )
                        cur.close()



	##########################
	#
	# Check Functions

	#
	#

	def check_county_exists(self, countyname):

                with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("SELECT countyid FROM counties WHERE LOWER(countyname) = %s", countyname.lower())
                        if len(cur.fetchall()) == 0:
				exists = False
			else:
				exists = True
		        cur.close()
                
                return exists

	def check_district_exists(self, districtname):

                with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("SELECT districtid FROM districts WHERE LOWER(districtname) = %s", districtname.lower())
                        if len(cur.fetchall()) == 0:
                                exists = False
                        else:
                                exists = True
		        cur.close()
                
                return exists

	def check_gradeorganization_exists(self, gradeorganizationname):

                with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("SELECT gradeorganizationid FROM gradeorganizations WHERE LOWER(gradeorganizationname) = %s", gradeorganizationname.lower())
                        if len(cur.fetchall()) == 0:
                                exists = False
                        else:
                                exists = True
		        cur.close()
                
                return exists

	def check_needresourcecategory_exists(self, needresourcecategoryname):

                with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("SELECT needresourcecategoryid FROM needresourcecategories WHERE LOWER(needresourcecategoryname) = %s", needresourcecategoryname.lower())
                        if len(cur.fetchall()) == 0:
                                exists = False
                        else:
                                exists = True
		        cur.close()
                
                return exists

	def check_schooltype_exists(self, schooltypename):

                with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("SELECT schooltypeid FROM schooltypes WHERE LOWER(schooltypename) = %s", schooltypename.lower())
                        if len(cur.fetchall()) == 0:
                                exists = False
                        else:
                                exists = True
		        cur.close()
                
                return exists


	def check_schoolyear_exists(self, schoolyearstart):

		with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("SELECT schoolyearid FROM schoolyears WHERE schoolyearstart = %s", schoolyearstart.lower())
                        if len(cur.fetchall()) == 0:
                                exists = False
                        else:
                                exists = True
                        cur.close()

                return exists

	
	def check_school_exists(self, schoolname, bedscode):

                with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("SELECT schoolid FROM schools WHERE LOWER(schoolname) = %s AND LOWER(bedscode) = %s", (schoolname.lower(), bedscode.lower()))
                        if len(cur.fetchall()) == 0:
                                exists = False
                        else:
                                exists = True
		        cur.close()
                
                return exists

	def check_incidenttype_exists(self, incidenttypename):

                with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("SELECT incidenttypeid FROM incidenttypes WHERE LOWER(incidenttypename) = %s", incidenttypename.lower())
                        if len(cur.fetchall()) == 0:
                                exists = False
                        else:
                                exists = True
		        cur.close()
                
                return exists


	##################################
	#
	# Update Functions
	#
	#
	
	def update_county_geometry(self,countyid,geometry):

		with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("UPDATE counties SET geometry = %s WHERE countyid = %s", (geometry, countyid) )
                        cur.close()


	###################################
	#
	# Get Functions
	#
	#

	def get_county_by_name(self, countyname):

                with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("SELECT countyid,countyname,geometry FROM counties WHERE LOWER(countyname) = %s", countyname.lower())
			row = cur.fetchone()
		        cur.close()
                
		countyid,countyname,geometry = row
		return (countyid, countyname, geometry)

	def get_all_counties(self):

		with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("SELECT countyid,countyname,geometry FROM counties")
                        rows = cur.fetchall()
                        cur.close()

		counties = []
		for row in rows:
			counties.append(row)

                return counties

	def get_district_by_name(self, districtname):

                with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("SELECT districtid,districtname,countyid FROM districts WHERE LOWER(districtname) = %s", districtname.lower())
                        row = cur.fetchone()
		        cur.close()
               
		if row == None:
			print "OMG WTF"
 
                districtid,districtname,countyid = row
                return (districtid, districtname, countyid)

	def get_all_incidenttypes(self):

		with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("SELECT incidenttypeid,incidenttypename,weaponrelated FROM incidenttypes ORDER BY incidenttypeid") # this assumes they were loaded into the database the way they show up in the spreadsheet
                        rows = cur.fetchall()
                        cur.close()

		incidenttypes = []
		for row in rows:
			incidenttypes.append(row)

                return incidenttypes


	def get_incidenttype_by_name(self, incidenttypename):

                with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("SELECT incidenttypeid,incidenttypename,weaponsrelated FROM incidenttypes WHERE LOWER(incidenttypename) = %s", incidenttypename.lower())
                        row = cur.fetchone()
		        cur.close()
                
		incidenttypeidincndenttypename,weaponsrelated = row
                return (incidenttypeid, incndenttypename, weaponsrelated)

	def get_gradeorganization_by_name(self, gradeorganizationname):

                with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("SELECT gradeorganizationid,gradeorganizationname FROM gradeorganizations WHERE LOWER(gradeorganizationname) = %s", gradeorganizationname.lower())
                        row = cur.fetchone()
		        cur.close()
                
                gradeorganizationid,gradeorganizationname = row
                return (gradeorganizationid, gradeorganizationname)

	def get_needresourcecategory_by_name(self, needresourcecategoryname):

                with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("SELECT needresourcecategoryid,needresourcecategoryname FROM needresourcecategories WHERE LOWER(needresourcecategoryname) = %s", needresourcecategoryname.lower())
                        row = cur.fetchone()
		        cur.close()
                
                needresourcecategoryid,needresourcecategoryname = row
                return (needresourcecategoryid, needresourcecategoryname)

	def get_schoolyear_by_startyear(self, schoolyearstart):

                with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("SELECT schoolyearid,schoolyearstart,schoolyearname FROM schoolyears WHERE schoolyearstart = %s", schoolyearstart )
                        row = cur.fetchone()
                        cur.close()

                schoolyearid,schoolyearstart,schoolyearname = row
                return (schoolyearid, schoolyearstart, schoolyearname)


	def get_schoolyear_by_name(self, schoolyearname):

		with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("SELECT schoolyearid,schoolyearstart,schoolyearname FROM schoolyears WHERE LOWER(schoolyearname) = %s", schoolyearname.lower())
                        row = cur.fetchone()
                        cur.close()

		schoolyearid,schoolyearstart,schoolyearname = row
                return (schoolyearid, schoolyearstart, schoolyearname)

	def get_schooltype_by_name(self, schooltypename):

                with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("SELECT schooltypeid,schooltypename FROM schooltypes WHERE LOWER(schooltypename) = %s", schooltypename.lower())
                        row = cur.fetchone()
		        cur.close()
                
                schooltypeid,schooltypename = row
                return (schooltypeid, schooltypename)

	def get_school_by_name(self, schoolname):

                with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("SELECT schoolid,schoolname,bedscode,enrollment,countyid,districtid,gradeorganizationid,needresourcecategoryid,schooltypeid FROM schools WHERE LOWER(schoolname) = %s", schoolname.lower())
                        row = cur.fetchone()
		        cur.close()
                
                schoolid,schoolname,bedscode,enrollment,countyid,districtid,gradeorganizationid,needresourcecategoryid,schooltypeid = row
                return (schoolid,schoolname,bedscode,enrollment,countyid,districtid,gradeorganizationid,needresourcecategoryid,schooltypeid)


