# # # # # # import streamlit as st
# # # # # # import matplotlib.pyplot as plt

# # # # # # class EF:
# # # # # #     def __init__(self, L, m0, m1, v0, v1):
# # # # # #         self.L = L
# # # # # #         self.efs = [m0, m1, v0, v1]

# # # # # #     @property
# # # # # #     def m0(self):
# # # # # #         return self.efs[0]

# # # # # #     @property
# # # # # #     def m1(self):
# # # # # #         return self.efs[1]

# # # # # #     @property
# # # # # #     def v0(self):
# # # # # #         return self.efs[2]

# # # # # #     @property
# # # # # #     def v1(self):
# # # # # #         return self.efs[3]

# # # # # # def SD(L, EI, t0, t1, d01=0):
# # # # # #     """Calculate slope deflection based on input parameters."""
# # # # # #     m0 = (EI / L) * (4 * t0 + 2 * t1 - 6 * d01 / L)
# # # # # #     m1 = (EI / L) * (2 * t0 + 4 * t1 - 6 * d01 / L)
# # # # # #     v1 = -(m0 + m1) / L
# # # # # #     v0 = v1
# # # # # #     return EF(L, m0, m1, v0, v1)

# # # # # # # Streamlit UI
# # # # # # st.title("Slope Deflection Calculator")
# # # # # # st.markdown("Enter the required values and click **Calculate**.")

# # # # # # # User Inputs
# # # # # # L = st.number_input("Enter Length (L)", min_value=0.1, value=5.0, step=0.1)
# # # # # # EI = st.number_input("Enter EI (Flexural Rigidity)", min_value=1.0, value=1000.0, step=10.0)
# # # # # # t0 = st.number_input("Enter Rotation at Left (t0)", value=0.1, step=0.01)
# # # # # # t1 = st.number_input("Enter Rotation at Right (t1)", value=0.1, step=0.01)
# # # # # # d01 = st.number_input("Enter Relative Displacement (d01)", value=0.0, step=0.01)

# # # # # # if st.button("Calculate"):
# # # # # #     result = SD(L, EI, t0, t1, d01)

# # # # # #     # Display the results
# # # # # #     st.subheader("Results:")
# # # # # #     st.write(f"**Left Moment (m0):** {result.m0:.4f}")
# # # # # #     st.write(f"**Right Moment (m1):** {result.m1:.4f}")
# # # # # #     st.write(f"**Left Shear (v0):** {result.v0:.4f}")
# # # # # #     st.write(f"**Right Shear (v1):** {result.v1:.4f}")

# # # # # #     # Optional: Plot results (for visualization)
# # # # # #     import matplotlib.pyplot as plt

# # # # # #     fig, ax = plt.subplots()
# # # # # #     ax.bar(["m0", "m1", "v0", "v1"], [result.m0, result.m1, result.v0, result.v1], color=["blue", "red", "green", "purple"])
# # # # # #     ax.set_ylabel("Force / Moment")
# # # # # #     ax.set_title("End Forces Visualization")
# # # # # #     st.pyplot(fig)



# # # # # import streamlit as st
# # # # # import matplotlib.pyplot as plt

# # # # # class EF:
# # # # #     def __init__(self, L, m0, m1, v0, v1):
# # # # #         self.L = L
# # # # #         self.efs = [m0, m1, v0, v1]

# # # # #     @property
# # # # #     def m0(self):
# # # # #         return self.efs[0]

# # # # #     @property
# # # # #     def m1(self):
# # # # #         return self.efs[1]

# # # # #     @property
# # # # #     def v0(self):
# # # # #         return self.efs[2]

# # # # #     @property
# # # # #     def v1(self):
# # # # #         return self.efs[3]

# # # # # def SD(L, EI, t0, t1, d01=0):
# # # # #     """Calculate slope deflection based on input parameters."""
# # # # #     m0 = (EI / L) * (4 * t0 + 2 * t1 - 6 * d01 / L)
# # # # #     m1 = (EI / L) * (2 * t0 + 4 * t1 - 6 * d01 / L)
# # # # #     v1 = -(m0 + m1) / L
# # # # #     v0 = v1
# # # # #     return EF(L, m0, m1, v0, v1)

# # # # # # Streamlit UI
# # # # # st.title("Beam & Frame Analysis Calculator")
# # # # # st.markdown("Select beam properties and loading conditions.")

# # # # # # Step 1: Number of spans
# # # # # num_spans = st.number_input("Number of Spans", min_value=1, value=1, step=1)

# # # # # # Step 2: Type of Supports
# # # # # support_types = ["Fixed", "Pinned", "Roller"]
# # # # # support_start = st.selectbox("Start Support Type", support_types)
# # # # # support_end = st.selectbox("End Support Type", support_types)

# # # # # # Step 3: Load Type
# # # # # load_type = st.radio("Select Load Type", ["Uniformly Distributed Load (UDL)", "Varying Distributed Load (VDL)", "Point Load"])

# # # # # # Step 4: Beam Properties
# # # # # L = st.number_input("Enter Length of Beam (L in meters)", min_value=0.1, value=5.0, step=0.1)
# # # # # EI = st.number_input("Enter EI (Flexural Rigidity)", min_value=1.0, value=1000.0, step=10.0)

# # # # # t0 = st.number_input("Enter Rotation at Left Support (t0)", value=0.1, step=0.01)
# # # # # t1 = st.number_input("Enter Rotation at Right Support (t1)", value=0.1, step=0.01)
# # # # # d01 = st.number_input("Enter Relative Displacement (d01)", value=0.0, step=0.01)

# # # # # # Step 5: Load Details
# # # # # if load_type == "Uniformly Distributed Load (UDL)":
# # # # #     w = st.number_input("Enter UDL Intensity (kN/m)", min_value=0.1, value=10.0, step=0.1)
# # # # #     m0, m1, v0, v1 = -w*L*L/12, w*L*L/12, w*L/2, -w*L/2
# # # # # elif load_type == "Point Load":
# # # # #     P = st.number_input("Enter Point Load (kN)", min_value=0.1, value=10.0, step=0.1)
# # # # #     a = st.number_input("Enter Distance of Load from Left Support (m)", min_value=0.1, value=L/2, step=0.1)
# # # # #     b = L - a
# # # # #     m0, m1 = -P*a*b*b/(L*L), P*a*a*b/(L*L)
# # # # #     v1 = -(m0 + m1 + P*a)/L
# # # # #     v0 = -(m0 + m1 - P*b)/L
# # # # # else:
# # # # #     m0, m1, v0, v1 = 0, 0, 0, 0  # Placeholder for future VDL implementation

# # # # # if st.button("Calculate"):
# # # # #     result = EF(L, m0, m1, v0, v1)
    
# # # # #     # Display the results
# # # # #     st.subheader("Results:")
# # # # #     st.write(f"**Left Moment (m0):** {result.m0:.4f} kN.m")
# # # # #     st.write(f"**Right Moment (m1):** {result.m1:.4f} kN.m")
# # # # #     st.write(f"**Left Shear (v0):** {result.v0:.4f} kN")
# # # # #     st.write(f"**Right Shear (v1):** {result.v1:.4f} kN")
    
# # # # #     # Plot results for visualization
# # # # #     fig, ax = plt.subplots()
# # # # #     ax.bar(["m0", "m1", "v0", "v1"], [result.m0, result.m1, result.v0, result.v1], color=["blue", "red", "green", "purple"])
# # # # #     ax.set_ylabel("Force / Moment (kN or kN.m)")
# # # # #     ax.set_title("End Forces & Moments Visualization")
# # # # #     st.pyplot(fig)


