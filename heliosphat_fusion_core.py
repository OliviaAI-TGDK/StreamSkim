# heliosphat_fusion_core.py
# HeliosPhat Fusion Core – TGDK Seal Center
# Copyright TGDK. All rights reserved.

import json
import time
from mahadevi_trace_geometry import MahadeviTraceGeometry
from maharaga_cluster_map import MaharagaClusterMap
from duo_vector_predictor import DuoVectorPredictor

class HeliosPhatFusionCore:
    def __init__(self):
        self.geometry_engine = MahadeviTraceGeometry()
        self.cluster_engine = MaharagaClusterMap()
        self.vector_engine = DuoVectorPredictor()
        self.event_log = []

    def ingest_signal(self, lat, lon, label, vector=None):
        self.geometry_engine.ingest(lat, lon, label)
        self.cluster_engine.add_point((lat, lon))
        if vector:
            self.vector_engine.record_vector(label, vector)
        self._log_event(f"[Ingested] {label} at ({lat}, {lon})")

    def run_analysis(self):
        self._log_event("[Fusion] Initiating predictive triangulation.")
        self.geometry_engine.plot_geometry()
        centroids = self.cluster_engine.compute_clusters()
        predictions = self.vector_engine.predict_missing_links()

        fused_data = {
            "centroids": centroids,
            "predictions": predictions
        }

        self._log_event("[Fusion] Prediction matrix synthesized.")
        return fused_data

    def export_snapshot(self, output_path="fusion_snapshot.json"):
        snapshot = {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "log": self.event_log
        }
        with open(output_path, "w") as f:
            json.dump(snapshot, f, indent=4)
        print(f"[HeliosPhat] Snapshot saved: {output_path}")

    def _log_event(self, message):
        timestamp = time.strftime("%H:%M:%S", time.gmtime())
        entry = f"{timestamp} | {message}"
        print(entry)
        self.event_log.append(entry)

if __name__ == "__main__":
    fusion = HeliosPhatFusionCore()

    # Example signals (can be replaced with real scan inputs)
    fusion.ingest_signal(37.551, -77.451, "initial_sighting", vector=[0.75, 0.4])
    fusion.ingest_signal(37.555, -77.457, "bluepill_lock", vector=[0.73, 0.42])
    fusion.ingest_signal(37.556, -77.455, "incident_zone", vector=[0.78, 0.38])

    data = fusion.run_analysis()
    fusion.export_snapshot()