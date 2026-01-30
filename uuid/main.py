# Importamos a classe do pacote Core
from Core.identifier import GenerateUUID

def testar_componente():
    print("--- Test Core Component ---")

    # 1. Teste do ID Aleatório
    random_id = GenerateUUID.v4()
    print(f"New ID de session: {random_id}")

    # 2. Teste do ID hex
    rando_id_hex = GenerateUUID.hex()
    print(f"New ID de session: {rando_id_hex }")

    # 3. Teste do ID Determinístico (v5)
    email = "user@exemplo.com"
    id_1 = GenerateUUID.v5(email)
    id_2 = GenerateUUID.v5(email)

    print(f"ID user (1): {id_1}")
    print(f"ID user (2): {id_2}")

    if id_1 == id_2:
        print("✅ Success: Consistence consistent!")
    else:
        print("❌ Erro: Os IDs não coincidem.")

if __name__ == "__main__":
    testar_componente()