import os
import json
from typing import List, Dict

class FamilyCodes:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self.codes: List[Dict] = []
            self.filepath = "hot_data/family_codes.json"

            if os.path.exists(self.filepath):
                self.load()
            else:
                self._save([])

            self._initialized = True

    def _save(self, data: List[Dict]):
        for c in data:
            c["is_enterprise"] = None
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def load(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            self.codes = json.load(f)
        for c in self.codes:
            c["is_enterprise"] = None

    def save(self):
        self._save(self.codes)

    def add(self, family_code: str, name: str = "") -> bool:
        if any(c["family_code"] == family_code for c in self.codes):
            print("Family code already exists.")
            return False
        self.codes.append({
            "family_code": family_code,
            "is_enterprise": None,
            "name": name,
        })
        self.save()
        print("Family code added.")
        return True

    def remove(self, family_code: str) -> bool:
        for i, c in enumerate(self.codes):
            if c["family_code"] == family_code:
                del self.codes[i]
                self.save()
                print("Family code removed.")
                return True
        print("Family code not found.")
        return False

    def list(self) -> List[Dict]:
        return [{"family_code": c["family_code"], "is_enterprise": None, "name": c.get("name", "")} for c in self.codes]

FamilyCodesInstance = FamilyCodes()
