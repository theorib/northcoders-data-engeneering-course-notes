# 2025-04-30 - Day 31 | Bash Cripting and AWS CLI Notes
- Bash scripts should start with a `shebang` which tells your shell which interpreter program to use to execute your script. It ensures that Bash is used to interpret the script, even if you run the file with a different shell. e.g. `#!/bin/bash`
- To access positional arguments we use `$1` `$2`, etc.
- The output of one command can be passed as input to another using the pipe operator `|`