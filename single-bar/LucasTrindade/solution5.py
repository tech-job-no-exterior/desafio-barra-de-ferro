def max_price(bar_size:int, price_map:list)->int|bool:
    if (bar_size < 1
        or len(price_map) < 1
        or bar_size != len(price_map)
    ):
        return False
    
    prices = [0] * (bar_size + 1)
      
    for source in range(bar_size, -1, -1):
        max_price_for_item = 0
        for step in range(source+1, bar_size+1):
            price = price_map[(step-source-1)] + prices[step]
            max_price_for_item = max(max_price_for_item, price)
        prices[source] = max_price_for_item

    return prices[0]