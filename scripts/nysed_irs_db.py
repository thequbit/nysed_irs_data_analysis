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

	def create_district(self, districtname):

                with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("INSERT INTO districts(districtname) VALUES(%s)", districtname)
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
                

	def create_school(self, schoolname, bedscode, enrollment, countyid, districtid, gradeorganizationid, needresourcecategoryid, schooltypeid):

                with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("INSERT INTO schools(schoolname, bedscode, enrollment, countyid, districtid, gradeorganizationid, needresourcecategoryid, schooltypeid) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)", (schoolname, bedscode, enrollment, countyid, districtid, gradeorganizationid, needresourcecategoryid, schooltypeid))
		        cur.close()
                


	def create_eventtype(self, eventtypename, withweapon, weaponrelated):

                with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("INSERT INTO eventtypes(eventtypename,withweapon,weaponrelated) VALUES(%s,%s,%s)", (eventtypename,int(withweapon),int(weaponrelated)))
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

	def check_eventtype_exists(self, eventtypename):

                with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("SELECT eventtypeid FROM eventtypes WHERE LOWER(eventtypename) = %s", eventtypename.lower())
                        if len(cur.fetchall()) == 0:
                                exists = False
                        else:
                                exists = True
		        cur.close()
                
                return exists

	

	###################################
	#
	# Get Functions
	#
	#

	def get_county_by_name(self, countyname):

                with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("SELECT countyid,countyname FROM counties WHERE LOWER(countyname) = %s", countyname.lower())
			row = cur.fetchone()
		        cur.close()
                
		countyid,countyname = row
		return (countyid, countyname)

	def get_district_by_name(self, districtname):

                with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("SELECT districtid,districtname FROM districts WHERE LOWER(districtname) = %s", districtname.lower())
                        row = cur.fetchone()
		        cur.close()
                
                districtid,districtname = row
                return (districtid, districtname)

	def get_eventtype_by_name(self, eventtypename):

                with self.__con:
                        cur = self.__con.cursor()
                        cur.execute("SELECT eventtypeid,eventtypename FROM eventtypes WHERE LOWER(eventtypename) = %s", eventtypename.lower())
                        row = cur.fetchone()
		        cur.close()
                
		eventtypeid,eventtypename = row
                return (eventtypeid, eventtypename)

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


