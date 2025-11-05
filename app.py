import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit app title
st.title("📊 Universal CSV Dataset Explorer")

st.markdown("""
Upload any CSV file to explore, visualize, and analyze your data interactively.  
Supports automatic summary, descriptive statistics, and chart generation.
""")

# Upload CSV file
uploaded_file = st.file_uploader("📂 Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read dataset
    df = pd.read_csv(uploaded_file)
    
    st.subheader("✅ Dataset Loaded Successfully!")
    st.write("**Shape of the dataset:**", df.shape)

    # Show dataset preview
    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    # Show basic statistics
    st.subheader("📈 Dataset Summary (describe)")
    st.write(df.describe())

    # Show info about columns
    st.subheader("📋 Column Information")
    st.write(df.dtypes)

    # Choose columns for visualization
    st.subheader("📊 Visualization")
    columns = df.columns.tolist()
    
    x_axis = st.selectbox("Select X-axis", columns)
    y_axis = st.selectbox("Select Y-axis", columns)

    chart_type = st.radio("Select Chart Type", ["Line", "Bar", "Scatter", "Heatmap"])

    if st.button("Generate Chart"):
        st.subheader(f"{chart_type} Chart for {x_axis} vs {y_axis}")

        if chart_type == "Line":
            fig, ax = plt.subplots()
            ax.plot(df[x_axis], df[y_axis])
            st.pyplot(fig)

        elif chart_type == "Bar":
            fig, ax = plt.subplots()
            ax.bar(df[x_axis], df[y_axis])
            st.pyplot(fig)

        elif chart_type == "Scatter":
            fig, ax = plt.subplots()
            ax.scatter(df[x_axis], df[y_axis])
            st.pyplot(fig)

        elif chart_type == "Heatmap":
            fig, ax = plt.subplots()
            sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)

    # Optional: Search in dataset
    st.subheader("🔎 Search Data")
    search_col = st.selectbox("Select column to search", df.columns)
    search_term = st.text_input("Enter value to search")
    
    if search_term:
        filtered_data = df[df[search_col].astype(str).str.contains(search_term, case=False)]
        st.write(f"Results found: {filtered_data.shape[0]}")
        st.dataframe(filtered_data)

else:
    st.info("📤 Please upload a CSV file to get started.")

st.markdown("---")
st.caption("Developed with ❤️ using Streamlit")
