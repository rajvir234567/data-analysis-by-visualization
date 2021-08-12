import pandas as pd
import statistics as stat
import plotly.graph_objects as go
df = pd.read_csv("data.csv")
print(df)

""" level_1 = []
level_2 = []
level_3 = []
level_4 = []
for i in df.values.tolist() :
    if(i[1] == "Level 1"):
        level_1.append(i[2])
    if(i[1] == "Level 2"):
        level_2.append(i[2])
    if(i[1] == "Level 3"):
        level_3.append(i[2])
    if(i[1] == "Level 4"):
        level_4.append(i[2])
print(stat.mean(level_1))
print(stat.mean(level_2))
print(stat.mean(level_3))
print(stat.mean(level_4))
 """
print(df.groupby("level")["attempt"].mean())

student_df = df.loc[df["student_id"] == "TRL_987"]
print(student_df.groupby("level")["attempt"].mean())
fig = go.Figure(go.Bar(x = student_df.groupby("level")["attempt"].mean(), y = ["level 1", "level 2", "level 3", "level 4"], orientation = "h"))
fig.show()
fig = go.Figure(go.Bar(x = df.groupby("level")["attempt"].mean(), y = ["level 1", "level 2", "level 3", "level 4"], orientation = "h"))
#fig.show()