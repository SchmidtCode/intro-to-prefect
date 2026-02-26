#!/usr/bin/env python3

import httpx
from prefect import flow, get_run_logger, task


@task
def retrieve_from_api(
    base_url: str,
    path: str,
    secure: bool,
):
    logger = get_run_logger()
    if secure:
        url = f"https://{base_url}{path}"
    else:
        url = f"http://{base_url}{path}"
    response = httpx.get(url)
    response.raise_for_status()
    inventory_stats = response.json()
    logger.info(inventory_stats)


@flow
def collect_petstore_inventory(
    base_url="petstore.swagger.io",
    path="/v2/store/inventory",
    secure=True,
):
    inventory_stats = retrieve_from_api(
        base_url,
        path,
        secure,
    )


def main():
    collect_petstore_inventory.serve("petstore-collection-deployment")


if __name__ == "__main__":
    main()
