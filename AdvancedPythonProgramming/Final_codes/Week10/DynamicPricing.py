def dynamic_price(basePrice, discount, taxRate):

    if discount > basePrice:
        return "Error: Discount cannot exceed base price!"

    priceFunc = lambda basePriceL, discountL, taxL : (basePriceL - discountL) * (1 + taxL)

    return priceFunc(basePrice, discount, taxRate)



print(dynamic_price(100, 15, 0.25))
print(dynamic_price(100, 150, 0.25))