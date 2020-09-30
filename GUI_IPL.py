import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.offline as ply
import tkinter
from tkinter import ttk
from PIL import ImageTk, Image

window = tkinter.Tk()
window.title("IPL Record Checker")
window.geometry('1000x400')

canv = tkinter.Canvas(window, width=620, height=120)
canv.pack(pady=18)
img = tkinter.PhotoImage(file="ipl_logo.png")
canv.create_image(310,60, image=img)

window.config(background = "#85aff2")

frame = tkinter.Frame(window, bg='#FFDF00', bd=20,relief=tkinter.GROOVE)
frame.pack()
title = tkinter.Label(frame, text='***IPL Analysis***', bg='#c9e3ff', fg='#1279ff')
title.config(font = ('Arial Black', 20, 'underline italic'))
title.pack()


def bts_win():
    bts_win = tkinter.Tk()
    bts_win.title("Batsman Stats")
    bts_win.geometry('650x650')
    bts_win.config(background = "#85aff2")
    frame = tkinter.Frame(bts_win, bg='#FFDF00', bd=20,relief=tkinter.GROOVE)
    frame.pack()
    titl = tkinter.Label(frame, text='***Batsman Stats***', bg='white', fg='#1279ff')
    titl.config(font = ('Arial Black', 20, 'underline italic'))
    titl.pack()

    df1=pd.read_csv('deliveries.csv')

    #TO CREATE LIST OF BATSMAN
    s1=set()
    for i in range (0,179078):
        s1.add(df1.batsman[i])
    bts_lst=list(s1)
    bts_lst.sort()

    frame = tkinter.Frame(bts_win, bg='#FFDF00', bd=20,relief=tkinter.GROOVE)
    frame.place(x=33,y=110)
    sel_bts = tkinter.Label(frame, text='  Select batsman  ', bg='white', fg='#1279ff')
    sel_bts.config(font = ('Arial Black', 20, 'underline italic'))
    sel_bts.pack()

    menu = ttk.Combobox(bts_win, value=bts_lst)
    menu.current(0)
    menu.config(width=42,height=20)
    menu.bind("<<ComboboxSelected>>")
    #menu["menu"].config(bg="#1279ff")
    menu.place(x=28,y=210)

    def reset():
        frame = tkinter.Frame(bts_win, bg='#FFDF00', bd=20,relief=tkinter.GROOVE)
        frame.place(x=380,y=120)
        rslt_lbl = tkinter.Label(frame, text='          \t        ', bg='white', fg='#1279ff')
        rslt_lbl.config(font = ('Arial Black', 20))
        rslt_lbl.pack()

    def show_result(result):
        rslt_lbl = tkinter.Label(bts_win, text='RESULT:-{}'.format(result), bg='white', fg='#1279ff')
        rslt_lbl.config(font = ('Arial Black', 20, 'underline italic'))
        rslt_lbl.place(x=400,y=140)
 
    def six():
        '''to calculate no. of sixes hit by a batsman in whole ipl'''

        ent_bts=menu.get()
        scor=df1.batsman_runs==6
        btsman=df1.batsman==ent_bts
        case=(scor & btsman)
        n=df1[case].count()
        result= (n.match_id)
        reset()
        show_result(result)

    def bowl_played():
        '''to calculate no. of bowl played by a batsman in whole ipl'''

        ent_bts=menu.get()
        btsman=df1.batsman==ent_bts
        scor=df1.extra_runs==0
        case=(btsman & scor)
        result= (df1[case].match_id.count())
        reset()
        show_result(result)

    def total_runs():
        '''to calculate runs scored by a batsman in whole ipl'''

        ent_bts=menu.get()
        btsman=df1.batsman==ent_bts
        scor1=df1.batsman_runs==1
        scor2=df1.batsman_runs==2
        scor3=df1.batsman_runs==3
        scor4=df1.batsman_runs==4
        scor6=df1.batsman_runs==6
        totalscor=df1[btsman & scor1].match_id.count()+(2*df1[btsman & scor2].match_id.count())+(3*df1[btsman & scor3].match_id.count())+(4*df1[btsman & scor4].match_id.count())+(6*df1[btsman & scor6].match_id.count())
        result= (totalscor)
        reset()
        show_result(result)

    def four():
        '''to calculate no. of fours hit by a batsman in whole ipl'''

        ent_bts=menu.get()
        scor=df1.batsman_runs==4
        btsman=df1.batsman==ent_bts
        case=(scor & btsman)
        n=df1[case].count()
        result= (n.match_id)
        reset()
        show_result(result)

    def caught():
        '''to find how many time particular batsman got caught in whole ipl'''

        ent_bts=menu.get()
        btsman=df1.player_dismissed==ent_bts
        wickt=df1.dismissal_kind=='caught'
        case=(btsman & wickt)
        n=df1[case].count()
        result= (n.match_id)
        reset()
        show_result(result)

    def bowled():
        '''to find how many time particular batsman got bowled in whole ipl'''

        ent_bts=menu.get()
        btsman=df1.player_dismissed==ent_bts
        wickt=df1.dismissal_kind=="bowled"
        case=(btsman & wickt)
        n=df1[case].count()
        result= (n.match_id)
        reset()
        show_result(result)

    def runout():
        '''to find how many time particular batsman got run-out in whole ipl'''

        ent_bts=menu.get()
        btsman=df1.player_dismissed==ent_bts
        wickt=df1.dismissal_kind=="run out"
        case=(btsman & wickt)
        n=df1[case].count()
        result= (n.match_id)
        reset()
        show_result(result)

    def lbw():
        '''to find how many time particular batsman got LBW in whole ipl'''

        ent_bts=menu.get()
        btsman=df1.player_dismissed==ent_bts
        wickt=df1.dismissal_kind=="lbw"
        case=(btsman & wickt)
        n=df1[case].count()
        result= (n.match_id)
        reset()
        show_result(result)

    def cgt_bld():
        '''to find how many time particular batsman got caught and bowled in whole ipl'''

        ent_bts=menu.get()
        btsman=df1.player_dismissed==ent_bts
        wickt=df1.dismissal_kind=="caught and bowled"
        case=(btsman & wickt)
        n=df1[case].count()
        result= (n.match_id)
        reset()
        show_result(result)

    def stump():
        '''to find how many time particular batsman got stumped in whole ipl'''

        ent_bts=menu.get()
        btsman=df1.player_dismissed==ent_bts
        wickt=df1.dismissal_kind=="stumped"
        case=(btsman & wickt)
        n=df1[case].count()
        result= (n.match_id)
        reset()
        show_result(result)

    six_bt = tkinter.Button(bts_win, text="Sixes hit", command=six, bg='#1279ff', fg='#FFDF00') 
    six_bt.config(width=10, font = ('italic bold', 20, 'underline italic bold') )  
    six_bt.place(x=20,y=260)

    blw_bt = tkinter.Button(bts_win, text="Balls played", command=bowl_played, bg='#1279ff', fg='#FFDF00') 
    blw_bt.config(width=10, font = ('italic bold', 20, 'underline italic bold') )  
    blw_bt.place(x=220,y=260)  

    run_bt = tkinter.Button(bts_win, text="Runs scored", command=total_runs, bg='#1279ff', fg='#FFDF00') 
    run_bt.config(width=10, font = ('italic bold', 20, 'underline italic bold') )  
    run_bt.place(x=420,y=260)  

    four_bt = tkinter.Button(bts_win, text="Fours hit", command=four, bg='#1279ff', fg='#FFDF00') 
    four_bt.config(width=10, font = ('italic bold', 20, 'underline italic bold') )  
    four_bt.place(x=20,y=360)  

    cgt_bt = tkinter.Button(bts_win, text="Caught out", command=caught, bg='#1279ff', fg='#FFDF00') 
    cgt_bt.config(width=10, font = ('italic bold', 20, 'underline italic bold') )  
    cgt_bt.place(x=220,y=360)  

    bld_bt = tkinter.Button(bts_win, text="Bowled out", command=bowled, bg='#1279ff', fg='#FFDF00') 
    bld_bt.config(width=10, font = ('italic bold', 20, 'underline italic bold') )  
    bld_bt.place(x=420,y=360)  

    rnot_bt = tkinter.Button(bts_win, text="Runout", command=runout, bg='#1279ff', fg='#FFDF00') 
    rnot_bt.config(width=10, font = ('italic bold', 20, 'underline italic bold') )  
    rnot_bt.place(x=20,y=460)  

    lbw_bt = tkinter.Button(bts_win, text="LBW", command=lbw, bg='#1279ff', fg='#FFDF00') 
    lbw_bt.config(width=10, font = ('italic bold', 20, 'underline italic bold') )  
    lbw_bt.place(x=220,y=460)  

    cgbd_bt = tkinter.Button(bts_win, text="Caught and\n Bowled", command=cgt_bld, bg='#1279ff', fg='#FFDF00') 
    cgbd_bt.config(width=10, font = ('italic bold', 20, 'underline italic bold') )  
    cgbd_bt.place(x=420,y=460)  

    stmp_bt = tkinter.Button(bts_win, text="Stumped", command=stump, bg='#1279ff', fg='#FFDF00') 
    stmp_bt.config(width=10, font = ('italic bold', 20, 'underline italic bold') )  
    stmp_bt.place(x=220,y=560)  



