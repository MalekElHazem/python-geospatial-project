"""
3D OLS (Obstacle Limitation Surfaces) Viewer

This script creates 3D visualizations for OLS data exported from ArcGIS.
Supports multiple 3D mapping libraries and formats.
"""

def setup_3d_environment():
    """Check and install required packages for 3D visualization."""
    import subprocess
    import sys
    
    required_packages = [
        'plotly',
        'pydeck', 
        'folium',
        'geopandas',
        'rasterio',
        'matplotlib'
    ]
    
    print("Setting up 3D visualization environment...")
    for package in required_packages:
        try:
            __import__(package)
            print(f"✓ {package} already installed")
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def create_plotly_3d_ols():
    """Create 3D OLS visualization using Plotly."""
    print("=== Plotly 3D OLS Viewer ===")
    print()
    
    # Example code (commented out until libraries are installed)
    print("# Load OLS data and create 3D surface")
    print("# import plotly.graph_objects as go")
    print("# import plotly.express as px")
    print("# import geopandas as gpd")
    print("# import numpy as np")
    print()
    
    print("# Load OLS surfaces from ArcGIS export")
    print("# ols_data = gpd.read_file('../data/raw/ols_surfaces.geojson')")
    print("# # or")
    print("# ols_data = gpd.read_file('../data/raw/ols_surfaces.shp')")
    print()
    
    print("# Create 3D surface plot")
    print("# fig = go.Figure()")
    print()
    
    print("# Add each OLS surface")
    print("# for idx, surface in ols_data.iterrows():")
    print("#     if surface.geometry.geom_type == 'Polygon':")
    print("#         coords = list(surface.geometry.exterior.coords)")
    print("#         x_coords = [coord[0] for coord in coords]")
    print("#         y_coords = [coord[1] for coord in coords]")
    print("#         z_coords = [coord[2] if len(coord) > 2 else surface.get('height', 100) for coord in coords]")
    print()
    print("#         fig.add_trace(go.Scatter3d(")
    print("#             x=x_coords,")
    print("#             y=y_coords,") 
    print("#             z=z_coords,")
    print("#             mode='lines+markers',")
    print("#             name=surface.get('ols_type', f'Surface {idx}'),")
    print("#             line=dict(width=3)")
    print("#         ))")
    print()
    
    print("# Configure 3D scene")
    print("# fig.update_layout(")
    print("#     title='OLS - Obstacle Limitation Surfaces',")
    print("#     scene=dict(")
    print("#         xaxis_title='Longitude',")
    print("#         yaxis_title='Latitude',") 
    print("#         zaxis_title='Elevation (m)',")
    print("#         camera=dict(")
    print("#             eye=dict(x=1.5, y=1.5, z=1.5)")
    print("#         )")
    print("#     ),")
    print("#     width=1000,")
    print("#     height=700")
    print("# )")
    print()
    
    print("# Save and show")
    print("# fig.write_html('../data/processed/ols_3d_view.html')")
    print("# fig.show()")
    
    print("To run this example:")
    print("1. Install required libraries: pip install plotly geopandas")
    print("2. Export your OLS data from ArcGIS as GeoJSON or Shapefile")
    print("3. Place the file in data/raw/")
    print("4. Uncomment and modify the code above")

def create_cesium_3d_viewer():
    """Create a Cesium-based 3D viewer (HTML/JavaScript)."""
    print("\n=== Cesium 3D OLS Viewer ===")
    
    cesium_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>OLS 3D Viewer - Cesium</title>
    <script src="https://cesium.com/downloads/cesiumjs/releases/1.114/Build/Cesium/Cesium.js"></script>
    <link href="https://cesium.com/downloads/cesiumjs/releases/1.114/Build/Cesium/Widgets/widgets.css" rel="stylesheet">
    
    <style>
        html, body, #cesiumContainer {
            width: 100%; height: 100%; margin: 0; padding: 0; overflow: hidden;
        }
        #toolbar {
            position: absolute;
            top: 10px;
            left: 10px;
            background: rgba(42, 42, 42, 0.8);
            padding: 10px;
            border-radius: 5px;
            color: white;
            font-family: sans-serif;
        }
        #toolbar button {
            margin: 5px;
            padding: 5px 10px;
            background: #48b;
            color: white;
            border: none;
            border-radius: 3px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div id="cesiumContainer"></div>
    <div id="toolbar">
        <div>OLS 3D Viewer</div>
        <button onclick="loadOLSSurfaces()">Load OLS Surfaces</button>
        <button onclick="toggleTerrain()">Toggle Terrain</button>
        <button onclick="resetView()">Reset View</button>
    </div>

    <script>
        let viewer;
        let olsDataSources = [];
        
        // Initialize Cesium viewer
        function initializeViewer() {
            viewer = new Cesium.Viewer("cesiumContainer", {
                terrainProvider: new Cesium.CesiumTerrainProvider({
                    url: Cesium.IonResource.fromAssetId(1),
                    requestWaterMask: true,
                    requestVertexNormals: true
                }),
                baseLayerPicker: false,
                timeline: false,
                animation: false,
                geocoder: false,
                homeButton: false,
                sceneModePicker: false,
                navigationHelpButton: false,
                infoBox: true,
                resolutionScale: 1.0
            });
            
            // Add satellite imagery
            const esriProvider = new Cesium.UrlTemplateImageryProvider({
                url: 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                maximumLevel: 18,
                credit: 'Tiles © Esri'
            });
            viewer.imageryLayers.addImageryProvider(esriProvider);
            
            // Set initial camera position (Tunis-Carthage Airport)
            viewer.camera.setView({
                destination: Cesium.Cartesian3.fromDegrees(10.21, 36.85, 5000),
                orientation: {
                    heading: 0.0,
                    pitch: -0.3,
                    roll: 0.0
                }
            });
        }
        
        // Load OLS surfaces
        function loadOLSSurfaces() {
            // Load GeoJSON files containing OLS data
            const olsFiles = [
                './data/raw/ols_takeoff.geojson',
                './data/raw/ols_approach.geojson', 
                './data/raw/ols_transitional.geojson',
                './data/raw/ols_horizontal.geojson'
            ];
            
            const colors = [
                Cesium.Color.RED.withAlpha(0.6),
                Cesium.Color.ORANGE.withAlpha(0.6),
                Cesium.Color.YELLOW.withAlpha(0.6),
                Cesium.Color.BLUE.withAlpha(0.6)
            ];
            
            olsFiles.forEach((file, index) => {
                Cesium.GeoJsonDataSource.load(file)
                    .then(function(dataSource) {
                        viewer.dataSources.add(dataSource);
                        olsDataSources.push(dataSource);
                        
                        // Style the OLS surfaces
                        const entities = dataSource.entities.values;
                        for (let i = 0; i < entities.length; i++) {
                            const entity = entities[i];
                            
                            if (entity.polygon) {
                                entity.polygon.material = colors[index % colors.length];
                                entity.polygon.outline = true;
                                entity.polygon.outlineColor = Cesium.Color.WHITE;
                                entity.polygon.height = 0;
                                entity.polygon.extrudedHeight = entity.properties?.height || 100;
                            }
                        }
                        
                        console.log(`Loaded OLS surface: ${file}`);
                    })
                    .catch(function(error) {
                        console.warn(`Could not load ${file}:`, error);
                    });
            });
        }
        
        // Toggle terrain
        function toggleTerrain() {
            if (viewer.terrainProvider instanceof Cesium.EllipsoidTerrainProvider) {
                viewer.terrainProvider = new Cesium.CesiumTerrainProvider({
                    url: Cesium.IonResource.fromAssetId(1)
                });
            } else {
                viewer.terrainProvider = new Cesium.EllipsoidTerrainProvider();
            }
        }
        
        // Reset camera view
        function resetView() {
            viewer.camera.setView({
                destination: Cesium.Cartesian3.fromDegrees(10.21, 36.85, 5000),
                orientation: {
                    heading: 0.0,
                    pitch: -0.3,
                    roll: 0.0
                }
            });
        }
        
        // Initialize when DOM is loaded
        document.addEventListener('DOMContentLoaded', function() {
            initializeViewer();
        });
    </script>
