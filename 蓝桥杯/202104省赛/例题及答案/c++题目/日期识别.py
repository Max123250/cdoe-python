big_date = list(input())
date = big_date.pop(3) + big_date.pop()
month = "".join(big_date[:3])
letter_month = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
for i in range(len(letter_month)):
    if month in letter_month[i]:
        end_month = i + 1
if date[0] == "0":
    end_date = date[1]
else:
    end_date = date
print("{} {}".format(end_month,end_date))