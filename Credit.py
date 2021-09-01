
# re-request for number if is not digit
while True:
    credit = input("Card number: ")
    if credit.isdigit() == True:
        break

# count sum of every number’s second-to-last digit multiplied by 2
sum1 = 0

# count sum of the remaining digits
sum2 = 0

for i in credit[-2::-2]:
    j = int(i) * 2

    # if j is 10 or more
    if j >= 10:
        k = (j // 10) + (j % 10)
        sum1 += int(k)
    else:
        sum1 += int(j)

for n in credit[-1::-2]:
    sum2 += int(n)
    # print(n)

# total sum of both sums
total = sum1 + sum2

# validation
if total % 10 != 0:
    print("INVALID")

else:
    # number of digits
    digits = 0

    for i in credit:
        digits += 1

    # is it American Express
    if digits == 15 and credit[:2] == "34" or credit[:2] == "37":
        print("AMEX")

    # is it Mastercard
    elif digits == 16 and int(credit[:2]) > 50 and int(credit[:2]) < 56:
        print("MASTERCARD")

    # is it Visa
    elif (digits == 13 or digits == 16) and credit[:1] == "4":
        print("VISA")

    # in case there is other type
    else:
        print("INVALID")