# # # # import streamlit as st
# # # # import matplotlib.pyplot as plt
# # # # import sympy as sp
# # # # import pandas as pd

# # # # class EF:
# # # #     def __init__(self, L, m0, m1, v0, v1):
# # # #         self.L = L
# # # #         self.efs = [m0, m1, v0, v1]

# # # #     @property
# # # #     def m0(self):
# # # #         return self.efs[0]

# # # #     @property
# # # #     def m1(self):
# # # #         return self.efs[1]

# # # #     @property
# # # #     def v0(self):
# # # #         return self.efs[2]

# # # #     @property
# # # #     def v1(self):
# # # #         return self.efs[3]

# # # # def SD(L, EI, t0, t1, d01=0):
# # # #     """Calculate slope deflection based on input parameters."""
# # # #     m0 = (EI / L) * (4 * t0 + 2 * t1 - 6 * d01 / L)
# # # #     m1 = (EI / L) * (2 * t0 + 4 * t1 - 6 * d01 / L)
# # # #     v1 = -(m0 + m1) / L
# # # #     v0 = v1
# # # #     return EF(L, m0, m1, v0, v1)

# # # # # Streamlit UI
# # # # st.title("Beam & Frame Analysis Calculator")
# # # # st.markdown("Select beam properties and loading conditions.")

# # # # # Step 1: Number of spans
# # # # num_spans = st.number_input("Number of Spans", min_value=1, value=1, step=1)

# # # # # Step 2: Type of Supports
# # # # support_types = ["Fixed", "Pinned", "Roller"]
# # # # support_start = st.selectbox("Start Support Type", support_types)
# # # # support_end = st.selectbox("End Support Type", support_types)

# # # # # Step 3: Load Type
# # # # load_type = st.radio("Select Load Type", ["Uniformly Distributed Load (UDL)", "Varying Distributed Load (VDL)", "Point Load"])

# # # # # Step 4: Beam Properties
# # # # L = st.number_input("Enter Length of Beam (L in meters)", min_value=0.1, value=5.0, step=0.1)
# # # # EI = st.number_input("Enter EI (Flexural Rigidity)", min_value=1.0, value=1000.0, step=10.0)

# # # # t0 = st.number_input("Enter Rotation at Left Support (t0)", value=0.1, step=0.01)
# # # # t1 = st.number_input("Enter Rotation at Right Support (t1)", value=0.1, step=0.01)
# # # # d01 = st.number_input("Enter Relative Displacement (d01)", value=0.0, step=0.01)

# # # # # Step 5: Load Details
# # # # if load_type == "Uniformly Distributed Load (UDL)":
# # # #     w = st.number_input("Enter UDL Intensity (kN/m)", min_value=0.1, value=10.0, step=0.1)
# # # #     m0, m1, v0, v1 = -w*L*L/12, w*L*L/12, w*L/2, -w*L/2
# # # # elif load_type == "Point Load":
# # # #     P = st.number_input("Enter Point Load (kN)", min_value=0.1, value=10.0, step=0.1)
# # # #     a = st.number_input("Enter Distance of Load from Left Support (m)", min_value=0.1, value=L/2, step=0.1)
# # # #     b = L - a
# # # #     m0, m1 = -P*a*b*b/(L*L), P*a*a*b/(L*L)
# # # #     v1 = -(m0 + m1 + P*a)/L
# # # #     v0 = -(m0 + m1 - P*b)/L
# # # # else:
# # # #     m0, m1, v0, v1 = 0, 0, 0, 0  # Placeholder for future VDL implementation

# # # # if st.button("Calculate"):
# # # #     result = EF(L, m0, m1, v0, v1)
    
# # # #     # Display the results
# # # #     st.subheader("Results:")
# # # #     st.write(f"**Left Moment (m0):** {result.m0:.4f} kN.m")
# # # #     st.write(f"**Right Moment (m1):** {result.m1:.4f} kN.m")
# # # #     st.write(f"**Left Shear (v0):** {result.v0:.4f} kN")
# # # #     st.write(f"**Right Shear (v1):** {result.v1:.4f} kN")
    
# # # #     # Visualization using Matplotlib & SymPy
# # # #     x = sp.symbols('x')
# # # #     shear_eq = result.v0 + (w * x if load_type == "Uniformly Distributed Load (UDL)" else 0)
# # # #     moment_eq = sp.integrate(shear_eq, x) + result.m0
    
# # # #     x_vals = pd.Series(range(int(L) + 1))
# # # #     shear_vals = x_vals.apply(lambda val: shear_eq.subs(x, val))
# # # #     moment_vals = x_vals.apply(lambda val: moment_eq.subs(x, val))
    
# # # #     fig, ax = plt.subplots(2, 1, figsize=(8, 6))
# # # #     ax[0].plot(x_vals, shear_vals, label="Shear Force", color='blue')
# # # #     ax[0].set_title("Shear Force Diagram")
# # # #     ax[0].set_ylabel("Shear Force (kN)")
# # # #     ax[0].grid()
    
# # # #     ax[1].plot(x_vals, moment_vals, label="Bending Moment", color='red')
# # # #     ax[1].set_title("Bending Moment Diagram")
# # # #     ax[1].set_xlabel("Beam Length (m)")
# # # #     ax[1].set_ylabel("Bending Moment (kN.m)")
# # # #     ax[1].grid()
    
# # # #     st.pyplot(fig)

# # # import streamlit as st
# # # import matplotlib.pyplot as plt
# # # import sympy as sp
# # # import pandas as pd

# # # class EF:
# # #     def __init__(self, L, m0, m1, v0, v1):
# # #         self.L = L
# # #         self.efs = [m0, m1, v0, v1]

# # #     @property
# # #     def m0(self):
# # #         return self.efs[0]

# # #     @property
# # #     def m1(self):
# # #         return self.efs[1]

# # #     @property
# # #     def v0(self):
# # #         return self.efs[2]

# # #     @property
# # #     def v1(self):
# # #         return self.efs[3]

# # # def SD(L, EI, t0, t1, d01=0):
# # #     """Calculate slope deflection based on input parameters."""
# # #     m0 = (EI / L) * (4 * t0 + 2 * t1 - 6 * d01 / L)
# # #     m1 = (EI / L) * (2 * t0 + 4 * t1 - 6 * d01 / L)
# # #     v1 = -(m0 + m1) / L
# # #     v0 = v1
# # #     return EF(L, m0, m1, v0, v1)

# # # # Streamlit UI
# # # st.title("Beam & Frame Analysis Calculator")
# # # st.markdown("Select beam properties and loading conditions.")

# # # # Step 1: Number of spans
# # # num_spans = st.number_input("Number of Spans", min_value=1, value=1, step=1)

# # # # Step 2: Input each span's properties
# # # L_values = []
# # # EI_values = []
# # # load_types = []
# # # load_values = []
# # # load_positions = []
# # # for i in range(num_spans):
# # #     st.subheader(f"Span {i+1} Properties")
# # #     L_values.append(st.number_input(f"Enter Length of Span {i+1} (meters)", min_value=0.1, value=5.0, step=0.1))
# # #     EI_values.append(st.number_input(f"Enter EI for Span {i+1} (Flexural Rigidity)", min_value=1.0, value=1000.0, step=10.0))
    
