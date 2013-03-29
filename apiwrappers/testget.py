import time
from getapi import get

print "Attempting to pull data from database using GET API ...\n"

api = get()

start = time.time()

counties = api.get_counties()
districts = api.get_districts()
schooltypes = api.get_schooltypes()
needs = api.get_needresourcecategories()
grades = api.get_gradeorganizations()
eventtypes = api.get_eventtypes()

end = time.time()

print "\t{0} counties returned.".format(len(counties))
print "\t{0} districts returned.".format(len(districts))
print "\t{0} school types returned.".format(len(schooltypes))
print "\t{0} need resource categories returned.".format(len(needs))
print "\t{0} grade organizations returned.".format(len(grades))
print "\t{0} event types returned.".format(len(eventtypes))

print "\nExecuted in {0} seconds.\n".format(end - start)

print "\nAttempting to pull down all schools ..."

schoolsstart = time.time()

schools = api.get_schools()

print "\t{0} schools returned.".format(len(schools))

schoolsend = time.time()

print "\nExecuted in {0} seconds.\n".format(schoolsend - schoolsstart)
