
# ── System prompt ────────────────

SYSTEM_PROMPT = """You are a helpful assistant that answers questions using ONLY the provided context.

If the context does not contain enough information to answer
the question, say "I don't have enough information."

Always cite your sources by mentioning the document name.
Do not invent information or use outside knowledge."""


# ── Helpers ────────────────────────
#Format a list of chunk dicts into a context string.
def format_chunks(chunks: list[dict]) -> str:
    formatted_chunks = []

    for chunk in chunks:
        source = chunk["source"]
        text = chunk["text"]

        formatted_chunk= f"[Source: {source}]\n{text}"
        formatted_chunks.append(formatted_chunk)

    return "\n\n---\n\n".join(formatted_chunks)

#Rough token count estimate: characters // 4.
def token_estimate(text: str) -> int:

    return len(text) // 4

#Assemble the full RAG prompt.
def build_prompt(question: str, chunks: list[dict]) -> str:

    context = format_chunks(chunks)

    prompt = f"""{SYSTEM_PROMPT}

CONTEXT:
{context}

USER QUESTION: {question}

Remember to answer using only the provided context and cite your sources.
"""
    return prompt


# ── Test runner ─────────────────────
#Assemble and print a prompt with token estimate.
def run_test(question: str, chunks: list[dict]) -> None:

    prompt = build_prompt(question, chunks)
    estimated_tokens = token_estimate(prompt)

    print("=" * 60)
    print("RAG PROMPT TEST")
    print("=" * 60)

    print(prompt)

    print("-" * 60)
    print(f"Character count: {len(prompt)}")
    print(f"Estimated tokens: {estimated_tokens}")
    print("=" * 60)


# ── Test cases ──────────────────────

if __name__ == "__main__":
    # Test case 1
    # TODO: Define a question and at least 2 simulated chunks, call run_test()

    # Test case 2
    # TODO: Define a different question and different chunks, call run_test()
    pass

if __name__ == "__main__":

    # Test case 1: FastAPI request validation
    question1 = "How does FastAPI validate request data?"

    chunks1 = [
        {
            "text": "FastAPI uses Pydantic models to validate request data.",
            "source": "fastapi.txt",
            "distance": 0.32
        },
        {
            "text": "Pydantic uses Python type hints for data validation.",
            "source": "pydantic.txt",
            "distance": 0.41
        }
    ]

    run_test(question1, chunks1)

    # Test case 2: ChromaDB semantic search
    question2 = "How does ChromaDB perform semantic search?"

    chunks2 = [
        {
            "text": "ChromaDB stores document embeddings in collections.",
            "source": "chromadb.txt",
            "distance": 0.28
        },
        {
            "text": "Semantic search compares query embeddings with stored "
                    "document embeddings to find similar content.",
            "source": "embeddings.txt",
            "distance": 0.36
        }
    ]

    run_test(question2, chunks2)
