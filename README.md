# markbot

A small Discord bot for mathematic calculations.

## Directory architecture

```
├── .gitignore
├── LICENSE
├── main.py       # Main code
├── .mise.toml    # mise-rtx specific configuration
├── README.md
├── requirements.txt
├── start.bat     # Start script for windows
```

## Installation

1. Clone the repository:
   ```bash
   https://github.com/seannnnnn-n/MarkBot-public-
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Create a new Discord bot and obtain the bot token.
2. Replace `YOUR_BOT_TOKEN` with your actual bot token.
3. Run the bot:
   ```bash
   python main.py
   ```

## Features

- Perform basic mathematical calculations.
- Respond to specific commands in Discord.

## Contributing

Contributions are limited currently.

### Code of Conduct

Please follow [Semantic commit message guides](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716) whlie writing commit message.

Here is a quick explanation of it :

```
feat: (new feature for the user, not a new feature for build script)
fix: (bug fix for the user, not a fix to a build script)
docs: (changes to the documentation)
style: (formatting, missing semi colons, etc; no production code change)
refactor: (refactoring production code, eg. renaming a variable)
test: (adding missing tests, refactoring tests; no production code change)
chore: (updating grunt tasks etc; no production code change)
```

## License

This project is licensed under the GNU GPL v3 Licence. See the [LICENSE](LICENSE) file for more details.
