from core.file_handler import FileHandler
from core.text_cleaner import TextCleaner

def run_pipeline():
    """
    Execute the complete data preprocessing pipeline for text data.
    
    This function orchestrates the entire data preprocessing workflow by:
    1. Loading raw text files from the 'data/raw' directory
    2. Applying text cleaning and preprocessing operations
    3. Saving the processed data to 'data/processed/cleaned_data.json'
    
    The pipeline uses the FileHandler class to manage file I/O operations and
    the TextCleaner class to perform text preprocessing tasks such as:
    - Removing special characters and noise
    - Normalizing text format
    - Tokenization and other cleaning operations
    
    Args:
        None
        
    Returns:
        None
        
    Raises:
        FileNotFoundError: If the input directory 'data/raw' doesn't exist
        PermissionError: If there are insufficient permissions to read/write files
        Exception: Any exceptions raised by FileHandler or TextCleaner operations
        
    Note:
        - Input files should be placed in 'data/raw/' directory
        - Output will be saved as 'data/processed/cleaned_data.json'
        - Progress messages are printed to console during execution
        - The pipeline assumes TextCleaner.process_dataset() returns JSON-serializable data
        
    Example:
        >>> run_pipeline()
        Starting ML Data Pipeline...
        Data preprocessing pipeline completed successfully.
    """

    print("Starting ML Data Pipeline...")

    # Initialize file handler and text processor
    handler = FileHandler(input_dir='data/raw', output_dir='data/processed')
    cleaner = TextCleaner()
    
    # Load raw text data from input directory
    raw_data = handler.load_text_files()
    
    # Process the dataset using the text processor
    cleaned_data = cleaner.process_dataset(raw_data)
    
    # Save the cleaned data to the output directory in JSON format
    handler.save_cleaned_data(cleaned_data, 'cleaned_data.json', file_format='json')
    print("Data preprocessing pipeline completed successfully.")

if __name__ == "__main__":
    run_pipeline()