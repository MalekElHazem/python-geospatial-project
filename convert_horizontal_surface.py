#!/usr/bin/env python3
"""
Convert horizontal surface shapefile to GeoJSON format for web visualization
"""

import os
import sys
import geopandas as gpd
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

def convert_horizontal_surface():
    """Convert the horizontal surface shapefile to GeoJSON"""
    
    print("🛩️ Horizontal Surface Converter")
    print("=" * 50)
    
    # Define paths
    source_file = "data/raw/horizental/horizental.shp"
    output_file = "data/processed/horizontal.geojson"
    
    # Check if source file exists
    if not os.path.exists(source_file):
        print(f"❌ Source file not found: {source_file}")
        return False
    
    # Create output directory if it doesn't exist
    Path("data/processed").mkdir(parents=True, exist_ok=True)
    
    try:
        print(f"🔍 Loading shapefile: {source_file}")
        
        # Load the shapefile
        gdf = gpd.read_file(source_file)
        
        print(f"📊 Loaded {len(gdf)} features")
        print(f"📏 Geometry type: {gdf.geom_type.iloc[0] if len(gdf) > 0 else 'Unknown'}")
        print(f"🗺️  CRS: {gdf.crs}")
        
        # Display column information
        print("\n📋 Columns in the shapefile:")
        for col in gdf.columns:
            if col != 'geometry':
                print(f"   - {col}: {gdf[col].dtype}")
        
        # Ensure we have WGS84 coordinates (EPSG:4326) for web use
        if gdf.crs != 'EPSG:4326':
            print(f"🔄 Converting from {gdf.crs} to EPSG:4326 (WGS84)")
            gdf = gdf.to_crs('EPSG:4326')
        
        # Save as GeoJSON
        print(f"💾 Saving as GeoJSON: {output_file}")
        gdf.to_file(output_file, driver="GeoJSON")
        
        # Verify the output
        file_size = os.path.getsize(output_file)
        file_size_mb = file_size / (1024 * 1024)
        
        print(f"✅ Conversion successful!")
        print(f"📁 Output file: {output_file}")
        print(f"📊 File size: {file_size_mb:.2f} MB")
        print(f"🔢 Features: {len(gdf)}")
        
        # Display sample coordinates for verification
        if len(gdf) > 0:
            bounds = gdf.total_bounds
            print(f"\n🌍 Geographic bounds:")
            print(f"   Longitude: {bounds[0]:.6f} to {bounds[2]:.6f}")
            print(f"   Latitude: {bounds[1]:.6f} to {bounds[3]:.6f}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error converting horizontal surface: {str(e)}")
        return False

def main():
    """Main function"""
    success = convert_horizontal_surface()
    
    if success:
        print(f"\n🎯 Next steps:")
        print(f"   1. Open your OLS 3D viewer (ols_3d_cesium_professional.html)")
        print(f"   2. Click 'Load Data Folder' button")
        print(f"   3. The horizontal surface should now load properly!")
        print(f"\n💡 The converted file is ready for web visualization!")
    else:
        print(f"\n❌ Conversion failed. Please check the error messages above.")

if __name__ == "__main__":
    main()
