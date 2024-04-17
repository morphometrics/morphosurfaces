"""A simple triangular mesh with properties.

The mesh is structured as shown below with vertices v_*
and faces f_*.

    v_0 ----- v_2 ---- v_4
     |       / |      /
     | f_0  /  | f_2 /
     |     /   |    /
     |   / f_1 |  /
     | /       | /
    v_1 ----- v_3

"""

import numpy as np

from morphosurfaces import TriangleMesh

# vertex coordinates
vertices = np.array([[0, 0, 0], [0, 5, 0], [0, 0, 5], [0, 5, 5], [0, 0, 10]])

# face indices
faces = np.array([[0, 1, 2], [1, 3, 2], [2, 3, 4]])

# we define a graph where the graph vertices are
# the mesh vertices and the graph edges connect
# neighboring mesh vertices.
# (i.e., vertex adjacency matrix)
vertex_adjacency = np.array(
    [
        [1, 1, 1, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1],
        [0, 0, 1, 1, 1],
    ]
)

# graphs where the graph vertices are the mesh vertices
# are called "vertex graphs". They are stored in
# a dictionary with string keys
vertex_graphs = {"vertex_adjacency": vertex_adjacency}

# we define a graph where the graph vertices are the mesh faces
# and the graph edges connect adjacent mesh faces.
# (i.e., face adjacency matrix)
face_adjacency = np.array([[1, 1, 0], [1, 1, 1], [0, 1, 1]])

# graphs where the graph vertices are the mesh faces
# are called "face graphs". They are stored in
# a dictionary with string keys.
face_graphs = {"face_adjacency": face_adjacency}

mesh = TriangleMesh.from_arrays(
    vertices=vertices, faces=faces, vertex_graphs=vertex_graphs, face_graphs=face_graphs
)
