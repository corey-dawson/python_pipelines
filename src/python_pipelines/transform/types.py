from dataclasses import dataclass

# create dataclass based on json data under tehe data direectory@dataclass
@dataclass
class DataItem:
    id: int
    value: float
    status_code: str

