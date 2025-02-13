import collections


def main():
	test_inputs_short: str = '''abcx
abcy
abcz'''
	test_inputs_long: str = '''abc

a
b
c

ab
ac

a
a
a
a

b'''

	real_inputs: str = '''necytxmlfhsu
uecosjvlhpmk

mnslbuziphawkxyg
whpmnesikaglzb

kaw
akw

qurg
hrqug
qrgu
gruq

sczomkv
zejkhvslmucbwdo
pxsianovzcmk
tcokmvsyz
ozskvimcr

tfzajkxngwsqrbleic
tijoqnerxsplwzgabkfc
ogkezbiwqtaxrscljfn
xsqauezwnjckbtgiryfdml

piz
zip

tlp
npl
lpt

idbnxuclqgw
sxfdnlatmbhcowigj
plzgbwdqkcinx
ydxinwgcblr

nbuxjwhsrlekfyzpq
kecyiurjfvqpbxhzsn
nkxfhpbsuyrqjezom
tinlhkbjsuydrqpzexf
pnzraelgquxhydsbjkf

obvmw
eoczsqun

nhdxqwk
dnzmlxwhkapq
whxqdnk

jnqdabgc
nacqdbgj

buyskiwz
uazbkwys

mbfxswpli
uswalhxz
xnq
tdcrjgoyekv

fancdpkmtuqy
zdmenqjpaxftuy

jkul
d
o

vhpoxgqsrtce
hgopxeqcdrstv
xcvrqoetpsgh

gekpzayfux
pyegazxukf
pkxaezhgyfu
fegypukaxz
zxpyefugka

yrpfd
ydsh

smjqcafnug
mnicqsu

tkxi
ixakt
tfncxkmi

kedibluzopjhagvtxf
afiklbvtjeoudhgpzx
lavbxpjzgedktoifuh
tbgpaxjqeoifvklhzud
zghidtfplxbvkoueja

gtvnqyrmf
hogpb

cnelsqwj
atyimdbvfxuozkg

lgybpaeztvhrxducjiqosmnwk
ivpaygxweszductombhljrqk

grli
lrig
sjglri
girl
rigl

qnwmxjbpecoyztufidhsg
ynqdiwhmusgtebjfzxcpo

luasrtmfkgywv
vgskmufywrat

ceyux
ycux

nurijfsovkbxdp
ayqclmthgzwe

xeqjdhsubiovwrg
gobdjqwvusehrx
weqjgvhosudrbx
ngdubsvqxejrhow

ywdfqpxekujbovr
yujfdoqbkxrepvw
owfkudjbvyrxqep
oqjvedypxukwbrf
xufwdpebyjrqokv

csujqndzmw
wznscqmjud
cqpwjzmunda
wjumnzcqd

dhsow
ohswd
wsnogh

cxfltiq
ixztfq
gtfqiux
jtqfxi
xiftzq

tr
rt
rt

pnuztcbegwiksd
cuewibkptdnm
nvqdpcjxekiwtauhofb
pbytreinuwdkc

y
y
hejq

rvmwqn
wvrmq

knxmwecsjlrft
hnmwzaqt
dmywnitg
tmwvquonh
bwqvtmnh

e
e
e

qjtywgdlek
nhifs
zvxinh

nzhroemi
dzruoegimh
emzoirh

hpfkraltbxg
gazxlmphrt

jyhugbxqz
zbnox
epdilfaw

vmr
vsfm
fmvsr
mnvckiaqy

zegpfuwtkrnoqdh
eorznfkgpduth
tkfpzhnredguo

zmqkwxipctney
ncwzeqpmkiytx
yptienwzxkcqm
yeqwcpxtkzmin

csbdyzl
ejoiwtzqabm
lzbkup
zbvprxf

wvpshngbmiftuzrxoyde
szobihvwpdtylqerc
phbdzoikvtajyesrw

ymuflnrxspqvkihbe
eymxrhlfnqksuivbp

rktwzd
wtdkzir
wkmaziqdrt
togpzwdkr

uwiazbylcpojst
lcyibajuptwzso

dtoqbcxhlyrpfwjnkasugvm
wunkfstmcjhqxliogrdvpy

wpnk
hdpkwuftjymv
cpkownz
kpwz
rqpwnk

tfplznqcju
puqlsnzfjtv
jqtfpzlun
ntqpczjflu

ozalwumpqv
ztheoalrwsciyk

wyiqbsr
bysqwri
yrbswiq
iqwrsyb
iwbrysq

elnroc
zmjlre
vhelbru
jyhruezflvk

ftyceboh
ofybh

jvlbdm
noakrg

dokjncqauebfpmszvtl
suebonpdjmflaqctkvz
dtjzmcblsvokpunaefq
tjzmeqkafluvpbconsd

qhrmvegsicnyupf
uifknverhsg
izlrvgefndjwasuh

syxvtjwfucilqogmnpk
jwkytpqofgimvcsnlxu
dwhglcxzoqnmjfkuiyvpst
ygwntxipqlmvkufcsoj

hdnqaburow
hqwadmbocsgue
bwoqtuadh
adqhbwuo

dzfohqe
ehfqzod
fdzhoqe
hdofzeq

sxmkrghyvlwzbc
yhkmwzxbgsvlc

qdumkytwlfsrja
drfqukzymilsjaw
jkwqumylsardf

pcvs
prvc
hmbpvc
svrpzc

epkjyc
jerpoy
gjpye
abxepuyj
ejyopc

ohe
gheo
eoh
ofehy

klhziowmjpyfubdsaqtgvrcn
aytbormdiksnqpzhcfvulgjw
lhmvkafdrscjgwnyiuptqobz

vcrqpdxljnmgusie
cgdwmipluoe

hqibentfmxyszljow
msozdjnibrfytxqhle
imlyxwehznjsbft
ysifkzbljphuxcmenvt

vjhdmkrpecniafgqlstxyzb
zxjrkebfvcwyqihlsmpgtd
xrfzidgthsbklmveypqcj
vjxytzgdlbefsirkcmpqh

dyxrwbngpijkt
xtwkdipaygjr
iklrmzwpjxgdtuye
pdgrxyjkitw
xtirhvwgdkjyp

zbjdt
jdat
shouqjtxcd

klarpuiv
iqaxjdps
cpnafbsi

xfpiourcst
ovfrlutxpb
trgqfxjuop
rsktucfpox
rtufoqpx

g
g
g

nfutbyvj
umvwyi

tjniwlydzqpsxbkcmugf
utpmixqdvzbfcwgljs

wetypdlnxm
cfavwyzji
mywgu
lyorqkbw
whdeyxp

qsbnwozepvhkmaxdrt
qmsopwtaznxfkehdyrv
xnvhwrzpemkqdtsoa
ituvkrhmdegazwsobnxpq

fxhwdio
hofdxi
hivztfonxdg
fhkoidx

ja
jca
ajzxt
ahjy
tajc

epan
pcn
udn

mfowepjdlnkags
oakwgflnp
pnlzgoawfk
kfgrowlnap

uw
aimwo
wzrhcjeq
wtf
w

x
tvx
x

tigsjdufrwomv
vjrstigqudohwkm
visrjodutwbmg

ety
exatp
hicfzqnb
uvejo

oqlgmk
kgvqxd
jzhgkpdqy
ikegfwatqub
nlogqkz

sl
q

rkpew
eqrwk
rakwe

r
r
r
rb

u
pua

pjmhtvd
drjnpuvib
djsplvy
dpvj

caugyqs
hxwyqst
sougylqre

krfshpzjmgav
uwrqidcotlbxhj

mzivctbfjgwq
lsomkypgajiq

ikoamrpc
kmociarp
brkmpiwycoa
itmckrodpa
kmipacro

htbpcdqx
ctpbxdq

gpduzcoiyxhleqrknbaw
nirehbulapcoxkzwdy
icuzyxopwhkalendrb
aokdrxhlcebpyiuwnz

yzlvptdaubjerkh
iyaoltghebpndkjszr
kqxjtldzpbcyawh
dbjtlavzmfhkyp

vg
sv

cdiaynroehqw
cqtaridyohewn
dciornehwayq
rwhnoaeqicdy
wqroadniechy

ivstkj
vgciqk
qkivg
vkgi

fp
pf
pf
fp
fp

xidyqnk
jbicfant
zabfhin

oqtys
stqyo
syqot
yostq
boqytws

gmnqxaictud
tucidaxqnmg
pgtquxidcnma
iagdtcfmquxn

yfhxgw
rgn
nsog

wndrqktbmfa
fwqadkrtbnm
mabfntkqword
qbwntakrmdf

elanoudxhbzfrtvci
ztalefiodxrubvckhn
ulvabcnthpdzxoifer

omdrvepliwafhjynbscu
mblrxjsfahocwnvyu
umcjlsowatvnfybhr
uahvcnbwlmsjzfoyr

n
tn
n

grk
rgk
krg
gkr
rgkhv

stmlnek
pgsltne

alcztk
bctvk
khcgtb

nsgevcthrpykbwfoizda
khneritgszvbfycaowdp
ivybwzeaogdsrnfctphk

e
e
e

cxkzdbgiqyawnm
afyvkbeirtjowmcl

omb
p

lnhwcoiyafs
soihnyxqfc
ohncjyifsq

o
o
om
oxqnsd
oaj

okucjhiq
xpgwcnqjiomyfluk
irhoukdsbjqc

uolgz
nglczu
zlngu
zmhlgvjru

mhdapszf
anmfwdvkc
dpamf

aqleivtyzsogjc
syvbgxqpdflezoac
ilvzqsjaegokyc

zxndhja
haxzd
xhazd

mo
om
mo
mo

vfxep
xfepv
xevpf
vexfp
pevfx

mrtkehqnjxizgp
kbunrqytcmes

nz
ipneu

bznteo
tbzeoqwp
olftzbpk
grzvityxudohjma

xg
rg

rdu
urvd
rud
rzud

somnbutz
tuosnmb
ntomsbu

fxsvrzqntbueoyp
eqzsvxyunbroptf
zvypnrxfsqebuot
zrosbxeqpunvfty
zprtfvsnbquexoy

qwzknfvl
funqlwkj
nqkwflz
fgxlkwzqn

rzqihd
rbz
zr
uzer
rbz

utrq
osa
pm

zgdci
brhu

bxvymlzqkpha
vmhlakpyxq
ypxvqkmhal
xhvpymaqkl
aplqvkhmyx

sjntbvyogeplwzu
rbjqiefhapxodwk

frlsoptqwbc
ljrzxqntfom

zlhvjamtpfonk
lcokjzdhmfvnp
siohzynkmbjvlrf

osvgwnticelpzm
jvswetpozlcg

npmgrvysfj
nvqxrjfsgmp
vofthkcjsblpmudizwr

oiev
lmeiov
oiezyv
uievodkac

iforupqjzykdtc
yqfhdcxvtopz
tzqpfdycgo
ceyqfozvtpd
dpxqflohzyatc

srz
zsrt
strz
xzs
sz

dgo
odg
ogd
dog
qogd

gotwqhick
okhqtgicw
gsouwitkjcqh
hctgioqwk
tkghocwiq

mfnziwvxtlpubqryojasd
mzojuctvnbriypwflskqda
pmuavqjifnlhrtbyzwods

ozj
joz
zjo
jzo

jzwbhrscm
rzmhjctb
zbrhcmj

sucgimtr
myliojcrsg
ipcsegxrmv

znhvi
hvin
wosganie

wptoqxmafhg
awqfhgcozmtx

azbqlviyrwjc
ybxcrawv

qa
vcuwbfgsl
hkraj

biglkjtpoqs
zvxcfumeywrhand

ske
s
sp
hs

n
yn
n
n
n

lrvsmxzkgi
zgrmkdsxl
lzgmpakrs
wgqtrkmsfz
nirmkugzds

crewvjdqsplkibthxz
wxjmtpirhalqsckbdz

iecxrbplho
xhrpibovlce
brxlgchopei
cbhioprexln
lchxirebop

f
f
q

nxqkrhdi
pkhdrquxn
ynqdlxkh
xghkndq

wvknrdjx
vknxrwdm
kfvicpwndb

rcqwlutsanpdz
yoxenmkvbjf

izqsa
sqzai
zqsai
osiazq
izqsa

ysokhbpzcqanmdifw
kdlowyusmqhbjxci
hibkmzocndqswy

yjwd
bgas
yj
k

tzruq
uorz
zckrvux

rjn
nrj
nrj
jrn
njr

ecu
pzus
wokxu
ruw
twu

fcnajztduyripl
chmpkvlynsxrauobji

cwfgtjre
ejwufr
frwje
newvryfjbhq
iwjextrf

ltqapiwhzfeoncxdg
hndclgoxeiwtpqfz
cwnpdogxteilfqhz

uerinxhsygpbzcdvfmo
lxeihducozgqnrymb
edmugnyxifoczrbha
ucezhnrsdybmiotgx

xuvfhjeyi
ztcgaqs

yxrospmijwvcdb
yjpbrcosuv

viuhdrgnlak
lniaruvkdgh
khrgdnuiavl

qfzxb
gfqx

k
nzyo
kcj

bmi
bmi
imb
imb
ubmi

pl
pl
pl
lp

x
v
x

hgwtocs
gdctwhoi
iczwfgtoxh

wrcjdaqm
wsrlog
jrnqmcw

ouhmpnyskxcqafidbjvgt
dnimvbpytfsoagucjx
jpctsmuxiaovyqnfdbg
gzbvfwmojuyxsrdtpcna
yxfolphstnabcmuvjgd

nlrdxe
ceksxuhazmjo
ywxedfgqtpr

ckuwoghtaxrledvzms
mtksozduwvrehxclag
xwvcusrmlazoetkdgh
regwvshxkdzuctomal

khsnymbpjz
hzknspmbj

zqc
kpgsjrqxiyd
wtbuhoq
qwc
eq

ljewzy
qlwjy
wzljy
lwyj
ljwy

vpodmhni
bvryknfg
jcutez

wedfcoh
wigfnjkaoz
exwoqfm
pfuohsw

adyzjwgqxv
qjwvxzagyd

cazpofbyd
nodypfbcam

ukvrcslyqzamhteowdfibx
ktrgqpmnawdycsivhzlbefx
fxdabuylcveksjwrmzqhtio

xyb
xesy
xdqcy
yex
xy

hotd
odhzqt
othd
htod

hvkc
lzei
asw
a
d

q
q
q
q
q

a
a
a

suqbvedipgzcjykfmaxno
jzfudeoxikpbvmgynsha
iswkepmodzvfgxnylujba

xpqjonkzlrfhtyw
fjqksrlozypwnmxth
pkrohjnxlfzyqtw

pxuhsc
hcxsnu
hxcse
cxhws
hcrsex

iglfosahy
hizgfalodbs
lgfoiahs
gsfalhyio

xrgzwbdnohfeijacsmltqp
djpgqrimtwcafsxnlebzoh

qlrn
qrn
qrn
qrn

xhbiakuzcjm
nfpykow
klfs

lcubkpfhnomgwyarjetqd
wtcrgofdnlpbaykquevhj

bdqusvnyetklmwizcopxjr
drbxlptyeqcvjwiusmzokn
oqcjzvuwslkpedbxmrntyi
jvlnxtdpkusyczbeomqirw
wltriuqnpzcxbysvojdmek

tyeorbzjdxpqn
oprlqdnwbzyx
brnydoqzxp

bupvcrylqazehoknjtf
aqfroczbylpvuejk
ubqvelyfrzoxcpagkj

awbzx
axuw
ywildxoa
uwxnba

mjfvro
wmrfjov
ojvmursf

zwxouqy
ouzyw

dsxf
sfdti
syrfd

zmibfjk
kimbz

nebq
beqn
eqnb
bqnpe

avtnckldjpeys
scjtklpdneyav
kytncdpsvaelj
tkpacjysdnvle
dycsvtjplenak

mkyojv
biwro
botsx

owxyu
wyuxo
yxwuo

qgjplcvo
vgjqocpl
ojvlcpgq

xczvkuohisrfqbagp
prbeilfzognvqws
voitfqpgjmrzsb
rvlfdoqigsbpz
ipqogbrzfmsv

j
s
st
t
pzde

kuwbthejxcfrzgosmn
xwcukhrtsgzf
tkfcguxwshrz
hxukfzgdwsrqict
zwucgkfqhvxtrs

wvthikzpgrjaf
swdnemkqobcyx

lewoquaprbkxyj
xpelwoaksubcrhqd
gbrxmluktiwnaopqe
epxuyczokafblwjrq

mcyepsvwxr
bhe
nqeztgd
uaehil

tq
be
e

duqgair
dfrwuiqga
qaugidr

hmofng
hgnomf
mofghn
gmotfhn

ewhblqnsmjict
whmbxvpjs
ufzyaogdkr

jqpynazsfvklied
sjilykvqza
izsvjlqayk
qiksvzlajy

vbps
vbstp
evnigorks
vbst
jslv

qgdzylwkbfou
jbwygulq
qwhxrugpeb
giqdfvbwu

jubto
aeuvgdpx
unl
yorqui
uqm

ic
kci
a
i
gyfe

tjxp
xtj
xjt

ldspeai
eapidul
peiadl
ipelad

oymwvfriux
moxuywvfir
rmvxwoujifyb
fpvwdumgyroxzi

mcplvnkgjfz
idszwngkfcvpl
njzfklgcpvo
fcvokpnlzg

xdnsilr
irnlsx

bndvimefz
atopdu
xhswykcqgrjl

kvlorsye

vsdoq
dvos
vodjs

bxczyfeajkmloi
jcimfkaloybxze
ceijaokfzyxmlb
feymoacbjxikzl
kcxmiebzyaoljf

lo
ol

etxkfsgjlqoy
fgshieyj
esywfgj
gwrjsyepf

jtzlgakxins
gqlznxfabskijp
ikaxgsnzljh
lgaizhkjxns
hgaznkjxtlis

urhjiycw
rhycisw
zrwihkcy

xc
cvx
cx
cxgl

audxneqrchg
efkmodwqplrzsiyb

g
x
x

ziuplaqo
czqtihuw
zufiq
nqzubpixak

cibdku
dbckiu
kdciub

eshpjzgtwrka
tgwpafmsjkrehz
sekbwtnxjhpzrag

dj
dm
dj

trqkdpwoxjfyg
csu
ancv
lui
ebhmaz

ljbvexnhgwfs
hfjbxneyilwgu
znejqblcdhfgwx

b
b
b
b
b

idxrcyjegnu
lrhvskceg
rozwmgafbce

gzasrwjlukomvdxhbpc
cahmgzurlvpwxbdjs
uxjzsbgmdlchvprwa
hramvdjxslubpzgcw

gw
wge

fpgdzy
wpfdbz
zpfahde
lfdpszcorx
zfdgbqpha

gfuclekqavitdxr
euwkvdirqtcxa
riuxvaqkcdte

eqaphotimfdrukcgwbyx
dxtowkygamibqcrfeuhp
oiutpbavhdyqergfcmxws
ahcteowdfrkugpibqjymx

pmixjle
uxljemp
lkpsej

mzqcwxuo
xoucwzmq
xcumzqsow
zcuqxmwo

wt
wt

tyrajn
hdtgroynjae
jrnyat

uqifnlv
iqnevl
vqienl
navciql

qjxpshtuzbmfnvogcalw
skvzqthufxcjeagrmdiwlyb

lvaftw
vkfaywtl
lfvawtq

wpusqdfkybg
mghtdxkpsur
dsgxhumpk
jmdkpzrsixug

qcbalvykixze
fmrhcsadlnio
cpautjihl
clgainupm
ilcaft

pklutwg
gdpkrl
lrpkg

wbup
bygfurw
ubw

xsoqjceyhunvat
jshgokqucxvlyn

pyk
pyk

l
s

m
m
hm

msultwhivz
vzitlhwmus
htsmluvzwi
ihszwmvult
iwthzsumvl

wlohkegqpb
jzguytqrncd
igqvesfa

h
hgy

xb
x
x
x
x

ij
ji
hqdl

k
k
fkswyr
zk

frvpln
vfcnlpr
vfnrlp
rnpvfl

ouy
yu
uy
yu
yug

rhekb
etnxfymlgdwovqzu
csbheji
beca

vj
nfpv
v
v

ruvqehmija
mdhjqrayuie
ksqrfgjeihpmlu

kbsnlqxfrizjauthodp
uxdjbqniholafzrskt
eaokjungrdfshlbtzqix
wjlsbciontzkdqfxhuar
qjlosubzkfitnahrdx

sbzcefm
zsmb
szmb
mszb
smzb

xzisbpmc
prihnxstmfzb
klpbmszijxw
vmepbiszxaq
zipmjbxvs

qjgbnvamedwi
qajzdoksweb

gtkfqwlzashcen
geiqzsnhkfwctv
esnmhfzgqutpwyk
igselxqndbfwthkz

obpdyswkvthxgreanmjluq
lahobnkyxtdrqgseuvcj

pw
wpe
ylp
ep

owrlgniy
iljkvwxyhopufzsqdc

wxzgdpt
saxprdtkf
qdxjotpgbwl
xtdhjpl
utdjphxci

gwkrjnizdxbvc
hfnpygvaw
ygvutnaw

pecfzghqxturdijsblmk
klsxuqpfhdbctrjgemzi
dtuzljfxhmbgciqkeprs

iznfycwdrh
zwnrchiydf

xutwndim
osidj

knwyjicb
jc
zjgc
cju

jwtep
hjer
egj

khwsitfnxyep
iwkpnxeh
wephiklnx
hcigwzkapxremn
nwehmapkxib

vuqbmineogja
dlrpainmvugj
ravsmgijfcuhynt
awvpiunjmg

zdcalubhniv
nclhvibudaz
vhcdbuznila

bzcaorhqflg
jteyvpwsuxdnik

icr
rvic
cri
ric
ric

bqikw
ibwqk

ipxdcvmfulwejyg
nqcelgydaskrxhi

pkovrgdljyh
vq
ixwv
vsxaczn

ix
xi
ix

hkxl
hklx
uxlkcsvgeh
khlyjx
blkxh

lhgcae
yczfas
conasulj
xgbflezcuayo
mvcidtapr

iwaepxckbvjnzmqft
pwiancxtmufqsvzj
cpanmiftxjwqzv
mhftvjnxzpowciqa

ir
rd
ir

xt
xt
tx
xtk
tx

rdatjzibwsu
mdsuarwtizjb

rselwj
wetbjy
pzxqjowe
njtgbvwmei

qgcazvn
gqsvcnz
vczgqn

vmufbi
efuinvmq
uicgmkvr
vnmilu
ubvwmix

lseymvjuidhkoptazcxrw
wnbsukhpjoedczrlavgtmf
scmrptkhdeazojwvquly

qopb
evwqyl

syuzojncfrliwap
wnocfplirjzsa
izwrhvftqbdgpcjoasln
ljiznraspxofwc
rzcpanjowslif

lpebrhxtam
iyuvknwfso

by
yb

qshtypdlocawvgjb
xvyrnwfqezshjoka

xhw
nwhx
hwx
whsex

xelcghsquwivjydnrzkbfpa
elviwcpnsokhjqubgadxyzfr
dcfqxvneymsutzkrlpgbjiwah

ghckb
bgh

rdojuvqncia
nracovyiw
cvryoina
echariovn

rjmdqahvbplcusigfx
cluaqvsfhmrjbpgidx
gvchlipxjsaufrbqdm
pjdsqmvlcaubfirhxg

tngbc
btcng
nbgct
bcgnt

aonpsbqkhwclrmdyuz
mcgubhqdokarzlspnwy
olhybcuasmrdzqwnkp
lkshamocyrdznwuqbp
wlunozascybqprmhkd

skilqth
qhlts
uslvqt
fqstl
ftshql

fbtxdirelcsqzu
icsyjfltxdeurq
rueptfdcqylixs
usqtxfdrclei
lwqdvtxeirsfucna

xphvrbl
bthixl
wqjmohcfxyazlsb
vhluxb

kbnogjrhe
krbngeohj
hnekjbrog
rkbeognjh
kjrohebng

z
yzn

wslprjfqa
regwpyqdksaci

glmkujvbatqwc
mtubqgclavrjwk
wuqmjlgcabvtk
galuqbvctmkjw
ckblwqujgvmat

kgrmfstlejw
bdithoauynzpv

wvyzhfdistmqkrugx
nzlspqermfwjahui
ufqsipwozmhr

fdsavukrbpcm
zrasokjlvudmpbf
eqvbkfrswpdtumag
dmhkfplvbarnus

tdorlvb
pvdhiko
omgsjwuavycxe
pziqbovhnf

f
a
u
u
u

efg
egf
feg
fge

wsf
lmcd
f
v
ve

mibscvfqnhoxty
rxphcsiqbofvnw
uexoibzljkqagcnf

sbmhgyqvkuoljzwrfnxietca
ocjebltaqwursipnfkmx

xeh
unxmh

du
ud
ud
du

tvzo
vo
ovft
vto
povdq

r
s
lhibgo
qny
nwk

cwxfhrgjdsyamtkv
fshogpwdinlrcjexmt
yxvdtzfrsgmcjqwbh

zil
liz
liz

iygvphrujkwaxl
ikjyutlxawvgrph
hvuliyrdjakwpxg
rjthkylwipxgvuad
wivxkhlausgpjyr

vrxkaqzgmsyon
vorxcumswqznyag

vlhuwzmdq
bsoryk
yeka

eiqwuz
uvwznpqikr
wluozi
xjbyizufsagdtwm
wzhuic

wydkjlfzpeqtgxorhmnuci
tuczlfqrdnyxihgjopkwem
tdpylmxcibgkfhjzwerasnou
zelpcrdoygnxjvfmktuhwi
gwmehyiojukcnfxrptzdl

vcuizfrlhqa
rvizlucafhqj
cviluqfhraz

wmgu
ve
sgly
fmwx

ke
ek

elhq
hqel
qehl
ehql

hzdfnwxtjysrio
mykgu
vy
kpmaqy
gbeykc

pfkj
hfkpj
kpfj
pfjk
kpfjd

z
t
z
t
oxy

ux
auhzoj
xu
u

gcaldiph
lhnfapi

slg
slg
lgs
lgs
sgl

h
h
h

qodwxpmskvjbtycuzghfe
pesjgxqzbtdcoyhwmu
ylthszqpuwebodxmgcj
chqjetzxgdyopbwmuls

fkgtmuyoivdehpjcxsba
agycjmdsfirvkuowtpbhex

ocaw
msclaw
cwm
jdwceh

ekfyibdncovguazhjr
jkhgzbaoyidunvfr
vyaihouznrkgjbfd
xghojvrbdnzfuyaki

jpgqlhvyi
pqihag
hqpig
gupqhi
ghqip

glatmnqesbiwzkhup
jykuqrbswnmvocx

ykqwxpjgcshtdbau
dfxqwpgbjcstkyua
xsgatjcbkwdyqup
usqykjpbgxdcwat

cmevolpwiq
moagpqevltjiw
fmwziqbpuvleko
djvspewmohiql

mdux
xmkud
xmdu

vptyrkjxhcmounzgaw
wkmranuoxcjhslzytdigq
mjcazrxkguwfhbtnoy

e
z
mr
e

vrqek
kevrq

wb
vcti
hyar

e
e

chqesv
vesqch
eqhvcs

uae
xzecw
eyl

bkgftdhvn
nbfkgdtvhj
nhftvgpkdb

fwxkbouizcyjg
kwfqjgcyxzou
gfkdoytrjpczuwx
gyjvzcxfuowk
mxcjzsnuaefowyhlkg

itwzbp
yhnafe

dtnzjkibprafm
fnarjbkiptzdm
njrtpifmkbdaze
qkndmpaufbrjtiwzx

eknujdxzmytriao
erkujinftzq
eskumatjicdnryz

lvzhmxewbgnkuorypfai
ibnwkrfogvhaezxumpyl
hvbarmnowygqizujxplkef
hegopvnwrfybamkluxiz

rdylnbotpv
raugkqfelbnwy

vk
gnuypkw
kvj
kjh

uprylxio
luixrp
ruxplki

u
gmu

ugbqne
ykvzwr
i

vcqosrjbuxtl
hovtxlrbcqsu
bequwsltvxco
vxarnqstcbuzlo
cvuxqpobtsjl

ctviybroekm
cyrtbevimok
tvokrbciyme
ekctbyvmoir
tymcviebokr

sdmkxgfhjlpyba
puaowzsdqthkle
zwredloshkpca

fjxo
joxf
fjxo
jfxo
fxoj

mrqtv
rvqtwfm
rqmnvt
wmrvtq
qrftvm

qwtjlfobuydncgzheisxr
qwxdlcuhjbnemaorpgfyzist

zenwdhikljm
nejlmiwzkdh
jndelhwzkbmi
zelhwnijkdm

jofdgmy
ojqdpbfg
gduojf

awsgplcxqu
mulxgapdcjqk
acqjhfldpxgu
xluqipvbngact

scdzqhyfplnx
nxkygdjuzbcqsmvt
zlxsqwnpdcay
czsxnrqyold

qzvlitw
njapdb
xkbcf
uaogk

ok
e
iu

qshidleorzbgjnvpuckyawt
piojqrtzbnaukgwvchlesd
gduvqkcnhioepstrljwbza
qhripvstdjznlbgwuocake
jevrwsibcqlnutgkohdapz

upcealv
gmpeyv
pve
lpkuevz

pbtldk
bpqhdk
cibzd

lk
hs
kx
l

fkuirx
sy
zgqw
qmv
qv

gdrtbwcjlhmqk
akdlqzjhctgm
dchqomkjylaftg

vwal
ficwjzusyom
lw

z
jyxo
n

x
x
x
twxs
ox

jzhaxuflebqwsipgctr
mgawzjihxrpcuesfbqtl
rljqhausvigxtofwczpbe
ifwjsdcbztphlxqrkeuag
hizafygceblrquxwtnsjp

ioamx
xiaomg
oxami
axoim
amibxo

dxgwsbmlnyqruckezp
xlurgtqncpwyfbisdkejm

vflkdqcxbzuwmengty
swdbuexzlqvgmf

ehsmravbk
ehmvrkadb

qh
hq
thqx
qh

uhi
aui
ui
iu
iu

wlrnmb
yblnpr
bztijfenkola

y
fgzyvds
yoj
iyp

ohbiqfxzp
fpqihobx
xhoeiqbfp

cgfi
figc
fgci
cflgi
cihgfnv

vytbdxlzuwarjphnogic
gexwbnqfizmhtdjyrcolas

hdeowrivjq
uzihgmjwxrve
wijeorhlqdsuv
ryeitfhvjw
ejhawvnuir

siaxlobjmkvcwhernytfugd
rmtfsolejkdxihgvbnwcyua
oxglvkinrcebswamujfhtdy
gwsatohiknljburmdycevxf
cwuzdbgnethrvysmxolfkaji

m
gm
bhslre

xonqwkzcfbmtidpyvlsheu
pylzcoxmvqkehdsnftubjwi
nworbkczxutyedsvqfhimpl

uatwvlgknhrfoqi
nwhbtokfiq
seniqpdzfhxmcotyw
utoiqafwhn
nqtoifwjh

oxiflw
hflwxo
loxwbf

mbt
tbm

ocjflngrdakuypqiwxstzhmvbe
ykdaueiczwglbtrhjqnmsfxovp

wtlzyrcomasqnjude
owhqdnmkzrpjlsxc
loqdmszxgvrjwcn

on
x
x

lbeyqfxkwm
jmqnfxbgwde
oezbufqrtm

d
y
y
ta

z
p

fyx
xfiy
fxyw
xdfcy
fyx

csjxkozmnl
slomjxkzc

hqwadymfsbtlxv
kdvbatlfshwqmxy
lyahsxmqfwdtbvz
wxmlyahfdstvqb
tvqdsxfynlhamwb

ojmvurikheablq
ukidqhvaljobe

imc
tdkjmp
mi

eq
eq

thgulyifqobdwvecmarsjnp
ndlygcmjahefquiswbrptvo

sjnptmdrlc
uvebzmlodrncp
lmypxkcfrnsd
cnmhdlqxiarwpg

nzvqlh
hlzvn
lzhnv

juq
ju
uj

tjqiucmynvozxh
kmdvwafrxtq
exgqmtv
ftsqxmv
qklbtmxva

r
r
pj

pkoy
ypok
kypo
okyp

f
fl
f
f
f

snvqdyx
tdsxvnqy
deqynxsv
dnsxqvy

lzhopfimuretwvd
jqgbvakrds

zfbocen
mzbnacu

ezyxtajrv
wzjuxreatv

mrsejiyuvfz
jkuctbxpoiw

nyvefxqicbah
brgeyltxvik
kyuvilexbs
ztvixyepb
pxiygvbe

nadq
nyt

prmt
ysjqkmocznhda
gmlibeu
bxmvf

rm
wm
m
m

wyfjzdlvcgreb
emlxnkpfjav
elijupnfvh

pybv
bpvy
yrbvp

zrjkxshpufec
vindgwtqbl

ngmtqzfcpudhw
tphzgcwnqdfmu
ftzgphnmcudqw
quzpmctfngdwh
gqpdhufwcmtzn

szfcnb
fczns
fnzcbsg
sznvafck

arcezgin
egcirazn
gezcrian
icgnraez

hgqucfnt
gqnukt
qgncut
tuqnhg
unfgqit

w
setbdgv

lck
lxk
kcl
kl

emaqhxorctykufp
tigjzqhv

mlvow
jqwo
ghksnruxipoac

hxnpeqt
htzen
nhte
pchtne

ehovjgfzaql
qhazvjlgeof
kfgljqhavzoe
jvlzfhgoeqa
veolzqfjgah

bdlitrzuwh
epfmuhgvstibr'''

	answers_test_cleaned: list = test_inputs_long.split("\n\n")
	answers_real_cleaned: list = real_inputs.split("\n\n")

	print(f"any yes answers: {count_yes_answers_from_anyone(answers_real_cleaned)}")
	print(f"everyone agreees answers: {count_yes_if_all_agree(answers_real_cleaned)}")


def count_yes_answers_from_anyone(cleaned_answers: list):
	total_yes_answers: int = 0

	for answer in cleaned_answers:
		yes_answers_list: list = []
		parts_of_answer: list = answer.split("\n")

		for part in parts_of_answer:
			for character in part:
				if character not in yes_answers_list:
					yes_answers_list.append(character)

		total_yes_answers += len(yes_answers_list)

	return total_yes_answers


def count_yes_if_all_agree(cleaned_answers: list):
	total_yes_answers: int = 0

	for answer in cleaned_answers:

		person_answers_list: list = []
		answers_dict: dict = {}

		answer_per_person = answer.split("\n")
		person_answers_list.append(answer_per_person)

		for index, person in enumerate(person_answers_list):
			for answer in person_answers_list[index]:
				for character in answer:
					if character in answers_dict:
						answers_dict[character] += 1
					else:
						answers_dict[character] = 1

		for answer_letter in answers_dict:
			if answers_dict[answer_letter] == len(answer_per_person):
				total_yes_answers += 1

	return total_yes_answers


if __name__ == '__main__':
	main()
