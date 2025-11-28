from app.service.family_codes import FamilyCodesInstance
from app.service.auth import AuthInstance
from app.menus.package import get_packages_by_family
from app.menus.util import clear_screen, pause

def show_family_codes_menu():
    api_key = AuthInstance.api_key
    tokens = AuthInstance.get_active_tokens()

    in_menu = True
    while in_menu:
        clear_screen()
        print("=== Family Codes Saved ===")
        codes = FamilyCodesInstance.list()
        if not codes:
            print("(no family codes saved)")
        else:
            for idx, c in enumerate(codes, start=1):
                name = c.get("name", "")
                ent = "Enterprise" if c.get("is_enterprise", False) else "Consumer"
                print(f"{idx}. {(name) if name else ''}")

        print("---------------------------")
        print("00. Kembali ke menu utama")
        print("Pilih nomor untuk membuka paket dari family code")

        choice = input("Pilihan: ")
        if choice == "00":
            in_menu = False
            return None

        # select by number
        if choice.isdigit():
            idx = int(choice)
            if idx < 1 or idx > len(codes):
                print("Nomor tidak valid.")
                pause()
                continue
            selected = codes[idx - 1]
            get_packages_by_family(selected["family_code"], selected.get("is_enterprise", False))
            in_menu = False
            return None

        print("Pilihan tidak valid.")
        pause()
