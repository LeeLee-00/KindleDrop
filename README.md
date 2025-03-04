# KindleDrop

KindleDrop is a Python-based application that enables users to send PDF documents directly to their Kindle devices via email. It uses a simple web interface built with Streamlit, allowing users to upload a PDF and send it to their Kindle's email address. This application supports various email providers like Outlook, Gmail, and Yahoo by utilizing their SMTP servers.

## Features

- **PDF Upload**: Users can upload PDF files they wish to send to their Kindle.
- **Email Integration**: Supports sending emails through Outlook, Gmail, and Yahoo.
- **Simple UI**: Built using Streamlit, the app offers a straightforward and easy-to-use interface.

## Installation

To set up KindleDrop on your local machine, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/LeeLee-00/KindleDrop
```

2. Navigate to the project directory:
```bash
cd KindleDrop
```

3. Install the required Python packages:
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
streamlit run app/main.py
```

## Usage

After starting the app, navigate to `http://localhost:8501` in your web browser. Follow the on-screen instructions to upload your PDF file and send it to your Kindle.

## Configuration

Ensure that the sender email address is added to your Kindle's approved personal document email list through your Amazon account settings.


## License

Distributed under the MIT License. See `LICENSE` for more information.
