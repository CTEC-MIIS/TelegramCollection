from telethon import TelegramClient
from telethon import utils
import pandas as pd

# Remember to use your own values from my.telegram.org!
api_id = YOURID
api_hash = 'YOURHASH'
client = TelegramClient('anon', api_id, api_hash)

async def main():
    # Getting information about yourself
    l = []
    # You can print the message history of any chat:
    async for message in client.iter_messages('CHANNEL NAME'):

        if message.forward is not None:
            try:
                id = message.forward.original_fwd.from_id
                if id is not None:
                    ent = await client.get_entity(id)
                    print(ent.title)
                    l.append(["CHANNEL NAME", ent.title])
            except:
              print("An exception occurred")



        # You can download media from messages, too!
        # The method will return the path where the file was saved.

        # if message.photo:
        #     path = await message.download_media()
        #     print('File saved to', path)  # printed after download is done
    df = pd.DataFrame(l, columns = ['From', 'To'])
    df.to_csv('ef_edgelist.csv')

with client:
    client.loop.run_until_complete(main())
#
# ### SECOND RUN
# async def new_main():
#     # Getting information about yourself
#     df = pd.read_csv('ef_edgelist.csv')
#     df = df.To.unique()
#     l = []
#     # You can print the message history of any chat:
#     for i in df:
#         async for message in client.iter_messages(i):
#             if message.forward is not None:
#                 try:
#                     id = message.forward.original_fwd.from_id
#                     if id is not None:
#                         ent = await client.get_entity(id)
#
#                         l.append([i, ent.title])
#                 except:
#                     print("An exception occurred")
#         print("Next channel: ", i)
#     df = pd.DataFrame(l, columns = ['From', 'To'])
#     df.to_csv("ecofash_net.csv")
#
#
#         # You can download media from messages, too!
#         # The method will return the path where the file was saved.
#
#         # if message.photo:
#         #     path = await message.download_media()
#         #     print('File saved to', path)  # printed after download is done
# with client:
#     client.loop.run_until_complete(new_main())
