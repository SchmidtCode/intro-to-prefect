#!/usr/bin/env python3

from prefect import flow


@flow
def collect_petstore_inventory():
    print("Collecting inventory from the Petstore API...")


def main():
    print("hello world")


if __name__ == "__main__":
    main()
