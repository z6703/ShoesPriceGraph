import pickle
import shoes

import redis

# r = redis.Redis(host="localhost", port=6379, decode_responses=True)
# r.set("name", "A")
# print(r["name"])
# print(r.get("name"))
pkl_file = open('shoes.pkl', 'rb')
obj = pickle.load(pkl_file)
for i in obj.color_info:
    i.print_info()
