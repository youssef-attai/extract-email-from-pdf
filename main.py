import re
import PyPDF2
import os

def extract_emails_from_pdf(pdf_path):
    emails = set()

    # Open the PDF file
    with open(pdf_path, 'rb') as pdf_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Iterate through each page in the PDF
        for page_num in range(len(pdf_reader.pages)):
            # Get the text content of the page
            page_text = pdf_reader.pages[page_num].extract_text()

            # Use a regular expression to find email addresses
            email_matches = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', page_text)

            # Add the found email addresses to the set
            emails.update(email_matches)

    return emails

if __name__ == "__main__":
    pdf_directory = input("Enter the path to the directory containing PDF files: ")
    pdf_directory = os.path.expanduser(pdf_directory)  # Expand ~ in the directory path

    # Initialize a list to store the filenames of PDFs without emails
    pdfs_without_emails = []

    # Initialize a list to store the extracted emails
    extracted_emails = []

    # Loop over all PDF files in the directory
    for filename in os.listdir(pdf_directory):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(pdf_directory, filename)

            emails = extract_emails_from_pdf(pdf_path)

            # Add the extracted emails to the list
            extracted_emails.extend(emails)

            # Check if any emails were extracted
            if not emails:
                pdfs_without_emails.append(filename)

    # Write the extracted emails to a file
    with open("extracted_emails.txt", "w") as email_file:
        for email in extracted_emails:
            email_file.write(email + "\n")

    # Write the filenames of PDFs without emails to a file
    with open("pdfs_without_emails.txt", "w") as pdf_file:
        for filename in pdfs_without_emails:
            pdf_file.write(filename + "\n")
