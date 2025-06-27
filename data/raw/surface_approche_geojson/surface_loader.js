/**
 * Surface Loader for 3D Airport Visualization
 * Loads all converted surface data into Cesium viewer
 * Generated automatically by convert_all_surfaces.py
 */

class SurfaceLoader {
    constructor(viewer) {
        this.viewer = viewer;
        this.loadedSurfaces = {
            approach: [],
            reseaux: [],
            dxf: []
        };
        this.surfaceVisibility = {
            approach: true,
            buildings: false,
            roads: false,
            ols: false,
            natural: false,
            transport: false
        };
    }

    // Load the original approach surface
    async loadApproachSurface() {
        try {
            const response = await fetch('./surface_approche_geojson/surfaceapproche.geojson');
            const geojsonData = await response.json();
            
            const entities = [];
            geojsonData.features.forEach((feature, index) => {
                const entity = this.viewer.entities.add({
                    name: `Approach Surface ${index + 1}`,
                    polygon: {
                        hierarchy: feature.geometry.coordinates[0].map(coord => 
                            Cesium.Cartesian3.fromDegrees(coord[0], coord[1], coord[2] || 0)
                        ),
                        material: Cesium.Color.YELLOW.withAlpha(0.6),
                        outline: true,
                        outlineColor: Cesium.Color.ORANGE,
                        extrudedHeight: 0,
                        height: feature.geometry.coordinates[0][0][2] || 0
                    }
                });
                entities.push(entity);
            });
            
            this.loadedSurfaces.approach = entities;
            console.log(`✅ Loaded ${entities.length} approach surfaces`);
            return entities;
        } catch (error) {
            console.error('❌ Error loading approach surfaces:', error);
            return [];
        }
    }

    // Load OLS surfaces from DXF conversion
    async loadOLSSurfaces() {
        const olsFiles = [
            'suraface dapproche aligned.geojson',
            'suraface de transition.geojson', 
            'suraface interieuere de transition.geojson',
            'surface conique aligned.geojson',
            'surface d\'atterrissage interrompu.geojson',
            'surface de montee au decollage.geojson',
            'surface horizontal interieur aligned.geojson',
            'surface interieure dapproche.geojson'
        ];

        const colors = [
            Cesium.Color.CYAN.withAlpha(0.5),
            Cesium.Color.PURPLE.withAlpha(0.5),
            Cesium.Color.PINK.withAlpha(0.5),
            Cesium.Color.ORANGE.withAlpha(0.5),
            Cesium.Color.RED.withAlpha(0.5),
            Cesium.Color.GREEN.withAlpha(0.5),
            Cesium.Color.BLUE.withAlpha(0.5),
            Cesium.Color.MAGENTA.withAlpha(0.5)
        ];

        const allEntities = [];

        for (let i = 0; i < olsFiles.length; i++) {
            try {
                const response = await fetch(`./surface_approche_geojson/dxf_surfaces/${olsFiles[i]}`);
                const geojsonData = await response.json();
                
                geojsonData.features.forEach((feature, featureIndex) => {
                    let entity;
                    
                    if (feature.geometry.type === 'Polygon') {
                        entity = this.viewer.entities.add({
                            name: `OLS: ${olsFiles[i].replace('.geojson', '')} - ${featureIndex + 1}`,
                            polygon: {
                                hierarchy: feature.geometry.coordinates[0].map(coord => 
                                    Cesium.Cartesian3.fromDegrees(coord[0], coord[1], 0)
                                ),
                                material: colors[i],
                                outline: true,
                                outlineColor: colors[i].withAlpha(1.0),
                                height: 0
                            },
                            show: this.surfaceVisibility.ols
                        });
                    } else if (feature.geometry.type === 'LineString') {
                        entity = this.viewer.entities.add({
                            name: `OLS Line: ${olsFiles[i].replace('.geojson', '')} - ${featureIndex + 1}`,
                            polyline: {
                                positions: feature.geometry.coordinates.map(coord => 
                                    Cesium.Cartesian3.fromDegrees(coord[0], coord[1], 0)
                                ),
                                material: colors[i],
                                width: 3,
                                clampToGround: true
                            },
                            show: this.surfaceVisibility.ols
                        });
                    }
                    
                    if (entity) allEntities.push(entity);
                });
                
                console.log(`✅ Loaded OLS surface: ${olsFiles[i]}`);
            } catch (error) {
                console.error(`❌ Error loading ${olsFiles[i]}:`, error);
            }
        }

        this.loadedSurfaces.dxf = allEntities;
        return allEntities;
    }

