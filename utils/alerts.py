import time
import streamlit as st
import platform

ALERT_COOLDOWN = 3  # seconds


def should_alert():
    """Cooldown-based alert control."""
    now = time.time()

    if "last_alert_time" not in st.session_state:
        st.session_state.last_alert_time = 0

    if now - st.session_state.last_alert_time > ALERT_COOLDOWN:
        st.session_state.last_alert_time = now
        return True

    return False


def play_alert_sound():
    """Cross-platform alert sound."""
    if platform.system() == "Windows":
        try:
            import winsound
            winsound.PlaySound(
                "assets/alert.wav",
                winsound.SND_FILENAME | winsound.SND_ASYNC
            )
        except Exception:
            pass
