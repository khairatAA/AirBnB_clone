# Airbnb Clone - The console

![HBNB](https://mma.prnewswire.com/media/1121685/Airbnb_Logo.jpg?p=twitter "HBNB Logo")

## Table of Content

- [Background-Context](#Background-Context)
- [The-console](#The-console)
- [Installation](#Installation)
- [Execution](#Execution)
- [Usage](#Usage)
- [Authors](#Authors)

## Background-Context

Welcome to the `AirBnB clone project!`.

This project represents a significant milestone as it marks the first step towards building a full web application – the AirBnB clone. This initial phase is crucial because it lays the foundation for the entire project, including HTML/CSS templating, database storage, API, and front-end integration.

## What can the console do???

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## Installation

- Git clone the repository `https://github.com/khairatAA/AirBnB_clone.git`

- Navigate to the cloned repository

## Execution

The console works like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

But also in non-interactive mode:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## Usage

- Type the `help` command to see how to use to navigate the console.

```
(hbnb)
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help all
Prints all string representation of all instances based or not on the class name.

(hbnb)
```

## Authors

- Adesina Khairat <khairatadesina01@gmail.com>
- Adebanjo Emmanuel <emmanueladebanjo01@gmail.com>
