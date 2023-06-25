import socket
import asyncio
import aiohttp


#
# ------Beginner-------#
# async def aprint():
#     print("this is an Async print !")
#
#
# async def main():
#     await aprint()
#
#
# asyn.run(main())

# ------Web Scraping-------#
async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    urls = ['https://www.digikala.com', 'https://www.google.com']
    tasks = [asyncio.create_task(fetch(url)) for url in urls]
    results = await asyncio.gather(*tasks)
    print(results)


if __name__ == '__main__':
    asyncio.run(main())

# ------Data streaming -------#

# async def process_stream(stream):
#     async for data in stream:
#          #process data
#
# async def main():
#     streams = [open(f'file_{i}.txt', 'r') for i in range(10)]
#     tasks = [asyncio.create_task(process_stream(stream)) for stream in streams]
#     await asyncio.gather(*tasks)
#
# if __name__ == '__main__':
#     asyncio.run(main())


# ------Network programing -------#
# async def handel_client(client_reader, client_writer):
#     data = await client_reader.read(1024)
#     message = data.decode()
#     address = client_writer.get_extra_info('peername')
#     print(f'Received{message!r} from {address!r}')
#     client_writer.close()
#
#
# async def main():
#     server = await asyncio.start_server(handel_client, '127.0.0.1', 8000)
#     async with server:
#         await server.serve_forever()
#
#
# if __name__ == '__main__':
#     asyncio.run(main())
#
