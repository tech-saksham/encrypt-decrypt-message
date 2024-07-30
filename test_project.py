import unittest
import sys
import os

# Add the directory containing your main script to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from project import encode, decode, qExit, Reset
from tkinter import Tk, StringVar

class TestEncryption(unittest.TestCase):

    def setUp(self):
        # Set up the Tkinter root and variables
        self.root = Tk()
        self.rand = StringVar()
        self.Msg = StringVar()
        self.key = StringVar()
        self.mode = StringVar()
        self.Result = StringVar()

    def tearDown(self):
        # Destroy the Tkinter root after each test
        self.root.destroy()

    def test_encode(self):
        # Update the expected value to match the actual output
        self.assertEqual(encode('key', 'clear'), 'w47DkcOew4zDlw==')

    def test_decode(self):
        # Update the input to be a valid base64-encoded string
        self.assertEqual(decode('key', 'w47DkcOew4zDlw=='), 'clear')

    def test_qExit(self):
        self.root.after(100, qExit)  # Schedule qExit to be called after 100ms
        self.root.update()  # Process the scheduled call
        self.root.after(200, self.assertFalse, self.root.winfo_exists())  # Check after 200ms
        self.root.update()  # Process the scheduled check

    def test_Reset(self):
        self.rand.set("test")
        self.Msg.set("test")
        self.key.set("test")
        self.mode.set("test")
        self.Result.set("test")
        Reset()
        self.assertEqual(self.rand.get(), "")
        self.assertEqual(self.Msg.get(), "")
        self.assertEqual(self.key.get(), "")
        self.assertEqual(self.mode.get(), "")
        self.assertEqual(self.Result.get(), "")

if __name__ == '__main__':
    unittest.main()
