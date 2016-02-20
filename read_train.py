#隨手寫讀檔的時候發現讀到一半會出現編碼錯誤，這是股溝大神改好的
import csv

def read_train(path):
    with open(path, newline='', encoding = 'ISO-8859-1') as csvfile:
        #用ISO-8859-1開才不會有編碼問題，不知為何
        train_file = csv.reader(csvfile, delimiter=',')
        id = []
        product_uid = []
        product_title = []
        search_term = []
        relevance = []
        row_id = 1
        for row in train_file:
            if row_id > 1:
                id.append(row[0])
                product_uid.append(1)
                product_title.append(2)
                search_term.append(3)
                relevance.append(4)
            row_id += 1
        return id, product_uid, product_title, search_term, relevance

path = 'train.csv'
[id, product_uid, product_title, search_term, relevance] = read_train('train.csv')
