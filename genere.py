import numpy as np
import spotipy
from keyring.backends._OS_X_API import fw
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time
import logging
import csv
import sys,os
import pickle

cid = '5ee9cd12cb744ff784b5e0f15cfc7ff5'
secret = 'cab13c28bd1549dd9e414da298aa6bb1'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#empty dic

namelist = list(range(9765))
dic = { }
new_dic = dic
newlist = []
#followers	genres	id	popularity	type
#for store
followers = list(range(9765))
genres = list(range(9765))
id_col = list(range(9765))
popularity = list(range(9765))
type_name = list(range(9765))
extra = list(range(9765))


def read_in_csv():
    # address = os.getcwd()
    # print(address)
    csvfile = open("our_muscian_name.csv")
    reader = csv.reader(csvfile)
    m = 0
    for item in reader:
        dic[item[0]] = item[1]
        namelist[m] = (item[0])
        m += 1




def get_artist_attribute(name):
    try:
        results = sp.search(q='artist:' + name, type='artist')
        items = results['artists']['items']
        if len(items) > 0:
            return items[0]
        else:
            return None
    except:
        return None

#followers	genres	id	popularity	type
def fill_in_col():
    not_exist = "None"
    size = len(namelist)
    c = 0
    degree = 0
    for name in namelist:

        degree = float(c / size)
        print("processing: ", degree,"%")

        temp_dic ={}
        try:
            artist = get_artist_attribute(name)
            extra[c] = " "
            temp_dic['name'] = name
            try:
                folnum = artist['followers']['total']
                print("success 1 followers")
                temp_dic["followers"] = folnum
                print("success 2 followers")
                print("sucess: follower: ", folnum)
            except:
                followers[c] = not_exist
            try:
                gen = artist['genres']
                print("success 1 genres")
                temp_dic["geners"] =gen
                print("success 2 genres")
                print("sucess: genres: ", gen)
            except:
                genres[c] = not_exist
            try:
                art_id =artist['id']
                print("success 1 id")
                temp_dic["id"] = art_id
                print("success 2 id")
                print("sucess: id: ", art_id)
            except:
                id_col[c] = not_exist
            try:
                pop = artist['popularity']
                print("success 1 popularity")
                temp_dic["popularity"] = pop
                print("success 2 popularity")
                print("sucess: popularity: ", pop)
            except:
                popularity[c] = not_exist
            try:
                ty = artist['type']
                print("success 1 type")
                temp_dic["type"] = ty
                print("success 2 type")
                print("sucess: type",ty)
            except:
                type_name[c] = not_exist
                print("no name exist")
        except:
            extra[c] = ("didn't find artist")
            temp_dic["extra"] = ("didn't find artist")
            print("didn't find artist")
            pass
        c += 1
        newlist.append(temp_dic)
        de = int(degree)
        if  de == 80. or de == 30. or de == 50. or de == 60. or de == 90. or de == 99.:
            pickle.dump(newlist,p_file2)
            print(newlist)
            print("dump at searching successful")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_in_csv()
    p_file2 = open('pic33.txt', 'wb')

    fill_in_col()

    # pickle.dump(followers,genres,id_col,popularity,type_name, p_file)
    try:
        pickle.dump(newlist, p_file2)
        print("dump newlist to p_file2")
    except:
        pass

    p_file2.close()


    try:
        print("try store newlist to new-new.csv")
        with open('task1-new.csv') as f:
            w = csv.writer(f)
            fieldnames = newlist[0].keys()
            w.writerow(fieldnames)
            for row in newlist:
                w.writerow(row.values())
    except:

        print("can't write list")
        try:
            dataf = pd.DataFrame(newlist)
            dataf.to_csv("newnewnewnew.csv")
        except:
            print("also fail newnewnewnew")
            pass



    # try:
    #     pd.DataFrame(dic).to_csv("star_temp.csv")
    # except:
    #     print("fail to star_temp.csv")
    #     pass

    # try:
    #     data_art = {'artist_name': namelist,'followers': followers,	'genres':genres,
    #                 'id':id_col,'popularity':popularity, 'type':type_name,'memo':extra}
    #     dataframe = pd.DataFrame(data_art)
    #     dataframe.to_csv('task1.csv',index = False)
    # except:
    #     print("task failed")
    #     pass

    #read txt
    # p_file = open('pic.txt','rb')
    # dic1 = pickle.load(p_file)
    # p_file.close()
    #
    # col = ['name','followers','genres','id_col','popularity','type_name']
    # csv_file = "task1-up.csv"
    # print(dic1)
    # try:
    #     with open(csv_file, 'w') as cf:
    #         writer = csv.DictWriter(cf, fieldnames=col)
    #         writer.writeheader()
    #         for data in dic1:
    #             a_name = data
    #             other = data.values()
    #             writer.writerow(other.values())
    # except:
    #     print("error")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
