import streamlit as st
from graphs import network_map
import streamlit.components.v1 as components


st.title(
    "Network Maps Showing the International Collaboration in Sickle Cell Retinopathy and Diabetic Retinopathy Research"
)

st.info(
    "Just a moment! Our maps are rich with complex data and might take a little longer to load than other content. We appreciate your patience as we bring the insights to life."
)

tab1, tab2 = st.tabs(
    [
        "Collaboration Network Map On SCR Research",
        "Collaboration Network Map on DR Research",
    ]
)

with tab1:
    st.header(
        "Which countries collaborate the most on sickle cell retinopathy Research"
    )

    components.html(network_map("maps/colabs_network.html"), height=800, width=800)

    st.markdown(
        """
                Researchers in the USA were on the highest number of collaborative publications.
                """
    )

with tab2:
    st.header("Which countries collaborate the most on Diabetic retinopathy Research")

    components.html(network_map("maps/dbr_colabs_network.html"), height=800, width=800)

    st.markdown(
        """
                Researchers in the USA were on the highest number of collaborative publications.
                """
    )

st.divider()

with st.container():
    st.markdown(
        """
    Built with ❤️ by [Mohammed-Sherrif Fuseini][1].   
    Member of the [Sickle Cell Retinopathy Network][4].  
    Connect with me: [LinkedIn][2] | [Email][3].   

    [1]: https://sites.google.com/view/msfuseini
    [2]: https://www.linkedin.com/in/msfuseini/
    [3]: mailto:msherrif04@gmail.com
    [4]: https://www.sicklecellretinopathy.net/
    """
    )
