# Football-Insights-A-Decadal-Analysis

This project analyzes the winning percentage trends of selected international football teams over a specified date range using data from a CSV file.

## Project Structure

- `football_analysis.py`: The main script that performs the analysis.
- `README.md`: This file, providing an overview of the project.
- `results.csv`: The dataset containing football match results.

## Requirements

- Python 3.x
- Pandas
- Matplotlib

## Installation

1. Clone the repository or download the files.
2. Install the required Python packages using pip:

    ```sh
    pip install pandas matplotlib
    ```

## Usage

1. Ensure that `results.csv` is in the same directory as `football_analysis.py`.
2. Run the script:

    ```sh
    python football_analysis.py
    ```

## Description

The script performs the following steps:

1. Loads the dataset from `results.csv` into a Pandas DataFrame.
2. Filters the data for the date range from 2011 to 2020 and for the selected international football teams: Germany, Brazil, Spain, Argentina, and France.
3. Calculates the winning percentage trend for each selected team by year.
4. Creates summary tables for winning percentages:
    - `Table 1a`: Winning Percentage by Team by Year
    - `Table 1b`: Winning Percentage by Year by Team
5. Displays the summary tables.
6. Visualizes the winning percentages using a line plot.

## Visualization

The script generates a line plot showing the winning percentage trends by year for each selected team.

## License

This project is licensed under the MIT License.