    // Load buildings from OSM data
    async loadBuildings() {
        try {
            const response = await fetch('./surface_approche_geojson/reseaux/gis_osm_buildings_a_free_1.geojson');
            const geojsonData = await response.json();
            
            const entities = [];
            let count = 0;
            const maxBuildings = 1000; // Limit for performance
            
            for (const feature of geojsonData.features) {
                if (count >= maxBuildings) break;
                
                const entity = this.viewer.entities.add({
                    name: `Building: ${feature.properties.name || 'Unnamed'}`,
                    polygon: {
                        hierarchy: feature.geometry.coordinates[0].map(coord => 
                            Cesium.Cartesian3.fromDegrees(coord[0], coord[1])
                        ),
                        material: Cesium.Color.LIGHTGRAY.withAlpha(0.8),
                        outline: true,
                        outlineColor: Cesium.Color.DARKGRAY,
                        extrudedHeight: Math.random() * 20 + 5, // Random building height
                        height: 0
                    },
                    show: this.surfaceVisibility.buildings
                });
                entities.push(entity);
                count++;
            }
            
            this.loadedSurfaces.reseaux.push(...entities);
            console.log(`✅ Loaded ${entities.length} buildings`);
            return entities;
        } catch (error) {
            console.error('❌ Error loading buildings:', error);
            return [];
        }
    }

    // Load roads from OSM data
    async loadRoads() {
        try {
            const response = await fetch('./surface_approche_geojson/reseaux/gis_osm_roads_free_1.geojson');
            const geojsonData = await response.json();
            
            const entities = [];
            let count = 0;
            const maxRoads = 500; // Limit for performance
            
            for (const feature of geojsonData.features) {
                if (count >= maxRoads) break;
                
                const entity = this.viewer.entities.add({
                    name: `Road: ${feature.properties.name || feature.properties.fclass}`,
                    polyline: {
                        positions: feature.geometry.coordinates.map(coord => 
                            Cesium.Cartesian3.fromDegrees(coord[0], coord[1])
                        ),
                        material: this.getRoadColor(feature.properties.fclass),
                        width: this.getRoadWidth(feature.properties.fclass),
                        clampToGround: true
                    },
                    show: this.surfaceVisibility.roads
                });
                entities.push(entity);
                count++;
            }
            
            this.loadedSurfaces.reseaux.push(...entities);
            console.log(`✅ Loaded ${entities.length} roads`);
            return entities;
        } catch (error) {
            console.error('❌ Error loading roads:', error);
            return [];
        }
    }

    // Helper function to get road color based on type
    getRoadColor(roadClass) {
        const colors = {
            'motorway': Cesium.Color.RED,
            'trunk': Cesium.Color.ORANGE,
            'primary': Cesium.Color.YELLOW,
            'secondary': Cesium.Color.LIGHTBLUE,
            'tertiary': Cesium.Color.LIGHTGREEN,
            'residential': Cesium.Color.LIGHTGRAY,
            'service': Cesium.Color.GRAY
        };
        return colors[roadClass] || Cesium.Color.WHITE;
    }

    // Helper function to get road width based on type
    getRoadWidth(roadClass) {
        const widths = {
            'motorway': 8,
            'trunk': 6,
            'primary': 5,
            'secondary': 4,
            'tertiary': 3,
            'residential': 2,
            'service': 1
        };
        return widths[roadClass] || 1;
    }

    // Toggle surface visibility
    toggleSurfaceVisibility(surfaceType) {
        this.surfaceVisibility[surfaceType] = !this.surfaceVisibility[surfaceType];
        const isVisible = this.surfaceVisibility[surfaceType];
        
        switch (surfaceType) {
            case 'approach':
                this.loadedSurfaces.approach.forEach(entity => entity.show = isVisible);
                break;
            case 'ols':
                this.loadedSurfaces.dxf.forEach(entity => entity.show = isVisible);
                break;
            case 'buildings':
            case 'roads':
                this.loadedSurfaces.reseaux.forEach(entity => {
                    if ((surfaceType === 'buildings' && entity.name.includes('Building')) ||
                        (surfaceType === 'roads' && entity.name.includes('Road'))) {
                        entity.show = isVisible;
                    }
                });
                break;
        }
        
        return isVisible;
    }

    // Load all surfaces
    async loadAllSurfaces() {
        console.log('🔄 Loading all surface data...');
        
        try {
            await this.loadApproachSurface();
            await this.loadOLSSurfaces();
            // await this.loadBuildings(); // Uncomment to load buildings
            // await this.loadRoads(); // Uncomment to load roads
            
            console.log('✅ All surfaces loaded successfully!');
            return true;
        } catch (error) {
            console.error('❌ Error loading surfaces:', error);
            return false;
        }
    }

    // Get surface statistics
    getSurfaceStats() {
        return {
            approach: this.loadedSurfaces.approach.length,
            dxf: this.loadedSurfaces.dxf.length,
            reseaux: this.loadedSurfaces.reseaux.length,
            total: this.loadedSurfaces.approach.length + 
                   this.loadedSurfaces.dxf.length + 
                   this.loadedSurfaces.reseaux.length
        };
    }
}

// Export for use in other scripts
window.SurfaceLoader = SurfaceLoader;
