from openai import OpenAI

client = OpenAI()

def call_llm(prompt):
    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt
        )
        return response.output_text
    except Exception as e:
        # Log or handle the error
        print(f"Error calling LLM: {e}")
        return "Error: Unable to generate job description at this time."
    
def create_prompt(payload):
    """
    Constructs a clear and informative prompt for generating a job description.
    Expects payload to have keys: 'audio', 'pdf', 'web'
    """

    prompt = f"""
    You are a seasoned HR specialist and professional content writer. Using the inputs below, generate a polished and engaging job description suitable for a job posting.

    Inputs:

    1. Job Requirements (from audio notes):
    {payload['audio']}

    2. Company Benefits (from PDF):
    {payload['pdf']}

    3. Company Information (from website):
    {payload['web']}

    Instructions:

    - Structure the job description with the following sections in this order:
        1. **Job Title**
        2. **Location** (if available)
        3. **About the Company** (give candidates context about the organization)
        4. **Responsibilities / Duties**
        5. **Requirements / Qualifications**
        6. **Benefits / Perks**
    - Use a professional and appealing tone that attracts qualified candidates.
    - Integrate benefits and company information naturally into the description.
    - Ensure clarity, conciseness, and readability.
    - Use proper Markdown formatting:
        * Actual line breaks, headings, and bullet points
        * Avoid literal `\n`, `\t`, or `---` in the output
    - Highlight key skills, experiences, and unique company perks.
    - End with a strong call-to-action encouraging candidates to apply.
    """

    return prompt


def create_job_description(payload):
    try:
        
        prompt = create_prompt(payload)
        return call_llm(prompt)
    except Exception as e:
        print(f"Error generating job description: {e}")
        return "Error: Could not generate job description."
