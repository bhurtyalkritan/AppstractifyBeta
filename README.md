# Appstractify

Welcome to Appstractify, a Streamlit-based application for data analysis, visualization, and synthetic data generation.

## Getting Started

### Prerequisites

Make sure you have the following installed on your machine:

- Python 3.6 or later
- Streamlit
- Pandas
- Plotly Express
- Other dependencies specified in `requirements.txt`

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/appstractify.git


### Usage
1. Run the Streamlit app:
   streamlit run app.py
2. Upload your CSV or Excel file using the file uploader in the sidebar.
3. Explore the dataset, filter data, visualize, or generate synthetic data using the provided functionalities.

### Features
Data Filtering: Filter your dataset based on various criteria.
Data Visualization: Create interactive charts and plots using different chart types.
Synthetic Data Generation: Generate synthetic data using various models and templates.

### Folder Structure

templates/: Contains pre-made data templates.
cleanser.py: Module for data cleansing functions.
synthetic.py: Module for synthetic data generation functions.
app.py: Main Streamlit application file.

### Contributing

If you'd like to contribute to Appstractify, please follow these steps:

1. Fork the repository.
2. Create a new branch: git checkout -b feature-name.
3. Make your changes and commit: git commit -m 'Add new feature'.
4. Push to your fork: git push origin feature-name.
5. Create a pull request.

## Sections

### 1. Data Loading and Exploration
- **Title and Sidebar Setup:** Setting up the Streamlit app title and sidebar with settings.
- **File Uploader:** Allows users to upload CSV or Excel files.
- **Read Data:** Reads the default "Disease.csv" file or the uploaded file, and uses the `dataframe_explorer` function for exploration.

### 2. Data Filtering
- **Filter Form:** Users can input filter type, choose columns, and select rows for data filtering.
- **Filter Functions:** Various filter functions are available, such as greater than, less than, not equal, and more.
- **Function List:** Displays a list of available edit and filtration functions.
- **Reset Dataframe:** Button to reset the dataframe to its original state.

### 3. Synthetic Data Generation
- **Model Selection:** Users can choose from OpenAI, Bard, Llama, Faker Library, or Data Templates for synthetic data generation.
- **Prompt Input:** Input area for the prompt if using OpenAI. If Bard or Llama is selected, it provides an input area for the prompt.
- **Data Templates:** Allows users to choose from pre-made data templates like Disease Data, People Data, etc.

### 4. Data Visualization
- **Chart Type and Selection:** Users can select the type of chart (Basic, Financial, Scientific, etc.) and then choose a specific chart.
- **Chart Settings:** Provides settings for various types of charts, such as Scatter Plots, Line Charts, Bar Charts, etc.
- **Export Option:** Users can export the generated charts in different file formats (png, pdf, jpeg).

## How to Run
1. Install the required libraries: `streamlit`, `pandas`, `plotly.express`, `streamlit_extras`, `cleanser`, `synthetic`, as well as other libraries in the requirements.txt file.
2. Run the Streamlit app: `streamlit run your_script.py`.
3. Use the app in your browser and explore the functionalities.

Feel free to customize and extend the app based on your requirements!

### License

This project is licensed under the MIT License - see the LICENSE.md file for details.

### Acknowledgments

1. Streamlit - For the easy creation of web apps with Python.
2. Plotly Express - For interactive plotting in Python.
3. Feel free to reach out for any questions or issues!

# Appstractify Streamlit App Functions

## 1. Data Loading and Exploration
### `file_uploader`
Allows users to upload CSV or Excel files.

### `read_data`
Reads the default "Disease.csv" file or the uploaded file and utilizes `dataframe_explorer` for exploration.

## 2. Data Filtering
### `main_filter`
Performs data filtering based on user-input filter type, column, and row.

## 3. Synthetic Data Generation
### `prompt_gpt`
Generates synthetic data using OpenAI GPT-3. Requires an API key for OpenAI.

## 4. Data Visualization
### `scatter_plot`
Generates a scatter plot based on user-selected options.

### `line_chart`
Generates a line chart based on user-selected options.

