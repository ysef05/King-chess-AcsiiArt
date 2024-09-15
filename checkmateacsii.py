import time
import os

# ASCII art of the knight leaning to the right
knight_right = [                                                                        
"                                          VW                     ",
"                                        VYWTRT                   ",
"                                   WXWUTWWSQPRT                  ",
"                                   VXUSRSSQPOMNQU                ",
"                                   YVSRQQQPPOOOOT                ",
"                                   XWURRQQPPPPOPS                ",
"                               XWVVVVXVSRQPPPQRU                 ",
"                            YXUSRRRVXWTSRQPPQU                   ",
"                            ZWUTTTTXYXWVTSQPJHMPS                ",
"                            YXYXUTTUVWVTSRPNJEEFGKR              ",
"                            XWXWWXXVUTTTTSSRPONNMLJP             ",
"                            XXWWVUUTSSSSRRRQQPONLKOX             ",
"                             XWWVUTSRQPONMLKJIHHIN               ",
"                             YWWVUTSQPONMKJIHGGKS                ",
"                             WXWVUTRQPNMKJIGGGO                  ",
"                            XYXWVUTRPOMLKIGGJR                   ",
"                            XXYYXVTRPNMKIHGGR                    ",
"                          WYVXXWWWWVTROLIGGL                     ",
"                       XWWXXXXYXWUSQPONLJHHN                     ",
"                      YYXXXYYYXXWVTRPNLIHFEFM                    ",
"                      YYYXXWXXXXWVVUTRPMKIGFEI                   ",
"                        YYYYXWWWVUTRQPOMKIHFEEL                  ",
"                           WUUVVUUUTTSRQONLKIHL                  ",
"                           XWUTRPOOOPOONMKJHIMO                  ",
"                           YXWUSQNLJHGMQSS                       ",
"                           YXWUTQOLJHJU                          ",
"                          YXXWUSPNLIHN                           ",
"                          YXXVURPMKHHN                           ",
"                         YYXWVTQOLJHJQ                           ",
"                        XYXXWUSPNKIGN                            ",
"                       YYXXWVTROMJHHS                            ",
"                      YYXXXWVSQOLJHJW                            ",
"                     VYYXXXVURPNKIGK                             ",
"                    WYXYXXWVTRPMKHGK                             ",
"                 XXVXXYYXXWUSQOLJHGL                             ",
"                YXWWXYYYXWVTSPNLJHGJ                             ",
"                WXXWWWXXXWUSRPNLJHFFJP                           ",
"               WXWWXYXWVVUTSRPOMKIGFEFP                          ",
"           WWWWWWWWWVVVWVUUTSSRPONLKIHM                          ",
"         XWWWXXXXXWWVUUTSRQPPONNMJJHGJP                          ",
"       XWWWWXXXXYYYXWVUTSQPOMLKJIHGFFJ                           ",
"      XXXXXXXXXYYYYXXXVTSRQONLKJHGGFEEK                          ",
"      XVXXXXYYYYYYYXXWUUTSRQOOQLJIGGFEDJT                        ",
"      XVVWXYYYYYYYXXVUUTTSSQPONMKJIHGFEEHT                       ",
"     XWWWVVWXXYYXXXWUUUTTSRRQPONMLKIHHGFEM                       ",
"      WVWXWVUVVWWWWVUUTTSSRQQPONMLKJIHGFFJS                      ",
"       WVVWXXVTSSTTTTSSRRRQPPONMLLKJIHGFFKS                      ",
"         XVTUUVXWTRPOOOOONNNMLKKJIIHGGFEEM                       ",
"            VTSRRSSSSRQPNLKJJJIIHHGGFEEEGR                       ",
"               SRRQONMMMMMMLLLKJIHHGFFEGM                        ",
"                     SSRONLJJIIHHHGGGIM                          ",
"                                                                 ",
"                  You are a brainless just saying. CHECKMATE!!!!!",
]

