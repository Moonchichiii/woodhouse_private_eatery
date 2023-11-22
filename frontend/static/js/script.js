let map;

async function initMap() {
  const { Map } = await google.maps.importLibrary("maps");

  map = new Map(document.getElementById("map"), {
    center: { lat: 56.629253, lng: 15.372672 },
    zoom: 12,
  });
}

initMap();