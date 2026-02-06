import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import io

st.set_page_config(
    page_title="Axis MF Portfolio Analyzer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================
# DATA PROCESSING
# ============================


@st.cache_data
def process_portfolio_file(uploaded_file):
    try:
        xls = pd.ExcelFile(uploaded_file)
        all_data = []

        for sheet in xls.sheet_names:
            if sheet.lower() == "index":
                continue

            df = pd.read_excel(uploaded_file, sheet_name=sheet, header=3)

            if "Unnamed: 0" in df.columns:
                df.rename(columns={"Unnamed: 0": "instrument_code"}, inplace=True)

            df.dropna(how="all", inplace=True)

            if "Quantity" in df.columns:
                df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
            else:
                continue

            df = df[
                (df["instrument_code"].notna())
                & (df["Quantity"].notna())
                & (df["Quantity"] > 0)
            ].copy()

            if len(df) == 0:
                continue

            df["scheme_name"] = sheet
            df["amc_name"] = "Axis Mutual Fund"
            df["reporting_date"] = datetime(2025, 12, 31)

            all_data.append(df)

        final_df = pd.concat(all_data, ignore_index=True)

        # -------- COLUMN CLEAN --------
        final_df.columns = (
            final_df.columns.str.strip()
            .str.lower()
            .str.replace(" ", "_")
            .str.replace("/", "_")
            .str.replace("\n", "")
        )

        # ======== BUG FIX START ========
        if "market_fair_value_(rs._in_lakhs)" in final_df.columns:
            final_df["market_fair_value_(rs._in_lakhs)"] = pd.to_numeric(
                final_df["market_fair_value_(rs._in_lakhs)"], errors="coerce"
            )

        if "%_to_net_assets" in final_df.columns:
            final_df["%_to_net_assets"] = pd.to_numeric(
                final_df["%_to_net_assets"], errors="coerce"
            )
        # ======== BUG FIX END ========

        final_df["instrument_type"] = final_df.apply(classify_instrument, axis=1)

        return final_df

    except Exception as e:
        st.error(str(e))
        return None


def classify_instrument(row):
    name = str(row.get("name_of_the_instrument", "")).lower()
    rating = str(row.get("rating", "")).lower()

    if "aaa" in rating or "aa" in rating or "crisil" in rating:
        return "Debt"
    if "%" in name or "bond" in name or "government" in name:
        return "Debt"

    return "Other"


# ============================
# MAIN APP
# ============================


def main():
    st.title("📊 Axis MF Portfolio Analyzer")

    uploaded_file = st.file_uploader("Upload Portfolio Excel", type=["xlsx"])

    if uploaded_file:
        if st.button("Process Portfolio"):
            df = process_portfolio_file(uploaded_file)
            st.session_state["portfolio_data"] = df

    if "portfolio_data" in st.session_state:
        df = st.session_state["portfolio_data"]

        st.metric("Total Holdings", len(df))

        top_holdings = df.nlargest(10, "market_fair_value_(rs._in_lakhs)")

        fig = px.bar(
            top_holdings,
            x="market_fair_value_(rs._in_lakhs)",
            y="instrument_code",
            orientation="h",
        )
        st.plotly_chart(fig, use_container_width=True)

        fig2 = px.pie(df, names="instrument_type")
        st.plotly_chart(fig2, use_container_width=True)

        st.dataframe(df.head(50), use_container_width=True)

        csv = df.to_csv(index=False)
        st.download_button("Download CSV", csv, "portfolio.csv")

    else:
        st.info("Upload file to start.")


if __name__ == "__main__":
    main()
