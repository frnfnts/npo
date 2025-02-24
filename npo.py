# 1 認定ＮＰＯ法人等寄附金の額
npo_donation = 0
# 2 ①以外の寄附金の額 (ふるさと納税を含む)
other_donation = 0
num3 = npo_donation + other_donation
# 4 所得金額の合計額
total_income = 0
num5 = int(total_income * 0.4)
num6 = num5 - other_donation
num7 = min(npo_donation, num6)
num8 = max(2000 - num7, 0)
num9 = int((num7 - num8) * 0.4)
# 10 XXXX年分の所得税の額
total_income_tax = 0
num11 = int(total_income_tax * 0.25 / 100) * 100
num12 = num11
num13 = min(num9, num12)

print(f"1\t{npo_donation:,}")
print(f"2\t{other_donation:,}")
print(f"3\t{num3}")
print(f"4\t{total_income:,}")
print(f"5\t{num5:,}")
print(f"6\t{num6:,}")
print(f"7\t{num7:,}")
print(f"8\t{num8:,}")
print(f"9\t{num9:,}")
print(f"10\t{total_income_tax:,}")
print(f"11\t{num11:,}")
print(f"12\t{num12:,}")
print(f"13\t{num13:,}")
