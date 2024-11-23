import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from model_pred import * 

st.title("Flood Risk Predection")

file = "data/final_rainfall_data.csv"

try:
    df = pd.read_csv(file)

    st.write("### Flood Risk Watch")
    def style_predictions(val):
        if val == 'No risk':
            return 'background-color: lightgreen; color: black; font-weight: bold;'
        elif val == 'Risk':
            return 'background-color: red; color: white; font-weight: bold;'
        return ''
    
    styled_df = df.style.applymap(style_predictions, subset=['Prediction'])

    st.dataframe(styled_df)

    # st.dataframe(df)

    # st.write("### First 5 Rows of the Dataset:")
    # st.table(df.head())

    # Provide a dowload botton if necessary
    # st.download_button(
    #     label="Download CSV",
    #     data=df.to_csv(index=False).encode('utf-8'),
    #     file_name="data/final_rainfall_data.csv",
    #     mime='text/csv'
    # )

    # # # # # # Visualization for the 'Prediction' column (Risk vs No Risk)

    if 'Prediction' in df.columns:
        prediction_counts = df['Prediction'].value_counts()
        col1, col2 = st.columns(2)
        with col1:
            st.write("### Distribution of Predictions (Risk vs No Risk):")
            fig1, ax1 = plt.subplots()
            ax1.pie(prediction_counts, labels=prediction_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightgreen'])
            ax1.axis('equal') 
            st.pyplot(fig1)

        with col2:
            st.write("### Bar Chart of Predictions (Risk & No Risk):")
            fig2, ax2 = plt.subplots()
            ax2.bar(prediction_counts.index, prediction_counts.values, color=['lightcoral', 'lightgreen'])
            ax2.set_xlabel('Prediction')
            ax2.set_ylabel('Count')
            ax2.set_title('Prediction Distribution')
            st.pyplot(fig2)


except FileNotFoundError:
    st.error("The file final_predection.csv was not found. Please ensure it is in the correct location.")


# Plot Visulaiztion

    # if 'Prediction' in df.columns:
    #     prediction_counts = df['Prediction'].value_counts()

    #     ####### Creating the pie chart

    #     st.write("### Distribution of Predictions (Risk vs No Risk):")
    #     fig, ax = plt.subplots()
    #     ax.pie(prediction_counts, labels=prediction_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightgreen'])
    #     ax.axis('equal')
    #     st.pyplot(fig)

    #     #####Creating the Bar Chart
    #     st.write("### Bar Chart of Predictions:")
    #     fig, ax = plt.subplots()
    #     ax.bar(prediction_counts.index, prediction_counts.values, color=['lightcoral', 'lightgreen'])
    #     ax.set_xlabel('Prediction')
    #     ax.set_ylabel('Count')
    #     ax.set_title('Prediction Distribution')
    #     st.pyplot(fig)


#     echo "# flood_predection" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/puzancozzu/flood_predection.git
# git push -u origin main