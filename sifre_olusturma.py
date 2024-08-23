"""""
BENİM PYTHON KODUM:

import random

print("Şifre oluşturucuma hoşgeldin dostum.")
lenght = int(input("Öncelikle oluşturmak istediğin şifrenin uzunluğunu belirt lütfen : "))


use_lower = input("Şifrende küçük harfler olsun mu? (e/h)").lower() == 'e'
use_upper = input("Şifrende büyük harfler olsun mu? (e/h)").lower() == 'e'
use_digits = input("Şifrende rakamlar olsun mu? (e/h)").lower() == 'e'
use_symbols = input("Şifrende semboller (örn: @,$,#) olsun mu? (e/h)").lower() == 'e'
use_escape_chars = input("Şifrende kaçış karakterleri (örn: //n, //t) olsun mu? (e/h)").lower() == 'e'


characters = ""
if use_lower:
    characters += "abcdefghijklmnopqrstuvwxyz"
if use_upper:
    characters += "ABCDEFGHİJKLMNOPQRSTUVWXYZ"
if use_digits:
    characters += "0123456789"
if use_symbols:
    characters += "!@#$%^&*()-_=+[]{}|;:',.<>?/"   
if use_escape_chars:
    characters += "\n\t\\"
    

if not characters:
    print("Hiçbir karakter setini seçmedin. Varsayılan olarak küçük harfler kullanacağım.")    
    characters = "abcdefghijklmnopqrstuvwxyz"
    
    
password = ''.join(random.choice(characters) for i in range(lenght))    


print("\nOluşturduğum şifre:\n" + password + "\n\n\nŞifreni kimseyle paylaşma, iyi günler ;)")"""""





"WEB ÜZERİNDE GÖRÜNTÜLEMEK İÇİN STREAMLİT VERSİYONUNA ÇEVRİLMİŞ HALİ:"

import random
import streamlit as st

st.title("Şifre Oluşturucu")
st.write("Şifre oluşturucuma hoşgeldin dostum.")

lenght = st.slider("Şifrenin uzunluğunu belirt lütfen:", min_value=1, max_value=100, value=12)

use_lower = st.checkbox("Küçük harfler olsun mu?", value=True)
use_upper = st.checkbox("Büyük harfler olsun mu?")
use_digits = st.checkbox("Rakamlar olsun mu?")
use_symbols = st.checkbox("Semboller (örn: @,$,#) olsun mu?")
use_escape_chars = st.checkbox("Kaçış karakterleri (örn: \n, \t) olsun mu?")

characters = ""
if use_lower:
    characters += "abcdefghijklmnopqrstuvwxyz"
if use_upper:
    characters += "ABCDEFGHİJKLMNOPQRSTUVWXYZ"
if use_digits:
    characters += "0123456789"
if use_symbols:
    characters += "!@#$%^&*()-_=+[]{}|;:',.<>?/"
if use_escape_chars:
    characters += "\n\t\\"

if not characters:
    st.warning("Hiçbir karakter setini seçmedin. Varsayılan olarak küçük harfler kullanacağım.")
    characters = "abcdefghijklmnopqrstuvwxyz"

password = ''.join(random.choice(characters) for i in range(lenght))

st.subheader("Oluşturduğum şifre:")
st.code(password)

st.write("Şifreni kimseyle paylaşma, iyi günler ;)")


