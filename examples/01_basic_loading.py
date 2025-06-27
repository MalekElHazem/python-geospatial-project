"""
Basic Geospatial Data Loading Example

This script demonstrates how to load and examine geospatial data.
"""

def example_basic_loading():
    """
    Example of loading and examining geospatial data.
    """
    print("=== Basic Geospatial Data Loading Example ===")
    print()
    
    # Example code (commented out until libraries are installed)
    print("# Load a shapefile")
    print("# import geopandas as gpd")
    print("# gdf = gpd.read_file('data/raw/your_shapefile.shp')")
    print()
    
    print("# Examine the data")
    print("# print(gdf.head())")
    print("# print(gdf.info())")
    print("# print(f'CRS: {gdf.crs}')")
    print("# print(f'Shape: {gdf.shape}')")
    print()
    
    print("# Load a GeoJSON file")
    print("# gdf_geojson = gpd.read_file('data/raw/your_file.geojson')")
    print()
    
    print("To run this example:")
    print("1. Install GeoPandas: pip install geopandas")
    print("2. Place your data files in the data/raw/ folder")
    print("3. Uncomment the code above and modify file paths")

if __name__ == "__main__":
    example_basic_loading()
