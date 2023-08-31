import streamlit as st
import pandas as pd
import plotly.express as px
import cleanser
#import synthetic
st.title("Appstractify")
st.sidebar.subheader("Settings")

uploaded_file = st.sidebar.file_uploader(label="Upload CSV file (200MB Limit)", type=['csv','xlsx'])

global numeric_columns
global df

base_dataset = pd.read_csv("templates/Disease.csv")
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
    except:
        df = pd.read_excel(uploaded_file)


try:
    with st.expander("Dataset"):
       st.session_state.key = df
       st.write(st.session_state.key)
except:
    with st.expander("data"):
        st.write("Please upload the data file")

df_replace = df

##selecting type of charts
type_select = st.sidebar.selectbox(
    label="Function Type",
    options=["Data Filtering","Data Visualization","Synthetic Data"]
)

def reset_dataframe(data):
    if(data != None):
        return data
    else:
        return df

def update_dataframe(data):
    return data

def get_column(data):
    df = data
    name_holder = []
    for col in df.columns:
        name_holder.append(col)
    name_holder.insert(0,None)
    return name_holder
def get_row(data):
    df = data
    blank = list(df.index)
    blank.insert(0,None)
    return blank
if type_select == "Data Filtering":
    with st.sidebar.form("my_form"):
        st.write("Filtration")
        user_input = st.text_input("filter type")
        user_col = st.selectbox(label="Columns", options=get_column(df))
        user_row = st.selectbox(label="Rows", options=get_row(df))
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("Filter: ", user_input, "| Column: ", user_col)
            user_input = [str(i) for i in user_input]
            print(user_input)
            lol = "".join(user_input)
            lol = str(lol)
            print(lol)
            df = cleanser.main_filter(df,lol, user_col)
            update_dataframe(df)
            print(df)
            st.write(df)
    func_types = st.sidebar.selectbox("Function List", options=[
        "Edit Functions (for both): ",
        "Delete Column: -c",
        "Delete Row: -r",
        "Add Column: +c{name: [values]}",
        "Add Row: +r[values]",
        "Change type: int,str,float",
        "Filtration Functions (for columns):",
        "Greater Than: #># or >#",
        "Less Than: #<# or >#",
        "Not equal: !=# or !=str",
        "Delete Duplicate: duplicate",
        "Delete Blank: Blank",
        "Delete Null: Null",
        "Delete wrong format: Format"
    ])
    reset_button = st.sidebar.button("Reset Dataframe")
elif type_select == "Synthetic Data":
    model_choice = st.sidebar.selectbox(label="Choose AI model",options=["OpenAI [requires key]",
                                                                         "Bard [free]",
                                                                         "Llama [free]",
                                                                         "Faker Library [free]",
                                                                         "Data Templates [Pre-made data]"])
    if model_choice == "Bard [free]" or model_choice == "Llama [free]":
        ai_input = st.sidebar.text_area("Prompt",height=300)
    elif model_choice == "OpenAI [requires key]":
        key = st.sidebar.text_input("API KEY")
        ai_input = st.sidebar.text_area("Prompt", height=300)
    elif model_choice == "Data Templates [Pre-made data]":
        template_choice = st.sidebar.selectbox(label="Data Templates", options=["Earthquake Data",
                                                                                "Flight Logs",
                                                                                "People Data",
                                                                                "Research data",
                                                                                "Machine Learning Data",
                                                                                "Economic Data",
                                                                                "Healthcare Data",
                                                                                "Education data",
                                                                                "Population Data",
                                                                                "Disease Data"])
        if template_choice == "Disease Data":
            st.sidebar.write(synthetic.Disease_df)
            if st.sidebar.button("export"):
                synthetic.export_dataframe(synthetic.Disease_df)
        elif template_choice == "People Data":
            st.sidebar.write(synthetic.Employee_df)
            if st.sidebar.button("export"):
                synthetic.export_dataframe(synthetic.Employee_df)
        elif template_choice == "Earthquake Data":
            st.sidebar.write(synthetic.Earthquake_df)
            if st.sidebar.button("export"):
                synthetic.export_dataframe(synthetic.Earthquake_df)
    elif model_choice == "Faker Library [Quickest]":
        pass

