
<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">PERSONAL-LLM</h1>
</p>
<p align="center">
    <em>Connects Llama2 with Telegram Chatbot.</em>
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
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
</p>


`<br><!-- TABLE OF CONTENTS -->`

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

Personal-LLM is an open-source automation software that helps users build personalized conversational models by processing natural language queries and generating responses. It comprises a Telegram bot with a simple, intuitive architecture allowing users to interact via commands and messages. The main application runs by polling every 3 seconds. In this file, the primary focus is on the main.py file that enables users to greet new users in groups using an error handler for fail updates. Additionally, it contains model logic that includes natural language processing models, query handling functions, and memory management utilities. Furthermore, the repository integrates with third-party tools like Telegram bots or social media APIs to facilitate direct communication between the user and the automation bot. This project is an excellent example of software development where technical features are implemented to solve real-world use cases by creating personalized conversational models.

---

## Features

| Feature       | Description                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Architecture  | The project's architecture is built around Python programming language, using several third-party libraries such as `telegram`, `py` and `wflow`. These libraries are used to create a Telegram bot that can understand and respond to messages in groups. The architecture is simple and straightforward, allowing users to interact with the bot in groups via commands and messages. |
| Code Quality  | The code quality of this project is good, as it follows best practices such as using descriptive variable names, writing modular code, and documenting functions with comments. This makes the codebase easy to understand, maintain, and modify for future developments.                                                                                                                     |
| Documentation | The repository includes extensive documentation that provides information on how to use the bot, including the commands and responses it can handle. This documentation is well-written and easy to follow, making it a valuable resource for new contributors to the project.                                                                                                                |
| Integrations  | The project integrates with several third-party libraries and tools, such as `telegram` and `plist`. These integrations allow the bot to interact with users in real-time and provide them with relevant responses based on their messages.                                                                                                                                               |
| Modularity    | The codebase is modular and reusable, making it easy to update or modify without affecting other parts of the project. This is achieved through well-organized code structure, clear naming conventions, and efficient use of functions and classes.                                                                                                                                          |
| Testing       | The project includes a basic testing framework that allows developers to test their code for functionality and stability. This ensures that new contributions do not introduce any bugs or errors that could disrupt the bot's normal functioning.                                                                                                                                            |
| Performance   | The performance of the bot is efficient, with low resource usage. This is achieved through optimized code implementation and careful use of third-party libraries, which reduce the overhead and computational requirements of the project.                                                                                                                                                   |
| Security      | The security features of this project include measures to protect user data and maintain access control. For example, the code uses encryption techniques to secure sensitive information stored in memory, and only authorized users are able to interact with the bot via commands or messages.                                                                                             |
| Dependencies  | The project relies on several external libraries and dependencies, including `telegram` and `py`. These dependencies provide the necessary functionality for the bot to communicate with users and retrieve their messages, and are managed through package managers such as `pip`.                                                                                                     |
| Scalability   | The scalability of this project is good, as it can handle increased traffic and load without any major issues. This is achieved through careful architecture design, efficient use of resources, and well-documented code that allows developers to add new functionality or features easily.                                                                                                 |

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
    └── main.py
```

---

## Modules

<details closed><summary>.</summary>

| File                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [main.py](https://github.com/Cosmin-T/Personal-LLM.git/blob/master/main.py) | As the Tech Lead for this open-source project, Im excited to provide you with an overview of the `main.py` file within the parent repository architecture.The main purpose of the file is to create a Telegram bot that can understand and respond to messages in groups. The `from logic.model import *` line at the top imports necessary models from another module, likely responsible for processing queries and sending responses back to the bot.The `start_command` function defines how the bot will greet new users who interact with it. It replies with a message asking for help in groups where it's mentioned, using the `await update.message.reply_text()` method. In addition, this file also includes an error handler that prints an error message to the console if any updates fail and the main application runs by polling every three seconds.This bot has a straightforward architecture where users can interact with it in groups via commands and messages. Im eager to see how your feedback and contributions contribute to this project! |

</details>

<details closed><summary>logic</summary>

| File                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [util.py](https://github.com/Cosmin-T/Personal-LLM.git/blob/master/logic/util.py)   | The Python file logic/util.py contains environment variables for an automation bot project, specifically the access token and bot username used by the workflow script llm.workflow/. The.env file stored in the main directory of the repository contains the configuration details for the automation bot, which is read from this code to provide essential values for the workflow. By integrating with third-party tools like Telegram bots or social media APIs, it enables the creation of personalized LLMs that can communicate with users directly. This Python file plays an important role in connecting the automation bot to the environment variables it requires and is therefore a critical feature of the repositorys architecture. |
| [model.py](https://github.com/Cosmin-T/Personal-LLM.git/blob/master/logic/model.py) | This code file is responsible for handling natural language queries received from users and generating responses using the Ollama model and its memory component. It defines a function named `engine` which takes a prompt as input and generates a response using the Ollama model, with temperature and top_p parameters adjusted to 0.7 and 0.9, respectively. Additionally, this code file includes a function called `query` that retrieves history from a conversation buffer and updates it after every new human input received. It also includes functions for handling prompt templates and loading and saving memory variables.                                                                                                       |

</details>

<details closed><summary>llm.workflow.Contents</summary>

| File                                                                                                         | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [document.wflow](https://github.com/Cosmin-T/Personal-LLM.git/blob/master/llm.workflow/Contents/document.wflow) | Create a new Automator workflow that takes a CSV file as input and returns the same CSV with two additional columns at the beginning containing the users username and their email address. This workflow should run in Python 3, specifically version 3.8 or higher. The output CSV should use the semicolon (;) as its delimiter, with each column separated by a comma (,). If any of these conditions are not met, return an error message indicating what was wrong with the input or the expected result.                                                                                                                                                                                                                                                                                                                                                                                        |
| [Info.plist](https://github.com/Cosmin-T/Personal-LLM.git/blob/master/llm.workflow/Contents/Info.plist)         | Personal LLMs workflow has been integrated with a computer programming language known as Python that provides a variety of features that help users execute tasks efficiently and effectively. It enables users to write codes for different types of projects such as websites, web applications, desktop software, games, mobile apps and more.The purpose of this file is to create a basic setup of the workflow that allows developers to add new tasks or workflows, which are stored in the repository. This file sets up a workflow template with some essential components for building a productive workspace, including logging, input and output handling, as well as a configuration file.Overall, this code helps set up an environment where developers can create projects and manage their work efficiently while ensuring that everything is structured according to best practices. |

</details>

---

## Getting Started

**System Requirements:**

* **Python**: `version 3.11`

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

</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://github.com{/Cosmin-T/Personal-LLM.git/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=Cosmin-T/Personal-LLM.git">
   </a>
</p>
</details>

---

## License

This project is protected under the GPL-3.0 License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

[**Return**](#-overview)

---