# # #     load_type = st.radio(f"Select Load Type for Span {i+1}", ["UDL", "Point Load"], key=f"load_type_{i}")
# # #     load_types.append(load_type)
    
# # #     if load_type == "UDL":
# # #         load_values.append(st.number_input(f"Enter UDL Intensity (kN/m) for Span {i+1}", min_value=0.1, value=10.0, step=0.1))
# # #         load_positions.append(None)  # Not needed for UDL
# # #     else:
# # #         load_values.append(st.number_input(f"Enter Point Load (kN) for Span {i+1}", min_value=0.1, value=10.0, step=0.1))
# # #         load_positions.append(st.number_input(f"Enter Load Position (m) from Left End for Span {i+1}", min_value=0.1, value=L_values[i]/2, step=0.1))

# # # if st.button("Calculate"):
# # #     all_results = []
# # #     shear_eqs = []
# # #     moment_eqs = []
# # #     x_vals = []
# # #     shear_vals = []
# # #     moment_vals = []
    
# # #     x = sp.symbols('x')
# # #     for i in range(num_spans):
# # #         L, EI = L_values[i], EI_values[i]
# # #         load_type, load_val, load_pos = load_types[i], load_values[i], load_positions[i]
        
# # #         if load_type == "UDL":
# # #             m0, m1, v0, v1 = -load_val*L*L/12, load_val*L*L/12, load_val*L/2, -load_val*L/2
# # #             shear_eq = v0 + load_val * x
# # #         else:
# # #             a = load_pos
# # #             b = L - a
# # #             m0, m1 = -load_val*a*b*b/(L*L), load_val*a*a*b/(L*L)
# # #             v1 = -(m0 + m1 + load_val*a)/L
# # #             v0 = -(m0 + m1 - load_val*b)/L
# # #             shear_eq = v0 + (load_val if x >= a else 0)
        
# # #         moment_eq = sp.integrate(shear_eq, x) + m0
        
# # #         result = EF(L, m0, m1, v0, v1)
# # #         all_results.append(result)
# # #         shear_eqs.append(shear_eq)
# # #         moment_eqs.append(moment_eq)
        
# # #         span_x_vals = pd.Series(range(int(L) + 1))
# # #         span_shear_vals = span_x_vals.apply(lambda val: shear_eq.subs(x, val))
# # #         span_moment_vals = span_x_vals.apply(lambda val: moment_eq.subs(x, val))
        
# # #         x_vals.append(span_x_vals)
# # #         shear_vals.append(span_shear_vals)
# # #         moment_vals.append(span_moment_vals)
    
# # #     # Plot results for all spans
# # #     fig, ax = plt.subplots(2, 1, figsize=(8, 6))
# # #     for i in range(num_spans):
# # #         ax[0].plot(x_vals[i], shear_vals[i], label=f"Span {i+1} Shear", linestyle="--")
# # #         ax[1].plot(x_vals[i], moment_vals[i], label=f"Span {i+1} Moment", linestyle="--")
    
# # #     ax[0].set_title("Shear Force Diagram")
# # #     ax[0].set_ylabel("Shear Force (kN)")
# # #     ax[0].grid()
# # #     ax[0].legend()
    
# # #     ax[1].set_title("Bending Moment Diagram")
# # #     ax[1].set_xlabel("Beam Length (m)")
# # #     ax[1].set_ylabel("Bending Moment (kN.m)")
# # #     ax[1].grid()
# # #     ax[1].legend()
    
# # #     st.pyplot(fig)

# # # import streamlit as st
# # # import matplotlib.pyplot as plt
# # # import sympy as sp
# # # import pandas as pd

# # # class EF:
# # #     def __init__(self, L, m0, m1, v0, v1):
# # #         self.L = L
# # #         self.efs = [m0, m1, v0, v1]

# # #     @property
# # #     def m0(self):
# # #         return self.efs[0]

# # #     @property
# # #     def m1(self):
# # #         return self.efs[1]

# # #     @property
# # #     def v0(self):
# # #         return self.efs[2]

# # #     @property
# # #     def v1(self):
# # #         return self.efs[3]

# # # def SD(L, EI, t0, t1, d01=0):
# # #     """Calculate slope deflection based on input parameters."""
# # #     m0 = (EI / L) * (4 * t0 + 2 * t1 - 6 * d01 / L)
# # #     m1 = (EI / L) * (2 * t0 + 4 * t1 - 6 * d01 / L)
# # #     v1 = -(m0 + m1) / L
# # #     v0 = v1
# # #     return EF(L, m0, m1, v0, v1)

# # # # Streamlit UI
# # # st.title("Beam & Frame Analysis Calculator")
# # # st.markdown("Select beam properties and loading conditions.")

# # # # Step 1: Number of spans
# # # num_spans = st.number_input("Number of Spans", min_value=1, value=1, step=1)

# # # # Step 2: Input each span's properties
# # # L_values = []
# # # EI_values = []
# # # load_types = []
# # # load_values = []
# # # load_positions = []
# # # for i in range(num_spans):
# # #     st.subheader(f"Span {i+1} Properties")
# # #     L_values.append(st.number_input(f"Enter Length of Span {i+1} (meters)", min_value=0.1, value=5.0, step=0.1))
# # #     EI_values.append(st.number_input(f"Enter EI for Span {i+1} (Flexural Rigidity)", min_value=1.0, value=1000.0, step=10.0))
    
# # #     load_type = st.radio(f"Select Load Type for Span {i+1}", ["UDL", "Point Load"], key=f"load_type_{i}")
# # #     load_types.append(load_type)
    
# # #     if load_type == "UDL":
# # #         load_values.append(st.number_input(f"Enter UDL Intensity (kN/m) for Span {i+1}", min_value=0.1, value=10.0, step=0.1))
# # #         load_positions.append(None)  # Not needed for UDL
# # #     else:
# # #         load_values.append(st.number_input(f"Enter Point Load (kN) for Span {i+1}", min_value=0.1, value=10.0, step=0.1))
# # #         load_positions.append(st.number_input(f"Enter Load Position (m) from Left End for Span {i+1}", min_value=0.1, value=L_values[i]/2, step=0.1))

# # # if st.button("Calculate"):
# # #     all_results = []
# # #     shear_eqs = []
# # #     moment_eqs = []
# # #     x_vals = []
# # #     shear_vals = []
# # #     moment_vals = []
    
# # #     x = sp.symbols('x')
# # #     for i in range(num_spans):
# # #         L, EI = L_values[i], EI_values[i]
# # #         load_type, load_val, load_pos = load_types[i], load_values[i], load_positions[i]
        
# # #         if load_type == "UDL":
# # #             m0, m1, v0, v1 = -load_val*L*L/12, load_val*L*L/12, load_val*L/2, -load_val*L/2
# # #             shear_eq = v0 + load_val * x
# # #         else:
# # #             a = load_pos
# # #             b = L - a
# # #             m0, m1 = -load_val*a*b*b/(L*L), load_val*a*a*b/(L*L)
# # #             v1 = -(m0 + m1 + load_val*a)/L
# # #             v0 = -(m0 + m1 - load_val*b)/L
# # #             shear_eq = v0 + sp.Piecewise((load_val, x >= a), (0, True))
        
# # #         moment_eq = sp.integrate(shear_eq, x) + m0
        
