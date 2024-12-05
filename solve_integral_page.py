
import streamlit as st
from sympy import symbols, integrate, sympify

def solve_integral_page():
    st.header("Solve an Integral")
    
    # Input function
    st.write("Enter the function to integrate (e.g., x**2 + 2*x + 1):")
    function_input = st.text_input("Function", value="x**2")
    
    # Input limits
    st.write("Enter the limits of integration:")
    lower_limit = st.number_input("Lower limit", value=0.0)
    upper_limit = st.number_input("Upper limit", value=1.0)
    
    if st.button("Calculate"):
        try:
            x = symbols('x')
            func = sympify(function_input)
            result = integrate(func, (x, lower_limit, upper_limit))
            st.success(f"The area under the curve is: {result}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
