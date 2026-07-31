import streamlit as st


def show_dashboard():

    st.title("🎓 Pocket Professor AI")

    st.subheader(
        "Offline Educational and Research Assistant"
    )

    st.markdown(
        """
**Developer:** Francis Akponome

**Competition:** Africa Deep Tech Challenge (ADTC) 2026

**Version:** 1.0
        """
    )

    st.markdown("---")

    # OFFLINE AI STATUS

    st.subheader("🧠 Offline AI Status")

    col1, col2 = st.columns(2)

    with col1:

        st.success(
            "🟢 AI Model Loaded"
        )

        st.info(
            """
Model:
llama3.2:3b

Deployment:
Local Ollama
            """
        )

    with col2:

        st.success(
            "🟢 Offline Mode Active"
        )

        st.info(
            """
Internet:
Not Required

Cloud Services:
None
            """
        )

    st.markdown("---")

    # SYSTEM REQUIREMENTS

    st.subheader("💻 System Requirements")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "RAM Target",
            "8 GB"
        )

    with col2:

        st.metric(
            "GPU",
            "Not Required"
        )

    with col3:

        st.metric(
            "AI Engine",
            "Ollama"
        )

    st.markdown("---")

    # SYSTEM STATUS

    st.subheader("🖥️ System Status")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.success(
            "🟢 AI Tutor Ready"
        )

    with col2:

        st.success(
            "🟢 PDF Assistant Ready"
        )

    with col3:

        st.success(
            "🟢 Research Tools Ready"
        )

    st.markdown("---")

    # FEATURES

    st.subheader("🚀 Available Features")

    col1, col2 = st.columns(2)

    with col1:

        st.info(
            """
🤖 AI Tutor

Ask questions and receive intelligent explanations.
            """
        )

        st.info(
            """
📄 PDF Assistant

Upload PDFs and ask questions from documents.
            """
        )

        st.info(
            """
📝 Notes Generator

Generate organized study notes automatically.
            """
        )

        st.info(
            """
💡 Research Ideas Generator

Discover innovative research topics.
            """
        )

        st.info(
            """
📚 Citation Generator

Generate APA, MLA, Harvard, and Chicago citations.
            """
        )

    with col2:

        st.info(
            """
📖 Literature Review Assistant

Generate structured literature reviews.
            """
        )

        st.info(
            """
🔍 Research Gap Finder

Identify gaps and future research opportunities.
            """
        )

        st.info(
            """
✍️ Academic Writing Assistant

Generate academic writing sections.
            """
        )

        st.info(
            """
📚 Research Project Generator

Generate abstracts, chapters, references, and appendices.
            """
        )

    st.markdown("---")

    # ADTC COMPLIANCE

    st.subheader("🌍 ADTC Compliance")

    st.success(
        """
✅ Fully Offline AI

✅ No Cloud Dependency

✅ No Internet Required

✅ No GPU Required

✅ Optimized for 8 GB RAM Laptops

✅ Built for African Learners and Researchers
        """
    )

    st.markdown("---")

    # PROJECT IMPACT

    st.subheader("🎯 Impact")

    st.info(
        """
Pocket Professor AI empowers students,
researchers, innovators, and founders with
offline artificial intelligence tools for learning,
research, academic writing, and project development.

The platform is designed specifically for
low-connectivity environments where access to
cloud-based AI systems may be limited.
        """
    )

    st.markdown("---")

    st.subheader("👨‍💻 Developer")

    st.info(
        """
Francis Akponome

Pocket Professor AI Developer

Africa Deep Tech Challenge (ADTC) 2026
        """
    )