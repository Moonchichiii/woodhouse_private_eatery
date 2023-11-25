let map;

async function initMap() {
  const { Map } = await google.maps.importLibrary("maps");

  map = new Map(document.getElementById("map"), {
    center: { lat: 56.629253, lng: 15.372672 },
    zoom: 12,
  });
}

initMap();


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


*/