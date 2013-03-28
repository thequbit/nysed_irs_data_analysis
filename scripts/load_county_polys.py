import sys

import csv

from nysed_irs_db import dbhelper

def main(argv):

	if len(argv) != 2:
                print "Usage:\n\t\t{0} <poly_file.csv>".format(argv[0])
                return

        print "Application Start."

	print "Loading poly file ..."

	csvfile = open(argv[1],"r")

        lines = csv.reader(csvfile,skipinitialspace=True)

        db = dbhelper()

	print "Getting all counties ..."

	counties = db.get_all_counties()

	print "Adding Geometry data to {0} counties ...".format(len(counties))

	for cells in lines:

		# pull out county name
		csvcountyname = cells[0]

		# pull out geometry
		csvgeometry = cells[4]

		if db.check_county_exists(csvcountyname) == True:

			countyid,countyname,geometry = db.get_county_by_name(csvcountyname)

			db.update_county_geometry(countyid,csvgeometry)

			print "Geometry Updated Successfull for '{0}' County".format(countyname)

		else:

			print "ERROR: Unknown county name: '{0}'".format(csvcountyname)


if __name__ == '__main__': sys.exit(main(sys.argv))
