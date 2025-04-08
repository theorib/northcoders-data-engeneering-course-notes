# 2025-04-07 - Notes
## File Imput and Output
```python

mistery_file = open('file1.txt', mode='a', encoding='utf8')

mistery_file.write('Good Morning')

# Very important to close streams
mistery_file.close()

```

### encoding, decoding and importance of codecs
binary `1`, `0`, each block is a bit
every 8 bits are equivalent to a byte of data
every byte can hold 256 different values

encoding, getting text into bytes, decoding getting bytes into text

What byte should translate into each character:


`bytestring` with byte literals
`b'some string'`byte literals

### `with` context manager
```python

with open('file1.txt', mode='a', encoding='utf8') as file_object:
    pass

```





### Serialisation



### Questions
- What is a stream
- Why exactly do we need to close the process if every time we alter a file we have to write code to deliberately do it

### JSON
"JavaScript Object Notation"
JSON is a string but it looks like a data structure
going from string to JSON and vice versa is called Serialization and De-serialization

#### Why
- Lightweight
- Readable
- Commonly used on the internet
- Looks like a python dictionary but it isn't

#### Methods
`json.dumps(data)` -> string
`json.loads(json_str)` -> dict

## Python
### Structure of Python Projects
- `data`
- `scripts`
    - Bash scripts and the like
- `src`
- `src/helpers`
- `tests`
    - Any temporaty tests that are failing but expecting to fail we should mark them as XFAIL
    ```python
    @pytest.mark.xfail(reason='my reason')
    def test_():
        pass
    
    
    ```
    
- `.gitignore`
- `README.md`
    - Instructions on how to set up the repository and use it
    - description
    - dependencies
    - licensing
    - where it is deployed
    - who the team are
- `requirements.txt`

### PEP8
- [Pep8 Docs](https://peps.python.org/pep-0008/)
### Tools for code compliance
- [Black](https://black.readthedocs.io/en/stable/index.html#)
- Flake8
- autopep8
### docstrings
- [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
### type hints
- [Pydantic](https://docs.pydantic.dev/latest/)
    `@validate_call`
### Pythonic coding
