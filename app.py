
import streamlit as st
from solve_integral_page import solve_integral_page
from about_integrals_page import about_integrals_page
from history_of_integrals_page import history_of_integrals_page

def main():
    st.title("Integral Solver and Area Calculator")
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    pages = ["Solve Integral", "About Integrals", "History of Integrals"]
    choice = st.sidebar.selectbox("Go to", pages)
    
    if choice == "Solve Integral":
        solve_integral_page()
    elif choice == "About Integrals":
        about_integrals_page()
    elif choice == "History of Integrals":
        history_of_integrals_page()

if __name__ == "__main__":
    main()
