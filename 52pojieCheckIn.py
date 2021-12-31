# -*- coding: utf8 -*-
import requests 
from bs4 import BeautifulSoup

cookie = 'htVC_2132_saltkey=qTcxhDV1; htVC_2132_lastvisit=1640654422; htVC_2132_client_created=1640659553; htVC_2132_client_token=DB337DDAD82C15F6BEADBA53D4F0EEFF; htVC_2132_auth=1017fw2ogY8rXsm57BqEF3IBMlzOkS63gVgqahWGkuwHQTqAr01RP4JdES00r5l6ZP6iYkJJH9IItxEZ3SXiC8mU7BM; htVC_2132_connect_login=1; htVC_2132_connect_is_bind=1; htVC_2132_connect_uin=DB337DDAD82C15F6BEADBA53D4F0EEFF; htVC_2132_sid=0; htVC_2132_atarget=1; htVC_2132_smile=1D1; htVC_2132_forum_lastvisit=D_10_1640853431D_66_1640871577D_48_1640872508; htVC_2132_noticonf=642163D1D3_3_1; htVC_2132_ulastactivity=1640915509%7C0; wzws_sid=66bd5bc06ea740b6cdb426489d652bc5b9ec16aefa2f90e2e060e5142f0206662fc7a59f1513225f230611a6ff78e531052af0a944569f32c92026774aba427c77a12e8b4b1f4390a5d843c22c7211f6; htVC_2132_ttask=642163%7C20211231; htVC_2132_visitedfid=16D48D66D10D8; htVC_2132_viewid=tid_1229300; htVC_2132_st_p=642163%7C1640916674%7Cc33d7058f7f0e85dcf69f79ee8f20c81; htVC_2132_lastcheckfeed=642163%7C1640916674; htVC_2132_checkfollow=1; htVC_2132_checkpm=1; htVC_2132_noticeTitle=1; Hm_lvt_46d556462595ed05e05f009cdafff31a=1640871564,1640915511,1640915772,1640916675; htVC_2132_onlineusernum=42457; Hm_lpvt_46d556462595ed05e05f009cdafff31a=1640916694; htVC_2132_lastact=1640916694%09plugin.php%09; useragent=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85Ni4wLjQ2NjQuMTEwIFNhZmFyaS81MzcuMzY%3D; '  # 配置你的cookie
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