bts_bt = tkinter.Button(window, text="Show \nBatsman Stats", command=bts_win, bg='#1279ff', fg='#FFDF00') 
bts_bt.config(width=15, font = ('italic bold', 20, 'underline italic bold') )  
bts_bt.place(x=50,y=260)  


def blw_win():
    blw_win = tkinter.Tk()
    blw_win.title("Bowler Stats")
    blw_win.geometry('650x650')
    blw_win.config(background = "#85aff2")
    frame = tkinter.Frame(blw_win, bg='#FFDF00', bd=20,relief=tkinter.GROOVE)
    frame.pack()
    titl = tkinter.Label(frame, text='***Bowler Stats***', bg='white', fg='#1279ff')
    titl.config(font = ('Arial Black', 20, 'underline italic'))
    titl.pack()

    df1=pd.read_csv('deliveries.csv')

    #TO CREATE LIST OF BOWLER
    s1=set()
    for i in range (0,179078):
        s1.add(df1.bowler[i])
    blw_lst=list(s1)
    blw_lst.sort()

    frame = tkinter.Frame(blw_win, bg='#FFDF00', bd=20,relief=tkinter.GROOVE)
    frame.place(x=33,y=110)
    sel_blw = tkinter.Label(frame, text='  Select Bowler  ', bg='white', fg='#1279ff')
    sel_blw.config(font = ('Arial Black', 20, 'underline italic'))
    sel_blw.pack()

    menu = ttk.Combobox(blw_win, value=blw_lst)
    menu.current(0)
    menu.config(width=42,height=20)
    menu.bind("<<ComboboxSelected>>")
    #menu["menu"].config(bg="#1279ff")
    menu.place(x=28,y=210)

    def reset():
        frame = tkinter.Frame(blw_win, bg='#FFDF00', bd=20,relief=tkinter.GROOVE)
        frame.place(x=380,y=120)
        rslt_lbl = tkinter.Label(frame, text='          \t        ', bg='white', fg='#1279ff')
        rslt_lbl.config(font = ('Arial Black', 20))
        rslt_lbl.pack()

    def show_result(result):
        rslt_lbl = tkinter.Label(blw_win, text='RESULT:-{}'.format(result), bg='white', fg='#1279ff')
        rslt_lbl.config(font = ('Arial Black', 20, 'underline italic'))
        rslt_lbl.place(x=400,y=140)
 
    def wicket():
        '''to calculate no. the no. of wicket taken by player in whole ipl'''

        ent_blw=menu.get()
        boler=df1.bowler==ent_blw
        wicktlb=df1.dismissal_kind=='lbw'
        wicktcgt=df1.dismissal_kind=='caught'
        wicktbld=df1.dismissal_kind=='bowled'
        wicktcgtbld=df1.dismissal_kind=='caught and bowled'
        wicktstmp=df1.dismissal_kind=='stumped'
        totalwikt=df1[boler & wicktlb].match_id.count()+df1[boler & wicktbld].match_id.count()+df1[boler & wicktcgt].match_id.count()+df1[boler & wicktcgtbld].match_id.count()+df1[boler & wicktstmp].match_id.count()
        result = (totalwikt)
        reset()
        show_result(result)

    def bowl_bowled():
        '''to calculate no. of bowl bowled by a bowler in whole ipl'''

        ent_blw=menu.get()
        boler=df1.bowler==ent_blw
        scor=df1.extra_runs==0
        case=(boler & scor)
        result= (df1[case].match_id.count())
        reset()
        show_result(result)

    def total_runs_given():
        '''to calculate runs given by a bowler in whole ipl'''

        ent_blw=menu.get()
        boler=df1.bowler==ent_blw
        scor1=df1.batsman_runs==1
        scor2=df1.batsman_runs==2
        scor3=df1.batsman_runs==3
        scor4=df1.batsman_runs==4
        scor6=df1.batsman_runs==6
        totalscor=df1[boler & scor1].match_id.count()+(2*df1[boler & scor2].match_id.count())+(3*df1[boler & scor3].match_id.count())+(4*df1[boler & scor4].match_id.count())+(6*df1[boler & scor6].match_id.count())
        result= (totalscor)
        reset()
        show_result(result)

    def six_given():
        '''to calculate no. of sixes given by a bowler in whole ipl'''

        ent_blw=menu.get()
        scor=df1.batsman_runs==6
        boler=df1.bowler==ent_blw
        case=(scor & boler)
        n=df1[case].count()
        result=(n.match_id)
        reset()
        show_result(result)

    def caught_tken():
        '''to find how many time particular bowler got caught wickets in whole ipl'''

        ent_blw=menu.get()
        boler=df1.bowler==ent_blw
        wickt=df1.dismissal_kind=='caught'
        case=(boler & wickt)
        n=df1[case].count()
        result= (n.match_id)
        reset()
        show_result(result)

    def bowled_tken():
        '''to find how many time particular bowler got bowled in whole ipl'''

        ent_blw=menu.get()
        boler=df1.bowler==ent_blw
        wickt=df1.dismissal_kind=="bowled"
        case=(boler & wickt)
        n=df1[case].count()
        result= (n.match_id)
        reset()
        show_result(result)

    def lbw_tken():
        '''to find how many time particular bowler got LBW in whole ipl'''

        ent_blw=menu.get()
        boler=df1.bowler==ent_blw
        wickt=df1.dismissal_kind=="lbw"
        case=(boler & wickt)
        n=df1[case].count()
        result= (n.match_id)
        reset()
        show_result(result)

    def cgt_bld_tken():
        '''to find how many time particular bowler got caught and bowled in whole ipl'''

        ent_blw=menu.get()
        boler=df1.bowler==ent_blw
        wickt=df1.dismissal_kind=="caught and bowled"
        case=(boler & wickt)
        n=df1[case].count()
        result= (n.match_id)
        reset()
        show_result(result)

    def stump_tken():
        '''to find how many time particular bowler got stumped in whole ipl'''

        ent_blw=menu.get()
        boler=df1.bowler==ent_blw
        wickt=df1.dismissal_kind=="stumped"
        case=(boler & wickt)
        n=df1[case].count()
        result= (n.match_id)
        reset()
        show_result(result)

    six_bt = tkinter.Button(blw_win, text="Sixes given", command=six_given, bg='#1279ff', fg='#FFDF00') 
    six_bt.config(width=10, font = ('italic bold', 20, 'underline italic bold') )  
    six_bt.place(x=20,y=260)

    blw_bt = tkinter.Button(blw_win, text="Balls Bowled", command=bowl_bowled, bg='#1279ff', fg='#FFDF00') 
    blw_bt.config(width=10, font = ('italic bold', 20, 'underline italic bold') )  
    blw_bt.place(x=220,y=260)  

    run_bt = tkinter.Button(blw_win, text="Runs Given", command=total_runs_given, bg='#1279ff', fg='#FFDF00') 
    run_bt.config(width=10, font = ('italic bold', 20, 'underline italic bold') )  
    run_bt.place(x=420,y=260)  

    cgt_bt = tkinter.Button(blw_win, text="Caught out", command=caught_tken, bg='#1279ff', fg='#FFDF00') 
    cgt_bt.config(width=10, font = ('italic bold', 20, 'underline italic bold') )  
    cgt_bt.place(x=20,y=360)  

    bld_bt = tkinter.Button(blw_win, text="Bowled out", command=bowled_tken, bg='#1279ff', fg='#FFDF00') 
    bld_bt.config(width=10, font = ('italic bold', 20, 'underline italic bold') )  
    bld_bt.place(x=220,y=360)  

    lbw_bt = tkinter.Button(blw_win, text="LBW", command=lbw_tken, bg='#1279ff', fg='#FFDF00') 
    lbw_bt.config(width=10, font = ('italic bold', 20, 'underline italic bold') )  
    lbw_bt.place(x=420,y=360)  

    cgbd_bt = tkinter.Button(blw_win, text="Caught and\n Bowled", command=cgt_bld_tken, bg='#1279ff', fg='#FFDF00') 
    cgbd_bt.config(width=10, font = ('italic bold', 20, 'underline italic bold') )  
    cgbd_bt.place(x=20,y=460)  

    stmp_bt = tkinter.Button(blw_win, text="Stumped", command=stump_tken, bg='#1279ff', fg='#FFDF00') 
    stmp_bt.config(width=10, font = ('italic bold', 20, 'underline italic bold') )  
    stmp_bt.place(x=420,y=460)

    wkt_bt = tkinter.Button(blw_win, text="wickets", command=wicket, bg='#1279ff', fg='#FFDF00') 
    wkt_bt.config(width=10, font = ('italic bold', 20, 'underline italic bold') )  
    wkt_bt.place(x=220,y=470)

