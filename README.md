# 🍔 Food Delivery Time Predictor

A beginner-friendly **Machine Learning project** that predicts the estimated food delivery time for a new order using **Linear Regression**.

The project demonstrates the complete machine learning workflow:

> **Generate Data → Explore Data → Train Model → Evaluate Model → Save Model → Make Predictions → Build Streamlit App**

The dataset used in this project is **synthetically generated** for educational purposes. It simulates how delivery distance, food preparation time, traffic, weather, and rider experience can influence delivery duration.

---

## 📌 Project Overview

Food delivery time depends on several factors. In this project, we use the following information about an order:

- 📍 Delivery distance
- 🍳 Food preparation time
- 🚦 Traffic level
- 🌧️ Weather severity
- 🛵 Rider experience

A **Linear Regression** model learns the relationship between these input features and the delivery time.

After training, the model is saved as a `.pkl` file and used by a **Streamlit web application** to predict delivery time for new orders.

> ⚠️ **Note:** This is an educational project using synthetic data. The prediction is an estimate and should not be treated as a real-world delivery guarantee.

---

## ✨ Features

- Generate a reproducible synthetic delivery dataset
- Explore the dataset using Pandas
- Check missing values and descriptive statistics
- Analyze correlations between features
- Visualize distance vs. delivery time
- Train a Linear Regression model
- Split data into training and testing sets
- Evaluate the model using:
  - MAE
  - MSE
  - RMSE
  - R² Score
- Display learned model coefficients
- Save the trained model using Pickle
- Make predictions from the command line
- Use the trained model through a Streamlit web interface
- Interactive input controls for new delivery orders

---

## 🛠️ Technologies Used

| Technology       | Purpose                                  |
| ---------------- | ---------------------------------------- |
| **Python**       | Main programming language                |
| **Pandas**       | Data loading, manipulation and analysis  |
| **NumPy**        | Synthetic data generation                |
| **Matplotlib**   | Data visualization                       |
| **Scikit-learn** | Linear Regression and model evaluation   |
| **Pickle**       | Saving and loading the trained model     |
| **Streamlit**    | Building the interactive web application |

---

## 📂 Project Structure

```text
Food-Delivery-Time-Predictor/
│
├── codes/
│   ├── 01_create_data.py
│   ├── 01_create_data.png
│   │
│   ├── 02_explore_data.py
│   ├── 02_explore_data.ipynb
│   │
│   ├── 03_train_model.py
│   ├── 03_train_model.png
│   │
│   ├── 04_predict.py
│   ├── 04_predict.png
│   │
│   ├── 05_app.py
│   │
│   ├── delivery_data.csv
│   ├── delivery_model.pkl
│   │
│   ├── FrontEnd.png
│   ├── Outputs.md
│   └── requirements.txt
│
└── README.md
```

---

## 🔄 Machine Learning Workflow

```text
                ┌─────────────────────┐
                │ Generate Synthetic  │
                │       Data          │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Explore & Analyze   │
                │       Data          │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Split Dataset into  │
                │ Train / Test Data   │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Train Linear        │
                │ Regression Model    │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Evaluate Model      │
                │ MAE / MSE / RMSE/R² │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Save Model as       │
                │ delivery_model.pkl  │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Prediction /        │
                │ Streamlit App       │
                └─────────────────────┘
```

---

## 📊 Dataset

The project creates **1,500 synthetic delivery records** using NumPy.

### Dataset Columns

| Column                   | Description                                  |
| ------------------------ | -------------------------------------------- |
| `distance_km`            | Delivery distance in kilometers              |
| `preparation_time_min`   | Food preparation time in minutes             |
| `traffic_level`          | Traffic level from 1 to 4                    |
| `weather_severity`       | Weather severity from 0 to 3                 |
| `rider_experience_years` | Rider experience in years                    |
| `delivery_time_min`      | Target variable: estimated delivery duration |

### Data Generation

The synthetic delivery time is generated using an illustrative formula:

```text
delivery_time =
    5
    + distance × 3
    + preparation_time
    + traffic × 4
    + weather × 2
    - rider_experience × 0.4
    + random_delay
```

A random seed of `42` is used so that the same sample data can be generated consistently.

The generated dataset is saved as:

```text
delivery_data.csv
```

---

# 📁 Code Navigation

## 1️⃣ Create the Dataset

### File

