import lib.technical_analysis as tech_ana
import ta
import pandas



def change(series, length=1):
    return series[0] - series[length]


def execute(bins):
    hlc3 = (bins["high"] + bins["low"] + bins["close"]) / 3

    up = rma(max(change(hlc3), 0), 6)
    down = rma(-min(change(hlc3), 0), 6)


    fastrsi = ud_cal(up, down)
    Buy_IN = close < open and abs(close - open) > ema(abs(close - open), 5) * 1.1 and sma(fastrsi, 4) < 20
    Sell_IN = open < close and abs(close - open) > ema(abs(close - open), 5) * 1.1 and sma(fastrsi, 4) > 80
    Buy_Close = fastrsi > 20
    Sell_Close = fastrsi < 80
    switch = 0
    setA = 0
    setB = 0
if (Buy_IN and (switch[1] == 0))
    switch: = 1
    setA: = 1
    setB: = 0
else
    if (Buy_Close and (switch[1] == 1))
        switch: = 0
        setA: = 0
        setB: = 1
    else
        switch: = nz(switch[1], 0)
        setA: = 0
        setB: = 0
switch2 = 0
setC = 0
setD = 0
if (Sell_IN and (switch2[1] == 0))
    switch2: = 1
    setC: = 1
    setD: = 0
else
    if (Sell_Close and (switch2[1] == 1))
        switch2: = 0
        setC: = 0
        setD: = 1
    else
        switch2: = nz(switch2[1], 0)
        setC: = 0
        setD: = 0
plotshape(setA, title="Buy_IN", style=shape.triangleup, text="Buy_IN", color=green, textcolor=green,
          location=location.belowbar)
plotshape(setC, title="Sell_IN", style=shape.triangledown, text="Sell_IN", color=red, textcolor=red,
          location=location.abovebar)
plotshape(setB, title="Buy_Close", style=shape.triangledown, text="Buy_Close", color=lime, textcolor=lime,
          location=location.abovebar)
plotshape(setD, title="Sell_Close", style=shape.triangleup, text="Sell_Close", color=orange, textcolor=orange,
          location=location.belowbar)

strategy.entry("Long", strategy.long, when=setA)
strategy.entry("Short", strategy.short, when=setC)
strategy.close(id="Long", when=setB)
strategy.close(id="Short", when=setD)

alertcondition(setA, title="Buy_IN", message=",crocodile,BUY,1,LONG")
alertcondition(setC, title="Sell_IN", message=",crocodile,SELL,1,SHORT")
alertcondition(setB, title="Buy_Close", message=",crocodile,SELL,1,LONG_EXIT")
alertcondition(setD, title="Sell_Close", message=",crocodile,BUY,1,SHORT_EXIT")


def ud_cal(up, down):
    if down == 0:
        return 100
    if up == 0:
        return 0
    else:
        return 100 - (100 / (1 + up / down))
