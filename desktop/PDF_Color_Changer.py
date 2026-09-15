import os, tkinter as tk
from tkinter import filedialog, messagebox, colorchooser, ttk
try:
    import fitz
except ImportError:
    raise SystemExit("Install first: pip install pymupdf")

PRESETS={
"Extra Dark Maroon":"#480012","Dark Maroon":"#5A1020",
"Dark Orange":"#C84B00","Deep Dark Green":"#14532D",
"Dark Green":"#1B5E20","Navy Blue":"#123A63","Black":"#000000","Custom…":None}

def rgb(h):
    h=h.strip().lstrip("#")
    if len(h)!=6: raise ValueError("HEX must look like #480012")
    return tuple(int(h[i:i+2],16) for i in (0,2,4))

def lum(r,g,b): return .2126*r+.7152*g+.0722*b

def recolor(data, target, threshold=125):
    d=bytearray(data); tr,tg,tb=target
    for i in range(0,len(d),3):
        r,g,b=d[i:i+3]; L=lum(r,g,b); sat=max(r,g,b)-min(r,g,b)
        # Recolor dark neutral pixels; preserve existing dark/saturated artwork.
        if L<=threshold and not (sat>45 and L>45):
            s=1 if L<threshold*.65 else max(0,min(1,(threshold-L)/threshold))
            d[i]=int(r*(1-s)+tr*s); d[i+1]=int(g*(1-s)+tg*s); d[i+2]=int(b*(1-s)+tb*s)
    return bytes(d)

def convert(src,dst,target,dpi,threshold):
    doc=fitz.open(src); out=fitz.open(); mat=fitz.Matrix(dpi/72,dpi/72)
    for page in doc:
        pix=page.get_pixmap(matrix=mat,colorspace=fitz.csRGB,alpha=False,annots=True)
        samples=recolor(pix.samples,target,threshold)
        npix=fitz.Pixmap(fitz.csRGB,pix.width,pix.height,samples,False)
        pg=out.new_page(width=page.rect.width,height=page.rect.height)
        pg.insert_image(pg.rect,pixmap=npix)
    out.save(dst,garbage=4,deflate=True); out.close(); doc.close()

class App:
    def __init__(self,root):
        self.r=root; root.title("PDF Color Changer — Brandex"); root.geometry("610x430"); root.resizable(False,False)
        self.src=tk.StringVar(); self.name=tk.StringVar(value="Extra Dark Maroon")
        self.hex=tk.StringVar(value="#480012"); self.dpi=tk.IntVar(value=300); self.th=tk.IntVar(value=125)
        ttk.Label(root,text="PDF Color Changer",font=("Segoe UI",18,"bold")).pack(anchor="w",padx=16,pady=(18,4))
        ttk.Label(root,text="Change dark/black text, table borders and lines. Wording stays unchanged.").pack(anchor="w",padx=16,pady=(0,12))
        f=ttk.LabelFrame(root,text="1. Choose PDF"); f.pack(fill="x",padx=16,pady=7)
        ttk.Entry(f,textvariable=self.src,width=57).grid(row=0,column=0,padx=10,pady=10)
        ttk.Button(f,text="Browse…",command=self.browse).grid(row=0,column=1,padx=(0,10))
        f=ttk.LabelFrame(root,text="2. Choose color"); f.pack(fill="x",padx=16,pady=7)
        ttk.Label(f,text="Preset:").grid(row=0,column=0,padx=10,pady=10)
        c=ttk.Combobox(f,textvariable=self.name,values=list(PRESETS),state="readonly",width=23); c.grid(row=0,column=1); c.bind("<<ComboboxSelected>>",self.changed)
        ttk.Label(f,text="HEX:").grid(row=0,column=2,padx=8); ttk.Entry(f,textvariable=self.hex,width=11).grid(row=0,column=3)
        ttk.Button(f,text="Pick color…",command=self.pick).grid(row=0,column=4,padx=10)
        f=ttk.LabelFrame(root,text="3. Settings"); f.pack(fill="x",padx=16,pady=7)
        ttk.Label(f,text="Resolution:").grid(row=0,column=0,padx=10,pady=9)
        ttk.Combobox(f,textvariable=self.dpi,values=[150,200,300,400,600],state="readonly",width=7).grid(row=0,column=1)
        ttk.Label(f,text="Darkness threshold:").grid(row=0,column=2,padx=10)
        ttk.Scale(f,from_=70,to=180,variable=self.th,orient="horizontal",length=140).grid(row=0,column=3)
        self.status=tk.StringVar(value="Ready.")
        ttk.Label(root,textvariable=self.status).pack(anchor="w",padx=18,pady=5)
        ttk.Button(root,text="CONVERT PDF",command=self.go).pack(fill="x",padx=18,pady=10,ipady=8)
        ttk.Label(root,text="Recommended for your TM-11: Extra Dark Maroon #480012 • Deep Dark Green #14532D",wraplength=570).pack(anchor="w",padx=18)

    def browse(self):
        x=filedialog.askopenfilename(filetypes=[("PDF files","*.pdf")])
        if x:self.src.set(x)
    def changed(self,e=None):
        if PRESETS[self.name.get()]: self.hex.set(PRESETS[self.name.get()])
    def pick(self):
        _,h=colorchooser.askcolor(initialcolor=self.hex.get())
        if h:self.hex.set(h.upper()); self.name.set("Custom…")
    def go(self):
        src=self.src.get().strip()
        if not os.path.isfile(src): return messagebox.showwarning("Select PDF","Please select a PDF first.")
        try:t=rgb(self.hex.get())
        except Exception as e:return messagebox.showerror("Color error",str(e))
        base=os.path.splitext(src)[0]
        dst=filedialog.asksaveasfilename(initialfile=os.path.basename(base+"_COLOR_CHANGED.pdf"),defaultextension=".pdf",filetypes=[("PDF files","*.pdf")])
        if not dst:return
        try:
            self.status.set("Processing…"); self.r.update_idletasks()
            convert(src,dst,t,int(self.dpi.get()),int(float(self.th.get())))
            self.status.set("Done."); messagebox.showinfo("Finished","Converted successfully.\n\n"+dst)
        except Exception as e: self.status.set("Error."); messagebox.showerror("Failed",str(e))

root=tk.Tk(); App(root); root.mainloop()
