import pdfplumber
import pandas as pd

def extract_tables_from_pdf(pdf_path, output_csv):
    """Extracts tables including headers from a PDF file and saves them as a CSV file."""
    all_tables = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                df = pd.DataFrame(table)
                all_tables.append(df)
    
    if all_tables:
        final_df = pd.concat(all_tables, ignore_index=True)
        final_df.to_csv(output_csv, index=False)
        print(f"Tables with headers extracted and saved to {output_csv}")
    else:
        print("No tables found in the PDF.")

# Example usage
pdf_path = r"D:\...\medication list\extractor\data\GHANA_EML_2017.pdf"  # Change to your local PDF file path
output_csv = r"D:\...\medication list\extractor\output\medication_extractor_with_headers.csv"  # Output CSV file path
extract_tables_from_pdf(pdf_path, output_csv)
