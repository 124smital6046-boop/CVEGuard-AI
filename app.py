import streamlit as st
import requests
import pandas as pd
# ================= PAGE CONFIG =================

st.set_page_config(
    page_title="CVEGuard AI",
    page_icon="🛡️",
    layout="wide"
)

# ================= SIDEBAR =================

st.sidebar.title("🛡️ CVEGuard AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🔍 Search CVE",
        "📊 Dashboard",
        "📈 Analytics",
        "🤖 AI Predictor",
        "ℹ️ About"
    ]
)

# ================= HOME =================

if page == "🏠 Home":

    st.title("🛡️ CVEGuard AI")

    st.subheader(
        "AI-Powered Vulnerability Analytics Platform"
    )

    st.markdown(
        "### Predict • Prioritize • Protect"
    )

    st.write(
        """
        CVEGuard AI is designed to help security teams
        search, analyze and prioritize cybersecurity
        vulnerabilities.
        """
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("🔍 **CVE Search**\n\nSearch real CVE information.")

    with col2:
        st.info("📊 **Analytics**\n\nAnalyze vulnerability data.")

    with col3:
        st.info("🤖 **AI Prediction**\n\nPredict vulnerability severity.")


# ================= SEARCH CVE =================

elif page == "🔍 Search CVE":

    st.title("🔍 Search CVE")

    cve_id = st.text_input(
        "Enter CVE ID",
        placeholder="Example: CVE-2023-23397"
    )

    if st.button("🔎 Search CVE"):

        if not cve_id.strip():

            st.warning("Please enter a CVE ID.")

        else:

            cve_id = cve_id.strip().upper()

            if not cve_id.startswith("CVE-"):

                st.error("Please enter a valid CVE ID.")

            else:

                st.info("🔄 Searching NVD database...")

                url = "https://services.nvd.nist.gov/rest/json/cves/2.0"

                try:

                    response = requests.get(
                        url,
                        params={"cveId": cve_id},
                        timeout=20
                    )

                    if response.status_code == 200:

                        data = response.json()

                        vulnerabilities = data.get(
                            "vulnerabilities",
                            []
                        )

                        if vulnerabilities:

                            cve = vulnerabilities[0]["cve"]

                            st.success("✅ CVE Found!")

                            st.subheader(
                                cve.get("id", cve_id)
                            )

                            # Description
                            descriptions = cve.get(
                                "descriptions",
                                []
                            )

                            description = "Not available"

                            for item in descriptions:

                                if item.get("lang") == "en":

                                    description = item.get(
                                        "value",
                                        "Not available"
                                    )

                                    break

                            st.markdown("### 📄 Description")

                            st.write(description)

                            # CVSS
                            metrics = cve.get(
                                "metrics",
                                {}
                            )

                            score = "N/A"
                            severity = "N/A"

                            if "cvssMetricV31" in metrics:

                                cvss = metrics[
                                    "cvssMetricV31"
                                ][0]["cvssData"]

                                score = cvss.get(
                                    "baseScore",
                                    "N/A"
                                )

                                severity = cvss.get(
                                    "baseSeverity",
                                    "N/A"
                                )

                            elif "cvssMetricV30" in metrics:

                                cvss = metrics[
                                    "cvssMetricV30"
                                ][0]["cvssData"]

                                score = cvss.get(
                                    "baseScore",
                                    "N/A"
                                )

                                severity = cvss.get(
                                    "baseSeverity",
                                    "N/A"
                                )

                            col1, col2 = st.columns(2)

                            with col1:
                                st.metric(
                                    "CVSS Score",
                                    score
                                )

                            with col2:
                                st.metric(
                                    "Severity",
                                    severity
                                )

                            st.markdown(
                                "### 📅 Information"
                            )

                            st.write(
                                f"**Published:** "
                                f"{cve.get('published', 'N/A')}"
                            )

                            st.write(
                                f"**Last Modified:** "
                                f"{cve.get('lastModified', 'N/A')}"
                            )

                        else:

                            st.error(
                                f"❌ {cve_id} was not found."
                            )

                    else:

                        st.error(
                            f"NVD API Error: "
                            f"{response.status_code}"
                        )

                except requests.exceptions.RequestException as e:

                    st.error(
                        f"Connection error: {e}"
                    )


# ================= DASHBOARD =================

elif page == "📊 Dashboard":

    st.title("📊 Vulnerability Dashboard")

    st.write(
        "Overview of vulnerability severity and risk."
    )

    st.divider()

    # Dashboard metrics

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🔴 Critical",
            "235"
        )

    with col2:
        st.metric(
            "🟠 High",
            "820"
        )

    with col3:
        st.metric(
            "🟡 Medium",
            "2400"
        )

    with col4:
        st.metric(
            "🟢 Low",
            "5100"
        )

    st.divider()

    # Severity chart

    st.subheader(
        "📊 Vulnerability Severity Distribution"
    )

    severity_data = {
        "Severity": [
            "Critical",
            "High",
            "Medium",
            "Low"
        ],
        "Count": [
            235,
            820,
            2400,
            5100
        ]
    }

    st.bar_chart(
        severity_data,
        x="Severity",
        y="Count"
    )

    st.divider()

    st.subheader("⚡ Patch Priority")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.error(
            "🔴 Immediate\n\nCritical vulnerabilities"
        )

    with col2:
        st.warning(
            "🟠 High Priority\n\nHigh severity vulnerabilities"
        )

    with col3:
        st.info(
            "🟡 Normal Priority\n\nMedium severity vulnerabilities"
        )

 # ================= ANALYTICS =================

