def confidence_score(output, source_text):
    tokens = [w for w in output.split() if len(w) > 4]
    matched = sum(1 for w in tokens if w.lower() in source_text.lower())
    return round(matched / max(1, len(tokens)), 2)
