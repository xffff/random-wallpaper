import sys, ctypes, os, random

def bgchg(p):
    print "Changing wallpaper"
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER,0,p)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if os.path.exists(sys.argv[1]):
            files = [files for root, dirs, files in os.walk(sys.argv[1])]
            files = files[0]
            newbg = files[random.randint(0, len(files)-1)]
            print "Changing background to: ", newbg
            bgchg(os.path.join(sys.argv[1],newbg))
        else:
            print "Folder doesn't exist: ", sys.argv[1]
    else:
        print "Usage: {0} folder-of-backgrounds".format(sys.argv[0])
        
