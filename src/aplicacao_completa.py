import pandas as pd
import streamlit as st
from validador import Estatisticas
from pydantic import ValidationError

def validar_dados(df):
    erros = []
    dados_validados = []
    
    # Substitui NaN por None
    df = df.where(pd.notnull(df), None)
    
    for index, row in df.iterrows():
        try:
            # Converte a linha do DataFrame para dicionário
            dados = row.to_dict()
            
            # Valida os dados usando o modelo Estatisticas
            usuario_validado = Estatisticas(**dados)
            dados_validados.append(usuario_validado)
            
        except ValidationError as e:
            erros.append(f"Erro na linha {index + 2}: {str(e)}")
    
    return dados_validados, erros

def main():
    st.title("Validador de Dados de Campanhas")
    st.write("Upload do arquivo Excel para validação")
    
    uploaded_file = st.file_uploader("Escolha um arquivo Excel", type="xlsx")
    
    if uploaded_file is not None:
        try:
            # Lê o arquivo Excel
            df = pd.read_excel(uploaded_file, 'Sheet1')
            
            st.write("Preview dos dados:")
            st.dataframe(df.head())
            
            if st.button("Validar Dados"):
                with st.spinner("Validando dados..."):
                    dados_validados, erros = validar_dados(df)
                    
                    if erros:
                        st.error("Foram encontrados erros na validação:")
                        for erro in erros:
                            st.write(erro)
                    else:
                        st.success("Todos os dados foram validados com sucesso!")
                        
                        # Mostra quantidade de registros validados
                        st.write(f"Total de registros validados: {len(dados_validados)}")
                        
                        # Opção para download dos dados validados
                        df_validado = pd.DataFrame([dados.dict() for dados in dados_validados])
                        st.download_button(
                            label="Download dos dados validados",
                            data=df_validado.to_excel(index=False),
                            file_name="dados_validados.xlxs",
                            mime="text/excel"
                        )
                    
        except Exception as e:
            st.error(f"Erro ao processar o arquivo: {str(e)}")

if __name__ == "__main__":
    main()