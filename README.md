**Weather Data Collection System**

- This project collects real-time weather information for multiple cities and stores the results in an AWS S3 bucket.
It demonstrates Python development, API integration, cloud storage, error handling, and DevOps practices including Infrastructure as Code and version control.

**Features**

1. Fetches real-time weather data from the OpenWeather API

2. Collects temperature, humidity and weather conditions

3. Supports multiple cities

4. Stores weather data in AWS S3 for historical tracking

5. Uses environment variables for sensitive keys

6. Includes Infrastructure as Code using Terraform

7. Version control using Git and GitHub

**How the System Works**

- The user runs the Python script.

- The script loads configuration from the .env file.

- It connects to the OpenWeather API and fetches weather details for each city.

- Weather data is formatted with a timestamp.

- The data is uploaded as a JSON file into an AWS S3 bucket.

- The terminal displays the collected weather details.

- Every run creates a new file in S3, allowing historical data storage.

**Architecture Diagram**
   
                 
                 
                 ┌──────────────────────────────────┐
                 │        Step 1: Developer         │
                 │  Writes Python code + Terraform  │
                 └──────────────────────────────────┘
                                  │
                                  ▼
                 ┌──────────────────────────────────┐
                 │     Step 2: GitHub Repository    │
                 │ Developer pushes all code to Git │
                 └──────────────────────────────────┘
                                  │
                                  ▼
                 ┌──────────────────────────────────┐
                 │  Step 3: GitHub Actions (CI)     │
                 │ - Install dependencies           │
                 │ - Syntax check                   │
                 │ - Validate code                  │
                 └──────────────────────────────────┘
                                  │
                                  ▼
                 ┌──────────────────────────────────┐
                 │  Step 4: GitHub Actions (CD)     │
                 │ Triggered only if CI succeeds    │
                 └──────────────────────────────────┘
                       │                    │
                       │                    │
                       ▼                    ▼
    ┌──────────────────────────┐     ┌──────────────────────────┐
    │ Step 5: Terraform (IaC)  │     │ Step 6: Run Python App   │
    │ - Creates/updates S3     │     │ python -m src.main       │
    │ - Manages infrastructure │     └──────────────────────────┘
    └──────────────────────────┘                    │
                       │                            ▼
                       ▼              ┌──────────────────────────────────┐
         ┌──────────────────────┐    │ Step 7: Load Configuration        │
         │ AWS S3 Bucket        │    │ Reads .env or GitHub Secrets      │
         │ weather-data-devops  │    └──────────────────────────────────┘
         └──────────────────────┘                            │
                                                             ▼
                                           ┌──────────────────────────────────┐
                                           │ Step 8: Call OpenWeather API    │
                                           │ Fetch weather for each city     │
                                           └──────────────────────────────────┘
                                                             │
                                                             ▼
                                           ┌──────────────────────────────────┐
                                           │ Step 9: Prepare Weather Data     │
                                           │ Temp, humidity, condition, time  │
                                           └──────────────────────────────────┘
                                                             │
                                                             ▼
                                           ┌──────────────────────────────────┐
                                           │ Step 10: Upload JSON to S3       │
                                           │ Using boto3 PutObject            │
                                           └──────────────────────────────────┘
                                                             │
                                                             ▼
                                           ┌──────────────────────────────────┐
                                           │ Step 11: Logs and Output         │
                                           │ Printed in Terminal or GitHub    │
                                           └──────────────────────────────────┘

**Architecture Diagram Summary:**
- The system reads settings from a .env file, fetches weather data from the OpenWeather API using Python, and uploads the processed results as JSON files to an AWS S3 bucket, with all code and infrastructure managed through GitHub and Terraform.

**Weather Output (Terminal Results)**

<img width="1366" height="768" alt="Screenshot (65)" src="https://github.com/user-attachments/assets/656d5938-bbd2-4d78-b8f2-bf270f8b5a3e" />

**S3 Uploaded File**

<img width="1366" height="768" alt="Screenshot (67)" src="https://github.com/user-attachments/assets/324760b6-f0f7-4503-8ef0-05874bd7d372" />

**View the JSON Content**

<img width="1366" height="768" alt="Screenshot (68)" src="https://github.com/user-attachments/assets/dd19765f-6f41-4024-8edb-13130586aa54" />

**Overall Project Summary**

- This project collects real-time weather information for multiple cities and stores the data safely in an AWS S3 bucket. The application is built using Python and uses the OpenWeather API to get temperature, humidity, and weather conditions. All settings, such as API keys and city names, are stored in a .env file so the code remains clean and secure.

- After collecting the weather data, the program creates a JSON file with a timestamp and uploads it to an S3 bucket using boto3. Every run creates a new file, which helps maintain a history of weather data. The terminal shows the weather results and whether the upload was successful.

- The project also includes Terraform for Infrastructure as Code, which allows the S3 bucket to be created and managed in an automated and repeatable way. All code is stored in a GitHub repository, showing proper version control and DevOps practices. The project demonstrates API integration, environment management, cloud usage, and automation in a simple and understandable workflow.


