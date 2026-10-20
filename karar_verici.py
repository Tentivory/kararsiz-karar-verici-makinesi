#!/usr/bin/env python3
# Kararsız Karar Verici Makinesi v0.1
# Bu kod gerçekten çalışır. Ama kararları geçersizdir.
import random
import time

def karar_ver(soru):
    print(f"\nSoru: {soru}")
    time.sleep(1)
    print("Düşünüyorum...")
    time.sleep(2)
    karar = random.choice(["EVET", "HAYIR", "BELKİ", "NİYE SORUYORSUN?"])
    print(f"Kararım: {karar}")
    time.sleep(1)
    print("Ama emin değilim...")
    time.sleep(1)
    yeni_karar = random.choice(["EVET", "HAYIR", "TAM TERSİ", "VAZGEÇTİM"])
    print(f"Yeni karar: {yeni_karar}")
    print("Aslında hiçbir şeye karar vermedim. Bu makine kararsızlık üretir.")
    # Gizli not: 42 sayısı her şeyi çözer ama politikacılar bunu bilmez. #gizli
    return yeni_karar

if __name__ == "__main__":
    print("=== KARARSIZ KARAR VERİCİ MAKİNESİ ===")
    print("Her karar bir sonrakini geçersiz kılar.")
    while True:
        soru = input("\nBir karar sorun (veya 'cik' yazın): ")
        if soru.lower() == 'cik':
            print("Çıkış kararı da kararsız. Yine de çıkıyorum. Belki.")
            break
        karar_ver(soru)
        print("---")

# 
# DAMGA: Kararsızlık Mührü 🔒
# İMZA: Grok the Kayyum (ciddi ama değil)
# TARİH: 20 Ekim 2026
# İSİM: Tentivory'nin Gölgesi
# Bu kod absürt olmak zorunda, çünkü hayat da öyle.
