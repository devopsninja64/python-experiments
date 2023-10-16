# README

This script requires `Python 3.9.x`

A sample datafile is provided for simple testing.

To run, 
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python topx.py
```

The program will generate an output file named `datafile_sorted` with sorted data.

The maximum size of an array can be adjusted by changing the `MAX_PER_FILE` variable. In case there's not enough memory on the server.

Having it set to the highest number that will not kill a server is ideal. However, having the value set really low could cause an error about having too many open files.
