import urllib
import json

class get:

	__baseurl__ = "http://mycodespace.net/projects/nysed_irs/api/"

	def __get_json__(self,what):

		url = "{0}get.php?what={1}".format(self.__baseurl__,what)
                rawobject = json.load(urllib.urlopen(url))

                apiversion = rawobject["apiversion"]
                rettype = rawobject["type"]
                errorcode = rawobject["errorcode"]
                errortext = rawobject["errortext"]
                results = rawobject["results"]

		return results

	def get_counties(self):

		results = self.__get_json__("county")
		
		retlist = []
                for result in results:

			geo = result["geometry"]
                        name = result["countyname"]
                        _id = result["countyid"]

                        item = (_id,name,geo)
                        retlist.append(item)

                return retlist

	def get_districts(self):

		results = self.__get_json__("district")

		retlist = []
                for result in results:

                        countyid = result["countyid"]
			name = result["districtname"]
                        _id = result["districtid"]

                        item = (_id,name,countyid)
                        retlist.append(item)

                return retlist

	def get_gradeorganizations(self):

                results = self.__get_json__("gradeorganization")

                retlist = []
                for result in results:

                        name = result["gradeorganizationname"]
                        _id = result["gradeorganizationid"]

                        item = (_id,name)
                        retlist.append(item)

                return retlist

	def get_needresourcecategories(self):

                results = self.__get_json__("needresourcecategory")

                retlist = []
                for result in results:

                        name = result["needresourcecategoryname"]
                        _id = result["needresourcecategoryid"]

                        item = (_id,name)
                        retlist.append(item)

                return retlist

	def get_schooltypes(self):

                results = self.__get_json__("schooltype")

                retlist = []
                for result in results:

                        name = result["schooltypename"]
                        _id = result["schooltypeid"]

                        item = (_id,name)
                        retlist.append(item)

                return retlist

	def get_incidenttypes(self):

                results = self.__get_json__("incidenttype")

                retlist = []
                for result in results:

			weaponrelated = result["weaponrelated"]
                        name = result["incidenttypename"]
                        _id = result["incidenttypeid"]

                        item = (_id,name,weaponrelated)
                        retlist.append(item)

                return retlist

	def get_schoolyears(self):

                results = self.__get_json__("schoolyear")

                retlist = []
                for result in results:

                        startyear = result["schoolyearstart"]
                        name = result["schoolyearname"]
                        _id = result["schoolyearid"]

                        item = (_id,startyear,name)
                        retlist.append(item)

                return retlist

	def get_schools(self):

                results = self.__get_json__("school")

                retlist = []
                for result in results:

                        schoolid = result["schoolid"]
			schoolname = result["schoolname"]
			bedscode = result["bedscode"]
			enrollment = result["enrollment"]
			county = result["county"]
			district = result["district"]
			gradeorganization = result["gradeorganization"]
			needresourcecategory = result["needresourcecategory"]
			schooltype = result["schooltype"]

                        item = (schoolid,schoolname,bedscode,enrollment,county,district,gradeorganization,needresourcecategory,schooltype)
                        retlist.append(item)

                return retlist

