import asyncio
from get_pumpswap_pools import listen_for_new_tokens

if __name__ == "__main__":
    asyncio.run(listen_for_new_tokens())