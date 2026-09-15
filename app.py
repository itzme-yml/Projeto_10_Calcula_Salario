import streamlit as st


def calcular_salario(valor_hora: float, horas_trabalhadas: float) -> float:
    "Calcula o salário mensal a partir do valor da hora e das horas trabalhadas."
    if valor_hora < 0:
        raise ValueError("O valor da hora não pode ser negativo.")

    if horas_trabalhadas < 0:
        raise ValueError("A quantidade de horas trabalhadas não pode ser negativa.")

    max_horas_mensais = 744
    if horas_trabalhadas > max_horas_mensais:
        raise ValueError("A quantidade de horas trabalhadas está fora do limite mensal razoável.")

    return valor_hora * horas_trabalhadas


def main() -> None:
    st.set_page_config(
        page_title="Calculadora de Salário Mensal",
        layout="centered",
    )

    st.title("Calculadora de Salário Mensal")
    st.caption("Informe o valor da hora e o número de horas trabalhadas para calcular o salário do mês.")

    valor_hora = st.number_input(
        "Quanto você ganha por hora?",
        min_value=0.0,
        step=0.01,
        format="%.2f",
        help="Use valores como 25.50",
    )

    horas_trabalhadas = st.number_input(
        "Quantas horas você trabalhou no mês?",
        min_value=0.0,
        step=1.0,
        format="%.0f",
        help="Exemplo: 160 horas",
    )

    if st.button("Calcular salário", type="primary"):
        try:
            salario = calcular_salario(valor_hora, horas_trabalhadas)
            st.success(f"Seu salário do mês é: R$ {salario:,.2f}")
            st.metric("Salário total", f"R$ {salario:,.2f}")
        except ValueError as erro:
            st.error(f"Erro: {erro}")

    st.markdown("---")
    st.subheader("Exemplo")
    st.write("Se você ganha R$ 25,50 por hora e trabalha 160 horas, o salário será: R$ 4.080,00.")


if __name__ == "__main__":
    main()
