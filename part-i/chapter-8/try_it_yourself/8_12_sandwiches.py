def order_sandwich(*fillings):
   """summarise sandwiches being made"""
   print("\nPlacing sandwich order with following fillings:")
   for filling in fillings:
       print(filling) 

order_sandwich('chicken')
order_sandwich('tuna','sweetcorn','mayo')