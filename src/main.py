#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Story: "title"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic
from config import ASSET
# import scenes
from scenes import mainstage


################################################################
#
#   1. Story memo
#   2. Story structure
#   3. Plot
#   4. Conte
#   5. Draft
#
################################################################

# Constant
TITLE = "いつも彼女はいなくなる"
OUTLINE = "ロボット猫を飼っていたが、ある日突然消えてしまう。見つけて連れ戻すが何故かすぐに出ていってしまう"


# Episodes
def ep_main(w: World):
    return w.episode('main',
            mainstage.a_cat(w),
            mainstage.vanish_her(w),
            mainstage.lookfor_her(w),
            mainstage.always_vanish(w),
            mainstage.friend(w),
            mainstage.her_inside(w),
            w.symbol("（了）"),
            )

def ch_main(w: World):
    return w.chapter('main',
            ep_main(w),
            )


def main(): # pragma: no cover
    w = World.create_world(f"{TITLE}")
    w.config.set_outline(f"{OUTLINE}")
    w.config.set_version(1,0,0)
    w.db.set_from_asset(basic.ASSET)
    w.db.set_from_asset(ASSET)
    return w.run(
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

