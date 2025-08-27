# 🤖 Intelligent Chatbot using AWS Services

## Overview

This project demonstrates the development of a cloud-native, intelligent chatbot application leveraging various AWS services. The chatbot is capable of handling real-time, domain-specific user queries (e.g., student services, FAQs) and provides context-aware responses with high availability and low latency.

## 🚀 Features

- Natural Language Understanding using **Amazon Lex**
- Serverless backend logic with **AWS Lambda (Python)**
- Secure, scalable access via **Amazon API Gateway**
- Role-based security using **IAM Policies**
- Event-driven, real-time response architecture
- Cloud-native and infrastructure-free deployment

## 📁 Project Structure

```
aws_intelligent_chatbot/
├── chatbot_configuration/         # Lex bot configuration files (JSON)
├── lambda_function/               # AWS Lambda function code (Python)
├── api_gateway/                   # API Gateway configuration (OpenAPI/Swagger)
├── architecture_diagram.png       # High-level architecture diagram
├── IAM_roles_notes.md             # IAM roles and permissions documentation
├── LICENSE                        # MIT License
└── README.md                      # Project documentation (this file)
```

## 🧠 Technologies Used

- **AWS Lex** – Natural language understanding
- **AWS Lambda** – Serverless backend compute
- **Amazon API Gateway** – Secure API exposure
- **IAM** – Secure execution roles and policies
- **Python** – Lambda function development
- **CloudWatch** – Monitoring and logs

## 📊 Architecture

```mermaid
flowchart LR
    User([User]) --> Lex["Amazon Lex"]
    Lex --> Lambda["AWS Lambda - index.py"]
    Lambda --> APIGW["Amazon API Gateway (/chat endpoint)"]
    APIGW --> User
    Lex --> IAM["IAM Roles (Permissions)"]
    Lambda --> IAM
    APIGW --> IAM


---

## 🔧 Setup Instructions

1. **Create the Lex Bot**  
   - Use `chatbot_configuration/lex_bot.json` or manually define intents using the AWS Console.  

2. **Deploy Lambda Function**  
   - Upload `lambda_function/index.py` script in AWS Lambda Console.  
   - Ensure the Lambda has an IAM role with permissions to log to CloudWatch and access Lex.  

3. **Connect Lex with Lambda**  
   - In your Lex bot, set the fulfillment Lambda ARN in the intent configuration.  

4. **Set Up API Gateway (Optional)**  
   - Use `api_gateway/openapi_definition.json` to import or manually create a POST method to trigger the Lambda.  

5. **Test the Chatbot**  
   - Use the Lex Test console or API Gateway endpoint to simulate queries.  

---

## 🔐 IAM Roles & Security
Refer to `IAM_roles_notes.md` for detailed role configuration, ensuring minimal privileges are used.  

---

## 📜 License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for more information.  