# # #         result = EF(L, m0, m1, v0, v1)
# # #         all_results.append(result)
# # #         shear_eqs.append(shear_eq)
# # #         moment_eqs.append(moment_eq)
        
# # #         span_x_vals = pd.Series(range(int(L) + 1))
# # #         span_shear_vals = span_x_vals.apply(lambda val: shear_eq.subs(x, val))
# # #         span_moment_vals = span_x_vals.apply(lambda val: moment_eq.subs(x, val))
        
# # #         x_vals.append(span_x_vals)
# # #         shear_vals.append(span_shear_vals)
# # #         moment_vals.append(span_moment_vals)
    
# # #     # Plot results for all spans
# # #     fig, ax = plt.subplots(2, 1, figsize=(8, 6))
# # #     for i in range(num_spans):
# # #         ax[0].plot(x_vals[i], shear_vals[i], label=f"Span {i+1} Shear", linestyle="--")
# # #         ax[1].plot(x_vals[i], moment_vals[i], label=f"Span {i+1} Moment", linestyle="--")
    
# # #     ax[0].set_title("Shear Force Diagram")
# # #     ax[0].set_ylabel("Shear Force (kN)")
# # #     ax[0].grid()
# # #     ax[0].legend()
    
# # #     ax[1].set_title("Bending Moment Diagram")
# # #     ax[1].set_xlabel("Beam Length (m)")
# # #     ax[1].set_ylabel("Bending Moment (kN.m)")
# # #     ax[1].grid()
# # #     ax[1].legend()
    
# # #     st.pyplot(fig)



# # # import streamlit as st
# # # import matplotlib.pyplot as plt
# # # import sympy as sp
# # # import pandas as pd

# # # class EF:
# # #     def __init__(self, L, m0, m1, v0, v1):
# # #         self.L = L
# # #         self.efs = [m0, m1, v0, v1]

# # #     @property
# # #     def m0(self):
# # #         return self.efs[0]

# # #     @property
# # #     def m1(self):
# # #         return self.efs[1]

# # #     @property
# # #     def v0(self):
# # #         return self.efs[2]

# # #     @property
# # #     def v1(self):
# # #         return self.efs[3]

# # # # Streamlit UI
# # # st.title("Beam & Frame Analysis Calculator")
# # # st.markdown("Select beam properties and loading conditions.")

# # # # Step 1: Number of spans
# # # num_spans = st.number_input("Number of Spans", min_value=1, value=1, step=1)

# # # # Step 2: Input each span's properties
# # # L_values = []
# # # load_types = []
# # # load_values = []
# # # load_positions = []
# # # for i in range(num_spans):
# # #     st.subheader(f"Span {i+1} Properties")
# # #     L_values.append(st.number_input(f"Enter Length of Span {i+1} (meters)", min_value=0.1, value=5.0, step=0.1))
    
# # #     load_type = st.radio(f"Select Load Type for Span {i+1}", ["UDL", "Point Load"], key=f"load_type_{i}")
# # #     load_types.append(load_type)
    
# # #     if load_type == "UDL":
# # #         load_values.append(st.number_input(f"Enter UDL Intensity (kN/m) for Span {i+1}", min_value=0.1, value=10.0, step=0.1))
# # #         load_positions.append(None)  # Not needed for UDL
# # #     else:
# # #         load_values.append(st.number_input(f"Enter Point Load (kN) for Span {i+1}", min_value=0.1, value=10.0, step=0.1))
# # #         load_positions.append(st.number_input(f"Enter Load Position (m) from Left End for Span {i+1}", min_value=0.1, value=L_values[i]/2, step=0.1))

# # # if st.button("Calculate"):
# # #     all_results = []
# # #     shear_eqs = []
# # #     moment_eqs = []
# # #     total_length = sum(L_values)
# # #     x = sp.symbols('x')
# # #     x_vals = []
# # #     shear_vals = []
# # #     moment_vals = []
    
# # #     current_x_offset = 0  # To merge spans into a single diagram
    
# # #     for i in range(num_spans):
# # #         L = L_values[i]
# # #         load_type, load_val, load_pos = load_types[i], load_values[i], load_positions[i]
        
# # #         if load_type == "UDL":
# # #             m0, m1, v0, v1 = -load_val*L*L/12, load_val*L*L/12, load_val*L/2, -load_val*L/2
# # #             shear_eq = v0 + load_val * (x - current_x_offset)
# # #         else:
# # #             a = load_pos
# # #             b = L - a
# # #             m0, m1 = -load_val*a*b*b/(L*L), load_val*a*a*b/(L*L)
# # #             v1 = -(m0 + m1 + load_val*a)/L
# # #             v0 = -(m0 + m1 - load_val*b)/L
# # #             shear_eq = v0 + sp.Piecewise((load_val, x >= (current_x_offset + a)), (0, True))
        
# # #         moment_eq = sp.integrate(shear_eq, x) + m0
        
# # #         result = EF(L, m0, m1, v0, v1)
# # #         all_results.append(result)
# # #         shear_eqs.append(shear_eq)
# # #         moment_eqs.append(moment_eq)
        
# # #         span_x_vals = pd.Series(range(int(L) + 1)) + current_x_offset
# # #         span_shear_vals = span_x_vals.apply(lambda val: shear_eq.subs(x, val))
# # #         span_moment_vals = span_x_vals.apply(lambda val: moment_eq.subs(x, val))
        
# # #         x_vals.extend(span_x_vals)
# # #         shear_vals.extend(span_shear_vals)
# # #         moment_vals.extend(span_moment_vals)
        
# # #         current_x_offset += L  # Shift x for the next span
    
# # #     # Plot merged results for all spans
# # #     fig, ax = plt.subplots(2, 1, figsize=(8, 6))
# # #     ax[0].plot(x_vals, shear_vals, label="Shear Force", color="blue")
# # #     ax[1].plot(x_vals, moment_vals, label="Bending Moment", color="red")
    
# # #     ax[0].set_title("Shear Force Diagram")
# # #     ax[0].set_ylabel("Shear Force (kN)")
# # #     ax[0].grid()
# # #     ax[0].legend()
    
# # #     ax[1].set_title("Bending Moment Diagram")
# # #     ax[1].set_xlabel("Beam Length (m)")
# # #     ax[1].set_ylabel("Bending Moment (kN.m)")
# # #     ax[1].grid()
# # #     ax[1].legend()
    
# # #     st.pyplot(fig)



# # import streamlit as st
# # import matplotlib.pyplot as plt
# # import sympy as sp
# # import pandas as pd

# # class EF:
# #     def __init__(self, L, m0, m1, v0, v1):
# #         self.L = L
# #         self.efs = [m0, m1, v0, v1]

# #     @property
# #     def m0(self):
# #         return self.efs[0]

# #     @property
# #     def m1(self):
# #         return self.efs[1]

# #     @property
# #     def v0(self):
# #         return self.efs[2]

# #     @property
# #     def v1(self):
# #         return self.efs[3]

# # # Streamlit UI
# # st.title("Beam & Frame Analysis Calculator")
# # st.markdown("Select structure type and loading conditions.")

# # # Toggle between Beam and Frame Analysis
# # structure_type = st.radio("Select Structure Type", ["Beam", "Frame"], key="structure_type")

