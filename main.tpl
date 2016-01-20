<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
<script>
$( document ).ready(function() {
       
               $( "#submit" ).click(function() {
                        var postObj = {};
                        postObj["k"] = $( "#k" ).val();
                        postObj["x_param"] = $( "#x_param" ).val();
                        postObj["y_param"] = $( "#y_param" ).val();
                        console.log(postObj);
               			$.post("/cluster",postObj,
    				function(data, status){
										//$("#content").text(data);
                                        console.log(data)
										var j = JSON.parse(data);
                                	
                                        $("#image").attr("src", "/static/"+j['filename'])
                                        $("#image").show()
										document.getElementById("total").innerHTML = json["total_points"];
                                        
               			});
		});

});
</script>

</head>

<body>
Enter the number of clusters:<input type= "text" name = "k" id = "k"/>
Parameter1:<select id = "x_param"><option value = "sepelLength">sepelLength</option><option value = "sepelWidth">sepelWidth</option><option value = "petalLength">petalLength</option><option value = "petalWidth">petalWidth</option></select>
Parameter2:<select id = "y_param"><option value = "sepelLength">sepelLength</option><option value = "sepelWidth">sepelWidth</option><option value = "petalLength">petalLength</option><option value = "petalWidth">petalWidth</option></select>
<div><input type = "submit" value = "submit" id = "submit"/>
</div>
<div>
<img id = "image" src = '' ></img>
<h1 id="h" ></h1>
</div>
</body>
</html>
