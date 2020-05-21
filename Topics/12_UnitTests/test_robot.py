import unittest

from robot import Robot

class TestRobot(unittest.TestCase):
    
    def test_testing(self):
        pass
    
    def test_robot_name(self):
        rob = Robot('R2D2')
        n = rob.get_name()
        self.assertTrue(n=='R2D2')
    
    