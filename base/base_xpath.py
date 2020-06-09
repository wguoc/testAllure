
# //*[contains(@text,'设')]
# //*[@text='设']
# //*[@text='设' and contains(@text,'设') and @text='设']

# "text,设置"
# "text,设置，1"
# "text,设置, 0"
# ["text,设置" , "text,设置,1", "text,设置,0"]
from selenium.webdriver.common.by import By


def make_xpath_with_unit_feature(loc):
    """
    拼接xpath中间的部分
    :param loc:
    :return:
    """
    key_index = 0
    value_index = 1
    option_index = 2

    args = loc.split(",")
    feature = ""

    if len(args) == 2:
        feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + "and"
    elif len(args) == 3:
        if args[option_index] == "1":
            feature = "@" + args[key_index] + "='" +args[value_index] + "'" + "and"
        elif args[option_index] == "0":
            feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + "and"

    return feature

def make_xpath_with_feature(loc):
    feature_start = "//*["
    feature_end = "]"
    feature = ""

    if isinstance(loc, str):
        # 如果是正常的xpath
        if loc.startswith("//"):
            return loc

        # loc str
        feature = make_xpath_with_unit_feature(loc)
    else:
        # loc 列表
        for i in loc:
            feature += make_xpath_with_unit_feature(i)

    feature = feature.rstrip("and")

    loc = feature_start + feature + feature_end

    return loc


def main():
    # loc = "text,设置"
    # loc = "text,设置,1"
    # loc = ["text,设置"]
    # loc = ["text,设置", "index,20,1", "index1,50"]
    loc = "//*[contains(@text11111,'设')]"
    a = make_xpath_with_feature(loc)
    # a = make_xpath_with_unit_feature(loc)
    print(a)

    search_button = By.ID, "@android/title"
    back_button = By.XPATH, "//*[@index='0']"
    back_button1 = By.XPATH, "text,0"

    find_el(back_button1)

def find_el(loc):
    loc_by = loc[0]
    loc_value = loc[1]

    # driver.find_element(loc_by, loc_value)
    # driver.find_element(by.id, "@android/title")
    # driver.find_element(by.xpath, "//*[xxxxxx]")


if __name__ == '__main__':
    main()










