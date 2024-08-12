## Setup Instructions

Follow these steps to set up the project on your local machine.

### Prerequisites

- Python 3.x
- Gemini API credentials

### 1. Clone the Repository

Clone the repository to your local machine using Git:

git clone https://github.com/abdul786rasool/smart-os.git
cd smart-os

### 2. Create and Activate a Virtual Environment

Create and activate a virtual environment to isolate your project dependencies.

- **On Windows:**

python -m venv env
.\env\Scripts\activate

- **On macOS/Linux:**

python3 -m venv env
source env/bin/activate

### 3. Install Dependencies

Install the necessary libraries and dependencies using the `requirements.txt` file:

pip install -r requirements.txt

### 4. Add Credentials to `.env` File

Create a `.env` file in the root of your project directory and add the following credentials:

GOOGLE_API_KEY=your_google_api_key

GOOGLE_APPLICATION_CREDENTIALS=path_to_your_google_application_credentials

GOOGLE_PROJECT_ID=your_google_project_id

BRAVE_API_KEY=your_brave_api_key

DESKTOP=path_to_your_desktop

DOWNLOADS=path_to_your_downloads

### 5. Run the Application

Start the application using Streamlit:

streamlit run app.py

### 6. Use the Streamlit App

In the Streamlit app, you'll find three options in the sidebar:

- **Fetch all files:** Click this to retrieve all necessary files.
- **Create Embeddings:** Click this to generate embeddings. (Note: This process may take 2-3 hours.)
 No need to do update files.

Complete these steps one by one for the best results.
