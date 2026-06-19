from dotenv import load_dotenv
import os

load_dotenv()


from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient

load_dotenv()

endpoint = os.getenv("DOCUMENT_INTELLIGENCE_ENDPOINT")
key = os.getenv("DOCUMENT_INTELLIGENCE_KEY")


def extract_resume_text(file_path):

    client = DocumentIntelligenceClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key)
    )

    with open(file_path, "rb") as f:

        poller = client.begin_analyze_document(
            "prebuilt-read",
            body=f
        )

    result = poller.result()

    extracted_text = ""

    for page in result.pages:
        for line in page.lines:
            extracted_text += line.content + "\n"

    return extracted_text