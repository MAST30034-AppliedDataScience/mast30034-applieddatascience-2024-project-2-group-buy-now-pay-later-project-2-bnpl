import folium
from IPython.display import display


def create_consumer_postcode_map(geojson,consumer_group_by_postcode):
    m = folium.Map(location=[-25.2744, 133.7751], zoom_start=4)
    # Add Choropleth layer to the map
    folium.Choropleth(
        geo_data=geojson,
        name='choropleth',
        data=consumer_group_by_postcode,
        columns=['postcode', 'total_consumer'],
        key_on='feature.properties.POA_CODE21',
        fill_color='YlOrRd',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Total Consumers'
    ).add_to(m)
    display(m)