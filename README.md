# Nutrition GenAI App

This project is a Streamlit application that allows users to interact with AnnGuru for chat and Gemini Vision for image-based nutrition facts extraction.

## Features

1. **Chat with AnnGuru**: Engage in a conversation with AnnGuru.
2. **Gemini Vision**: Upload an image of nutrition facts and generate a caption based on the image.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd nutrition_genai_app
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - **Windows**:
        ```sh
        .\venv\Scripts\Activate.ps1
        ```
    - **macOS/Linux**:
        ```sh
        source venv/bin/activate
        ```

4. **Install the required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

### Running the App

1. **Start the Streamlit app**:
    ```sh
    streamlit run src/app.py
    ```

2. **Interact with the app**:
    - Choose between "Chat with AnnGuru" and "Gemini Vision" from the sidebar.
    - For "Chat with AnnGuru", type your message and interact with the assistant.
    - For "Gemini Vision", upload an image of nutrition facts and generate a caption.

## File Structure

The project has the following file structure:

- `src/app.py`: The main script of the Streamlit app. It handles the UI layout and navigation between chat and vision interfaces.
- [`src/frontend/chat.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2Fnutrition_genai_app%2Fsrc%2Ffrontend%2Fchat.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22a486438a-544e-40f9-af8e-ede9971d4d69%22%5D "c:\nutrition_genai_app\src\frontend\chat.py"): Handles the chat interface with AnnGuru.
- [`src/frontend/vision.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2Fnutrition_genai_app%2Fsrc%2Ffrontend%2Fvision.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22a486438a-544e-40f9-af8e-ede9971d4d69%22%5D "c:\nutrition_genai_app\src\frontend\vision.py"): Handles the image upload and caption generation for nutrition facts.
- [`src/nutri_code.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2Fnutrition_genai_app%2Fsrc%2Fnutri_code.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22a486438a-544e-40f9-af8e-ede9971d4d69%22%5D "c:\nutrition_genai_app\src\nutri_code.py"): Contains functions for processing nutrition facts images.
- [`requirements.txt`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2Fnutrition_genai_app%2Frequirements.txt%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22a486438a-544e-40f9-af8e-ede9971d4d69%22%5D "c:\nutrition_genai_app\requirements.txt"): Python dependencies required for the project.

Feel free to modify the app and add your own image processing or text generation logic as needed.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.