</body>
</html>'''
    
    # Save the Cesium HTML file
    with open('../examples/ols_3d_cesium_viewer.html', 'w') as f:
        f.write(cesium_html)
    
    print("✓ Created Cesium 3D viewer: examples/ols_3d_cesium_viewer.html")
    print("Features:")
    print("- 3D terrain visualization")
    print("- Multiple OLS surface layers")
    print("- Interactive controls")
    print("- Satellite imagery basemap")

def create_pydeck_3d_viewer():
    """Create PyDeck 3D OLS viewer."""
    print("\n=== PyDeck 3D OLS Viewer ===")
    print()
    
    print("# PyDeck example for 3D OLS visualization")
    print("# import pydeck as pdk")
    print("# import geopandas as gpd")
    print("# import pandas as pd")
    print()
    
    print("# Load OLS data")
    print("# ols_data = gpd.read_file('../data/raw/ols_surfaces.geojson')")
    print()
    
    print("# Convert to PyDeck format")
    print("# ols_data['coordinates'] = ols_data.geometry.apply(")
    print("#     lambda x: [list(x.exterior.coords)] if x.geom_type == 'Polygon' else []")
    print("# )")
    print()
    
    print("# Create 3D polygon layer")
    print("# polygon_layer = pdk.Layer(")
    print("#     'PolygonLayer',")
    print("#     ols_data,")
    print("#     get_polygon='coordinates',")
    print("#     get_elevation='height',")
    print("#     get_fill_color='[255, 165, 0, 160]',")
    print("#     get_line_color='[255, 255, 255]',")
    print("#     line_width_min_pixels=2,")
    print("#     elevation_scale=1,")
    print("#     extruded=True,")
    print("#     wireframe=True")
    print("# )")
    print()
    
    print("# Set initial view")
    print("# view_state = pdk.ViewState(")
    print("#     longitude=10.21,")
    print("#     latitude=36.85,")
    print("#     zoom=12,")
    print("#     pitch=45,")
    print("#     bearing=0")
    print("# )")
    print()
    
    print("# Create deck")
    print("# deck = pdk.Deck(")
    print("#     layers=[polygon_layer],")
    print("#     initial_view_state=view_state,")
    print("#     map_style='satellite'")
    print("# )")
    print()
    
    print("# Save to HTML")
    print("# deck.to_html('../data/processed/ols_pydeck_3d.html')")
    
    print("To run this example:")
    print("1. Install PyDeck: pip install pydeck")
    print("2. Prepare your OLS GeoJSON data")
    print("3. Uncomment and run the code above")

if __name__ == "__main__":
    print("🛩️  OLS 3D Visualization Toolkit")
    print("=" * 50)
    
    # Show available options
    create_plotly_3d_ols()
    create_cesium_3d_viewer()
    create_pydeck_3d_viewer()
    
    print("\n" + "=" * 50)
    print("📋 Quick Start Guide:")
    print("1. Export your OLS surfaces from ArcGIS as GeoJSON or Shapefile")
    print("2. Place files in data/raw/ folder")
    print("3. Choose your preferred 3D viewer:")
    print("   - Plotly: Interactive Python plots")
    print("   - Cesium: Professional web-based 3D")
    print("   - PyDeck: Uber's deck.gl visualization")
    print("4. Install required packages and run examples")
