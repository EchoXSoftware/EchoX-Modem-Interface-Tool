import webbrowser
import tkinter as tk

# IP adresini dosyadan oku
try:
    with open("saved_ip.txt", "r") as f:
        ip_address = f.read()
except FileNotFoundError:
    ip_address = "" # dosya bulunamazsa boş bir değer atanır

window = tk.Tk()
window.geometry("540x540")

if ip_address:
    # IP adresi dosyada bulunursa tarayıcıda açar ve pencerede gösterir
    webbrowser.open_new_tab("http://" + ip_address)
    exit()
    ip_label = tk.Label(window, text=ip_address)
else:
    # IP adresi dosyada bulunamazsa pencerede uyarı mesajı gösterir
    ip_label = tk.Label(window, text="Please enter IP address")
ip_label.pack()

def change_ip():
    global ip_address
    ip_address = input_field.get() # alınan ip adresi değişkenine atanır
    ip_label.config(text=ip_address)
    webbrowser.open_new_tab("http://" + ip_address)

    # IP adresini dosyaya kaydet
    with open("saved_ip.txt", "w") as f:
        f.write(ip_address)

    # kodu kapat
    window.quit()

# girdi alanının oluşturulması
input_field = tk.Entry(window)
input_field.pack()

change_button = tk.Button(window, text="Change IP", command=change_ip)
change_button.pack()

window.mainloop()