import bpy

# Create a new mesh object for the box
box_mesh = bpy.data.meshes.new("BoxMesh")
box_obj = bpy.data.objects.new("Box", box_mesh)

# Set the vertices and faces of the box mesh
box_verts = [
    (1, 1, 0), (-1, 1, 0), (-1, -1, 0), (1, -1, 0),  # bottom vertices
    (1, 1, 1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1)   # top vertices
]
box_edges = []
box_faces = [
    (0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1),  # bottom, back, left faces
    (1, 5, 6, 2), (2, 6, 7, 3), (4, 0, 3, 7)   # front, right, top faces
]
box_mesh.from_pydata(box_verts, box_edges, box_faces)

# Create a new mesh object for the smaller cover
cover_mesh = bpy.data.meshes.new("CoverMesh")
cover_obj = bpy.data.objects.new("Cover", cover_mesh)

# Set the vertices and faces of the smaller cover mesh
cover_verts = [
    (1, 1, 1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1)   # top vertices of the box
]
cover_edges = []
cover_faces = [
    (0, 1, 2, 3)   # single face covering the top of the box
]
cover_mesh.from_pydata(cover_verts, cover_edges, cover_faces)

# Create a new mesh object for the larger cover
large_cover_mesh = bpy.data.meshes.new("LargeCoverMesh")
large_cover_obj = bpy.data.objects.new("LargeCover", large_cover_mesh)

# Set the vertices and faces of the larger cover mesh
large_cover_verts = [
    (1.2, 1.2, 1.2), (-1.2, 1.2, 1.2), (-1.2, -1.2, 1.2), (1.2, -1.2, 1.2)   # top vertices outside of box
]
large_cover_edges = []
large_cover_faces = [
    (0, 1, 2, 3)   # single face covering the top of the box
]
large_cover_mesh.from_pydata(large_cover_verts, large_cover_edges, large_cover_faces)

# Set the location of the box and covers
box_obj.location = (0, 0, 0)
#cover_obj.location = (0, 0, 1)
large_cover_obj.location = (0, 0, 0.001)

# Link the objects to the scene and make the box active
scene = bpy.context.scene
scene.collection.objects.link(box_obj)
scene.collection.objects.link(cover_obj)
scene.collection.objects.link(large_cover_obj)
scene.view_layers[0].objects.active = box_obj

# Add a material to the box and set its color
box_material = bpy.data.materials.new(name="BoxMaterial")
box_material.diffuse_color = (0.7, 0.5, 0.2)   # dark brown color
