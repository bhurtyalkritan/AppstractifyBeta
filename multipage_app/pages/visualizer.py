import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import kaleido

st.title("Appstractify")
st.sidebar.subheader("Settings")

uploaded_file = st.sidebar.file_uploader(label="Upload CSV file (200MB Limit)", type=['csv','xlsx'])

global numeric_columns
global df

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
    except:
        df = pd.read_excel(uploaded_file)

try:
    with st.expander("Dataset"):
        st.write(df)
except:
    with st.expander("data"):
        st.write("Please upload the CSV file")

##selecting type of charts
library_select = st.sidebar.selectbox(
    label="Chart Type",
    options=['Basic','Financial','Scientific',"Machine Learning", "Maps", "3D","Bioinformatics"]
)
if library_select == "Basic":
    chart_select = st.sidebar.selectbox(
        label="Select Chart",
        options=["Scatter Plots","Line Charts", "Bar Charts", "Pie Charts", "Bubble Charts", "Dot Plots", "Gantt Charts",
                 "Filled Area Plots", "Horizontal Bar Charts", "Sunburts Charts", "Tables", " Sankey Diagram", "Treemap Charts",
                 "Categorical Axes", "Icicle Charts","Dumbell Plots", "Patterns,Hatching,Texture"]
    )
elif library_select == "Financial":
    chart_select = st.sidebar.selectbox(
        label="Select Chart",
        options=["Candlestick Charts", "Waterfall Charts", "Funnel Chart","OHLC Charts","Time Series", "Indicators", "Gauge Charts", "Bullet Charts" ])


elif library_select == "3D":
    chart_select = st.sidebar.selectbox(
        label="Select Chart",
        options=['Scatterplots', 'Lineplots', 'Histogram', 'Boxplot',
                 'Pie Chart', 'Heat Map', 'Bubble Chart',
                 "Dot Plot", "Area Chart", "Error Bar"])
elif library_select == "Bioinformatics":
    chart_select = st.sidebar.selectbox(
        label="Select Chart",
        options=['Scatterplots', 'Lineplots', 'Histogram', 'Boxplot',
             'Pie Chart','Heat Map', 'Bubble Chart',
             "Dot Plot","Area Chart", "Error Bar"])
elif library_select == "Maps":
    chart_select = st.sidebar.selectbox(
        label="Select Chart",
        options=['Scatterplots', 'Lineplots', 'Histogram', 'Boxplot',
             'Pie Chart','Heat Map', 'Bubble Chart',
             "Dot Plot","Area Chart", "Error Bar"])
elif library_select == "Machine Learning":
    chart_select = st.sidebar.selectbox(
        label="Select Chart",
        options=['Scatterplots', 'Lineplots', 'Histogram', 'Boxplot',
             'Pie Chart','Heat Map', 'Bubble Chart',
             "Dot Plot","Area Chart", "Error Bar"])
elif library_select == "Scientific":
    chart_select = st.sidebar.selectbox(
        label="Select Chart",
        options=[""])
numeric_columns=list(df.select_dtypes(['float','int']).columns)
color_columns = list(df.columns)

color_columns.append(None)
numeric_columns.append(None)


if chart_select == "Scatter Plots":
    st.sidebar.subheader("Scatterplot Settings")
    try:
        title_value = st.sidebar.text_input("Graph Title")
        x_values = st.sidebar.selectbox("X axis", options=numeric_columns)
        y_values = st.sidebar.selectbox("Y axis", options=numeric_columns)
        color_value = st.sidebar.selectbox('Color', options=color_columns)
        size_value = st.sidebar.selectbox('Size', options=numeric_columns)
        plot = px.scatter(data_frame=df, x=x_values, y=y_values,title=title_value, color=color_value, size=size_value)
        st.plotly_chart(plot)
        with st.expander("Export"):
            type_select = st.selectbox(
                label="File Type",
                options=["png", "pdf", "jpeg"]
            )
            if st.button("Export"):
                plot.write_image("Downloads/fig1.png")

    except Exception as e:
        print(e)
elif chart_select == "Line Charts":
    st.sidebar.subheader("Line Chart Settings")
    try:
        title_value = st.sidebar.text_input("Graph Title")
        x_values = st.sidebar.selectbox("X axis", options=numeric_columns)
        y_values = st.sidebar.selectbox("Y axis", options=numeric_columns)
        color_value = st.sidebar.selectbox('Color',options=color_columns)
        plot = px.line(data_frame=df, x=x_values, y=y_values, title=title_value, color=color_value)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

elif chart_select == "Box Plots":
    st.sidebar.subheader("Box Plot Settings")
    try:
        title_value = st.sidebar.text_input("Graph Title")
        x_values = st.sidebar.selectbox("X axis", options=numeric_columns)
        y_values = st.sidebar.selectbox("Y axis", options=numeric_columns)
        plot = px.box(data_frame=df, x=x_values, y=y_values, title=title_value,points="all")
        st.plotly_chart(plot)
    except Exception as e:
        print(e)
elif chart_select == "Histogram":
    try:
        title_value = st.sidebar.text_input("Graph Title")
        x_values = st.sidebar.selectbox("X axis", options=numeric_columns)
        y_values = st.sidebar.selectbox("Y axis", options=numeric_columns)
        plot = px.histogram(data_frame=df, x=x_values, y=y_values, title=title_value)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)
elif chart_select == "Pie Charts":
    try:
        title_value = st.sidebar.text_input("Graph Title")
        values = st.sidebar.selectbox("Values", options=numeric_columns)
        names = st.sidebar.selectbox("Names", options=color_columns)
        plot = px.pie(data_frame=df, names=names, values=values, title=title_value)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)
elif chart_select == "Dot Plots":
    try:
        title_value = st.sidebar.text_input("Graph Title")
        values = st.sidebar.selectbox("Values", options=numeric_columns)
        names = st.sidebar.selectbox("Names", options=color_columns)
        plot = px.pie(data_frame=df, names=names, values=values, title=title_value)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)
elif chart_select == "Gantt Charts":
    try:
        title_value = st.sidebar.text_input("Graph Title")
        values = st.sidebar.selectbox("Values", options=numeric_columns)
        names = st.sidebar.selectbox("Names", options=color_columns)
        plot = px.pie(data_frame=df, names=names, values=values, title=title_value)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)
elif chart_select == "Tables":
    try:
        title_value = st.sidebar.text_input("Graph Title")
        values = st.sidebar.selectbox("Values", options=numeric_columns)
        names = st.sidebar.selectbox("Names", options=color_columns)
        plot = px.pie(data_frame=df, names=names, values=values, title=title_value)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)
elif chart_select == "Bubble Charts":
    try:
        title_value = st.sidebar.text_input("Graph Title")
        Yaxis = st.sidebar.selectbox("Y Axis",options=numeric_columns)
        Xaxis = st.sidebar.selectbox("X Axis", options=numeric_columns)
        Color = st.sidebar.selectbox("Color", options=color_columns)
        Size = st.sidebar.selectbox("Size", options=numeric_columns)
        hovername = st.sidebar.selectbox("Hover Name", options=color_columns)
        sizemax = st.sidebar.number_input("Max Size")
        fig = px.scatter(df, x=Xaxis, y=Yaxis,
                         size=Size, color=Color,
                         hover_name= hovername, log_x=True, size_max=sizemax, title=title_value)
        st.plotly_chart(fig)


    except Exception as e:
        print(e)