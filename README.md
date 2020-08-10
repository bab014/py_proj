# Experimenting with files and the Progress module

```python
import progress as pg
import pwd
import os

print('> Login: ' + pwd.getpwuid(os.getuid()).pw_name)
```