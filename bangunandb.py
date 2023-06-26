import sqlite3

# Create a connection to the database
conn = sqlite3.connect('bangunandb.sqlite')
cursor = conn.cursor()

# Create the Produk table
cursor.execute('''CREATE TABLE Produk (
                    id_produk INTEGER PRIMARY KEY AUTOINCREMENT,
                    nama_produk TEXT,
                    jenis TEXT,
                    satuan TEXT
                )''')


# Create the Penjualan table
cursor.execute('''CREATE TABLE Penjualan (
                    id_penjualan INTEGER PRIMARY KEY AUTOINCREMENT,
                    nama_pembeli TEXT,
                    tanggal_jual DATE,
                    tanggal_tempo DATE,
                    pembayaran REAL
                )''')

# Create the DetailJual table
cursor.execute('''CREATE TABLE DetailJual (
                    id_detailjual INTEGER PRIMARY KEY,
                    id_penjualan INTEGER,
                    id_produk INTEGER,
                    harga_jual REAL,
                    jumlah INTEGER,
                    FOREIGN KEY (id_penjualan) REFERENCES Penjualan (id_penjualan),
                    FOREIGN KEY (id_produk) REFERENCES Produk (id_produk)
                )''')

# Create the Supplier table
cursor.execute('''CREATE TABLE Supplier (
                    id_supplier INTEGER PRIMARY KEY AUTOINCREMENT,
                    nama_supplier TEXT,
                    alamat TEXT,
                    nomor_hp TEXT
                )''')

# Create the Pembelian table
cursor.execute('''CREATE TABLE Pembelian (
                    id_pembelian INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_supplier INTEGER,
                    tanggal_beli DATE,
                    tanggal_tempo DATE,
                    pembayaran REAL,
                    FOREIGN KEY (id_supplier) REFERENCES Supplier (id_supplier)
                )''')

# Create the DetailBeli table
cursor.execute('''CREATE TABLE DetailBeli (
                    id_detailbeli INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_pembelian INTEGER,
                    id_produk INTEGER,
                    harga_beli REAL,
                    jumlah_produk INTEGER,
                    FOREIGN KEY (id_pembelian) REFERENCES Pembelian (id_pembelian),
                    FOREIGN KEY (id_produk) REFERENCES Produk (id_produk)
                )''')

# Create the Utang table
cursor.execute('''CREATE TABLE Utang (
                    id_utang INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_pembelian INTEGER,
                    tanggal_bayar DATE,
                    pembayaran REAL,
                    FOREIGN KEY (id_pembelian) REFERENCES Pembelian (id_pembelian)
                )''')

# Create the Piutang table
cursor.execute('''CREATE TABLE Piutang (
                    id_piutang INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_penjualan INTEGER,
                    tanggal_bayar DATE,
                    pembayaran REAL,
                    FOREIGN KEY (id_penjualan) REFERENCES Penjualan (id_penjualan)
                )''')

# Create the Penerimaan table
cursor.execute('''CREATE TABLE Transaksi (
                    id_transaksi INTEGER PRIMARY KEY AUTOINCREMENT,
                    tanggal_transaksi DATE,
                    penerima TEXT,
                    jenis TEXT,
                    keterangan TEXT,
                    pembayaran REAL
                )''')

# Create the Pengeluaran table
cursor.execute('''CREATE TABLE Pembayaran (
                    id_pembayaran INTEGER PRIMARY KEY AUTOINCREMENT,
                    tanggal_transaksi DATE,
                    penerima TEXT,
                    jenis TEXT,
                    keterangan TEXT,
                    pembayaran REAL
                )''')

# Commit the changes and close the connection
conn.commit()
conn.close()