### `box_plot`
Generates a box plot based on user-selected options.

### `histogram`
Generates a histogram based on user-selected options.

### `bar_chart`
Generates a bar chart based on user-selected options.

### `sankey_diagram`
Generates a sankey diagram based on user-selected options.

### `pie_chart`
Generates a pie chart based on user-selected options.

### `dot_plot`
Generates a dot plot based on user-selected options.

### `gantt_chart`
Generates a Gantt chart based on user-selected options.

### `sunburst_chart`
Generates a sunburst chart based on user-selected options.

### `bubble_chart`
Generates a bubble chart based on user-selected options.

### `area_plot`
Generates an area plot based on user-selected options.

## 5. Helper Functions
### `reset_dataframe`
Resets the dataframe to its original state.

### `update_dataframe`
Updates the dataframe with new data.

### `get_column`
Retrieves the column names from the dataframe.

### `get_row`
Retrieves the row indices from the dataframe.

# Cleanser Module

The `cleanser` module provides functions for data filtering and cleaning in the Appstractify application.

## Functions

### `main_filter(data, user, row)`

Main function for data filtering based on user input.

- **Parameters:**
  - `data`: DataFrame to be filtered.
  - `user`: String containing user input for filtering.
  - `row`: Column/row index for filtering.

- **Returns:**
  - Filtered DataFrame based on user input.

### `delete_greater(data, val, col)`

Deletes rows where the specified column values are greater than the given value.

### `delete_less(data, val, col)`

Deletes rows where the specified column values are less than the given value.

### `delete_equal(data, val, col)`

Deletes rows where the specified column values are equal to the given value.

### `greater_lesser_equal(data, num1, num2, col)`

Filters rows where the specified column values are between or equal to the given range.

### `greater_lesser(data, num1, num2, col)`

Filters rows where the specified column values are strictly between the given range.

### `delete_duplicate(df)`

Deletes duplicate rows from the DataFrame.

### `drop_null(df)`

Drops rows with null values from the DataFrame.

### `blank(df, row)`

Replaces blank values in a specified column with NaN and drops null rows.

### `delete_column(df, index)`

Deletes the specified column from the DataFrame.

## Operators

- `d<`: Deletes rows where the specified column values are less than the given value.
- `d>`: Deletes rows where the specified column values are greater than the given value.
- `=`: Deletes rows where the specified column values are equal to the given value.
- `$`: Filters rows where the specified column values are between or equal to the given range.
- `-r`: Deletes the specified row from the DataFrame.
- `+r`: Adds a new row to the DataFrame.
- `-c`: Deletes the specified column from the DataFrame.
- `+c`: Adds a new column to the DataFrame.

## Usage

```python
import cleanser

# Example Usage
data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
cleanser.delete_greater(data, 2, 'A')

# LangChain Functions

## 1. OpenAI Language Model (LLM)
### `prompt_gpt(user_input, key)`
Generates text using the OpenAI language model. Requires user input and an OpenAI API key.

## 2. Google Bard Language Model
### `prompt_bard(query)`
Generates text using the Google Bard language model. Requires a query and an API key.

## 3. Language Models
### `prompt_llama()`
Placeholder function for a language model called Llama.

# Data Export Functions

## 1. DataFrame Export
### `export_dataframe(data, format)`
Exports a Pandas DataFrame to a specified file format (e.g., CSV). Requires the DataFrame and the desired format.

## 2. Excel Converter
### `excel_converter(df)`
Converts a CSV file to an Excel file. Requires the CSV file.

## 3. CSV Converter
### `csv_converter()`
Placeholder function for a CSV converter.

# Data Templates
Global Data Templates:
- `Earthquake_df`: Earthquake data template.
- `Employee_df`: Employee data template.
- `Disease_df`: Disease data template.
- `Econ_df`: Economic data template.
- `Healthcare_df`: Healthcare data template.
- `Education_df`: Education data template.
- `Flight_df`: Flight data template.

# Faker Library
### `faker_lib()`
Placeholder function for the Faker library, will be implemented to be used to generate synthetic data without need of LLMs and api keys.



