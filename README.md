# Inventory Management System- Web App

## Project Overview

This project is a web-based *Inventory Management System* designed to bridge the gap between core software development and enterprise resource planning (ERP) workflows. Built as part of my B.Tech specialization in *SAP*, it demonstrates how a backend system can manage warehouse stock, track pricing, and automate critical business alerts.

## Features

* *Real-time Stock Tracking:* Add and monitor product quantities and pricing via a dynamic web interface.
* *SAP-Style Material Alerts:* Automated "Low Stock" triggers that mimic the Material Management (MM) module in SAP HANA.
* *Persistent Data Storage:* Utilizes a structured SQL database to ensure data integrity and persistence.
* *Responsive UI:* A clean, user-friendly dashboard built with HTML5 and CSS3.

## Tech Stack

* *Backend:* Python (Flask Framework)
* *Frontend:* HTML5, CSS3 (Vanilla)
* *Database:* SQLite / SQL
* *Logic:* Object-Oriented Programming (OOP) in Python

## SAP Integration Logic

As a student specializing in SAP, I implemented this project to simulate real-world *ERP workflows*:

1. *Threshold Management:* Just like in SAP MM, every item has a "Safety Stock" level.
2. *Alert System:* When stock falls below the safety level, the system flags the item for reordering, simulating an automated purchase requisition flow.

## Installation & Setup

1. *Clone the repository:*
git clone https://github.com/your-username/inventory-management-system.git

2. *Create virtual environment*
python -m venv .env

3. *Activate virtual environment*
.env\scripts\Activate

4. *Install dependencies:*
pip install flask

5. *Run the application:*
python app.py

6. *Access the dashboard:*
Open http://127.0.0.1:5000/ in your browser.

## Author

*Svara Pankilkumar Shah* 

B.Tech CSE (Industry Embedded with SAP) | 2nd Year 

