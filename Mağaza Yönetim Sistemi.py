import tkinter as tk
from tkinter import ttk, messagebox

class MagazaUygulamasi:
    def __init__(self, root):
        self.magaza = Magaza()
        self.extra_giderler = [] 
        root.title("") # Pencere başlığını
    
        title_label = tk.Label(root, text="Mağaza Yönetim Sistemi", font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="#FFFFFF")
        title_label.pack(fill="x", pady=10)

        root.geometry("600x370")  # Pencere boyutu
        root.configure(bg="#ADD8E6") # Pencere arka plan rengi

        # Treeview için başlık
        self.tree = ttk.Treeview(root)
        self.tree["columns"] = ("Ad", "Fiyat", "Model", "Tarih", "Adet", "Kategori")
        self.tree.heading("#0", text="ID")
        self.tree.heading("Ad", text="Ürün Adı")
        self.tree.heading("Fiyat", text="Fiyat")
        self.tree.heading("Model", text="Model")
        self.tree.heading("Tarih", text="Tarih")
        self.tree.heading("Adet", text="Adet")
        self.tree.heading("Kategori", text="Kategori")
        self.tree.column("#0", stretch=tk.NO, minwidth=0, width=0)
        self.tree.column("Ad", anchor=tk.CENTER, width=100)
        self.tree.column("Fiyat", anchor=tk.CENTER, width=100)
        self.tree.column("Model", anchor=tk.CENTER, width=100)
        self.tree.column("Tarih", anchor=tk.CENTER, width=100)
        self.tree.column("Adet", anchor=tk.CENTER, width=100)
        self.tree.column("Kategori", anchor=tk.CENTER, width=100)
        self.tree.pack(pady=10)

        # Butonlar için çerçeve oluştur
        button_frame = ttk.Frame(root)
        button_frame.pack(pady=10)

        btn_ekle = ttk.Button(button_frame, text="Ürün Ekle", command=self.urun_ekle_pencere)
        btn_ekle.grid(row=0, column=0, padx=10)

        btn_sat = ttk.Button(button_frame, text="Ürün Sat", command=self.urun_sat_pencere)
        btn_sat.grid(row=0, column=1, padx=10)

        btn_gider_ekle = ttk.Button(button_frame, text="Extra Gider Ekle", command=self.extra_gider_ekle_pencere)
        btn_gider_ekle.grid(row=0, column=2, padx=10)

        btn_rapor = ttk.Button(button_frame, text="Rapor Al", command=self.rapor_al)
        btn_rapor.grid(row=0, column=3, padx=10)
        # Butonların stilini özelleştirmek için bir ttk.Style objesi
        
        style = ttk.Style()
        style.configure("TButton", foreground="#355E3B", background="#808080", font=("Helvetica", 10, "bold"))


    def urun_ekle_pencere(self):
        pencere = tk.Toplevel()
        pencere.title("Ürün Ekle")

        label_ad = ttk.Label(pencere, text="Ürün Adı:")
        label_ad.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        entry_ad = ttk.Entry(pencere)
        entry_ad.grid(row=0, column=1, padx=5, pady=5)

        label_fiyat = ttk.Label(pencere, text="Fiyat:")
        label_fiyat.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

        entry_fiyat = ttk.Entry(pencere)
        entry_fiyat.grid(row=1, column=1, padx=5, pady=5)

        label_model = ttk.Label(pencere, text="Model:")
        label_model.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

        entry_model = ttk.Entry(pencere)
        entry_model.grid(row=2, column=1, padx=5, pady=5)

        label_tarih = ttk.Label(pencere, text="Tarih:")
        label_tarih.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

        entry_tarih = ttk.Entry(pencere)
        entry_tarih.grid(row=3, column=1, padx=5, pady=5)

        label_adet = ttk.Label(pencere, text="Adet:")
        label_adet.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)

        entry_adet = ttk.Entry(pencere)
        entry_adet.grid(row=4, column=1, padx=5, pady=5)

        label_kategori = ttk.Label(pencere, text="Kategori:")
        label_kategori.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)

        entry_kategori = ttk.Entry(pencere)
        entry_kategori.grid(row=5, column=1, padx=5, pady=5)

        btn_kaydet = ttk.Button(pencere, text="Kaydet", command=lambda: self.urun_ekle(
            entry_ad.get(),
            float(entry_fiyat.get()),
            entry_model.get(),
            entry_tarih.get(),
            int(entry_adet.get()),
            entry_kategori.get()
        ))
        btn_kaydet.grid(row=6, column=0, columnspan=2, pady=10)
    
    def urun_sat_pencere(self):
        if not self.tree.selection():
            messagebox.showwarning("Uyarı", "Lütfen bir ürün seçin.")
            return

        secilen_urun_id = self.tree.selection()[0]
        secilen_urun = self.magaza.urunler[int(secilen_urun_id) - 1]

        pencere = tk.Toplevel()
        pencere.title("Ürün Sat")

        label_adet = ttk.Label(pencere, text=f"Adet (Mevcut Adet: {secilen_urun['Adet']}):")
        label_adet.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        entry_adet = ttk.Entry(pencere)
        entry_adet.grid(row=0, column=1, padx=5, pady=5)

        label_satis_fiyati = ttk.Label(pencere, text="Satış Fiyatı:")
        label_satis_fiyati.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

        entry_satis_fiyati = ttk.Entry(pencere)
        entry_satis_fiyati.grid(row=1, column=1, padx=5, pady=5)

        btn_sat = ttk.Button(pencere, text="Sat", command=lambda: self.urun_sat(
            secilen_urun_id,
            int(entry_adet.get()),
            float(entry_satis_fiyati.get())  # Eklenen satış fiyatı
        ))
        btn_sat.grid(row=2, column=0, columnspan=2, pady=10)

    def extra_gider_ekle_pencere(self):
        pencere = tk.Toplevel()
        pencere.title("Extra Gider Ekle")

        label_aciklama = ttk.Label(pencere, text="Gider Açıklama:")
        label_aciklama.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        entry_aciklama = ttk.Entry(pencere)
        entry_aciklama.grid(row=0, column=1, padx=5, pady=5)

        label_miktar = ttk.Label(pencere, text="Gider Miktarı:")
        label_miktar.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

        entry_miktar = ttk.Entry(pencere)
        entry_miktar.grid(row=1, column=1, padx=5, pady=5)

        btn_ekle = ttk.Button(pencere, text="Ekle", command=lambda: self.extra_gider_ekle(
            entry_aciklama.get(),
            float(entry_miktar.get())
        ))
        btn_ekle.grid(row=2, column=0, columnspan=2, pady=10)

    def extra_gider_ekle(self, aciklama, miktar):
        self.extra_giderler.append({
            'Aciklama': aciklama,
            'Miktar': miktar
        })

    def urun_ekle(self, ad, fiyat, model, tarih, adet, kategori):
        self.magaza.urun_ekle(ad, fiyat, model, tarih, adet, kategori)
        self.guncelle_tree()

    def urun_sat(self, urun_id, satilan_adet,satis_fiyati):
        secilen_urun = self.magaza.urunler[int(urun_id) - 1]

        if satilan_adet > secilen_urun['Adet']:
            messagebox.showwarning("Uyarı", "Satılacak adet, mevcut adetten fazla olamaz.")
            return

        secilen_urun['Adet'] -= satilan_adet
        secilen_urun['SatilanAdet'] += satilan_adet
        secilen_urun['SatisFiyati'] = satis_fiyati  # Yeni eklenen satış fiyatını kaydet
        self.guncelle_tree()

    def rapor_al(self):
        toplam_gelir, toplam_gider, toplamfiyat = self.magaza.toplam_gelir_gider()
        toplam_extra_gider = sum(gider['Miktar'] for gider in self.extra_giderler)
        toplam_gelir = sum(urun['SatisFiyati'] * urun['SatilanAdet'] for urun in self.magaza.urunler)
        # Pop-up penceresi

        alış_fiyatı = sum(urun['Fiyat'] * urun['SatilanAdet'] for urun in self.magaza.urunler)
        rapor_mesaji = f"Toplam Gelir: {toplam_gelir}\nToplam Gider: {toplam_gider+toplam_extra_gider}\n Net Kar-Zarar: {toplam_gelir-alış_fiyatı-toplam_extra_gider }"
        # rapor_mesaji += f"\nToplam Extra Gider: {toplam_extra_gider}"
        messagebox.showinfo("Rapor", rapor_mesaji)

    def guncelle_tree(self):
        for row_id in self.tree.get_children():
            self.tree.delete(row_id)

        for i, urun in enumerate(self.magaza.urunler, 1):
            self.tree.insert("", "end", iid=i, values=(
                urun['Ad'], urun['Fiyat'], urun['Model'], urun['Tarih'], urun['Adet'], urun['Kategori']
            ))

class Magaza:
    def __init__(self):
        self.urunler = []

    def urun_ekle(self, ad, fiyat, model, tarih, adet, kategori):
        self.urunler.append({
            'Ad': ad,
            'Fiyat': fiyat,
            'Model': model,
            'Tarih': tarih,
            'Adet': adet,
            'Kategori': kategori,
            'SatilanAdet': 0  # Initialize sold quantity to 0
        })

    def toplam_gelir_gider(self):
        toplam_gelir = 0
        toplam_gider = 0
        toplamfiyat=0
        for urun in self.urunler:
            toplam_gelir += urun['Fiyat'] * urun['SatilanAdet']
            toplam_gider += urun['Fiyat'] * urun['Adet']
            toplamfiyat += urun['Fiyat']

        return toplam_gelir, toplam_gider,toplamfiyat

if __name__ == "__main__":
    root = tk.Tk()
    uygulama = MagazaUygulamasi(root)
    root.mainloop()