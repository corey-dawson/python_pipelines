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

def transform_pipeline(data: List[Dict[str, Any]]) -> List[DataItem]:
    """function that runs all the transform steps

    Args:
        data (List[Dict[str, Any]]): input json data

    Returns:
        List[DataItem]: outputted structured and transformed data
    """
    data = structure_data(data)
    data = [x for x in data if x.value > 50]
    return data
