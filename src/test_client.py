#!/usr/local/bin/python3

# WS client example

import asyncio
import websockets
from aioconsole import ainput


async def run_client():
    async with websockets.connect('ws://localhost:8765') as socket:
        while True:
            raw = await ainput(">>>")

            await socket.send(raw)
            print(f"> {raw}")

            resp = await socket.recv()
            print(f"< {resp}")


if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    event_loop.create_task(run_client())
    event_loop.run_forever()
