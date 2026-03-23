import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium

def track_phone_precise(number_string):
    # 1. Setup OpenCage (PASTE YOUR KEY HERE)
    key = "8edc3ad2c7ab4e13a7657f858a388d8e"
    geocoder_api = OpenCageGeocode (key)

    try:
        # 2. Parse and get general location
        parsed_number = phonenumbers.parse(number_string)
        location_name = geocoder.description_for_number(parsed_number, "en")
        service_provider = carrier.name_for_number(parsed_number, "en")

        print(f"Tracking: {number_string}")
        print(f"General Region: {location_name}")

        # 3. Get Precise Coordinates (Lat/Lng)
        results = geocoder_api.geocode(location_name)
        if results:
            lat = results[0]['geometry']['lat']
            lng = results[0]['geometry']['lng']
            
            print(f"Coordinates: {lat}, {lng}")
            print(f"Carrier: {service_provider}")

            # 4. Generate a Map File
            my_map = folium.Map(location=[lat, lng], zoom_start=9)
            folium.Marker([lat, lng], popup=location_name).add_to(my_map)
            
            file_name = "mylocation.html"
            my_map.save(file_name)
            print(f"Success! Map saved as {file_name}. Open this file in your browser.")
        else:
            print("Could not find precise coordinates for that region.")

    except Exception as e:
        print(f"Error: {e}")

# Run the tracker
track_phone_precise("+26771279587")