import pandas as pd

from app.schemas.invoice import InvoiceCreate

RESUME_INDEX = 4

DATE_INDEX = 2
ACESS_KEY_INDEX = 5
AUTH_PROTOCOLE_INDEX = 6
CONSUMER = 8

KEYS_INDEX = 0


def get_invoice_details(iframe_content, iframe_url) -> InvoiceCreate:
    resume = get_resume(iframe_content)
    details = get_details(iframe_content, iframe_url)


def get_resume(iframe_content) -> dict:
    content = iframe_content.findAll("table", "NFCCabecalho")[RESUME_INDEX]

    # Get first tables
    resume_df = pd.read_html(str(content))[0]
    resume_dict = resume_df.to_dict("records")

    amount = int(resume_dict[0][1])
    discount = int(resume_dict[1][1])

    return {"amount": amount, "discount": discount}


def get_details(iframe_content, iframe_url) -> dict:
    content = iframe_content.findAll("td", "NFCCabecalho_SubTitulo")
    date = content[DATE_INDEX].text.split("\n")

    del date[KEYS_INDEX]

    def invoice_date_treatment(word: str) -> str:
        index = word.index(":")
        return word[slice(index + 1, len(word))].strip()

    date = map(invoice_date_treatment, date)
    date = list(date)

    nfce_number = date[0]
    series = date[1]
    date_time = date[2]

    acess_key = content[ACESS_KEY_INDEX].text
    acess_key = "".join(acess_key.split(" "))

    auth_protocole = content[AUTH_PROTOCOLE_INDEX].text.split(":")
    auth_protocole = auth_protocole[1].strip()

    consumer = content[CONSUMER].text.strip()

    return {
        "nfce_number": nfce_number,
        "series": series,
        "date_time": date_time,
        "acess_key": acess_key,
        "auth_protocole": auth_protocole,
        "consumer": consumer,
        "url": iframe_url,
    }
