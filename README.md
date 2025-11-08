# Customer-Segmentation-in-ML
This project uses Machine Learning K-Means Clustering to group customers based on their age, income and spending score. It helps businesses understand customer types and improve marketing strategies.

---

## 📘 Introduction:

Customer segmentation is the process of dividing customers into groups based on similar characteristics such as age, income and spending habits.
This helps businesses understand their audience and target each group effectively with personalized marketing strategies.

In this project, we use K-Means Clustering, a popular unsupervised machine learning algorithm, to segment customers and visualize their behavior using Matplotlib.

---

## 💡 Explanation:  

### What is K-Means Clustering?  
K-Means is an unsupervised learning algorithm used for clustering data points.  
It divides data into K groups (clusters) based on feature similarity.  

Steps:  
1. Choose number of clusters K  
2. Randomly assign cluster centers  
3. Calculate distance between data points and centers  
4. Reassign points to nearest cluster  
5. Repeat until clusters stabilize  



### What is Matplotlib?  
Matplotlib is a data visualization library in Python.  
It helps us to plot:  
- Elbow graphs (to find best K)  
- Cluster scatter plots (to visualize customer groups)  

---

## 🚀 Features:  
- Cluster customers based on Age, Annual Income, and Spending Score  
- Visualize customer groups with color-coded clusters  
- Identify high-value and low-value customers  
- Easy to customize for your own dataset

  ---

## 📊 Customer Segmentation Explanation:

| Column Name        | Description                               |
| ------------------ | ----------------------------------------- |
| **CustomerID**     | Unique ID for each customer               |
| **Age**            | Age of the customer                       |
| **Annual_Income**  | Yearly income of the customer             |
| **Spending_Score** | Score assigned based on spending behavior |
| **Cluster**        | Group assigned by the K-Means algorithm   |

lusters Example:

- Cluster 0: High-income, high-spending customers

- Cluster 1: Average income, medium-spending customers

- Cluster 2: Low-income, low-spending customers

![customer seg](https://github.com/user-attachments/assets/c04be7fe-9423-407d-8d01-8262ca5bd6e9)

---


## ⚙️ Technologies Used:

| Technology                 | Purpose                              |
| -------------------------- | ------------------------------------ |
| **Python**                 | Programming Language                 |
| **Pandas**                 | Data handling and analysis           |
| **Matplotlib**             | Data visualization                   |
| **Scikit-Learn (sklearn)** | Machine Learning (K-Means Algorithm) |

---
## 🧩 Installation & Setup:

1. Clone this repository:

git clone https://github.com/harish/customer-segmentation-ml.git


2. Navigate to the project folder:

cd customer-segmentation-ml


3. Install required libraries:

pip install pandas matplotlib scikit-learn


4. Run the Python script:

python customer_segmentation.py


5. Output Run: 

A graph window opens showing the customer clusters

Console displays the dataset with assigned cluster numbers

---

## 🎥 Output:
<img width="1920" height="1080" alt="Screenshot 2025-11-08 101121" src="https://github.com/user-attachments/assets/8d8a518a-d2ed-4da8-ae25-7f3c10274412" />

---

## 🎥 Demo video:


https://github.com/user-attachments/assets/aab3a1d4-bd53-4dea-8a84-318586fdb7d6


---

## 📜 License:

This project is licensed under the MIT License.
You are free to use, modify and share it  just give proper credit to the author.

---

## 🏁 Conclusion:

- This project demonstrates how unsupervised machine learning can be applied to real world business problems like customer segmentation.

- It’s a great beginner-friendly project to showcase my machine learning skills 

