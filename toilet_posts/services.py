import folium as folium
import geocoder


def map_markers(addresses):
    m = folium.Map(location=[55.7, 37.5], zoom_start=10)
    for el in addresses:
        location = geocoder.osm(el[2])
        lat = location.lat
        lng = location.lng
        folium.Marker([lat, lng], popup=f"Автор: {el[1]}", tooltip=f"Рейттинг: {el[4]}").add_to(m)
    m = m._repr_html_()

    return m


def map_marker_detail(address):
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng

    m = folium.Map(location=[55.7, 37.5], zoom_start=10)
    folium.Marker([lat, lng]).add_to(m)
    m = m._repr_html_()
    return m
