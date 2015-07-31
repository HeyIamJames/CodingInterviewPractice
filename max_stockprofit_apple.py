"""
I have an array stock_prices_yesterday where:

The indices are the time in minutes past trade opening time, which was 9:30am local time.
The values are the price in dollars of Apple stock at that time.
For example, the stock cost $500 at 10:30am, so stock_prices_yesterday[60] = 500.

Write an efficient algorithm for computing the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

No "shorting"—you must buy before you sell. You may not buy and sell in the same time step (at least 1 minute must pass).

https://www.interviewcake.com/
"""

def get_max_profit(stock_prices_yesterday):

    max_profit = 0

    # go through every time
    for outer_time in xrange(len(stock_prices_yesterday)):

        # for every time, go through every OTHER time
        for inner_time in xrange(len(stock_prices_yesterday)):

            # for each pair, find the earlier and later times
            earlier_time = min(outer_time, inner_time)
            later_time   = max(outer_time, inner_time)

            # and use those to find the earlier and later prices
            earlier_price = stock_prices_yesterday[earlier_time]
            later_price   = stock_prices_yesterday[later_time]

            # see what our profit would be if we bought at the
            # earlier price and sold at the later price
            potential_profit = later_price - earlier_price

            # update max_profit if we can do better
            max_profit = max(max_profit, potential_profit)

    return max_profit

#non brute force method
  def get_max_profit2(stock_prices_yesterday):

    max_profit = 0

    # go through every price (with its index as the time)
    for earlier_time, earlier_price in enumerate(stock_prices_yesterday):

        # and go through all the LATER prices
        for later_price in stock_prices_yesterday[earlier_time:]:

            # see what our profit would be if we bought at the
            # earlier price and sold at the later price
            potential_profit = later_price - earlier_price

            # update max_profit if we can do better
            max_profit = max(max_profit, potential_profit)

    return max_profit
