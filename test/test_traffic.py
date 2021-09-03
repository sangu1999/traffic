import pytest
from app import TrafficLights

traffic_light = TrafficLights()
@pytest.mark.parametrize(
    "test_input,expected")
def test_preprocess_features(test_input, expected):
    assert  traffic_light.mannual_mode(test_input) == expected
