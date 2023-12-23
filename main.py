import re
import PyPDF2

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
    pdf_path = 'test.pdf'

    extracted_emails = extract_emails_from_pdf(pdf_path)

    # Print the extracted emails
    if extracted_emails:
        print("Extracted Emails:")
        for email in extracted_emails:
            print(email)
    else:
        print("No emails found in the PDF.")
