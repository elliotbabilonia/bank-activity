import statistics as stats
from code.StockData import StockData

class StockMetrics(StockData):
    def __init__(self, path):
        # Call the parent class constructor
        super(StockMetrics, self).__init__(path)

        # Load the data
        self.load()

    def average01(self):
        averages = []  # List to store computed averages

        for row in self.data:
            valid_prices = []  # List to store valid numerical stock prices for each row

            for price_str in row:
                try:
                    # Attempt to convert the price string to a float
                    price = float(price_str)
                    valid_prices.append(price)
                except (ValueError, TypeError):
                    # Skip values that cannot be converted to floats (e.g., empty strings)
                    pass

            if valid_prices:
                # Calculate the average of valid prices for the current row
                average = sum(valid_prices) / len(valid_prices)
                # Round the average to 3 decimal places
                rounded_average = round(average, 3)
                averages.append(rounded_average)
            else:
                # If there are no valid prices in the row, append None to indicate missing data
                averages.append(None)

        return averages

    def median02(self):
        medians = []  # List to store computed medians

        for row in self.data:
            valid_prices = []  # List to store valid numerical stock prices for each row

            for price_str in row:
                try:
                    # Attempt to convert the price string to a float
                    price = float(price_str)
                    valid_prices.append(price)
                except (ValueError, TypeError):
                    # Skip values that cannot be converted to floats (e.g., empty strings)
                    pass

            if valid_prices:
                # Calculate the median of valid prices for the current row
                median = stats.median(valid_prices)
                medians.append(median)
            else:
                # If there are no valid prices in the row, append None to indicate missing data
                medians.append(None)

        return medians

    def stddev03(self):
        standard_deviations = []  # List to store computed standard deviations

        for row in self.data:
            valid_prices = []  # List to store valid numerical stock prices for each row

            for price_str in row:
                try:
                    # Attempt to convert the price string to a float
                    price = float(price_str)
                    valid_prices.append(price)
                except (ValueError, TypeError):
                    # Skip values that cannot be converted to floats (e.g., empty strings)
                    pass

            if valid_prices:
                # Calculate the sample standard deviation of valid prices for the current row
                standard_deviation = round(stats.stdev(valid_prices), 3)
                standard_deviations.append(standard_deviation)
            else:
                # If there are no valid prices in the row, append None to indicate missing data
                standard_deviations.append(None)

        return standard_deviations