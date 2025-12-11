import pandas as pd
import numpy as np
import math
'''
    Вариант №8
'''
excel_file = "lab3ByCode.xlsx"

data = dict({
    "X":[i for i in range(-1,3,1)],
    "Y":[float(i) for i in np.arange(1.0, 2.6, 0.5)],
})

data.update({
    "P":[True if (3*x+y*y) > 0 else False for x,y in zip(data["X"], data["Y"])],
    "Q":[True if (x*x-3*y) > 10 else False for x,y in zip(data["X"], data["Y"])],
    "R":[True if abs(x) > 1 else False for x in data["X"]],
})

data.update({
    "Q*R":[q and r for q,r in zip(data["Q"], data["R"])],
})

data.update({
    "PV(Q*R)":[p or qar for p, qar in zip(data["P"], data["Q*R"])],
    "PVR":[p or r for p, r in zip(data["P"], data["R"])],
    "PVQ":[p or q for p, q in zip(data["P"], data["Q"])],
})

data.update({
    "(PVQ)*(PVR)":[pq and pr for pq, pr in zip(data["PVQ"], data["PVR"])],
})

data.update({
    "EQUAL CHECK":[f == s for f,s in zip(data["PV(Q*R)"],data["(PVQ)*(PVR)"])]
})


df = pd.DataFrame({
    "X":data["X"],
    "Y":data["Y"],
    "P":data["P"],
    "Q":data["Q"],
    "R":data["R"],
    "Q*R":data["Q*R"],
    "PV(Q*R)":data["PV(Q*R)"],
    "PVQ":data["PVQ"],
    "PVR":data["PVR"],
    "(PVQ)*(PVR)":data["(PVQ)*(PVR)"],
    "EQUAL CHECK":data["EQUAL CHECK"]
})

df.to_excel(excel_file, sheet_name="lab3",index=False)
