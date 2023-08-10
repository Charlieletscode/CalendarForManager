from streamlit_calendar import calendar
import streamlit as st

st.set_page_config(page_title="On Call Schedule Calendar", page_icon="📆", layout="wide")

mode = st.selectbox(
    "Calendar Mode:", ("daygrid", "timegrid","list",
                       "resource-daygrid", "resource-timegrid", "resource-timeline")
)

calendar_options = {}
calendar_events = [
    {"title": "Event 1", "color": "blue", "start": "2023-07-03", "end": "2023-07-05", "resourceId": "a"},
    {"title": "Event 2", "color": "orange", "start": "2023-07-01", "end": "2023-07-10", "resourceId": "b"},
    {"title": "Event 3", "color": "#FF4B4B", "start": "2023-07-20", "end": "2023-07-20", "resourceId": "c"},
    {"title": "Event 4", "color": "#FF6C6C", "start": "2023-07-23", "end": "2023-07-25", "resourceId": "d"},
    {"title": "Event 5", "color": "orange", "start": "2023-07-29", "end": "2023-07-30", "resourceId": "e"},
    {"title": "Event 6", "color": "#FF4B4B", "start": "2023-07-28", "end": "2023-07-20", "resourceId": "f"},
    {"title": "Event 7", "color": "#FF4B4B", "start": "2023-07-01T08:30:00",
     "end": "2023-07-01T10:30:00", "resourceId": "a"},
    {"title": "Event 8", "color": "#3D9DF3", "start": "2023-07-01T07:30:00",
     "end": "2023-07-01T10:30:00", "resourceId": "b"},
    {"title": "Event 9", "color": "#3DD56D", "start": "2023-07-02T10:40:00",
     "end": "2023-07-02T12:30:00", "resourceId": "c"},
    {"title": "Event 10", "color": "#FF4B4B", "start": "2023-07-15T08:30:00",
     "end": "2023-07-15T10:30:00", "resourceId": "d"},
    {"title": "Event 11", "color": "#3DD56D", "start": "2023-07-15T07:30:00",
     "end": "2023-07-15T10:30:00", "resourceId": "e"},
    {"title": "Event 12", "color": "#3D9DF3", "start": "2023-07-21T10:40:00",
     "end": "2023-07-21T12:30:00", "resourceId": "f"},
    {"title": "Event 13", "color": "#FF4B4B", "start": "2023-07-17T08:30:00",
     "end": "2023-07-17T10:30:00", "resourceId": "a"},
    {"title": "Event 14", "color": "#3D9DF3", "start": "2023-07-17T09:30:00",
     "end": "2023-07-17T11:30:00", "resourceId": "b"},
    {"title": "Event 15", "color": "#3DD56D", "start": "2023-07-17T10:30:00",
     "end": "2023-07-17T12:30:00", "resourceId": "c"},
    {"title": "Event 16", "color": "#FF6C6C", "start": "2023-07-17T13:30:00",
     "end": "2023-07-17T14:30:00", "resourceId": "d"},
    {"title": "Event 17", "color": "#FFBD45", "start": "2023-07-17T15:30:00",
     "end": "2023-07-17T16:30:00", "resourceId": "e"},
]
calendar_resources = [
    {'id': 'a', 'building': 'Building A', 'title': 'Room A'},
    {'id': 'b', 'building': 'Building A', 'title': 'Room B'},
    {'id': 'c', 'building': 'Building B', 'title': 'Room C'},
    {'id': 'd', 'building': 'Building B', 'title': 'Room D'},
    {'id': 'e', 'building': 'Building C', 'title': 'Room E'},
    {'id': 'f', 'building': 'Building C', 'title': 'Room F'},
]

if ("resource" in mode):
    if (mode == "resource-daygrid"):
        calendar_options = {
            'navLinks': 'true',
            'initialDate': '2023-07-01',
            "slotMinTime": "08:00:00",
            "slotMaxTime": "18:00:00",
            'initialView': 'resourceDayGridDay',
            'resourceGroupField': 'building',
            'resources': calendar_resources
        }
    elif (mode == "resource-timegrid"):
        calendar_options = {
            'headerToolbar': {
                'left': 'today',
                'center': 'title',
                'right': '',
            },
            'navLinks': 'true',
            'initialDate': '2023-07-01',
            "slotMinTime": "08:00:00",
            "slotMaxTime": "18:00:00",
            'initialView': 'resourceTimeGridDay',
            'resourceGroupField': 'building',
            'resources': calendar_resources
        }
else:
    if (mode == "daygrid"):
        calendar_options = {
            'headerToolbar': {
                'left': 'today',
                'center': 'title',
            },
            'navLinks': 'true',
            'initialDate': '2023-07-01',
            "slotMinTime": "08:00:00",
            "slotMaxTime": "18:00:00",
            'initialView': 'dayGridMonth',
        }
    elif (mode == "timegrid"):
        calendar_options = {
            'headerToolbar': {
                'left': 'today prev,next',
                'center': 'title',
                'right': 'timeGridDay,timeGridWeek'
            },
            # "weekends": False,
            'navLinks': 'true',
            "slotMinTime": "08:00:00",
            "slotMaxTime": "18:00:00",
            'initialView': 'timeGridWeek',
        }
    elif (mode == "list"):
        calendar_options = {
            'navLinks': 'true',
            'initialDate': '2023-07-01',
            "slotMinTime": "08:00:00",
            "slotMaxTime": "18:00:00",
            'initialView': 'listMonth'
        }


state = calendar(events=calendar_events, options=calendar_options, key=mode)

st.write(state)

st.markdown("## API reference")
st.help(calendar)
