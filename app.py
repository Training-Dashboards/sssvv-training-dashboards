
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
from io import BytesIO

st.set_page_config(
    page_title="SSSVV | Training Analytical Dashboards",
    page_icon="📊",
    layout="wide"
)
DEFAULT_FILE = Path(__file__).parent / "SSSVV_SET_Analytics_Summary_FINAL.xlsx"
USERS = {
    "madhu": {
        "password": "admin123",
        "role": "admin"
    },
    "chandra": {
        "password": "admin123",
        "role": "admin"
    },
    "admin3": {
        "password": "admin123",
        "role": "admin"
    },
    "member1": {
        "password": "member123",
        "role": "member"
    },
    "viewer1": {
        "password": "view123",
        "role": "viewer"
    }
}
# =====================================
# LOGIN SYSTEM
# =====================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "role" not in st.session_state:
    st.session_state.role = None

if not st.session_state.logged_in:

    st.title("🔐 SSSVV Dashboard Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username in USERS and USERS[username]["password"] == password:

            st.session_state.logged_in = True
            st.session_state.role = USERS[username]["role"]
            st.session_state.username = username

            st.success("Login successful")
            st.rerun()

        else:
            st.error("Invalid username or password")

    st.stop()
@st.cache_data
def load_data(file_bytes):
    xls = pd.ExcelFile(BytesIO(file_bytes))
    overall = pd.read_excel(xls, sheet_name="Overall SET Summary", header=2)
    states = pd.read_excel(xls, sheet_name="State-wise Analysis", header=2)
    schools = pd.read_excel(xls, sheet_name="School-wise Analysis", header=2)
    return overall, states, schools
# =====================================
# USER INFO & LOGOUT
# =====================================

with st.sidebar:
    st.markdown("---")

    st.info(f"👤 User: {st.session_state.username}")
    st.success(f"🔑 Role: {st.session_state.role.title()}")

    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.session_state.role = None
        st.session_state.username = None
        st.rerun()
# Header Section

logo_col, title_col = st.columns([1, 5])

with logo_col:
    st.image("swamy.jpg", width=120)

with title_col:

    st.markdown(
        "<h1 style='color:#0B3D91;margin-bottom:0px;'>Sri Sathya Sai Vidya Vahini</h1>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<h3 style='color:#E67E22;margin-top:0px;'>Training Analytical Dashboards</h3>",
        unsafe_allow_html=True,
    )   
page = st.radio(
    "Navigate",
    [
        "🏠 Home",
        "📖 TATVAM",
        "📊 SET",
        "📚 CPD",
        "🎓 CTP",
        "🏫 SCHOOL",
        "💻 LMS",
        "🏫 LHS",
        "🌍 T2",
        "📅 YEAR-WISE",
        "🎯 COURSES",
        "📈 REPORTS",
        "🏆 CERTIFICATION"
    ],
    horizontal=True
)
if page == "🏠 Home":

    st.markdown("## 🌹 Welcome to SSSVV Training Analytical Dashboards")

    # Row 1
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.info("📖 TATVAM\n🚧 Coming Soon")

    with col2:
        st.info("📊 SET\n✅ Live Dashboard")

    with col3:
        st.info("📚 CPD\n🚧 Coming Soon")

    with col4:
        st.info("🎓 CTP\n🚧 Coming Soon")

    # Row 2
    col5, col6, col7, col8 = st.columns(4)

    with col5:
        st.info("🏫 SCHOOL\n🚧 Coming Soon")

    with col6:
        st.info("💻 LMS\n🚧 Coming Soon")

    with col7:
        st.info("🏫 LHS\n🚧 Coming Soon")

    with col8:
        st.info("🌍 T2\n🚧 Coming Soon")

    # Row 3
    col9, col10, col11, col12 = st.columns(4)

    with col9:
        st.info("📅 YEAR-WISE\n🚧 Coming Soon")

    with col10:
        st.info("🎯 COURSES\n🚧 Coming Soon")

    with col11:
        st.info("📈 REPORTS\n🚧 Coming Soon")

    with col12:
        st.info("🏆 CERTIFICATION\n🚧 Coming Soon")

    st.stop()
if page == "📖 TATVAM":
    st.title("TALK - ANALYSE - TRAIN - VALIDATE - AFFIRM - MENTOR")
    st.caption("TATVAM")
    st.info("Dashboard Coming Soon")
    st.stop()

if page == "📚 CPD":
    st.title("Continuous Professional Development (CPD)")
    st.info("Dashboard Coming Soon")
    st.stop()

if page == "🎓 CTP":
    st.title("Chapter Teaching Plan (CTP)")
    st.info("Dashboard Coming Soon")
    st.stop()

if page == "🏫 SCHOOL":
    st.title("School Analytics")
    st.info("Dashboard Coming Soon")
    st.stop()

if page == "💻 LMS":
    st.title("Learning Management System (LMS)")
    st.info("Dashboard Coming Soon")
    st.stop()

if page == "🏫 LHS":
    st.title("Light House School (LHS)")
    st.info("Dashboard Coming Soon")
    st.stop()

if page == "🌍 T2":
    st.title("State Training (T2)")
    st.info("Dashboard Coming Soon")
    st.stop()

if page == "📅 YEAR-WISE":
    st.title("Year-wise Analytics")
    st.info("Dashboard Coming Soon")
    st.stop()

if page == "🎯 COURSES":
    st.title("Training Courses")
    st.info("Dashboard Coming Soon")
    st.stop()

if page == "📈 REPORTS":
    st.title("Reports")
    st.info("Dashboard Coming Soon")
    st.stop()

if page == "🏆 CERTIFICATION":
    st.title("Certification Analytics")
    st.info("Dashboard Coming Soon")
    st.stop()
if page != "📊 SET":
    st.stop()
with st.sidebar:
    st.header("Dashboard controls")
    uploaded = st.file_uploader("Upload an updated SET summary workbook", type=["xlsx"])
    st.caption("If you do not upload a new file, the included workbook will be used.")

if uploaded is not None:
    file_bytes = uploaded.getvalue()
elif DEFAULT_FILE.exists():
    file_bytes = DEFAULT_FILE.read_bytes()
else:
    st.error("The Excel workbook is missing. Place SSSVV_SET_Analytics_Summary_FINAL.xlsx beside app.py.")
    st.stop()

try:
    overall, states, schools = load_data(file_bytes)
except Exception as e:
    st.error(f"Could not read the workbook: {e}")
    st.stop()

# Clean up rows and numeric values
overall = overall.dropna(subset=["Session Number"]).copy()
overall["Teacher Attendance"] = pd.to_numeric(overall["Teacher Attendance"], errors="coerce").fillna(0)
overall["No. of Participants"] = pd.to_numeric(overall["No. of Participants"], errors="coerce").fillna(0)
overall["No. of Responses"] = pd.to_numeric(overall["No. of Responses"], errors="coerce").fillna(0)

states = states[states["State"].notna()].copy()
states = states[~states["State"].astype(str).str.contains("GRAND TOTAL|Check against", case=False, regex=True)]
for c in [f"SET-{i}" for i in range(1, 11)] + ["Total attendance"]:
    if c in states.columns:
        states[c] = pd.to_numeric(states[c], errors="coerce").fillna(0)

schools = schools[schools["School Name"].notna()].copy()
schools = schools[~schools["School Name"].astype(str).str.contains("TOTAL|Others", case=False, regex=True)]
schools["Total attendance"] = pd.to_numeric(schools["Total attendance"], errors="coerce").fillna(0)
schools["School ID"] = schools["School ID"].fillna("ID pending").astype(str)
for c in [f"SET-{i}" for i in range(1, 11)]:
    if c in schools.columns:
        schools[c] = pd.to_numeric(schools[c], errors="coerce").fillna(0)

with st.sidebar:
    all_states = sorted(states["State"].dropna().astype(str).unique().tolist())
    chosen_states = st.multiselect("Select state(s)", all_states, default=all_states)
    session_options = [
    col for col in states.columns
    if str(col).startswith("SET-")
]
    chosen_sessions = st.multiselect("Select session(s)", session_options, default=session_options)

state_filtered = states[states["State"].astype(str).isin(chosen_states)].copy()
school_filtered = schools[schools["State"].astype(str).isin(chosen_states)].copy()
# Count how many sessions each school attended

session_cols = [
    col for col in school_filtered.columns
    if str(col).startswith("SET-")
]
school_filtered["Sessions Attended"] = (
    school_filtered[session_cols] > 0
).sum(axis=1)
# Consistency Champions

max_sessions = school_filtered["Sessions Attended"].max()

state_champions = school_filtered[
    school_filtered["Sessions Attended"] == max_sessions
][
    ["State", "School Name", "Sessions Attended"]
]


if not chosen_sessions:
    st.warning("Select at least one SET session in the sidebar to display attendance charts.")
    st.stop()
# Build session attendance using selected states
session_data = []

for session in chosen_sessions:
    if session in state_filtered.columns:

        attendance = state_filtered[session].sum()

        match = overall[
            overall["Session Number"].astype(str) == session
        ]

        session_data.append({
            "Session Number": session,
            "Teacher Attendance": attendance,
            "Date": match["Date"].iloc[0] if not match.empty else "",
            "Topic": match["Topic"].iloc[0] if not match.empty else "",
            "Presenter": match["Presenter"].iloc[0] if not match.empty else "",
        })

session_filtered = pd.DataFrame(session_data)

total_attendance = int(session_filtered["Teacher Attendance"].sum())
total_sessions = len(session_filtered)
if len(chosen_sessions) == 1:

    selected_session = chosen_sessions[0]

    participating_schools = school_filtered[
        school_filtered[selected_session] > 0
    ]["School Name"].nunique()

    participating_states = school_filtered[
        school_filtered[selected_session] > 0
    ]["State"].nunique()

if len(chosen_sessions) == 1:

    total_schools = participating_schools
    total_states = participating_states

else:

    total_schools = int(school_filtered["School Name"].nunique())
    total_states = int(state_filtered["State"].nunique())
# Consistency Champion

champion = school_filtered.loc[
    school_filtered["Sessions Attended"].idxmax()
]

champion_school = champion["School Name"]
champion_state = champion["State"]
champion_sessions = champion["Sessions Attended"]
m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown(
        f"""
        <div style="background-color:#FFF3E0;
                    padding:8px;
                    border-radius:8px;
                    text-align:center;
                    border-left:4px solid #E67E22;">
            <h5>📊 Teacher Attendance</h5>
            <h3>{total_attendance:,}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

with m2:

    if len(chosen_sessions) == 1:

        display_value = chosen_sessions[0]
        display_title = "📚 Session"

    else:

        display_value = total_sessions
        display_title = "📚 SET Sessions"

    st.markdown(
        f"""
        <div style="background-color:#EAF4FF;
                    padding:8px;
                    border-radius:8px;
                    text-align:center;
                    border-left:4px solid #3498DB;">
            <h5>{display_title}</h5>
            <h3>{display_value}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )
with m3:
    st.markdown(
        f"""
        <div style="background-color:#EAFBF1;
                    padding:8px;
                    border-radius:8px;
                    text-align:center;
                    border-left:4px solid #27AE60;">
            <h5>🏫 Schools</h5>
            <h3>{total_schools}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

with m4:
    st.markdown(
        f"""
        <div style="background-color:#F5ECFA;
                    padding:8px;
                    border-radius:8px;
                    text-align:center;
                    border-left:4px solid #8E44AD;">
            <h5>🌍 States</h5>
            <h3>{total_states}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )
if len(chosen_sessions) == 1:

    selected = session_filtered.iloc[0]

    st.markdown("### 📘 Session Details")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.info(f"📅 Date\n\n{selected['Date']}")

    with c2:
        st.info(f"📖 Topic\n\n{selected['Topic']}")

    with c3:
        st.info(f"🎤 Presenter\n\n{selected['Presenter']}")

    with c4:
        st.info(f"👥 Attendance\n\n{int(selected['Teacher Attendance'])}")

st.write("")
st.markdown("### 🌟 State Participation Insights")
# Best school from each state
state_insights = (
    school_filtered
    .sort_values("Sessions Attended", ascending=False)
    .groupby("State", as_index=False)
    .first()
)

total_sessions_available = len(session_cols)

def get_recognition(attended, total_sessions):

    if attended == total_sessions:
        return "🏆 Outstanding Commitment"

    elif attended >= total_sessions * 0.80:
        return "🌟 Highly Consistent"

    elif attended >= total_sessions * 0.50:
        return "👍 Good Engagement"

    elif attended >= total_sessions * 0.30:
        return "📘 Growing Participation"

    else:
        return "🤝 Support & Encouragement Needed"
state_insights["Participation Consistency"] = (
    state_insights["Sessions Attended"].astype(str)
    + "/"
    + str(total_sessions_available)
)

state_insights["Recognition"] = state_insights["Sessions Attended"].apply(
    lambda x: get_recognition(x, total_sessions_available)
)

state_insights = state_insights.sort_values(
    "Sessions Attended",
    ascending=False
)

st.dataframe(
    state_insights[
        ["State", "Participation Consistency", "Recognition"]
    ],
    use_container_width=True,
    hide_index=True
)


st.divider()

left, right = st.columns(2)

with left:
    st.markdown("### Teacher attendance by SET session")
    fig = px.bar(
    session_filtered,
    x="Session Number",
    y="Teacher Attendance",
    text="Teacher Attendance",
    labels={
        "Session Number": "SET session",
        "Teacher Attendance": "Teacher attendance"
    },
)
    fig.update_traces(textposition="outside")
    fig.update_layout(showlegend=False, margin=dict(l=10, r=10, t=20, b=10), yaxis_title="Teachers")
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.markdown("### Teacher attendance by state")
    state_session_cols = [s for s in chosen_sessions if s in state_filtered.columns]
    state_plot = state_filtered[["State"] + state_session_cols].copy()
    state_plot["Selected session attendance"] = state_plot[state_session_cols].sum(axis=1)
if len(chosen_sessions) == 1:
    state_plot = state_plot[
        state_plot["Selected session attendance"] > 0
    ]
    state_plot = state_plot.sort_values("Selected session attendance", ascending=True)
    fig_state = px.bar(
        state_plot,
        x="Selected session attendance",
        y="State",
        orientation="h",
        text="Selected session attendance",
        hover_data=state_session_cols,
        labels={"Selected session attendance": "Teacher attendance"},
    )
    fig_state.update_traces(textposition="outside")
    fig_state.update_layout(showlegend=False, margin=dict(l=10, r=25, t=20, b=10), yaxis_title="")
    st.plotly_chart(fig_state, use_container_width=True)

st.divider()
st.markdown("### School-wise teacher attendance")
st.caption("The chart shows School IDs only. Hover over a bar to see the school name and state. 'Others' is excluded because it is not an identified school.")
school_plot = school_filtered.copy()
school_plot["Selected session attendance"] = school_plot[chosen_sessions].sum(axis=1)
school_plot = school_plot.sort_values("Selected session attendance", ascending=False).head(20)
school_plot["School ID display"] = school_plot["School ID"].replace("ID pending", "ID pending")
fig_school = px.bar(
    school_plot.sort_values("Selected session attendance", ascending=True),
    x="Selected session attendance",
    y="School ID display",
    orientation="h",
    text="Selected session attendance",
    hover_data={"School Name": True, "State": True, "Selected session attendance": True, "School ID display": False},
    labels={"School ID display": "School ID", "Selected session attendance": "Teacher attendance"},
)
fig_school.update_traces(textposition="outside")
fig_school.update_layout(showlegend=False, height=max(520, 28 * len(school_plot)), margin=dict(l=10, r=35, t=20, b=10), yaxis_title="")
st.plotly_chart(fig_school, use_container_width=True)

with st.expander("School reference list (School ID – School Name)"):
    ref = school_filtered[["School ID", "School Name", "State"]].drop_duplicates().sort_values(["State", "School ID"])
    st.dataframe(ref, use_container_width=True, hide_index=True)

with st.expander("Session details"):
    detail_cols = ["Session Number", "Date", "Presenter", "Topic", "No. of Participants", "No. of Responses", "Teacher Attendance", "YouTube Recording Link"]
    detail = session_filtered[[c for c in detail_cols if c in session_filtered.columns]].copy()
    st.dataframe(detail, use_container_width=True, hide_index=True)

# Download the currently filtered tables
def excel_bytes(sheets):
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        for name, df in sheets.items():
            df.to_excel(writer, sheet_name=name[:31], index=False)
    return output.getvalue()

download_data = excel_bytes({
    "Session Summary": session_filtered,
    "State Analysis": state_filtered,
    "School Analysis": school_filtered,
})
if st.session_state.role in ["admin", "member"]:

    st.download_button(
        "Download filtered dashboard data (Excel)",
        data=download_data,
        file_name="SSSVV_SET_Dashboard_Filtered_Data.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
st.caption("Data source: the supplied SSSVV_SET_Analytics_Summary_FINAL.xlsx workbook. Verify any future workbook revision before publishing.")
