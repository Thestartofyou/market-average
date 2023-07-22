import pandas as pd

# Sample data - replace this with your actual data source
# For demonstration purposes, I'm using a pandas DataFrame.
# In a real scenario, data may come from APIs, databases, or CSV files.
data = {
    'Address': ['123 Main St', '456 Elm St', '789 Oak St', '101 Maple St'],
    'Price': [250000, 320000, 280000, 370000],
    'Bedrooms': [3, 4, 3, 5],
    'Bathrooms': [2, 3, 2, 4],
    'SquareFootage': [1800, 2400, 2100, 3000],
}
df = pd.DataFrame(data)

def calculate_average_price(df):
    return df['Price'].mean()

def calculate_average_bedrooms(df):
    return df['Bedrooms'].mean()

def calculate_average_square_footage(df):
    return df['SquareFootage'].mean()

def main():
    # Filter data for single-family homes in Example City
    example_city_homes = df[df['Address'].str.contains('Example City', case=False)]

    # Calculate average price, bedrooms, and square footage
    avg_price = calculate_average_price(example_city_homes)
    avg_bedrooms = calculate_average_bedrooms(example_city_homes)
    avg_sq_footage = calculate_average_square_footage(example_city_homes)

    print("Market Assessment for Single-Family Homes in Example City:")
    print("-------------------------------------------------------")
    print(f"Average Price: ${avg_price:.2f}")
    print(f"Average Bedrooms: {avg_bedrooms:.2f}")
    print(f"Average Square Footage: {avg_sq_footage:.2f} sq. ft.")
    print("-------------------------------------------------------")

if __name__ == "__main__":
    main()

