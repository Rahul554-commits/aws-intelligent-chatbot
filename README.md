🤖 Intelligent Chatbot using AWS Services
📌 Overview

This project demonstrates the development of a cloud-native, intelligent chatbot application leveraging AWS services. The chatbot is capable of handling real-time, domain-specific queries (e.g., student services, FAQs) and provides context-aware responses with high availability and low latency.

🚀 Features

Natural Language Understanding using Amazon Lex

Serverless backend logic with AWS Lambda (Python)

Secure, scalable access via Amazon API Gateway

Role-based security using IAM Policies

Event-driven, real-time response architecture

Cloud-native and infrastructure-free deployment

📁 Project Structure
aws_intelligent_chatbot/
├── chatbot_configuration/         # Lex bot configuration files (JSON)
├── lambda_function/               # AWS Lambda function code (Python)
├── api_gateway/                   # API Gateway configuration (OpenAPI/Swagger)
├── architecture_diagram.png       # High-level architecture diagram (optional if Mermaid used)
├── IAM_roles_notes.md             # IAM roles and permissions documentation
├── LICENSE                        # MIT License
└── README.md                      # Project documentation (this file)

🧠 Technologies Used

AWS Lex – Natural language understanding

AWS Lambda – Serverless backend compute

Amazon API Gateway – Secure API exposure

IAM – Secure execution roles and policies

Python – Lambda function development

CloudWatch – Monitoring and logs

📊 Architecture

flowchart TD
    User([👤 User]) --> Lex["🤖 Amazon Lex"]
    Lex --> Lambda["⚡ AWS Lambda - index.py"]
    Lambda --> APIGW["🌐 Amazon API Gateway (/chat endpoint)"]
    APIGW --> User
    Lex --> IAM["🔒 IAM Roles (Permissions)"]
    Lambda --> IAM
    APIGW --> IAM

    %% Styling
    classDef aws fill=#FF9900,stroke=#232F3E,color=white,stroke-width=2px;
    classDef user fill=#4CAF50,stroke=#1B5E20,color=white,stroke-width=2px;
    classDef sec fill=#232F3E,stroke=#FF9900,color=white,stroke-width=2px;

    class Lex,APIGW,Lambda aws;
    class User user;
    class IAM sec;

    

🔧 Setup Instructions

    Create the Lex Bot

        Use chatbot_configuration/lex_bot.json or manually define intents using the AWS Console.

    Deploy Lambda Function

        Upload lambda_function/index.py in AWS Lambda Console.

        Ensure the Lambda has an IAM role with permissions to log to CloudWatch and access Lex.

    Connect Lex with Lambda

        In your Lex bot, set the fulfillment Lambda ARN in the intent configuration.

    Set Up API Gateway (Optional)

        Use api_gateway/openapi_definition.json to import or manually create a POST method to trigger the Lambda.

    Test the Chatbot

        Use the Lex Test console or API Gateway endpoint to simulate queries.

🔐 IAM Roles & Security

Refer to IAM_roles_notes.md for detailed role configuration, ensuring least privilege principle is followed.
📜 License

This project is licensed under the MIT License. See LICENSE
for more information.
