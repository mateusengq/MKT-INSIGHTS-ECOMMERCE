# Marketing Insights for E-Commerce Company

# Context
In this project, I will answer some Business Questions given in a [Kaggle Dataset](https://www.kaggle.com/datasets/rishikumarrajvansh/marketing-insights-for-e-commerce-company/data).

In the competitive world of retail, understanding the clients and purchases is key. These datset help us dig into how customers shop and interact a store over the course of a year, from January, 2019, to December 31, 2019. By looking at this data, we can answer some questions that can help the business grow and keep customers happy.

## About Dataset and Variables

The data set includes several files:
- **Online_Sales.csv:** This file contains actual orders data (point of Sales data) at transaction level with below variables.
    - CustomerID: Customer unique ID  
    - Transaction_ID: Transaction Unique ID  
    - Transaction_Date: Date of Transaction  
    - Product_SKU: SKU ID – Unique Id for product  
    - Product_Description: Product Description  
    - Product_Cateogry: Product Category  
    - Quantity: Number of items ordered  
    - Avg_Price: Price per one quantity  
    - Delivery_Charges: Charges for delivery  
    - Coupon_Status: Any discount coupon applied  
- **Customers_Data.csv:** This file contains customer’s demographics.  
    - CustomerID: Customer Unique ID  
    - Gender: Gender of customer  
    - Location: Location of Customer  
    - Tenure_Months: Tenure in Months  
- **Discount_Coupon.csv:** Discount coupons have been given for different categories in different months.  
    - Month: Discount coupon applied in that month  
    - Product_Category: Product category  
    - Coupon_Code: Coupon Code for given Category and given month  
    - Discount_pct: Discount Percentage for given coupon  
- **Marketing_Spend.csv:** Marketing spend on both offline & online channels on day wise.  
    - Date: Date
    - Offline_Spend: Marketing spend on offline channels like TV, Radio, NewsPapers, Hordings etc…  
    - Online_Spend: Marketing spend on online channels like Google keywords, facebook etc..  
- **Tax_Amount.csv:** GST Details for given category  
    - Product_Category: Product Category  
    - GST: Percentage of GST

## Structure
- Question 1: Calculate Invoice amount or sale_amount or revenue for each transaction and item level.
  - File:  [Business_Questions](https://github.com/mateusengq/MKT-INSIGHTS-ECOMMERCE/blob/main/NOTEBOOK/Business_Questions.ipynb)
- Question 2: Perform Detailed exploratory analysis
  - File:  [Business_Questions](https://github.com/mateusengq/MKT-INSIGHTS-ECOMMERCE/blob/main/NOTEBOOK/Business_Questions.ipynb)
  - Detailed Questions:
    - How many customers are acquired every month?
    - What is the month-to-month retention rate of customers?
    - How do revenues from existing and new customers change month-to-month?
    - What role do discounts play in revenues?
    - Analyze KPIs such as Revenue, number of orders, average order value, number of customers (existing/new), quantity, by category, by month, by week, by day, etc.
    - Understand sales trends and seasonality by category, location, month, etc.
    - How do the number of orders and sales vary on different days?
    - Calculate Revenue, Marketing Spend, percentage of marketing spend out of revenue, Tax, and percentage of delivery charges by month.
    - How does marketing spend impact revenue?
    - Which products appear in transactions?
    - Which products are purchased most frequently based on quantity?
- Question 3: Performing Customer Segmentation
  - File: [Business_Questions_Group3](https://github.com/mateusengq/MKT-INSIGHTS-ECOMMERCE/blob/main/NOTEBOOK/Business_Questions_Group3.ipynb)
  - Detailed Questions:
    - Heuristic (Value-based, RFM): Divide customers into Premium, Gold, Silver, and Standard categories and define strategies for each.
    - Scientific (Using K-Means): Understand customer profiles and define strategies for each segment.
- Question 4: Predicting Customer Lifetime Value (Low Value/Medium Value/High Value)
  - File: [Business_Questions_Group3](https://github.com/mateusengq/MKT-INSIGHTS-ECOMMERCE/blob/main/NOTEBOOK/Business_Questions_Group3.ipynb)
  - Detailed Questions:
    - Define the dependent variable with categories (low value, medium value, high value) based on customer revenue.
    - Perform a Classification model.
- Question 5: Cross-Selling (Which products are selling together)
  - File: [Business_Questions_Group5](https://github.com/mateusengq/MKT-INSIGHTS-ECOMMERCE/blob/main/NOTEBOOK/Business_Questions_Group5.ipynb)
- Complementary Analysis:
  - File: [Complementary Analysis](https://github.com/mateusengq/MKT-INSIGHTS-ECOMMERCE/blob/main/NOTEBOOK/EDA.ipynb)
During the process, I conducted some exploratory analyses and tests that weren't essential for answering the main business questions. These extra analyses are included in this file for reference.

# Business Objective Answers and Insights
In this README file, I have included just the main insights extracted from the analysis. The complete answers can be accessed in the files above.

## Question 1: Calculate Invoice amount or sale_amount or revenue for each transaction and item level
$$ Invoice Value =[\frac{Quantity*Avg\_price}{(1-Dicount\_pct)}*(1+GST)]+Delivery\_Charges$$

- The total invoice amount is $6,183,896.12.