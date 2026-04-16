import re
from typing import List, Dict

class TextCleaner:
    """A class to clean and preprocess structured text data."""

    def remove_html_tags(self, text: str) -> str:
        """Remove HTML tags entirely before stripping special characters."""
        return re.sub(r'<[^>]+>', ' ', text)

    def remove_special_characters(self, text: str) -> str:
        """Remove punctuation and special characters from text."""
        return re.sub(r'[^a-zA-Z0-9\s]', '', text)

    def normalize_whitespace(self, text: str) -> str:
        """Fix multiple spaces and tab characters."""
        return ' '.join(text.split())

    def to_lowercase(self, text: str) -> str:
        """Convert text to lowercase."""
        return text.lower()

    def process_dataset(self, raw_data: List[str]) -> List[Dict[str, str]]:
        """
        Parse the delimited dataset, skip invalid rows, and apply 
        cleaning methods ONLY to the text portion.
        """
        cleaned_data = []
        
        for line in raw_data:
            # Clean up the line break at the end of the string
            line = line.strip()
            
            # Skip completely empty lines
            if not line:
                continue
                
            # Split the data by the pipe delimiter
            parts = line.split('|')
            
            # Ensure the row is valid (User ID, Prod ID, Text)
            if len(parts) != 3:
                continue 
                
            user_id, prod_id, review_text = parts
            
            # Skip rows where the review text is missing
            if not review_text.strip():
                continue

            # Apply cleaning pipeline ONLY to the review text
            cleaned_text = self.remove_html_tags(review_text)
            cleaned_text = self.remove_special_characters(cleaned_text)
            cleaned_text = self.normalize_whitespace(cleaned_text)
            cleaned_text = self.to_lowercase(cleaned_text)
            
            # Structure the output for JSON/CSV export
            cleaned_data.append({
                'user_id': user_id.strip(),
                'product_id': prod_id.strip(),
                'original_review': review_text.strip(),
                'cleaned_review': cleaned_text
            })
        
        return cleaned_data