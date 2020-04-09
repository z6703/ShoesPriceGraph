class Shoes(object):
    # id = 0
    # name = ''
    # color_info = []
    def __init__(self):
        self.id = 0
        self.name = ''
        self.color_info = []

    def append_color(self, color_info):
        self.color_info.append(color_info)


class ColorInfo(object):
    # color_id = 0
    # color_name = ''
    # img_link = ''
    # price_dict = dict()
    def __init__(self):
        self.color_id = 0
        self.color_name = ''
        self.img_link = ''
        self.price_dict = dict()

    def print_info(self):
        print('id: ', self.color_id)
        print('name: ', self.color_name)
        print('link: ', self.img_link)
        print('price: ', self.price_dict)
