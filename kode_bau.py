"""Contoh kode yang diperbaiki agar lolos Pylint."""


def tambah(angka_pertama, angka_kedua):
    """Menjumlahkan dua angka."""
    return angka_pertama + angka_kedua


def main():
    """Fungsi utama program."""
    hasil = tambah(10, 5)
    print(f"Hasil: {hasil}")


if __name__ == "__main__":
    main()
