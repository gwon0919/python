import pack2.test21singer

def process():
    jungkuk = pack2.test21singer.Singer()
    print('타이블 송: ', jungkuk.title_song)
    jungkuk.sing()
    jungkuk.title_song = '3D'
    jungkuk.co = '하이브'
    print('소속사가 ' + jungkuk.co + "인 정국의 노래 " + jungkuk.title_song)
    
    print()
    iu = pack2.test21singer.Singer()
    print('타이블 송: ', iu.title_song)
    iu.sing()
    # print('소속사가 ' + iu.co + "인 정국의 노래 " + iu.title_song) # err co를 가지고 있지 않다.
    print(id(pack2.test21singer.Singer),id(iu))     # 1467253713088 1467252540752
    
    print()
    bp = pack2.test21singer.Singer
    print(id(pack2.test21singer.Singer),id(bp))     # 1467253713088 1467253713088
    # print(bp.sing())    # err
    print('타이블 송: ', bp.title_song)
    
if __name__ == '__main__':
    process()
    