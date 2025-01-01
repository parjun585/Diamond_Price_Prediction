# Diamond Price Prediction Project

## Overview
This project aims to predict diamond prices based on various features such as carat, depth, table, and dimensions (x, y, z). The solution is built as a machine learning pipeline using regression models, and it is deployed using **Streamlit** for easy interaction. The application can also be deployed on **AWS EC2** for scalability and accessibility.

---

## Key Features

### 1. **Regression Models Used**
We experimented with several regression algorithms to achieve optimal performance:
- **Linear Regression**
- **Lasso Regression**
- **Ridge Regression**
- **ElasticNet Regression**
- **Decision Tree Regressor**

### 2. **Pipeline Architecture**
The project includes modular pipelines for both training and prediction:
- **Training Pipeline:** Prepares the data, trains the model, and evaluates performance.
- **Prediction Pipeline:** Loads the trained model and makes predictions on new input data.

### 3. **Frameworks and Libraries**
- **Scikit-learn:** For regression models, data preprocessing, and evaluation.
- **Pandas:** For data manipulation and preprocessing.
- **NumPy:** For numerical computations.
- **Streamlit:** For web-based deployment and user interaction.
- **Flask:** For testing and an alternative deployment method.

---

## How to Use

### 1. **Streamlit Deployment**
#### Steps to Run Locally:
1. Clone this repository:
   ```bash
   git clone https://github.com/parjun585/Diamond_Price_Prediction.git
   cd diamond-price-prediction
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
4. Open the URL displayed in the terminal (e.g., `http://localhost:8501`) to interact with the app.

#### Features:
- Input diamond attributes via sidebar widgets.
- Predict diamond prices instantly with a click.
- Clean and interactive user interface.

### 2. **AWS EC2 Deployment**
This project can also be deployed on an AWS EC2 instance for broader accessibility.
#### Steps:
1. Launch an EC2 instance (preferably Ubuntu) and set up security groups for HTTP and SSH access.
2. SSH into the instance and clone the repository:
   ```bash
   git clone https://github.com/your-repo/diamond-price-prediction.git
   ```
3. Install Python and required libraries:
   ```bash
   sudo apt update && sudo apt install python3-pip
   pip3 install -r requirements.txt
   ```
4. Run the Streamlit app or Flask server:
   ```bash
   streamlit run app.py --server.port 80 --server.enableCORS false --server.enableXsrfProtection false
   ```
5. Access the app via the public IP of your EC2 instance.

---

## Project Structure

| Level | Folder/File Name                          | Description                                              |
|-------|------------------------------------------|----------------------------------------------------------|
| 1     | logs                                     | Stores log files for monitoring and debugging            |
| 1     | notebooks                                | Contains Jupyter notebooks for data analysis and experimentation |
| 1     | src                                      | Source code directory                                    |
| 2     | src/components                           | Modular components for different parts of the pipeline   |
| 3     | src/components/data_ingestion.py         | Handles data loading and preprocessing                   |
| 3     | src/components/data_transform.py         | Performs data transformations and feature engineering    |
| 3     | src/components/model_trainer.py          | Trains and evaluates machine learning models             |
| 2     | src/pipelines                            | Contains pipelines for training and prediction           |
| 3     | src/pipelines/training_pipeline.py       | Defines the pipeline for training the model              |
| 3     | src/pipelines/prediction_pipeline.py     | Defines the pipeline for making predictions              |
| 1     | app.py                                   | Streamlit app file                                       |
| 1     | requirements.txt                         | Python dependencies for the project                     |

---

## Future Scope
- **Hyperparameter Tuning:** Experiment with advanced techniques to improve model performance.
- **Cloud Integration:** Automate deployment and scaling using cloud services like AWS Lambda or GCP.
- **Model Explainability:** Integrate tools like SHAP or LIME to explain predictions.

---

## Acknowledgments
- **Scikit-learn Documentation** for regression models.
- **Streamlit Community** for interactive application examples.
- **AWS Documentation** for deployment guidance.

---

## License
This project is licensed under the MIT License. See `LICENSE` for details.



