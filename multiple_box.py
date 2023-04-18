import bpy
import random

# Create a new mesh object for the box
mesh = bpy.data.meshes.new("BoxMesh")
obj = bpy.data.objects.new("Box", mesh)

# Set the vertices and faces of the box mesh
verts = [(1, 1, 0), (-1, 1, 0), (-1, -1, 0), (1, -1, 0),  # bottom vertices
         (1, 1, 1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1)]  # top vertices
edges = []
faces = [(0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1),  # bottom, back, left faces
         (1, 5, 6, 2), (2, 6, 7, 3), (4, 0, 3, 7)]  # front, right, top faces
mesh.from_pydata(verts, edges, faces)

# Create 3 boxes
for i in range(3):
    # Create a new mesh object for the box
    mesh = bpy.data.meshes.new("BoxMesh")
    obj = bpy.data.objects.new("Box", mesh)

    # Set the vertices and faces of the box mesh with random position
    x, y, z = random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(0, 2)
    verts = [(1, 1, 0), (-1, 1, 0), (-1, -1, 0), (1, -1, 0),  # bottom vertices
             (1, 1, 1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1)]  # top vertices
    for v in verts:
        v = (v[0] + x, v[1] + y, v[2] + z)
    edges = []
    faces = [(0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1),  # bottom, back, left faces
             (1, 5, 6, 2), (2, 6, 7, 3), (4, 0, 3, 7)]  # front, right, top faces
    mesh.from_pydata(verts, edges, faces)

    # Set the location of the box
    obj.location = (x, y, z)

    # Link the object to the scene
    scene = bpy.context.scene
    scene.collection.objects.link(obj)
