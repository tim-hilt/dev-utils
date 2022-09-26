## Purpose

This script analyzes the imports in a number of java-packages (=== contexts) and finds imports, from foreign packages (aka context-violations).

outputs a json-file in the directory the script is started from.

## Usage

```shell
python main.py --contexts ctx1 ctx2 ctx3 -- /path/to/backend-root
```

## Dependencies

- Python >= v3.10
- Ripgrep
