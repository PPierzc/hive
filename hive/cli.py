#!/usr/bin/env python3
import os
import uuid

import torch
import typer
from qdrant_client import QdrantClient
from qdrant_client.http import models as rest
from rich.console import Console
from rich.panel import Panel
from sentence_transformers import SentenceTransformer

from hive.parsers import parse_markdown
from hive.spinner import BeeStatus

client = QdrantClient(path="./db")

app = typer.Typer()
console = Console()


@app.command()
def search(query: str):
    # Loader with the text "Searching for 'query'..."
    with BeeStatus(f"Parsing files") as status:
        status.update(f"Searching paragraphs for '[bold]{query}[/bold]'...")

        from sentence_transformers import SentenceTransformer

        model = SentenceTransformer("msmarco-distilbert-base-dot-prod-v3")

        # get the text embeddings for the query and the data
        with torch.no_grad():
            text_embeddings = model.encode(query)
            text_embeddings = torch.tensor(text_embeddings).numpy().tolist()

        response = client.search(
            collection_name="paragraphs", query_vector=text_embeddings, limit=3
        )

        search_results = [
            {**res.payload, "match_score": res.score * 100} for res in response
        ]

    # show results
    if len(search_results) == 0:
        console.print(f"No results found for '{query}'")
        return

    header = f'[bold]Search results for "{query}"[/bold].'
    console.print(header)
    console.print()

    for item in search_results:
        title = f"[bold]{item['filename']}[/bold]"
        body = f"{item['body']}"
        match_score = f"[dim]Match score: {item['match_score']:.0f}%[/dim]"

        panel = Panel(
            body,
            title=title,
            title_align="left",
            subtitle=match_score,
            subtitle_align="left",
            expand=False,
            width=120,
            padding=(1, 2),
            border_style="#ffa908",
        )
        console.print(panel)
        # add a line break
        console.print()


@app.command()
def add(path: str):
    """
    Adds files given the path to the database
    :param path: path to the file or directory
    :return:
    """

    model = SentenceTransformer("msmarco-distilbert-base-dot-prod-v3")

    if os.path.isfile(path):
        console.print(f"Adding file: {path}", style="#ffa908")
        with open(path, "r") as f:
            body = f.read()
            paragraphs = parse_markdown(body)

            with torch.no_grad():
                text_embeddings = model.encode(paragraphs)
                text_embeddings = torch.tensor(text_embeddings).numpy().tolist()

            # generate a unique uuid for the file
            file_ids = [str(uuid.uuid4()) for _ in range(len(paragraphs))]

            client.upsert(
                collection_name="paragraphs",
                points=rest.Batch(
                    ids=file_ids,
                    vectors=text_embeddings,
                    payloads=[
                        {"filename": path, "body": paragraph}
                        for paragraph in paragraphs
                    ],
                ),
            )

    elif os.path.isdir(path):
        for file in os.listdir(path):
            if file.endswith(".md"):
                add(os.path.join(path, file))
    else:
        console.print(f"Invalid path: {path}")


@app.command()
def init():
    welcome = """   
 |_|  o       _  
 | |  |  \/  (/_ 
 """

    console.print(welcome, style="#ffa908")

    with BeeStatus(f"Initializing model") as status:
        from sentence_transformers import SentenceTransformer

        SentenceTransformer("msmarco-distilbert-base-dot-prod-v3")

        status.update(f"Initializing database")
        """
        Create a new collection with a vector index
        """
        client.recreate_collection(
            collection_name="paragraphs",
            vectors_config=rest.VectorParams(size=768, distance=rest.Distance.COSINE),
        )

    success_message = """Hive initialized successfully! 🐝
You can now add files to the database using the [yellow]'hive add'[/yellow] command.
"""

    console.print(success_message, style="#ffa908")


@app.command()
def check():
    response = client.get_collection(collection_name="paragraphs")
    console.print(response)


if __name__ == "__main__":
    app()
