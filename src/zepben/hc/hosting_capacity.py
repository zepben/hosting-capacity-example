import asyncio
import json
from typing import Dict

from zepben.eas.client.eas_client import EasClient, WorkPackageConfig


async def main():
    auth_config = read_json_config("auth_config.json")
    eas_client = EasClient(
        host="<some_host>",
        port=443,
        protocol="https",
        client_id="<some_client_id>",
        username="<some_user>",
        password="<some_pass>",
        verify_certificate=True,
    )

    result = await eas_client.async_run_hosting_capacity_work_package(WorkPackageConfig(["CPM3B3"], [2023], ["base"]))

    print(f'work_package_id={result["data"]["runHostingCapacity"]}')
    await eas_client.aclose()


def read_json_config(config_file_path: str) -> Dict:
    file = open(config_file_path)
    config_dict = json.load(file)
    file.close()
    return config_dict


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
