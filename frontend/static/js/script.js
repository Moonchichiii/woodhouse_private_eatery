let map; 

async function initMap() {
  
  const { Map, LatLng } = await google.maps.importLibrary("maps");


  const center = new LatLng(56.629253, 15.372672);


  map = new Map(document.getElementById("map"), {
    center: center, 
    zoom: 12, 
  });
}


window.initMap = initMap;
 

document.addEventListener("DOMContentLoaded", function() {    
    emailjs.init("hvENepDl1NjzqvuzK");

    document.getElementById('contact-form').addEventListener('submit', function(event) {
        event.preventDefault();

        var params = {
            from_name: document.getElementById("contact-name").value,
            contact_email: document.getElementById("contact-email").value,
            message: document.getElementById("contact-message").value,
        };

        
        const serviceID = "service_s5xj2pk";
        const templateID = "template_wsh7w2j";

        emailjs.send(serviceID, templateID, params)
        .then(res => {

            document.getElementById("contact-name").value = "";
            document.getElementById("contact-email").value = "";
            document.getElementById("contact-message").value = "";

            document.getElementById("success-alert").style.display = "block";
            document.getElementById("fail-alert").style.display = "none";
            
            setTimeout(() => {
                document.getElementById("success-alert").style.display = "none";
            }, 8000);  
        })    
        .catch(err => {    
            document.getElementById("fail-alert").style.display = "block";
            document.getElementById("success-alert").style.display = "none";
            
            setTimeout(() => {
                document.getElementById("fail-alert").style.display = "none";
            }, 8000);  
        });
    });
});

