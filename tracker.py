import pandas as pd
import os

class WorkoutTracker:
    def __init__(self, data_file='data/workout_data.csv'):
        self.data_file = data_file
        self.workout_days = {
            "Leg Day": {
                "Leg Press": {"sets": 4, "reps": 12, "weight": None},
                "Dumbbell Squat": {"sets": 4, "reps": 12, "weight": None},
                "Leg Extension": {"sets": 4, "reps": 12, "weight": None},
                "Lying Leg Curl": {"sets": 4, "reps": 12, "weight": None},
                "Barbarian Split Squat": {"sets": 3, "reps": 10, "weight": None},
            },
            "Shoulder Day": {
                "Dumbbell Side Laterals": {"sets": 4, "reps": 12, "weight": None},
                "Cable Side Laterals": {"sets": 4, "reps": 12, "weight": None},
                "Dumbbell Front Raise": {"sets": 4, "reps": 12, "weight": None},
                "Rear Peck Deck Machine": {"sets": 4, "reps": 12, "weight": None},
            },
            "Back Day": {
                "Lat Pulldown": {"sets": 4, "reps": 12, "weight": None},
                "Seated Cable Row": {"sets": 4, "reps": 12, "weight": None},
                "Single-Arm Dumbbell Row": {"sets": 4, "reps": 12, "weight": None},
                "Bent-Over Barbell Row": {"sets": 4, "reps": 10, "weight": None},
                "Face Pull": {"sets": 4, "reps": 15, "weight": None},
                "Reverse Grip Lat Pulldown": {"sets": 4, "reps": 12, "weight": None},
            },
            "Bicep_Tricep Day": {
                "Incline Dumbbell Curls": {"sets": 4, "reps": 12, "weight": None},
                "Preacher Curls": {"sets": 4, "reps": 12, "weight": None},
                "Skull Crushers": {"sets": 4, "reps": 12, "weight": None},
                "Tricep Rope Pull Down": {"sets": 4, "reps": 12, "weight": None},
                "Overhead Tricep Dumbbell Raise": {"sets": 4, "reps": 12, "weight": None},
            },
            "Glute Day": {
                "Glute Bridge": {"sets": 4, "reps": 12, "weight": None},
                "Francielle Cable Back": {"sets": 3, "reps": 15, "weight": None},
                "B-Stance RDL": {"sets": 3, "reps": 10, "weight": None},
                "Stiff Leg Deadlift": {"sets": 3, "reps": 10, "weight": None},
            }
        }
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            return pd.read_csv(self.data_file)
        else:
            columns = ['date', 'workout_day', 'exercise', 'sets', 'reps', 'weight']
            return pd.DataFrame(columns=columns)

    def save_data(self):
        self.data.to_csv(self.data_file, index=False)

    def record_session(self, workout_day, exercise, sets, reps, weight):
        new_entry = pd.DataFrame({
            'date': [pd.Timestamp.today().strftime('%Y-%m-%d')],
            'workout_day': [workout_day],
            'exercise': [exercise],
            'sets': [sets],
            'reps': [reps],
            'weight': [weight]
        })

        self.data = pd.concat([self.data, new_entry], ignore_index=True)
        self.save_data()

    def recommend_weight(self, workout_day, exercise):
        if self.data.empty:
            return 5  # Starting weight

        last_sessions = self.data[(self.data['workout_day'] == workout_day) &
                                  (self.data['exercise'] == exercise)]
        if not last_sessions.empty:
            last_weight = last_sessions.iloc[-1]['weight']
            return last_weight + 2.5  # Increase by 2.5 kg for progressive overload
        else:
            return 5  # Starting weight

    def get_progress(self, workout_day, exercise):
        return self.data[(self.data['workout_day'] == workout_day) &
                        (self.data['exercise'] == exercise)]

    def print_options(self):
        print("\nAvailable Workout Days:")
        for day in self.workout_days.keys():
            print(f"- {day}")

        print("\nExercises for each day:")
        for day, exercises in self.workout_days.items():
            print(f"\n{day}:")
            for exercise in exercises.keys():
                print(f"  - {exercise}")