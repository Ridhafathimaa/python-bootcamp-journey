bank = {
    56458: {
        "profile": {
            "username": "irfan",
            "full_name": {
                "first": "Irfan",
                "last": "K"
            },
            "contact": {
                "phone": ["+91-9876543210"],
                "email": ["irfan@example.com"]
            }
        },
        "security": {
            "pin": 8945,
            "login_history": [
                {"date": "2026-06-01", "device": "mobile"},
                {"date": "2026-06-03", "device": "laptop"}
            ]
        },
        "account": {
            "balance": 72000,
            "currency": "INR",
            "linked_cards": [
                {"type": "debit", "last4": "1234"},
                {"type": "credit", "last4": "5678"}
            ]
        },
        "transactions": [
            ["deposit", 5000, "2026-05-30"],
            ["withdraw", 2000, "2026-06-02"]
        ]
    },

    485965: {
        "profile": {
            "username": "alice",
            "full_name": {
                "first": "Alice",
                "last": "Johnson"
            },
            "contact": {
                "phone": ["+91-9123456780"],
                "email": ["alice@example.com"]
            }
        },
        "security": {
            "pin": 8745,
            "login_history": [
                {"date": "2026-06-02", "device": "tablet"},
                {"date": "2026-06-03", "device": "mobile"}
            ]
        },
        "account": {
            "balance": 98000,
            "currency": "INR",
            "linked_cards": [
                {"type": "debit", "last4": "1111"}
            ]
        },
        "transactions": [
            ["deposit", 10000, "2026-06-01"],
            ["transfer", 3000, "2026-06-03"]
        ]
    },

    748596: {
        "profile": {
            "username": "sajwa",
            "full_name": {
                "first": "Sajwa",
                "last": "M"
            },
            "contact": {
                "phone": ["+91-9988776655"],
                "email": ["sajwa@example.com"]
            }
        },
        "security": {
            "pin": 7895,
            "login_history": [
                {"date": "2026-06-01", "device": "desktop"}
            ]
        },
        "account": {
            "balance": 120000,
            "currency": "INR",
            "linked_cards": [
                {"type": "debit", "last4": "2222"},
                {"type": "debit", "last4": "3333"}
            ]
        },
        "transactions": [
            ["withdraw", 7000, "2026-06-02"],
            ["deposit", 15000, "2026-06-03"]
        ]
    }
}
new_deposit = int(input("Enter the deposited amount: "))
bank[748596]["transactions"].append( ["deposit", new_deposit, "2026-06-05"])
bank[748596]["account"]["balance"] += new_deposit
print("Balance:", bank[748596]["account"]["balance"])
print("Transactions:", bank[748596]["transactions"])