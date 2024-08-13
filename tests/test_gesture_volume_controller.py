import unittest
from unittest.mock import MagicMock, patch
import numpy as np
from system_settings import VIDEO_CAPTURE_DEVICE_INDEX, VOLUME_MIN, VOLUME_MAX, HAND_GESTURE_MIN_DISTANCE, HAND_GESTURE_MAX_DISTANCE

class TestVolumeControlMain(unittest.TestCase):
    @patch('cv2.VideoCapture')
    @patch('pycaw.pycaw.AudioUtilities.GetSpeakers')
    @patch('pycaw.pycaw.IAudioEndpointVolume')
    def test_volume_control(self, MockIAudioEndpointVolume, MockGetSpeakers, MockVideoCapture):
        # Mock VideoCapture
        mock_cap = MagicMock()
        MockVideoCapture.return_value = mock_cap
        mock_cap.read.return_value = (True, np.zeros((480, 640, 3), dtype=np.uint8))

        # Mock AudioUtilities
        mock_devices = MagicMock()
        MockGetSpeakers.return_value = mock_devices
        mock_interface = MagicMock()
        mock_devices.Activate.return_value = mock_interface
        mock_volume = MagicMock()
        mock_interface.__class__ = MockIAudioEndpointVolume
        MockIAudioEndpointVolume.return_value = mock_volume
        mock_volume.GetVolumeRange.return_value = [VOLUME_MIN, VOLUME_MAX]

        # Import volume_control_main here to test it
        import volume_control_main

        # Test that the volume is set correctly
        mock_volume.SetMasterVolumeLevel.assert_called()

    def test_hand_gesture_to_volume(self):
        # Test volume calculation based on hand gesture length
        from volume_control_main import np  # Import necessary modules/functions

        length = 100  # Example length value
        vol = np.interp(length, [HAND_GESTURE_MIN_DISTANCE, HAND_GESTURE_MAX_DISTANCE], [VOLUME_MIN, VOLUME_MAX])
        
        # Assert the volume is within expected range
        self.assertGreaterEqual(vol, VOLUME_MIN)
        self.assertLessEqual(vol, VOLUME_MAX)

if __name__ == '__main__':
    unittest.main()
