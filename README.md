# markbot

An actually maintained, small discord bot - or say, a starter template for basic mathematic calculation using `discord.py`.

## Directory architecture

```
├── .gitignore
├── LICENSE
├── main.py       # Main code
├── .mise.toml    
├── README.md
├── requirements.txt
```

## Prerequisites
- `python 3.10` or above.
## Installation

1. Create a new Discord bot and obtain the bot token. 
   - If you have no idea how to recreate this step, you may follow  [#1.Introduction To Discord.py](https://dev.to/mannu/1-introduction-to-discordpy-3c3j).
1. Clone the repository:
   ```bash
   $ git clone https://github.com/seannnnnn-n/markbot-public
   ```
1. Create `virtualenv` (Optional, but recommended)
   ```bash
   $ mkdir -p .venv 
   $ python -m venv /path/to/this/repository/.venv
   ```
1. Activate `virtualenv` ( If you skipped step 3, this process is unnecessary)
   - For Windows
   ```
   $ .venv\bin\Activate.ps1
   ```
   - For Mac
   ```
   $ source .venv/bin/activate
   ```
   - For Linux or WSL
   ```
   $ .venv/bin/activate
   ```
   - Or, if you are using `fish shell`
   ```
   $ .venv/bin/activate.fish
   ```
1. Install the required dependencies:
   ```bash
   $ pip install -r requirements.txt
   ```
1. Run `main.py`
   ```
   $ python main.py
   ```

## Features

- [x] Perform basic mathematical calculations, using slash command interface.

## Contributing

Contributions are welcome! Feel free to open an issue to discuss anything, or submit a PR:)

### Code of Conduct

Please follow [Semantic commit message guides](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716) while writing commit message.

Here is a quick recap of it :

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