elif type_select == "Data Visualization":
    library_select = st.sidebar.selectbox(
        label="Chart Type",
        options=['Basic', 'Financial', 'Scientific', "Machine Learning", "Maps", "3D", "Bioinformatics"])
    if library_select == "Basic":
        chart_select = st.sidebar.selectbox(
            label="Select Chart",
            options=["Scatter Plots", "Line Charts", "Bar Charts", "Pie Charts", "Bubble Charts", "Dot Plots",
                     "Gantt Charts",
                     "Filled Area Plots", "Horizontal Bar Charts", "Sunburst Charts", "Tables", " Sankey Diagram",
                     "Treemap Charts",
                     "Categorical Axes", "Icicle Charts", "Dumbell Plots", "Patterns,Hatching,Texture"]
        )
    elif library_select == "Financial":
        chart_select = st.sidebar.selectbox(
            label="Select Chart",
            options=["Candlestick Charts", "Waterfall Charts", "Funnel Chart", "OHLC Charts", "Time Series",
                     "Indicators",
                     "Gauge Charts", "Bullet Charts"])


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
                     'Pie Chart', 'Heat Map', 'Bubble Chart',
                     "Dot Plot", "Area Chart", "Error Bar"])
    elif library_select == "Maps":
        chart_select = st.sidebar.selectbox(
            label="Select Chart",
            options=['Scatterplots', 'Lineplots', 'Histogram', 'Boxplot',
                     'Pie Chart', 'Heat Map', 'Bubble Chart',
                     "Dot Plot", "Area Chart", "Error Bar"])
    elif library_select == "Machine Learning":
        chart_select = st.sidebar.selectbox(
            label="Select Chart",
            options=['Scatterplots', 'Lineplots', 'Histogram', 'Boxplot',
                     'Pie Chart', 'Heat Map', 'Bubble Chart',
                     "Dot Plot", "Area Chart", "Error Bar"])
    elif library_select == "Scientific":
        chart_select = st.sidebar.selectbox(
            label="Select Chart",
            options=[""])
    numeric_columns = list(df.select_dtypes(['float', 'int']).columns)
    color_columns = list(df.columns)
    pure_color = list(df.select_dtypes('string').columns)

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
            plot = px.scatter(data_frame=df, x=x_values, y=y_values, title=title_value, color=color_value,
                              size=size_value)
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
            color_value = st.sidebar.selectbox('Color', options=color_columns)
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
            plot = px.box(data_frame=df, x=x_values, y=y_values, title=title_value, points="all")
            st.plotly_chart(plot)
        except Exception as e:
            print(e)
    elif chart_select == "Histogram":
        st.sidebar.subheader("Histogram Settings")
        try:
            title_value = st.sidebar.text_input("Graph Title")
            x_values = st.sidebar.selectbox("X axis", options=numeric_columns)
            y_values = st.sidebar.selectbox("Y axis", options=numeric_columns)
            plot = px.histogram(data_frame=df, x=x_values, y=y_values, title=title_value)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)
    elif chart_select == "Bar Charts":
        st.sidebar.subheader("Bar Chart Settings")
        try:
            title_value = st.sidebar.text_input("Graph Title")
            x_values = st.sidebar.selectbox("X axis", options=color_columns)
            y_values = st.sidebar.selectbox("Y axis", options=color_columns)
            color = st.sidebar.selectbox("Color", options=color_columns)
            height = st.sidebar.number_input("Height", min_value=500, max_value=1000)
            fig = px.bar(df, x=x_values, y=y_values, color=color, title=title_value, height=height)
            st.plotly_chart(fig)
        except Exception as e:
            print(e)
    elif chart_select == "Sankey Diagrams":
        st.sidebar.subheader("Sankey Diagram Settings")
        try:
            title_value = st.sidebar.text_input("Graph Title")
            x_values = st.sidebar.selectbox("X axis", options=color_columns)
            y_values = st.sidebar.selectbox("Y axis", options=color_columns)
            color = st.sidebar.selectbox("Color", options=color_columns)
            height = st.sidebar.number_input("Height", min_value=500, max_value=1000)
            fig = px.bar(df, x=x_values, y=y_values, color=color, title=title_value, height=height)
            st.plotly_chart(fig)
        except Exception as e:
            print(e)
    elif chart_select == "Categorical Axes":
        st.sidebar.subheader("Categorical Axes Settings")
        try:
            title_value = st.sidebar.text_input("Graph Title")
            x_values = st.sidebar.selectbox("X axis", options=color_columns)
            y_values = st.sidebar.selectbox("Y axis", options=color_columns)
            color = st.sidebar.selectbox("Color", options=color_columns)
            height = st.sidebar.number_input("Height", min_value=500, max_value=1000)
            fig = px.bar(df, x=x_values, y=y_values, color=color, title=title_value, height=height)
            st.plotly_chart(fig)
        except Exception as e:
            print(e)
    elif chart_select == "Pie Charts":
        st.sidebar.subheader("Pie Chart Settings")
        try:
            title_value = st.sidebar.text_input("Graph Title")
            values = st.sidebar.selectbox("Values", options=numeric_columns)
            names = st.sidebar.selectbox("Names", options=color_columns)
            plot = px.pie(data_frame=df, names=names, values=values, title=title_value)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)
    elif chart_select == "Dot Plots":
        st.sidebar.subheader("Dot Plot Settings")
        try:
            title_value = st.sidebar.text_input("Graph Title")
            y_axis = st.sidebar.selectbox("Y Axis", options=color_columns)
            x_axis = st.sidebar.selectbox("X Axis", options=numeric_columns)
            color = st.sidebar.selectbox("Color", options=color_columns)
            symbol = st.sidebar.selectbox("Symbol", options=color_columns)
            plot = px.scatter(data_frame=df, y=y_axis, x=x_axis, color=color, symbol=symbol)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)
    elif chart_select == "Gantt Charts":
        st.sidebar.subheader("Gantt Chart Settings")
        try:
            title_value = st.sidebar.text_input("Graph Title")
            x_start = st.sidebar.selectbox("Start Date", options=numeric_columns)
            x_end = st.sidebar.selectbox("End Date", options=numeric_columns)
            y_axis = st.sidebar.selectbox("y_axis", options=numeric_columns)
            color = st.sidebar.selectbox("color", options=color_columns)
            plot = px.timeline(data_frame=df, x_start=x_start, x_end=x_end, y=y_axis, title=title_value)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)
    elif chart_select == "Sunburst Charts":
        st.sidebar.subheader("Sunburst Chart Settings")
        try:
            print(df.to_dict())
            names = st.sidebar.selectbox("Names", options=color_columns)
            parents = st.sidebar.selectbox("Parents", options=color_columns)
            values = st.sidebar.selectbox("Values", options=numeric_columns)
            fig = px.sunburst(
                df.to_dict(),
                names=names,
                parents=parents,
                values=values,
            )
            st.plotly_chart(fig)
        except Exception as e:
            print(e)
    elif chart_select == "Bubble Charts":
        st.sidebar.subheader("Bubble Chart Settings")
        try:
            title_value = st.sidebar.text_input("Graph Title")
            Yaxis = st.sidebar.selectbox("Y Axis", options=numeric_columns)
            Xaxis = st.sidebar.selectbox("X Axis", options=numeric_columns)
            Color = st.sidebar.selectbox("Color", options=color_columns)
            Size = st.sidebar.selectbox("Size", options=numeric_columns)
            hovername = st.sidebar.selectbox("Hover Name", options=color_columns)
            sizemax = st.sidebar.number_input("Max Size")
            fig = px.scatter(df, x=Xaxis, y=Yaxis,
                             size=Size, color=Color,
                             hover_name=hovername, log_x=True, size_max=sizemax, title=title_value)
            st.plotly_chart(fig)
        except Exception as e:
            print(e)
    elif chart_select == "Filled Area Plots":
        st.sidebar.subheader("Area Plot Settings")
        try:
            title_value = st.sidebar.text_input("Graph Title")
            x_axis = st.sidebar.selectbox("X Axis", options=numeric_columns)
            y_axis = st.sidebar.selectbox("Y_Axis", options=numeric_columns)
            color = st.sidebar.selectbox("Color", options=color_columns)
            line_group = st.sidebar.selectbox("Line Group", options=color_columns)
            pattern = st.sidebar.selectbox("Pattern", options=color_columns)
            fig = px.area(df, x=x_axis, y=y_axis, color=color, line_group=line_group, pattern_shape=pattern)
            st.plotly_chart(fig)
        except Exception as e:
            print(e)







