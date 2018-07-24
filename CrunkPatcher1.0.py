import random



def CrunkPatcher():
    
    #crunkpatcher ASCII banner hell yes
    
    print('  _____                  _    _____      _       _               ')
    print(' / ____|                | |  |  __ \    | |     | |              ')
    print('| |     _ __ _   _ _ __ | | _| |__) |_ _| |_ ___| |__   ___ _ __ ')
    print("| |    | '__| | | | '_ \| |/ /  ___/ _` | __/ __| '_ \ / _ \ '__|")
    print("| |____| |  | |_| | | | |   <| |  | (_| | || (__| | | |  __/ |   ")
    print(" \_____|_|   \__,_|_| |_|_|\_\_|   \__,_|\__\___|_| |_|\___|_|   ")
    print('                                                                 ')
    print('                          VERSION 1.0                            ')
    print('\n')    

    #greeting
    print("       Welcome to CrunkPatcher 1.0 for the MakeNoise 0-coast!")
    print('\n')
    print('This script will generate & display a new random patch for you to explore. ')
    print("CrunkPatcher was inspired by Tom Whitwell (http://www.musicthing.co.uk)  ")
    print("and his awesome compose.py script. ")
    print('\n')
    
    #patchcables to be used. 8 is the current limit 
    print("Enter quantity of patch cables you wish to use (1-8) and press ENTER." ,'\n')
    patchcables = int(input('PATCHCABLES: '))
    print('\n')
    if patchcables > 8:
        print("Too many patchcables!")
        quit()
    #handling low quantities of patch cables for some lists
    if patchcables > 3:
        default_cables = 3
    else:
        default_cables = patchcables
    
    #setting chaocity level
    print("Select Chaocity and press ENTER.")
    print("     1. Tame")
    print("     2. Chaotic")
    print("     3. Total Disaster", '\n')
    print("NOTE: Setting '3' may patch outputs to other outputs. ")
    print("DISCRETION ADVISED!", '\n')
    chaocity = int(input('CHAOCITY LEVEL: '))
    print('\n')
    print('Your patch is:', '\n')
    
    #hardcoded lists of 0-coast patch points. Replace these with your synthesizer's patch points for a custom random patch generator
    cv_o = ['Stepped Random OUTput', 'Voltage MATH: Channel 1 Output', 'Voltage MATH: Channel 2 Output', 
            'Slope: CV Output', 'Contour: CV Output']
    
    cv_i = ['Voltage MATH: Channel 1 Input', 'Voltage MATH: Channel 2 Input', 'Oscillator: 1/V OCTave Input', 
            'Oscillator: Linear FM Input','Overtone: CV Input', 'Multiply CV Input', 'Slope: Rise/Fall Time CV Input', 
            'Contour: Decay Time CV Input', 'Balance: CV Input', 'Dynamics CV Input']

    a_o = ['Oscillator: Triangle Wave Output', 'Oscillator: Square Wave Output', 'Dynamics Output: Modular level Audio Signal']

    a_i = ['Balance: Channel External Input', ]

    t_i = ['TEMPO Input', 'Slope: Trigger Input', 'Contour: Gate Input']

    t_o = ['CLocK OUTput', 'Slope: End of Cycle (EOC) Gate Output', 'Contour: End of Onset (EON) Output']

    h = ['Your Inner Self']

    #chaos level = 1: cv/audio outputs to cv/audio inputs, trigger ins to trigger outs
    rrcvout = random.sample(cv_o + a_o, patchcables-1)
    rrcvin = random.sample(cv_i + a_i, patchcables-1)
    rrtrigin = random.sample(t_i, 1)
    rrtrigout = random.sample(t_o, default_cables)

    #chaos level = 2: outputs to inputs, classes ignored
    bigmessouts = random.sample(cv_o + a_o + t_o, patchcables)
    bigmessins = random.sample(cv_i + a_i + t_i, patchcables)

    #chaos level = 3: all I/O can route to all other I/O, some may be invalid
    maxchaos = random.sample(cv_o + a_o + t_o + cv_i + a_i + t_i, patchcables)
    maxchaos2 = random.sample(cv_o + a_o + t_o + cv_i + a_i + t_i + h, patchcables)

    #chaocity loops
    if chaocity == 1:
        for o,i in zip(rrcvout, rrcvin):
            print(o, '  TO  ', i, '\n')
        for ao,ai in zip(rrtrigout, rrtrigin):
            print(ao, '  TO  ', ai, '\n')
        
    elif chaocity == 2:
        for i,n in zip(bigmessouts,bigmessins):
            print(i + '  TO  ' + n, '\n')
    
    elif chaocity == 3:
        for m,x in zip(maxchaos,maxchaos2):
            print(m + '  TO  ' + x, '\n')
    
    else:
        print('Entered value is TOO chaotic. Please restart!')
        quit()
    print('\n')  


CrunkPatcher()



