# coding: shift_jis
from PIL import Image, ImageDraw, ImageFont
import os

# x × y ピクセルのr値の合計を求める関数
def r_sum_calc(im,x_f,y_f):
    r_sum_f = 0
    for i in range(x_f):
            for j in range(y_f):
                r,g,b=im.getpixel((i,j))
                r_sum_f = r_sum_f+r
    return r_sum_f

# 画像を置き換える文字を探す関数
def choose_letter(r_ave_norm_list_f,test_r_f):
    near_check = 256
    near_index_f = 0
    for i in r_ave_norm_list:
        diff = abs(test_r_f-i)
        if diff<near_check:
            near_check = diff
            near_index_f = r_ave_norm_list_f.index(i)
    return near_index_f

x = 5
y = 5
r_ave_list = []
r_ave_norm_list = []
font = ImageFont.truetype(r'C:\Windows\Fonts\msmincho.ttc',x)  #フォントの設定(等幅のMS明朝を選ぶ)
# 描画に使う文字列　スペースと小学校1年生の漢字
kanjis="　　、・，。￥＾＃＄％＆（）一／＼？０１２３４５６７８９ＡＢＣＤＥＦＧＨＩＪあいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわあ一右雨円王音下火花経験"
# kanjis0='''　、・，。￥＾”＃＄％＆（）一／＼？０１２３４５６７８９ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚあいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわあ一右雨円王音下火花貝学気九休玉金空月犬見五口校左三山子四糸字耳七車手十出女小上森人水正生青夕石赤千川先早草足村大男竹中虫町天田土二日入年白八百文木本名目立力林六引羽雲園遠何科夏家歌画回会海絵外角楽活間丸岩顔汽記帰弓牛魚京強教近兄形計元言原戸古午後語工公広交光考行高黄合谷国黒今才細作算止市矢姉思紙寺自時室社弱首秋週春書少場色食心新親図数西声星晴切雪船線前組走多太体台地池知茶昼長鳥朝直通弟店点電刀冬当東答頭同道読内南肉馬売買麦半番父風分聞米歩母方北毎妹万明鳴毛門夜野友用曜来里理話悪安暗医委意育員院飲運泳駅央横屋温化荷界開階寒感漢館岸起期客究急級宮球去橋業曲局銀区苦具君係軽血決研県庫湖向幸港号根祭皿仕死使始指歯詩次事持式実写者主守取酒受州拾終習集住重宿所暑助昭消商章勝乗植申身神真深進世整昔全相送想息速族他打対待代第題炭短談着注柱丁帳調追定庭笛鉄転都度投豆島湯登等動童農波配倍箱畑発反坂板皮悲美鼻筆氷表秒病品負部服福物平返勉放味命面問役薬由油有遊予羊洋葉陽様落流旅両緑礼列練路和愛案以衣位印英栄塩億加果貨課芽改械害街各覚完官管関観願希季旗器機議求泣給挙漁共協鏡競極訓軍郡径景芸欠結建健験固功好候康差菜最材昨札刷察参産散残氏司試児治辞失借種周祝順初松笑唱焼照臣信成省清静席積折節説浅戦選然争倉巣束側続卒孫帯隊達単置仲兆低底的典伝徒努灯働特熱念敗梅博飯飛必票標不夫付府副兵別辺変便包法望牧末満未民無約勇要養浴利陸良料量輪類令冷例連老労録賀群徳富城茨媛岡潟岐熊香佐埼崎滋鹿縄井沖栃奈梨阪阜囲紀喜救型航告殺士史象賞貯停堂得毒費粉脈歴圧移因永営衛易益液演応往桜可仮価河過解格確額刊幹慣眼基寄規技義逆久旧居許境均禁句経潔件険検限現減故個護効厚耕鉱構興講混査再災妻採際在財罪雑酸賛支志枝師資飼示似識質舎謝授修述術準序招証条状常情織職制性政勢精製税責績接設絶祖素総造像増則測属率損貸態団断築張提程適統銅導独任燃能破犯判版比肥非備評貧布婦武復複仏編弁保墓報豊防貿暴務夢迷綿輸余容略留領快'''

# 文字列kanjisのそれぞれの文字の白ピクセル値を求める
counter = 0
for kanji,counter in zip(kanjis,range(len(kanjis))):
    im = Image.new('RGB',(x,y),(0,0,0))  # 下地となるイメージオブジェクトの生成
    draw = ImageDraw.Draw(im)  # drawオブジェクトを生成
    draw.multiline_text((0,0),kanjis[counter], fill=(255,255,255), font=font)  # 1行分の文字列を画像に描画
    r_ave = 0
    r_sum = r_sum_calc(im,x,y)
    for i in range(x):
        for j in range(y):
            r,g,b=im.getpixel((i,j))
            r_sum = r_sum+r
    r_ave = r_sum/(x*y)
    r_ave_list.append(r_ave)
offset = min(r_ave_list)
r_range =max(r_ave_list)-offset
mag = 255/r_range

# 0?255に規格化する
for i in r_ave_list:
    i = (i-offset)*mag
    r_ave_norm_list.append(int(i))

im_draw = Image.open('test.png')  # アスキーアートに変換する画像の読み出し
im_draw_gray = im_draw.convert('L')  # グレースケール画像に変換
x_im_draw_gray,y_im_draw_gray = im_draw_gray.size  # グレースケール画像サイズ取得

# 画像を1/x,1/yに縮小
x_resize = x_im_draw_gray//x
y_resize = y_im_draw_gray//y
im_draw_gray_resize = im_draw_gray.resize((x_resize,y_resize))

# 縮小画像の各ピクセルの輝度を取得し割り当てる文字を探して表示
with open("pictxts.txt","w",newline="",encoding="shift_jis",) as filetxt:
    for y_check in range(y_resize):
        text_row =''
        for x_check in range(x_resize):
            brightness=255-im_draw_gray_resize.getpixel((x_check,y_check))
            near_index = choose_letter(r_ave_norm_list,brightness)
            text_row =text_row+kanjis[near_index]
        text_row = text_row+str("\n")
        filetxt.write(text_row)
filetxt.close()
os.system("pictxts.txt")