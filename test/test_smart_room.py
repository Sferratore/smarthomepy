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
        mock_sensor.assert_called_once_with(system.INFRARED_PIN)
        self.assertTrue(result)

    @patch.object(GPIO, "input")
    def test_check_enough_light(self, mock_sensor: Mock):
        mock_sensor.return_value(True)
        system = SmartRoom()
        result = system.check_enough_light()
        mock_sensor.assert_called_once_with(system.PHOTO_PIN)
        self.assertTrue(result)

    @patch.object(GPIO, "output")
    @patch.object(SmartRoom, "check_room_occupancy")
    @patch.object(SmartRoom, "check_enough_light")
    def test_manage_light_level_when_room_occupied_and_not_enough_light(self, mock_light: Mock, mock_occupancy: Mock, mock_output: Mock):
        mock_light.return_value(False)
        mock_occupancy.return_value(True)
        system = SmartRoom()
        mock_output.assert_called_once_with(system.LED_PIN, True)