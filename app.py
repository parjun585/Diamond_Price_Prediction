import streamlit as st
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline

# Streamlit app title
st.title("Diamond Price Prediction")

# Sidebar for user input
st.sidebar.header("Enter Diamond Features")
carat = st.sidebar.number_input("Carat", min_value=0.0, step=0.01)
depth = st.sidebar.number_input("Depth", min_value=0.0, step=0.01)
table = st.sidebar.number_input("Table", min_value=0.0, step=0.01)
x = st.sidebar.number_input("X (length in mm)", min_value=0.0, step=0.01)
y = st.sidebar.number_input("Y (width in mm)", min_value=0.0, step=0.01)
z = st.sidebar.number_input("Z (depth in mm)", min_value=0.0, step=0.01)
cut = st.sidebar.selectbox("Cut", options=["Ideal", "Premium", "Good", "Fair", "Very Good"])
color = st.sidebar.selectbox("Color", options=["D", "E", "F", "G", "H", "I", "J"])
clarity = st.sidebar.selectbox("Clarity", options=["IF", "VVS1", "VVS2", "VS1", "VS2", "SI1", "SI2", "I1"])

# Button for prediction
if st.sidebar.button("Predict"):
    # Gather inputs and prepare for prediction
    data = CustomData(
        carat=carat,
        depth=depth,
        table=table,
        x=x,
        y=y,
        z=z,
        cut=cut,
        color=color,
        clarity=clarity
    )
    final_new_data = data.get_data_as_dataframe()
    
    # Make a prediction
    predict_pipeline = PredictPipeline()
    pred = predict_pipeline.predict(final_new_data)
    results = round(pred[0], 2)

    # Display the result
    st.success(f"The predicted price of the diamond is: ${results}")

# Optional footer
st.sidebar.markdown("### Diamond Price Prediction App")
st.sidebar.text("Adjust the features to predict.")
