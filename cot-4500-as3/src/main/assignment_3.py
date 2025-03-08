
def euler_method(f, t0, y0, h, n):
"""
f - derivative func
n-number of iterations
h-step size
"""
    t = np.zeros(n+1)
    y = np.zeros(n+1)
    t[0] = t0 # initialize
    y[0] = y0 #initialize 
    
    for i in range(n):
        y[i+1] = y[i] + h * f(t[i], y[i])
        t[i+1] = t[i] + h
    
    return t, y #returns the array of time points and array of solutions

def runge_kutta_4th_order(f, t0, y0, h, n):
    """
4th-order Runge-Kutta method for solving differential equations.
    
Same  Parameters as previous function
    """
    t = np.zeros(n+1)
    y = np.zeros(n+1)
    t[0] = t0
    y[0] = y0
    
    for i in range(n):
        k1 = h * f(t[i], y[i])
        k2 = h * f(t[i] + h/2, y[i] + k1/2)
        k3 = h * f(t[i] + h/2, y[i] + k2/2)
        k4 = h * f(t[i] + h, y[i] + k3)
        
        y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
        t[i+1] = t[i] + h
    
    return t, y #returns array of time points and array of solutions

#define the main function
def main():
    # Define the function f(t, y) = t - y^2
    def f(t, y):
        return t - y**2
    
    # Parameters
    t0 = 0
    y0 = 1
    t_end = 2
    n = 10
    h = (t_end - t0) / n
    
    # Euler Method
    t_euler, y_euler = euler_method(f, t0, y0, h, n)
    print("Euler Method Result at t=2:", y_euler[-1])
    
    # Runge-Kutta 4th Order Method
    t_rk, y_rk = runge_kutta_4th_order(f, t0, y0, h, n)
    print("Runge-Kutta 4th Order Result at t=2:", y_rk[-1])

if __name__ == "__main__":
    main() # call main function
