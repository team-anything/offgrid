prov = document.getElementById("provForm")

prov.addEventListener("click", (e) => {
    e.preventDefault();
    console.log("Form submit")

    setTimeout(() => {
        console.log("ZZZZZZZZZZZZZ")
        console.log(xmarkers)
        init = function initMap(){
            
            // Map options
            var options = {
              zoom:12,
              center:{lat:latx,lng:lngx}
            }
          
            // console.log("XXXX")
            // console.log(options)
            
            // New map
            var map = new google.maps.Map(document.getElementById('map'), options);
            
            // Listen for click on map
            // google.maps.event.addListener(map, 'click', function(event){
            //   // Add marker
            //   addMarker({coords:event.latLng});
            // });
            
            // Array of markers
            var markers = [
              {
                coords:{lat:19.017750,lng:72.835823},
                iconImage:'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png',
                content: card
              },
              {
                coords:{lat:42.7762,lng:-71.0773}
              },
            ];
            
            // Loop through markers
            for(var i = 0;i < markers.length;i++){
              // Add marker
              addMarker(markers[i]);
            }
            
            // Add Marker Function
            function addMarker(props){
              var marker = new google.maps.Marker({
                position:props.coords,
                map:map,
                //icon:props.iconImage
              });
              
              // Check for customicon
              if(props.iconImage){
                // Set icon image
                marker.setIcon(props.iconImage);
              }
              
              // Check content
              if(props.content){
                var infoWindow = new google.maps.InfoWindow({
                  content:props.content
                });
                
                marker.addListener('click', function(){
                  infoWindow.open(map, marker);
                });
              }
            }
          }

          init();
          
        console.log("HERE");
    }, 500)
});

