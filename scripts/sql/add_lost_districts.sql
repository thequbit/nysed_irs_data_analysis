insert into districts(districtname, countyid) select "Altmar-Parish-Williamstown Central School District", counties.countyid from counties where lower(countyname) like "%oswego%";

insert into districts(districtname, countyid) select "Mount Vernon City School District", counties.countyid from counties where lower(countyname) like "%westchester%";