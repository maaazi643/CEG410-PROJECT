import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# # Styling
# from streamlit_lottie import st_lottie
# import requests
# import time



# Apply custom CSS styles
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
        
        * {
            font-family: 'Inter', sans-serif;
            color: white;
        }
        .stApp {
            background-color: #1e1e2e;
            color: white;
        }
        .stButton>button {
            background-color: #FF5733;
            color: white;
            border-radius: 10px;
            font-size: 18px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #C70039;
        }
        .stRadio label, .stNumberInput label, .stSelectbox label {
            color: white !important;
            font-weight: 600;
        }
    </style>
    """, unsafe_allow_html=True)



# Function to calculate Shear and Bending Moment for Beams with UDL
def beam_moment_shear(L, w):
    x = np.linspace(0, L, 100)
    shear_force = w * (L/2 - x)
    bending_moment = (w/2) * x * (L - x)
    return x, shear_force, bending_moment

# Function to calculate Shear and Bending Moment for Beams with Point Load
def beam_moment_shear_point(L, P, a):
    x = np.linspace(0, L, 100)
    shear_force = np.piecewise(x, [x < a, x >= a], [lambda x: P, lambda x: 0])
    bending_moment = np.piecewise(x, [x < a, x >= a], [lambda x: P * x, lambda x: P * a])
    return x, shear_force, bending_moment

# Function to calculate Shear and Bending Moment for Frames with UDL
def frame_moment_shear(L, w, h):
    x = np.linspace(0, L, 100)
    shear_force = w * (L/2 - x)
    bending_moment = (w/2) * x * (L - x)
    return x, shear_force, bending_moment

# Function to calculate Shear and Bending Moment for Frames with Point Load
def frame_moment_shear_point(L, P, a, h):
    x = np.linspace(0, L, 100)
    shear_force = np.piecewise(x, [x < a, x >= a], [lambda x: P, lambda x: 0])
    bending_moment = np.piecewise(x, [x < a, x >= a], [lambda x: P * x, lambda x: P * a])
    return x, shear_force, bending_moment

# Streamlit UI
st.title("Beam & Frame Analysis Calculator")
st.markdown("Select structure type and loading conditions.")

# Toggle between Beam and Frame Analysis
structure_type = st.radio("Select Structure Type", ["Beam", "Frame"], key="structure_type")

if structure_type == "Beam" or structure_type == "Frame":
    st.subheader(f"{structure_type} Analysis")
    num_spans = st.number_input("Number of Spans/Members", min_value=1, value=1, step=1)
    L_values = []
    load_values = []
    load_types = []
    load_positions = []
    height_values = [] if structure_type == "Frame" else None

    for i in range(num_spans):
        st.subheader(f"Span/Member {i+1} Properties")
        L = st.number_input(f"Enter Length of Span/Member {i+1} (meters)", min_value=0.1, value=5.0, step=0.1)
        load_type = st.selectbox(f"Select Load Type for Span/Member {i+1}", ["UDL", "Point Load"])
        if structure_type == "Frame":
            h = st.number_input(f"Enter Height of Member {i+1} (meters)", min_value=0.1, value=3.0, step=0.1)
            height_values.append(h)
        if load_type == "UDL":
            w = st.number_input(f"Enter UDL Intensity (kN/m) for Span/Member {i+1}", min_value=0.1, value=10.0, step=0.1)
            load_values.append(w)
            load_positions.append(None)
        elif load_type == "Point Load":
            P = st.number_input(f"Enter Point Load Magnitude (kN) for Span/Member {i+1}", min_value=0.1, value=10.0, step=0.1)
            a = st.number_input(f"Enter Distance from Left End to Point Load (m) for Span/Member {i+1}", min_value=0.1, value=2.5, step=0.1)
            load_values.append(P)
            load_positions.append(a)
        load_types.append(load_type)
        L_values.append(L)

    if st.button("Calculate"):
        st.subheader(f"{structure_type} Analysis Results")
        fig, ax = plt.subplots(2, 1, figsize=(8, 6))
        
        x_combined = np.array([])
        shear_combined = np.array([])
        moment_combined = np.array([])
        offset = 0
        
        for i, (L, load_type, load_value, load_position) in enumerate(zip(L_values, load_types, load_values, load_positions)):
            if structure_type == "Beam":
                if load_type == "UDL":
                    x, shear_force, bending_moment = beam_moment_shear(L, load_value)
                elif load_type == "Point Load":
                    x, shear_force, bending_moment = beam_moment_shear_point(L, load_value, load_position)
            else:
                h = height_values[i]
                if load_type == "UDL":
                    x, shear_force, bending_moment = frame_moment_shear(L, load_value, h)
                elif load_type == "Point Load":
                    x, shear_force, bending_moment = frame_moment_shear_point(L, load_value, load_position, h)
            
            x += offset
            x_combined = np.concatenate((x_combined, x))
            shear_combined = np.concatenate((shear_combined, shear_force))
            moment_combined = np.concatenate((moment_combined, bending_moment))
            offset += L
        
        ax[0].plot(x_combined, shear_combined, label="Shear Force")
        ax[1].plot(x_combined, moment_combined, label="Bending Moment")
        
        ax[0].set_title("Shear Force Diagram")
        ax[0].set_ylabel("Shear Force (kN)")
        ax[0].legend()
        ax[0].grid()
        
        ax[1].set_title("Bending Moment Diagram")
        ax[1].set_xlabel("Structure Length (m)")
        ax[1].set_ylabel("Bending Moment (kNm)")
        ax[1].legend()
        ax[1].grid()
        
        st.pyplot(fig)
        st.success(f"{structure_type} analysis complete!")



