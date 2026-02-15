def chunk_text(text, chunk_size=500):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]


def rank_chunks(chunks, query):
    query_words = set(query.lower().split())
    scored = []

    for chunk in chunks:
        score = sum(word in chunk.lower() for word in query_words)
        scored.append((score, chunk))

    scored.sort(reverse=True, key=lambda x: x[0])
    return [chunk for score, chunk in scored[:5]]