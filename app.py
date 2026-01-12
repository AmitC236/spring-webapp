# -*- coding: utf-8 -*-

import streamlit as st
import math
import pandas as pd

st.set_page_config(page_title="Helical Spring Design", layout="centered")

st.image("header.png", use_container_width=True)

st.title("Helical Compression Spring Design Calculator")
st.write("Design of Machine Elements – Web Application")

W = st.number_input("Load W (N)", value=500.0)
tau_allow = st.number_input("Allowable shear stress (MPa)", value=400.0)
G = st.number_input("Modulus of rigidity G (Pa)", value=8e10, format="%.2e")
C = st.number_input("Spring index C (D/d)", value=8.0)
delta_mm = st.number_input("Required deflection (mm)", value=25.0)
end_type = st.selectbox("End type", ["plain", "squared", "squared_ground"])

if st.button("CALCULATE DESIGN"):

    st.subheader("What is a Helical Compression Spring?")
    st.write(
        "A helical compression spring is a mechanical element made of a wire coiled "
        "in a helical shape that resists compressive loads by storing strain energy."
    )

    st.subheader("Conclusion")
    st.write(
        "This tool assists in designing a safe and efficient helical compression spring "
        "based on given load and material constraints."
    )

    tau_allow = tau_allow * 1e6
    delta = delta_mm / 1000

    standard_diameters = [
        0.008,0.009,0.010,0.011,0.012,
        0.014,0.016,0.018,0.020
    ]

    rows = []

    for d in standard_diameters:
        D = C * d
        Kw = (4*C - 1)/(4*C - 4) + 0.615/C
        tau_max = Kw * (8 * W * D) / (math.pi * d**3)
        n = (delta * G * d**4) / (8 * W * D**3)

        rows.append([
            round(d*1000,2),
            round(D*1000,2),
            round(tau_max/1e6,2),
            round(n,2)
        ])

    df = pd.DataFrame(rows, columns=[
        "Wire dia (mm)",
        "Mean dia (mm)",
        "Max stress (MPa)",
        "Active coils"
    ])

    st.dataframe(df)
