# HomeAutomation-RPi

## Basic Authentication Settings
Please create your own ```<root_dir>/auth_config.py``` file containing the following items:
```python
USERNAME = 'your_username'
HASHED_PASSWORD = b"<bytes_here>"
HASH_SECRET = 'your_hash_secret'
```

The basic authentication decorator will automatically check for the authentication header and compare the username and password with the one specified in ```auth_config.py```.
