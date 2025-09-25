📝 Recruiter Help – Job Description Generator
An agentic system built with FastAPI that generates structured job descriptions by combining:  

🎙️ Audio input → job requirements  
📄 PDF documents → company benefits  
🌐 Website scraping → company information  
🤖 LLM (OpenAI GPT) → polished, structured job description


🚀 Features
```
Upload an audio file (job requirements).
Upload a PDF file (company benefits).
Provide a company website URL (company info).
Automatically generates a well-formatted job description with:
Job Title  
Responsibilities / Duties  
Requirements / Qualifications  
Benefits / Perks  
About the Company
```

📂 Project Structure
```
src/
├── inputs/
│   ├── audio_processor.py  # Whisper-based audio transcription
│   ├── pdf_processor.py   # Extract text from PDFs
│   ├── web_scraper.py     # Scrape company info from website
├── processing/
│   ├── job_description.py # Builds prompt + LLM call
│   ├── orchestrator.py    # Coordinates inputs and pipelines
├── api/
│   ├── routes.py          # FastAPI routes
│   ├── app.py             # Entry point for FastAPI
```

⚙️ Installation

Clone the repository:
```
git clone https://github.com/yourusername/recruiter-help.git
cd recruiter-help
```

Create and activate a virtual environment:
```
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

Install dependencies:
```
pip install -r requirements.txt
```

🔑 Set OpenAI API KeyBefore running the project, export your OpenAI API key:
Linux/Mac
```
export OPENAI_API_KEY="your_api_key_here"
```

Windows (PowerShell)
```
setx OPENAI_API_KEY "your_api_key_here"
```

▶️ Running the APIFrom the project root:
```
uvicorn src.app:app
```

Visit API docs at:👉 http://127.0.0.1:8000/docs


📤 Example Usage
Endpoint
```
POST /api/generate-job-description
Request (multipart/form-data)  

audio_file: audio file upload (job requirements)  
pdf_file: PDF upload (benefits)  
url: string (company website URL)
```

Response  
{
  "job_description": "Generated professional job description text..."
}


🧰 Tech Stack

FastAPI – web framework  
OpenAI GPT – LLM for job description generation  
[PyPDF2 / pdfplumber] – PDF text extraction  
[BeautifulSoup / requests] – web scraping

