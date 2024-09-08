import json
import svgwrite

# Convert lat/lon to simple XY coordinates (equirectangular projection)
def lat_lon_to_xy(lat, lon, scale=1000, translate=(0, 0)):
    x = (lon + 180) * (scale / 360) + translate[0]
    y = (90 - lat) * (scale / 180) + translate[1]
    return x, y

# Function to generate SVG path data from GeoJSON (handling MultiLineString)
def geojson_to_svg(geojson, scale=1000, translate=(0, 0), svg_size=(1000, 1000)):
    # Create an SVG drawing
    dwg = svgwrite.Drawing('output_map.svg', size=svg_size, profile='tiny')
    
    for feature in geojson['features']:
        geometry_type = feature['geometry']['type']
        
        if geometry_type == 'MultiLineString':
            for linestring in feature['geometry']['coordinates']:
                path_data = []
                for lon, lat in linestring:
                    x, y = lat_lon_to_xy(lat, lon, scale, translate)
                    path_data.append((x, y))
                
                # Create a polyline for the linestring
                dwg.add(dwg.polyline(path_data, stroke='black', fill='none'))

    # Save the SVG file
    dwg.save()

# Load GeoJSON data from the export.geojson file
with open('N3.geojson', 'r') as file:
    geojson_data = json.load(file)

# Generate the SVG from the GeoJSON data (as lines)
geojson_to_svg(geojson_data, scale=500, translate=(0, 0))
