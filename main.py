import sys
from random import randint


def generate_random_ip():
    """Generate a random IP address."""
    return '.'.join(str(randint(0, 255)) for _ in range(4))


def generate_wrong_ip():
    """Generate an IP address with one incorrect octet."""
    octets = [randint(0, 255) for _ in range(4)]
    wrong_octet_index = randint(0, 3)
    octets[wrong_octet_index] = 255 + randint(1, 69)
    return '.'.join(map(str, octets))


def print_help_message():
    """Print a help message."""
    print("Usage: python script.py [--wrong] [--bool] [custom_ip]")
    print("--wrong   : Generate an IP address with one incorrect octet.")
    print("--bool    : Print True if the IP is valid, else print the IP.")
    print("custom_ip : Use a custom IP address.")


def parse_ip(ip: str):
    """Parse and validate an IP address."""
    octets = ip.split(".")

    if len(octets) != 4 or not all(octet.isdigit() and 0 <= int(octet) <= 255 for octet in octets):
        print("Invalid IP address. Error: 23FA")
        sys.exit(1)

    return list(map(int, octets))


def check_ip_numbers(ip):
    """Check if IP octets are within the valid range."""
    if any(octet > 255 for octet in ip):
        print("Invalid IP address. Error: 983AF")
        sys.exit(1)


def main():
    if len(sys.argv) < 2:
        input_ip = generate_random_ip()
        print(f"Running with random IP: {input_ip}")

    elif sys.argv[1] == "--wrong":
        input_ip = generate_wrong_ip()

    elif sys.argv[1] == "--help":
        print_help_message()
        sys.exit(0)

    else:
        input_ip = sys.argv[1]

    print(f"The input IP is {input_ip}")

    ip_octets = parse_ip(input_ip)
    check_ip_numbers(ip_octets)

    if "--bool" in sys.argv:
        print(True)
    else:
        print(f"The IP {input_ip} is valid")


if __name__ == '__main__':
    main()