[`01_create_data.py`](codes/01_create_data.py)

This script:

- Generates 1,500 delivery records
- Creates all input features
- Calculates synthetic delivery time
- Creates a Pandas DataFrame
- Saves the dataset as `delivery_data.csv`

### Output

![Dataset Creation Output](codes/01_create_data.png)

---

## 2️⃣ Explore the Dataset

### Python File

[`02_explore_data.py`](codes/02_explore_data.py)

### Jupyter Notebook

[`02_explore_data.ipynb`](codes/02_explore_data.ipynb)

This stage explores the generated dataset using Pandas and Matplotlib.

It performs:

- First five records
- Dataset shape
- Dataset information
- Data types
- Missing-value checking
- Statistical summary
- Correlation analysis
- Scatter plot of distance vs. delivery time

The notebook contains the interactive exploration output.

---

## 3️⃣ Train the Machine Learning Model

### File

[`03_train_model.py`](codes/03_train_model.py)

The model uses these features:

```python
[
    "distance_km",
    "preparation_time_min",
    "traffic_level",
    "weather_severity",
    "rider_experience_years"
]
```

The target variable is:

```python
delivery_time_min
```

The dataset is divided into:

```text
80% → Training Data
20% → Testing Data
```

A **Linear Regression** model from Scikit-learn is then trained.

### Model Evaluation

The project evaluates the model using:

- **MAE — Mean Absolute Error**
- **MSE — Mean Squared Error**
- **RMSE — Root Mean Squared Error**
- **R² Score**

The model's learned coefficients are also displayed to understand how each feature contributes to the prediction.

Finally, the trained model and feature names are saved as:

```text
delivery_model.pkl
```

### Training Output

![Model Training Output](codes/03_train_model.png)

---

## 4️⃣ Make a Prediction

### File

[`04_predict.py`](codes/04_predict.py)

This script loads the saved model and asks the user for information about a new delivery:

```text
Distance
Food preparation time
Traffic level
Weather severity
Rider experience
```

The values are converted into a Pandas DataFrame using the same feature order used during training.

The trained model then predicts the estimated delivery duration.

### Prediction Output

![Prediction Output](codes/04_predict.png)

---

# 🌐 5️⃣ Streamlit Web Application

### File

[`05_app.py`](codes/05_app.py)

The Streamlit application provides a simple graphical interface for making predictions.

The user can enter:

- 📍 Delivery distance
- 🍳 Food preparation time
- 🚦 Traffic level
- 🌧️ Weather severity
- 🛵 Rider experience

Then clicking:

```text
Predict Delivery Time
```

produces an estimated delivery duration.

The application also loads the trained model using Streamlit's resource caching mechanism.

---

## 🖥️ Application Preview

![Food Delivery Time Predictor](codes/FrontEnd.png)

The web application provides a clean interface where users can enter delivery details and immediately receive a predicted delivery time.

---

## 🚀 How to Run the Project

### 1. Clone the Repository

````bash
git clone https://github.com/cloudsony999/Food_Delivery_Delay_ML
``

Then move into the project directory:

```bash
cd Food-Delivery-Time-Predictor
````

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

---

### 3. Install Dependencies

Move into the `codes` directory:

```bash
cd codes
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

### 4. Generate the Dataset

Run:

```bash
python 01_create_data.py
```

This creates:

```text
delivery_data.csv
```

---

### 5. Explore the Data

Run:

```bash
python 02_explore_data.py
```

Or open:

```text
02_explore_data.ipynb
```

in Jupyter Notebook.

---

### 6. Train the Model

Run:

```bash
python 03_train_model.py
```

This creates:

```text
delivery_model.pkl
```

---

### 7. Make a Command-Line Prediction

Run:

```bash
python 04_predict.py
```

Enter the requested delivery details.

---

### 8. Launch the Streamlit Application

Run:

```bash
streamlit run 05_app.py
```

Streamlit will start a local web server, usually at:

```text
http://localhost:8501
```

---

# 🧠 Understanding the Model

The project uses **Linear Regression**.

Conceptually, the model tries to learn a relationship like:

```text
Delivery Time =
    Intercept
    + distance coefficient
    + preparation-time coefficient
    + traffic coefficient
    + weather coefficient
    + rider-experience coefficient
```

The model learns these coefficients from the training data.

### Expected relationships in the synthetic data

