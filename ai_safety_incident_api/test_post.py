import requests

print("📢 Starting API request...")  # <-- NEW LINE

url = "http://127.0.0.1:5000/incidents"

data = {
    "title": "Bias Filtering",
    "description": "Showing bias in filtering resumes",
    "severity": "Medium"
}

response = requests.post(url, json=data)

print("✅ Status Code:", response.status_code)
print("📦 Response JSON:", response.json())
