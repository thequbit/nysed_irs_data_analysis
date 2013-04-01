import sys

from nysed_irs_db import dbhelper

import csv

def add_school(name, bedscode, enrollment, countyid, districtid, gradeorganizationid, needresourcecategoryid, schooltypeid):

        nysed = dbhelper()

        exists = nysed.check_school_exists(name, bedscode)

        if exists == False:

                nysed.create_school(name, bedscode, enrollment, countyid, districtid, gradeorganizationid, needresourcecategoryid, schooltypeid)

                #print "\tAdded School '{0}' Successfully.".format(name)

        ret = nysed.get_school_by_name(name)

        return ret


def add_schooltype(name):

        nysed = dbhelper()

        exists = nysed.check_schooltype_exists(name)

        if exists == False:

                nysed.create_schooltype(name)

                #print "\tAdded School Type '{0}' Successfully.".format(name)

        ret = nysed.get_schooltype_by_name(name)

        return ret

def add_needresourcecategory(name):

        nysed = dbhelper()

        exists = nysed.check_needresourcecategory_exists(name)

        if exists == False:

                nysed.create_needresourcecategory(name)

                #print "\tAdded Need/Resource Category '{0}' Successfully.".format(name)

        ret = nysed.get_needresourcecategory_by_name(name)

        return ret

def add_gradeorganization(name):

        nysed = dbhelper()

        exists = nysed.check_gradeorganization_exists(name)

        if exists == False:

                nysed.create_gradeorganization(name)

                #print "\tAdded Grade Organization '{0}' Successfully.".format(name)

        ret = nysed.get_gradeorganization_by_name(name)

        return ret

def add_district(name,countyid):

	nysed = dbhelper()

        exists = nysed.check_district_exists(name)

        if exists == False:

                nysed.create_district(name,countyid)

                #print "\tAdded District '{0}' Successfully.".format(name)

        ret = nysed.get_district_by_name(name)

        return ret

def add_county(name):

	nysed = dbhelper()

	exists = nysed.check_county_exists(name)

	if exists == False:

		nysed.create_county(name)

		#print "\tAdded County '{0}' Successfully.".format(name)
	
	ret = nysed.get_county_by_name(name)

	return ret

def main(argv):

	if len(argv) != 2:
		print "Usage:\n\t\timport_simplespy <file.csv>\n"
		return

	print "Application Start."

	print "Reading input file ..."

	# open the csv files
	csvfile = open(argv[1],"r")

	#filedata = csvfile.read()

	print "Breaking file into rows ..."

	# break the file into rows
	#lines = filedata.split("\n"); # can't do this because they HAVE FREAKIN COMMA'S IN THE SCHOOL NAMES, OMG ...

	# pull lines from csv file
	lines = csv.reader(csvfile,skipinitialspace=True)

	# remove the first 4 rows, as these are not data
	#lines.remove(lines[0])
	#lines.remove(lines[1])
	#lines.remove(lines[2])
	#lines.remove(lines[3])

	#print "Iterating Through {0} Rows ...".format(len(lines))

	rowcount = 0

	helper = dbhelper()

	# see if the unknown category for these exists, and if it doesn't then create it
	if helper.check_gradeorganization_exists("UNKNOWN") == False:
		helper.create_gradeorganization("UNKNOWN")
	if helper.check_needresourcecategory_exists("UNKNOWN") == False:
		helper.create_needresourcecategory("UNKNOWN")

	# pull the index of the unknowns for these two.  If the school is already known, these are ignored
	gradeorganizationid,_name = helper.get_gradeorganization_by_name("UNKNOWN")
	needresourcecategoryid, _name = helper.get_needresourcecategory_by_name("UNKNOWN")

	for cells in lines:

		if rowcount < 3:

			print "Ignoring line row."

		else:

			# split on commas to get each individual cell
			#cells = line.split(",")

			#print "Procesing cell data ..."

			# cell decode
			#
			# data will only be valid for 2010 - 2011
			#
			
			#print "Row {0}: {1},{2},{3},{4},{5},{6},{7},{8}".format(rowcount,cells[0],cells[1],cells[2],cells[3],cells[4],cells[5],cells[6],cells[7])

			county = cells[0].replace('"','')
			district = cells[2].replace('"','')
			schoolname = cells[3].replace('"','')
			bedscode = cells[1].replace('"','')
			#gradeorg = cells[4].replace('"','')
			#resoucecat = cells[5].replace('"','')
			schooltype = cells[4].replace('"','')
			cell5 = cells[5].replace('"','')
			if cell5 != "":
				enrollment = long(float(cell5))
			else:
				enrollment = 0

			# add all the new data to the database
			countyid,_name,_geometry = add_county(county)
			districtid,_name,_countyid = add_district(district,countyid)
			#gradeorganizationid,_name = add_gradeorganization(gradeorg)
			#needresourcecategoryid,_name = add_needresourcecategory(resoucecat)
			schooltypeid,_name = add_schooltype(schooltype)

			# since county, gradeorg, or resourcecat aren't in the spreadsheet for this school year,
                        # we need to query them from 'future' years where the data is available
			
			# make the assumption the distrct exists since this file should have already gone
			# through import_simples_<schoolyear>.py
			
			# get district and make sure it exists
			#if helper.check_district_exists(district) == False:

			#	print "District '{0}' is unknown, ".format(district)

				#return

			if True:
				
				districtid,_districtname,countyid = helper.get_district_by_name(district)

				# check to see if the school exists
				if helper.check_school_exists(schoolname,bedscode) == False:
				
					print "New School Found, fudging grade organization and need/resource category"

				# set to invalid index's, if the school already exists these will be ignored
				#gradeorganizationid = invalidgradeorganizationindex;
				#needresourcecategoryid = 
		
				# add the school with the database data
				schoolid,_schoolname,_bedscode,_enrollment,_countyid,_districtid,_gradeorganizationid,_needresourcecategoryid,_schooltypeid = add_school(schoolname,bedscode, enrollment, countyid, districtid, gradeorganizationid, needresourcecategoryid, schooltypeid)

				#print "Added School: Name = {0}, ID = {1}".format(_schoolname,schoolid)

		if rowcount % 100 == 0:
			print "Row {0} Processed.".format(rowcount)

		rowcount += 1

	print "\n{0} Rows processed successfully.\n".format(rowcount)

	print "Application End."

if __name__ == '__main__': sys.exit(main(sys.argv))
