import sys

import csv

from nysed_irs_db import dbhelper

def main(argv):

	if len(argv) != 2:
		print "Usage:\n\t\t{0} <file.csv>".format(argv[0])
		return

	print "Application Start."

	csvfile = open(argv[1],"r")

	lines = csv.reader(csvfile,skipinitialspace=True)

	db = dbhelper()

	rowcount = 0
	startcolumn = 8

	schoolyear = 2010

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

				# get all of the events in the correct order from the db
				eventtypes = db.get_all_eventtypes()

				#print "Processing {0} eventtypes ...".format(len(eventtypes))

				# start at our column offset
				ccount = startcolumn

				# add all of the counts with their respective eventtypes
				for i in range(0, len(eventtypes)):

					# split tuple
					eventtypeid,eventtypename,weaponsrelated = eventtypes[i]

					#print "\tCreating event(s) for event type '{0}'".format(eventtypename)

					# if weapons related, we need to add the next two columns, else just the 1
					if weaponsrelated == 1:

						#print "\tSetting Value '{0}' for weapon involved event type '{1}'".format(cells[ccount],eventtypename)

						# add with the weapon 
						db.create_event(cells[ccount], schoolyear, 1, eventtypeid, schoolid)
						# inc to next cell
						ccount += 1

						#print "\tSetting Value '{0}' for no weapon involved event type '{1}'".format(cells[ccount],eventtypename)

						# add without the weapon
						db.create_event(cells[ccount], schoolyear, 0, eventtypeid, schoolid)
					else:

						#print "\tSetting Value '{0}' for weapon-independant event type '{1}'".format(cells[ccount],eventtypename)

						# add just without the weapon
						db.create_event(cells[ccount], schoolyear, 0, eventtypeid, schoolid)

					# inc to next cell
					ccount += 1

				#print "Row Proccessed."

			else:
			
				print "ERROR: School did not exists within database, possible database corruption."

				break
			

		rowcount += 1

		if rowcount % 100 == 0:
			print "Row {0} Processed.".format(rowcount)


	print "Application End."

if __name__ == '__main__': sys.exit(main(sys.argv))
