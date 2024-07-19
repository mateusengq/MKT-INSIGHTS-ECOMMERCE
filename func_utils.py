'''
This script aims to provide functions that will turn the exploratory data analysis (EDA) process easier. 
'''

import pandas as pd
import numpy as np
import scipy.stats as stats
import statsmodels.api as sm

def detect_outliers(data, column):
    # Calculate Q1 and Q3
    Q1 = np.percentile(data[column], 25)
    Q3 = np.percentile(data[column], 75)

    # Calculate IQR
    IQR = Q3 - Q1

    # Define the outliers bounds
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    data['Outlier'] = data[column].apply(lambda x: 'YES' if x < lower_bound or x > upper_bound else 'NO')

    return data

    
    # Use NumPy to create a boolean array indicating outliers
    #is_outlier = (data[column] < lower_bound) | (data[column] > upper_bound)
    # Convert the boolean array to 'YES'/'NO'
    #data['Outlier'] = np.where(is_outlier, 'YES', 'NO')
    #return data


def proportion_calc(data, column):
    tmp = data[column].value_counts().reset_index(name = 'count')
    tmp['prop'] = tmp['count']/tmp['count'].sum()*100
    return tmp

def test_means_equality(df, data_col, group_col, alpha=0.05):
    # Group the data by the group column
    groups = df[group_col].unique()
    if len(groups) != 2:
        raise ValueError("This function requires exactly 2 groups.")
    
    group1 = df[df[group_col] == groups[0]][data_col].values
    group2 = df[df[group_col] == groups[1]][data_col].values
    
    # Perform Shapiro-Wilk test for normality for each group
    normal1 = stats.shapiro(group1)[1] > alpha
    normal2 = stats.shapiro(group2)[1] > alpha
    
    # Perform Levene's test for equal variances
    equal_var = stats.levene(group1, group2)[1] > alpha
    
    if normal1 and normal2:
        # Use t-test for independent samples
        t_val, p_val = stats.ttest_ind(group1, group2, equal_var=equal_var)
    else:
        # Use Mann-Whitney U test as a non-parametric alternative
        u_val, p_val = stats.mannwhitneyu(group1, group2)
    
     # Determine the result message
    if p_val < alpha:
        message = "There is a statistically significant difference between the groups."
    else:
        message = "There is no statistically significant difference between the groups."


    result = {
        "p-value": p_val,
        "statistically_significant": p_val < alpha,
        "message": message
    }
    
    return result


# Function to perform test for mean - many groups
def perform_test(month, df):
    discount_applied = df[(df['month'] == month) & (df['Discount_pct_ajus'] > 0)]['Invoice']
    no_discount = df[(df['month'] == month) & (df['Discount_pct_ajus'] == 0)]['Invoice']
    
    if len(discount_applied) > 0 and len(no_discount) > 0:
        # Normality test
        _, p_value_discount = stats.shapiro(discount_applied)
        _, p_value_no_discount = stats.shapiro(no_discount)

        if p_value_discount > 0.05 and p_value_no_discount > 0.05:
            # ANOVA
            f_stat, p_value = stats.f_oneway(discount_applied, no_discount)
            test_used = 'ANOVA'
        else:
            # Mann-Whitney U Test
            u_stat, p_value = stats.mannwhitneyu(discount_applied, no_discount)
            f_stat = u_stat  # Assign u_stat to f_stat to ensure a value is returned
            test_used = 'Mann-Whitney'

        return test_used, f_stat, p_value
    
    else:
        return None, None, None
    

# Function to calculate lagged correlations
def calculate_lagged_correlation(df, target_column, columns, max_lag):
    '''
    Calcular a correlacao considerando um deslocamento temporal dos dados.
    '''
    results = []
    for col in columns:
        for lag in range(1, max_lag + 1):
            df[f'{col}_lag{lag}'] = df[col].shift(lag)
            correlation = df[[target_column, f'{col}_lag{lag}']].corr().iloc[0, 1]
            results.append({'Lag': lag, 'Variable': col, 'Correlation': correlation})
    return pd.DataFrame(results)


def label_rfm_graph_method(data, col_x, col_y):
    '''
    Funcao para nomear os agrupamentos gerados considerando o RFM definido pela recencia e pela media da frequencia e valor monetario
    '''
    try:
        if data[col_x] <= 2 and data[col_y] <= 2:
            return 'Hibernating'
        elif data[col_x] <= 2 and data[col_y] <= 4:
            return 'At Risk'
        elif data[col_x] <= 2 and data[col_y] == 5:
            return "Can't lose them"
        elif data[col_x] == 3 and data[col_y] == 3:
            return "About to sleep"
        elif data[col_x] == 3 and data[col_y] <= 2:
            return "Need Attention"
        elif data[col_x] == 4 and data[col_y] == 1:
            return "Promising"
        elif data[col_x] == 5 and data[col_y] == 1:
            return "New Customers"
        elif data[col_x] <= 5 and data[col_y] <= 3:
            return "Potential Loyalist"
        elif data[col_x] <= 4 and data[col_y] <= 4:
            return "Loyal Customers"
        elif data[col_x] == 5 and data[col_y] <= 5:
            return "Champions"
        else:
            return "Other"
    except KeyError as e:
        return f"Column not found: {e}"