blw_bt = tkinter.Button(window, text="Show \nBowler Stats", command=blw_win, bg='#1279ff', fg='#FFDF00') 
blw_bt.config(width=15 ,font = ('italic bold', 20, 'underline italic bold') )  
blw_bt.place(x=400,y=260)


def fld_win():

    fld_win = tkinter.Tk()
    fld_win.title("fielder Stats")
    fld_win.geometry('650x650')
    fld_win.config(background = "#85aff2")
    frame = tkinter.Frame(fld_win, bg='#FFDF00', bd=20,relief=tkinter.GROOVE)
    frame.pack(pady='15')
    titl = tkinter.Label(frame, text='***Fielder Stats***', bg='white', fg='#1279ff')
    titl.config(font = ('Arial Black', 20, 'underline italic'))
    titl.pack()

    df1=pd.read_csv('deliveries.csv')

    #TO CREATE LIST OF FIELDERS
    s1=set()
    for i in range (0,179078):
        s1.add(df1.fielder[i])
    fld_lst=list(s1)

    frame = tkinter.Frame(fld_win, bg='grey', bd=20,relief=tkinter.GROOVE)
    frame.place(x=36,y=130)
    sel_fld = tkinter.Label(frame, text='  Select Fielder  ', bg='white', fg='#1279ff')
    sel_fld.config(font = ('Arial Black', 20, 'underline italic'))
    sel_fld.pack()

    menu = ttk.Combobox(fld_win, value=fld_lst)
    menu.current(0)
    menu.config(width=42,height=20)
    menu.bind("<<ComboboxSelected>>")
    #menu["menu"].config(bg="#1279ff")
    menu.place(x=30,y=230)

    def reset():
        frame = tkinter.Frame(fld_win, bg='red', bd=20,relief=tkinter.GROOVE)
        frame.place(x=380,y=120)
        rslt_lbl = tkinter.Label(frame, text='          \t        ', bg='white', fg='#1279ff')
        rslt_lbl.config(font = ('Arial Black', 20))
        rslt_lbl.pack()

    def show_result(result):
        rslt_lbl = tkinter.Label(fld_win, text='RESULT:-{}'.format(result), bg='white', fg='#1279ff')
        rslt_lbl.config(font = ('Arial Black', 20, 'underline italic'))
        rslt_lbl.place(x=400,y=140)
 
    def wicket_contribution():
        '''to calculate no. the no. of wicket contribution given by player in whole ipl'''

        ent_fld=menu.get()
        fildr=df1.fielder==ent_fld
        wicktcgt=df1.dismissal_kind=='caught'
        wicktrnot=df1.dismissal_kind=='run out'
        wicktstmp=df1.dismissal_kind=='stumped'
        totalwikt=df1[fildr & wicktcgt].match_id.count()+df1[fildr & wicktrnot].match_id.count()+df1[fildr & wicktstmp].match_id.count()
        result = (totalwikt)
        reset()
        show_result(result)

    def caught_tken():
        '''to find how many catches taken by particular fielder in whole ipl'''

        ent_fld=menu.get()
        fildr=df1.fielder==ent_fld
        wickt=df1.dismissal_kind=="caught"
        case=(fildr & wickt)
        n=df1[case].count()
        result = (n.match_id)
        reset()
        show_result(result)


    def runout_tken():
        '''to find how many runout done by particular fielder in whole ipl'''

        ent_fld=menu.get()
        fildr=df1.fielder==ent_fld
        wickt=df1.dismissal_kind=="run out"
        case=(fildr & wickt)
        n=df1[case].count()
        result = (n.match_id)
        reset()
        show_result(result)

    def stump_tken():
        '''to find how many stumpes taken by particular wicketkepeer in whole ipl'''

        ent_fld=menu.get()
        fildr=df1.fielder==ent_fld
        wickt=df1.dismissal_kind=="stumped"
        case=(fildr & wickt)
        n=df1[case].count()
        result = (n.match_id)
        reset()
        show_result(result)

 
    cgt_bt = tkinter.Button(fld_win, text=" Catches taken ", command=caught_tken, bg='#1279ff', fg='#FFDF00') 
    cgt_bt.config(width=10, font = ('italic bold', 20, 'italic bold') )  
    cgt_bt.place(x=20,y=360)  

    stmp_bt = tkinter.Button(fld_win, text=" Stumped ", command=stump_tken, bg='#1279ff', fg='#FFDF00') 
    stmp_bt.config(width=10, font = ('italic bold', 20) )  
    stmp_bt.place(x=220,y=360)

    rnot_bt = tkinter.Button(fld_win, text=" Run out ", command=runout_tken, bg='#1279ff', fg='#FFDF00') 
    rnot_bt.config(width=10, font = ('italic bold', 20, 'underline italic bold') )  
    rnot_bt.place(x=420,y=360)

    ctrb_bt = tkinter.Button(fld_win, text=" Wicket contr ", command=wicket_contribution, bg='#1279ff', fg='#FFDF00') 
    ctrb_bt.config(width=10, font = ('italic bold', 20) )  
    ctrb_bt.place(x=220,y=460)  


fld_bt = tkinter.Button(window, text="Show \nfielder Stats", command=fld_win, bg='#1279ff', fg='#FFDF00') 
fld_bt.config(width=15 ,font = ('italic bold', 20, 'underline italic bold') )  
fld_bt.place(x=750,y=260)
                          
    
window.mainloop()



