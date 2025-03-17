import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import silhouette_score
import warnings
warnings.filterwarnings('ignore')

# Set style for plots
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette('viridis')

# Load all datasets
def load_data():
    """Load all the supply chain datasets"""
    sales_df = pd.read_csv('sales_data-2.csv')
    purchases_df = pd.read_csv('purchase_orders_data.csv')
    suppliers_df = pd.read_csv('suppliers_data.csv')
    inventory_df = pd.read_csv('inventory_data.csv')
    
    # Convert date columns to datetime
    sales_df['Sale_Date'] = pd.to_datetime(sales_df['Sale_Date'])
    purchases_df['Order_Date'] = pd.to_datetime(purchases_df['Order_Date'])
    purchases_df['Arrival_Date'] = pd.to_datetime(purchases_df['Arrival_Date'])
    inventory_df['Last_Updated'] = pd.to_datetime(inventory_df['Last_Updated'])
    
    return sales_df, purchases_df, suppliers_df, inventory_df

# Task 1: Demand Forecasting
def demand_forecasting(sales_df):
    """
    Perform time-series analysis on sales data and predict demand for next month
    """
    print("\n===== DEMAND FORECASTING =====")
    
    # Aggregate sales by date and product
    sales_df['Year_Month'] = sales_df['Sale_Date'].dt.to_period('M')
    monthly_sales = sales_df.groupby(['Year_Month', 'Product_ID'])['Quantity_Sold'].sum().reset_index()
    monthly_sales['Year_Month'] = monthly_sales['Year_Month'].dt.to_timestamp()
    
    # Get unique products
    products = sales_df['Product_ID'].unique()
    
    # Create a dictionary to store forecasts
    forecasts = {}
    
    for product in products:
        print(f"\nForecasting demand for product: {product}")
        
        # Filter data for the current product
        product_sales = monthly_sales[monthly_sales['Product_ID'] == product]
        
        if len(product_sales) <= 3:
            print(f"  Not enough data for product {product} to forecast")
            continue
            
        # Set up time series
        product_sales = product_sales.set_index('Year_Month')
        
        try:
            # Plot the historical sales
            plt.figure(figsize=(10, 6))
            plt.plot(product_sales.index, product_sales['Quantity_Sold'], marker='o')
            plt.title(f'Monthly Sales for Product {product}')
            plt.xlabel('Date')
            plt.ylabel('Quantity Sold')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig(f'product_{product}_sales.png')
            plt.close()
            
            # Apply Holt-Winters Exponential Smoothing model
            model = ExponentialSmoothing(
                product_sales['Quantity_Sold'],
                trend='add',
                seasonal='add',
                seasonal_periods=12
            ).fit()
            
            # Forecast next month
            forecast_period = 1
            forecast = model.forecast(forecast_period)
            last_date = product_sales.index[-1]
            next_month = pd.date_range(start=last_date, periods=2, freq='M')[1]
            
            print(f"  Forecasted demand for {next_month.strftime('%Y-%m')}: {int(forecast[0])}")
            
            # Store forecast in the dictionary
            forecasts[product] = {
                'next_month': next_month,
                'forecast_quantity': int(forecast[0])
            }
            
        except Exception as e:
            print(f"  Error forecasting for product {product}: {e}")
    
    return forecasts

