#!/usr/local/bin/python3

# WS server example

import asyncio
from aioconsole import ainput
import websockets
import commands


class McServer:

    def __init__(self, host='localhost', port=8765):
        self.is_online = False
        self.host = host
        self.port = port
        self.sockets = set()
        self.event_loop = None

    def start(self):
        async def query_input():
            try:
                while self.is_online:
                    raw = await ainput(">>>")
                    print(f"Console got: {raw}")
                    cmd = self.process(raw)
                    for s in self.sockets:
                        await cmd.send_to(s)
            except Exception as ex:
                self.terminate(str(ex))

        async def query_socket(socket, path):
            print("Client Connected")
            self.sockets.add(socket)
            try:
                while self.is_online:
                    raw = await socket.recv()
                    print(f"Client has connected and sent {raw}")
                    for msg in self.process(raw):
                        await socket.send(msg)
                        resp = await socket.recv()
                        msg(resp)
            finally:
                print("Socket has closed")
                self.sockets.remove(socket)

        print("Initializing Event Loop")
        self.event_loop = asyncio.get_event_loop()

        try:
            print('Attempting to start server')
            start_server = websockets.serve(query_socket, self.host, self.port)
            self.is_online = True
            self.event_loop.run_until_complete(start_server)
            self.event_loop.create_task(query_input())
            print('Server is online and awaiting connections')
            self.event_loop.run_forever()

        except KeyboardInterrupt:
            pass
        except Exception as ex:
            self.terminate(str(ex))
        finally:
            self.terminate("System Shutdown")

    def process(self, raw):
        parts = raw.split(' ')
        cmd_name = parts[0]
        cmd_type = commands.CommandMeta.commands[cmd_name]
        cmd = cmd_type(*parts[1:])
        return cmd

    def terminate(self, msg):
        print(f"Terminating server with message: {msg}")
        self.is_online = False

        if self.sockets:
            for s in self.sockets:
                s.close()
            self.sockets = set()

        if self.event_loop:
            print("Closing Event Loop")
            self.event_loop.stop()
            self.event_loop.close()
            self.event_loop = None


if __name__ == '__main__':
    server = McServer()
    server.start()
