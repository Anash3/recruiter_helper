from fastapi import APIRouter, HTTPException, UploadFile, File, Form
import io
import tempfile
from urllib.parse import urlparse


from src.processing.job_description import create_job_description
from src.models.jobdesc import JobDescriptionResponse
from src.processing.orchestrator import gather_all_inputs

router = APIRouter()

@router.post(
    "/generate-job-description",
    response_model=JobDescriptionResponse
    )
async def generate_job_endpoint(
    audio_file: UploadFile = File(...),
    pdf_file: UploadFile = File(...),
    url: str = Form(...)
):
    """
    Expects:
        audio_file: uploaded audio file
        pdf_file: uploaded PDF file
        url: company website URL
    """
    try:
        # Validate files are provided
        if not audio_file:
            raise HTTPException(status_code=400, detail="Audio file is required.")
        if not pdf_file:
            raise HTTPException(status_code=400, detail="PDF file is required.")

        # Validate file types (extension-based)
        if not audio_file.filename.lower().endswith(".mp3"):
            raise HTTPException(status_code=400, detail="Audio file must be an MP3.")
        if not pdf_file.filename.lower().endswith(".pdf"):
            raise HTTPException(status_code=400, detail="File must be a PDF.")

        # Validate URL
        if not url:
            raise HTTPException(status_code=400, detail="URL is required.")
        parsed_url = urlparse(url)
        if parsed_url.scheme not in ("http", "https") or not parsed_url.netloc:
            raise HTTPException(status_code=400, detail="Invalid URL. Must start with http:// or https://")
        
        # Read audio and PDF bytes
        audio_bytes = await audio_file.read()
        pdf_bytes = await pdf_file.read()

        # Wrap audio bytes in BytesIO and give a filename
        audio_file_like = io.BytesIO(audio_bytes)
        audio_file_like.name = "audio.mp3"  # OpenAI requires a name to detect format

        # Save PDF to temp file for functions expecting a path
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_pdf:
            tmp_pdf.write(pdf_bytes)
            tmp_pdf_path = tmp_pdf.name
        
        # Call the orchestrator (you might need to adjust your processors
        # to accept raw bytes instead of file paths)
        payload = await gather_all_inputs(audio_file_like, tmp_pdf_path, url)
        result = create_job_description(payload)

        return {"job_description": result}

    except Exception as e:
        # Log the error
        print(f"Error generating job description: {e}")
        # Return a proper HTTP error response
        raise HTTPException(
            status_code=500,
            detail="Failed to generate job description. Please try again later."
        )
