import json  #the timetable file is stored in json file format
import time
import datetime
import os


timetablefile = "timetable.json"
checkinterval = 10    # to refresh the program and check in every 10 seconds

def loadtimetable():
    if not os.path.exists(timetablefile):
        return []
    try:
        with open(timetablefile, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
    except:
        pass
    return []

def hhmm_to_time(hhmm):
    if not isinstance(hhmm, str):
        return None
    try:
        h, m = hhmm.strip().split(":")
        h = int(h)
        m = int(m)
        if 0 <= h < 24 and 0 <= m < 60:
            return datetime.time(h, m)
    except:
        pass
    return None

def notify(title):
    print("\n" + "=" * 40)
    print(" REMINDER:", title)
    print("=" * 40 + "\n")
    print("\a")     #for the bell sound 
    print(end="", flush=True)

def main():
    print("Timetable Notifier started.")
    notifiedtoday = set()
    lastdate = datetime.date.today()

    try:
        while True:
            now = datetime.datetime.now()
            today = now.date()

            if today != lastdate:
                notifiedtoday.clear()
                lastdate = today

            currenttime = now.time().replace(second=0, microsecond=0)
            timetable = loadtimetable()

            for entry in timetable:
                t_str = entry.get("time")
                title = entry.get("title")
                if not t_str or not title:
                    continue

                t_obj = hhmm_to_time(t_str)
                if t_obj is None:
                    continue

                key = f"{today.isoformat()}|{t_str}|{title}"

                if currenttime.hour == t_obj.hour and currenttime.minute == t_obj.minute and key not in notifiedtoday:
                    notify(title)
                    notifiedtoday.add(key)

            time.sleep(checkinterval)
    except KeyboardInterrupt:
        print("\nNotifier stopped.")

if __name__ == "__main__":
    main()