# # if structure_type == "Beam":
# #     st.subheader("Beam Analysis")
# #     num_spans = st.number_input("Number of Spans", min_value=1, value=1, step=1)
# #     L_values = []
# #     load_types = []
# #     load_values = []
# #     load_positions = []
# #     for i in range(num_spans):
# #         st.subheader(f"Span {i+1} Properties")
# #         L_values.append(st.number_input(f"Enter Length of Span {i+1} (meters)", min_value=0.1, value=5.0, step=0.1))
# #         load_type = st.radio(f"Select Load Type for Span {i+1}", ["UDL", "Point Load"], key=f"load_type_{i}")
# #         load_types.append(load_type)
# #         if load_type == "UDL":
# #             load_values.append(st.number_input(f"Enter UDL Intensity (kN/m) for Span {i+1}", min_value=0.1, value=10.0, step=0.1))
# #             load_positions.append(None)  # Not needed for UDL
# #         else:
# #             load_values.append(st.number_input(f"Enter Point Load (kN) for Span {i+1}", min_value=0.1, value=10.0, step=0.1))
# #             load_positions.append(st.number_input(f"Enter Load Position (m) from Left End for Span {i+1}", min_value=0.1, value=L_values[i]/2, step=0.1))

# # elif structure_type == "Frame":
# #     st.subheader("Frame Analysis")
# #     num_columns = st.number_input("Number of Columns", min_value=1, value=1, step=1)
# #     num_beams = st.number_input("Number of Beams", min_value=1, value=1, step=1)
# #     frame_elements = []
# #     for i in range(num_columns + num_beams):
# #         st.subheader(f"Element {i+1} Properties")
# #         element_type = st.selectbox(f"Select Element Type for Element {i+1}", ["Column", "Beam"], key=f"element_type_{i}")
# #         length = st.number_input(f"Enter Length of Element {i+1} (meters)", min_value=0.1, value=3.0, step=0.1)
# #         if element_type == "Beam":
# #             load_type = st.radio(f"Select Load Type for Beam {i+1}", ["UDL", "Point Load"], key=f"beam_load_type_{i}")
# #             if load_type == "UDL":
# #                 load_value = st.number_input(f"Enter UDL Intensity (kN/m) for Beam {i+1}", min_value=0.1, value=10.0, step=0.1)
# #             else:
# #                 load_value = st.number_input(f"Enter Point Load (kN) for Beam {i+1}", min_value=0.1, value=10.0, step=0.1)
# #                 load_position = st.number_input(f"Enter Load Position (m) from Left End for Beam {i+1}", min_value=0.1, value=length/2, step=0.1)
# #             frame_elements.append((element_type, length, load_type, load_value, load_position if load_type == "Point Load" else None))
# #         else:
# #             frame_elements.append((element_type, length))

# # if st.button("Calculate"):
# #     if structure_type == "Beam":
# #         st.subheader("Beam Analysis Results")
# #         st.write("Beam calculations and diagrams coming soon...")
# #     elif structure_type == "Frame":
# #         st.subheader("Frame Analysis Results")
# #         st.write("Frame calculations and diagrams coming soon...")



# import streamlit as st
# import matplotlib.pyplot as plt
# import sympy as sp
# import pandas as pd
# import time
# import numpy as np
# from matplotlib.animation import FuncAnimation

# class EF:
#     def __init__(self, L, m0, m1, v0, v1):
#         self.L = L
#         self.efs = [m0, m1, v0, v1]

#     @property
#     def m0(self):
#         return self.efs[0]

#     @property
#     def m1(self):
#         return self.efs[1]

#     @property
#     def v0(self):
#         return self.efs[2]

#     @property
#     def v1(self):
#         return self.efs[3]

# # Function to apply Slope Deflection Method

# def slope_deflection(L, t0, t1, d01, M_fixed):
#     """Calculate moments using the Slope Deflection Method."""
#     M0 = (4/L) * t0 + (2/L) * t1 - (6/L**2) * d01 + M_fixed[0]
#     M1 = (2/L) * t0 + (4/L) * t1 - (6/L**2) * d01 + M_fixed[1]
#     return M0, M1

# # Streamlit UI
# st.title("Beam & Frame Analysis Calculator")
# st.markdown("Select structure type and loading conditions.")

# # Toggle between Beam and Frame Analysis
# structure_type = st.radio("Select Structure Type", ["Beam", "Frame"], key="structure_type")

# if structure_type == "Frame":
#     st.subheader("Frame Analysis")
#     num_columns = st.number_input("Number of Columns", min_value=1, value=1, step=1)
#     num_beams = st.number_input("Number of Beams", min_value=1, value=1, step=1)
#     frame_elements = []
#     for i in range(num_columns + num_beams):
#         st.subheader(f"Element {i+1} Properties")
#         element_type = st.selectbox(f"Select Element Type for Element {i+1}", ["Column", "Beam"], key=f"element_type_{i}")
#         length = st.number_input(f"Enter Length of Element {i+1} (meters)", min_value=0.1, value=3.0, step=0.1)
#         t0 = st.number_input(f"Enter Rotation at Start of Element {i+1}", value=0.0, step=0.01)
#         t1 = st.number_input(f"Enter Rotation at End of Element {i+1}", value=0.0, step=0.01)
#         d01 = st.number_input(f"Enter Displacement between Ends of Element {i+1}", value=0.0, step=0.01)
        
#         M_fixed = [0, 0]  # Placeholder for fixed-end moments
#         frame_elements.append((element_type, length, t0, t1, d01, M_fixed))

# if st.button("Calculate"):
#     if structure_type == "Frame":
#         st.subheader("Frame Analysis Results")
#         moments = []
#         for element in frame_elements:
#             if element[0] == "Beam":
#                 M0, M1 = slope_deflection(element[1], element[2], element[3], element[4], element[5])
#                 moments.append((M0, M1))
#                 st.write(f"Beam {frame_elements.index(element) + 1}: M0 = {M0:.2f} kNm, M1 = {M1:.2f} kNm")
#                 time.sleep(1)
#             else:
#                 st.write(f"Column {frame_elements.index(element) + 1}: No moment calculation required.")
#                 time.sleep(1)
        
#         # Visualization - Animated Bending Moment Diagram
#         fig, ax = plt.subplots()
#         x_data = np.linspace(0, sum([e[1] for e in frame_elements if e[0] == "Beam"]), 100)
#         y_data = np.zeros_like(x_data)
        
#         def update(frame):
#             ax.clear()
#             ax.plot(x_data[:frame], y_data[:frame], color='red', linewidth=2)
#             ax.set_title("Bending Moment Diagram")
#             ax.set_xlabel("Beam Length (m)")
#             ax.set_ylabel("Bending Moment (kNm)")
#             ax.grid()
        
#         ani = FuncAnimation(fig, update, frames=len(x_data), interval=50)
#         st.pyplot(fig)
        
#         st.success("Analysis complete! Frame visualization updated.")

# import streamlit as st
# import matplotlib.pyplot as plt
# import sympy as sp
# import pandas as pd
# import time
# import numpy as np
# from matplotlib.animation import FuncAnimation

# class EF:
#     def __init__(self, L, m0, m1, v0, v1):
#         self.L = L
#         self.efs = [m0, m1, v0, v1]

#     @property
#     def m0(self):
#         return self.efs[0]

#     @property
#     def m1(self):
#         return self.efs[1]

#     @property
#     def v0(self):
#         return self.efs[2]

#     @property
#     def v1(self):
#         return self.efs[3]

# # Function to apply Slope Deflection Method

