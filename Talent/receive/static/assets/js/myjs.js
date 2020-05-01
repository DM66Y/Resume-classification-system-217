
window.onload = function(){
    document.getElementById("switch_resume_file").onclick = function(){
        document.getElementById("resume_textarea").style.display = "none";
        document.getElementById("resume_upload").style.display = "block";
        $("#resume_textarea").val("");
       }
     document.getElementById("switch_resume_text").onclick = function(){
        document.getElementById("resume_textarea").style.display = "block";
        document.getElementById("resume_upload").style.display = "none";
       }
}