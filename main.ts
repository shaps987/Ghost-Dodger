controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (mySprite.isHittingTile(CollisionDirection.Bottom)) {
        mySprite.vy = -200
    }
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.x += -5
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.x += 5
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function (sprite, otherSprite) {
    game.over(false, effects.dissolve)
})
let projectile: Sprite = null
let mySprite: Sprite = null
tiles.setTilemap(tilemap`background`)
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
tiles.placeOnTile(mySprite, tiles.getTileLocation(1, 5))
mySprite.ay = 500
game.onUpdateInterval(1000, function () {
    projectile = sprites.createProjectileFromSide(img`
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
        `, randint(-125, -70), 0)
    tiles.placeOnTile(projectile, tiles.getTileLocation(9, 5))
    info.changeScoreBy(1)
})