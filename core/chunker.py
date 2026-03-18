"""
NeuTTS Studio — Smart Text Chunker
Splits any length of text into model-safe chunks using a 4-tier strategy.
"""

import re
from config import MAX_CHUNK_CHARS

_SENTENCE_END = re.compile(r'(?<=[.!?])\s+')
_CLAUSE_SPLIT = re.compile(r'(?<=[,;:])\s+')


def chunk_text(text: str, max_chars: int = MAX_CHUNK_CHARS) -> list[str]:
    """
    Split text into chunks safe for NeuTTS inference (within 2048 token window).

    4-tier strategy:
      1. Sentence boundaries  (.  !  ?)
      2. Clause boundaries    (,  ;  :)
      3. Word boundaries      (space)
      4. Hard cut             (last resort)

    Args:
        text:      Input text.
        max_chars: Max characters per chunk (default 250 ≈ ~20s audio).

    Returns:
        List of text chunks.
    """
    text = text.strip()
    if not text:
        return []
    if len(text) <= max_chars:
        return [text]

    # Tier 1: sentence split
    sentences = [s.strip() for s in _SENTENCE_END.split(text) if s.strip()]

    # Tier 2: clause split for oversized sentences
    units: list[str] = []
    for s in sentences:
        if len(s) <= max_chars:
            units.append(s)
        else:
            clauses = [c.strip() for c in _CLAUSE_SPLIT.split(s) if c.strip()]
            for clause in clauses:
                if len(clause) <= max_chars:
                    units.append(clause)
                else:
                    # Tier 3+4: word/hard split
                    units.extend(_word_split(clause, max_chars))

    # Greedy pack
    chunks: list[str] = []
    current = ""
    for unit in units:
        sep = " " if current else ""
        if len(current) + len(sep) + len(unit) <= max_chars:
            current += sep + unit
        else:
            if current:
                chunks.append(current.strip())
            current = unit
    if current.strip():
        chunks.append(current.strip())

    return chunks


def _word_split(text: str, max_chars: int) -> list[str]:
    words  = text.split()
    chunks = []
    current = ""
    for word in words:
        sep = " " if current else ""
        if len(current) + len(sep) + len(word) <= max_chars:
            current += sep + word
        else:
            if current:
                chunks.append(current)
            # Hard cut if single word is too long
            current = word if len(word) <= max_chars else word[:max_chars]
    if current:
        chunks.append(current)
    return chunks


def chunk_summary(text: str, max_chars: int = MAX_CHUNK_CHARS) -> dict:
    """Return a summary dict about how text will be chunked."""
    chunks = chunk_text(text, max_chars)
    return {
        "total_chunks":  len(chunks),
        "total_chars":   len(text),
        "chunks":        chunks,
        "avg_chars":     sum(len(c) for c in chunks) / len(chunks) if chunks else 0,
        "max_chunk_len": max((len(c) for c in chunks), default=0),
    }
