from .types import DataItem
from typing import List, Dict, Any

def structure_data(data: List[Dict[str, Any]]) -> List[DataItem]:
    """_summary_

    Args:
        data (List[Dict[str, Any]]): _description_

    Returns:
        List[Data]: _description_
    """
    
    return [DataItem(**x) for x in data]
