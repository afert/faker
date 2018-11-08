function checkField()
{  

 var letterNumber = /^[\d\w\s\.\?\!ñáéíóúü]+$/;  
 var page1=$('#page1').val()
 var page2=$('#page2').val()
    if(page1.match(letterNumber) && page2.match(letterNumber) )   
      {  
       return true; 
      }  
    else if(page1.match(letterNumber) && !page2.match(letterNumber)){

    	// $('#page2').after(' <div class="alert alert-danger" role="alert"> <strong>Oh snap!</strong> Change a few things up and try submitting again.</div>');
    		
    	    $("form").submit(function(e){
    		e.preventDefault(); });
    	    
    }
    else  if(!page1.match(letterNumber) && page2.match(letterNumber)){
    	//$('#page1').after(' <div class="alert alert-danger" role="alert"> <strong>Oh snap!</strong> Change a few things up and try submitting again.</div>');

    	    $("form").submit(function(e){
    		e.preventDefault(); });

    	   		
    	   }
    }
    else if(!page1.match(letterNumber) && !page2.match(letterNumber)){
    	//$('#page1').after(' <div class="alert alert-danger" role="alert"> <strong>Oh snap!</strong> Change a few things up and try submitting again.</div>');
    	//$('#page2').after(' <div class="alert alert-danger" role="alert"> <strong>Oh snap!</strong> Change a few things up and try submitting again.</div>');
    	$("form").submit(function(e){
    		e.preventDefault(); });
    }
    // {   
    
    // $(who).after(' <div class="alert alert-danger" role="alert"> <strong>Oh snap!</strong> Change a few things up and try submitting again.</div>');
    // // $('.alert.alert-danger').hide('5000');
     
        
    // }
    
 }