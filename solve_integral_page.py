import streamlit as st
from sympy import symbols, integrate, sympify, lambdify
import numpy as np
import plotly.graph_objects as go
import re

def preprocess_function_input(function_input):
    """
    Preprocess the input function:
    - Replace ^ with **
    - Add * for implicit multiplication (e.g., 2x -> 2*x)
    """
    function_input = function_input.replace("^", "**")
    function_input = re.sub(r'(\d)([a-zA-Zπ])', r'\1*\2', function_input)  # Add * between number and variable
    return function_input

def solve_integral_page():
    st.header("Solve an Integral")
    
    # Input function
    st.write("Enter the function to integrate (e.g., x^2 + 2x + 1):")
    function_input = st.text_input("Function", value="x^2")
    
    # Input limits
    st.write("Enter the limits of integration:")
    lower_limit = st.number_input("Lower limit", value=0.0)
    upper_limit = st.number_input("Upper limit", value=1.0)
    
    if st.button("Calculate and Plot"):
        try:
            x = symbols('x')
            # Preprocess function input
            preprocessed_function = preprocess_function_input(function_input)
            func = sympify(preprocessed_function)
            
            # Calculate the integral
            area = integrate(func, (x, lower_limit, upper_limit))
            st.success(f"The area under the curve is: {area}")
            
            # Create a numerical version of the function for plotting
            func_lambdified = lambdify(x, func, modules=["numpy"])
            
            # Generate data points
            x_vals = np.linspace(lower_limit - 1, upper_limit + 1, 500)
            y_vals = func_lambdified(x_vals)
            
            # Create the plot
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name='Function'))
            
            # Highlight the area under the curve
            area_x_vals = np.linspace(lower_limit, upper_limit, 500)
            area_y_vals = func_lambdified(area_x_vals)
            fig.add_trace(go.Scatter(x=np.concatenate(([lower_limit], area_x_vals, [upper_limit])),
                                     y=np.concatenate(([0], area_y_vals, [0])),
                                     fill='toself',
                                     name='Area',
                                     mode='lines',
                                     line=dict(width=0),
                                     fillcolor='rgba(0,100,200,0.2)'))
            
            # Update plot layout
            fig.update_layout(
                title="Function and Calculated Area",
                xaxis_title="x",
                yaxis_title="f(x)",
                showlegend=True
            )
            
            # Display the plot
            st.plotly_chart(fig)
            
        except Exception as e:
            st.error(f"An error occurred: {e}")