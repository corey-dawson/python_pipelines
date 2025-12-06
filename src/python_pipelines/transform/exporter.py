from typing import Protocol, Optional, Dict, Type
from json import dump
from pathlib import Path

class Exporter(Protocol):
    def save(self, data: any, file_path: Optional[str] = None):
        ...
        
class FileExporter:
    def save(self, data: any, file_path: str):
        path = Path(file_path).resolve()
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w') as f:
            dump(data, f, indent=4)
            
class OracleExporter:
    def save(self, data: any, file_path: Optional[str] = None):
        # In a real scenario, this would connect to Oracle and write data
        print(f"Saving {len(data)} records to Oracle... (Not Implemented)")

class NullExporter:
    def save(self, data: any, file_path: Optional[str] = None):
        print("Skip Export")

# used for argparse selection of exporter
exporter_map: Dict[str, Type[Exporter]] = {
    'file': FileExporter,
    'oracle': OracleExporter,
    'skip': NullExporter
}