# def slope_deflection(L, t0, t1, d01, M_fixed):
#     """Calculate moments using the Slope Deflection Method."""
#     M0 = (4/L) * t0 + (2/L) * t1 - (6/L**2) * d01 + M_fixed[0]
#     M1 = (2/L) * t0 + (4/L) * t1 - (6/L**2) * d01 + M_fixed[1]
#     return M0, M1

# # Function to calculate Shear and Bending Moment for Beams

# def beam_moment_shear(L, w):
#     """Calculate shear force and bending moment for a simply supported beam with UDL."""
#     x = np.linspace(0, L, 100)
#     shear_force = w * (L/2 - x)
#     bending_moment = (w/2) * x * (L - x)
#     return x, shear_force, bending_moment

# # Streamlit UI
# st.title("Beam & Frame Analysis Calculator")
# st.markdown("Select structure type and loading conditions.")

# # Toggle between Beam and Frame Analysis
# structure_type = st.radio("Select Structure Type", ["Beam", "Frame"], key="structure_type")

# if structure_type == "Beam":
#     st.subheader("Beam Analysis")
#     num_spans = st.number_input("Number of Spans", min_value=1, value=1, step=1)
#     L_values = []
#     load_values = []
#     for i in range(num_spans):
#         st.subheader(f"Span {i+1} Properties")
#         L = st.number_input(f"Enter Length of Span {i+1} (meters)", min_value=0.1, value=5.0, step=0.1)
#         w = st.number_input(f"Enter UDL Intensity (kN/m) for Span {i+1}", min_value=0.1, value=10.0, step=0.1)
#         L_values.append(L)
#         load_values.append(w)

# if st.button("Calculate"):
#     if structure_type == "Beam":
#         st.subheader("Beam Analysis Results")
#         fig, ax = plt.subplots(2, 1, figsize=(8, 6))
        
#         for i, (L, w) in enumerate(zip(L_values, load_values)):
#             x, shear_force, bending_moment = beam_moment_shear(L, w)
            
#             ax[0].plot(x, shear_force, label=f"Span {i+1}")
#             ax[1].plot(x, bending_moment, label=f"Span {i+1}")
            
#         ax[0].set_title("Shear Force Diagram")
#         ax[0].set_ylabel("Shear Force (kN)")
#         ax[0].legend()
#         ax[0].grid()
        
#         ax[1].set_title("Bending Moment Diagram")
#         ax[1].set_xlabel("Beam Length (m)")
#         ax[1].set_ylabel("Bending Moment (kNm)")
#         ax[1].legend()
#         ax[1].grid()
        
#         st.pyplot(fig)
#         st.success("Beam analysis complete!")
        
#         # Animated Beam Deformation Visualization
#         fig_anim, ax_anim = plt.subplots()
#         x, shear_force, bending_moment = beam_moment_shear(L_values[0], load_values[0])
#         y_data = -bending_moment / max(abs(bending_moment))  # Normalize for visualization
        
#         def update(frame):
#             ax_anim.clear()
#             ax_anim.plot(x[:frame], y_data[:frame], color='blue', linewidth=2)
#             ax_anim.set_title("Beam Deflection Shape")
#             ax_anim.set_xlabel("Beam Length (m)")
#             ax_anim.set_ylabel("Deflection (scaled)")
#             ax_anim.grid()
        
#         ani = FuncAnimation(fig_anim, update, frames=len(x), interval=50)
#         st.pyplot(fig_anim)
        
#     elif structure_type == "Frame":
#         st.subheader("Frame Analysis Results")
#         st.write("Frame calculations and diagrams coming soon...")

# # Next Steps
# st.subheader("Next Steps:")
# st.markdown("✅ Add more load conditions (point loads, varying loads).")
# st.markdown("✅ Implement internal hinge support conditions.")
# st.markdown("✅ Enhance visualization for frames with animated deformation.")



# import streamlit as st
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.animation import FuncAnimation

# # Function to calculate Shear and Bending Moment for Beams with UDL
# def beam_moment_shear(L, w):
#     x = np.linspace(0, L, 100)
#     shear_force = w * (L/2 - x)
#     bending_moment = (w/2) * x * (L - x)
#     return x, shear_force, bending_moment

# # Function to calculate Shear and Bending Moment for Beams with Point Load
# def beam_moment_shear_point(L, P, a):
#     x = np.linspace(0, L, 100)
#     shear_force = np.piecewise(x, [x < a, x >= a], [lambda x: P, lambda x: 0])
#     bending_moment = np.piecewise(x, [x < a, x >= a], [lambda x: P * x, lambda x: P * a])
#     return x, shear_force, bending_moment

# # Function to calculate Shear and Bending Moment for Frames with UDL
# def frame_moment_shear(L, w, h):
#     x = np.linspace(0, L, 100)
#     shear_force = w * (L/2 - x)
#     bending_moment = (w/2) * x * (L - x)
#     return x, shear_force, bending_moment

# # Function to calculate Shear and Bending Moment for Frames with Point Load
# def frame_moment_shear_point(L, P, a, h):
#     x = np.linspace(0, L, 100)
#     shear_force = np.piecewise(x, [x < a, x >= a], [lambda x: P, lambda x: 0])
#     bending_moment = np.piecewise(x, [x < a, x >= a], [lambda x: P * x, lambda x: P * a])
#     return x, shear_force, bending_moment

# # Streamlit UI
# st.title("Beam & Frame Analysis Calculator")
# st.markdown("Select structure type and loading conditions.")

# # Toggle between Beam and Frame Analysis
# structure_type = st.radio("Select Structure Type", ["Beam", "Frame"], key="structure_type")

# if structure_type == "Beam":
#     st.subheader("Beam Analysis")
#     num_spans = st.number_input("Number of Spans", min_value=1, value=1, step=1)
#     L_values = []
#     load_values = []
#     load_types = []
#     load_positions = []

#     for i in range(num_spans):
#         st.subheader(f"Span {i+1} Properties")
#         L = st.number_input(f"Enter Length of Span {i+1} (meters)", min_value=0.1, value=5.0, step=0.1)
#         load_type = st.selectbox(f"Select Load Type for Span {i+1}", ["UDL", "Point Load"])
#         if load_type == "UDL":
#             w = st.number_input(f"Enter UDL Intensity (kN/m) for Span {i+1}", min_value=0.1, value=10.0, step=0.1)
#             load_values.append(w)
#             load_positions.append(None)
#         elif load_type == "Point Load":
#             P = st.number_input(f"Enter Point Load Magnitude (kN) for Span {i+1}", min_value=0.1, value=10.0, step=0.1)
#             a = st.number_input(f"Enter Distance from Left End to Point Load (m) for Span {i+1}", min_value=0.1, value=2.5, step=0.1)
#             load_values.append(P)
#             load_positions.append(a)
#         load_types.append(load_type)
#         L_values.append(L)

#     if st.button("Calculate"):
#         st.subheader("Beam Analysis Results")
#         fig, ax = plt.subplots(2, 1, figsize=(8, 6))
        
#         for i, (L, load_type, load_value, load_position) in enumerate(zip(L_values, load_types, load_values, load_positions)):
#             if load_type == "UDL":
#                 x, shear_force, bending_moment = beam_moment_shear(L, load_value)
#             elif load_type == "Point Load":
#                 x, shear_force, bending_moment = beam_moment_shear_point(L, load_value, load_position)
            
#             ax[0].plot(x, shear_force, label=f"Span {i+1}")
#             ax[1].plot(x, bending_moment, label=f"Span {i+1}")
            
