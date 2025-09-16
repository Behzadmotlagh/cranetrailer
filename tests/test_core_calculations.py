import unittest
from backend.core_calculations import (
    compute_tipping_moment,
    compute_center_of_gravity,
    compute_axle_loads,
    estimate_swl
)

class TestCoreCalculations(unittest.TestCase):
    def test_tipping_moment(self):
        result = compute_tipping_moment(30)
        expected = 1000 * 9.81 * math.cos(math.radians(30)) * 5.0
        self.assertAlmostEqual(result, expected, places=2)

    def test_center_of_gravity(self):
        data = [(500, 2.0), (1000, 4.0)]
        result = compute_center_of_gravity(data)
        expected = (500*2 + 1000*4) / (500+1000)
        self.assertAlmostEqual(result, expected, places=2)

    def test_axle_loads(self):
        cg = 3.0
        total_mass = 1500
        wheelbase = 5.0
        front, rear = compute_axle_loads(cg, total_mass, wheelbase)
        self.assertAlmostEqual(front + rear, total_mass, places=2)

    def test_estimate_swl(self):
        result = estimate_swl(45, 6.0)
        self.assertTrue(result > 0)
