$("#btnsave").click(function(){ 
    var nm = $("#nameid").val();
    var em = $("#emailid").val();
    var pwd = $("#passid").val();

    if (nm == "") {
        console.log("Please Enter Your Name!")
    }else if(em == ""){
        console.log("Please Enter Your Email!")
    }else if(pwd == ""){
        console.log("Please Enter Your password!")
    }else{
        console.log(nm, em, pwd)
        mydata = {name:nm, email:em, password:pwd};
    $.ajax({
        // url: "{% url 'save' %}",
        url: "/save/",
        method: "POST",
        data: mydata,
        success: function(data){
            console.log(data);
        }
    })
    }
});