from .data_loader import DataLoader
from .exporter import Exporter
from .transform import structure_data


class Pipeline:
    def run(self, loader: DataLoader, exporter: Exporter):

        # import
        data = loader.load("data/input.json")

        # transform logic here
        print(f"Transforming {len(data)} data points...")
        data = structure_data(data)
        data = [x for x in data if x.value > 50]
        print(f"Filtered: {len(data)} remaining rows")
        
        # export
        exporter.save(data, "data/output.json")
        print("pipeline run successfully")
