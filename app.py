from modules.upi_checker import check_upi_id

def main():
    print("🔐 UPI Scam Detector")
    while True:
        upi = input("\nEnter UPI ID (or 'exit' to quit): ")
        if upi.lower() == "exit":
            break
        print(check_upi_id(upi))

if __name__ == "__main__":
    main()
