import wikipedia
import asyncio

async def main():
    print(await wikipedia.summary("John"))
    print(await wikipedia.summary("kek"))
    print(await wikipedia.summary("New York"))
    print(await wikipedia.summary("Internet"))
    print(await wikipedia.summary("Hillary Clinton"))
    print(await wikipedia.summary("Donald Trump"))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
