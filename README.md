# Extract Emails From PDFs

This is a simple script to extract emails from PDFs. I made it specifically to facilitate the process of extracting emails from resumes in my job. It uses [PyPDF2](https://github.com/py-pdf/pypdf) to read the PDFs and [regular expressions](https://docs.python.org/3/library/re.html) to find the emails.

## Installation

Clone the repository and install the requirements:

```bash
git clone https://github.com/youssef-attai/extract-emails-from-pdfs.git
cd extract-emails-from-pdfs
pip install -r requirements.txt
```

## Usage

```bash
python main.py <path_to_pdf_directory>
```

The script will create 2 files: `extracted_emails.txt` and `pdfs_without_emails.txt`. The first file contains all the emails extracted from the PDFs and the second file contains the names of the PDFs that the regex couldn't find an email in.

## Note to applicants

If you are applying for a job and you are asked to send your resume, PLEASE, FOR GOD'S SAKE, WRITE YOUR GODDAMN EMAIL IN THE FUCKING RESUME. AND YOU BETTER MAKE SURE IT'S WRITTEN IN PURE, PLAIN TEXT. NOT AN IMAGE, NOT A `mailto:` LINK, JUST GOOD OLD PLAIN TEXT BECAUSE IT CONFUSES MY PUNY REGEX. Thank you.

## License

This project is licensed under the terms of the [MIT](LICENSE) license.
