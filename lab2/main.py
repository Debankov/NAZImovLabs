import pandas as pd
import numpy as np
import math

excel_file = "lab2.xlsx"

data = dict({
    "X":[i for i in range(-5,8,2)],
    "Y":[float(i) for i in np.arange(1.0, 2.6, 0.25)],
})
data.update({
    "A":[True if float((x*x-3*y)) > 10 else False for x,y in zip(data["X"], data["Y"])],
    "B":[True if abs(x) > 1 else False for x in data["X"]],
    "C":[True if (3*x+y*y) > 0 else False for x,y in zip(data["X"],data["Y"])],
})
data.update({
    "A>B":[b if a else False for a,b in zip(data["A"],data["B"])],
    "!C":[not c for c in data["C"]],
})
data.update({
    "(A>B)V!C":[(ab or c) for ab,c in zip(data["A>B"],data["!C"])],
    "!B":[not b for b in data["B"]],
})
data.update({
    "((A>B)V!C)<->!B":[True if abc == nb else False for abc, nb in zip(data["(A>B)V!C"],data["!B"])]
})

# print(data.get("A>B"))
# print(data.get("!C"))
# for ab,c in zip(data.get("A>B"),data.get("!C")):


df = pd.DataFrame({"X":data["X"],
                   "Y":data["Y"],
                   "A":data["A"],
                   "B":data["B"],
                   "C":data["C"],
                   "A>B":data["A>B"],
                   "!C":data["!C"],
                   "(A>B)V!C":data["(A>B)V!C"],
                   "!B":data["!B"],
                   "((A>B)V!C)<->!B":data["((A>B)V!C)<->!B"],
})

df.to_excel(excel_file, sheet_name="Лист1", index=False)
