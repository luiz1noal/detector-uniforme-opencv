import cv2

# Carrega as imagens
img_color = cv2.imread("3pv.jpg")
if img_color is None:
    raise SystemExit("Erro: imagem base '3pv.jpg' não encontrada.")
logo = cv2.imread("logoStarB.jpg")
if logo is None:
    raise SystemExit("Erro: logo 'logoStarB.jpg' não encontrada.")

# Converte para escala de cinza
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
logo_gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)

# Cria o detector ORB
orb = cv2.ORB_create(1000)  # número de pontos de interesse

# Extrai keypoints e descritores
kp1, des1 = orb.detectAndCompute(logo_gray, None)
kp2, des2 = orb.detectAndCompute(img_gray, None)

# Cria o matcher (comparador)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Faz a correspondência
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)

# Define um limite para o que é considerado “bom”
num_bons = sum(1 for m in matches if m.distance < 60)

print(f"Total de matches: {len(matches)}, bons matches: {num_bons}")

# Se há muitos matches bons, provavelmente o logo foi detectado
if num_bons > 25:
    print("✅ Logo detectado!")
    # Desenha os matches para visualizar
    resultado = cv2.drawMatches(logo, kp1, img_color, kp2, matches[:50], None, flags=2)
    cv2.imshow("Matches ORB", resultado)
else:
    print("❌ Logo não detectado (poucos pontos em comum).")
    resultado = cv2.drawMatches(logo, kp1, img_color, kp2, matches[:30], None, flags=2)
    cv2.imshow("Matches ORB", resultado)

cv2.waitKey(0)
cv2.destroyAllWindows()
