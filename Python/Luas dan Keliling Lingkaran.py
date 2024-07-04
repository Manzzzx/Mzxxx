print ("========== MENGHITUNG KELILING ==========")

r = float(input("Masukan nilai jari-jari :"))
phi = 3.14
diameter = 2*r

# menghitung Luas
Luas = phi*r*r
# menghitung keliling
Keliling = 2*diameter

print("\nLuas Lingkaran         =", str("%.2f" % Luas))
print("Keliling Lingkaran     =", str("%.2f" % Keliling))