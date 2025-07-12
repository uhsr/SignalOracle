# test_signaloracle.py
"""
Tests for SignalOracle module.
"""

import unittest
from signaloracle import SignalOracle

class TestSignalOracle(unittest.TestCase):
    """Test cases for SignalOracle class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SignalOracle()
        self.assertIsInstance(instance, SignalOracle)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SignalOracle()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
