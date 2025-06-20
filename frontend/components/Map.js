'use client';

import React, { useEffect, useRef, useState } from 'react';
import {
  GoogleMap,
  LoadScript,
  Marker,
} from '@react-google-maps/api';

const libraries = ['places'];

const containerStyle = {
  width: '100%',
  height: '500px',
};

const categories = [
  { label: 'Pet Shops', keyword: 'pet shop' },
  { label: 'Dog Parks', keyword: 'dog park' },
  { label: 'Vet Clinics', keyword: 'veterinary clinic' },
  { label: 'Pet Grooming', keyword: 'pet grooming' },
  { label: 'Pet Boarding', keyword: 'pet boarding' },
];

const Map = () => {
  const [userLocation, setUserLocation] = useState(null);
  const [places, setPlaces] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState(null);
  const mapRef = useRef(null);

const [mapsApi,setMapsApi]=useState(null);

  useEffect(() => {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        setUserLocation({
          lat: position.coords.latitude,
          lng: position.coords.longitude,
        });
      },
      (error) => {
        console.error('Geolocation error:', error);
      }
    );
  }, []);

  const handleCategoryClick = (keyword) => {
    setSelectedCategory(keyword);
    if (mapRef.current && userLocation) {
      const service = new window.google.maps.places.PlacesService(mapRef.current);
      const request = {
        location: userLocation,
        radius: 5000,
        keyword,
      };

      service.nearbySearch(request, (results, status) => {
        if (status === window.google.maps.places.PlacesServiceStatus.OK) {
          setPlaces(results);
        } else {
          console.error('Search failed:', status);
        }
      });
    }
  };

  return (
    <LoadScript googleMapsApiKey="AIzaSyDcUPm64bSj8dUATwXAUJ9FpY-NOqBGeYg" libraries={libraries}>
        {/* butoni za kontrolu pinova na mapi */}
      <div style={{ marginBottom: '1rem' }}>
        {categories.map((cat) => (
          <button
            key={cat.keyword}
            onClick={() => handleCategoryClick(cat.keyword)}
            style={{
              marginRight: '10px',
              padding: '8px 12px',
              background: selectedCategory === cat.keyword ? '#0070f3' : '#eee',
              color: selectedCategory === cat.keyword ? '#fff' : '#000',
              border: 'none',
              borderRadius: '5px',
              cursor: 'pointer',
            }}
          >
            {cat.label}
          </button>
        ))}
      </div>
         
      {userLocation ? (
        <GoogleMap
          mapContainerStyle={containerStyle}
          center={userLocation}
          zoom={14}
          onLoad={(map) => {
            mapRef.current = map
            setMapsApi(window.google.maps)
            console.log('User location:', userLocation);
          }}
        >
            
        {mapsApi && userLocation && (<Marker position={userLocation} label="Ja" icon={{url: './pins/locate.svg',       
                    scaledSize: new window.google.maps.Size(40, 40)}}   />)} 

          {places.map((place, idx) => (
            <Marker
              key={idx}
              position={{

                // lat: 39.1825133326777, 
                // lng: 22.758784814443654,
                lat: place.geometry.location.lat(),
                lng: place.geometry.location.lng(),
              }}
              title={place.name}
            />
          ))}
        </GoogleMap>
      ) : (
        <p>Getting your location...</p>
      )}
    </LoadScript>
  );
};

export default Map;