import pandas as pd
import yaml
import IEEE


def save_data(data: list,source,topic):
    inf = pd.DataFrame(data, columns=['article', 'author',  'url','DOI','year'])
    outputpath = ('{}_{}.csv'.format(source,topic))  #填写你要保存的路径
    inf.to_csv(outputpath, sep=',', index=False, header=True, encoding='UTF-8')


def load():
    with open("config.yml","r") as f:
        config=yaml.load(f.read(),Loader=yaml.Loader)
        return config

def crawler():
    config=load()
    topics=config["Topic"]
    sources=config["Source"]
    for source in sources:
        for topic in topics:
            if source=="IEEE":
                data=IEEE.get_paperinfo(topic)
                save_data(data,source,topic)

crawler()