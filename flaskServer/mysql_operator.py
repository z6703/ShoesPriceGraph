import datetime

import pymysql


class MysqlOperator:
    def __init__(self, ip_address='db', uname='root', password='123456', db_name='db_shoes'):
        self.db_connection = pymysql.Connect(host="182.92.90.232", port=3310, user="root", password="123456",
                                             charset="utf8", db="db_shoes")
        self.cursor = self.db_connection.cursor()
        self.date = str(datetime.date.today())
        self.size_table = [
            '35.5', '36', '36.5', '37.5', '38', '38.5',
            '39', '40', '40.5', '41', '42', '43', '43.5', '44', '44.5',
            '46', '47', '47.5', '48',
        ]
        # self.cursor.execute("SELECT VERSION()")
        # data = self.cursor.fetchone()
        # print ("Database version : %s " % data)

    def __del__(self):
        self.db_connection.close()

    def run_sql_file(self, path='script.sql'):
        with open(path, 'r+') as f:
            sql_list = f.read().split(';')[:-1]  # sql文件最后一行加上;
            sql_list = [x.replace('\n', ' ') if '\n' in x else x for x in sql_list]
        for sql_item in sql_list:
            self.cursor.execute(sql_item)

    def sql_excute(self, sql):
        try:
            self.cursor.execute(sql)
            self.db_connection.commit()
        except:
            self.db_connection.rollback()

    def insert_shoes_data(self, shoes):
        """
        input:shoes class
        output:None
        """
        sql = "INSERT INTO Shoes(id, name) \
                VALUES ('%s', '%s')" % \
              (shoes.id, shoes.name)
        self.sql_excute(sql)

        for color in shoes.color_info:
            sql = "INSERT INTO ShoesColor(color_id, color_name, img_link) \
                VALUES ('%s', '%s', '%s')" % \
                  (color.color_id, color.color_name, color.img_link)
            self.sql_excute(sql)

            for size in color.price_dict.keys():
                if color.price_dict[size] == 0:
                    continue

                sql = "INSERT INTO ShoesPrice(shoes_id, shoes_color_id, size,update_time,price) \
                    VALUES ('%s', '%s', '%s', '%s', '%s')" % \
                      (shoes.id, color.color_id, self.size_table.index(size), self.date, color.price_dict[size])
                self.sql_excute(sql)

    # def search_by_shoes_id(self,shoes_id,color_id=-1,size=-1):
    #     """
    #     output:If nothing was found, return None. Else, a Shoes class.
    #     """
    #     sql = "SELECT * FROM Shoes WHERE id ='%s'"%(shoes_id)
    #     self.sql_excute(sql)
    #     try:
    #         shoes_info = Shoes()
    #         shoes_info.id ,shoes_info.name = self.cursor.fetchone()
    #     except:
    #         return None

    #     sql = "SELECT * FROM ShoesPrice WHERE shoes_id ='%s' "%(shoes_id)
    #     if not color_id == -1:
    #         sql += " AND shoes_color_id='%s' "%(color_id)
    #     if not size == -1:
    #         sql += " AND size='%s' "%(size)
    #     self.sql_excute(sql)   
    #     color_search_result = self.cursor.fetchall()
    #     for row in color_search_result:
    #         _,color_id,size,date,price = row
    #         size = self.size_table[int(size)]

    #         index = shoes_info.find_color_date(color_id,date)
    #         if index ==-1:
    #             color_info = ColorInfo()
    #             color_info.color_id,color_info.date = color_id,date
    #             color_info.price_dict[size] = price
    #             sql = "SELECT * FROM ShoesColor WHERE color_id ='%s'"%(color_id)
    #             self.sql_excute(sql) 
    #             _,color_info.color_name,color_info.img_link = self.cursor.fetchone()
    #             shoes_info.append_color(color_info)
    #         else:
    #             shoes_info.color_info[index].price_dict[size] = price

    #     return shoes_info

    def search_by_name(self, name):
        sql = "SELECT * FROM Shoes WHERE name like '%" + name + "%' "
        self.sql_excute(sql)
        result_list = [] # id , name, color_num, link
        try:
            for row in self.cursor.fetchall():
                result_list.append([row[0],row[1]])
        except:
            return None

        for i,item in enumerate(result_list):
            shoes_id,_=item
            sql = "SELECT DISTINCT shoes_color_id FROM ShoesPrice WHERE shoes_id=%s" % shoes_id
            self.sql_excute(sql)
            try:
                color_ids = self.cursor.fetchall()
            except:
                return None
            result_list[i].append(len(color_ids))

            sql = "SELECT img_link FROM ShoesColor WHERE color_id=%s" % color_ids[0]
            self.sql_excute(sql)
            try:
                result_list[i].append(self.cursor.fetchone()[0])
            except:
                return None

        return result_list

    def search_color_id(self, shoes_id):
        sql = "SELECT DISTINCT a.color_name,a.img_link,a.color_id \
                FROM ShoesColor a INNER JOIN ShoesPrice b \
                on a.color_id=b.shoes_color_id \
                WHERE shoes_id=%s" % shoes_id
        self.sql_excute(sql)

        result = []
        try:
            for row in self.cursor.fetchall():
                result.append([row[0], row[1], row[2]])

        except:
            return None

        return result

    def search_size_list(self, shoes_id, color_id):
        sql = "SELECT DISTINCT size FROM ShoesPrice WHERE shoes_id=%s and shoes_color_id=%s " % (shoes_id, color_id)
        self.sql_excute(sql)
        size_list = []
        try:
            for row in self.cursor.fetchall():
                size_list.append(self.size_table[row[0]])
        except:
            return None
        return size_list

    def search_price_data(self, shoes_id, color_id, size):
        sql = "SELECT  name FROM Shoes WHERE id=%s" % (shoes_id)
        self.sql_excute(sql)
        result_dict = dict()
        try:
            result_dict['shoes_name'] = self.cursor.fetchone()
        except:
            return None

        sql = "SELECT color_name,img_link FROM ShoesColor WHERE color_id=%s" % (color_id)
        self.sql_excute(sql)
        try:
            result_dict['color_name'], result_dict['img_link'] = self.cursor.fetchone()
        except:
            return None

        sql = "SELECT price,update_time as date \
                FROM ShoesPrice \
                WHERE shoes_id=%s and shoes_color_id=%s and size=%s " % (
            shoes_id, color_id, self.size_table.index(str(size)))
        self.sql_excute(sql)
        price_list, date_list = [], []
        try:
            for row in self.cursor.fetchall():
                price_list.append(row[0])
                date_list.append(row[1])
        except:
            None
        result_dict['price_list'], result_dict['date_list'] = price_list, date_list

        return result_dict


if __name__ == "__main__":
    a = MysqlOperator()

    # del a
    f = open('shoes.pkl', 'rb')
    # data = pickle.load(f)
    # a.run_sql_file()
    # a.insert_shoes_data(data)

    # b = a.search_by_shoes_id(data.id)
    # # print(b.id,b.name,end='\n\n')
    # for item in b.color_info:
    #     item.print_info()

    b = a.search_by_name('nik')
    print(b)
    # print("--------------------")
    # b = a.search_color_id(424041)
    # print(b)
    # print("--------------------")
    # b = a.search_size_list(424041, 1362818)
    # print(b)
    # print("--------------------")
    # b = a.search_price_data(424041, 1350886, 43)
    # print(b.keys())
    # print("--------------------")
    # print(b['img_link'], b['price_list'], b['date_list'])
