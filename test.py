from requests import get

def download(url, file_name):
    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)

i=1;

if __name__ == '__main__':
    url = "http://172.21.27.207/kpop/info/LTE_SITE_INFO.php" #LTE_SITE_INFO 다운로드
    download(url, "DAY" + str(i) + ".xlsx")

i += 1

print(i)