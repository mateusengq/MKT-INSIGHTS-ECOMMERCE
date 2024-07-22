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
File: [Business_Questions_Group3](https://github.com/mateusengq/MKT-INSIGHTS-ECOMMERCE/blob/main/NOTEBOOK/Business_Questions_Group3.ipynb)
$$Invoice Value =[\frac{Quantity*Avg\_price}{(1-Dicount\_pct)}*(1+GST)]+Delivery\_Charges$$

- The total invoice amount is $6,183,896.12.
- The top 2 products are from the Nest-USA and Apparel categories, with $3,156,170.05 and $936,162.07 respectively. However, as seen in the Sankey Graph, the Nest-USA category has many products/items (just 9 items represent the entire invoice), whereas Apparel has 211 products/items.
Given the large number of products, the Sankey graph can be a bit confusing to read. The idea here is to show the importance of each category and product, rather than the exact impact of each.

![Sankey Graph](https://github.com/mateusengq/MKT-INSIGHTS-ECOMMERCE/blob/main/IMAGES/Sankey_Graph.png)


## Question 2: Perform Detailed exploratory analysis
File: [Business_Questions_Group3](https://github.com/mateusengq/MKT-INSIGHTS-ECOMMERCE/blob/main/NOTEBOOK/Business_Questions_Group3.ipynb)
- The highest number of distinct clients is in July (300), while the lowest is in February (109).
- There is an increasing trend in transactions from January to December, with a notable peak in December (2684 transactions).
- The lowest number of transactions occurs in February (1664 transactions).
- This indicates that while February has fewer clients, those clients make more transactions on average.
- Clients who made their first purchase in the first half of the year (months 1 to 6) tend to have a lower re-purchase rate in the following months compared to those who started purchasing later in the year. This can be observed from the retention rates, where the percentages decrease more quickly for clients acquired earlier in the year.
- There is a noticeable peak in client retention rates from October to December. This increase is likely due to promotions, discounts, and special events during these months, which encourage clients to return and make additional purchases.
![Customer Retention Rate](https://github.com/mateusengq/MKT-INSIGHTS-ECOMMERCE/blob/main/IMAGES/question2_retention_rate.png)
- Analysing the proportion of Invoice(News) comparing with the Invoice(Existent), the graph shows that the proportion tends to be half to half.
- There is a statistically significant difference between the news and the existing customers.
![Customer Type x Invoice](https://github.com/mateusengq/MKT-INSIGHTS-ECOMMERCE/blob/main/IMAGES/question2_new_existing_clients.png)
- There are significant differences between invoices with discounts and those without discounts, including for each month.
- There are 20 product categories. **Nest-USA** and **Nest** categories show notable peaks towards the end of the year, particularly around November and December. This indicates a significant increase in purchases, likely due to holiday sales and promotions.
- Categories such as Nest-USA, Nest, and Gift Cards show clear seasonal peaks, likely due to holiday shopping and promotions.
- Categories like Apparel, Office, and Bags maintain stable sales throughout the year, indicating a steady demand.
- For categories with low and stable sales, exploring new marketing strategies or bundling with more popular items could help boost sales.
![Trends](https://github.com/mateusengq/MKT-INSIGHTS-ECOMMERCE/blob/main/IMAGES/question2_trends.png)
- There are 5 locations. Chicago represents 35% of purchases. The top 3 represents more than 85% of the sales.
- The analysis of the marketing spend as a proportion of invoice shows that, on average, marketing spend is 28.15 times de revenue, with a standart deviation of 2.55. The minimum and the maximum are 24.25 and 32.40, respectively.
- To answer the question "How marketing spend is impacting on revenue?", I will analyze the correlation between the market spend and the invoce. For to test it, I will compare the invoice total with the lags of the mkt investment.
![Correlation](https://github.com/mateusengq/MKT-INSIGHTS-ECOMMERCE/blob/main/IMAGES/question2_corr_lag.png)