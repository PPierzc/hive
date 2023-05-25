import PyPDF2


def parse_markdown(path):
    """
    Parses markdown text into paragraphs optimized for semantic search.
    :param path: path to the markdown file
    :return:
    """
    with open(path, "r") as f:
        text = f.read()

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


def parse_pdf(path):
    """
    Parses a PDF file into paragraphs optimized for semantic search.
    :param path:
    :return:
    """

    with open(path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        paragraphs = []
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text = page.extract_text()
            paragraphs += [text]
            # print(len(paragraphs))

        # paragraphs = [
        #     paragraph
        #     for paragraph in paragraphs
        #     if len(paragraph) > 250
        #        and not paragraph.startswith("!")
        #        and not paragraph.startswith("http")
        #        and not paragraph.startswith("    ")
        #        and not paragraph.startswith("[")
        #        and not paragraph.startswith("---")
        # ]

    return paragraphs
