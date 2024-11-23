import os
import requests
import csv

def upload_eml_file(url, file_path):
    """
    Uploads an .eml file to the specified URL and returns the server response.

    Parameters:
    url (str): The URL of the Flask application.
    file_path (str): The path to the .eml file.

    Returns:
    dict: The JSON response from the server.
    """
    with open(file_path, 'rb') as file:
        files = {'file': file}
        response = requests.post(url, files=files)
    return response.json()

def process_eml_files(folder_path, url, output_csv):
    """
    Processes all .eml files in the specified folder, sends them to the URL, and stores the responses in a CSV file.

    Parameters:
    folder_path (str): The path to the folder containing .eml files.
    url (str): The URL of the Flask application.
    output_csv (str): The path to the output CSV file.
    """
    results = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.eml'):
            file_path = os.path.join(folder_path, filename)
            response = upload_eml_file(url, file_path)
            results.append(response)

    if results:
        # Define custom order for headers
        ordered_headers = [
            'date',
            'customer_email',
            'subject',
            'customer_name',
            'order_id',
            'sentiment',
            'score',
            'feedback_category',
            'feedback_summary',
            'action_needed'
        ]
        
        # Write the results to a CSV file with pipe delimiter
        with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=ordered_headers, delimiter='|')
            writer.writeheader()
            for result in results:
                writer.writerow(result)

# Define the URL of the Flask application
url = 'https://extract-details.onrender.com'

# Path to the folder containing .eml files
folder_path = r'C:\Emails\SaveIMAPmail'

# Path to the output CSV file
output_csv = r'C:\Emails\eml_responses.csv'

# Process the .eml files and store the responses in a CSV file
process_eml_files(folder_path, url, output_csv)