# Task 2: Reorder Point Calculation
def calculate_reorder_points(sales_df, purchases_df, suppliers_df, inventory_df):
    """
    Calculate optimal reorder point for each product
    """
    print("\n===== REORDER POINT CALCULATION =====")
    
    # Calculate average daily demand per product
    sales_df['Year_Month'] = sales_df['Sale_Date'].dt.to_period('M').dt.to_timestamp()
    monthly_demand = sales_df.groupby(['Product_ID', 'Year_Month'])['Quantity_Sold'].sum().reset_index()
    
    # Calculate days in each month for daily averages
    monthly_demand['days_in_month'] = monthly_demand['Year_Month'].dt.daysinmonth
    monthly_demand['daily_demand'] = monthly_demand['Quantity_Sold'] / monthly_demand['days_in_month']
    
    # Average daily demand across all months
    avg_daily_demand = monthly_demand.groupby('Product_ID')['daily_demand'].mean().reset_index()
    
    # Get lead times for each product from suppliers data
    product_lead_times = suppliers_df.groupby('Product_ID')['Lead_Time (days)'].mean().reset_index()
    
    # Calculate standard deviation of demand for safety stock
    demand_std = monthly_demand.groupby('Product_ID')['daily_demand'].std().reset_index()
    demand_std = demand_std.rename(columns={'daily_demand': 'demand_std'})
    
    # Merge all the calculations
    reorder_data = pd.merge(avg_daily_demand, product_lead_times, on='Product_ID', how='left')
    reorder_data = pd.merge(reorder_data, demand_std, on='Product_ID', how='left')
    
    # Fill NaN values in demand_std with 0
    reorder_data['demand_std'] = reorder_data['demand_std'].fillna(0)
    
    # Service factor (for 95% service level)
    service_factor = 1.65
    
    # Calculate reorder point: ROP = Average Lead Time Demand + Safety Stock
    reorder_data['lead_time_demand'] = reorder_data['daily_demand'] * reorder_data['Lead_Time (days)']
    reorder_data['safety_stock'] = service_factor * reorder_data['demand_std'] * np.sqrt(reorder_data['Lead_Time (days)'])
    reorder_data['reorder_point'] = np.ceil(reorder_data['lead_time_demand'] + reorder_data['safety_stock'])
    
    # Get current inventory levels
    current_inventory = inventory_df.groupby('Product_ID')['Stock_Level'].sum().reset_index()
    reorder_data = pd.merge(reorder_data, current_inventory, on='Product_ID', how='left')
    
    # Compare with current reorder levels from inventory data
    current_reorder_levels = inventory_df.groupby('Product_ID')['Reorder_Level'].mean().reset_index()
    reorder_data = pd.merge(reorder_data, current_reorder_levels, on='Product_ID', how='left')
    reorder_data['reorder_point_diff'] = reorder_data['reorder_point'] - reorder_data['Reorder_Level']
    
    # Display the results
    results = reorder_data[['Product_ID', 'daily_demand', 'Lead_Time (days)', 
                           'safety_stock', 'reorder_point', 'Stock_Level', 'Reorder_Level']]
    
    print("\nCalculated Reorder Points:")
    print(results.to_string(index=False))
    
    # Create a bar chart comparing calculated vs. current reorder points
    plt.figure(figsize=(12, 8))
    products = results['Product_ID'].tolist()
    calculated = results['reorder_point'].tolist()
    current = results['Reorder_Level'].tolist()
    
    x = range(len(products))
    width = 0.35
    
    plt.bar([i - width/2 for i in x], calculated, width, label='Calculated Reorder Point')
    plt.bar([i + width/2 for i in x], current, width, label='Current Reorder Level')
    
    plt.xlabel('Product ID')
    plt.ylabel('Quantity')
    plt.title('Calculated vs Current Reorder Points')
    plt.xticks(x, products, rotation=90)
    plt.legend()
    plt.tight_layout()
    plt.savefig('reorder_points_comparison.png')
    plt.close()
    
    return results

