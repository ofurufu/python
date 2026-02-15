# list-dir-files

A small, dependency-free Python script that lists files for one or more directories you provide.

## Summary

`list-dir-files.py` prompts the user to enter one or more directory paths (separated by spaces) and prints the contents and item counts for each directory. It handles common errors like missing directories and permission issues.

## Features

- Accepts multiple directories in a single prompt
- Prints an item count and lists each file/directory name
- Gracefully handles `FileNotFoundError` and `PermissionError`

## Requirements

- Python 3.6+
- No external packages required

## Installation

Clone or download this repository and run the script with your Python interpreter.

```bash
git clone <repo-url>
cd list-dir-files
```

## Usage

Run the script and, when prompted, provide one or more directory paths separated by spaces.

```bash
python list-dir-files.py
```

Example input (Windows):

```
C:\Users\ME\Documents C:\Temp
```

Example input (POSIX):

```
./examples /var/log
```

Sample output produced by the script:

```
Please provide list of dir(s) with spaces inbetween: ./examples /var/log

====== Listing files in ./examples =====
(3 items)
file1.txt
file2.log
subdir

====== Listing files in /var/log =====
(12 items)
syslog
kern.log
...

===== Done listing all dir(s) =====
```

## Short example

Run the script and enter two paths separated by a space when prompted.

Input:

```
./examples /var/log
```

Minimal output:

```
====== Listing files in ./examples =====
(3 items)
file1.txt
file2.log
subdir
====== Listing files in /var/log =====
(12 items)
syslog
kern.log
...
===== Done listing all dir(s) =====
```

## Error handling

- If a directory does not exist, the script prints an error and continues to the next path.
- If the script lacks permission to read a directory, it prints a permission error and continues.

## Notes

- Paths containing spaces should be quoted when invoking from shells that split arguments; however this script reads a single prompt line and splits on spaces, so to provide a directory path that contains spaces, run the script from a shell and use an escaped or quoted path as appropriate for your OS.
- The script lists entries returned by `os.listdir()`, which includes files and subdirectories but does not recurse into subdirectories.

## Contributing

Contributions and suggestions are welcome—please open an issue or submit a pull request.

## License

This project is unlicensed. Add a `LICENSE` file if you wish to apply an open-source license (for example, MIT).

## Author
 Ayodele Adewuyi
 
README for `list-dir-files.py`.

