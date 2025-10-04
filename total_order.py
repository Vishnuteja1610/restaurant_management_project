def calculate_order_total(order_items):
    """
    Calculate the total Cost of an Order.

    parameters:
    order_items(list of dict ): list where each dict contains 'quantity' and 'price' keys.

    Return:
    float: Total cost Calculated as sum of item price * quantity.

    Example:
    calculate_order_total([
        {'quantity':2, 'price':9.99}
        {'quantity' : 1 'price':5.49}
    ])
    """

    if not order_items:
        retrun 0.0

    total = 0.0
    for item in order_items:
        qty=item.get('quantity',0)
        price = item.get('price',0.0)
        total += qty*price
    
    return round(total, 2 )