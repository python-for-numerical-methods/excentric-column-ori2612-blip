   def column_stress_error(L, E, A, r, c, e, sigma_allow):
    # פרמטרים לדוגמה
   # A, E, L, r, e, c = 5000, 200000, 3000, 50, 20, 100
    # נוסחת הסקנט
    sec_term = 1 / np.cos((L/(2*r)) * np.sqrt(P/(E*A)))
    sigma_max = (P/A) * (1 + (e*c/r**2) * sec_term)
    return sigma_max - sigma_allow
