# Python File Handling

## Creating a directory if it doesn't exist
`os.makedirs` is recursive and will create all directories if they don't exist, not only the rightmost one. `exist_ok=True` means it won't throw an error if the directory already exists, it will just leave the existing directory untouched.
```python
os.makedirs(os.path.dirname("some_folder/some_other_folder"), exist_ok=True)
```

This is a non recursive way of doing it and we have to do the check for the directory existing ourselves. We also have to create each directory in a chain separately.
```python
if not os.path.exists('sample_dir'):
    os.mkdir('sample_dir')
```

## Deleting Files
Ra
```python
os.remove('file_path/file_name.file_extension')
```

## Deleting All folders