| Feature          | Expected Effect                                  |
| ---------------- | ------------------------------------------------ |
| Distance         | More distance → longer delivery time             |
| Preparation Time | More preparation time → longer delivery time     |
| Traffic          | More traffic → longer delivery time              |
| Weather Severity | Worse weather → longer delivery time             |
| Rider Experience | More experience → slightly shorter delivery time |

These relationships come from the **synthetic formula used to create the dataset**, so they should not be interpreted as findings from real delivery-company data.

---

# 📈 Model Evaluation Metrics

### MAE

**Mean Absolute Error** measures the average absolute difference between the actual and predicted delivery times.

```text
MAE = average(|actual - predicted|)
```

It is expressed in minutes for this project.

---

### MSE

**Mean Squared Error** squares the prediction errors before averaging them.

```text
MSE = average((actual - predicted)²)
```

Larger errors receive greater penalties.

---

### RMSE

**Root Mean Squared Error** is the square root of MSE.

```text
RMSE = √MSE
```

Because it is expressed in minutes, it is easier to interpret than MSE.

---

### R² Score

The **R² score** indicates how much of the variation in the target variable is explained by the model.

A value closer to `1` generally indicates a stronger fit to the data.

---

# 📦 Important Project Files

| File                    | Purpose                                |
| ----------------------- | -------------------------------------- |
| `01_create_data.py`     | Creates the synthetic dataset          |
| `02_explore_data.py`    | Performs data exploration              |
| `02_explore_data.ipynb` | Notebook version of exploration        |
| `03_train_model.py`     | Trains and evaluates Linear Regression |
| `04_predict.py`         | Makes command-line predictions         |
| `05_app.py`             | Streamlit web application              |
| `delivery_data.csv`     | Generated dataset                      |
| `delivery_model.pkl`    | Saved trained model                    |
| `requirements.txt`      | Python dependencies                    |
| `Outputs.md`            | Records project outputs                |
| `FrontEnd.png`          | Streamlit application screenshot       |

---

# 🖼️ Project Outputs

## Dataset Creation

![Dataset Creation](codes/01_create_data.png)

## Model Training

![Model Training](codes/03_train_model.png)

## Prediction

![Prediction](codes/04_predict.png)

## Streamlit Frontend

![Streamlit Frontend](codes/FrontEnd.png)

---

# 📝 Outputs Documentation

The project also contains an output documentation file:

[`Outputs.md`](codes/Outputs.md)

It records the outputs obtained at different stages of the project, including:

- Data exploration
- Model training
- Prediction
- Streamlit application

---

# 🔍 What I Learned From This Project

This project demonstrates several important beginner-to-intermediate machine learning concepts:

- Creating synthetic datasets with NumPy
- Working with Pandas DataFrames
- Reading and writing CSV files
- Understanding features and target variables
- Exploratory Data Analysis
- Correlation analysis
- Data visualization
- Train-test splitting
- Linear Regression
- Model evaluation
- MAE, MSE, RMSE and R²
- Model coefficients
- Saving models with Pickle
- Loading a trained model for inference
- Building a machine-learning application with Streamlit
- Connecting a trained ML model to a user interface

---

# 🔮 Future Improvements

Some possible improvements for this project are:

- Use a real-world food delivery dataset
- Add restaurant preparation complexity
- Include time of day
- Include day of week
- Include order size
- Include restaurant location
- Include customer location
- Include rider location
- Add distance-based geographic information
- Compare Linear Regression with Random Forest and other models
- Add feature scaling where appropriate
- Add cross-validation
- Improve model visualization
- Display prediction confidence or uncertainty
- Deploy the Streamlit application online
- Add historical prediction tracking

---

# ⚠️ Disclaimer

This project is created for **educational and demonstration purposes**.

The dataset is synthetically generated and the model is not trained on real food-delivery company data. Therefore, the predictions should not be used for operational, business, financial, or safety-critical decisions.

---

# 👩‍💻 Author

**Amitava Chatterjee**

GitHub: **[@cloudsony999](https://github.com/cloudsony999)**

---

## ⭐ Support the Project

If you found this project useful or interesting:

⭐ **Star the repository**

🍴 **Fork the repository**

📚 Explore the code and experiment with the model

💡 Feel free to improve the project and build your own version!

---

## 📜 License

This project is intended for educational and learning purposes.
