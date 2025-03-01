# Medication Extractor

## Overview

The **Medication Extractor** project is a Python-based tool that extracts medication tables from a PDF document and saves them as a structured CSV file. This allows for easier data manipulation and analysis.

## Project Structure

```plaintext
medication_extractor/
│── src/
│   ├── extract.py         # Python script for extracting tables
│── data/
│   ├── GHANA_EML_2017.pdf # Source PDF file containing medication list
│── output/
│   ├── medication_extractor_with_headers.csv  # Extracted CSV output
│── venv/                   # Virtual environment (optional)
│── requirements.txt        # Dependencies list
│── .gitignore              # Ignore unnecessary files
│── README.md               # Project documentation
```

## Prerequisites

Ensure you have Python installed (Python 3.6 or later). You also need the following dependencies:

- `pdfplumber` (for extracting tables from PDF)
- `pandas` (for handling tabular data)

To install the required libraries, run:

```bash
pip install -r requirements.txt
```

## How to Use

1. Place the target PDF file in the `data/` folder.
2. Update the `pdf_path` and `output_csv` variables in `src/extract.py` to match your file paths.
3. Run the script:
   ```bash
   python src/extract.py
   ```
4. The extracted data will be saved as a CSV file in the `output/` folder.

## File Paths (Default)

- **Input PDF:** `D:\ObedVideos\medication list\extractor\data\GHANA_EML_2017.pdf`
- **Output CSV:** `D:\ObedVideos\medication list\extractor\output\medication_extractor_with_headers.csv`

## Notes

- The script automatically detects and extracts tables, including headers.
- If no tables are found, it prints a message and exits without creating an output file.

## Contributing

Feel free to modify and improve the script. If you encounter any issues, open a pull request or create an issue.

## License

This project is open-source and available under the MIT License.
