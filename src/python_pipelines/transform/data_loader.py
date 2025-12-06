from typing import Protocol, Dict, Type
from json import load
from pathlib import Path

class DataLoader(Protocol):
    def load(self, file_path: str | Path) -> list | dict:
        ...
        
class JSONLoader:
    def load(self, file_path: str | Path):
        if isinstance(file_path, str):
            path = Path(file_path).resolve()
        else: 
            path = file_path
        with open(path, 'r') as f:
            content = load(f)
        return content

# quick example of another loader option. could have a file laoder and a db loader
class OracleLoader:
    def load(self, file_path: str | None = None):
        # In a real scenario, this would connect to Oracle and query data
        print("Loading data from Oracle... (Not Implemented)")
        return []

# used for argparse selection of laoder
loader_map: Dict[str, Type[DataLoader]] = {
    'json': JSONLoader,
    'oracle': OracleLoader,
}