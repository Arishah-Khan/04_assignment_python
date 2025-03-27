import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Advanced Data Dashboard", layout="wide")
st.title("Advanced Data Dashboard")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("File successfully loaded!") 
        st.write("**CSV Data Preview**")
        st.write(df.head())  

        with st.expander("**View Raw Data**"):
            st.dataframe(df.head(10))

        tab1, tab2, tab3 = st.tabs([" Summary", " Visualization", " Filters"])

        with tab1:
            st.subheader(" Data Summary")
            st.write(df.describe())

        with tab2:
            st.subheader(" Customizable Graphs")

            x_column = st.selectbox("Select X-axis", df.columns)
            y_column = st.selectbox("Select Y-axis", df.columns)

            if x_column and y_column:
                fig, ax = plt.subplots(figsize=(8, 5))
                sns.lineplot(data=df, x=x_column, y=y_column, ax=ax, marker="o", linewidth=2, color="royalblue")
                ax.set_title(f"{y_column} vs {x_column}", fontsize=14)
                ax.grid(True, linestyle="--", alpha=0.6)

                st.pyplot(fig)
            else:
                st.warning(" Please select both X and Y columns!")

        with tab3:
            st.subheader("Filter Your Data")

            selected_column = st.selectbox("Select Column to Filter", df.columns)
            unique_values = df[selected_column].unique()
            selected_value = st.selectbox("Select Value", unique_values)

            if selected_value:
                filtered_df = df[df[selected_column] == selected_value]
                st.dataframe(filtered_df)
            else:
                st.warning(" Please select a filter value!")

    except Exception as e:
        st.error(f" Error loading CSV file: {e}") 
else:
    st.info(" Please upload a CSV file to continue.")
