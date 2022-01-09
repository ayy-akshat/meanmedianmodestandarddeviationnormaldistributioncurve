import random
import plotly.graph_objs as go
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import statistics

df = pd.read_csv("data.csv")
s = df["math score"].tolist()

mean = sum(s)/len(s)
sd = statistics.stdev(s)
median = statistics.median(s)
mode = statistics.mode(s)

print("Mean: " + str(mean))
print("Median: " + str(median))
print("Mode: " + str(mode))
print("Standard Deviation: " + str(sd))

def d(devs):
    amt = len([i for i in s if ((mean - (devs*sd)) < i < (mean + (devs*sd)))])
    print(str(round(amt/len(s)*1000) / 10) + "% of data is within " + str(devs) + " deviations of the mean.")

d(1)
d(2)
d(3)


graph = ff.create_distplot([s], ["student math score"], show_hist=False)
graph.add_trace(go.Scatter(x=[mean, mean], y=[0.1, 0]))
graph.add_trace(go.Scatter(x=[mean - sd, mean - sd], y=[0.1, 0]))
graph.add_trace(go.Scatter(x=[mean - (2*sd), mean - (2*sd)], y=[0.1, 0]))
graph.add_trace(go.Scatter(x=[mean - (3*sd), mean - (3*sd)], y=[0.1, 0]))
graph.add_trace(go.Scatter(x=[mean + sd, mean + sd], y=[0.1, 0]))
graph.add_trace(go.Scatter(x=[mean + (2*sd), mean + (2*sd)], y=[0.1, 0]))
graph.add_trace(go.Scatter(x=[mean + (3*sd), mean + (3*sd)], y=[0.1, 0]))
graph.show()