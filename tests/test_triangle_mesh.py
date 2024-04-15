import numpy as np

from morphosurfaces import TriangleMesh


def test_triangle_mesh_from_arrays():
    vertices = np.array([[10, 0, 0], [10, 10, 10], [10, 0, 10], [10, 10, 0]])
    faces = np.array([[0, 1, 2], [1, 2, 3]])
    mesh = TriangleMesh.from_arrays(vertices=vertices, faces=faces)

    np.testing.assert_array_equal(mesh.vertices, vertices)
    np.testing.assert_array_equal(mesh.faces, faces)


def test_triangle_mesh_from_arrays_with_vertex_array():
    rng = np.random.default_rng(42)

    vertices = np.array([[10, 0, 0], [10, 10, 10], [10, 0, 10], [10, 10, 0]])
    faces = np.array([[0, 1, 2], [1, 2, 3]])
    vertex_normals = rng.random((vertices.shape[0], vertices.shape[1]))
    normals_key = "normal"
    mesh = TriangleMesh.from_arrays(
        vertices=vertices, faces=faces, vertex_arrays={normals_key: vertex_normals}
    )

    # check that the face array was added correctly
    np.testing.assert_allclose(mesh.vertex_arrays[normals_key], vertex_normals)

    # test that this didn't impact the face normals
    np.testing.assert_array_equal(mesh.vertices, vertices)
    np.testing.assert_array_equal(mesh.faces, faces)


def test_triangle_mesh_from_arrays_with_face_array():
    rng = np.random.default_rng(42)

    vertices = np.array([[10, 0, 0], [10, 10, 10], [10, 0, 10], [10, 10, 0]])
    faces = np.array([[0, 1, 2], [1, 2, 3]])
    face_normals = rng.random((faces.shape[0], faces.shape[1]))
    normals_key = "normals"
    mesh = TriangleMesh.from_arrays(
        vertices=vertices, faces=faces, face_arrays={normals_key: face_normals}
    )

    # check that the face array was added correctly
    np.testing.assert_allclose(mesh.face_arrays[normals_key], face_normals)

    # test that this didn't impact the face normals
    np.testing.assert_array_equal(mesh.vertices, vertices)
    np.testing.assert_array_equal(mesh.faces, faces)
