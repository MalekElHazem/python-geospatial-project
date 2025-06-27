"""
Interactive Map Creation Example

This script demonstrates how to create interactive maps using Folium.
"""

def example_folium_map():
    """
    Example of creating an interactive map with Folium.
    """
    print("=== Interactive Map Creation Example ===")
    print()
    
    # Example code (commented out until libraries are installed)
    print("# Create a basic map centered on Tunisia")
    print("# import folium")
    print("# import geopandas as gpd")
    print()
    
    print("# Initialize map")
    print("# m = folium.Map(")
    print("#     location=[36.85, 10.21],  # Tunis coordinates")
    print("#     zoom_start=10,")
    print("#     tiles='OpenStreetMap'")
    print("# )")
    print()
    
    print("# Add a marker")
    print("# folium.Marker(")
    print("#     [36.85, 10.21],")
    print("#     popup='Tunis-Carthage Airport',")
    print("#     tooltip='Click for more info'")
    print("# ).add_to(m)")
    print()
    
    print("# Load and add GeoJSON data")
    print("# gdf = gpd.read_file('data/raw/your_file.geojson')")
    print("# folium.GeoJson(")
    print("#     gdf,")
    print("#     style_function=lambda feature: {")
    print("#         'fillColor': 'orange',")
    print("#         'color': 'black',")
    print("#         'weight': 2,")
    print("#         'fillOpacity': 0.7")
    print("#     }")
    print("# ).add_to(m)")
    print()
    
    print("# Save map")
    print("# m.save('output_map.html')")
    print()
    
    print("To run this example:")
    print("1. Install required libraries: pip install folium geopandas")
    print("2. Uncomment the code above")
    print("3. Modify data paths as needed")

if __name__ == "__main__":
    example_folium_map()
