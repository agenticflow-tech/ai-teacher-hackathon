import pypdf
import docx

def extract_text_from_file(uploaded_file):
    """Extracts raw text from PDF, DOCX, or TXT files."""
    file_extension = uploaded_file.name.split('.')[-1].lower()
    extracted_text = ""
    
    if file_extension == 'pdf':
        reader = pypdf.PdfReader(uploaded_file)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                extracted_text += text + "\n"
                
    elif file_extension in ['docx', 'doc']:
        doc = docx.Document(uploaded_file)
        for paragraph in doc.paragraphs:
            if paragraph.text:
                extracted_text += paragraph.text + "\n"
                
    elif file_extension == 'txt':
        extracted_text = uploaded_file.read().decode('utf-8')
        
    return extracted_text.strip()

def create_text_chunks(text, chunk_size=1000, chunk_overlap=150):
    """Splits large text into smaller chunks for RAG knowledge grounding."""
    if not text:
        return []
        
    chunks = []
    start = 0
    text_length = len(text)
    
    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - chunk_overlap
        
    return chunks