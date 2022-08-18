import requests
import json
import os
from tqdm import tqdm


def download(url: str, fname: str,headers: dict): #进度条下载(转载自网络)
    # 用流stream的方式获取url的数据
    resp = requests.get(url, stream=True, headers=headers)
    # 拿到文件的长度，并把total初始化为0
    total = int(resp.headers.get('content-length', 0))
    # 打开当前目录的fname文件(名字你来传入)
    # 初始化tqdm，传入总数，文件名等数据，接着就是写入，更新等操作了
    with open(fname, 'wb') as file, tqdm(
        desc=fname,
        total=total,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in resp.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)


url = "https://ntp.msn.cn/resolver/api/resolve/v3/config/?expType=AppConfig&expInstance=default&apptype=edgeChromium&v=20220811.477&targetScope={%22audienceMode%22:%22adult%22,%22browser%22:{%22browserType%22:%22edgeChromium%22,%22version%22:%22104%22,%22ismobile%22:%22false%22},%22deviceFormFactor%22:%22desktop%22,%22domain%22:%22ntp.msn.cn%22,%22locale%22:{%22content%22:{%22language%22:%22zh%22,%22market%22:%22cn%22},%22display%22:{%22language%22:%22zh%22,%22market%22:%22cn%22}},%22os%22:%22windows%22,%22platform%22:%22web%22,%22pageType%22:%22dhp%22,%22pageExperiments%22:[%22prg-1s-mtsn%22,%22prg-1sbgbanner%22,%22prg-1sp-esprt_sl%22,%22prg-1sw-bnhdtbk%22,%22prg-1sw-bnrrksc3%22,%22prg-1sw-clbdg%22,%22prg-1sw-clctrl%22,%22prg-1sw-clrot%22,%22prg-1sw-ct-irni%22,%22prg-1sw-curtsd%22,%22prg-1sw-cwinphfl%22,%22prg-1sw-dmosg%22,%22prg-1sw-etrc%22,%22prg-1sw-fibdgih%22,%22prg-1sw-fibdgih-comp%22,%22prg-1sw-fibdgpm%22,%22prg-1sw-ficurtsd%22,%22prg-1sw-fidbref2%22,%22prg-1sw-fidbrefnc%22,%22prg-1sw-fidbrefnc-comp%22,%22prg-1sw-fiidxtsh%22,%22prg-1sw-fimdm%22,%22prg-1sw-hcnwc%22,%22prg-1sw-hident%22,%22prg-1sw-idxtsh%22,%22prg-1sw-mbnodp%22,%22prg-1sw-mmlb-c%22,%22prg-1sw-p1wtrclm%22,%22prg-1sw-pmosg%22,%22prg-1sw-prepwr%22,%22prg-1sw-sazhbt11%22,%22prg-1sw-sbn-mm%22,%22prg-1sw-sdb7c%22,%22prg-1sw-slot3zhcn%22,%22prg-1sw-sphdn%22,%22prg-1sw-sphstp%22,%22prg-1sw-tpsntrtc%22,%22prg-1sw-tpsntrtc-t%22,%22prg-1sw-trpf2%22,%22prg-1sw-wblis%22,%22prg-1sw-weart1%22,%22prg-1sw-weart3%22,%22prg-1sw-winpmh%22,%22prg-1sw-wxbdg%22,%22prg-1sw-wxdecap%22,%22prg-1sw-wxhfctrl%22,%22prg-1sw-wxrus%22,%22prg-2pb4-media%22,%22prg-adspeek%22,%22prg-apilogcon%22,%22prg-c-superdp%22,%22prg-ccmfa-t%22,%22prg-ctelrefactor%22,%22prg-ctr-pnpc%22,%22prg-da21rf%22,%22prg-disableworker%22,%22prg-ent-cmwrnt%22,%22prg-ent-cmwrt%22,%22prg-ent-linear5sd%22,%22prg-entcomp%22,%22prg-feed2feed-c5%22,%22prg-fi-skipauth%22,%22prg-fin-staginc%22,%22prg-g-monitorc%22,%22prg-highlightc%22,%22prg-hp-stopsw%22,%22prg-hp-t1%22,%22prg-hp-t1int3%22,%22prg-ias%22,%22prg-m-hurr%22,%22prg-p2-pinsamec%22,%22prg-prrndr-ttvr-c%22,%22prg-rfrshprrndr%22,%22prg-sc-car2nd%22,%22prg-sf-100sasdp%22,%22prg-sh-cdnslots%22,%22prg-sh-prctslt3%22,%22prg-shop-staging%22,%22prg-tds-fsmb1%22,%22prg-temp-xap%22,%22prg-tok21%22,%22prg-upsaip-r-t%22,%22prg-upsaip-w1-t%22,%22prg-useredirect-c%22,%22prg-views-stage%22,%22prg-wea-allxap%22,%22prg-wea-staging%22,%22prg-wea-subxap%22,%22prg-wea-tempv2%22,%22prg-winhp-rshdedupc%22,%22prg-wpo-cm%22,%22prg-wpo-dftifeac%22,%22prg-wpo-dftifeanc%22,%22prg-wpo-hprankc%22,%22prg-wpo-ifpv3%22,%22prg-wpo-layout1%22,%22prg-wpo-lypmly%22,%22prg-wpo-sdb7-5sd%22,%22prg-wtch-srchdel%22,%22prg-wx-3cad-u%22,%22prg-wx-anmpr%22,%22prg-wx-sbn-vm%22,%22prg-wxmapv2%22]}"

payload={}
headers = {
  'Referer': 'https://ntp.msn.cn/bundles/v1/edgeChromium/latest/web-worker.f30ac37d95d6f1961eb1.js',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47'
}

response = requests.request("GET", url, headers=headers, data=payload)

rsp_json=json.loads(response.text)

config_ip=rsp_json['configs']['BackgroundImageWC/default']['properties']['video']['data']

ip_len=len(config_ip)

i=0

ips=[]

while i<ip_len:
    now_json=config_ip[i]

    attribution=now_json['attribution']
    firstFrame=now_json['firstFrame']
    video=now_json['video']

    #将attribution中的/替换为-
    attribution=attribution.replace('/','-')

    now_nug=[]

    now_nug.append(attribution)
    now_nug.append(firstFrame)
    now_nug.append(video)
    
    ips.append(now_nug)
    
    i=i+1


ips_len=len(ips)

i=0

while i<ips_len:

  print(str(i+1)+'/'+str(ips_len))
  dirname=ips[i][0]

  #去除dirname后空格
  dirname=dirname.strip()

  #判断文件是否存在
  if os.path.exists(dirname+'.mp4'):
    dirname=dirname+'--'
  
  dirname=dirname+'.mp4'

  # #创建空白文件
  # blank_file=open(dirname+'/'+'','w')
  # blank_file.close()


  video_url=ips[i][2]['v2160']


  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47',
  }

  download(video_url,dirname,headers)
  

  i=i+1
