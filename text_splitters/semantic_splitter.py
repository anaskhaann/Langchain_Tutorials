# semantic text splutter is in experimental stage
from dotenv import load_dotenv
from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings

load_dotenv()

sample_text = """
Farmers were working hard in the fields, preparing the soil and planting seeds for the next season. The sun was bright, and the air smelled of earth and fresh grass. The Indian Premier League (IPL) is the biggest cricket league in the world. People all over the world watch the matches and cheer for their favourite teams.

Terrorism is a big danger to peace and safety. It causes harm to people and creates fear in cities and villages. When such attacks happen, they leave behind pain and sadness. To fight terrorism, we need strong laws, alert security forces, and support from people who care about peace and safety.
"""

# in this pass model, threshold, and criteria to check how we are measuring low
text_splitter = SemanticChunker(
    GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001"),
    breakpoint_threshold_amount=1,
    breakpoint_threshold_type="standard_deviation",
)

result = text_splitter.split_text(sample_text)

print(result)
print("=" * 60)
print(result[0])
