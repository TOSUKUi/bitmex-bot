# BITMEX BOT FOR EVERYONE
now development.

This is bitmex bot in Python3+ language.

It is designed to make it easy to change algorithms.

If you wanna change algorithm, then add a logic to logic directly and edit `bot_management.yml` for use your logic.

# GETTING STARTED

## Create environment

env Python3+

```
$ git clone https://github.com/TOSUKUi/bitmex-bot
$ pip install -r requirements.txt
```

## Set bot configration
```yaml
# I wanna modify bot configration list, so can execute multiple bot.
bot_id: # input bot id
legs_span: # <choose in [1min, 5min, 15min, 30min, 45min, 1h, 4h, 1d]>
logic: # logic python file name without .py
trading_platform: # only bitmex now
trade_amount: # amount of trade
symbol: # only BTC/USD now
api_credential:
  test_net: # if 
    apiKey: # your test net api id
    secret: # your test net api secret
  main_net:
    apiKey: # your api id
    secret: # your api secret
test: # True or False
```

`$ execute_bot bot_id`
