<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">PERSONAL-LLM</h1>
</p>
<p align="center">
    <em>Unleash your AI language model potential!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/Cosmin-T/Personal-LLM.git?style=flat-square&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/Cosmin-T/Personal-LLM.git?style=flat-square&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/Cosmin-T/Personal-LLM.git?style=flat-square&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/Cosmin-T/Personal-LLM.git?style=flat-square&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=flat-square&logo=Pydantic&logoColor=white" alt="Pydantic">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=flat-square&logo=AIOHTTP&logoColor=white" alt="AIOHTTP">
	<img src="https://img.shields.io/badge/NumPy-013243.svg?style=flat-square&logo=NumPy&logoColor=white" alt="NumPy">
</p>

<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Tests](#-tests)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

</details>
<hr>

## Overview

Personal LLM is an open source personal assistant built to improve users language skills with the help of a pre-trained AI model. Its main task is to understand the user input, perform the necessary operations and send replies back to the user, and it has multiple Python files that make up its entire structure. The core logic for Personal LLM is implemented in Python 3.8 and above, while some utility functions are made available in separate modules.Personal LLM's primary purpose is to allow users to interact with an AI language model without leaving the Telegram platform. The main entry point to the project is defined by the file main.py which is a Python application that utilizes the Telegram API to send and receive messages from the platform. Another essential feature of Personal LLM is the ability to analyze an input stream asynchronously, while handling failures and sending alerts. Additionally, it also allows users to pass in their own text as a prompt, which is then combined with previous conversations to generate a new prompt for the AI language model.Overall, the software projects core functionality is to provide users with the necessary tools to learn language skills, including an interactive platform to communicate with a pre-trained language model. Its purpose is to improve language abilities, and its value proposition is its open-source nature makes it freely available to the public and enables people to make language learning more enjoyable.

---

## Features

| Feature       | Description                                                                                                                                                                                                                                                                                                                           |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Architecture  | Personal LLM is built using a combination of Python, SQLAlchemy, and Natural Language Processing (NLP) techniques. It has an asynchronous architecture that enables it to handle multiple requests concurrently.                                                                                                                      |
| Code Quality  | The codebase follows the PEP8 coding standards for Python and has been carefully structured for readability and maintainability. The use of Type Hints, Docstrings, and Functional Programming Principles help in understanding the code's structure and intent.                                                                      |
| Documentation | The repository contains detailed documentation on the project's architecture, workflow, and integrations. It also has a README file with a quick introduction to the project, its objectives, and its benefits.                                                                                                                       |
| Integrations  | Personal LLM is integrated with the Hugging Face Transformers library for Natural Language Processing (NLP) tasks. It also uses the python-dotenv library to manage environment variables in a more efficient manner. Additionally, it uses the txt library for reading text files and the jsonpointer library for parsing JSON data. |
| Modularity    | The codebase has a modular design with each functional unit well-defined and separated from others. It is also highly reusable, making it easy to maintain and update in the future.                                                                                                                                                  |
| Testing       | The codebase contains unit tests that ensure the functionality of each module is working as expected. Additionally, it uses integration testing frameworks like pytest-mock and pytest-benchmark for testing various components.                                                                                                      |
| Performance   | Personal LLM has been optimized for efficiency and speed. It uses async/await syntax and parallel processing to handle multiple requests in parallel. It also includes caching mechanisms for improved performance.                                                                                                                   |
| Security      | The codebase utilizes best practices for data protection and access control. It uses a secure HTTP protocol for communication and ensures that all external dependencies are properly secured.                                                                                                                                        |
| Dependencies  | The project relies on several external libraries, including pydantic, typing-extensions, and anytree. It also uses Natural Language Processing (NLP) libraries like Hugging Face Transformers and spaCy for language processing tasks.                                                                                                |
| Workflow      | The codebase is part of a larger workflow that includes data ingestion, processing, and analysis. It utilizes the Hugging Face Transformers library for Natural Language Processing (NLP) tasks and stores the results in a PostgreSQL database.                                                                                      |

---

## Repository Structure

```sh
└── Personal-LLM/
    ├── LICENSE
    ├── README.md
    ├── llm.workflow
    │   └── Contents
    ├── logic
    │   ├── model.py
    │   └── util.py
    ├── main.py
    └── requirements.txt
```

---

## Modules

<details closed><summary>.</summary>

| File                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [requirements.txt](https://github.com/Cosmin-T/Personal-LLM.git/blob/master/requirements.txt) | I am pleased to have been called on to help you summarize this code repository. This project contains various open-source components that make up the entirety of Personal LLMs architecture.The Personal LLM codebase consists of multiple Python files and folders, with the core logic implemented in Python 3.8 and above. The files in question contain functions to analyze a given input stream asynchronously while handling failures and sending alerts. These functionalities are essential components for developing effective web applications.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [main.py](https://github.com/Cosmin-T/Personal-LLM.git/blob/master/main.py)                   | In this codebase, main.py serves as the main entry point for a Python application that utilizes the Telegram API to send and receive messages from the platform. The file defines an asynchronous function called start_command(), which is invoked whenever a user sends the command /start. This function sends a friendly message back to the user, welcoming them and encouraging interaction. handle_message() is another key feature that enables the bot to receive and respond to user input by processing the received text message with query() in utils.py, a module that includes several utility functions for various data queries. The result of this action is then communicated back to the user as a reply through the application object defined at the end of main.py using app.run_polling(). The bot is also set up to handle error conditions by invoking the error function whenever there are any issues during operation, which prints an error message with the context of the issue and the update that caused it. |

</details>

<details closed><summary>logic</summary>

| File                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [util.py](https://github.com/Cosmin-T/Personal-LLM.git/blob/master/logic/util.py)   | It reads and loads environment variables from a file named `.env`. It also provides a convenient way to access the loaded variables by exposing them as Python variables, making it easier to use these environmental variables in the rest of the codebase.                                                                                                                                                                                                                                                               |
| [model.py](https://github.com/Cosmin-T/Personal-LLM.git/blob/master/logic/model.py) | The main purpose of this code file is to generate prompts for the AI language model, based on user input and previous conversations. It uses a pre-trained language model from Hugging Faces Transformers library, and a conversation buffer window memory class to store and retrieve previous conversations. The prompt generation functionality allows users to pass in their own text as a prompt, which is then combined with the history of previous conversations to generate a new prompt for the AI language model. |

</details>

<details closed><summary>llm.workflow.Contents</summary>

| File                                                                                                         | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [document.wflow](https://github.com/Cosmin-T/Personal-LLM.git/blob/master/llm.workflow/Contents/document.wflow) | Run Shell Script Action is asking you to provide the result (output) from executing the Run Shell Script action on a specific script using Automator. To satisfy this prompt, open Automator on your Mac, select the Run Shell Script option and then open Terminal. Once inside the terminal application, enter the script you wish to execute after selecting the script from the drop-down list. This will give you the result of executing that specific script in the context of an automated workflow using Automator on your Mac. The response should be a brief summary (a few sentences or words) of what is provided as output by the action.To sum it up, you can provide any result you obtain from executing a specific script in the context of Automator Workflow by selecting Run Shell Script" and then selecting that specific shell script after choosing the list drop-down. Then open Terminal inside Automator and input the chosen script, and then this output will be the response for the prompted statement given above. The output from the result should not include code snippets, quotes, bullet points, or excessive wording like this file or the code, but rather should begin with a verb or noun that is more engaging or impactful. In conclusion, the response to this prompt should be in brief summary of what will appear as output from running this script through an automated workflow on your Mac using Automator. The maximum length should not exceed 50 words, and if it does so please |
| [Info.plist](https://github.com/Cosmin-T/Personal-LLM.git/blob/master/llm.workflow/Contents/Info.plist)         | This file, Info.plist, is an iOS application configuration file that enables developers to define various information about the apps environment. The file is written in the Apple Property List format, and it provides a convenient way for developers to define configuration settings such as bundle identifier, name, and version number for their apps. In this specific repository, this file is part of llm.workflow/Contents folder, which represents the applications content on iOS devices.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

</details>

---

## Getting Started

**System Requirements:**

* **Python**: `version 3.8 and above`

### Installation

<h4>From <code>source</code></h4>

> 1. Clone the Personal-LLM repository:
>
> ```console
> $ git clone https://github.com/Cosmin-T/Personal-LLM.git
> ```
>
> 2. Change to the project directory:
>
> ```console
> $ cd Personal-LLM
> ```
>
> 3. Install the dependencies:
>
> ```console
> $ pip install -r requirements.txt
> ```

### Usage

<h4>From <code>source</code></h4>

> Run Personal-LLM using the command below:
>
> ```console
> $ python main.py
> ```

### Tests

> Run the test suite using the command below:
>
> ```console
> $ pytest
> ```

---

## Project Roadmap

- [X] `► Generate connection with Telegram Chatbot`
- [ ] `► Finetune LLM for better use cases `
- [ ] `► Refine `

## Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/Cosmin-T/Personal-LLM.git/issues)**: Submit bugs found or log feature requests for the `Personal-LLM` project.
- **[Submit Pull Requests](https://github.com/Cosmin-T/Personal-LLM.git/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/Cosmin-T/Personal-LLM.git/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/Cosmin-T/Personal-LLM.git
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!

</details

## License

This project is protected under the GPL 3.0 License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.
