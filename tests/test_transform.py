import pytest
from python_pipelines.transform import JSONLoader, loader_map
from python_pipelines.transform.types import DataItem
from python_pipelines.transform.transform import structure_data
import json

@pytest.fixture
def data():
    data = [
        {
            "id": 5,
            "value": 33.3,
            "status_code": "OLD"
        },
        {
            "id": 6,
            "value": 77.7,
            "status_code": "NEW"
        },
        {
            "id": 7,
            "value": 99.9,
            "status_code": "NEW"
        }
    ]
    return data

class TestDataLoaders:
    def test_json_loader(self, tmpdir, data):
        """Tests that JSONLoader can correctly load data from a file."""

        # create temp directory and json file
        file_path = tmpdir.join("data.json")
        with open(file_path, "w") as f:
            json.dump(data, f)
        
        # run test
        loader = JSONLoader()
        
        # test sending string for path
        loaded_data = loader.load(str(file_path))
        assert loaded_data == data, "Error loading data using string"
        
        # test sending Path for apth
        loaded_data = loader.load(file_path)
        assert loaded_data == data, "Error loading data using Path"
        
        # load data via the map
        loader = loader_map["json"]()
        loaded_data = loader.load(file_path)
        assert loaded_data == data, "Error loading via loader map"

class TestTransforms:
    def test_structure_data(self, data):
        clean = structure_data(data)
        assert len(clean) == 3
        assert isinstance(clean, list), f"Expected result to be a list, but got {type(clean)}"
        assert all(isinstance(item, DataItem) for item in clean), "Not all elements in the list are instances of DataItem"
