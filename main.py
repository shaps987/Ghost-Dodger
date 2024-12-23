def on_a_pressed():
    if mySprite.is_hitting_tile(CollisionDirection.BOTTOM):
        mySprite.vy = -200
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    mySprite.x += -5
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    mySprite.x += 5
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap(sprite, otherSprite):
    game.over(False, effects.dissolve)
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap)

projectile: Sprite = None
mySprite: Sprite = None
tiles.set_tilemap(tilemap("""
    background
"""))
mySprite = sprites.create(img("""
        ........................
            ....ffffff..............
            ..ffeeeef2f.............
            .ffeeeef222f............
            .feeeffeeeef...cc.......
            .ffffee2222ef.cdc.......
            .fe222ffffe2fcddc.......
            fffffffeeeffcddc........
            ffe44ebf44ecddc.........
            fee4d41fddecdc..........
            .feee4dddedccc..........
            ..ffee44e4dde...........
            ...f222244ee............
            ...f2222e2f.............
            ...f444455f.............
            ....ffffff..............
            .....fff................
            ........................
            ........................
            ........................
            ........................
            ........................
            ........................
            ........................
    """),
    SpriteKind.player)
tiles.place_on_tile(mySprite, tiles.get_tile_location(1, 5))
mySprite.ay = 500

def on_update_interval():
    global projectile
    projectile = sprites.create_projectile_from_side(img("""
            ........................
                    ........................
                    ........................
                    ........................
                    ..........fffff.........
                    ........ff1111bff.......
                    .......fb1111111bf......
                    .......f111111111f......
                    ......fd1111111ffff.....
                    ......fd111dd1c111bf....
                    ......fb11fcdf1b1bff....
                    ......f11111bfbfbff.....
                    ......f1b1bdfcffff......
                    ......fbfbfcfcccf.......
                    ......ffffffffff........
                    .........ffffff.........
                    .........ffffff.........
                    .........fffffff..f.....
                    ..........fffffffff.....
                    ...........fffffff......
                    ........................
                    ........................
                    ........................
                    ........................
        """),
        randint(-125, -70),
        0)
    tiles.place_on_tile(projectile, tiles.get_tile_location(9, 5))
    info.change_score_by(1)
game.on_update_interval(1000, on_update_interval)
