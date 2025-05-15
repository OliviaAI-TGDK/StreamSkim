# maharaga_cluster_map.py
# TGDK GeoTrace Aggregator – Maharaga Cluster Module
# Copyright TGDK. All rights reserved.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
import datetime

class MaharagaClusterMap:
    def __init__(self, eps=0.002, min_samples=3):
        self.eps = eps
        self.min_samples = min_samples
        self.entries = []

    def add_point(self, lat, lon, label="unclassified", timestamp=None):
        self.entries.append({
            "coords": [lat, lon],
            "label": label,
            "timestamp": timestamp or datetime.datetime.utcnow().isoformat()
        })

    def cluster_and_plot(self, output_path="maharaga_cluster.png"):
        if not self.entries:
            print("[Maharaga] No entries to cluster.")
            return

        X = np.array([e["coords"] for e in self.entries])
        db = DBSCAN(eps=self.eps, min_samples=self.min_samples).fit(X)
        labels = db.labels_

        unique_labels = set(labels)
        colors = plt.cm.jet(np.linspace(0, 1, len(unique_labels)))

        plt.figure(figsize=(10, 8))
        for k, col in zip(unique_labels, colors):
            if k == -1:
                col = 'k'  # noise
            class_member_mask = (labels == k)
            xy = X[class_member_mask]
            plt.plot(xy[:, 1], xy[:, 0], 'o', markerfacecolor=col,
                     markeredgecolor='k', markersize=8, label=f'Cluster {k}' if k != -1 else "Noise")

        plt.title("Maharaga GeoCluster Map")
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.legend(loc='best')
        plt.grid(True)
        plt.savefig(output_path)
        print(f"[Maharaga] Cluster map saved to {output_path}")

    def export_cluster_data(self):
        return [{"lat": e["coords"][0], "lon": e["coords"][1], "label": e["label"], "timestamp": e["timestamp"]}
                for e in self.entries]

if __name__ == "__main__":
    maha = MaharagaClusterMap()

    # Simulated intake from Duo vectors
    maha.add_point(37.553, -77.460, "sighting")
    maha.add_point(37.556, -77.462, "pattern_match")
    maha.add_point(37.552, -77.459, "gate_contact")
    maha.add_point(37.558, -77.461, "noise")
    maha.add_point(37.557, -77.460, "verified")

    maha.cluster_and_plot()