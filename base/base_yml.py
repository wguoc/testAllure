import yaml








def yml_data_with_file(filePath):
    with open("./data/%s.yml" % filePath, "r", encoding="utf-8") as f:
        data = yaml.load(f)
        return data




# if __name__ == '__main__':
#     yml_data_with_file("../data/search_data.yml");