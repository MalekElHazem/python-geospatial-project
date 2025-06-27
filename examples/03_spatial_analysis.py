"""
Spatial Analysis Example

This script demonstrates basic spatial analysis operations.
"""

def example_spatial_analysis():
    """
    Example of performing spatial analysis operations.
    """
    print("=== Spatial Analysis Example ===")
    print()
    
    # Example code (commented out until libraries are installed)
    print("# Load data")
    print("# import geopandas as gpd")
    print("# from shapely.geometry import Point")
    print()
    
    print("# Load airport and surrounding data")
    print("# airports = gpd.read_file('data/raw/airports.geojson')")
    print("# buildings = gpd.read_file('data/raw/buildings.geojson')")
    print()
    
    print("# Calculate buffers around airports")
    print("# airport_buffers = airports.copy()")
    print("# airport_buffers.geometry = airports.geometry.buffer(0.01)  # ~1km buffer")
    print()
    
    print("# Find buildings within airport buffer zones")
    print("# buildings_near_airports = gpd.sjoin(")
    print("#     buildings, airport_buffers,")
    print("#     how='inner', predicate='intersects'")
    print("# )")
    print()
    
    print("# Calculate areas")
    print("# buildings['area_m2'] = buildings.geometry.area")
    print("# print(f'Total building area: {buildings.area_m2.sum():.2f} m²')")
    print()
    
    print("# Distance analysis")
    print("# airport_point = Point(10.21, 36.85)  # Tunis-Carthage coordinates")
    print("# buildings['distance_to_airport'] = buildings.geometry.distance(airport_point)")
    print()
    
    print("# Coordinate transformation")
    print("# buildings_utm = buildings.to_crs('EPSG:32632')  # UTM Zone 32N")
    print("# print(f'Original CRS: {buildings.crs}')")
    print("# print(f'Transformed CRS: {buildings_utm.crs}')")
    print()
    
    print("To run this example:")
    print("1. Install required libraries: pip install geopandas shapely")
    print("2. Prepare your geospatial data files")
    print("3. Uncomment and modify the code above")

if __name__ == "__main__":
    example_spatial_analysis()
