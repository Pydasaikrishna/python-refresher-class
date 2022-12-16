import pandas as pd
calories = {"Day1":400,"Day2":500,"Day3":600,"Day4":600,"Day5":650}
check = pd.Series(calories, index=["Day1","Day5"])
print(check)
