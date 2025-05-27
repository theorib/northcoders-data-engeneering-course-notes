# uv

## Resources
[uv main website](https://docs.astral.sh/uv/)
[Real Python uv Article](https://realpython.com/python-uv/)

## Commands

### initializing a project
```bash
uv init
```

### Adding all dependencies from a requirements.txt
```bash
uv add -r requirements.txt
```

### Adding packages as dev dependencies
```bash
uv add --dev pytest
```

### upgrading a package
```bash
uv add --upgrade requests
```

### removing a package
```bash
uv remove requests
```

### adding all dependencies, creating venv, etc
```bash
uv sync
```


### running a file
```bash
uv run main.py
```