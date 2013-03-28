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

	for cells in lines:

		if rowcount < 4:

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
			district = cells[1].replace('"','')
			schoolname = cells[2].replace('"','')
			bedscode = cells[3].replace('"','')
			gradeorg = cells[4].replace('"','')
			resoucecat = cells[5].replace('"','')
			schooltype = cells[6].replace('"','')
			cell7 = cells[7].replace('"','')
			if cell7 != "":
				enrollment = long(float(cell7))
			else:
				enrollment = 0

			# add all the new data to the database
			countyid,_name,_geometry = add_county(county)
			districtid,_name = add_district(district,countyid)
			gradeorganizationid,_name = add_gradeorganization(gradeorg)
			needresourcecategoryid,_name = add_needresourcecategory(resoucecat)
			schooltypeid,_name = add_schooltype(schooltype)

			# add the school with the database data
			schoolid,_schoolname,_bedscode,_enrollment,_dountyid,_districtid,_gradeorganizationid,_needresourcecategoryid,_schooltypeid = add_school(schoolname,bedscode, enrollment, countyid, districtid, gradeorganizationid, needresourcecategoryid, schooltypeid)

			#print "Added School: Name = {0}, ID = {1}".format(_schoolname,schoolid)

		if rowcount % 100 == 0:
			print "Row {0} Processed.".format(rowcount)

		rowcount += 1

	print "\n{0} Rows processed successfully.\n".format(rowcount)

	print "Application End."

if __name__ == '__main__': sys.exit(main(sys.argv))
