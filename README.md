# Finance Assistant Project

Finance Assistant is a financial analysis tool designed to help users make informed investment decisions. This project uses Django for the backend and React for the frontend, enabling financial data analysis and visualization.

---

## Table of Contents
1. [Project Context](#project-context)
2. [Project Objectives](#project-objectives)
   - [Main Objective](#main-objective)
   - [Specific Objectives](#specific-objectives)
3. [Project Structure](#project-structure)
4. [Requirements](#requirements)
5. [Setup Instructions](#setup-instructions)
6. [Financial Data from API](#financial-data-from-api)
7. [Features](#Features)
7. [Contributing](#Contributing)
8. [License](#License)

---

## Project Context

Investing in the stock market is often perceived as complex and time-consuming, requiring expertise in financial analysis and access to detailed company data. This project aims to simplify the investment process for users by providing an intelligent virtual assistant that:
- Retrieves and analyzes financial reports.
- Calculates growth potential and financial health indicators.
- Presents data clearly through an interactive dashboard.

---

## Project Objectives

### Main Objective
Develop an intelligent virtual financial assistant that provides personalized and real-time investment advice.

### Specific Objectives
- Retrieve and analyze financial reports, including income statements, cash flow statements, and balance sheets.
- Calculate financial health indicators and growth potential.
- Present data visually to facilitate decision-making.
- Integrate a chatbot for conversational interaction.
- Develop an intuitive user interface for seamless user experience.

---

## Project Structure
- **`backend/`**: 
  - Django backend with REST API endpoints for financial data processing (e.g., `/analysis/`).
- **`frontend/`**: 
  - React frontend for user interaction and data visualization.(e.g., `/frontend/`)

---

## Requirements
- **Python 3.x**
- **Node.js and npm**
- **PostgreSQL** (or any other preferred database)

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/jbernardo6u/Finance_assistant.git
cd finance_assistant
```

### 2. Backend Setup
#### 2.1. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```
#### 2.2. Install dependencies:
```bash
pip install -r requirements.txt
```
#### 2.3. Apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```
#### 2.4. Start the server:
```bash
python manage.py runserver
```
### 3. Frontend Setup
#### 3.1. Navigate to the frontend directory and install dependencies:
```bash
cd frontend
npm install
```

#### 3.2. Start the React development server:
```bash
npm start
```

### 4. Verify Connectivity
Test the backend by visiting http://127.0.0.1:8000/.
Test the frontend by visiting http://localhost:3000/.

---

## Financial Data from API
### Income Statement Items
1. Total Revenue: Operating Revenue
2. Cost of Revenue: Cost of Goods Sold
3. Gross Profit: Gross Profit
4. General and Administrative Expense: Operating Expenses (General and Admin)
5. Selling General and Administration: Operating Expenses (Selling)
6. Selling and Marketing Expense: Operating Expenses (Selling and Marketing)
7. Research and Development: Operating Expenses (R&D)
8. Operating Expense: Sum of all Operating Expenses 
9. Operating Income: Operating Profit 
10. Interest Expense

### Cash Flow Items
1. Operating Cash Flow: Cash generated from operating activities 
2. Free Cash Flow: Operating Cash Flow - Capital Expenditure 
3. Capital Expenditure: Cash used for acquiring/maintaining assets

### Balance Sheet Items
1. Total Assets: Sum of all assets
2. Current Liabilities: Short-term liabilities
3. Stockholders' Equity: Shareholders' Equity
---
## Features
- Financial Data Analysis: Retrieve and process 10 years of financial reports.
- Indicators Calculation: Automatically compute financial health and growth indicators.
- Interactive Dashboard: Visualize financial data for better insights.
- Chatbot Integration: Offer users an interactive way to clarify financial data.
---
## Contributing
We welcome contributions! To contribute:

1. Fork the repository. 
2. Create a new branch (```git checkout -b feature-branch ```). 
3. Commit changes (``` git commit -m "Add new feature" ```). 
4. Push to your branch (``` git push origin feature-branch ```). 
5. Open a pull request.

---
## License
This project is licensed under the MIT License. (optional)

---
## Contact
For any inquiries or issues, please contact:
- Name: [José Bernardo](https://www.linkedin.com/in/jose-bernardo-research-engineer/)
- Email: [josebernardofisico@gmail.com](josebernardofisicio@gmail.com)
- GitHub: [jbernardo6u](https://github.com/jbernardo6u)

---

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/jose-bernardo-research-engineer/) [![GitHub](https://img.shields.io/badge/GitHub-Profile-black?style=flat-square&logo=github)](https://github.com/jbernardo6u) [![Instagram](https://img.shields.io/badge/Instagram-Follow-pink?style=flat-square&logo=instagram)](https://www.instagram.com/jb_bantu/)