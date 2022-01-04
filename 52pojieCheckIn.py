# -*- coding: utf8 -*-
import requests 
from bs4 import BeautifulSoup

cookie = 'htVC_2132_lastvisit=1640654422; htVC_2132_client_created=1640659553; htVC_2132_client_token=DB337DDAD82C15F6BEADBA53D4F0EEFF; htVC_2132_connect_login=1; htVC_2132_connect_is_bind=1; htVC_2132_connect_uin=DB337DDAD82C15F6BEADBA53D4F0EEFF; htVC_2132_atarget=1; htVC_2132_smile=1D1; htVC_2132_ignore_rate=1; htVC_2132_sid=0; htVC_2132_noticonf=642163D1D3_3_1; Hm_lvt_46d556462595ed05e05f009cdafff31a=1640915511,1640915772,1640916675,1641257649; htVC_2132_ttask=642163%7C20220104; htVC_2132_st_p=642163%7C1641257788%7C9a5faa12abe72b02a504c03a2cc82965; htVC_2132_viewid=tid_1489330; htVC_2132_ulastactivity=1641280502%7C0; htVC_2132_lastcheckfeed=642163%7C1641280503; htVC_2132_st_t=642163%7C1641280524%7C324bb6406abb33aad447ed0295b83a3b; htVC_2132_forum_lastvisit=D_66_1640917712D_10_1640917868D_48_1641280524; htVC_2132_visitedfid=48D16D10D66D8; Hm_lpvt_46d556462595ed05e05f009cdafff31a=1641280501; htVC_2132_lastact=1641281293%09forum.php%09ajax'  # 配置你的cookie
sckey = '' # 配置你的server酱SCKEY

def pushinfo(info,specific):
    headers={   
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'ContentType': 'text/html'
    }
    requests.session().get("https://sc.ftqq.com/"+sckey+".send?text=" + info + "&desp=" + specific,headers=headers)

def main(*args):
    headers={
        'Cookie': cookie,
        'ContentType':'text/html;charset=gbk'
    }
    requests.session().get('https://www.52pojie.cn/home.php?mod=task&do=apply&id=2',headers=headers)
    a=requests.session().get('https://www.52pojie.cn/home.php?mod=task&do=draw&id=2',headers=headers)
    b=BeautifulSoup(a.text,'html.parser')          
    c=b.find('div',id='messagetext').find('p').text

    if "您需要先登录才能继续本操作"  in c: 
        pushinfo("Cookie失效", c)
    elif "恭喜"  in c:
        pushinfo("吾爱破解签到成功",c)
    else:
        pushinfo("吾爱破解签到失败",c)
    print(c)


if __name__ == '__main__':
    main()
