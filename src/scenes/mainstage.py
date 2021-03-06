# -*- cofing: utf-8 -*-
'''
Stage: main
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def a_cat(w: World):
    yuji = w.get('yuji')
    ally = w.get('ally')
    return w.scene("猫",
            yuji.do("真っ白なソファの上に、雉色をした猫が気怠そうに前足に顎を載せ、目を伏せている"),
            yuji.do("ちゃんとそこに居ることを確認してから僕は前に向き直り、モニタに映った蟻の行列のような英数字の並びに溜息をつく。キーボードを叩く度に彼女が目覚めないだろうかと不安になるが、特にこちらを気にする気配はない", "&"),
            yuji.do("彼女は人間に関心など示さない、ということだろうか",
                "それならそれで構わない。ただ目の届く範囲で穏やかに居てくれるだけで良い",
                "空調の温度を一度下げ、一息入れようと席を立つ"),
            yuji.do("ソファの背には斜めに引っかき傷が付いていて、それはおそらくこれからも少しずつ増えていくのだろうが、彼女のことを考えると新しく買い換えるのもどうなのだろうかとなかなか踏ん切りが付かない。やはり慣れたものの方が居心地良く思ってくれるような気がするのだ",
                "キッチンの小さな方の冷蔵庫には炭酸水のボトルの脇にビールのミニ缶がずらりと並んでいる。僕はそれを一つ手にし、封を切る。コップは使わない。いつもそのままだ。何口かに分けて流し入れると、空になったそれをゴミ箱に投げ入れた",
                "缶同士が乾いた音を響かせたのが彼女の気に障ったようだ"),
            yuji.talk("アリィ？"),
            yuji.hear("そう呼びかけると小さな返事がした。実によく似ている。猫の声そのものだ"),
            yuji.do("$meはソファまで戻ると、自分を見上げて小さく歯を見せた彼女の頭を撫でると目を閉じて気持ちよさそうに低く唸る。最初は喉を鳴らすその声に慣れなかったが、最近ではこれが彼女の安寧の声なのだと理解が進んできた",
                "だがその声は不意に無機質な電子音声に変わる"),
            ally.talk("バッテリィ残量が少なくなりました。充電して下さい"),
            yuji.talk("ああ、分かったよ"),
            yuji.do("$meは仕方なく彼女を足元から抱き上げ、壁際に立つロケット発射台のような金属のアームとプラスチックの置き型充電器まで運ぶ。四肢を支えながら腹部を台に載せ、背中を押さえるようにアームを下ろすと、彼女は目を閉じて動かなくなってしまった。その胴体に『Charging』と赤字が浮かび上がったのを確認し、僕はパソコンデスクに戻る"),
            yuji.do("彼女を食肉目ネコ科ネコ属の生物にうまく見せているのはその外見と人工皮膚および人工毛だと理解しているが、それ以上に実際のネコの神経回路をトレースした人工脳回路があるからだということを、こうして一緒に生活しているとよく忘れてしまう",
                "だからこそ意図しないタイミングで彼女が只のロボットであることを認識させるのは止めて欲しいところだが、開発者のキースにはそれを譲ろうという考えは微塵もなかった"),
            yuji.talk("ロボットであることを捨てさせてはいけない……か"),
            yuji.think("彼の言葉を思い出し、改めて彼女に視線を向ける。それなら何故これほど外見を猫そのものに似せてしまったのだろうと思わなくもない"),
            yuji.do("それでも、ただ彼女がそこに居る"),
            yuji.do("そのことが今の僕の人生を支えてくれていることだけは確かなのだ"),
            )

def vanish_her(w: World):
    yuji = w.get('yuji')
    return w.scene("消える彼女",
            w.symbol("　　　　◆"),
            yuji.talk("流石に今回のは参った"),
            yuji.do("玄関ドアを開けてそのまま転がり込むように上がる",
                "急な呼び出しから約一月、殆ど会社に泊まり込みで何とか頓挫しかけた決済システムのベータ版の提出は間に合わせたが、叩いた先からバグが噴出して、正直もう誰の手にも負えない状態だった",
                "それでもやっと一日の休みを手に入れて我が家に帰って来られたのだ"),
            yuji.talk("アリィ？　どこだ？"),
            yuji.do("出かける前に充電器に掛けておいたはずだがそこに彼女はいなかった。胴体を押さえつけておく金属のアームが曲がっている。強引に上げたのだろう",
                "ロボット猫が一人で目覚めてどこかに行ったという可能性もあるが、一番疑うべきは盗難被害だった。すぐにリビングだけでなく寝室や物置を探る。だが荒らされた様子はなく、見慣れた整然さがどの部屋にも敷き詰められていた"),
            yuji.do("それでも一箇所だけ、トイレの窓が割れているのを見つけて僕は慌ててリビングに戻る"),
            yuji.do("パソコンを起動する。携帯電話の方にはソフトが入っていないから一分ほど我慢して、モニタに地図と彼女の位置が表示されるのを待った",
                "電波が捉えられない場所に入り込んだりしていなければＧＰＳが誤差一キロ圏内で特定してくれる"),
            yuji.talk("ん……？"),
            yuji.do("彼女を示す赤い点は臨海公園付近を差していた"),
            )

def lookfor_her(w: World):
    yuji = w.get('yuji')
    return w.scene("彼女を探して",
            w.symbol("　　　　◆"),
            yuji.do("慌てて駅の階段を駆け上がるとブロックが敷き詰められた駅前広場にはベビィカーを押す女性やカップルらしき男女が目に付いたが、鳩以外の動物の姿はなかった"),
            yuji.do("右手には数年前から故障したままになっている大観覧車の姿が見えてあまり良くない思い出が蘇ったが、それを振り切るように頭を揺らすと公園の方に足を向けた",
                "猫だから何かの拍子に家を出ていき迷子になったりして居なくなる。そういう可能性については既にキースと検討を充分に済ませていたから、一つの対策としてＧＰＳで場所を特定できるようにはしておいた",
                "ただそれは猫ロボットが電波を発信できる状態が確保されている必要があり、意図的にそれを遮断されてしまった場合においては従来の猫と同様、目視で探すしかなくなる",
                "その不完全さを解消する手段は結局家から彼女を出られないようにするしかないのだろう"),
            yuji.think("――プログラム的な監禁"),
            yuji.do("そんな言葉が思い浮かび、僕は苦笑する"),
            yuji.talk("おーい。アリィ？　いないのか？"),
            yuji.do("自分の声の周波数を検知して何かしら反応を返すようになっていると説明は受けているが、物陰や人の足元からこそっと顔を覗かせる様子はない"),
            yuji.talk("アリィ"),
            yuji.do("最初こそ丁寧に呼びかけていたのだがそのうちに面倒になってきて、ただ彼女の名を連呼しているだけになってしまう"),
            yuji.do("けれどそれは仕方のないことだ。彼女は人ではない。猫ですらない。ただのロボットだ。見た目こそよく自然の猫に似せて造られているが、その声も温度も仕草も所詮は造りものでしかない",
                "キースはこうなることも踏まえて『ロボットはロボットらしさが大切だ』と言ったのだろう"),
            yuji.do("動かなくなったままの大観覧車の下までやってきたが、彼女は見つからない",
                "見上げると数カ所サビているのが分かったが、メンテもなく、誰も気にしないようになったらこんなものだろう。やがては朽ちてどこかが傾いたり或いは部品やワゴンの落下もあるかも知れない。そういう出来事が発生してようやく危険だと認識され、修理するか解体するかという選択が取られる",
                "閉鎖中と書かれた黄色いプレートのぶら下がる前に腰を下ろし、砂浜の方を見やる。まだ入るには水が冷たいかも知れないと思うが意外と人が集まっていて賑やかな声が聞こえてくる"),
            yuji.talk("いや、あれは……"),
            yuji.do("よく見れば何かを見つけて騒いでいるのだ"),
            yuji.do("それが何か確かめようと向かった僕を待っていたのは、水分を含んだ砂に埋まっていたキジトラの猫だった。いや猫ではない。彼女だ"),
            yuji.talk("すまない。それは僕の物なんだ"),
            yuji.do("集まっていた若者を掻き分け、黒っぽい砂が付着してしまった猫ロボットの成れの果てを受け取る。シャツの袖が汚れるが仕方ない。彼女はずっしりと重く、人工毛が濡れていた"),
            yuji.do("その人垣から抜け出て大観覧車の前まで戻ってくる",
                "ハンカチでは上手く水分を取り切れないが、内部にまで水が入っていないことは確認できた。注意深く彼女の胴体側面にある起動スイッチを入れる。一瞬目が光るが彼女は動いたりはしない"),
            yuji.talk("アリィ？"),
            yuji.do("名前を呼んでみる"),
            yuji.talk("アリィどうしたんだ？"),
            yuji.do("反応はなく、何度かスイッチを入れ直してみたがもう起動サインの目の発光すら見られない",
                "電源か、或いは本格的な故障か",
                "諦めて彼女を手に立ち上がる",
                "観覧車を見上げると強い風に上の方のワゴンが揺られて軋んだ音を立てていた"),
            yuji.talk("やはり厭な場所だな"),
            yuji.do("僕は重くなった彼女を抱いて駅に向かった"),
            )

def always_vanish(w: World):
    yuji = w.get('yuji')
    return w.scene("いつもいなくなる",
            w.symbol("　　　　◆"),
            yuji.do("彼女はその後もことあるごとに失踪した"),
            yuji.do("最初に僕は電波などのハードへの影響を考えたが、キースはすぐソフト面、つまりプログラムか或いは猫を模した人工脳そのものの作用だと指摘した",
                "納得はいかなかったが、それでも無限に代用のボディを用意できる訳ではない。仕方なく彼女の人工神経回路にある種のブレーキプログラムを組み込んだ。それは彼女がいなくなる直前に発する奇妙な回路の動きを捉えたことからキースが提案したものだったが、実際そのブレーキは上手く利いた"),
            yuji.talk("またなのか……"),
            yuji.do("会社から帰ってくると玄関先で彼女が横になって倒れている。目は開かれたままで前足を僅かに伸ばし、後ろ足は蹴り出そうとしたところで動きを止められたままで床の上にいる",
                "僕は溜息をついて彼女を拾い上げると、鍵の破壊されたドアから家の中に入った"),
            yuji.do("ひとまず彼女のボディを充電器に戻すと、ひん曲がった金属のアームを構わずに降ろして固定する",
                "それから僕はジャケットだけ脱いでハンガーに引っ掛け、冷蔵庫から缶ビールを取り出すとそれを一気に喉に入れた"),
            yuji.talk("……どうしてなんだ"),
            yuji.do("十一月に入ってからこれでもう四度目だった。何が気に入らないのか知らないが、突発的に発生するこの脱走行動は徐々にその間隔が短くなっていた",
                "僕は彼女の定位置である引っかき傷のあるソファに腰を下ろすと、疲れた頭をもたれさせて天井を見上げる"),
            yuji.think("何が悪い？　どこを間違えた？　そもそも問題など幾ら探しても見つからないじゃないか",
                "足の先で机を蹴る"),
            yuji.do("人を殴ったりはしないが、苛立った時に物に当たるのが小さい頃からの癖だった",
                "右の脛に痛みを感じながら、それでも僕は彼女がここから姿を消そうとする仕組みを考えようとする"),
            yuji.think("――問題は一つ一つ丁寧に紐解いていけば必ずその先に原因となる事象を見つけられる"),
            yuji.think("それは研究者である父から教えられたことだが、事実、世の中の大半の問題は丁寧に分析していけばそれなりの原因がちゃんと見つかるものばかりだった。ただそれをせずに勝手に思い込みで原因をでっち上げて、挙句に関係ない人間を非難する。そういう輩の方がずっと多いことに僕は辟易してしまう",
                "だからこそこうしてある程度在宅でもできる仕事を選んだのだ",
                "だったらどうして今の自分はこんなにも苛立っているのだろう"),
            yuji.do("と、携帯電話が鳴った。キースからのショートメールで駅まで迎えに来てくれないかと書かれていた"),
            )

def friend(w: World):
    yuji = w.get('yuji')
    kieth = w.get('kieth')
    return w.scene("友人",
            w.symbol("　　　　◆"),
            yuji.talk("来日するだなんて一言も言ってなかったじゃないか"),
            yuji.do("それでも何度かやり取りをし、東京駅までの時間を考えて今すぐに出た方が良いと分かり、呼気に僅かなアルコールを含んだままハンガーに掛けたジャケットを掴んで玄関を出た",
                "壊された鍵の代わりに足元にブロックを挟んでおいたが、先に修理の電話を掛けておくんだったと後悔した"),
            yuji.do("半年ぶりに会ったキースは相変わらず日焼けした真っ黒な肌で、毛深い腕を派手なアニメのシャツからはみ出させながらガハハと笑った",
                "そのまま自宅には向かわずにジャパニーズラーメンが食べたいと言うものだから仕方なく、五分ほど並んで人気のラーメン店に入った"),
            kieth.talk("ユージはまだゴワサンになった決済プログラムをやってるの？"),
            yuji.do("ご破算という言葉が引っかかることなく出てくる彼の日本語能力に今更感心はしなかったが、僕は「ああ」とだけ短く頷き、チャーシュー麺を頼んだ"),
            yuji.talk("来るなら一声掛けておいてくれればよかったのに"),
            yuji.do("がっしりとした器から湯気を昇らせるラーメンが出されると、まずは脂の浮いたスープを蓮華で掬い上げて唇を湿らせる"),
            yuji.talk("忙しくて迎えに行けなかったら、また東京駅構内で一日過ごすつもりだったのか？"),
            kieth.talk("そういう時の為にアリィを使えるようにしてあったんだヨ。ただ君の彼女をどこにもやりたくないからという要望からその機能はオミットしてあるんダ。そろそろ彼女を自由にしてあげてもいいんじゃないか？"),
            kieth.do("キースの前には山盛りのモヤシとコーンを載せた味噌ラーメンが置かれた"),
            kieth.talk("彼女は猫だヨ。猫というのは何かをサトった時には自分の居場所から立ち去るものダ"),
            kieth.do("器用に割り箸を二つにしてモヤシの山を切り崩し、麺を掴んで引っ張り出すと、彼はそれを口に入れる。音を立てて豪快に啜る"),
            yuji.talk("猫だがロボットだ。いくら猫の神経回路を模したといっても、そんな意味不明なところまで真似てもらう必要はない"),
            yuji.think("熱い。脂混じりのスープを纏った麺はやたらと攻撃的な熱がある"),
            yuji.talk("自由というなら、僕は既に彼女に十分な自由を提供しているはずだ"),
            yuji.do("それを空気と一緒に吸い込む。喉を抜け、胃袋までもその熱で焼いてしまおうというラーメンは、どうしようもなく胃をキリキリとさせた"),
            kieth.talk("なあユージ。この丼の中のラーメンは自由だろうか？"),
            yuji.talk("またお得意のくだらないジョークか？"),
            kieth.do("ふうふうと息を吹きかけている僕の隣で豪快に麺を啜り上げてから、キースは首を横に振る"),
            kieth.talk("このラーメンはオレたちに食べられる為にこの中に収まっているヨネ？　それをどう食べるかどの順番で食べるか、それについてはオレたちが選ぶ。でもそれは制限された自由でしかなくて、オレたちには結局食べるか残すか、そもそも食べないというくらいの選択肢しか渡されていないんだヨ"),
            yuji.do("いつも彼が言うことは少しズレている。ただ何が言いたいかは察することができたから、僕は小さな吐息を落としてから、無言でラーメンの続きを食べた",
                "甘みの強い脂が口の中でのたうち回る",
                "いつも三分の一程度までは美味しい、と感じるのにそこから先になると急にやる気を失った子供みたいに、麺を丼の中でかき回し、胡椒を振ってみたり、水で何度も口の中をすすいでみたり、サイドメニューを頼んだり、本当はもう食べたくないんだという自分の気持ちと向き合うことから目を逸してしまう"),
            kieth.talk("ユージは初めて会った時から変わらないヨネ。なら最初からハーフサイズを頼めば良かった"),
            yuji.talk("いつも見積もりが甘いだけさ。誰だって最初はそれくらい食べ切れると思うんだよ。けどそのうちに自分の手には余ると気づいて、途方に暮れながらも何とか口の中に突っ込む。人生ってそういうものだろう？"),
            yuji.do("既にその殆どを胃袋に入れてしまったキースは笑って僕の肩を叩くと、「要らないなら食べてやるヨ」と蓮華と箸を使って麺の移動を始める"),
            yuji.think("その仕草に、この男と会うきっかけを与えてくれた彼女のことを思い出す",
                "外に出て、人と人を会わせるのが自分の仕事だと楽しそうに語ってくれた彼女も、いつの間にか僕の前からいなくなってしまった。ひょっとすると誰もが僕から離れていってしまうのかも知れない。そういうプログラムが組み込まれているのだ。なら、アリィが出ていくのもまた僕の所為ということになる",
                "結局、問題というのは一番目を背けていたところにひっそりと眠っているのだ"),
            yuji.do("いつの間にか場所はラーメン店から居酒屋に移っていて、既に頬を赤くしたキースが僕の右肩にしなだれかかっていた。カウンターに横並びで座る中、後ろを忙しなくパートの女性が行き来する。ビールのジョッキを幾つも束ねれば重いだろうにそれでも彼女は笑顔だ。無理をしているのかどうかまでは推測することしかできない。それでも今の僕からすると、心の底から楽しく働いているように見えた"),
            kieth.talk("何だヨ、ユージ。やっぱりまだ未練があるんだネ？"),
            yuji.talk("何を言ってるんだ。だから何度も言ったろう？　もう僕は諦めた。アリィはどうしたって僕の前からいなくなってしまうんだ"),
            kieth.talk("アリィじゃない。有紗のことだ"),
            )

def her_inside(w: World):
    yuji = w.get('yuji')
    arisa = w.get('arisa')
    return w.scene("彼女の中身",
            w.symbol("　　　　◆"),
            yuji.come("酔い潰れたキースを予約したホテルの部屋まで送ってから、自宅に戻ってきた"),
            yuji.do("ドアを開けようとして鍵が壊れたままだったことを思い出したが、足元に置いたブロックを手ではなく足で押し退けるくらいには充分に疲れていて、リビングまで上がってくるとそのままソファにダイブする"),
            yuji.talk("アリィ……いるか？"),
            yuji.think("どうせまたいなくなる", "&"),
            yuji.do("そんな思いで充電器を見ると、そこには雉柄の猫ロボットが寝そべったままになっていた"),
            yuji.talk("アリィ……そうか。まだ、ここに居てくれるんだな？"),
            yuji.do("既に充電は終わっている。ひしゃげたアームを上げ、彼女を抱き起こす。胴体側面の起動スイッチに手をやると、目が光ってから彼女は小さく鳴いた"),
            arisa.talk("ごめんなさい"),
            yuji.do("と"),
            yuji.talk("え？　アリィ？"),
            arisa.talk("もう動けないの。すまないけれどソファに置いてくれないかしら"),
            yuji.do("彼女にそう言われ、僕は曖昧に返事をしながらその体をソファの上まで運んで寝そべらせた。前足の上に顎を置こうとするが、小刻みに震えて上手く動かせないようだ。彼女の代わりに僕が頭を置いてやる"),
            arisa.talk("ありがとう"),
            yuji.talk("アリィ……ではなく、君なのか、本当に？"),
            arisa.talk("どうして驚いているの？　このロボット猫の人工脳に私、日陰有紗のものを使うことを提案したのはあなただったじゃない？"),
            yuji.do("音声こそ合成した無機質な駅や売店でよく耳にするものだったが、その話しぶりは正に彼女、日陰有紗のそれだった"),
            yuji.talk("猫の人工脳では上手くいかなかったからどうせなら人間の人工脳を試してみればと、そう言っただけで、何も君のものを使うだなんて……そんなこと一言も"),
            arisa.talk("その理由は、考えたことがあるの？"),
            yuji.think("キースならやりかねない。そういう予感がなかった訳ではない。けれどそんな倫理に反することを黙ってやるとは思ってなかったのだ",
                "何より彼女は、有紗は、僕たちの前から姿を消して三年になる"),
            arisa.talk("今日、私の件について彼から話は聞いてないようね"),
            yuji.do("ああ、と脱力して答え、僕はそのままカーペットの上に腰を下ろした。ソファの彼女と目線が近くなる"),
            arisa.talk("猫がある日突然飼い主の前からいなくなる。それについての幾つかの説を、あなたに話したことがあるわね"),
            yuji.do("結婚したら絶対に猫を飼いたいと言っていた有紗は、自分よりも早く死ぬことが分かっていても決して手放したりせずに最期の瞬間まで一緒にいることを選ぶ。そう言っていたことを思い出す"),
            arisa.talk("その気持ちがね、今ならよく分かるの"),
            yuji.talk("猫になって学習した、とでも言いたいのか？　猫になってまで僕の前から何度も逃げ出した君は、ただ僕という器から出たかっただけなんだろう？"),
            arisa.do("猫の黒目が大きくなる。細く縦長のネコ科のそれではなく、人間の瞳のように見えた"),
            arisa.talk("何故逃げ出したのか。いつもみたいにちゃんと分析をしなかったの？"),
            yuji.talk("ハード的にもソフト的にも何も問題はなかった。だから勝手にいなくなったのは気まぐれだよ。気分だよ。ずっと家に閉じ込めていたから嫌になったんだよ。それでいいか？"),
            arisa.talk("すぐ大声になる。声が大きければ相手は黙る。黙れば自分の言葉が届く。正しいと思える。でもそうやって目の前の考えを排除してきたあなたには、結局猫一匹の気持ちすら理解できなかったのね"),
            yuji.do("立ち上がり、思い切りテーブルを蹴飛ばした。派手な音を立ててひっくり返り、上に置いてあったリモコンが投げ出される"),
            arisa.talk("アリィはね、もう自分の命がそう長くないことを知ったの"),
            yuji.talk("何だよ。ロボットに命も何もないだろう？"),
            arisa.talk("ハードはいつか壊れるし、ソフトだってそれを運用するシステムのアップデートについていけなくなる。いつかはね、みんないなくなるのよ。それがいつ、とはっきり分からなくても、予感するに値する何かがあれば、それで充分なの"),
            yuji.do("涙を流す機能は備わっていないはずだ",
                "それなのに彼女の瞳からは液体が溢れていた"),
            yuji.talk("やはり壊れているんだな？　明日にでもキースに来てもらって向こうで最初から作り直す手続きを"),
            arisa.talk("祐司"),
            yuji.do("有紗の呼び方そっくりに、僕の名が呼ばれた"),
            arisa.talk("あなたに伝えておくべきだったのかも知れない。でもね、悲しい顔を二度もさせてしまうのは、やはり嫌だったのよ"),
            yuji.talk("有紗？"),
            arisa.talk("さよならを言わない為に、猫はあなたの前から消えるのよ"),
            yuji.talk("何を言ってるんだ？"),
            yuji.do("電源が落ちたのが分かった。妙なモータ音が響き、目の光が消えた"),
            yuji.do("僕は慌てて起動スイッチを押したが反応はない"),
            yuji.do("充電器にセットしたがそれも反応はない"),
            yuji.do("キースに電話したが反応がない"),
            yuji.do("この手に猫ロボットの冷たい感触はあったが、もう彼女はいなかった"),
            w.symbol("　　　　◆"),
            yuji.do("翌日、キースの電話で目覚めた僕は、日陰有紗が脳腫瘍で亡くなったことを知った。昨夜の十二時少し過ぎたくらいだったそうだ"),
            )

