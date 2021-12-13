INFO_INDEX = 0
ADDRESS_INDEX = 1
CNPJ_INDEX = 1
INSCRICAO_ESTADUAL_INDEX = -1
INSCRICAO_ESTADUAL_NUMERO_INDEX = 1


def get_grocery_store_info(iframe_content) -> dict:
    content = iframe_content.findAll("table", "NFCCabecalho")

    info = content[INFO_INDEX]
    address_info = content[ADDRESS_INDEX]

    details = info.find("td", "NFCCabecalho_SubTitulo1").text.strip().split("\n")

    name = get_grocery_store_name(info)
    cnpj = get_grocery_store_cnpj(details)
    inscricao_estadual = get_grocery_store_inscricao_estadual(details)
    address = get_grocery_store_address(address_info)

    return {
        "name": name,
        "cnpj": cnpj,
        "inscricao_estadual": inscricao_estadual,
        "address": address,
    }


def get_grocery_store_address(address_info) -> str:
    address = address_info.find("td", "NFCCabecalho_SubTitulo1").text.split(
        "\n"
    )

    def strip_address(word: str) -> str:
        return word.strip()

    address = map(strip_address, address)
    address = " ".join(address)
    return address


def get_grocery_store_name(info) -> str:
    return info.find("td", "NFCCabecalho_SubTitulo").text


def get_grocery_store_cnpj(details) -> str:
    return details[CNPJ_INDEX].strip()


def get_grocery_store_inscricao_estadual(details) -> str:
    return (
        details[INSCRICAO_ESTADUAL_INDEX]
        .split(":")[INSCRICAO_ESTADUAL_NUMERO_INDEX]
        .strip()
    )
