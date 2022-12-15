import pandas as pd


def clean_author(csv_path, save_path=None):
    if save_path is None:
        save_path = 'D:\\2022-2023大三上学习笔记\\数据库系统\\WHU-MMS\\admin\\database\\book_crawler\\sample_data\\dushu_clean.csv'


    with open(csv_path, 'r', encoding='utf-8') as fp:
        raw_data = pd.read_csv(fp, index_col=False)
        authors = raw_data["author"].tolist()
        title = raw_data["title"].tolist()
        for i in range(len(authors)):
            # if i == 5684:
            #     print(authors[i])
            #     print(title[i])
            # if type(authors[i]) == str:
            #     if len(authors[i]) > 25:  # 这是简介
            #         authors[i] = "佚名 著"
            #     else:
            #         authors[i] = authors[i].replace('（', '[').replace('）', ']')
            #         authors[i] = authors[i].replace('(', '[').replace(')', ']')
            #         authors[i] = authors[i].replace('【', '[').replace('】', ']')
            #         authors[i] = authors[i].replace('〔', '[').replace('〕', ']')
            #         authors[i] = authors[i].replace('；', '，')
            #         if authors[i] == '著':
            #             authors[i] = authors[i].replace('著', '佚名 著')
            #         if authors[i] == '著，':
            #             authors[i] = authors[i].replace('著，', '佚名 著')
            #         if authors[i] == '注':
            #             authors[i] = authors[i].replace('注', '佚名 注')
            #         if authors[i] == '注，':
            #             authors[i] = authors[i].replace('注，', '佚名 注')
            #         if authors[i] == '编':
            #             authors[i] = authors[i].replace('编', '佚名 编')
            #         if authors[i] == '编，':
            #             authors[i] = authors[i].replace('编，', '佚名 编')
            #         if authors[i] == "译":
            #             authors[i] = authors[i].replace('译', '佚名 译')
            #         if authors[i] == "译，":
            #             authors[i] = authors[i].replace('译，', '佚名 译')
            #         if authors[i] == "，" or authors[i] == "暂缺简介..." or authors[i] == "等著" or authors[i] =="主编" or authors[i] == "暂缺作者" or authors[i] == "等编著" or authors[i] == "等著" or authors[i] == "等主编" or authors[i] == "主编，" or authors[i] == "等" or authors[i] == "绘":
            #             authors[i] = "佚名 著"
            #         if authors[i] == "编著" or authors[i] == "编辑" or authors[i] == "编写" or authors[i] == "撰":
            #             authors[i] = "佚名 著"
            #         if "[" in authors[i] and "]" in authors[i] and len(authors[i]) <= 4 or authors[i] == "春秋":
            #             authors[i] = authors[i] + " 佚名 著"
            #         if not("著" in authors[i] or "注" in authors[i] or "编" in authors[i] or "译" in authors[i]):
            #             authors[i] = authors[i] + " 著"
            #         if authors[i] == "、 著":
            #             authors[i] = "佚名 著"
            #         if "、" in authors[i]:
            #             authors[i].replace("、", "，")
            # else:
            #     authors[i] = "佚名 著"
            if "[等]主编" in authors[i] or "选注" in authors[i] or "总主编" in authors[i] or "[等]著" in authors[i]:
                authors[i] = "佚名 著"
        authors = pd.DataFrame(authors)
        raw_data["author"] = authors
        release_date = raw_data["release_date"]
        isbn = raw_data["ISBN"]
        isbn = isbn.tolist()
        release_date = release_date.tolist()
        for i in range(len(release_date)):
            if release_date[i] == "精装" or "cm" in release_date[i]:
                release_date[i] = isbn[i]
                isbn[i] = "未知"
        raw_data["release_date"] = release_date
        raw_data["ISBN"] = isbn
        # raw_data.drop(axis=1)
        raw_data.to_csv(save_path, index=False)



if __name__ == '__main__':
    clean_author('D:\\2022-2023大三上学习笔记\\数据库系统\\WHU-MMS\\admin\\database\\book_crawler\\sample_data\\dushu_clean.csv')
    # df = pd.read_csv("D:\\2022-2023大三上学习笔记\\数据库系统\\WHU-MMS\\admin\database\\book_crawler\\sample_data\\dushu_clean.csv")
    # df = df.drop(["id"], axis=1)
    # df.to_csv("D:\\2022-2023大三上学习笔记\\数据库系统\\WHU-MMS\\admin\database\\book_crawler\\sample_data\\dushu_clean.csv")
