<?php
	require_once("_header.php");
?>

	<div class="miniheader">
		Welcome to the NYS Eduation VADIR API Access Website
	</div>
	<br>

	The State of New York has a Stat Education Department.  One of the many things this department supplies to the tens of thousands of 
	students and their families of New York state is a yearly report of Violent and Disruptive Incidents, or VADIR.  The last several years 
	of these reports can be found here:<br>
	<br>
	<div class="tab">
		<a href="http://www.p12.nysed.gov/irs/vadir/vadir-reporting.html">NYSED:IRS:Violent and Disruptive Incidents Report</a>
	</div>
	<br>
	
	There is a plethera of information stored in these documents about incidents with county, district, and down to school level granularity 
	across a number of different incident types.  As of the 2010-2011 school year the state recognized 22 different types of incidents, some
	with a distiction of weapon use during the incident.<br>
	<br>
	
	The amount of data here is staggering, and difficult to consume in it's form within multiple Excel documents.  It is the effort of this site
	to provide a set of tools to allow for easier access to, and querying of this data.<br>
	<br>
	
	This publicly accessable website currently holds information starting from the 2006-2007 school year threw the 2010-2011 school year.  It also
	holds information about counties, school districts, and schools located within New York state outside of New York City.<br>
	<br>

	<div class="tab">
		The database currently holds information on ...
	</div>
	
	<?php
	
		require_once("./api/tools/SchoolTool.class.php");
		require_once("./api/tools/DistrictTool.class.php");
		require_once("./api/tools/CountyTool.class.php");
	
		$stool = new SchoolTool();
		$schoolCount = $stool->GetSchoolCount();
			
		$dtool = new DistrictTool();
		$districtCount = $dtool->GetDistrictCount();
		
		$ctool = new CountyTool();
		$countyCount = $ctool->GetCountyCount();
	
		echo '<div class="tab2"><b>' . $countyCount . ' Counties</b><br></div>';
		echo '<div class="tab2"><b>' . $districtCount . ' School Districts</b><br></div>';
		echo '<div class="tab2"><b>' . $schoolCount . ' Schools</b><br></div>';
		echo '<div class="tab2">As well as <b>over half a million</b> cells imported from the Excel documents provided by New York State</div>';

	?>
	<br>
	
	The purpose for this site is to provive an Application Programming Interface (API) in the form of JSON objects to developers that would like to access 
	this data.  The intent of this site is to provide robust methods of gaining access to the raw data, as well as specific queries.<br>
	
	<br>
	If there are any specific API's you would like added, please do not hesitate to contact the maintainer of this website.  Contact information can be
	found on the <a href="about.php">about</a> page.<br>
	
	<br>
	<br>
	
	<hr>
	
	<!--
	
	<br>
	<div id="querytime"></div>
	<br>
	
	<h4>Below is a list of all of the counties in the database</h4>
	<br>
	<div id="counties">
	</div>
	
	<br><br>
	
	<h4>Below is a list of all of the school districts in the database</h4>
	<br>
	<div id="districts">
	</div>
	
	<script src="http://code.jquery.com/jquery-latest.js"></script>
	<script src="example.js"></script>
	<script type="text/javascript">
	
		$(document).ready(function() {
		
			//getCounties();
			//getDistricts();
	
		});
	
	</script>

	-->

<?php
	require_once("_footer.php");
?>