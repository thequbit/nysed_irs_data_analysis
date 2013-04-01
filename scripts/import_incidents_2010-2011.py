import sys

import csv

from nysed_irs_db import dbhelper

def main(argv):

	if len(argv) != 4:
		print "Usage:\n\t\t{0} <file.csv> <startyear> <schoolyearname>".format(argv[0])
		return

	print "Application Start."

	csvfile = open(argv[1],"r")

	lines = csv.reader(csvfile,skipinitialspace=True)

	db = dbhelper()

	# create a new school year if it doesn't already exists, and then get the id for use later
	startyear = argv[2]
	schoolyearname = argv[3]
	if db.check_schoolyear_exists(startyear) == False:
		db.create_schoolyear(startyear,schoolyearname)
	schoolyearid,_start,_name = db.get_schoolyear_by_startyear(startyear)


	rowcount = 0
	startcolumn = 8

	for cells in lines:

		if rowcount < 4:

                        print "Ignoring line row."

                else:

			_schoolname = cells[2]
			_bedscode = cells[3]

			#print "School = {0}".format(_schoolname)

			if db.check_school_exists(_schoolname, _bedscode):

				# get school name
				schoolid,schoolname,bedscode,enrollment,countyid,districtid,gradeorganizationid,needresourcecategoryid,schooltypeid = db.get_school_by_name(_schoolname)

				# get all of the incidentss in the correct order from the db
				incidentstypes = db.get_all_incidentstypes()

				#print "Processing {0} incidentstypes ...".format(len(incidentstypes))

				# start at our column offset
				ccount = startcolumn

				# add all of the counts with their respective incidentstypes
				for i in range(0, len(incidentstypes)):

					# split tuple
					incidentstypeid,incidentstypename,weaponsrelated = incidentstypes[i]

					#print "\tCreating incidents(s) for incidents type '{0}'".format(incidentstypename)

					# if weapons related, we need to add the next two columns, else just the 1
					if weaponsrelated == 1:

						#print "\tSetting Value '{0}' for weapon involved incidents type '{1}'".format(cells[ccount],incidentstypename)

						# add with the weapon 
						db.create_incidents(cells[ccount], schoolyearid, 1, incidentstypeid, schoolid)
						# inc to next cell
						ccount += 1

						#print "\tSetting Value '{0}' for no weapon involved incidents type '{1}'".format(cells[ccount],incidentstypename)

						# add without the weapon
						db.create_incidents(cells[ccount], schoolyearid, 0, incidentstypeid, schoolid)
					else:

						#print "\tSetting Value '{0}' for weapon-independant incidents type '{1}'".format(cells[ccount],incidentstypename)

						# add just without the weapon
						db.create_incidents(cells[ccount], schoolyearid, 0, incidentstypeid, schoolid)

					# inc to next cell
					ccount += 1

				#print "Row Proccessed."

			else:
			
				print "ERROR: School did not exists within database, possible database corruption."

				print "\nSchool Name: \n\t'{0}'\nBEDS Code:\n\t'{1}'".format(_schoolname,_bedscode)

				break
			

		rowcount += 1

		if rowcount % 100 == 0:
			print "Row {0} Processed.".format(rowcount)


	print "Application End."

if __name__ == '__main__': sys.exit(main(sys.argv))
