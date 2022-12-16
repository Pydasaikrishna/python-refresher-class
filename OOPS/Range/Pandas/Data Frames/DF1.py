#Data frames is an multi-Dimensional Array
import pandas as pd
Enteries = {
    "Temperature":[99,100,101,102,109],
    "Days":["mon","tue","wed","thu","fri"]
}

df = pd.DataFrame(Enteries)
# print(df)
print(df.loc[3])