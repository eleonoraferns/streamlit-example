import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Restrobot!

Im a restaurant chatbot

In the meantime, below is an example of what you can do with just a few lines of code:
"""


x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})
st.text_input(label, value, max_chars, key, type, help, autocomplete, on_change, args, kwargs)
st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))
