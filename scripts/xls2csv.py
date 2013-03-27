import sys
import xlrd
import csv

def csv_from_excel(filename):

	# open the xls file
	wb = xlrd.open_workbook(filename)
	
	#get a list of all the sheets in the work book
	for sheetname in wb.sheet_names():
	
		# open the sheet
		sh = wb.sheet_by_name(sheetname)
	
		csvfilename = "{0}_{1}.csv".format(filename,sheetname)

		csv_file = open(csvfilename, 'wb')
		wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

		for rownum in xrange(sh.nrows):
			wr.writerow(sh.row_values(rownum))

		csv_file.close()

def main(argv):
	
	if len(argv) != 2:

		print "\nUsage:\n\t\txls2csv.py <inputfile>\n\n"	

	else:

		# get input file
		inputfile = argv[1]

		csv_from_excel(inputfile);

	print "Done.";

if __name__ == '__main__': sys.exit(main(sys.argv)) 