# Task 3: Supplier Performance Analysis
def supplier_performance_analysis(purchases_df, suppliers_df):
    """
    Cluster suppliers based on lead time and order frequency
    """
    print("\n===== SUPPLIER PERFORMANCE ANALYSIS =====")
    
    # Calculate actual lead time from purchase orders data
    purchases_df['Actual_Lead_Time'] = (purchases_df['Arrival_Date'] - purchases_df['Order_Date']).dt.days
    
    # Calculate average lead time by supplier
    supplier_lead_times = purchases_df.groupby('Supplier_ID')['Actual_Lead_Time'].mean().reset_index()
    
    # Convert order frequency to numeric values
    order_freq_map = {
        'Daily': 1,
        'Weekly': 7,
        'Bi-weekly': 14,
        'Monthly': 30,
        'Quarterly': 90
    }
    
    suppliers_df['Order_Frequency_Days'] = suppliers_df['Order_Frequency'].map(order_freq_map)
    
    # Merge supplier data
    supplier_metrics = pd.merge(
        suppliers_df[['Supplier_ID', 'Supplier_Name', 'Order_Frequency_Days']],
        supplier_lead_times,
        on='Supplier_ID',
        how='left'
    )
    
    # Fill NaN values
    supplier_metrics = supplier_metrics.dropna()
    
    if len(supplier_metrics) < 3:
        print("Not enough supplier data for clustering analysis")
        return supplier_metrics
    
    # Scale the features for clustering
    features = supplier_metrics[['Order_Frequency_Days', 'Actual_Lead_Time']]
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    
    # Determine optimal number of clusters (2-5) using silhouette score
    silhouette_scores = []
    max_clusters = min(5, len(supplier_metrics) - 1)
    
    for n_clusters in range(2, max_clusters + 1):
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        cluster_labels = kmeans.fit_predict(scaled_features)
        
        try:
            silhouette_avg = silhouette_score(scaled_features, cluster_labels)
            silhouette_scores.append(silhouette_avg)
            print(f"For n_clusters = {n_clusters}, the silhouette score is {silhouette_avg:.3f}")
        except:
            print(f"Error calculating silhouette score for n_clusters = {n_clusters}")
    
    # Find the optimal number of clusters
    if silhouette_scores:
        optimal_clusters = range(2, max_clusters + 1)[np.argmax(silhouette_scores)]
    else:
        optimal_clusters = 2  # Default if calculation fails
    
    print(f"\nOptimal number of clusters: {optimal_clusters}")
    
    # Apply K-means clustering with optimal number of clusters
    kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
    supplier_metrics['Cluster'] = kmeans.fit_predict(scaled_features)
    
    # Map cluster numbers to performance categories
    cluster_centers = kmeans.cluster_centers_
    # Sort clusters based on distance from origin (lower = better performance)
    cluster_distances = np.sqrt(np.sum(cluster_centers**2, axis=1))
    cluster_ranks = np.argsort(cluster_distances)
    
    performance_categories = {
        cluster_ranks[0]: 'High Performer',
        cluster_ranks[-1]: 'Needs Improvement'
    }
    
    # For clusters in the middle, assign appropriate labels
    for i in range(1, len(cluster_ranks) - 1):
        performance_categories[cluster_ranks[i]] = f'Medium Performer {i}'
    
    supplier_metrics['Performance_Category'] = supplier_metrics['Cluster'].map(performance_categories)
    
    # Display results
    print("\nSupplier Performance Categories:")
    results = supplier_metrics[['Supplier_ID', 'Supplier_Name', 'Order_Frequency_Days', 
                               'Actual_Lead_Time', 'Performance_Category']]
    print(results.to_string(index=False))
    
    # Create a scatter plot with clusters
    plt.figure(figsize=(10, 8))
    
    # Plot each cluster with different color
    for cluster_id in range(optimal_clusters):
        cluster_data = supplier_metrics[supplier_metrics['Cluster'] == cluster_id]
        plt.scatter(
            cluster_data['Order_Frequency_Days'], 
            cluster_data['Actual_Lead_Time'],
            s=100, 
            label=f"{performance_categories[cluster_id]} (Cluster {cluster_id+1})"
        )
    
    # Plot cluster centers
    plt.scatter(
        scaler.inverse_transform(cluster_centers)[:, 0],
        scaler.inverse_transform(cluster_centers)[:, 1],
        s=200,
        marker='X',
        color='black',
        label='Cluster Centers'
    )
    
    plt.xlabel('Order Frequency (days)')
    plt.ylabel('Lead Time (days)')
    plt.title('Supplier Clustering Based on Performance')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('supplier_clusters.png')
    plt.close()
    
    return supplier_metrics

# Main function to run the analysis
def main():
    print("===== SUPPLY CHAIN ANALYTICS =====")
    
    # Load data
    sales_df, purchases_df, suppliers_df, inventory_df = load_data()
    
    # Perform analysis
    demand_forecasts = demand_forecasting(sales_df)
    reorder_points = calculate_reorder_points(sales_df, purchases_df, suppliers_df, inventory_df)
    supplier_performance = supplier_performance_analysis(purchases_df, suppliers_df)
    
    print("\nAnalysis completed successfully!")
    
    return {
        'demand_forecasts': demand_forecasts,
        'reorder_points': reorder_points,
        'supplier_performance': supplier_performance
    }

if __name__ == "__main__":
    main()