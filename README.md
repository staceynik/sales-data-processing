# Data Engineering Project: Sales Data Processing

This project involves processing sales data from Excel files located in the "input" folder. The script reads the data from these files, performs data cleaning and enrichment, and then creates individual JSON files for each record in the "output" folder.
Project Structure

The project directory is organized as follows:

```
test_data_engineer/
│
├── input/
│   ├── sales.xlsx
│
├── output/
│
├── log/
│   ├── execution.log
│
├── config.ini
│
├── main.py
│
└── README.md
```
- The `input` folder contains the input Excel files with sales data.
- The `output` folder stores the resulting JSON files after processing.
- The `log` folder contains the execution log file.
- `config.ini` is the configuration file specifying paths and settings.
- `main.py` is the Python script responsible for processing the data.
- `README.md` (this file) provides project documentation and instructions.

## Getting Started

### Installation:

Install the required Python packages using the following command:

`pip install pandas openpyxl`

### Configuration:

Edit the config.ini file to set up the paths to the input, output, and log directories.

### Running the Script:

Run the script using the following command:

```css

    python3 main.py
```

The script will read Excel files from the input folder, clean and process the data, and save individual JSON files in the output folder. An execution log will be created in the log folder.

### Viewing Results:

The processed data will be saved as JSON files in the output folder. Each row of the input data corresponds to a JSON file with cleaned and enriched data.

### Additional Notes

The script employs the pandas library to read and manipulate data.
Data cleaning and enrichment operations can be customized in the script.
Make sure to review the script and adjust it to meet your specific requirements.
