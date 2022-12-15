import click
import aiohttp
import asyncio
import os
import json


@click.command()
@click.option("--typ", required=True, help="CPE type.")
@click.option("--product", default="*", help="CPE product.")
@click.option("--vendor", default="*", help="CPE vendor.")
@click.option("--version", default="*", help="CPE version.")
def search(typ, product, vendor, version):
    url = "https://services.nvd.nist.gov/rest/json/cves/1.0?cpeMatchString=cpe:2.3:"

    if typ[0] == "a":
        url += "a"
    elif typ[0] == "h":
        url += "h"
    elif typ[0] == "o":
        url += "o"
    else:
        raise typ

    url += ":" + product + ":" + vendor + ":" + version

    async def req(index=0):
        print("Requesting url", index)
        print(url)
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url + "&startIndex=" + str(index), proxy=os.getenv("HTTP_PROXY", None)
            ) as response:

                print("Status:", response.status)
                print("Content-type:", response.headers["content-type"])

                html = await response.text()
                return html

    async def main():
        total = totalResults(await req(0))
        import math

        pages = math.ceil(total / 20)  # todo не 20

        print("total pages", pages)

        tasks = []
        for i in range(0, 3):
            tasks.append(req(i * 20))
        asyncio.gather(*tasks)

        for i in range(0, 3):
            handle(await tasks[i])

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


def totalResults(text):
    data = json.loads(text)
    return data["totalResults"]


def handle(text):
    print("handle", len(text))
    data = json.loads(text)
    for cve in data["result"]["CVE_Items"]:
        print(
            cve["cve"]["CVE_data_meta"]["ID"],
            ",",
            cve["impact"]["baseMetricV3"]["cvssV3"]["attackVector"],
        )


search()
