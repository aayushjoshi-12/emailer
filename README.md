# Emailer Project

This project allows you to send emails to a list of recruiters using Gmail API.

## Prerequisites

Before you can use this project, you need to complete the following steps:

1. Download the `credentials.json` file from the [Google Cloud Console](https://console.cloud.google.com/).
    - Go to the [APIs & Services](https://console.cloud.google.com/apis/credentials) page.
    - Create a new project or select an existing one.
    - Enable the Gmail API.
    - Create credentials and download the `credentials.json` file.
    - Add it to project directory.

2. Add a `recruiters.xlsx` file with all the email addresses of the recruiters you want to send emails to.

3. Modify the `credentials.py` file to add your own credentials.

4. Add your resume as `resume.pdf` in the project directory.

## Installation

To set up this project, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/aayushjoshi-12/emailer.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the project:

    ```bash
    python main.py
    ```

That's it! You should now be able to send emails to the recruiters using the Gmail API.

## License

This project is licensed under the [MIT License](LICENSE).