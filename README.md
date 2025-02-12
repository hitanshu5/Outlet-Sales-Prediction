# 📊 Outlet Sales Prediction

This project predicts sales for various retail outlets using **Machine Learning** and is deployed using **Streamlit** for an interactive web application. The model is trained on historical sales data to help businesses forecast future sales and optimize inventory management.

![image](https://github.com/user-attachments/assets/c348e51d-e761-4aa8-9aa3-93fcc228ea2f)
![image](https://github.com/user-attachments/assets/9d55594e-e441-4874-90cf-d85c0cfabf96)
![image](https://github.com/user-attachments/assets/1912910a-c54f-49d0-94f0-848a5de58313)

## 📑 **Table of Contents**
- [🎯 Project Objective](#-project-objective)
- [📂 Dataset Description](#-dataset-description)
- [📊 Exploratory Data Analysis (EDA)](#-exploratory-data-analysis-eda)
- [🛠️ Data Preprocessing](#-data-preprocessing)
- [🤖 Model Training & Performance](#-model-training--performance)
- [🎮 Streamlit Web Application](#-streamlit-web-application)

## 🎯 **Project Objective**
The main goal of this project is to **predict outlet sales** based on various factors, such as:
- **Product details** (Item type, weight, visibility, price)
- **Outlet details** (Size, location type, establishment year)
- **Sales trends over time**  

By accurately forecasting sales, retailers can **optimize inventory management**, **set pricing strategies**, and **boost revenue**.

---

## 📂 **Dataset Description**
The dataset contains **sales data from multiple retail outlets**, with the following key features:

| Feature | Description |
|---------|------------|
| **Item_Identifier** | Unique product ID |
| **Item_Weight** | Weight of the product |
| **Item_Fat_Content** | Low Fat / Regular |
| **Item_Visibility** | How much the item is displayed |
| **Item_Type** | Category of the product |
| **Item_MRP** | Maximum Retail Price |
| **Outlet_Identifier** | Unique store ID |
| **Outlet_Establishment_Year** | Year the outlet was established |
| **Outlet_Size** | Small, Medium, or Large |
| **Outlet_Location_Type** | Tier 1, 2, or 3 city |
| **Outlet_Type** | Grocery store, supermarket, etc. |
| **Item_Outlet_Sales** | **Target Variable** (Sales prediction) |

## 📊 **Exploratory Data Analysis (EDA)**  
EDA was performed to gain insights into sales patterns.  

### **1️⃣ Distribution of Sales Across Outlets**
- Some outlet types generate **significantly higher** sales than others.
- **Supermarkets** have higher sales than **grocery stores**.

📊 *Visualization:*
![image](https://github.com/user-attachments/assets/581c1af2-2b23-4929-890b-40a4813dd108)

### **2️⃣ Impact of Item MRP on Sales**
- Sales increase as **MRP increases**, but there are specific price points where sales drop.

📊 *Visualization:* 
![image](https://github.com/user-attachments/assets/1cc64c13-38e8-4cad-85d9-e328159408c1)

### **3️⃣ Outlet Type vs. Sales**
- **Supermarkets** (Type 3) generate **higher sales** compared to **grocery stores**.

📊 *Visualization:*  
![image](https://github.com/user-attachments/assets/b880deca-43af-4865-8118-de6275208ec0)

## 🛠️ **Data Preprocessing**
To prepare data for modeling:
✅ **Handling Missing Values:**  
- **Item_Weight** missing values were filled with the **mean weight per item type**.  
- **Outlet_Size** missing values were inferred from **similar outlets**.  

✅ **Feature Engineering:**  
- Created **"Years Since Establishment"** from **Outlet_Establishment_Year**.  
- Standardized **Item_Fat_Content** labels (`Low Fat → LF`).  

✅ **Encoding Categorical Variables:**  
- Used **One-Hot Encoding** for **Item_Type, Outlet_Size, and Outlet_Location_Type**.  

---

## 🤖 **Model Training & Performance**
We trained multiple **machine learning models** to predict sales:
✅ **XGBoost performed the best** with the **highest R² score** and **lowest MAE/RMSE**.

## 🎮 **Streamlit Web Application**
The project is deployed using **Streamlit**, allowing users to input item and outlet details to **predict sales instantly**.



