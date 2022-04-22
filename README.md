<h3 align="center">Codice</h3>

---

<p align="center"> Codice is a tool that generates a random password for your account, stores it in a password file and encrypts the file with an encryption of algorithm of your choosing.
    <br> 
</p>

## 📝 Table of Contents

- [Getting Started](#getting_started)
- [Usage](#usage)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

Write about 1-2 paragraphs describing the purpose of your project.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

GnuPG

### Installing

```
cd Codice/
```

chmod +x install.sh

```
./install.sh
```

## 🎈 Usage <a name="usage"></a>

usage: codice.py [-h] [-c CRYPT] [-a APP] [-u USER] [-l LEN] [-o OUT]

optional arguments:
  -h, --help            show this help message and exit

required named arguments:
  -c CRYPT, --crypt CRYPT
                        Encryption algorithm
  -a APP, --app APP     Resitration app Name
  -u USER, --user USER  Username associated with the generated password
  -l LEN, --len LEN     Generated password length
  -o OUT, --out OUT     Output file

## ✍️ Authors <a name = "authors"></a>

- [@kod34](https://github.com/kod34)