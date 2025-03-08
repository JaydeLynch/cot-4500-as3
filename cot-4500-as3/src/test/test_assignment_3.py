import unittest
from src.main.assignment_3 import euler_method, runge_kutta_4th_order

class TestNumericalMethods(unittest.TestCase):
    def test_euler_method(self):
        def f(t, y): #define function
            return t - y**2
        #Parameters
        t0 = 0
        y0 = 1
        h = 0.2
        n = 10

        #Run Euler method
        t, y = euler_method(f, t0, y0, h, n)
        self.assertAlmostEqual(y[-1], 1.2446380979332121, places=10) #check final value of your at t=2
    
    def test_runge_kutta_4th_order(self):
        def f(t, y): #define function
            return t - y**2
       
        #Parameters
        t0 = 0
        y0 = 1
        h = 0.2
        n = 10
        
        # Run Runge-Kutta 4th order method
        t, y = runge_kutta_4th_order(f, t0, y0, h, n)
        self.assertAlmostEqual(y[-1], 1.251316587879806, places=10)# Check the final value of y at t=2

if __name__ == "__main__":
    unittest.main()
