import sys

from random import randint

from nysed_irs_db import dbhelper

def test_create_eventtype():

        nysdb = dbhelper()

        print "Testing create_eventtype() ..."

        rnd = randint(0,10000)
        name = "__test_name_{0}__".format(rnd)

        # ... assume that there is an id #1 in each of these ...
        nysdb.create_eventtype(name,1,1);

        exists = nysdb.check_eventtype_exists(name)
        if exists:
                print "PASSED\n"
                success = 1
        else:
                print "FAILED\n"
                success = 0

        return success


def test_create_school():

        nysdb = dbhelper()

        print "Testing create_school() ..."

        rnd = randint(0,10000)
        name = "__test_name_{0}__".format(rnd)

	# ... assume that there is an id #1 in each of these ...
        nysdb.create_school(name,13,11,1,1,1,1,1);

        exists = nysdb.check_school_exists(name)
        if exists:
                print "PASSED\n"
                success = 1
        else:
                print "FAILED\n"
                success = 0

        return success


def test_create_schooltype():

        nysdb = dbhelper()

        print "Testing create_schooltype() ..."

        rnd = randint(0,10000)
        name = "__test_name_{0}__".format(rnd)

        nysdb.create_schooltype(name);

        exists = nysdb.check_schooltype_exists(name)
        if exists:
                print "PASSED\n"
                success = 1
        else:
                print "FAILED\n"
                success = 0

        return success


def test_create_needresourcecatigory():

        nysdb = dbhelper()

        print "Testing create_needresourcecatigory() ..."

        rnd = randint(0,10000)
        name = "__test_name_{0}__".format(rnd)

        nysdb.create_needresourcecatigory(name);

        exists = nysdb.check_needresourcecatigory_exists(name)
        if exists:
                print "PASSED\n"
                success = 1
        else:
                print "FAILED\n"
                success = 0

        return success


def test_create_gradeorganization():

        nysdb = dbhelper()

        print "Testing create_gradeorganization() ..."

        rnd = randint(0,10000)
        name = "__test_name_{0}__".format(rnd)

        nysdb.create_gradeorganization(name);

        exists = nysdb.check_gradeorganization_exists(name)
        if exists:
                print "PASSED\n"
                success = 1
        else:
                print "FAILED\n"
                success = 0

        return success


def test_create_district():

        nysdb = dbhelper()

        print "Testing create_district() ..."

        rnd = randint(0,10000)
        name = "__test_name_{0}__".format(rnd)

        nysdb.create_district(name);

        exists = nysdb.check_district_exists(name)
        if exists:
                print "PASSED\n"
                success = 1
        else:
                print "FAILED\n"
                success = 0

        return success

def test_create_county():

	nysdb = dbhelper()

	print "Testing crete_county() ..."

	rnd = randint(0,10000)
	name = "__test_name_{0}__".format(rnd)
	
	nysdb.create_county(name);
	
	exists = nysdb.check_county_exists(name)
	if exists:
		print "PASSED\n"
		success = 1
	else:
		print "FAILED\n"
		success = 0

	return success

def main(argv):

	print "Application Start."

	totaltests = 1
	success = 0

	print "Running {0} tests ...\n\n".format(totaltests)

	#success += test_create_county()

	#success += test_create_district()

	#success += test_create_gradeorganization()

	#success += test_create_needresourcecatigory()

	#success += test_create_schooltype()

	#success += test_create_school()	

	success += test_create_eventtype()

	print "{0} out of {1} tests passed.".format(success, totaltests)

	if success != totaltests:
		print "!!!! THERE WERE FAILED TESTS !!!!"

	print "\n\nApplication End."

if __name__ == '__main__': sys.exit(main(sys.argv))
