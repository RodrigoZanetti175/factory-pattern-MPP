import pandas as pd
import numpy as np
from xhtml2pdf import pisa

# FACTORY METHOD


class Saver:
    def save(self, data: pd.DataFrame, fw):
        pass


class PDFSaver(Saver):
    def save(self, df: pd.DataFrame, fw):
        print("salvando documento PDF")
        pisa.CreatePDF(str(df.to_html()), dest=fw)


class ExcelSaver(Saver):
    def save(self, df: pd.DataFrame, fw):
        print("salvando documento Excel")
        df.to_excel(fw)

        
class TextSaver(Saver):
    def save(self, df: pd.DataFrame, fw):
        print("salvando documento TXT")
        s = df.to_string()
        fw.write(s.encode())


class SaverFactory:
    def new(self, type: str) -> Saver:
        match type:
            case "pdf":
                return PDFSaver()
            case "excel":
                return ExcelSaver()
            case _:
                return TextSaver()


if __name__ == "__main__":
    columns = input("colunas: ").split()
    rows = []
    while True:
        _input = input("linha: ").split()
        if len(_input) == 0:
            break
        rows.append(_input)

    file_name = input("Qual o nome do arquivo? ")
    saver_type = input("Qual arquivo queres salvar? ")
    factory = SaverFactory()
    saver = factory.new(saver_type)

    df = pd.DataFrame(np.array(rows), columns=columns)

    with open(file_name, "w+b") as fw:
        saver.save(df, fw)
