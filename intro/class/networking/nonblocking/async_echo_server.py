# /networking/nonblocking/async_echo_server.py
import asyncio

ENCODING = "utf8"


class EchoServerProtocol(asyncio.Protocol):
    def __init__(self):
        super().__init__()
        self._transport = None

    # Called when we accept a new connection
    def connection_made(self, transport: asyncio.BaseTransport):
        peername = transport.get_extra_info("peername")
        print(f"Connection from {peername}")
        self._transport = transport

    # Called when new data is incoming
    def data_received(self, data: bytes) -> None:
        message = data.decode(ENCODING)
        print(f"Data received: {message}")

        message = message.upper()
        self._transport.write(message.encode(ENCODING))

    def connection_lost(self, exc: Exception):
        peername = self._transport.get_extra_info("peername")
        print(f"Lost connection from {peername}")
        return super().connection_lost(exc)


async def main():
    # Get a reference to the event loop since we are using
    # low-level APIs

    loop = asyncio.get_running_loop()
    host = "127.0.0.1"
    port = 5001

    server = await loop.create_server(lambda: EchoServerProtocol(), host, port)

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
