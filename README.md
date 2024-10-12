# Sense of Humor

A command-line tool to generate jokes based on type, length, and audience.

## Description

The `sense-of-humor` package provides a CLI tool `joke` that allows you to fetch jokes tailored to your preferences. Whether you're a presenter, educator, or just someone who loves a good laugh, this tool has you covered.

## Installation

1. **Clone the repository**

   ```bash
   git clone git@github.com:Frajder/sense-of-humor.git
   ```

2. **Navigate to the project directory**

   ```bash
   cd sense-of-humor
   ```

3. **Create a virtual environment (optional but recommended)**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. **Install the package**

   ```bash
   pip install .
   ```

## Usage

Run the `joke` command with optional arguments:

```bash
joke --type pun --length short --audience tech-savvy
```

### Arguments

- `--type`: Type of joke (`pun`, `knock-knock`, `one-liner`). Default is `pun`.
- `--length`: Length of the joke (`short`, `medium`, `long`). Default is `short`.
- `--audience`: Intended audience (`kids`, `adults`, `tech-savvy`). Default is `adults`.

## Examples

- **Get a tech-savvy pun**

  ```bash
  joke --type pun --length short --audience tech-savvy
  ```

- **Get a medium-length knock-knock joke for kids**

  ```bash
  joke --type knock-knock --length medium --audience kids
  ```

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue.

## Support

For support, please reach out to our dedicated support group:

```
/dev/null
```

We value your feedback, but please note that due to high volume, responses may be directed accordingly.