#         ax[0].set_title("Shear Force Diagram")
#         ax[0].set_ylabel("Shear Force (kN)")
#         ax[0].legend()
#         ax[0].grid()
        
#         ax[1].set_title("Bending Moment Diagram")
#         ax[1].set_xlabel("Beam Length (m)")
#         ax[1].set_ylabel("Bending Moment (kNm)")
#         ax[1].legend()
#         ax[1].grid()
        
#         st.pyplot(fig)
#         st.success("Beam analysis complete!")
        
#         # Animated Beam Deformation Visualization
#         fig_anim, ax_anim = plt.subplots()
#         if load_types[0] == "UDL":
#             x, shear_force, bending_moment = beam_moment_shear(L_values[0], load_values[0])
#         elif load_types[0] == "Point Load":
#             x, shear_force, bending_moment = beam_moment_shear_point(L_values[0], load_values[0], load_positions[0])
#         y_data = -bending_moment / max(abs(bending_moment))  # Normalize for visualization
        
#         def update(frame):
#             ax_anim.clear()
#             ax_anim.plot(x[:frame], y_data[:frame], color='blue', linewidth=2)
#             ax_anim.set_title("Beam Deflection Shape")
#             ax_anim.set_xlabel("Beam Length (m)")
#             ax_anim.set_ylabel("Deflection (scaled)")
#             ax_anim.grid()
        
#         ani = FuncAnimation(fig_anim, update, frames=len(x), interval=50)
#         st.pyplot(fig_anim)

# elif structure_type == "Frame":
#     st.subheader("Frame Analysis")
#     num_members = st.number_input("Number of Members", min_value=1, value=1, step=1)
#     L_values = []
#     load_values = []
#     load_types = []
#     load_positions = []
#     height_values = []

#     for i in range(num_members):
#         st.subheader(f"Member {i+1} Properties")
#         L = st.number_input(f"Enter Length of Member {i+1} (meters)", min_value=0.1, value=5.0, step=0.1)
#         h = st.number_input(f"Enter Height of Member {i+1} (meters)", min_value=0.1, value=3.0, step=0.1)
#         load_type = st.selectbox(f"Select Load Type for Member {i+1}", ["UDL", "Point Load"])
#         if load_type == "UDL":
#             w = st.number_input(f"Enter UDL Intensity (kN/m) for Member {i+1}", min_value=0.1, value=10.0, step=0.1)
#             load_values.append(w)
#             load_positions.append(None)
#         elif load_type == "Point Load":
#             P = st.number_input(f"Enter Point Load Magnitude (kN) for Member {i+1}", min_value=0.1, value=10.0, step=0.1)
#             a = st.number_input(f"Enter Distance from Left End to Point Load (m) for Member {i+1}", min_value=0.1, value=2.5, step=0.1)
#             load_values.append(P)
#             load_positions.append(a)
#         load_types.append(load_type)
#         L_values.append(L)
#         height_values.append(h)

#     if st.button("Calculate"):
#         st.subheader("Frame Analysis Results")
#         fig, ax = plt.subplots(2, 1, figsize=(8, 6))
        
#         for i, (L, h, load_type, load_value, load_position) in enumerate(zip(L_values, height_values, load_types, load_values, load_positions)):
#             if load_type == "UDL":
#                 x, shear_force, bending_moment = frame_moment_shear(L, load_value, h)
#             elif load_type == "Point Load":
#                 x, shear_force, bending_moment = frame_moment_shear_point(L, load_value, load_position, h)
            
#             ax[0].plot(x, shear_force, label=f"Member {i+1}")
#             ax[1].plot(x, bending_moment, label=f"Member {i+1}")
            
#         ax[0].set_title("Shear Force Diagram")
#         ax[0].set_ylabel("Shear Force (kN)")
#         ax[0].legend()
#         ax[0].grid()
        
#         ax[1].set_title("Bending Moment Diagram")
#         ax[1].set_xlabel("Frame Length (m)")
#         ax[1].set_ylabel("Bending Moment (kNm)")
#         ax[1].legend()
#         ax[1].grid()
        
#         st.pyplot(fig)
#         st.success("Frame analysis complete!")
        
#         # Animated Frame Deformation Visualization
#         fig_anim, ax_anim = plt.subplots()
#         if load_types[0] == "UDL":
#             x, shear_force, bending_moment = frame_moment_shear(L_values[0], load_values[0], height_values[0])
#         elif load_types[0] == "Point Load":
#             x, shear_force, bending_moment = frame_moment_shear_point(L_values[0], load_values[0], load_positions[0], height_values[0])
#         y_data = -bending_moment / max(abs(bending_moment))  # Normalize for visualization
        
#         def update(frame):
#             ax_anim.clear()
#             ax_anim.plot(x[:frame], y_data[:frame], color='blue', linewidth=2)
#             ax_anim.set_title("Frame Deflection Shape")
#             ax_anim.set_xlabel("Frame Length (m)")
#             ax_anim.set_ylabel("Deflection (scaled)")
#             ax_anim.grid()
        
#         ani = FuncAnimation(fig_anim, update, frames=len(x), interval=50)
#         st.pyplot(fig_anim)


# import streamlit as st
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.animation import FuncAnimation

# # Function to calculate Shear and Bending Moment for Beams with UDL
# def beam_moment_shear(L, w):
#     x = np.linspace(0, L, 100)
#     shear_force = w * (L/2 - x)
#     bending_moment = (w/2) * x * (L - x)
#     return x, shear_force, bending_moment

# # Function to calculate Shear and Bending Moment for Beams with Point Load
# def beam_moment_shear_point(L, P, a):
#     x = np.linspace(0, L, 100)
#     shear_force = np.piecewise(x, [x < a, x >= a], [lambda x: P, lambda x: 0])
#     bending_moment = np.piecewise(x, [x < a, x >= a], [lambda x: P * x, lambda x: P * a])
#     return x, shear_force, bending_moment

# # Function to calculate Shear and Bending Moment for Frames with UDL
# def frame_moment_shear(L, w, h):
#     x = np.linspace(0, L, 100)
#     shear_force = w * (L/2 - x)
#     bending_moment = (w/2) * x * (L - x)
#     return x, shear_force, bending_moment

# # Function to calculate Shear and Bending Moment for Frames with Point Load
# def frame_moment_shear_point(L, P, a, h):
#     x = np.linspace(0, L, 100)
#     shear_force = np.piecewise(x, [x < a, x >= a], [lambda x: P, lambda x: 0])
#     bending_moment = np.piecewise(x, [x < a, x >= a], [lambda x: P * x, lambda x: P * a])
#     return x, shear_force, bending_moment

# # Streamlit UI
# st.title("Beam & Frame Analysis Calculator")
# st.markdown("Select structure type and loading conditions.")

# # Toggle between Beam and Frame Analysis
# structure_type = st.radio("Select Structure Type", ["Beam", "Frame"], key="structure_type")

# if structure_type == "Beam":
#     st.subheader("Beam Analysis")
#     num_spans = st.number_input("Number of Spans", min_value=1, value=1, step=1)
#     L_values = []
#     load_values = []
#     load_types = []
#     load_positions = []

