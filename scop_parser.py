def load_scop_data(file_path="scop.txt"):
    scop_map = {}

    with open(file_path, "r") as f:
        for line in f:
            if line.startswith("#") or "CL=" not in line:
                continue

            parts = line.strip().split()

            try:
                pdb_id = parts[1].lower()
                chain_field = parts[2]
                chain = chain_field.split(":")[0].upper()

                class_info_str = [p for p in parts if p.startswith("TP=")][0]
                class_info = {}

                for item in class_info_str.split(","):
                    key, val = item.split("=")
                    if key in {"CL", "CF", "SF", "FA"}:
                        class_info[key] = int(val)

                key = (pdb_id, chain)
                scop_map.setdefault(key, []).append(class_info)

            except Exception as e:
                print(f"[GRESKA] Neispravna linija: {line.strip()}")
                continue
    return scop_map
