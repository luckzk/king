function bv(){
	alert("如果设置背景视频失败 可去豚鼠公众号自行修改代码（有提示） 公众号@豚鼠极客");
	bvbvb=document.getElementById("bvt");
			xinbiao=document.createElement("source");
			xinbiao.setAttribute("type","video/mp4");
			xinbiao.setAttribute("src","niconico.mp4");
			bvbvb.appendChild(xinbiao);
	
	
	
	
	document.getElementById("wenjian").click();
		filebg=document.getElementById("wenjian").files[0];
		var reader=new FileReader();
		reader.readAsDataURL(filebg);
		reader.onload=function(){
		var result = this.result;
		 try {
            localStorage.setItem("myBV", result);
			bvbvb=document.getElementById("bvt");
			xinbiao=document.createElement("source");
			xinbiao.setAttribute("type","video/mp4");
			xinbiao.setAttribute("src","niconico.mp4");
			bvbvb.appendChild(xinbiao);
        }catch (e) {
            console.log("Storage failed: " + e);
        }	
		}
	}	