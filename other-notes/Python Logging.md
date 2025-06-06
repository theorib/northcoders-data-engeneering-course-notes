# Python Logging
[Basic Logging Tutorial](https://docs.python.org/3/howto/logging.html#)
## Creating a logger instance
```python
import logging

logger = logging.getLogger(__name__)

# setting the log level
logger.setLevel(logging.INFO)
```

## Logging Errors:
```python
logger.error('my error message')
```

## Logging Warnings:
```python
logger.error('my error message')
```

## Logging Levels
[Link to Docs](https://docs.python.org/3/library/logging.html#logging-levels)
| **Level** | **Numeric value** | **What it means / When to use it** |
|---|---|---|
| logging.NOTSET¶ <br> | 0 | When set on a logger, indicates that ancestor loggers are to be consulted to determine the effective level. If that still resolves to NOTSET, then all events are logged. When set on a handler, all events are handled. |
| logging.DEBUG¶ <br> | 10 | Detailed information, typically only of interest to a developer trying to diagnose a problem. |
| logging.INFO¶ <br> | 20 | Confirmation that things are working as expected. |
| logging.WARNING¶ <br> | 30 | An indication that something unexpected happened, or that a problem might occur in the near future (e.g. ‘disk space low’). The software is still working as expected. |
| logging.ERROR¶ <br> | 40 | Due to a more serious problem, the software has not been able to perform some function. |
| logging.CRITICAL¶ <br> | 50 | A serious error, indicating that the program itself may be unable to continue running. |
