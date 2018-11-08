	
	function zuoshiqing(){
		
		sousuo=document.getElementById("neirong").value;
		if(!sousuo){
			alert("请输入搜索内容");
		}
		else{
		var baidu="https://www.baidu.com/";
		var lianjie=baidu+"s?"+"wd="+sousuo;
		window.open(lianjie);     
		}
		
	}


	
