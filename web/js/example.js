	function getCounties()
		{
			postData = {};
			
			postData.what = "county";
		
			// get json from api call
			$.getJSON("./api/get.php",
			postData,
			function(data) {
			
				var resultsHtml = "";
				
				// check to see if there was an error
				if( data.errorcode != "0" )
				{
					resultsHtml += "<br><p>There was an error processing your request, please try again later.  If the error persists, please contact the site administrator.</p><br>";
				}
				else
				{
					var rounderQueryTime = Math.round(data.querytime*10000)/10000;
					
					$("#querytime").html("Query Took " + rounderQueryTime + " Seconds.");
					
					if( data.results.length == 0 )
					{
						resultsHtml += "<br><p>Your search criteria returned zero results.  Please refine your search and try again.</p><br>";
					}
					else
					{
						// iterate through the returned json array and add each document to the div
						$.each(data.results, 
							function(i,item){
							
								resultsHtml += '<div class="tab2">';
								
								resultsHtml += item.countyname;
								
								resultsHtml += '</div>';
							
						});
					}
				
				}
	
				// display built html
				$("#counties").html(resultsHtml);
				$('#counties').hide();
				$('#counties').show("slow");
			
			});
		}
	
		function getDistricts()
		{
			postData = {};
			
			postData.what = "district";
		
			// get json from api call
			$.getJSON("./api/get.php",
			postData,
			function(data) {
			
				var resultsHtml = "";
				
				// check to see if there was an error
				if( data.errorcode != "0" )
				{
					resultsHtml += "<br><p>There was an error processing your request, please try again later.  If the error persists, please contact the site administrator.</p><br>";
				}
				else
				{
					var rounderQueryTime = Math.round(data.querytime*10000)/10000;
					
					$("#querytime").html("Query Took " + rounderQueryTime + " Seconds.");
					
					if( data.results.length == 0 )
					{
						resultsHtml += "<br><p>Your search criteria returned zero results.  Please refine your search and try again.</p><br>";
					}
					else
					{
						// iterate through the returned json array and add each document to the div
						$.each(data.results, 
							function(i,item){
							
								resultsHtml += '<div class="tab2">';
								
								resultsHtml += item.districtname;
								
								resultsHtml += '</div>';
							
						});
					}
				
				}
	
				// display built html
				$("#districts").html(resultsHtml);
				$('#districts').hide();
				$('#districts').show("slow");
			
			});
		}