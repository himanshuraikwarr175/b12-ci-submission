import json
import hmac
import hashlib
import requests
from datetime import datetime, timezone
import os
from dotenv import load_dotenv


load_dotenv()
URL = "https://b12.io/apply/submission"

if not URL:
    raise ValueError("API_URL must be set")

SECRET = "hello-there-from-b12"

# - TIMESTAMP -
timestamp = datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


payload = {
    "action_run_link": os.environ["ACTION_RUN_LINK"],
    "email": "himanshu.raikwarr175@gmail.com",
    "name": "Himanshu",
    "repository_link": os.environ["REPO_LINK"],
    "resume_link": "https://drive.google.com/file/d/1GB45psY-X0S7pIW88CuCYSbRjrlrUlkz/view?usp=sharing",
    "timestamp": timestamp
}


body_str = json.dumps(payload, separators=(',', ':'), sort_keys=True)
body_bytes = body_str.encode("utf-8")


# - HMAC SHA256 SIGNATURE -
signature = hmac.new(
    key=SECRET.encode("utf-8"),
    msg=body_bytes,
    digestmod=hashlib.sha256
).hexdigest()

headers = {
    "Content-Type": "application/json",
    "X-Signature-256": f"sha256={signature}"
}

# - POST REQUEST -
response = requests.post(URL, data=body_bytes, headers=headers)

# - PRINT RECEIPT -
if response.status_code == 200:
    data = response.json()
    print("Receipt:", data.get("receipt"))
else:
    raise Exception("Submission failed with status:", response.status_code)
