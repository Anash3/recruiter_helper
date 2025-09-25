import asyncio
from src.inputs import audio_processor, pdf_processor, web_scrapper

async def fetch_audio_data(file_path):
    return audio_processor.process_audio(file_path)

async def fetch_pdf_data(file_path):
    return pdf_processor.extract_text(file_path)

async def fetch_web_data(url):
    return web_scrapper.scrape_job_info(url)

async def gather_all_inputs(audio_file, pdf_file, url):
    # Run all input processors concurrently
    results = await asyncio.gather(
        fetch_audio_data(audio_file),
        fetch_pdf_data(pdf_file),
        fetch_web_data(url)
    )
    audio_text, pdf_text, web_text = results
    # Combine into a single structured payload
    payload = {
        "audio": audio_text,
        "pdf": pdf_text,
        "web": web_text
    }
    return payload