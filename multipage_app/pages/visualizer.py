import streamlit as st
import plotly_express as px
import pandas as pd
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


library_select = st.sidebar.selectbox(
    label="Library",
    options=['Matplotlib','Plotly_express','Seaborn']
)
chart_select = st.sidebar.selectbox(
    label="Select Chart",
    options=['Scatterplots', 'Lineplots', 'Histogram', 'Boxplot','Pie Chart']
)




numeric_columns=list(df.select_dtypes(['float','int']).columns)
color_columns = list(df.columns)

color_columns.append(None)
numeric_columns.append(None)


if chart_select == "Scatterplots":
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
elif chart_select == "Lineplots":
    st.sidebar.subheader("Lineplot Settings")
    try:
        title_value = st.sidebar.text_input("Graph Title")
        x_values = st.sidebar.selectbox("X axis", options=numeric_columns)
        y_values = st.sidebar.selectbox("Y axis", options=numeric_columns)
        color_value = st.sidebar.selectbox('Color',options=color_columns)
        plot = px.line(data_frame=df, x=x_values, y=y_values, title=title_value, color=color_value)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

elif chart_select == "Boxplot":
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
elif chart_select == "Pie Chart":
    try:
        title_value = st.sidebar.text_input("Graph Title")
        values = st.sidebar.selectbox("Values", options=numeric_columns)
        names = st.sidebar.selectbox("Names", options=color_columns)
        plot = px.pie(data_frame=df, names=names, values=values, title=title_value)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)
