import streamlit as st
from config.app_config import PRIMARY_COLOR, SECONDARY_COLOR
import requests
import time

def get_github_stars():
    try:
        response = requests.get("https://api.github.com/repos/ZeroxxG/HIA")
        if response.status_code == 200:
            return response.json()["stargazers_count"]
        return None
    except:
        return None

def show_footer(in_sidebar=False):
    # Cache the stars count for 1 hour
    @st.cache_data(ttl=3600)
    def get_cached_stars():
        return get_github_stars()
    
    stars_count = get_cached_stars()
    
    base_styles = f"""
        text-align: center;
        padding: 0.75rem;
        background: linear-gradient(to right, 
            rgba(25, 118, 210, 0.03), 
            rgba(100, 181, 246, 0.05), 
            rgba(25, 118, 210, 0.03)
        );
        border-top: 1px solid rgba(100, 181, 246, 0.15);
        margin-top: {'0' if in_sidebar else '2rem'};
        {'width: 100%' if not in_sidebar else ''};
        box-shadow: 0 -2px 10px rgba(100, 181, 246, 0.05);
    """
    
    st.markdown(
        f"""
        <div style='{base_styles}'>
            <p style='
                font-family: "Source Sans Pro", sans-serif;
                color: #64B5F6;
                font-size: 0.75rem;
                letter-spacing: 0.02em;
                margin: 0;
                opacity: 0.95;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                gap: 8px;
            '>
                <span style="
                    display: flex;
                    align-items: center;
                    gap: 4px;
                    padding: 2px 8px;
                    border-radius: 4px;
                    background: rgba(100, 181, 246, 0.05);
                    transition: all 0.2s ease;
                ">
                </span>
                <span style="
                    color: #1976D2;
                    display: flex;
                    align-items: center;
                    gap: 4px;
                    transition: all 0.2s ease;
                ">
                </span>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
