"""
Raster Data Processing Example

This script demonstrates how to work with raster data.
"""

def example_raster_processing():
    """
    Example of working with raster data using Rasterio.
    """
    print("=== Raster Data Processing Example ===")
    print()
    
    # Example code (commented out until libraries are installed)
    print("# Load raster data")
    print("# import rasterio")
    print("# import numpy as np")
    print("# import matplotlib.pyplot as plt")
    print()
    
    print("# Open and read raster file")
    print("# with rasterio.open('data/raw/elevation.tif') as src:")
    print("#     elevation = src.read(1)  # Read first band")
    print("#     transform = src.transform")
    print("#     crs = src.crs")
    print("#     bounds = src.bounds")
    print()
    
    print("# Basic raster statistics")
    print("# print(f'Shape: {elevation.shape}')")
    print("# print(f'Min elevation: {np.nanmin(elevation):.2f}m')")
    print("# print(f'Max elevation: {np.nanmax(elevation):.2f}m')")
    print("# print(f'Mean elevation: {np.nanmean(elevation):.2f}m')")
    print()
    
    print("# Visualize raster data")
    print("# plt.figure(figsize=(10, 8))")
    print("# plt.imshow(elevation, cmap='terrain')")
    print("# plt.colorbar(label='Elevation (m)')")
    print("# plt.title('Digital Elevation Model')")
    print("# plt.show()")
    print()
    
    print("# Raster calculations")
    print("# slope = np.gradient(elevation)")
    print("# high_elevation = elevation > np.percentile(elevation, 90)")
    print()
    
    print("# Export processed raster")
    print("# with rasterio.open(")
    print("#     'data/processed/processed_elevation.tif',")
    print("#     'w',")
    print("#     driver='GTiff',")
    print("#     height=elevation.shape[0],")
    print("#     width=elevation.shape[1],")
    print("#     count=1,")
    print("#     dtype=elevation.dtype,")
    print("#     crs=crs,")
    print("#     transform=transform")
    print("# ) as dst:")
    print("#     dst.write(elevation, 1)")
    print()
    
    print("To run this example:")
    print("1. Install required libraries: pip install rasterio matplotlib numpy")
    print("2. Place DEM/elevation data in data/raw/")
    print("3. Uncomment and modify the code above")

if __name__ == "__main__":
    example_raster_processing()
