<?php
	require_once("_header.php");
?>

	<script src="http://code.jquery.com/jquery-latest.js"></script>
	<script src="js/compare.js"></script>
	<script type="text/javascript">
	
		$(document).ready(function() {
		
			populateDistricts();
			//getCounties();
			//getDistricts();
	
		});
	
	</script>

	This simple tool allows you to compare different districts against each other.  Select the school year you are interested in, and then two districts to display data about those districts.
	
	<br>
	<br>
	
	<div class="selecta">
		Select District A:
		<div id="selectdistricta"></div>
	</div>
	
	<div class="selectb">
		Select District B:
		<div id="selectdistrictb"></div>
	</div>

	<br><br><br>
	<input id="comparebutton" type="button" value="Compare" onclick="compare();" />
	<br>
	
	<div id="compareresults" class="compareresults">
		
		<div id="resultsa" class="selecta">
			<div id="districttitlea"></div>
			<div id="schoolcounta"></div>
			<div id="incidentcountsa"></div>
		</div>
		
		<div id="resultsb" class="selectb">
			<div id="districttitleb"></div>
			<div id="schoolcountb"></div>
			<div id="incidentcountsb"></div>
		</div>
	</div>

	<br>

<?php
	require_once("_footer.php");
?>