# mahadevi_trace_geometry.py
# TGDK Predictive Geometry Engine – Mahadevi
# Copyright TGDK. All rights reserved.

import numpy as np
from scipy.spatial import ConvexHull, distance_matrix
import matplotlib.pyplot as plt

class MahadeviTraceGeometry:
    def __init__(self):
        self.points = []
        self.labels = []

    def ingest(self, lat, lon, label="unclassified"):
        self.points.append((lat, lon))
        self.labels.append(label)

    def generate_convex_hull(self):
        if len(self.points) < 3:
            print("[Mahadevi] Not enough points for convex geometry.")
            return None
        coords = np.array(self.points)
        hull = ConvexHull(coords)
        return hull

    def plot_geometry(self, output_path="mahadevi_geometry.png"):
        if len(self.points) < 3:
            print("[Mahadevi] Insufficient data for plotting geometry.")
            return

        coords = np.array(self.points)
        hull = self.generate_convex_hull()
        plt.figure(figsize=(10, 8))
        plt.plot(coords[:, 1], coords[:, 0], 'o', label="Trace Points")

        # Convex hull boundary
        for simplex in hull.simplices:
            plt.plot(coords[simplex, 1], coords[simplex, 0], 'k--')

        # Annotate labels
        for i, label in enumerate(self.labels):
            plt.annotate(label, (coords[i][1], coords[i][0]))

        plt.title("Mahadevi Predictive Geometry Trace")
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.grid(True)
        plt.savefig(output_path)
        print(f"[Mahadevi] Geometry trace saved to {output_path}")

    def pairwise_distances(self):
        if len(self.points) < 2:
            print("[Mahadevi] Not enough points for distance computation.")
            return []
        coords = np.array(self.points)
        return distance_matrix(coords, coords)

if __name__ == "__main__":
    mahadevi = MahadeviTraceGeometry()

    # Sample geospatial input
    mahadevi.ingest(37.551, -77.451, "lead1")
    mahadevi.ingest(37.554, -77.454, "lead2")
    mahadevi.ingest(37.550, -77.456, "incident")
    mahadevi.ingest(37.553, -77.455, "signal")
    mahadevi.ingest(37.552, -77.453, "relay")

    mahadevi.plot_geometry()
    distances = mahadevi.pairwise_distances()