# ASCII art of the knight leaning to the left
knight_left = [

"                WXVRRT                                           ",
"                WXTQPPQPRU                                       ",
"               UVXURPOOONPU                                      ",
"             YWTTSRQPPOOOOR                                      ",
"             WYTSRQQQPPPPQT                                      ",
"              YVSRRRQQPPQUVWUVVT                                 ",
"               XXUWURRQPPNHHFGHIKMT                              ",
"               VVTYVTSSTSQMGHKNNMLS                              ",
"             WURQXXXXWUTQOOQQPPLIJU                              ",
"           WXTSTTUWWWVUTTSSRPMJHGK                               ",
"           YXVTTTTTTUUUTSQOMKJHGGM                               ",
"            YXYXXXWVUTSRQONLKIHGGO                               ",
"             YXWWWVUTSSQPONLKIHGHR                               ",
"               XXWWVUTSRQPNMKJHGGO                               ",
"                YXWWVUTSRPOMLJIGFJ                               ",
"                  XXWVUTSRPOMKJJIHO                              ",
"                  YYXWWVUTTTSQNKHFEEFJR                          ",
"                   YYYYYXVTRPNLKHGGHGFEFL                        ",
"                    XXXXWVUTRQPOONMJHHIHHP                       ",
"                  WXXXXYXXWVVUTRPNLMNLJIK                        ",
"                 ZWWYYYYYYWVUTSSSRQPNKLQ                         ",
"                 YWXWXXXWWWWVUTTRPMLOV                           ",
"                 XYXYYYYYYWVTSPMIHGIU                            ",
"                    YXYXWWVUTRPNMKIGM                            ",
"                          XWWUSQOMKHIO                           ",
"                          YYWWUSQOLJHKS                          ",
"                           YXWVURPNKIGM                          ",
"                           ZYXWUTROMKHHQ                         ",
"                            YXXWUSQNLIGJP                        ",
"                            YXXWVTRPMKHGJ                        ",
"                            YYXXWUSQOMJHGL                       ",
"                            YYXXXVUSPNLJHGK                      ",
"                             YYXXWVTRPNLJHGINQ                   ",
"                             YYXXXWUSQPNLJHGFEEHP                ",
"                             XXYYXWVTSQONLJHHHIIIO               ",
"                            VWXYYXXWUSRQOONNNMJHFM               ",
"                           XVWXYYYXWVTTSSRQQNJHGFFHLT            ",
"                           YXXWWWWVVVUTTRPNLKIHGFFEEDFJQ         ",
"                           XXXXXXXWVUTRQPNMLKJIHHGGFFEEEGN       ",
"                            WWWWWVVUTTRQPONMMNMKJJIHHHGGFFJ      ",
"                           WXWXXXWWWVUTSSRQPPONMLLKJJIHHGFFM     ",
"                          VVWXXYYYYXXXVTTSSRQQPONMMLKJIHGFEEN    ",
"                         WVWXXXYYYYYXWVUTTSSRQQPONMLKJHGGFEEI    ",
"                        XWWWXXXYYYYXXWVUUTTSRRQPOOOLJIHGFFFEJ    ",
"                        XWXXXXXYYYYYXXVUUTTSRQPONLKJIHHHGFFK     ",
"                        YXXXXYYYYYYXXXWVTTSRPONLKJJJKJHGGIR      ",
"                         XVWWXXXXWWWVUUTSQPNMMMNNMLJIHJNS        ",
"                         XXWWVVUUUTTSSRSSSSSQONLKJKLQS           ",
"                          WWVWXXXXXWWVUTSQONNNPQR                ",
"                            XWVVVUUUTSSSRTUT                     ",
"                                                                 ",
"                  You are a brainless just saying. CHECKMATE!!!!!"                                                                 
]

def clear_console():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_knight(knight_art):
    """Print the knight art."""
    for line in knight_art:
        print(line)
    print('\n')

def main():
    while True:
        clear_console()
        print_knight(knight_right)
        time.sleep(0.6)  # Adjust speed as needed
        
        clear_console()
        print_knight(knight_left)
        time.sleep(0.6)  # Adjust speed as needed

if __name__ == "__main__":
    main()
