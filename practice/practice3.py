from googletrans import Translator

translator=Translator()
phrase=input("책을 읽으며 인상 깊었던 구절을 적어주세요: ")
detected=translator.detect(phrase)
result1=translator.translate(phrase,"en","ko")
result2=translator.translate(phrase,"de","ko")

print("========== 번역 결과 ==========")
print(f"입력어 - {detected.lang} : {phrase}")
print(f"번역어1 - en : {result1.text} ")
print(f"번역어2 - de : {result2.text}  ")