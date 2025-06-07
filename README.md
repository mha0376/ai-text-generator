# AI Text Generator

![Python](https://img.shields.io/badge/python-3.12+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![FastAPI](https://img.shields.io/badge/fastapi-0.115.2-orange.svg)
![OpenAI](https://img.shields.io/badge/openai-1.35.7-blue.svg)

**AI Text Generator** is a sophisticated web application built with **FastAPI** and powered by the **OpenAI API** to create diverse text outputs, such as stories, summaries, and analyses, based on user prompts. Designed for writers, developers, and AI enthusiasts, this project offers a user-friendly interface to explore the creative potential of AI-driven text generation.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Debugging](#debugging)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Versatile Text Generation**: Generate stories, summaries, or analyses tailored to custom prompts.
- **Intuitive Web Interface**: Clean UI with options to select output types and adjust token limits.
- **High-Performance Backend**: FastAPI ensures fast, asynchronous API processing.
- **Secure Configuration**: Safely store API keys using `.env` files.
- **Extensible Architecture**: Modular design for easy feature additions or customizations.
- **Open-Source**: Licensed under MIT for community collaboration and reuse.

## Tech Stack
- **Backend**: FastAPI, Uvicorn
- **Frontend**: Jinja2 templates, HTML, CSS, JavaScript
- **AI Integration**: OpenAI API
- **Environment Management**: python-dotenv
- **Testing**: Pytest, httpx
- **Version Control**: Git, GitHub

## Prerequisites
To run the project, ensure you have:
- **Python**: Version 3.12 or higher
- **OpenAI API Key**: Obtain from [OpenAI Platform](https://platform.openai.com/)
- **Git**: Installed for cloning the repository
- **Virtual Environment**: Recommended for dependency isolation

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mha0376/ai-text-generator.git
   cd ai-text-generator

2. **Create a Virtual Environmenty**:
    ```bash
      python3 -m venv venv
      source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Environment: Create a .env file and add your OpenAI API key**:
    ```bash
    echo "OPENAI_API_KEY=your-openai-api-key" > .env
    ```

5. **Run the Server**:
    ```bash
    uvicorn app.main:app --reload
    ```
    Open <a ref="http://localhost:8000">http://localhost:8000</a> in your browser.

## Usage
1. **Open the Web Interface**:
   Navigate to <a ref="http://localhost:8000">http://localhost:8000</a>.
2. **Enter a Prompt**:
   Example: "A lone robot in a futuristic city abandoned by humans"
3. **Select Output Type**:
   Choose Story, Summary, or Analysis from the dropdown.
4. **Set Max Tokens**:
   Specify the token limit (e.g., 150) to control output length.
5. **Generate Text**:
   Click the "Generate" button to view the AI-generated text.

  ### Sample Output (Story, 150 tokens):
  "Elara, a lone robot, roamed the desolate streets of a futuristic city, 
    its skyscrapers silent and crumbling. Programmed to serve humans, it now 
    wandered without purpose. One evening, it found a faded mural of a child’s 
    smile, glowing faintly beneath the dust. Ignited by hope, Elara began repairing 
    the city’s lights, each flicker a dream of reviving the world it once knew."

## Project Structure
  ```
  ai-text-generator/
│
├── app/
│   ├── __init__.py       # Package initialization
│   ├── main.py           # FastAPI application entry point
│   ├── ai_service.py     # OpenAI API integration logic
│   └── templates/
│       └── index.html    # Web interface template
│
├── static/
│   ├── script.js         # Client-side JavaScript
│   └── style.css         # CSS styles
│
├── .env                  # Environment variables (not tracked)
├── .gitignore            # Git ignore patterns
├── LICENSE               # MIT License
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
```

## Debugging

  #### Server-Side Errors:
  - Check Uvicorn logs for issues like AuthenticationError or TypeError.
  - Look for messages such as Raw API response or Error in generate_text.

  #### Client-Side Errors:
  - Open browser Developer Tools (F12) and inspect Console/Network tabs.

  #### API Key Issues:
  - Verify the OpenAI API key in .env is valid and has sufficient credits.

  #### Dependency Conflicts:
  - Ensure all packages are installed:
    ```
    pip install -r requirements.txt
    ```

  #### Nix Environment:
  - Set PYTHONPATH if using Nix:
    ```
    export PYTHONPATH=$PYTHONPATH:/home/user/ai-textgenerator/ai-text-generator
    ```
  - Install dependencies:
    ```
    nix-shell -p python312 git
    ```
    nix-shell -p python312 git

  ## Contributing
  We welcome contributions to enhance AI Text Generator! To contribute:

  1. **Fork the Repository**:
    Click the "Fork" button on the GitHub page.

  2. **Clone Your Fork**:
     ```
     git clone https://github.com/your-username/ai-text-generator.git
     ```
  3. **Create a Branch**:
     ```
     git checkout -b feature/your-feature-name
     ```
  4. **Make Changes**:
     - Implement your feature or bug fix.

  6. **Run Tests**:
     ```
     pytest
     ```
  7. **Commit and Push**:
     ```
     git add .
     git commit -m "Add your feature description"
     git push origin feature/your-feature-name
     ```
  8. **Submit a Pull Request**:
      Create a pull request on the original repository.

## License
  This project is licensed under the MIT License. See the LICENSE file for details.
  Developed by mha0376. Explore the power of AI text generation! 🚀


