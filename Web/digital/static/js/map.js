// GET CURRENT LOCATION

var card = "<html><head></head><body><div class='card' style=' width: 200px; font-size: 12px; background-color: #fff; color: #222; padding: 10px; border: 0; '><div style='margin: 2px;' class='cardname'> <strong>Name:</strong> John Doe</div><div style='margin: 2px;' class='cardneed'> <strong>Need</strong> Food</div><div style='margin: 2px;' class='cardtimestamp'> <strong>Timestamp</strong> 22:25:56</div><div style='margin: 2px;' class='carddescription'> <strong>Description</strong> Need urgent help, for family of 4</div><div style='margin: 2px;' class='cardaddress'> <strong>Address</strong> 123, CA Lane</div><div style='margin: 2px;' class='cardnumber'> <strong>Phone No.</strong> 1234567890</div><div style='text-align: center;'><a href='tel:1234567890'><div style=' padding: 5px; background-color: orangered; display: inline-block; margin: 2px; color: #222; font-size: 15px; box-shadow: 0px 2px 5px 0 rgba(0,0,0,.5); border-radius: 3px; '>I can help!</div></a></div></div></body></html>"
var latx;
var lngx;
window.onload = function geoloc (){
  //var data = {};
if(navigator.geolocation) {
    navigator.geolocation.watchPosition(function(position) {
      data = {
        latitude: position.coords.latitude,
        longitude: position.coords.longitude,
        accuracy: position.coords.accuracy, 
      };
      latx = data.latitude;
      lngx = data.longitude;
      console.log(typeof(latx))
      console.log(data); 
      init();
    //   $.ajax({
    //     type: 'POST',
    //     url: '/update',
    //     data: data,
    //   });
    }, function() {
      alert('Geolocation failed. Bummer.');
    });
  } else {
      // Browser doesn't support Geolocation
      alert('Your browser doesn\'t support geolocation. Harrumph.');
    }
    //console.log(data);
}



init = function initMap(){
  // Map options
  var options = {
    zoom:12,
    center:{lat:latx,lng:lngx}
  }

  console.log("XXXX")
  console.log(options)
  
  // New map
  var map = new google.maps.Map(document.getElementById('map'), options);
  
  // Listen for click on map
  google.maps.event.addListener(map, 'click', function(event){
    // Add marker
    addMarker({coords:event.latLng});
  });
  
  // Array of markers
  var markers = [
    {
      coords:{lat:42.4668,lng:-70.9495},
      iconImage:'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png',
      content: card
    },
    {
      coords:{lat:19.084249,lng:72.885178},
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