elif page == "📈 Analytics":

    st.title("📈 Vulnerability Analytics")

    st.subheader("Security Vulnerability Insights")

    st.divider()

    # Severity data
    severity_data = {
        "Critical": 235,
        "High": 820,
        "Medium": 2400,
        "Low": 5100
    }

    st.markdown("### 📊 Severity Distribution")

    for severity, count in severity_data.items():

        percentage = count / sum(severity_data.values()) * 100

        st.write(
            f"**{severity}:** {count} vulnerabilities "
            f"({percentage:.1f}%)"
        )

        st.progress(
            int(percentage)
        )

    st.divider()

    st.markdown("### 🔥 Risk Analysis")

    total = sum(severity_data.values())

    critical_high = (
        severity_data["Critical"]
        + severity_data["High"]
    )

    risk_percentage = (
        critical_high / total * 100
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Vulnerabilities",
            total
        )

    with col2:
        st.metric(
            "Critical + High",
            critical_high
        )

    with col3:
        st.metric(
            "High Risk %",
            f"{risk_percentage:.1f}%"
        )

    st.divider()

    st.info(
        "💡 Critical and High severity vulnerabilities "
        "should receive the highest patching priority."
    )

# ================= AI PREDICTOR =================

elif page == "🤖 AI Predictor":

    st.title("🤖 AI Severity & Patch Priority Predictor")

    st.subheader(
        "Predict vulnerability severity and determine patch priority using CVSS score."
    )

    st.divider()

    cvss_score = st.slider(
        "CVSS Score",
        min_value=0.0,
        max_value=10.0,
        value=5.0,
        step=0.1
    )

    if st.button("🤖 Predict Severity"):

        # ================= SEVERITY =================

        if cvss_score >= 9:
            severity = "Critical"

        elif cvss_score >= 7:
            severity = "High"

        elif cvss_score >= 4:
            severity = "Medium"

        else:
            severity = "Low"

        # ================= PATCH PRIORITY =================

        if cvss_score >= 9:
            priority = "Immediate"

        elif cvss_score >= 7:
            priority = "High"

        elif cvss_score >= 4:
            priority = "Medium"

        else:
            priority = "Low"

        # ================= RESULTS =================

        st.success("✅ Prediction Completed")

        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Predicted Severity",
                severity
            )

        with col2:
            st.metric(
                "⚡ Patch Priority",
                priority
            )

        st.divider()

        # ================= RECOMMENDATION =================

        if priority == "Immediate":

            st.error(
                "🚨 IMMEDIATE PATCH REQUIRED"
            )

            st.write(
                "This vulnerability has a very high CVSS score "
                "and should be patched immediately."
            )

        elif priority == "High":

            st.warning(
                "⚠️ HIGH PRIORITY PATCH"
            )

            st.write(
                "This vulnerability should be patched as soon as possible."
            )

        elif priority == "Medium":

            st.info(
                "🟡 MEDIUM PRIORITY PATCH"
            )

            st.write(
                "Schedule this vulnerability for patching."
            )

        else:

            st.success(
                "🟢 LOW PRIORITY"
            )

            st.write(
                "This vulnerability can be handled during routine patching."
            )
# ================= ABOUT =================

elif page == "ℹ️ About":

    st.title("ℹ️ About CVEGuard AI")

    st.subheader(
        "AI-Powered Vulnerability Analytics & Severity Prediction"
    )

    st.divider()

    st.markdown("### 🎯 Project Objective")

    st.write("""
    CVEGuard AI is designed to help security teams
    identify, analyze and prioritize software vulnerabilities.

    The system provides CVE information, vulnerability
    analytics, severity prediction and patch priority
    recommendations.
    """)

    st.markdown("### 🚀 Current Features")

    st.write("""
    ✅ Real-time CVE Search using NVD API

    ✅ CVSS Score and Severity Information

    ✅ Vulnerability Dashboard

    ✅ Severity Analytics

    ✅ CVSS-based Severity Prediction

    ✅ Patch Priority Recommendation
    """)

    st.markdown("### 🛠️ Technologies Used")

    st.write("""
    • Python

    • Streamlit

    • REST API

    • Pandas

    • Machine Learning

    • NVD Vulnerability Database
    """)

    st.markdown("### 🔮 Future Scope")

    st.write("""
    • Machine Learning-based severity prediction

    • Automatic exploit availability detection

    • Advanced Patch Priority Score

    • Vulnerability trend analysis

    • Security recommendations
    """)

    st.divider()

    st.success(
        "🛡️ CVEGuard AI — Predict • Prioritize • Protect"
    )