#     for i in range(num_spans):
#         st.subheader(f"Span {i+1} Properties")
#         L = st.number_input(f"Enter Length of Span {i+1} (meters)", min_value=0.1, value=5.0, step=0.1)
#         load_type = st.selectbox(f"Select Load Type for Span {i+1}", ["UDL", "Point Load"])
#         if load_type == "UDL":
#             w = st.number_input(f"Enter UDL Intensity (kN/m) for Span {i+1}", min_value=0.1, value=10.0, step=0.1)
#             load_values.append(w)
#             load_positions.append(None)
#         elif load_type == "Point Load":
#             P = st.number_input(f"Enter Point Load Magnitude (kN) for Span {i+1}", min_value=0.1, value=10.0, step=0.1)
#             a = st.number_input(f"Enter Distance from Left End to Point Load (m) for Span {i+1}", min_value=0.1, value=2.5, step=0.1)
#             load_values.append(P)
#             load_positions.append(a)
#         load_types.append(load_type)
#         L_values.append(L)

#     if st.button("Calculate"):
#         st.subheader("Beam Analysis Results")
#         fig, ax = plt.subplots(2, 1, figsize=(8, 6))
        
#         # Initialize arrays to store combined shear force and bending moment
#         combined_shear_force = np.array([])
#         combined_bending_moment = np.array([])
#         current_position = 0

#         for i, (L, load_type, load_value, load_position) in enumerate(zip(L_values, load_types, load_values, load_positions)):
#             if load_type == "UDL":
#                 x, shear_force, bending_moment = beam_moment_shear(L, load_value)
#             elif load_type == "Point Load":
#                 x, shear_force, bending_moment = beam_moment_shear_point(L, load_value, load_position)
            
#             # Adjust x values to account for the current position
#             x += current_position
#             combined_shear_force = np.concatenate((combined_shear_force, shear_force))
#             combined_bending_moment = np.concatenate((combined_bending_moment, bending_moment))
#             current_position += L

#             ax[0].plot(x, shear_force, label=f"Span {i+1}")
#             ax[1].plot(x, bending_moment, label=f"Span {i+1}")
            
#         ax[0].set_title("Shear Force Diagram")
#         ax[0].set_ylabel("Shear Force (kN)")
#         ax[0].legend()
#         ax[0].grid()
        
#         ax[1].set_title("Bending Moment Diagram")
#         ax[1].set_xlabel("Beam Length (m)")
#         ax[1].set_ylabel("Bending Moment (kNm)")
#         ax[1].legend()
#         ax[1].grid()
        
#         st.pyplot(fig)
#         st.success("Beam analysis complete!")
        
#         # Animated Beam Deformation Visualization
#         fig_anim, ax_anim = plt.subplots()
#         if load_types[0] == "UDL":
#             x, shear_force, bending_moment = beam_moment_shear(L_values[0], load_values[0])
#         elif load_types[0] == "Point Load":
#             x, shear_force, bending_moment = beam_moment_shear_point(L_values[0], load_values[0], load_positions[0])
#         y_data = -bending_moment / max(abs(bending_moment))  # Normalize for visualization
        
#         def update(frame):
#             ax_anim.clear()
#             ax_anim.plot(x[:frame], y_data[:frame], color='blue', linewidth=2)
#             ax_anim.set_title("Beam Deflection Shape")
#             ax_anim.set_xlabel("Beam Length (m)")
#             ax_anim.set_ylabel("Deflection (scaled)")
#             ax_anim.grid()
        
#         ani = FuncAnimation(fig_anim, update, frames=len(x), interval=50)
#         st.pyplot(fig_anim)

# elif structure_type == "Frame":
#     st.subheader("Frame Analysis")
#     num_members = st.number_input("Number of Members", min_value=1, value=1, step=1)
#     L_values = []
#     load_values = []
#     load_types = []
#     load_positions = []
#     height_values = []

#     for i in range(num_members):
#         st.subheader(f"Member {i+1} Properties")
#         L = st.number_input(f"Enter Length of Member {i+1} (meters)", min_value=0.1, value=5.0, step=0.1)
#         h = st.number_input(f"Enter Height of Member {i+1} (meters)", min_value=0.1, value=3.0, step=0.1)
#         load_type = st.selectbox(f"Select Load Type for Member {i+1}", ["UDL", "Point Load"])
#         if load_type == "UDL":
#             w = st.number_input(f"Enter UDL Intensity (kN/m) for Member {i+1}", min_value=0.1, value=10.0, step=0.1)
#             load_values.append(w)
#             load_positions.append(None)
#         elif load_type == "Point Load":
#             P = st.number_input(f"Enter Point Load Magnitude (kN) for Member {i+1}", min_value=0.1, value=10.0, step=0.1)
#             a = st.number_input(f"Enter Distance from Left End to Point Load (m) for Member {i+1}", min_value=0.1, value=2.5, step=0.1)
#             load_values.append(P)
#             load_positions.append(a)
#         load_types.append(load_type)
#         L_values.append(L)
#         height_values.append(h)

#     if st.button("Calculate"):
#         st.subheader("Frame Analysis Results")
#         fig, ax = plt.subplots(2, 1, figsize=(8, 6))
        
#         # Initialize arrays to store combined shear force and bending moment
#         combined_shear_force = np.array([])
#         combined_bending_moment = np.array([])
#         current_position = 0

#         for i, (L, h, load_type, load_value, load_position) in enumerate(zip(L_values, height_values, load_types, load_values, load_positions)):
#             if load_type == "UDL":
#                 x, shear_force, bending_moment = frame_moment_shear(L, load_value, h)
#             elif load_type == "Point Load":
#                 x, shear_force, bending_moment = frame_moment_shear_point(L, load_value, load_position, h)
            
#             # Adjust x values to account for the current position
#             x += current_position
#             combined_shear_force = np.concatenate((combined_shear_force, shear_force))
#             combined_bending_moment = np.concatenate((combined_bending_moment, bending_moment))
#             current_position += L

#             ax[0].plot(x, shear_force, label=f"Member {i+1}")
#             ax[1].plot(x, bending_moment, label=f"Member {i+1}")
            
#         ax[0].set_title("Shear Force Diagram")
#         ax[0].set_ylabel("Shear Force (kN)")
#         ax[0].legend()
#         ax[0].grid()
        
#         ax[1].set_title("Bending Moment Diagram")
#         ax[1].set_xlabel("Frame Length (m)")
#         ax[1].set_ylabel("Bending Moment (kNm)")
#         ax[1].legend()
#         ax[1].grid()
        
#         st.pyplot(fig)
#         st.success("Frame analysis complete!")
        
#         # Animated Frame Deformation Visualization
#         fig_anim, ax_anim = plt.subplots()
#         if load_types[0] == "UDL":
#             x, shear_force, bending_moment = frame_moment_shear(L_values[0], load_values[0], height_values[0])
#         elif load_types[0] == "Point Load":
#             x, shear_force, bending_moment = frame_moment_shear_point(L_values[0], load_values[0], load_positions[0], height_values[0])
#         y_data = -bending_moment / max(abs(bending_moment))  # Normalize for visualization
        
#         def update(frame):
#             ax_anim.clear()
#             ax_anim.plot(x[:frame], y_data[:frame], color='blue', linewidth=2)
#             ax_anim.set_title("Frame Deflection Shape")
#             ax_anim.set_xlabel("Frame Length (m)")
#             ax_anim.set_ylabel("Deflection (scaled)")
#             ax_anim.grid()
        
#         ani = FuncAnimation(fig_anim, update, frames=len(x), interval=50)
#         st.pyplot(fig_anim)