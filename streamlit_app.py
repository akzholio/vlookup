import streamlit as st
import pandas as pd


def wide_space_default():
    st.set_page_config(layout="wide")


st.title(":gray[Look up & replace]", )

col1, col2, col3 = st.columns(3)

with col1:
    file_with_lookup_values = st.file_uploader("Choose a file with lookup values", type=["csv"])
    lookup_df = pd.DataFrame()
    if file_with_lookup_values is not None:
        if file_with_lookup_values.name.split(".")[-1] == "csv":
            dataframe = pd.read_csv(file_with_lookup_values)
            lookup_df.loc[:, "SKU"] = dataframe["SKU"].astype(str)
            st.dataframe(lookup_df, use_container_width=True)

with col2:
    variant_df = pd.DataFrame()
    file_to_update = st.file_uploader("Choose a file to update", type=["csv"])
    if file_to_update is not None:
        variant_df = pd.read_csv(file_to_update)
        st.dataframe(variant_df, use_container_width=True)

with col3:
    lookup_column = st.text_input('Lookup column')
    column_to_update = st.text_input('Column to update')
    new_column_value = st.text_input('New column value')

    if st.button("Update", type="primary", use_container_width=True):
        variant_df.loc[:, lookup_column] = variant_df[lookup_column].astype(str)
        variant_df.loc[variant_df[lookup_column].isin(lookup_df["SKU"]), column_to_update] = 3.5

st.dataframe(variant_df, use_container_width=True)
