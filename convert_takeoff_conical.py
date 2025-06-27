#!/usr/bin/env python3
"""
Convert montee (takeoff climb) surface shapefile to GeoJSON format
This script converts the takeoff climb surface from shapefile format to GeoJSON
for use in the Cesium 3D viewer.
"""

import geopandas as gpd
import os
import json

def convert_montee_surface():
    """Convert montee (takeoff climb) surface shapefile to GeoJSON"""
    
    # Input and output paths
    input_shapefile = "data/raw/montee/montee.shp"
    output_geojson = "data/processed/takeoff.geojson"
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_geojson), exist_ok=True)
    
    try:
        print("🛫 Loading takeoff climb (montee) surface shapefile...")
        
        # Read the shapefile
        gdf = gpd.read_file(input_shapefile)
        
        print(f"✅ Loaded shapefile with {len(gdf)} features")
        print(f"📊 Columns: {list(gdf.columns)}")
        print(f"🌍 CRS: {gdf.crs}")
        
        # Ensure we're in WGS84 (EPSG:4326) for web mapping
        if gdf.crs != 'EPSG:4326':
            print("🔄 Converting to WGS84 (EPSG:4326)...")
            gdf = gdf.to_crs('EPSG:4326')
        
        # Add height properties if not present
        if 'height' not in gdf.columns:
            # Default height for takeoff climb surface (typically starts low and climbs)
            gdf['height'] = 100  # meters above sea level - takeoff climb surface
            print("➕ Added default height property (100m)")
        
        # Add surface type and metadata
        gdf['surface_type'] = 'takeoff'
        gdf['surface_name'] = 'Take-off Climb Surface'
        gdf['regulation'] = 'ICAO Annex 14'
        gdf['description'] = 'Surface de montée au décollage'
        
        # Save as GeoJSON
        print(f"💾 Saving to {output_geojson}...")
        gdf.to_file(output_geojson, driver='GeoJSON')
        
        print("✅ Successfully converted takeoff climb surface to GeoJSON!")
        print(f"📂 Output file: {output_geojson}")
        
        # Display some info about the converted data
        print(f"\n📊 Conversion Summary:")
        print(f"   Features: {len(gdf)}")
        print(f"   Geometry type: {gdf.geometry.geom_type.unique()}")
        print(f"   Bounds: {gdf.total_bounds}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error converting takeoff climb surface: {str(e)}")
        return False

def convert_conical_3d_surface():
    """Convert the 3D conical surface if it's different from the existing one"""
    
    # Input and output paths
    input_shapefile = "data/raw/conique/conique_3D.shp"
    output_geojson = "data/processed/conical_3d.geojson"
    
    try:
        print("\n🔵 Loading 3D conical surface shapefile...")
        
        # Read the shapefile
        gdf = gpd.read_file(input_shapefile)
        
        print(f"✅ Loaded 3D conical shapefile with {len(gdf)} features")
        print(f"📊 Columns: {list(gdf.columns)}")
        print(f"🌍 CRS: {gdf.crs}")
        
        # Ensure we're in WGS84 (EPSG:4326) for web mapping
        if gdf.crs != 'EPSG:4326':
            print("🔄 Converting to WGS84 (EPSG:4326)...")
            gdf = gdf.to_crs('EPSG:4326')
        
        # Add height properties if not present
        if 'height' not in gdf.columns:
            # Default height for conical surface (typically 45m + slope)
            gdf['height'] = 200  # meters above sea level for conical surface
            print("➕ Added default height property (200m)")
        
        # Add surface type and metadata
        gdf['surface_type'] = 'conical'
        gdf['surface_name'] = 'Conical Surface 3D'
        gdf['regulation'] = 'ICAO Annex 14'
        gdf['description'] = 'Surface conique 3D'
        
        # Save as GeoJSON
        print(f"💾 Saving to {output_geojson}...")
        gdf.to_file(output_geojson, driver='GeoJSON')
        
        print("✅ Successfully converted 3D conical surface to GeoJSON!")
        print(f"📂 Output file: {output_geojson}")
        
        # Display some info about the converted data
        print(f"\n📊 3D Conical Conversion Summary:")
        print(f"   Features: {len(gdf)}")
        print(f"   Geometry type: {gdf.geometry.geom_type.unique()}")
        print(f"   Bounds: {gdf.total_bounds}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error converting 3D conical surface: {str(e)}")
        return False

if __name__ == "__main__":
    print("🛩️ OLS Surface Converter - Takeoff & Conical")
    print("=" * 50)
    
    success_takeoff = convert_montee_surface()
    success_conical = convert_conical_3d_surface()
    
    if success_takeoff and success_conical:
        print("\n🎉 All conversions completed successfully!")
        print("Both takeoff climb and 3D conical surfaces are now ready to load in the Cesium viewer.")
    elif success_takeoff:
        print("\n✅ Takeoff surface conversion completed!")
    elif success_conical:
        print("\n✅ Conical surface conversion completed!")
    else:
        print("\n💥 Conversions failed!")
