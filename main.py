brilho = 0
def ativar_leds(direcao: str):
    global brilho
    brilho = 9
    while brilho < -1:
        if direcao == "N":
            basic.show_leds("""
                . . # . .
                                . # # # .
                                # # # # #
                                . . . . .
                                . . . . .
            """)
            if brilho == 9:
                music.play_tone(440, music.beat(BeatFraction.DOUBLE))
        if direcao == "E":
            basic.show_leds("""
                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
            """)
            if brilho == 9:
                music.play_tone(330, music.beat(BeatFraction.DOUBLE))
        if direcao == "S":
            basic.show_leds("""
                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
            """)
            if brilho == 9:
                music.play_tone(262, music.beat(BeatFraction.DOUBLE))
        if direcao == "W":
            basic.show_leds("""
                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
            """)
            if brilho == 9:
                music.play_tone(165, music.beat(BeatFraction.DOUBLE))
        brilho += -1

def on_forever():
    pass
basic.forever(on_forever)
