# %%
import napari
import networkx as nx
import numpy as np
import polars as pl
from scipy import spatial

df = pl.read_csv(r"C:\Users\hessm\Documents\Programming\Python\zfish\zfish\features\ccp\Ccp_cycle10.csv")
df_one = df.filter(pl.col('roi')=='G03_px+2426_py-0008')

def delaunay_neighborhood(points):
    delaunay = spatial.Delaunay(points)
    G = nx.Graph()
    for path in delaunay.simplices:
        nx.add_path(G, path)
    adjacency_matrix = nx.adjacency_matrix(G).todense()
    order_points = points[np.array(G.nodes())]
    distance_matrix = spatial.distance_matrix(order_points, order_points)
    return order_points, adjacency_matrix, distance_matrix

points = df_one[sorted(df_one.select('^Centroid-[xyz]$').columns, reverse=True)].to_numpy()
points, adj, dists = delaunay_neighborhood(points)

# %%
vectors = (np.expand_dims(points, 0) - np.expand_dims(points, 1))

feature = points[:, 0] + points[:, 1]
feature = feature / feature.max()

feature_diff = np.expand_dims(feature, 0) - np.expand_dims(feature, 1)
# %%
adjacent_vectors = vectors * np.expand_dims(adj, -1)
# %%
grad = (adjacent_vectors * np.expand_dims(feature_diff, -1)).sum(axis=0)
# %%
norm = np.linalg.norm(grad, axis=1, keepdims=True)

grad_n = grad / norm

grad_vecs = np.stack([points, grad_n], axis=1)
# %%
viewer = napari.Viewer()
viewer.add_points(points, features={'feature': feature}, face_color='feature', size=5)
viewer.add_vectors(grad_vecs, features={'norm': norm.squeeze()}, edge_color='norm', edge_colormap='viridis', length=10)
