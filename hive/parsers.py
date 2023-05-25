def parse_markdown(text):
    """
    Parses markdown text into paragraphs optimized for semantic search.
    :param text:
    :return:
    """

    paragraphs = text.split("\n\n")

    # if a paragraph is a header add it to the next paragraph
    for i, paragraph in enumerate(paragraphs):
        if paragraph.startswith("#") and i < len(paragraphs) - 1:
            paragraphs[i] = paragraph + "\n" + paragraphs[i + 1]
            paragraphs[i + 1] = ""

        if (paragraph.startswith("$") or paragraph.startswith("<")) and i > 0:
            paragraphs[i] = paragraph + "\n" + paragraphs[i - 1]
            paragraphs[i - 1] = ""

    # remove paragraphs that are too short or are not valid paragraphs
    paragraphs = [
        paragraph
        for paragraph in paragraphs
        if len(paragraph) > 250
        and not paragraph.startswith("!")
        and not paragraph.startswith("http")
        and not paragraph.startswith("    ")
        and not paragraph.startswith("[")
        and not paragraph.startswith("---")
    ]

    return paragraphs
