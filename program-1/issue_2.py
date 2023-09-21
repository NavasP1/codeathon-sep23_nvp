def max_stock_profit(prices):
    # Step 1: Initialize variables
    min_price = float('inf')
    max_profit = 0

    # Step 2: Loop through prices and update min_price and max_profit
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    # Step 3: Return max_profit
    return max_profit