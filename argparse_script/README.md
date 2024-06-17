## Python script

### Run

1. Example
``` sh
$ python script.py -h
usage: script.py [-h] message
Process some strings.
positional arguments:
  message     The message to display
optional arguments:
  -h, --help  show this help message and exit
```

2. Example:
```sh
$ python script.py 
usage: script.py [-h] message
script.py: error: the following arguments are required: message
```

3. Example

```sh
$ python script.py "Hello, World !!!"
python script.py "Hello, World python script.py !"
Hello, World python script.py !
val@ubuntu:~/sda4/py_simple_apps/argparse_script$ 
```

