# Milla Contract Generator
A Python-based real estate contract generator designed to automate document creation and streamline administrative workflows, integrated with Microsoft Power Automate Desktop.

## Overview
Milla Contract Generator is a project developed to simplify and automate the creation of real estate purchase and sale contracts.
The application collects structured information through a terminal interface, validates input data, and generates Word documents (`.docx`) using a predefined contract template.
The project also integrates Microsoft Power Automate Desktop to automate the execution of the Python application and the organization of generated contracts.

## Features
- Structured data collection through a command-line interface.
- Input validation to improve data consistency.
- Automated generation of Word documents (`.docx`).
- Document generation based on a predefined template.
- Automatic file organization using Microsoft Power Automate Desktop.
- Automatic transfer of generated contracts to a destination folder.

## Technologies Used
- **Python 3.14**
- **Microsoft Power Automate Desktop**
- **Python-docx**
- **Git and GitHub**
- **Microsoft Word**

## Project Structure
```text
milla-contract-generator/
│
├── templates/
│   └── contrato_compra_venda.docx
│
├── output/
│
├── power-automate/
│   └── Milla-Gerador-Contrato.txt
│
├── main.py
├── contract_generator.py
├── validators.py
├── .gitignore
└── README.md
```

## How It Works
1. The user launches the Python application.
2. Contract information is entered through the terminal.
3. The application validates the provided information.
4. A Word contract is generated using the predefined template.
5. Power Automate Desktop waits for the Python process to finish.
6. The generated document is identified and automatically moved to the destination folder.

## How to Run

### Requirements
- Python 3.14 or compatible version.
- Microsoft Word or another application compatible with `.docx` files.
- Microsoft Power Automate Desktop (for workflow automation).

### Install Dependencies
```bash
pip install python-docx
```

### Run the Application
From the project directory, execute:
```bash
python main.py
```
Follow the terminal instructions to enter the contract information.

## Power Automate Desktop Integration
The project includes a Microsoft Power Automate Desktop workflow that:
- Executes the Python application.
- Waits for the application to finish.
- Searches for generated `.docx` files.
- Selects the most recently modified file.
- Moves the document to the designated contracts folder.

The workflow's textual documentation is available in the `power-automate/` directory.
**Note:** The `.txt` file documents the workflow actions; it is not an importable Power Automate Desktop flow package.

## Disclaimer
This project is intended for educational and workflow automation purposes. Generated contracts must be reviewed by qualified professionals before being used in actual real estate transactions.

## Author
**Enzo Oliveira**
Computer Science Student | FEI
GitHub: [Enzouu-code](https://github.com/Enzouu-code)
