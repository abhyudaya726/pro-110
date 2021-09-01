import statistics as st
import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd
import random

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()

def calc_rand_mean(counter):
    mean_dataSet = []
    for i in range(0,counter):
        index = random.randint(0,len(data)-1)
        value = data[index]
        mean_dataSet.append(value)
    mean = st.mean(mean_dataSet)
    return mean

def show_fig(meanSampleList):
    df = meanSampleList
    mean = st.mean(df)
    fig = ff.create_distplot([df],["reading_time"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
    fig.show()

def setup():
    meanSampleList = []
    for i in range(0,1000):
        set_of_means = calc_rand_mean(100)
        meanSampleList.append(set_of_means)
    show_fig(meanSampleList)
    mean = st.mean(meanSampleList)
    print(mean)

setup()