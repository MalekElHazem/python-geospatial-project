# OLS 3D Integration Guide

## Quick Setup for Your ArcGIS OLS Data

### 1. Export from ArcGIS

Export your OLS surfaces from ArcGIS in one of these formats:

**Option A: GeoJSON (Recommended)**
1. In ArcGIS, right-click your OLS layer
2. Export → Export Data
3. Format: GeoJSON
4. Include Z-values (height) if available

**Option B: Shapefile**
1. Export as Shapefile with Z-values
2. We'll convert to GeoJSON in Python

**Option C: KML**
1. Export as KML with 3D geometry
2. We'll convert in Python

### 2. File Naming Convention

Name your exported files with these patterns for automatic detection:

```
ols_takeoff.geojson       - Take-off surfaces
ols_approach.geojson      - Approach surfaces  
ols_transitional.geojson  - Transitional surfaces
ols_horizontal.geojson    - Horizontal surfaces
ols_conical.geojson       - Conical surfaces
ols_inner.geojson         - Inner horizontal surfaces
```

### 3. File Placement

Place your OLS files in:
```
python-geospatial-project/
├── data/
│   └── raw/
│       ├── ols_takeoff.geojson
│       ├── ols_approach.geojson
│       ├── ols_transitional.geojson
│       └── ... (other OLS files)
```

### 4. Quick Start Commands

```bash
# Navigate to project
cd "d:\School\PFE\projet oussema\python-geospatial-project"

# Install required libraries
pip install plotly geopandas pydeck folium

# Run the 3D viewer script
python examples/05_3d_ols_viewer.py

# Or open the Cesium web viewer
# Open: examples/ols_3d_cesium_professional.html in your browser
```

### 5. 3D Viewer Options

**🌐 Web-based (Cesium) - RECOMMENDED**
- File: `examples/ols_3d_cesium_professional.html`
- Features: Professional 3D globe, terrain, interactive controls
- Just open in any modern web browser
- Automatically detects and loads OLS files

**📊 Python-based (Plotly)**
- File: `examples/05_3d_ols_viewer.py`
- Features: Interactive Python plots, export to HTML
- Run in Jupyter notebook or Python script

**🎮 Advanced (PyDeck)**
- Uber's deck.gl visualization
- High-performance 3D rendering
- Best for large datasets

### 6. Data Format Requirements

Your OLS data should include these attributes:

```json
{
  "type": "Feature",
  "properties": {
    "height": 150,           // Height in meters
    "ols_type": "takeoff",   // Surface type
    "elevation": 100,        // Ground elevation
    "runway": "01/19"        // Associated runway
  },
  "geometry": {
    "type": "Polygon",
    "coordinates": [[[lon, lat, height], ...]]
  }
}
```

### 7. Troubleshooting

**File not loading?**
- Check file path and naming
- Verify GeoJSON format validity
- Ensure Z-coordinates are included

**Colors not showing correctly?**
- Check the OLS type detection in filename
- Modify color scheme in code if needed

**Performance issues?**
- Simplify geometry in ArcGIS before export
- Use lower resolution for web viewing

### 8. Customization

**Change Colors:**
Edit the color schemes in the viewer files:
- Cesium: Modify `olsConfig` object
- Plotly: Modify `ols_colors` dictionary

**Add New Surface Types:**
Add entries to the configuration objects with your custom OLS types.

**Integrate with Existing Maps:**
Copy the OLS loading code into your existing 3D map applications.

### 9. Example Data Structure

If you don't have OLS data yet, the viewers include sample data creation functions that generate example OLS surfaces around Tunis-Carthage Airport.

### 10. Next Steps

1. Export your ArcGIS OLS data
2. Place files in `data/raw/` folder  
3. Open `ols_3d_cesium_professional.html` in browser
4. Click "Load OLS Data" button
5. Enjoy your 3D OLS visualization!

### Support

- Check the Jupyter notebook: `notebooks/ols_3d_visualization.ipynb`
- Run example scripts in `examples/` folder
- Modify code as needed for your specific requirements
