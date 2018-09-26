import  pandas as pd
import  requests
#读取数据
def read_csv():
    path=input('请输入导入数据的文件路径');
    file=pd.read_csv(path,engine='python');
    return file
#提取数据中的title列
def extract_data(file):
    data=file['title']
    return data
#遍历数据返回每条数据的经纬度
def mapping(data):
    l=[]
    ak='6atYrs16wC5oTo66s2NvXDsuzd4aenLX'
    url='http://api.map.baidu.com/geocoder/v2/?address={}&output=json&ak={}&ret_coordtype=gcj02ll'
    n=0
    for i in data:
        n+=1
        print('已成功匹配{}条数据'.format(n))
        u=url.format(i,ak)
        r=requests.get(u).json()
        lng=r['result']['location']['lng']
        lat=r['result']['location']['lat']
        l.append([i,lng,lat])
    result=pd.DataFrame(l,columns=['title','lng','lat'])
    return result
#存储函数
def save_data(result):
    result.to_csv('./result.csv',index=0)
    print('已完成！');

#主函数
def main():
    file=read_csv()
    data=extract_data(file)
    result=mapping(data)
    save_data(result)


if __name__ == '__main__':
        main()
