# Self-Assessment
# 1.
# The first bug that I spotted when debugging was a colon missing from the for loop. This was especially obvious as it turns VSC red and shows that there is an error.
# The first bug that wasn't that obvious I found by rubber ducking. I noticed that total was not being calculated correctly and was only showing the last value in the list since it was missing the += operator.
# Lastly, I found the error but didn't understand it until I asked AI to help me understand why the while loop was giving me an index error.
# My debugging process was to first look for any obvious errors that VSC would highlight. Then I would run the code and see if it was giving me any errors.
# I feel I should take more time to rubber duck and think about the code before asking AI for help.
# 2.
# apply_discount basically takes into account the 2 arguments, price and tier, and applies a discount based on them.
# If you enter apply_discount(200, "gold"), it will return 170.0 because the gold tier has a 15% discount.
# A colleague could use it without reading the body, since they only need to know it takes a price and a tier name and returns the discounted price, and any tier that isn't gold, silver, or bronze just gets the original price back.
# 3.
#I used Claude code to help me with the broken_sales.py file. I didn't ask for the answers and instead asked for the reasoning behind the errors
#I figured out all errors and was able to get the code to run correctly. 
#I also used Claude code to check any errors in the functions.py file. I made two mistake in regards to the discount percent and what % was assingned and the discrepincy between tax2 and what waas being printed
#I let Claude correct it itself and was able to understand the reasoning behind it. 

#Exercise 1

#Defining a function
def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1= calculate_tax(100, 0.07)
tax2= calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")

#Exercise 2

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

#Calling the function with different tiers

original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

#Exercise 3

def final_price(price, discount_tier, tax_rate):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

discounted = apply_discount(200, "gold")
print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${discounted + calculate_tax(discounted, 0.07):.2f}")

#Calling the final_price function
print(f"final_price(200, 'gold', 0.07): ${final_price(200, 'gold', 0.07):.2f}")

#Exercise 4

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

rate = 0.07
for price, tier in orders:
    total = final_price(price, tier, rate)
    print(f"Order price: ${price}, Tier: {tier}, Final price: ${total:.2f}")

#Exercise 5

# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    #Not using the += caused the total to end up being 90, instead of 715. Fixing this allows total to accumulate the sum of all sales.
    total += sale
print(f"Total: ${total}")

count = 0
#At the end of every for loop, you need a colon.
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
#Instead of using <=, using < allows the loop to stay in bounds and avoids an IndexError. The loop now properly iterates through the sales list.
while i < len(sales):
    print(sales[i])
    i += 1

#Exercise 6

x = 100

def double_it():
    x = 999
    return x * 2

print(x)
print(double_it())
print(x)

# When looking at the code before, I noticed double_it is defined but not with a global variable. 
# Since this function has a local variable x, the inside x does not affect the outside x.
# I predict that it will print 100 then 1998 then 100 again.
# ^^^ This was correct.