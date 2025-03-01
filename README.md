# South Africa Highways Map Plotter

This Python script is designed to plot highways in South Africa from a GeoJSON file containing highway data. The data is converted into an SVG file, where each highway is represented as a series of connected line segments. The GeoJSON data is expected to contain highways in the form of `MultiLineString` geometries.

## Script Overview

### Steps:

1. **GeoJSON to SVG Conversion**: The script reads a GeoJSON file containing highway data and converts the latitude and longitude coordinates into a simple XY coordinate system using an equirectangular projection.
2. **SVG Generation**: The script generates an SVG file with paths representing highways.
3. **Map Scaling**: A simple scaling factor is applied to the XY coordinates to control the map's size.

### Key Functions

- **`lat_lon_to_xy(lat, lon, scale, translate)`**:
  - Converts the latitude and longitude of each point into XY coordinates for plotting.
  - The `scale` parameter controls the zoom level (default: 1000), and the `translate` parameter allows for offsetting the map (default: `(0, 0)`).
  
- **`geojson_to_svg(geojson, scale, translate, svg_size)`**:
  - Converts the GeoJSON data into SVG path data, handling `MultiLineString` geometries for highways.
  - Creates a polyline for each line segment and adds it to an SVG file.
 
  
