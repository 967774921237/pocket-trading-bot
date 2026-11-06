import random
def get_balance_demo():
    return {"real": 4297.95, "demo": 53161.67, "tokens": 5407}
def generate_signal(symbol="CSCO OTC"):
    trend = random.choice(["BEARISH","BULLISH"])
    rsi = random.randint(20,80)
    price = round(random.uniform(105.97,105.99),3)
    return f"{'🐻 BEARISH SETUP' if trend=='BEARISH' else '🐂 BULLISH SETUP'}\nالسعر: {price} RSI: {rsi}\n☑️ Smart Scaling"
