from .data_loader import DataLoader
from .exporter import Exporter
from .transform import transform_pipeline


class Pipeline:
    def run(self, loader: DataLoader, exporter: Exporter):

        # import
        data = loader.load("data/input.json")

        # transform logic here
        print(f"Transforming {len(data)} data points...")
        data = transform_pipeline(data)
        print(f"Filtered: {len(data)} remaining rows")
        
        # export
        exporter.save(data, "data/output.json")
        print("pipeline run successfully")
