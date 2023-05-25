<p align="center">
  <img height="175" src="https://github.com/PPierzc/hive/blob/main/docs/logo.png" alt="Qdrant">
</p>

<p align="center">
    <b>Unleash the power of Hive and navigate your knowledge base like a busy bee!  🐝🔍✨</b>
</p>

<p align="center">
<a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Black Code Style"></a>
<a href="https://github.com/ppierzc/hive/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License"></a>
</p>

🐝 Hive is a CLI tool for semantic searching of your knowledge base 📚. It allows you to easily search through your collection of files and directories, extracting meaningful information based on your prompts.
 No more searching through haystacks—let Hive find the golden honey! 🍯🐝 Embrace the buzz and let your knowledge thrive! 🚀💡

## Getting Started

### Installation
You can install Hive using pip:

```shell
pip install hive-cli
```

### Initializing Hive
To get started with Hive, initialize it in your project directory using the following command:

```shell
hive init
```
This sets up Hive and creates the necessary configuration files to enable knowledge base searching.

### Adding Files or Directories
You can add files or directories to your Hive knowledge base using the add command:

```shell
hive add <file_or_dir_to_add>
```
This command allows Hive to index and analyze the content of the specified files or directories, making them searchable within your knowledge base.

#### Supported File Types
Hive currently supports only Markdown and PDF files. Support for other file types is coming soon!

### Searching the Knowledge Base
To perform a semantic search within your knowledge base, use the search command along with your prompt:

```shell
hive search "your prompt"
```
Hive will analyze your prompt and match it against the indexed content, providing you with the most relevant results based on semantic similarity.

#### Example Search Output
Here's an example output of a search performed with Hive:

```shell
hive search "are honey bees good?"              

╭─ ./data/the-problem-with-honey-bees.md ──────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                      │
│  But think about them, we must. I used to believe that honey bees were a gateway species, and that concern over      │
│  their health and prosperity would spill over onto native bees, benefitting them, too. While this may have happened  │
│  in some cases, evidence is mounting that misguided enthusiasm for honey bees has likely been to the native bees’    │
│  detriment. Beekeeping doesn’t make me feel good, anymore. In fact, quite the opposite.                              │
│                                                                                                                      │
╰─ Match score: 73% ───────────────────────────────────────────────────────────────────────────────────────────────────╯
```
The search output displays the matched file, along with the relevant text snippet and a match score indicating the similarity between the prompt and the content.

🔍 Hive makes it easy to find the information you need, saving you time and effort!

## Contributing
We welcome contributions to Hive! Feel free to open issues and submit pull requests for any enhancements or bug fixes. Let's make Hive even better together! 🚀

## License
Hive is licensed under the MIT License.

🐝 Don't waste time searching, let Hive be your knowledge navigator! Start exploring your knowledge base effortlessly with Hive. Happy searching! 🚀✨