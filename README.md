# b12-ci-submission
A simple Python script that submits a structured application payload to B12’s API with proper HMAC-SHA256 signing. The project also includes a GitHub Actions workflow to automate the submission and provide a verifiable run link.

The system performs the following:
- Generates a structured JSON payload
- Signs the payload using HMAC SHA256
- Sends a POST request to the B12 submission API
- Prints a receipt upon successful submission
- Executes automatically using GitHub Actions (CI)

## Tech Stack
- Python 3.10+
- Requests Library
- HMAC & Hashlib (for secure signing)
- GitHub Actions (CI/CD Automation)

##  Project Structure
.
├── .github/
│ └── workflows/
│ └── submit.yml
├── app/
│ └── submit.py
├── requirements.txt
└── README.md


##  Setup Instructions
### 1. Clone the Repository
git clone <your-repo-url>
cd b12-ci-submission
### 2. Install Dependencies
pip install -r requirements.txt
### 3. Environment Variables

The script uses the following environment variables:

- `REPO_LINK` → GitHub repository URL  
- `ACTION_RUN_LINK` → GitHub Actions run URL  

These are automatically injected via GitHub Actions.

## Running the Script Locally

You can run the script manually:


export REPO_LINK="your_repo_url"
export ACTION_RUN_LINK="your_action_run_url"

python app/submit.py


##  Security Mechanism

- Payload is serialized using JSON
- Signed using **HMAC SHA256**
- Signature is passed via header:


X-Signature-256: sha256=<signature>


This ensures:
- Data integrity
- Authenticity of the request



## API Payload Structure

```json
{
  "action_run_link": "...",
  "email": "...",
  "name": "...",
  "repository_link": "...",
  "resume_link": "...",
  "timestamp": "..."
}
