/**
 * Created by badban on 2017/6/24.
 */
function changePage() {
    if( document.getElementById("category").value=="2" ){
        document.getElementById("recent_event_date").style.display="";
        document.getElementById("event_leader").style.display="";
    }
    else if( document.getElementById("category").value=="3" ){
        document.getElementById("location").style.display="";

    }
    else if( document.getElementById("category").value=="4" ){
        document.getElementById("ebook_abstract").style.display="";
        document.getElementById("ebook_author").style.display="";
        document.getElementById("ebook_isbn").style.display="";

    }
    else{
        document.getElementById("recent_event_date").style.display="none";
        document.getElementById("event_leader").style.display="none";
        document.getElementById("location").style.display="none";
        document.getElementById("ebook_abstract").style.display="none";
        document.getElementById("ebook_author").style.display="none";
        document.getElementById("ebook_isbn").style.display="none";
    }

}
