# IP-Checker

IP-Checker is a Python script designed to generate, validate, and manipulate IP addresses. It provides the ability to generate random IP addresses, generate IP addresses with one incorrect octet, and validate user-supplied IP addresses.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Options](#options)
- [Examples](#examples)
- [License](#license)

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/Kerkpower/ip-checker.git
cd ip-checker
```

## Usage

Run the script using the following command:

```bash
python script.py [options] [custom_ip]
```

## Options

- `--wrong`: Generate an IP address with one incorrect octet.
- `--bool`: Print True if the IP is valid, else print the IP.
- `--help`: Print a help message.

## Examples

1. Generate a random IP:
   ```bash
   python script.py
   ```

2. Generate an IP with one incorrect octet:
   ```bash
   python script.py --wrong
   ```

3. Validate a custom IP:
   ```bash
   python script.py 192.168.0.1
   ```

4. Print True if the IP is valid:
   ```bash
   python script.py --bool 192.168.0.1
   ```

## License

This project is licensed under the [Apache License 2.0](LICENSE).
