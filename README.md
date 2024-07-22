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

## Question 3: Performing Customer Segmentation
File: [Business_Questions_Group3](https://github.com/mateusengq/MKT-INSIGHTS-ECOMMERCE/blob/main/NOTEBOOK/Business_Questions_Group3.ipynb)
- Heuristic (Value based, RFM): 
  - Each variable (Recency, Frequency, and Monetary) was divided into 5 groups based on percentiles.
  - The values from each group were summed and then divided into 4 new groups to create the final score.
Important to Note:
  - There are other methods and aggregations to calculate the final score. For example, different weights can be assigned based on the importance of each variable.
  - In the Exploratory Data Analysis (EDA) file, another method was included using the formula: Recency x (Frequency + Monetary) and concatenating the values.
- KMeans: I will use K-Means as suggested in the question with k = 4 to compare the two ways to determine the groups.

**Comparing Two Clustering Methods**

The heuristic-based segmentation and KMeans clustering showed significant differences in how customers are classified into four groups. The heuristic approach, which divides groups based on percentiles, ensures that each group is of equal size, making it straightforward and easy to implement. However, this method can be less flexible and might not capture the full complexity of customer behaviors. The equal group sizes may lead to oversimplification and potentially overlook important nuances in the data.

On the other hand, KMeans clustering does not guarantee equal group sizes but offers greater flexibility in capturing the underlying patterns in customer behavior. The method can adapt to the data's natural structure, resulting in more detailed and potentially more accurate customer segments. The overall accuracy of 45.23% between the two methods suggests some consistency, but the variations in group distributions highlight that KMeans clustering might identify more nuanced behaviors that the heuristic approach misses. Therefore, while the heuristic method is useful for its simplicity and equal-sized groups, KMeans clustering is often preferred for its ability to uncover deeper insights and more tailored customer segments.

![Comparing the 2 methods](https://github.com/mateusengq/MKT-INSIGHTS-ECOMMERCE/blob/main/IMAGES/comparing_euristic_kmeas.png)

**KMeans Results**:
![KMeans Results - 1](https://github.com/mateusengq/MKT-INSIGHTS-ECOMMERCE/blob/main/IMAGES/question3_kmeans.png)
![KMeans Results - 2](https://github.com/mateusengq/MKT-INSIGHTS-ECOMMERCE/blob/main/IMAGES/question3_kmeans2.png)

**Strategies for Each Segment**
1. Premium Customers:
   - **Personalized Offers**: Provide exclusive discounts and personalized product recommendations based on their purchase history.
   - **Exclusive Previews**: Offer early access to new products, sales, or events to make them feel valued.
   - **Loyalty Programs**: Enhance loyalty programs with benefits like points multipliers, exclusive rewards, or tiered memberships.
   - **Premium Services**: Offer premium services such as free expedited shipping, dedicated customer support, and easy returns.
2. Gold Customers
    - **Upsell and Cross-Sell**: Encourage higher-value purchases by recommending complementary products or higher-end items.
    - **Engagement Campaigns**: Keep them engaged with regular updates, newsletters, and special promotions.
    - **Feedback Requests**: Solicit feedback to understand their needs better and improve their experience.
    - **Loyalty Incentives**: Provide loyalty incentives such as discounts on the next purchase or bonus points for referring friends.
3. Silver Customers
    - **Discounts and Promotions**: Offer time-limited discounts or bundle deals to encourage purchases.
    - **Re-engagement Emails**: Send personalized re-engagement emails highlighting new arrivals, special offers, or upcoming sales.
    - **Loyalty Programs**: Introduce or promote a loyalty program to encourage more frequent shopping.
    - **Educational Content**: Share content that educates them about your products and their benefits, possibly through blog posts, videos, or tutorials.
4. Standard Customers
    - **Awareness Campaigns**: Use targeted social media ads and content marketing to increase brand awareness.
    - **First Purchase Incentives**: Offer welcome discounts and free samples to encourage initial purchases.
    - **Re-engagement Campaigns**: Send email reminders about new products, special offers, and win-back campaigns.
    - **Educational Content**: Provide product guides, tutorials, and customer success stories to build trust.
    - **Personalized Recommendations**: Use tailored product suggestions and customized email campaigns.
    - **Exclusive Offers**: Create special promotions and limited-time offers to encourage immediate purchases.


## Question 4: Predicting Customer Lifetime Value (Low Value/Medium Value/High Value)
File: [Business_Questions_Group3](https://github.com/mateusengq/MKT-INSIGHTS-ECOMMERCE/blob/main/NOTEBOOK/Business_Questions_Group3.ipynb)

To try to answer this question, I used Random Forest and Regression models, but both yielded unsatisfactory results. Moving forward, I plan to explore new models and adjust the parameters to enhance performance. Additionally, relying solely on Revenue/Invoice might not be the best approach for defining Customer Lifetime Value (CLV).

## Question 5: Cross-Selling (Which products are selling together)
- Considering a market analysis, there are 494 products that are frequently purchased together.
- 




# Further Steps
- Improve the results for question 4 by testing different models and fine-tuning parameters.
- Train a model to determine the client customer, taking into account client characteristics and their first two purchases, for example.
