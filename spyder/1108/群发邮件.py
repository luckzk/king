# -*- coding: utf-8 -*-
'''
#intent      :
#Author      :Michael Jack hu
#start date  : 2018/11/8
#File        : 群发邮件.py
#Software    : PyCharm
#finish date :
'''

import requests

header = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'cookie':'pgv_pvi=1911784448; RK=bhTNzmcg9P; ptcz=2868d411bba8bf395e813f9532cb2fc0e45785fe0fa879af1fcacf8d63bb13f6; pgv_pvid=717600508; LW_uid=F115o2H219O984u087v6T8t0N3; eas_sid=j145E202z9r9R4O0s7P7S1v5Q0; tvfe_boss_uuid=4a8d324bff07fae2; pgv_pvid_new=1062272335_82c4a91433; ue_uid=52da62ea0b4e3b5e0c280d8405853206; _ga=GA1.2.1709091329.1528465272; edition=mail.qq.com; CCSHOW=000001; webp=1; pac_uid=1_169633778; pt2gguin=o1062272335; mobileUV=1_1659f7f9b67_bda46; vfwebqq=39ea4d4aafc97b5e6bece56dcca76741561dd3e8b399398e6504ec21324a0b6d7b9ca5c34820def5; pgv_si=s6389896192; wimrefreshrun=0&; qm_flag=0; qm_domain=https://mail.qq.com; ssl_edition=sail.qq.com; _qpsvr_localtk=0.2388192119368282; foxacc=1062272335&1|392162042&0|169633778&0; username=1062272335&1062272335|392162042&392162042|169633778&169633778; o_cookie=169633778; midas_openid=169633778; midas_openkey=@TeFGrX83B; ue_uk=cb7a22ecc922a5b9db054f25dee9ddee; LW_pid=4809746f32829c643ea9911a680ad775; ue_ts=1538394413; ue_skey=72c79556a2b7cd24c182359e610bbc58; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2278d1ec97fb3448cf9de53c232845ab25%22%2C%22%24device_id%22%3A%2216639bdc9493c1-0b21ebb308aac7-8383268-2073600-16639bdc94c1d%22%2C%22props%22%3A%7B%22_latest_ADTAG%22%3A%22bilievent%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; luin=o1062272335; qm_ptlsk=1062272335&0001000081041fbec60aaac02655b1c36db97ecf78ae316e07405c3818f56a5c1b4d6e2972b1fa31b11b675c; pgv_info=ssid=s870926723; lskey=00010000784e7308e43cbd00e2c68bbbbf76ad08c46b1d9609e039d2975694439d129aaa23a1bd6875b958a8; ptui_loginuin=392162042; pt2gguin=o0392162042; uin=o0392162042; skey=@vejMTipOg; ptisp=cm; p_uin=o0392162042; pt4_token=EfcttW6iFQjDVVnk1*XmXAQk9AAiH*IncDamg5I5QnM_; p_skey=ZstgyC3sbSRUWByiC1h25MaxaqSEZW-dhtfAfpQhxhY_; qqmail_alias=gent.hu@qq.com; sid=392162042&d9255b06de2b9e6ebc7671b19a9c3e1c,qWnN0Z3lDM3NiU1JVV0J5aUMxaDI1TWF4YXFTRVpXLWRodGZBZnBRaHhoWV8.; qm_username=392162042; qm_ptsk=392162042&@vejMTipOg; qm_loginfrom=392162042&wpt; new_mail_num=392162042&0; qm_authimgs_id=2; qm_verifyimagesession=h0161de5079c018e1933fbb5a03291102a2b63cc2447d7bb5ce9b0c77a01f56728f7381c65b39806c38',
    'referer':'https://mail.qq.com/zh_CN/htmledition/ajax_proxy.html?mail.qq.com&v=140521',
    'content-type':'application/x-www-form-urlencoded',

}

data = {
    '8be637f309cccc8712d3f734795f9223':'d9255b06de2b9e6ebc7671b19a9c3e1c',
    'sid':'6hDSWbMsfyDDZHMo',
    'from_s':'cnew',
    'to':'%22鲜果橙%22<1062272335@qq.com>',
    'subject':'撒开发',
    'content__html':'<div>撒旦恢复较快拉升akjsdgfa 发</div><div><br></div>',
    'sendmailname':'gent.hu@qq.com',
    'savesendbox':'1',
    'actiontype':'send',
    'sendname':'凉夏故人难守',
    'acctid':'0',
    'separatedcopy':'false',
    'attachlist_log':'IDCKL%5DRE0O~10K0%5B)D%5DJA%24E.png%C2%A0(133.2K)%2C1%2C0%7CIDCKL%5DRE0O~10K0%5B)D%5DJA%24E.png%2Ccomplete%2CH5CPopupMail%2CRw%252BlpE46',
    'attach2BigList':'IDCKL%5DRE0O~10K0%5B)D%5DJA%24E.png,136445,cfbdc9644c6d0693bd3d6ce2b6ac16e675ff7cc2,59357d910dba10255de7a91a4dc235b5',
    'upfilelist':'Rw%2BlpE46mjPFzvPHCU1sNpkRO1Tz3ksu9zDZ%2BZhh8lHcqKDvqmwf6BDd%2B0WNXo%2BtyS9YTbkiWw6yR66%2B2LJyWrdz6uJdX7T3yhykakJnJzm2swbpzWMgiVZv%2FVClNWxE7UBsSsHGsdx9u6Oqs25PAW7rR0uc%2FAN2',
    's':'comm',
    'hitaddrbook':'0',
    'selfdefinestation':'-1',
    'domaincheck':'0',
    'cgitm':'1541644226660',
    'clitm':'1541644945120',
    'comtm':'1541645073827',
    'logattcnt':'0',
    'logattsize':'0',
    'cginame':'compose_send',
    'ef':'js',
    't':'compose_send.json',
    'resp_charset':'UTF8',
}
url = "https://mail.qq.com/cgi-bin/compose_send?sid=6hDSWbMsfyDDZHMo"
res = requests.post(url,headers=header,data=data)
print(res)

