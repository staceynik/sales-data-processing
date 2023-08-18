import pandas as pd
import json
import os
import logging
import configparser

class DataProcessor:
    def __init__(self, config):
        self.config = config
        self.log_path = self.config['LOG']['LogPath']
        self.input_path = self.config['PATHS']['InputPath']
        self.output_path = self.config['PATHS']['OutputPath']

    def read_excel(self, file_path):
        return pd.read_excel(file_path)

    def clean_data(self, df):
        # Perform data cleaning and enrichment operations as needed
        # ...

        return df

    def process_data(self):
        logging.basicConfig(filename=self.log_path, level=logging.INFO)

        input_files = os.listdir(self.input_path)
        for input_file in input_files:
            input_file_path = os.path.join(self.input_path, input_file)
            df = self.read_excel(input_file_path)
            cleaned_df = self.clean_data(df)

            output_file_name = os.path.splitext(input_file)[0] + '.json'
            output_file_path = os.path.join(self.output_path, output_file_name)

            cleaned_df.to_json(output_file_path, orient='records', lines=True)
            logging.info(f'Processed {input_file} and saved {output_file_name}')

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.ini')  # Provide the path to your config file
    processor = DataProcessor(config)
    processor.process_data()
