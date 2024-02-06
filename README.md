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

### License

This project is licensed under the MIT License - see the LICENSE.md file for details.

### Acknowledgments

1. Streamlit - For the easy creation of web apps with Python.
2. Plotly Express - For interactive plotting in Python.
3. Feel free to reach out for any questions or issues!

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


