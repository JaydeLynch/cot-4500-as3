{\rtf1\ansi\ansicpg1252\cocoartf2820
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 \
### `src/test/test_assignment_3.py`\
\
```python\
import unittest\
from src.main.assignment_3 import euler_method, runge_kutta_4th_order\
\
class TestNumericalMethods(unittest.TestCase):\
    def test_euler_method(self):\
        def f(t, y):\
            return t - y**2\
        \
        t0 = 0\
        y0 = 1\
        h = 0.2\
        n = 10\
        \
        t, y = euler_method(f, t0, y0, h, n)\
        self.assertAlmostEqual(y[-1], 1.2446380979332121, places=10)\
    \
    def test_runge_kutta_4th_order(self):\
        def f(t, y):\
            return t - y**2\
        \
        t0 = 0\
        y0 = 1\
        h = 0.2\
        n = 10\
        \
        t, y = runge_kutta_4th_order(f, t0, y0, h, n)\
        self.assertAlmostEqual(y[-1], 1.251316587879806, places=10)\
\
if __name__ == "__main__":\
    unittest.main()}