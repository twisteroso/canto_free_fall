import requests, time

def canto_free_fall():
    print("Canto — Free-Fall Detector: > $3M withdrawn from Note (native USDT) in one tx")
    seen = set()
    while True:
        # Canto Note contract (native USDT/USDC on Canto)
        r = requests.get("https://cantoscan.com/api?module=account&action=txlist"
                        "&address=0x9f4d8e6e8e6a8f8d8a8f8d8a8f8d8a8f8d8a8f8d&sort=desc")
        for tx in r.json().get("result", [])[:30]:
            h = tx["hash"]
            if h in seen: continue
            seen.add(h)

            # Withdraw from Note = burning Note to get real USDT/USDC back
            if "0x2e1a7d4d" not in tx.get("input", "")[:10]: continue  # burn function selector

            value = int(tx["value"]) / 1e6  # Note uses 6 decimals
            if value >= 3_000_000:  # > $3M leaving Canto's "free banking" model
                print(f"FREE FALL INITIATED\n"
                      f"${value:,.0f} USDT/USDC withdrawn from Canto Note\n"
                      f"Wallet: {tx['from']}\n"
                      f"Tx: https://cantoscan.com/tx/{h}\n"
                      f"→ Someone just rejected the 'free banking' dream\n"
                      f"→ Real stablecoins leaving the Cosmos chain forever\n"
                      f"{'-'*70}")
        time.sleep(3.1)

if __name__ == "__main__":
    canto_free_fall()
