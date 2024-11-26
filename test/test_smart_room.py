import unittest
import mock.GPIO as GPIO
from unittest.mock import patch, PropertyMock
from unittest.mock import Mock

from mock.adafruit_bmp280 import Adafruit_BMP280_I2C
from src.smart_room import SmartRoom
from mock.senseair_s8 import SenseairS8


class TestSmartRoom(unittest.TestCase):

    @patch.object(GPIO, "input")
    def test_check_room_occupancy(self, mock_sensor: Mock):
        mock_sensor.return_value(True)
        system = SmartRoom()
        result = system.check_room_occupancy()
        mock_sensor.assert_called_once_with(system.INFRARED_PIN, False)
        self.assertTrue(result)
