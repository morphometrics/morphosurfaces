"""Classes for working with meshes."""

from typing import Dict, Optional, Union

import anndata as ad
import numpy as np
import pandas as pd
import scipy

from morphosurfaces.constants import FACES_KEY, VERTICES_KEY


class TriangleMesh:
    """Triangular mesh with annotations."""

    def __init__(self, vertex_data: ad.AnnData, face_data: ad.AnnData):
        self._vertices = vertex_data
        self._faces = face_data

    @property
    def vertices(self) -> np.ndarray:
        """The coordinates of each vertex in the mesh."""
        return self._vertices.obsm[VERTICES_KEY]

    @property
    def faces(self) -> np.ndarray:
        """The indices of the vertex for each face in the mesh."""
        return self._faces.obsm[FACES_KEY]

    @property
    def vertex_features(self) -> pd.DataFrame:
        """Features for each vertex."""
        return self._vertices.obs

    @property
    def face_features(self) -> Dict[str, Union[np.ndarray, scipy.sparse.spmatrix]]:
        """Features for each face."""
        return self._faces.obs

    @property
    def vertex_arrays(self) -> Dict[str, np.ndarray]:
        """Arrays that annotate each vertex.

        For example, this might be used for vertex normals.
        """
        return self._vertices.obsm

    @property
    def face_arrays(self) -> Dict[str, np.ndarray]:
        """Arrays that annotate each face.

        For example, this might be used for face normals.
        """
        return self._faces.obsm

    @property
    def vertex_graphs(self) -> Dict[str, Union[np.ndarray, scipy.sparse.spmatrix]]:
        """Graphs where each node is a vertex."""
        return self._vertices.obsp

    @property
    def face_graphs(self) -> Dict[str, Union[np.ndarray, scipy.sparse.spmatrix]]:
        """Graphs where each face is a vertex."""
        return self._faces.obsp

    @classmethod
    def from_arrays(
        cls,
        vertices: np.ndarray,
        faces: np.ndarray,
        vertex_features: Optional[pd.DataFrame] = None,
        face_features: Optional[pd.DataFrame] = None,
        vertex_arrays: Optional[Dict[str, np.ndarray]] = None,
        face_arrays: Optional[Dict[str, np.ndarray]] = None,
        vertex_graphs: Optional[
            Dict[str, Union[np.ndarray, scipy.sparse.spmatrix]]
        ] = None,
        face_graphs: Optional[
            Dict[str, Union[np.ndarray, scipy.sparse.spmatrix]]
        ] = None,
    ):
        """Create a mesh from data."""
        # make the vertex data
        if vertex_arrays is None:
            vertex_arrays = {}
        vertex_arrays.update({VERTICES_KEY: vertices})
        vertex_data = ad.AnnData(
            obsm=vertex_arrays, obs=vertex_features, obsp=vertex_graphs
        )

        # make the face data
        if face_arrays is None:
            face_arrays = {}
        face_arrays.update({FACES_KEY: faces})
        face_data = ad.AnnData(obsm=face_arrays, obs=face_features, obsp=face_graphs)

        return cls(vertex_data=vertex_data, face_data=face_data)
