# 读取文件内容，返回list
import csv


def get_content_for_file(filepath):
    if isinstance(filepath, str):
        with open(filepath, 'r', encoding='UTF-8') as f:
            content_list = []
            for line in f.readlines():
                content_list.append(line.strip())
        return content_list
    else:
        print(u'文件路径需要是字符串')


# 2个文件的list进行比较，有重复取出
def get_same_ip_for_two_file(file1, file2):
    if isinstance(file1, list) and isinstance(file2, list):
        for i in file2:
            if i in file1:
                return i
    else:
        print(u'必须是list类型文件')


# 取重复数据，方法2：将2个list转换成set类型，然后取交集即可
def get_same_ip_for_two_file_another(file1, file2):
    if isinstance(file1, list) and isinstance(file2, list):
        return set(file1) & set(file2)
    else:
        print(u'必须是list类型文件')


# 列表推导式
def get_new_products(file1, file2):
    if isinstance(file1, list) and isinstance(file2, list):
        return [x for x in file2 if x not in file1]


def get_updated_products(file1, file2):
    if isinstance(file1, list) and isinstance(file2, list):
        return [x for x in file1 if x not in file2]


def write_to_file(compare_results,file):
    with open(file, "a+", newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(compare_results)


if __name__ == '__main__':
    latest_file = get_content_for_file(r'./products.csv')
    current_file = get_content_for_file(r'./products2020-04-20.csv')
    print(latest_file)
    print(current_file)
    # for循环方法
    # print(get_same_ip_for_two_file(test_file, test1_file))
    # 转换成set取交集方法
    # print(get_same_ip_for_two_file_another(test_file, test1_file))
    # # 列表推导式
    new_products = get_new_products(latest_file, current_file)
    updated_products = get_updated_products(latest_file, current_file)
    write_to_file(new_products, "./new_products.csv")
    write_to_file(updated_products, "./updated_products.csv")
