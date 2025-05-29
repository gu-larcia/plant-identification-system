# Plant Identification System

A sophisticated plant identification application powered by LangChain agents and Google's Gemini AI. Upload a plant photo and receive comprehensive botanical analysis including identification, care instructions, and geographic distribution data.

## Features
- AI-Powered Plant Identification: Uses Gemini Vision to identify plants from photos
- Multi-Agent Architecture: Specialized LangChain agents for different analysis tasks
- Comprehensive Analysis: Get detailed information across four key areas:
- Plant identification with scientific names
- Botanical research and characteristics
- Care instructions and cultivation tips
- Geographic distribution and climate data
- Clean, reference-quality output
- Responsive Gradio interface with beautiful styling

##  Quick Start
### Prerequisites
- Python 3.8+
- Google Gemini API key

### Installation
- Clone or download the notebook
- Install dependencies
- Run the application by running all cells
- Enter your Gemini API key when prompted
- Upload a plant image and click "Run Analysis Pipeline"

### Using Google Colab
- Clone or download the notebook
- Install dependencies
- Run the application by running all cells
- Enter your Gemini API key when prompted
- Upload a plant image and click "Run Analysis Pipeline"

## How It Works
The system uses a multi-agent architecture with specialized AI agents:
Agent Pipeline

    Identification Agent - Analyzes the uploaded image to identify the plant
    Research Agent - Gathers comprehensive botanical information
    Care Specialist Agent - Provides cultivation and care instructions
    Geographic Agent - Compiles distribution and climate data
    Formatting Agent - Cleans and professionalizes all outputs

## Technical Architecture

    Frontend: Gradio web interface with custom CSS styling
    Backend: LangChain agent framework
    AI Model: Google Gemini 2.0 Flash for vision and text generation
    Error Handling: Robust validation and error recovery

## Usage
1) Enter API key;
2) Select and upload a clear photo of the plant you want to identify;
3)  Click the "Run Analysis Pipeline" button;
4) Review results.

## Example Output

The system provides structured, professional output including:

        COMMON NAME: Monstera Deliciosa
        SCIENTIFIC NAME: Monstera deliciosa
        FAMILY: Araceae
        CONFIDENCE: High

        KEY FEATURES:
        - Large, fenestrated leaves with natural holes
        - Climbing growth habit with aerial roots
        - Glossy, heart-shaped juvenile leaves

        CARE DIFFICULTY: Easy

        WATERING:
        - Frequency: Weekly during growing season
        - Amount: Water thoroughly until drainage
        - Seasonal adjustments: Reduce in winter

## Configuration
API Key Setup
- Get your API key from Google AI Studio
- Enter it in the password field when prompted
- The system validates the key before processing

## Security & Privacy

    API keys are handled securely through Gradio's password input
    No plant images are stored permanently
    All processing happens in your session

## Troubleshooting
Common Issues

"API key error"

    Verify your Gemini API key is correct
    Check API quota and billing status

"Error: Input data is required"

    Ensure you've uploaded a plant image
    Try a clearer, well-lit photo

"Plant name not found"

    Upload a clearer image with the plant as the main subject
    Ensure good lighting and focus

## Error Handling

The system includes comprehensive error handling:

    API validation before processing
    Graceful degradation for unclear images
    Detailed error messages for troubleshooting


##  License
This project is open source.


Note: This system is for educational and research purposes. While highly accurate, always consult botanical experts for critical plant identification needs.
