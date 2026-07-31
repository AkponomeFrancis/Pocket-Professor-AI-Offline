from services.chunking import chunk_text

sample_text = "Pocket Professor AI " * 500

chunks = chunk_text(sample_text)

print("Number of chunks:", len(chunks))

print("\nFirst chunk:\n")

print(chunks[0][:300])