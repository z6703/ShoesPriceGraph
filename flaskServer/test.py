import pickle
import shoes
import controller
import redis

# r = redis.Redis(host="localhost", port=6379, decode_responses=True)
# r.set("name", "A")
# print(r["name"])
# print(r.get("name"))
# pkl_file = open('shoes.pkl', 'rb')
# obj = pickle.load(pkl_file)
# print(obj.id)
# print(obj.name)
# for i in obj.color_info:
#     print(i.color_id)
#     print(i.color_name)
#     print(i.img_link)
#
# c = controller.Controller()
# print(c.search_specific_shoes(1))