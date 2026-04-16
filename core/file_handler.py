import os
import json
import csv


class FileHandler:
    """
    Handles file I/O operations for the data preprocessing pipeline.
    
    This class provides methods to load text files and save processed data
    in various formats (JSON, CSV).
    
    Attributes:
        input_dir (str): Directory path for input files
        output_dir (str): Directory path for output files
    """
    
    def __init__(self, input_dir, output_dir):
        """
        Initialize FileHandler with input and output directories.
        
        Args:
            input_dir (str): Path to the directory containing input files
            output_dir (str): Path to the directory where output files will be saved
        """
        self.input_dir = input_dir
        self.output_dir = output_dir
        
    def load_text_files(self):
        """
        Load all text files from the input directory line by line.
        """
        files = os.listdir(self.input_dir)
        text_lines = []
        for file in files:
            if file.endswith('.txt'):
                with open(os.path.join(self.input_dir, file), 'r', encoding='utf-8') as f:
                    # Extend adds each line as a separate item in the list
                    text_lines.extend(f.readlines()) 
        return text_lines 
        
    def save_cleaned_data(self, processed_data, filename, file_format='json'):
        """
        Save processed data to either JSON or CSV format.
        
        This method saves data in the specified format to the output directory.
        Automatically manages file extensions to ensure correct format handling.
        
        Args:
            processed_data: Data to save. 
                - For JSON: Can be any JSON-serializable structure (dict, list, etc.)
                - For CSV: Should be a list of dicts (with headers) or list of lists (rows)
            filename (str): Name of the output file (extension is managed automatically)
            file_format (str): Output format - 'json' or 'csv' (default: 'json')
            
        Returns:
            None
            
        Raises:
            IOError: If the output directory doesn't exist or isn't writable
            TypeError: If data cannot be serialized to the specified format
            
        Note:
            - File extensions are automatically handled (.json or .csv)
            - UTF-8 encoding is used for both formats
            - CSV with dict data will include headers automatically
            - For empty data, an empty file will be created
            
        Examples:
            # Save as JSON (default)
            handler.save_cleaned_data(data, 'output.json')
            
            # Save as CSV
            handler.save_cleaned_data(data, 'output', file_format='csv')
        """
        output_path = os.path.join(self.output_dir, filename)
        
        if file_format.lower() == 'csv':
            # Ensure filename has .csv extension
            if not output_path.endswith('.csv'):
                output_path = output_path.replace('.json', '.csv') if '.json' in output_path else output_path + '.csv'
            
            with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
                if isinstance(processed_data, list) and len(processed_data) > 0:
                    if isinstance(processed_data[0], dict):
                        writer = csv.DictWriter(csvfile, fieldnames=processed_data[0].keys())
                        writer.writeheader()
                        writer.writerows(processed_data)
                    else:
                        writer = csv.writer(csvfile)
                        writer.writerows(processed_data)
        else:  # Default to JSON
            # Ensure filename has .json extension
            if not output_path.endswith('.json'):
                output_path = output_path.replace('.csv', '.json') if '.csv' in output_path else output_path + '.json'
            
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(processed_data, f, indent=4)
        
    
    
        