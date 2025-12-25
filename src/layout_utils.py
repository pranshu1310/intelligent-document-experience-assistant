def detect_sections(text):
    sections = []
    current_title = "Introduction"
    current_content = []

    for line in text.split("\n"):
        line = line.strip()
        if line.isupper() and len(line.split()) < 8:
            sections.append({
                "section": current_title,
                "content": "\n".join(current_content).strip()
            })
            current_title = line
            current_content = []
        else:
            current_content.append(line)

    sections.append({
        "section": current_title,
        "content": "\n".join(current_content).strip()
    })

    return sections
