# StackMeOver

Executes the first StackOverflow code snippet matching a query. By default it will ask you to confirm the code before it is run, but this can be disabled in YOLO-mode.


## Requirements
`python3.x` and the module [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
There's probably some modules that I've forgot to mention, but if you made it this far you'll probably figure it out yourself.

## Usage
```
main.py [-h] [--y] query

Executes the first StackOverflow code snippet matching your query

positional arguments:
query       The query you wish to search for

options:
-h, --help  show this help message and exit
--y         YOLO mode - runs the retrieved command without asking for confirmation or even telling you what it is
```

